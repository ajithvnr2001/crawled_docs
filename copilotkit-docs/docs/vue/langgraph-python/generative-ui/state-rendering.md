---
url: https://docs.copilotkit.ai/vue/langgraph-python/generative-ui/state-rendering/
title: State Rendering
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:55.402052+00:00
---

# State Rendering

> Source: https://docs.copilotkit.ai/vue/langgraph-python/generative-ui/state-rendering/

Controlled

# State Rendering

Render your agent's state with custom UI components in real-time.

Copy MarkdownOpen

## What is this?Copy Anchor Link

State rendering lets you build UI that reflects your agent's state in real-time. As your agent progresses through nodes and emits state updates, your frontend renders those changes, showing progress, drafts, or intermediate results.

## When should I use this?Copy Anchor Link

Use state rendering when you want to:

  * Show real-time progress (e.g. "Researching... 2/5 complete")
  * Display drafts that update as the agent works
  * Build dashboards that reflect agent state
  * Render structured output outside of the chat



## How it works in codeCopy Anchor Link

On the frontend, subscribe to the agent's state. Each time the backend forwards a fresh value, your component re-renders with the latest partial output. `useAgent` returns an `agent` ref; read `agent.value?.state` in script or let templates unwrap the ref. Keep the provider in an ancestor SFC.

src/components/ResearchProgress.vue

Copy Text
    
    
    <script setup lang="ts">
    import { computed } from "vue";
    import { useAgent, UseAgentUpdate } from "@copilotkit/vue/v2";
    
    type ResearchState = { status?: string; draft?: string; completed?: number; total?: number };
    
    const { agent } = useAgent({
      agentId: "researcher",
      updates: [UseAgentUpdate.OnStateChanged, UseAgentUpdate.OnRunStatusChanged],
    });
    
    const state = computed(() => (agent.value?.state ?? {}) as ResearchState);
    </script>
    
    <template>
      <section aria-live="polite">
        <p>{{ state.status ?? "Idle" }}</p>
        <progress :value="state.completed ?? 0" :max="state.total ?? 1" />
        <article v-if="state.draft">{{ state.draft }}</article>
      </section>
    </template>

src/App.vue

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotChat, CopilotKitProvider } from "@copilotkit/vue/v2";
    import ResearchProgress from "./components/ResearchProgress.vue";
    </script>
    
    <template>
      <CopilotKitProvider runtime-url="/api/copilotkit">
        <ResearchProgress />
        <CopilotChat agent-id="researcher" />
      </CopilotKitProvider>
    </template>

On the backend, a state-streaming mapping forwards a tool argument into a state key while the model writes it. Some frameworks provide that as middleware. Direct SDK adapters can emit `STATE_SNAPSHOT` events from their streaming loop. Either way, the UI can watch the answer assemble token-by-token rather than appearing in one burst between checkpoints.

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

Ask the researcher agent to write a report. The status line and the progress bar change while the agent runs, and the draft text grows as the tokens arrive.

Treat agent state as untrusted external data. Validate it before using it for privileged actions, and avoid putting secrets in state that is streamed to the browser.

How is this guide?

GoodBad

[Previous PageTool Call Rendering](https://docs.copilotkit.ai/vue/langgraph-python/generative-ui/tool-rendering)[Next PageMCP Apps](https://docs.copilotkit.ai/vue/langgraph-python/generative-ui/mcp-apps)
