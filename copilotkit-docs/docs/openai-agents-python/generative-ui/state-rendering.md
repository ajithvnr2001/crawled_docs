---
url: https://docs.copilotkit.ai/openai-agents-python/generative-ui/state-rendering/
title: State Rendering
method: scrapling+scrapegraph
fetched_at: 2026-11-12T10:53:41.473640+00:00
---

# State Rendering

> Source: https://docs.copilotkit.ai/openai-agents-python/generative-ui/state-rendering/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendOpenAI Agents SDK (Python)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/openai-agents-python)[Quickstart](https://docs.copilotkit.ai/openai-agents-python/quickstart)[Build with agents](https://docs.copilotkit.ai/openai-agents-python/build-with-agents)[Intelligence](https://docs.copilotkit.ai/openai-agents-python/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/openai-agents-python/frontend-tools)

Generative UI

Controlled

[Components as Tools](https://docs.copilotkit.ai/openai-agents-python/generative-ui/tool-based)[Tool Call Rendering](https://docs.copilotkit.ai/openai-agents-python/generative-ui/tool-rendering)[State Rendering](https://docs.copilotkit.ai/openai-agents-python/generative-ui/state-rendering)

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/openai-agents-python/webmcp)

Agent capabilities

[Sub-agents](https://docs.copilotkit.ai/openai-agents-python/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/openai-agents-python/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/openai-agents-python/learning)

[User Memories](https://docs.copilotkit.ai/openai-agents-python/intelligence/memories)

[Trajectories](https://docs.copilotkit.ai/openai-agents-python/intelligence/trajectories)

[Standalone collector](https://docs.copilotkit.ai/openai-agents-python/intelligence/standalone-collector)[Product Analytics](https://docs.copilotkit.ai/openai-agents-python/intelligence/analytics)[Channels](https://docs.copilotkit.ai/openai-agents-python/intelligence/channels)

Hosting

Backend

Runtime

Deployment

Debugging

Learn

Concepts

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/openai-agents-python/telemetry)[Community frameworks](https://docs.copilotkit.ai/openai-agents-python/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

State Rendering

Generative UIControlled

# State Rendering

Render your agent's state with custom UI components in real-time.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

shared_state_streaming.py

page.tsx

document-view.tsx

route.ts
    
    
    """shared-state-streaming: ``state.document`` grows while the model writes it.The model calls ``write_document`` with the whole text as its ``document``argument. The adapter streams that argument as TOOL_CALL_ARGS deltas, and``DocumentStreamingAgent`` follows them: after each delta it sends theargument's text so far as ``state.document``. The page renders``agent.state.document``, so the document appears token by token, aslanggraph-python's ``StateStreamingMiddleware`` does. The tool body thencommits the final text."""from collections.abc import AsyncIteratorfrom contextlib import aclosingfrom ag_ui.core import BaseEvent, EventType, RunAgentInput, StateDeltaEventfrom ag_ui_openai_agents import OpenAIAgentsAgent, shared_statefrom agents import Agent, function_toolfrom pydantic_core import from_jsonfrom demo_agents._common import MODEL, chat_settingsSYSTEM_PROMPT = (    "You are a collaborative writing assistant. Whenever the user asks you "    "to write, draft, or revise any piece of text, ALWAYS call the "    "`write_document` tool with the full content as a single string in the "    "`document` argument. Never paste the document into a chat message "    "directly — the document belongs in shared state and the UI renders it "    "live as you type. After the tool returns, reply with one short sentence.")@function_tooldef write_document(document: str) -> str:    """Write a document for the user. Always call this tool when the user asks    you to write, draft, or revise any text. The `document` argument is    streamed into shared state under the `document` key so the UI renders    the body live.    """    shared_state().update(document=document)    return "Document written to shared state."shared_state_streaming_agent = Agent(    name="writer",    instructions=SYSTEM_PROMPT,    model=MODEL,    model_settings=chat_settings(),    tools=[write_document],)def _document_so_far(arguments: str) -> str | None:    """The ``document`` argument as far as the model has written it."""    try:        # Unfinished JSON: a string cut off mid-way is kept as it stands.        value = from_json(arguments, allow_partial="trailing-strings")    except ValueError:        return None    document = value.get("document") if isinstance(value, dict) else None    return document if isinstance(document, str) else Noneclass DocumentStreamingAgent(OpenAIAgentsAgent):    """Streams ``write_document``'s ``document`` argument into the state."""    async def run_streamed(self, input: RunAgentInput) -> AsyncIterator[BaseEvent]:        arguments: dict[str, str] = {}  # tool call id -> arguments so far        async with aclosing(super().run_streamed(input)) as events:            async for event in events:                yield event                if (                    event.type == EventType.TOOL_CALL_START                    and event.tool_call_name == write_document.name                ):                    arguments[event.tool_call_id] = ""                elif (                    event.type == EventType.TOOL_CALL_ARGS                    and event.tool_call_id in arguments                ):                    arguments[event.tool_call_id] += event.delta                    document = _document_so_far(arguments[event.tool_call_id])                    if document is not None:                        yield StateDeltaEvent(                            type=EventType.STATE_DELTA,                            delta=[                                {"op": "add", "path": "/document", "value": document}                            ],                        )

## What is this?#

State rendering lets you build UI that reflects your agent's state in real-time. As your agent progresses through nodes and emits state updates, your frontend renders those changes, showing progress, drafts, or intermediate results.

**Free course:** See this pattern built end-to-end in [Build Interactive Agents with Generative UI](https://www.deeplearning.ai/short-courses/build-interactive-agents-with-generative-ui/) — a free DeepLearning.AI short course taught by CopilotKit's CEO covering the full Generative UI spectrum (Controlled, Declarative, and Open-Ended).

## When should I use this?#

Use state rendering when you want to:

  * Show real-time progress (e.g. "Researching... 2/5 complete")
  * Display drafts that update as the agent works
  * Build dashboards that reflect agent state
  * Render structured output outside of the chat



## How it works in code#

On the frontend, subscribe to the agent's state. Each time the backend forwards a fresh value, your component re-renders with the latest partial output.

page.tsx
    
    
      // Subscribe to BOTH state changes and run-status changes. The former  // drives the per-token document rerender; the latter toggles the  // "LIVE" badge when the agent starts / stops.  const { agent } = useAgent({    agentId: "shared-state-streaming",    updates: [UseAgentUpdate.OnStateChanged, UseAgentUpdate.OnRunStatusChanged],  });

On the backend, a state-streaming mapping forwards a specific tool argument straight into a state key _as it's being generated_. Some frameworks provide that as middleware; direct SDK adapters can emit `STATE_SNAPSHOT` events from their streaming loop. Either way, the UI can watch the answer assemble token-by-token rather than appearing in one burst between checkpoints.

The adapter streams a tool call's arguments as `TOOL_CALL_ARGS` events while the model writes them, but it does not copy them into state. The tool writes the finished value to state when it runs:

shared_state_streaming.py
    
    
    @function_tool
    def write_document(document: str) -> str:
        """Write a document for the user. Always call this tool when the user asks
        you to write, draft, or revise any text. The `document` argument is
        streamed into shared state under the `document` key so the UI renders
        the body live.
        """
        shared_state().update(document=document)
        return "Document written to shared state."
    
    

To fill the state while the model is still writing the argument, subclass `OpenAIAgentsAgent` and turn those argument chunks into `STATE_DELTA` events. The arguments are unfinished JSON until the call ends, so parse them with `pydantic_core.from_json(..., allow_partial="trailing-strings")`, which keeps a string that is cut off mid-way:

shared_state_streaming.py
    
    
    def _document_so_far(arguments: str) -> str | None:
        """The ``document`` argument as far as the model has written it."""
        try:
            # Unfinished JSON: a string cut off mid-way is kept as it stands.
            value = from_json(arguments, allow_partial="trailing-strings")
        except ValueError:
            return None
        document = value.get("document") if isinstance(value, dict) else None
        return document if isinstance(document, str) else None
    
    
    class DocumentStreamingAgent(OpenAIAgentsAgent):
        """Streams ``write_document``'s ``document`` argument into the state."""
    
        async def run_streamed(self, input: RunAgentInput) -> AsyncIterator[BaseEvent]:
            arguments: dict[str, str] = {}  # tool call id -> arguments so far
            async with aclosing(super().run_streamed(input)) as events:
                async for event in events:
                    yield event
                    if (
                        event.type == EventType.TOOL_CALL_START
                        and event.tool_call_name == write_document.name
                    ):
                        arguments[event.tool_call_id] = ""
                    elif (
                        event.type == EventType.TOOL_CALL_ARGS
                        and event.tool_call_id in arguments
                    ):
                        arguments[event.tool_call_id] += event.delta
                        document = _document_so_far(arguments[event.tool_call_id])
                        if document is not None:
                            yield StateDeltaEvent(
                                type=EventType.STATE_DELTA,
                                delta=[
                                    {"op": "add", "path": "/document", "value": document}
                                ],
                            )
    
    

Mount the agent wrapped in that subclass, `DocumentStreamingAgent(shared_state_streaming_agent)`, instead of a plain `OpenAIAgentsAgent`. The page then sees the document grow token by token, and the tool's own `STATE_SNAPSHOT` settles it once the call runs.

shared_state_streaming.py
    
    
    def _document_so_far(arguments: str) -> str | None:    """The ``document`` argument as far as the model has written it."""    try:        # Unfinished JSON: a string cut off mid-way is kept as it stands.        value = from_json(arguments, allow_partial="trailing-strings")    except ValueError:        return None    document = value.get("document") if isinstance(value, dict) else None    return document if isinstance(document, str) else Noneclass DocumentStreamingAgent(OpenAIAgentsAgent):    """Streams ``write_document``'s ``document`` argument into the state."""    async def run_streamed(self, input: RunAgentInput) -> AsyncIterator[BaseEvent]:        arguments: dict[str, str] = {}  # tool call id -> arguments so far        async with aclosing(super().run_streamed(input)) as events:            async for event in events:                yield event                if (                    event.type == EventType.TOOL_CALL_START                    and event.tool_call_name == write_document.name                ):                    arguments[event.tool_call_id] = ""                elif (                    event.type == EventType.TOOL_CALL_ARGS                    and event.tool_call_id in arguments                ):                    arguments[event.tool_call_id] += event.delta                    document = _document_so_far(arguments[event.tool_call_id])                    if document is not None:                        yield StateDeltaEvent(                            type=EventType.STATE_DELTA,                            delta=[                                {"op": "add", "path": "/document", "value": document}                            ],                        )

### On this page

What is this?When should I use this?How it works in code
