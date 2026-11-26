---
url: https://docs.copilotkit.ai/deepagents/shared-state/streaming/
title: State Streaming
method: scrapling+scrapegraph
fetched_at: 2026-11-26T12:11:26.847927+00:00
---

# State Streaming

> Source: https://docs.copilotkit.ai/deepagents/shared-state/streaming/

Shared state

# State Streaming

Stream partial agent state updates to the UI while a tool call is still running.

Copy MarkdownOpen

Not available for Langchain DeepAgents yet

The code on this page comes from the showcase's `shared-state-streaming` demo, and Langchain DeepAgents doesn't have it yet. See this page for [CopilotKit's Built-in Agent](https://docs.copilotkit.ai/shared-state/streaming), [LangGraph (Python)](https://docs.copilotkit.ai/langgraph-python/shared-state/streaming), [LangGraph (TypeScript)](https://docs.copilotkit.ai/langgraph-typescript/shared-state/streaming).

## What is this?Copy Anchor Link

By default, agent state only updates _between_ backend checkpoints, so a long-running tool call (writing a full document, drafting an email) appears to the UI as one big burst at the end. For agent-native apps, that feels broken: users expect to watch the output materialise.

**State streaming** copies one tool argument into an agent state key while the model writes the argument. The UI, subscribed via `useAgent`, re-renders every token.

## When should I use this?Copy Anchor Link

Use state streaming whenever a tool's output is long-form text or a growing structured value and you want the user to see it assemble in real time. Common shapes:

  * A collaborative writing agent that emits a document
  * A research agent that accumulates a list of findings
  * A planning agent that builds up a step-by-step plan



## The backend: one streaming state mappingCopy Anchor Link

### Build an agent that streams a tool argument into stateCopy Anchor Link

Deep Agents has no live demo on this page yet, so the demo code on this page does not show for it. Define the state key, add a tool that saves the completed value, and add `StateStreamingMiddleware` with one `StateItem` that maps the tool argument to the state key. This example streams a `searches` list:

PythonTypeScript

agent.py

Copy Text
    
    
    from typing import Any, TypedDict
    
    from copilotkit import (
        CopilotKitMiddleware,
        CopilotKitState,
        StateItem,
        StateStreamingMiddleware,
    )
    from deepagents import create_deep_agent
    from langchain_openai import ChatOpenAI
    from langchain.agents.middleware import AgentMiddleware
    from langchain.messages import ToolMessage
    from langchain.tools import ToolRuntime, tool
    from langgraph.types import Command
    
    class Search(TypedDict):
        query: str
        done: bool
    
    class AgentState(CopilotKitState):
        searches: list[Search]
    
    class SearchesStateMiddleware(AgentMiddleware[AgentState, Any, Any]):
        state_schema = AgentState
    
    @tool
    def report_research_progress(
        searches: list[Search],
        runtime: ToolRuntime[None, AgentState],
    ) -> Command:
        """Report the current research tasks and completion status."""
        return Command(
            update={
                "searches": searches,
                "messages": [
                    ToolMessage(
                        content="Research progress saved.",
                        tool_call_id=runtime.tool_call_id,
                    )
                ],
            }
        )
    
    agent = create_deep_agent(
        model=ChatOpenAI(model="gpt-6-luna", reasoning_effort="none"),
        tools=[report_research_progress],
        middleware=[
            SearchesStateMiddleware(),
            CopilotKitMiddleware(),
            StateStreamingMiddleware(
                StateItem(
                    state_key="searches",
                    tool="report_research_progress",
                    tool_argument="searches",
                )
            ),
        ],
        system_prompt=(
            "You are a research assistant. Use report_research_progress "
            "to show each task and mark it done when complete."
        ),
    )

### Understand the two update phasesCopy Anchor Link

The state-streaming middleware sends the partial `searches` argument while the model writes it. The frontend can show each partial value at once.

The tool then returns a `Command` that saves the completed list. Its `ToolMessage` closes the active tool call.

When the run finishes, the agent's final state is the single source of truth. A streamed value that the tool does not also save in its `Command` disappears at the end of the run, with no error.

Each setting must match your code. A mismatch sends updates to the wrong state field, or to none:

  * `state_key` (`stateKey`): the state field.
  * `tool`: the name of the tool.
  * `tool_argument` (`toolArgument`): the argument of the tool.



### Render the state in the UICopy Anchor Link

Use `useAgent` to read the state anywhere in your app: in the chat, in a dashboard, in a sidebar.

app/page.tsx

Copy Text
    
    
    import { useAgent } from "@copilotkit/react-core/v2";
    
    function YourMainContent() {
      const { agent } = useAgent({
        agentId: "sample_agent",
      });
    
      const state = (agent.state ?? {}) as {
        searches?: { query: string; done: boolean }[];
      };
      const searches = state.searches ?? [];
    
      return (
        <div>
          {searches.map((search, index) => (
            <div key={index}>
              {search.done ? "✅" : "⏳"} {search.query}
            </div>
          ))}
        </div>
      );
    }

Ask the agent to research a topic. The search items appear and update while the agent works.

The backend pattern is always the same: map one streaming tool argument to one shared-state key. Each framework does this in its own way:

  * LangGraph Python: `StateStreamingMiddleware` with `StateItem(...)` entries.
  * LangGraph TypeScript: `copilotkitCustomizeConfig` with an `emitIntermediateState` mapping.
  * Direct SDK adapters: parse partial tool arguments in the streaming loop, and emit `STATE_SNAPSHOT` whenever the mapped value changes.
  * LlamaIndex and Pydantic AI: there is no per-token mapping. A backend tool sends a state snapshot after each step or tool call instead (see the setup above).



When the LLM streams that argument, CopilotKit writes every partial value into shared state before the tool even finishes executing.

A few things to note:

  * The state key must exist in your agent state (`document` in this demo).
  * The tool and argument names must match the exact LLM-facing tool call you want to forward (`write_document.document` here).
  * Streamed values are previews. When the step ends, the state the agent saves replaces them, so save the final value when the tool finishes. On CrewAI, LlamaIndex and Pydantic AI, write the final value to the agent state yourself, or it is overwritten when the step returns.



## The frontend: useAgent + OnStateChangedCopy Anchor Link

The UI side is the same as any other [shared-state](https://docs.copilotkit.ai/deepagents/shared-state) subscription: `useAgent` with `OnStateChanged` gives you a reactive `agent.state`. Add `OnRunStatusChanged` if you want a "LIVE" / "done" indicator.

From there, `agent.state.document` is just a string that grows on every token, and `agent.isRunning` tells you whether to show a streaming indicator.

## Try itCopy Anchor Link

Ask the agent to write a short poem. The `document` text grows in your UI while the agent writes. When the run ends, `agent.isRunning` is `false`, so your streaming indicator turns off.

How is this guide?

GoodBad

[Previous PageRender agent state in your app](https://docs.copilotkit.ai/deepagents/shared-state/rendering-in-app)[Next PageAgent Read-Only Context](https://docs.copilotkit.ai/deepagents/shared-state/agent-readonly)
