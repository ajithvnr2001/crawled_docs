---
url: https://docs.copilotkit.ai/ms-agent-python/shared-state/streaming/
title: State Streaming
method: scrapling+scrapegraph
fetched_at: 2026-11-26T12:11:23.168595+00:00
---

# State Streaming

> Source: https://docs.copilotkit.ai/ms-agent-python/shared-state/streaming/

Shared state

# State Streaming

Stream partial agent state updates to the UI while a tool call is still running.

Copy MarkdownOpen

State Streaming

DemoCode

[](https://showcase-ms-agent-python-production.up.railway.app/demos/shared-state-streaming "Open in a new tab")[](https://github.com/CopilotKit/CopilotKit/tree/main/showcase/integrations/ms-agent-python/src/app/demos/shared-state-streaming "View the code on GitHub")

Waking up the demo

## What is this?Copy Anchor Link

By default, agent state only updates _between_ backend checkpoints, so a long-running tool call (writing a full document, drafting an email) appears to the UI as one big burst at the end. For agent-native apps, that feels broken: users expect to watch the output materialise.

**State streaming** copies one tool argument into an agent state key while the model writes the argument. The UI, subscribed via `useAgent`, re-renders every token.

## When should I use this?Copy Anchor Link

Use state streaming whenever a tool's output is long-form text or a growing structured value and you want the user to see it assemble in real time. Common shapes:

  * A collaborative writing agent that emits a document
  * A research agent that accumulates a list of findings
  * A planning agent that builds up a step-by-step plan



## The backend: one streaming state mappingCopy Anchor Link

### Map the tool argument with `predict_state_config`Copy Anchor Link

`predict_state_config` names the tool and the argument to stream into a state key. While the model generates the `write_document` call, the adapter sends each partial `document` argument to the UI as a state update. Returning `state_update(...)` from the tool commits the final value when the call completes:

src/agents/shared_state_streaming.py

Copy Text
    
    
    from typing import Annotated
    
    from agent_framework import tool
    from agent_framework_ag_ui import state_update
    from pydantic import Field
    
    # Stream tool-argument deltas straight into `state.document` while
    # `write_document` is still streaming.
    PREDICT_STATE_CONFIG: dict[str, dict[str, str]] = {
        "document": {
            "tool": "write_document",
            "tool_argument": "document",
        }
    }
    
    
    @tool(
        name="write_document",
        description=(
            "Write a document for the user. Always call this tool when the "
            "user asks you to write, draft, or revise any text. The "
            "`document` argument is streamed per-token into shared state "
            "under the `document` key so the UI renders the body live."
        ),
    )
    def write_document(
        document: Annotated[
            str,
            Field(description="The full document content as a single string."),
        ],
    ):
        return state_update(
            text="Document written to shared state.",
            state={"document": document},
        )

### Seed the state key before the deltas arriveCopy Anchor Link

The streamed updates are JSON Patch `replace` operations on `/document`. The agent's initial state is `{}`, and a `state_schema` defines properties but sets no starting values, so on the first turn the path does not exist yet. The frontend rejects the patch ("Failed to apply state patch") and the run never settles.

Emit a `STATE_SNAPSHOT` that carries the key right after `RUN_STARTED`, keeping any value from an earlier turn:

src/agents/shared_state_streaming.py

Copy Text
    
    
    from collections.abc import AsyncGenerator
    from typing import Any
    
    from ag_ui.core import BaseEvent, EventType, StateSnapshotEvent
    from agent_framework import Agent, BaseChatClient
    from agent_framework_ag_ui import AgentFrameworkAgent
    
    
    class SharedStateStreamingFrameworkAgent(AgentFrameworkAgent):
        async def run(  # type: ignore[override]
            self,
            input_data: dict[str, Any],
        ) -> AsyncGenerator[BaseEvent, None]:
            incoming = input_data.get("state")
            state = incoming if isinstance(incoming, dict) else {}
            document = state.get("document", "")
            seeded = False
            async for event in super().run(input_data):
                yield event
                # RUN_STARTED must be the first event; the seed follows it.
                if not seeded and getattr(event, "type", None) == EventType.RUN_STARTED:
                    yield StateSnapshotEvent(
                        type=EventType.STATE_SNAPSHOT,
                        snapshot={**state, "document": document},
                    )
                    seeded = True
    
    
    def create_shared_state_streaming_agent(
        chat_client: BaseChatClient,
    ) -> AgentFrameworkAgent:
        base_agent = Agent(
            client=chat_client,
            name="shared_state_streaming_agent",
            instructions=SYSTEM_PROMPT,  # tells the model to call write_document
            tools=[write_document],
        )
    
        return SharedStateStreamingFrameworkAgent(
            agent=base_agent,
            name="SharedStateStreamingAgent",
            description=(
                "Per-token state streaming: `write_document` arg deltas land "
                "in `state.document` as the tool call is generated."
            ),
            predict_state_config=PREDICT_STATE_CONFIG,
            require_confirmation=False,
        )

The backend pattern is always the same: map one streaming tool argument to one shared-state key. Each framework does this in its own way:

  * LangGraph Python: `StateStreamingMiddleware` with `StateItem(...)` entries.
  * LangGraph TypeScript: `copilotkitCustomizeConfig` with an `emitIntermediateState` mapping.
  * Direct SDK adapters: parse partial tool arguments in the streaming loop, and emit `STATE_SNAPSHOT` whenever the mapped value changes.
  * LlamaIndex and Pydantic AI: there is no per-token mapping. A backend tool sends a state snapshot after each step or tool call instead (see the setup above).



When the LLM streams that argument, CopilotKit writes every partial value into shared state before the tool even finishes executing.

shared_state_streaming.py

Copy Text
    
    
    # Tells the runtime to stream tool-argument deltas straight into
    # `state.document` while `write_document` is still streaming — matches
    # LGP's StateStreamingMiddleware setup.
    PREDICT_STATE_CONFIG: dict[str, dict[str, str]] = {
        "document": {
            "tool": "write_document",
            "tool_argument": "document",
        }
    }

A few things to note:

  * The state key must exist in your agent state (`document` in this demo).
  * The tool and argument names must match the exact LLM-facing tool call you want to forward (`write_document.document` here).
  * Streamed values are previews. When the step ends, the state the agent saves replaces them, so save the final value when the tool finishes. On CrewAI, LlamaIndex and Pydantic AI, write the final value to the agent state yourself, or it is overwritten when the step returns.



## The frontend: useAgent + OnStateChangedCopy Anchor Link

The UI side is the same as any other [shared-state](https://docs.copilotkit.ai/ms-agent-python/shared-state) subscription: `useAgent` with `OnStateChanged` gives you a reactive `agent.state`. Add `OnRunStatusChanged` if you want a "LIVE" / "done" indicator.

page.tsx

Copy Text
    
    
      // Subscribe to BOTH state changes and run-status changes. The former
      // drives the per-token document rerender; the latter toggles the
      // "LIVE" badge when the agent starts / stops.
      const { agent } = useAgent({
        agentId: "shared-state-streaming",
        updates: [UseAgentUpdate.OnStateChanged, UseAgentUpdate.OnRunStatusChanged],
      });

From there, `agent.state.document` is just a string that grows on every token, and `agent.isRunning` tells you whether to show a streaming indicator.

## Try itCopy Anchor Link

Ask the agent to write a short poem. The `document` text grows in your UI while the agent writes. When the run ends, `agent.isRunning` is `false`, so your streaming indicator turns off.

How is this guide?

GoodBad

[Previous PageRender agent state in your app](https://docs.copilotkit.ai/ms-agent-python/shared-state/rendering-in-app)[Next PageAgent Read-Only Context](https://docs.copilotkit.ai/ms-agent-python/shared-state/agent-readonly)
