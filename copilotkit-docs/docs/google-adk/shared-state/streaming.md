---
url: https://docs.copilotkit.ai/google-adk/shared-state/streaming/
title: State Streaming
method: scrapling+scrapegraph
fetched_at: 2026-11-26T12:11:27.216023+00:00
---

# State Streaming

> Source: https://docs.copilotkit.ai/google-adk/shared-state/streaming/

Shared state

# State Streaming

Stream partial agent state updates to the UI while a tool call is still running.

Copy MarkdownOpen

State Streaming

DemoCode

[](https://showcase-google-adk-production.up.railway.app/demos/shared-state-streaming "Open in a new tab")[](https://github.com/CopilotKit/CopilotKit/tree/main/showcase/integrations/google-adk/src/app/demos/shared-state-streaming "View the code on GitHub")

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

### Install the ADK + AG-UI bridgeCopy Anchor Link

Copy Text
    
    
    pip install ag-ui-adk

### Declare the predicted state mappingCopy Anchor Link

ADK state streaming uses `PredictStateMapping` to map the streaming `write_document` tool argument into `state["document"]`. Add `AGUIToolset()` to the agent so CopilotKit can forward the state deltas to the UI.

shared_state_streaming_agent.py

Copy Text
    
    
    from __future__ import annotations
    
    from ag_ui_adk import AGUIToolset
    from ag_ui_adk.config import PredictStateMapping
    from google.adk.agents import LlmAgent
    from google.adk.tools import ToolContext
    
    from agents.shared_chat import get_model, stop_on_terminal_text
    
    
    def write_document(tool_context: ToolContext, document: str) -> dict:
        """Write a document into shared state.
    
        Whenever the user asks you to write or draft anything (essay, poem,
        email, summary, etc.), call this tool with the full content as a
        single string. The UI renders state["document"] live as you type.
    
        Argument name `document` mirrors langgraph-python's `write_document`
        signature so the shared D5 fixture (`tool_argument="document"`) and
        the LGP-aligned PredictStateMapping below stay in lock-step.
        """
        tool_context.state["document"] = document
        return {"status": "ok", "length": len(document)}
    
    
    _INSTRUCTION = (
        "You are a collaborative writing assistant. Whenever the user asks "
        "you to write, draft, or revise any piece of text, ALWAYS call the "
        "`write_document` tool with the full content as a single string. "
        "Never paste the document into a chat message directly — the document "
        "belongs in shared state and the UI renders it live as you type."
    )
    
    shared_state_streaming_agent = LlmAgent(
        name="SharedStateStreamingAgent",
        model=get_model(),
        instruction=_INSTRUCTION,
        tools=[write_document, AGUIToolset()],
        after_model_callback=stop_on_terminal_text,
    )
    
    
    SHARED_STATE_STREAMING_PREDICT_STATE = [
        PredictStateMapping(
            state_key="document",
            tool="write_document",
            tool_argument="document",
            emit_confirm_tool=False,
            stream_tool_call=True,
        ),
    ]

### Pass the mapping to `ADKAgent`Copy Anchor Link

The mapping does nothing until it reaches the `ADKAgent` middleware. Pass it as `predict_state`, and turn on `streaming_function_call_arguments` so the middleware receives the tool arguments while the model writes them. The showcase server builds each endpoint this way:

src/agent_server.py

Copy Text
    
    
    from ag_ui_adk import ADKAgent, add_adk_fastapi_endpoint
    
    middleware = ADKAgent(
        adk_agent=shared_state_streaming_agent,
        user_id="demo_user",
        session_timeout_seconds=3600,
        use_in_memory_services=True,
        predict_state=SHARED_STATE_STREAMING_PREDICT_STATE,
        streaming_function_call_arguments=True,
    )
    add_adk_fastapi_endpoint(app, middleware, path="/shared-state-streaming")

With `predict_state`, the frontend gets `document` while the model writes the `document` argument of `write_document`. When the tool runs, `tool_context.state` stores the final value.

Per-token streaming needs `google-adk` 1.24.0 or later through Vertex AI. On older versions, or through Gemini in Google AI Studio, the middleware logs a `UserWarning` at startup and streams in larger chunks. The state still updates, only less often.

### Stop after the final model responseCopy Anchor Link

The agent above imports `stop_on_terminal_text` and registers it as its `after_model_callback`. This prevents Gemini from issuing the same tool call again after its final text response. See the canonical [`stop_on_terminal_text` implementation](https://github.com/CopilotKit/CopilotKit/blob/main/showcase/integrations/google-adk/src/agents/shared_chat.py) when adapting the callback for your project.

The backend pattern is always the same: map one streaming tool argument to one shared-state key. Each framework does this in its own way:

  * LangGraph Python: `StateStreamingMiddleware` with `StateItem(...)` entries.
  * LangGraph TypeScript: `copilotkitCustomizeConfig` with an `emitIntermediateState` mapping.
  * Direct SDK adapters: parse partial tool arguments in the streaming loop, and emit `STATE_SNAPSHOT` whenever the mapped value changes.
  * LlamaIndex and Pydantic AI: there is no per-token mapping. A backend tool sends a state snapshot after each step or tool call instead (see the setup above).



When the LLM streams that argument, CopilotKit writes every partial value into shared state before the tool even finishes executing.

shared_state_streaming_agent.py

Copy Text
    
    
    from __future__ import annotations
    
    from ag_ui_adk import AGUIToolset
    from ag_ui_adk.config import PredictStateMapping
    from google.adk.agents import LlmAgent
    from google.adk.tools import ToolContext
    
    from agents.shared_chat import get_model, stop_on_terminal_text
    
    
    def write_document(tool_context: ToolContext, document: str) -> dict:
        """Write a document into shared state.
    
        Whenever the user asks you to write or draft anything (essay, poem,
        email, summary, etc.), call this tool with the full content as a
        single string. The UI renders state["document"] live as you type.
    
        Argument name `document` mirrors langgraph-python's `write_document`
        signature so the shared D5 fixture (`tool_argument="document"`) and
        the LGP-aligned PredictStateMapping below stay in lock-step.
        """
        tool_context.state["document"] = document
        return {"status": "ok", "length": len(document)}
    
    
    _INSTRUCTION = (
        "You are a collaborative writing assistant. Whenever the user asks "
        "you to write, draft, or revise any piece of text, ALWAYS call the "
        "`write_document` tool with the full content as a single string. "
        "Never paste the document into a chat message directly — the document "
        "belongs in shared state and the UI renders it live as you type."
    )
    
    shared_state_streaming_agent = LlmAgent(
        name="SharedStateStreamingAgent",
        model=get_model(),
        instruction=_INSTRUCTION,
        tools=[write_document, AGUIToolset()],
        after_model_callback=stop_on_terminal_text,
    )
    
    
    SHARED_STATE_STREAMING_PREDICT_STATE = [
        PredictStateMapping(
            state_key="document",
            tool="write_document",
            tool_argument="document",
            emit_confirm_tool=False,
            stream_tool_call=True,
        ),
    ]
    

A few things to note:

  * The state key must exist in your agent state (`document` in this demo).
  * The tool and argument names must match the exact LLM-facing tool call you want to forward (`write_document.document` here).
  * Streamed values are previews. When the step ends, the state the agent saves replaces them, so save the final value when the tool finishes. On CrewAI, LlamaIndex and Pydantic AI, write the final value to the agent state yourself, or it is overwritten when the step returns.



## The frontend: useAgent + OnStateChangedCopy Anchor Link

The UI side is the same as any other [shared-state](https://docs.copilotkit.ai/google-adk/shared-state) subscription: `useAgent` with `OnStateChanged` gives you a reactive `agent.state`. Add `OnRunStatusChanged` if you want a "LIVE" / "done" indicator.

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

[Previous PageRender agent state in your app](https://docs.copilotkit.ai/google-adk/shared-state/rendering-in-app)[Next PageAgent Read-Only Context](https://docs.copilotkit.ai/google-adk/shared-state/agent-readonly)
