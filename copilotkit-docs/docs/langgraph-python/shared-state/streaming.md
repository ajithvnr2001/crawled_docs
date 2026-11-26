---
url: https://docs.copilotkit.ai/langgraph-python/shared-state/streaming/
title: State Streaming
method: scrapling+scrapegraph
fetched_at: 2026-11-26T12:11:25.511273+00:00
---

# State Streaming

> Source: https://docs.copilotkit.ai/langgraph-python/shared-state/streaming/

Shared state

# State Streaming

Stream partial agent state updates to the UI while a tool call is still running.

Copy MarkdownOpen

Shared State: Streaming

DemoCode

[](https://showcase-langgraph-python-production.up.railway.app/demos/shared-state-streaming "Open in a new tab")[](https://github.com/CopilotKit/CopilotKit/tree/main/showcase/integrations/langgraph-python/src/app/demos/shared-state-streaming "View the code on GitHub")

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

### Install the LangGraph Python SDKCopy Anchor Link

uvpoetrypipconda

Copy Text
    
    
    uv add copilotkit

### Add state streaming middlewareCopy Anchor Link

`StateStreamingMiddleware` maps a tool argument to an agent state key and forwards partial tool-call arguments as state updates while the model is still generating.

shared_state_streaming.py

Copy Text
    
    
    import uuid
    
    from langchain.agents import AgentState as BaseAgentState, create_agent
    from langchain.tools import ToolRuntime, tool
    from langchain_core.messages import ToolMessage
    from langchain_openai import ChatOpenAI
    from langgraph.types import Command
    
    from copilotkit import (
        CopilotKitMiddleware,
        StateItem,
        StateStreamingMiddleware,
    )
    
    
    class AgentState(BaseAgentState):
        """Shared state. `document` is streamed token-by-token."""
    
        document: str
    
    
    @tool
    def write_document(document: str, runtime: ToolRuntime) -> Command:
        """Write a document for the user.
    
        Always call this tool when the user asks you to write or draft
        something of any length (an essay, poem, email, summary, etc.).
        The `document` argument is streamed *per token* into shared agent
        state under the `document` key, so the UI can render it as it is
        generated.
        """
        return Command(
            update={
                "document": document,
                "messages": [
                    ToolMessage(
                        content="Document written to shared state.",
                        name="write_document",
                        id=str(uuid.uuid4()),
                        tool_call_id=runtime.tool_call_id,
                    )
                ],
            }
        )
    
    
    graph = create_agent(
        model=ChatOpenAI(reasoning_effort="none", model="gpt-6-luna"),
        tools=[write_document],
        middleware=[
            CopilotKitMiddleware(),
            # Forward every token of write_document's `document` argument
            # straight into state["document"] while the tool call is still
            # streaming. Without this, `document` would only update once
            # the tool call completes.
            #
            # NOTE: the frontend `usePredictStateSubscription` hook indexes
            # the (partial-JSON-parsed) tool args by `state_key`, so the
            # tool's argument name MUST match `state_key` ("document") for
            # per-token deltas to land in `state.document`.
            StateStreamingMiddleware(
                StateItem(
                    state_key="document",
                    tool="write_document",
                    tool_argument="document",
                )
            ),
        ],
        state_schema=AgentState,
        system_prompt=(
            "You are a collaborative writing assistant. Whenever the user asks "
            "you to write, draft, or revise any piece of text, ALWAYS call the "
            "`write_document` tool with the full content as a single string in "
            "the `document` argument. Never paste the document into a chat "
            "message directly — the document belongs in shared state and the "
            "UI renders it live as you type."
        ),
    )

### Using a custom graph instead of `create_agent`Copy Anchor Link

`StateStreamingMiddleware` is a `create_agent` middleware. In a graph where you define the nodes and edges yourself, map the tool argument with `copilotkit_customize_config` and pass the returned config to the model call:

agent.py

Copy Text
    
    
    from copilotkit import CopilotKitState
    from copilotkit.langgraph import copilotkit_customize_config
    from langchain_core.messages import SystemMessage
    from langchain_core.runnables import RunnableConfig
    
    class AgentState(CopilotKitState):
        observed_steps: list[str]
    
    async def chat_node(state: AgentState, config: RunnableConfig):
        streaming_config = copilotkit_customize_config(
            config,
            emit_intermediate_state=[
                {
                    "state_key": "observed_steps",
                    "tool": "step_progress_tool",
                    "tool_argument": "steps",
                },
            ]
        )
    
        model_with_tools = model.bind_tools(
            [
                *state["copilotkit"]["actions"],
                *tools,
            ],
            parallel_tool_calls=False,
        )
    
        response = await model_with_tools.ainvoke(
            [
                SystemMessage(
                    content="You are a task performer. Report your steps "
                    "using step_progress_tool."
                ),
                *state["messages"],
            ],
            streaming_config,
        )
        return {"messages": [response]}

To push progress from your own code instead of a tool call, call `copilotkit_emit_state` with the state you want the UI to show:

agent.py

Copy Text
    
    
    from copilotkit.langgraph import copilotkit_emit_state
    
    for step in steps:
        state["observed_steps"] = state.get("observed_steps", []) + [step]
        await copilotkit_emit_state(config, state)

Streamed values are previews. When the node finishes, the state it returns replaces them, so return every key you want to keep, or the UI loses the streamed value.

The backend pattern is always the same: map one streaming tool argument to one shared-state key. Each framework does this in its own way:

  * LangGraph Python: `StateStreamingMiddleware` with `StateItem(...)` entries.
  * LangGraph TypeScript: `copilotkitCustomizeConfig` with an `emitIntermediateState` mapping.
  * Direct SDK adapters: parse partial tool arguments in the streaming loop, and emit `STATE_SNAPSHOT` whenever the mapped value changes.
  * LlamaIndex and Pydantic AI: there is no per-token mapping. A backend tool sends a state snapshot after each step or tool call instead (see the setup above).



When the LLM streams that argument, CopilotKit writes every partial value into shared state before the tool even finishes executing.

shared_state_streaming.py

Copy Text
    
    
    import uuid
    
    from langchain.agents import AgentState as BaseAgentState, create_agent
    from langchain.tools import ToolRuntime, tool
    from langchain_core.messages import ToolMessage
    from langchain_openai import ChatOpenAI
    from langgraph.types import Command
    
    from copilotkit import (
        CopilotKitMiddleware,
        StateItem,
        StateStreamingMiddleware,
    )
    
    
    class AgentState(BaseAgentState):
        """Shared state. `document` is streamed token-by-token."""
    
        document: str
    
    
    @tool
    def write_document(document: str, runtime: ToolRuntime) -> Command:
        """Write a document for the user.
    
        Always call this tool when the user asks you to write or draft
        something of any length (an essay, poem, email, summary, etc.).
        The `document` argument is streamed *per token* into shared agent
        state under the `document` key, so the UI can render it as it is
        generated.
        """
        return Command(
            update={
                "document": document,
                "messages": [
                    ToolMessage(
                        content="Document written to shared state.",
                        name="write_document",
                        id=str(uuid.uuid4()),
                        tool_call_id=runtime.tool_call_id,
                    )
                ],
            }
        )
    
    
    graph = create_agent(
        model=ChatOpenAI(reasoning_effort="none", model="gpt-6-luna"),
        tools=[write_document],
        middleware=[
            CopilotKitMiddleware(),
            # Forward every token of write_document's `document` argument
            # straight into state["document"] while the tool call is still
            # streaming. Without this, `document` would only update once
            # the tool call completes.
            #
            # NOTE: the frontend `usePredictStateSubscription` hook indexes
            # the (partial-JSON-parsed) tool args by `state_key`, so the
            # tool's argument name MUST match `state_key` ("document") for
            # per-token deltas to land in `state.document`.
            StateStreamingMiddleware(
                StateItem(
                    state_key="document",
                    tool="write_document",
                    tool_argument="document",
                )
            ),
        ],
        state_schema=AgentState,
        system_prompt=(
            "You are a collaborative writing assistant. Whenever the user asks "
            "you to write, draft, or revise any piece of text, ALWAYS call the "
            "`write_document` tool with the full content as a single string in "
            "the `document` argument. Never paste the document into a chat "
            "message directly — the document belongs in shared state and the "
            "UI renders it live as you type."
        ),
    )

A few things to note:

  * The state key must exist in your agent state (`document` in this demo).
  * The tool and argument names must match the exact LLM-facing tool call you want to forward (`write_document.document` here).
  * Streamed values are previews. When the step ends, the state the agent saves replaces them, so save the final value when the tool finishes. On CrewAI, LlamaIndex and Pydantic AI, write the final value to the agent state yourself, or it is overwritten when the step returns.



## The frontend: useAgent + OnStateChangedCopy Anchor Link

The UI side is the same as any other [shared-state](https://docs.copilotkit.ai/langgraph-python/shared-state) subscription: `useAgent` with `OnStateChanged` gives you a reactive `agent.state`. Add `OnRunStatusChanged` if you want a "LIVE" / "done" indicator.

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

[Previous PageRender agent state in your app](https://docs.copilotkit.ai/langgraph-python/shared-state/rendering-in-app)[Next PageAgent Read-Only Context](https://docs.copilotkit.ai/langgraph-python/shared-state/agent-readonly)
