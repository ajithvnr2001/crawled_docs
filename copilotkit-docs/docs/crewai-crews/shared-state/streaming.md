---
url: https://docs.copilotkit.ai/crewai-crews/shared-state/streaming/
title: State Streaming
method: scrapling+scrapegraph
fetched_at: 2026-11-26T12:11:26.655965+00:00
---

# State Streaming

> Source: https://docs.copilotkit.ai/crewai-crews/shared-state/streaming/

Shared state

# State Streaming

Stream partial agent state updates to the UI while a tool call is still running.

Copy MarkdownOpen

State Streaming

DemoCode

[](https://showcase-crewai-crews-production.up.railway.app/demos/shared-state-streaming "Open in a new tab")[](https://github.com/CopilotKit/CopilotKit/tree/main/showcase/integrations/crewai-crews/src/app/demos/shared-state-streaming "View the code on GitHub")

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

### Install the CrewAI AG-UI packageCopy Anchor Link

Copy Text
    
    
    pip install ag-ui-crewai litellm

### Declare the state keyCopy Anchor Link

src/agents/shared_state_streaming.py

Copy Text
    
    
    from ag_ui_crewai import CopilotKitState
    
    
    class SharedStateStreamingState(CopilotKitState):
        document: str = ""

### Map the tool argument to the state keyCopy Anchor Link

Call `copilotkit_predict_state` with one `StateItem` before the model call. While the model streams `write_document`, CopilotKit copies the partial `document` argument into the `document` state key. Wrap the call in `copilotkit_stream`, or nothing streams until the turn ends.

src/agents/shared_state_streaming.py

Copy Text
    
    
    from crewai.flow.flow import Flow, start
    from litellm import acompletion
    
    from ag_ui_crewai import StateItem, copilotkit_predict_state, copilotkit_stream
    
    
    class SharedStateStreamingFlow(Flow[SharedStateStreamingState]):
        @start()
        async def write(self) -> None:
            await copilotkit_predict_state(
                [
                    StateItem(
                        state_key="document",
                        tool="write_document",
                        tool_argument="document",
                    )
                ]
            )
            tools = [*self.state.copilotkit.actions, WRITE_DOCUMENT_TOOL]
            response = await copilotkit_stream(
                await acompletion(
                    reasoning_effort="none",
                    allowed_openai_params=["reasoning_effort"],
                    model="openai/gpt-6-luna",
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        *self.state.messages,
                    ],
                    tools=tools,
                    parallel_tool_calls=False,
                    stream=True,
                )
            )

`WRITE_DOCUMENT_TOOL` is a plain OpenAI-format tool schema with one required `document` string argument.

### Persist the final valueCopy Anchor Link

When a Flow method finishes, **its state becomes the single source of truth**. The streamed predictions are not written to `self.state`, so assign the final value yourself. Otherwise it is overwritten when the method completes.

src/agents/shared_state_streaming.py

Copy Text
    
    
            # Still inside write(), after the model call (needs `import json`)
            message = response.choices[0].message
            self.state.messages.append(message)
            calls = message.get("tool_calls") or []
            write_call = next(
                (
                    call
                    for call in calls
                    if call.get("function", {}).get("name") == "write_document"
                ),
                None,
            )
            if write_call is None:
                return
    
            arguments = json.loads(
                write_call.get("function", {}).get("arguments") or "{}"
            )
            document = arguments.get("document")
            self.state.document = document if isinstance(document, str) else ""

The showcase Flow then appends a `role: "tool"` message, calls `copilotkit_emit_tool_result`, and asks the model for a one-line confirmation. See `src/agents/shared_state_streaming.py`.

Emit progress without a tool argument

To show progress that is not a tool argument, assign the value and call `copilotkit_emit_state` after each sub-step:

agent.py

Copy Text
    
    
    from ag_ui_crewai import copilotkit_emit_state
    
    for step in steps:
        self.state.observed_steps = [*self.state.observed_steps, step]
        await copilotkit_emit_state(self.state)
        await asyncio.sleep(1)

The backend pattern is always the same: map one streaming tool argument to one shared-state key. Each framework does this in its own way:

  * LangGraph Python: `StateStreamingMiddleware` with `StateItem(...)` entries.
  * LangGraph TypeScript: `copilotkitCustomizeConfig` with an `emitIntermediateState` mapping.
  * Direct SDK adapters: parse partial tool arguments in the streaming loop, and emit `STATE_SNAPSHOT` whenever the mapped value changes.
  * LlamaIndex and Pydantic AI: there is no per-token mapping. A backend tool sends a state snapshot after each step or tool call instead (see the setup above).



When the LLM streams that argument, CopilotKit writes every partial value into shared state before the tool even finishes executing.

shared_state_streaming.py

Copy Text
    
    
    class SharedStateStreamingState(CopilotKitState):
        document: str = ""
    
    
    class SharedStateStreamingFlow(Flow[SharedStateStreamingState]):
        """Predict write_document arguments into state, then persist the result."""
    
        @start()
        async def write(self) -> None:
            await copilotkit_predict_state(
                [
                    StateItem(
                        state_key="document",
                        tool="write_document",
                        tool_argument="document",
                    )
                ]
            )

A few things to note:

  * The state key must exist in your agent state (`document` in this demo).
  * The tool and argument names must match the exact LLM-facing tool call you want to forward (`write_document.document` here).
  * Streamed values are previews. When the step ends, the state the agent saves replaces them, so save the final value when the tool finishes. On CrewAI, LlamaIndex and Pydantic AI, write the final value to the agent state yourself, or it is overwritten when the step returns.



## The frontend: useAgent + OnStateChangedCopy Anchor Link

The UI side is the same as any other [shared-state](https://docs.copilotkit.ai/crewai-crews/shared-state) subscription: `useAgent` with `OnStateChanged` gives you a reactive `agent.state`. Add `OnRunStatusChanged` if you want a "LIVE" / "done" indicator.

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

[Previous PageRender agent state in your app](https://docs.copilotkit.ai/crewai-crews/shared-state/rendering-in-app)[Next PageAgent Read-Only Context](https://docs.copilotkit.ai/crewai-crews/shared-state/agent-readonly)
