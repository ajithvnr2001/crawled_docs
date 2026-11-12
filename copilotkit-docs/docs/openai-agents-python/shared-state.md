---
url: https://docs.copilotkit.ai/openai-agents-python/shared-state/
title: Shared State
method: scrapling+scrapegraph
fetched_at: 2026-11-12T10:53:47.147241+00:00
---

# Shared State

> Source: https://docs.copilotkit.ai/openai-agents-python/shared-state/

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

Declarative

Open-ended

Interactivity

Shared state

[Shared State](https://docs.copilotkit.ai/openai-agents-python/shared-state)[Render agent state in your app](https://docs.copilotkit.ai/openai-agents-python/shared-state/rendering-in-app)[State Streaming](https://docs.copilotkit.ai/openai-agents-python/shared-state/streaming)[Agent Read-Only Context](https://docs.copilotkit.ai/openai-agents-python/shared-state/agent-readonly)

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

Shared State

InteractivityShared state

# Shared State

Create a two-way connection between your UI and agent state.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is shared state?#

Agentic Copilots maintain a shared state that seamlessly connects your UI with the agent's execution. This shared state system allows you to:

  * Display the agent's current progress and intermediate results
  * Update the agent's state through UI interactions
  * React to state changes in real-time across your application

![Shared State Demo](https://cdn.copilotkit.ai/docs/copilotkit/images/coagents/SharedStateCoAgents.gif)

See this in Inspector

Open Inspector on localhost. Open a thread, then click **State**. Agent state updates here as the run proceeds.

More detail: [Inspector](https://docs.copilotkit.ai/openai-agents-python/inspector).

## When should I use this?#

Use shared state when you want the agent and the user to collaborate through the same application state. The agent's outputs are reflected in the UI, and user updates in the UI are reflected in the agent's execution.

[Building stateful agents?Persistent threads ship with CopilotKit Intelligence on the free Developer tier.Get CopilotKit Intelligence free](https://ssr-placeholder.invalid/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=docs_shared_state&utm_frontend=react&utm_backend=openai-agents-python)

## Reading agent state#

### Show the model the state in its instructions

The page's state arrives with every run as `RunAgentInput.state`, and the adapter makes it the run's shared state. It does not reach the prompt by itself. Give the agent dynamic instructions that read it with the adapter's `shared_state()`, so the model sees the current value on every turn, including edits the user made with `agent.setState`:

shared_state.py
    
    
    def with_state(prompt: str) -> Callable[[RunContextWrapper[Any], Agent[Any]], str]:
        """Dynamic instructions: ``prompt`` plus the run's shared state as JSON."""
    
        def instructions(_ctx: RunContextWrapper[Any], _agent: Agent[Any]) -> str:
            state = shared_state().value
            if not state:
                return prompt
            return (
                f"{prompt}\n\nCurrent shared application state (JSON; the user may "
                f"have edited it since your last turn):\n{json.dumps(state)}"
            )
    
        return instructions
    
    

shared_state.py
    
    
    READ_WRITE_PROMPT = (
        "You are a helpful, concise assistant. The shared application state below "
        "has a `preferences` object with the user's name, preferred tone, "
        "language and interests, which the user edits in the app: always respect "
        "them, and address the user by name when you know it. Its `notes` list "
        "holds what you have remembered so far. When the user asks you to "
        "remember something, or when you observe something worth surfacing in "
        "the UI, call `set_notes` with the FULL updated list of short note "
        "strings (existing notes + new)."
    )
    
    
    shared_state_read_write_agent = Agent(
        name="preferences_assistant",
        instructions=with_state(READ_WRITE_PROMPT),
        model=MODEL,
        model_settings=chat_settings(),
        tools=[set_notes],
    )
    
    

### Write state from a server tool

Server tools are ordinary `@function_tool` functions. Inside one, `shared_state().update(...)` merges top-level keys into the state and streams a `STATE_SNAPSHOT` to the browser before the tool's own result, so any component subscribed with `useAgent` re-renders while the agent is still running.

shared_state.py
    
    
    @function_tool
    def set_notes(notes: list[str]) -> str:
        """Replace the notes array in shared state with the full updated list.
    
        Use this tool whenever the user asks you to "remember" something, or
        when you have an observation about the user worth surfacing in the
        UI's notes panel. Always pass the FULL notes list (existing notes +
        any new ones), not a diff. Keep each note short (< 120 chars).
        """
        shared_state().update(notes=notes)
        return "Notes updated."
    
    

`shared_state().set(value)` replaces the whole state instead. The request's own `state` is never changed.

Inside an OpenAIAgentsAgent run

`OpenAIAgentsAgent` sets up `shared_state()` for every request. If you drive the SDK yourself with the adapter's translator, start the run inside `use_shared_state(SharedState(run_input.state))` and pass the same object to `to_agui`.

Subscribe a component to the agent's state with `useAgent`. Any time the agent mutates its state, for example via a tool call, the hook fires and your UI re-renders with the new values.

page.tsx
    
    
      // Subscribe the component to agent state changes. Any time the agent  // mutates its state (e.g. via its `set_notes` tool) this hook fires,  // we re-render, and the sidebar panels reflect the new values.  const { agent } = useAgent({    agentId: "shared-state-read-write",    updates: [UseAgentUpdate.OnStateChanged],  });

The returned `agent.state` is just a plain object. Read it like any other piece of React state and render the parts you care about: agent-written notes, structured outputs, progress indicators, anything the agent has put there.

## Writing agent state#

The same `agent` object exposes a `setState` setter. Calling it from a UI event handler pushes the new value into shared state, and the agent reads it back on its next turn. The UI's writes visibly steer the model.

page.tsx
    
    
      // WRITE: every edit in the sidebar goes straight into agent state.  // On the agent's next turn, its dynamic instructions show the model this  // state — so the UI's writes visibly steer the model.  const handlePreferencesChange = (next: Preferences) => {    agent.setState({      preferences: next,      notes, // preserve what the agent has written    } as RWAgentState);  };

This is what makes the channel two-way: the UI doesn't just observe the agent, it can hand the agent fresh inputs (preferences, selections, partial work) without going through the chat thread.

## Rendering shared state in the UI#

Because `agent.state` is plain React data, the UI layer is whatever you'd normally build. The demo on this page wires the agent's outputs into a small card component and feeds user edits back through `setState`.

notes-card.tsx
    
    
    // Read-side render: this card reflects the agent-authored `notes` slice// of shared state. The parent page passes `state.notes` in; we never// touch agent state ourselves — we just render it. The Clear button is// a small write-back, exposed as an `onClear` prop.export function NotesCard({ notes, onClear }: NotesCardProps) {  return (    <Card data-testid="notes-card" className="w-full">      <CardHeader>        <div className="flex items-start justify-between gap-3">          <div className="space-y-1.5">            <CardTitle>Agent Scratch pad</CardTitle>            <CardDescription>              The agent writes here via its{" "}              <code className="font-mono text-[11px] text-[#010507] dark:text-foreground">                set_notes              </code>{" "}              tool. The UI re-renders from shared state.            </CardDescription>          </div>          {notes.length > 0 && (            <Button              type="button"              onClick={onClear}              data-testid="notes-clear-button"              variant="destructive"              size="sm"              className="uppercase tracking-[0.14em] text-[10px]"            >              Clear            </Button>          )}        </div>      </CardHeader>      <CardContent>        {notes.length === 0 ? (          <div            data-testid="notes-empty"            className="text-sm text-[#838389] italic min-h-[160px] flex items-center justify-center text-center px-4 border border-dashed border-[#E9E9EF] rounded-xl bg-[#FAFAFC] dark:text-muted-foreground dark:border-border dark:bg-muted"          >            the agent will make observations about you and note them here!          </div>        ) : (          <ul            data-testid="notes-list"            className="space-y-2 text-sm text-[#010507] dark:text-foreground"          >            {notes.map((note, i) => (              <li                key={i}                data-testid="note-item"                className="flex gap-2 rounded-lg border border-[#E9E9EF] bg-[#FAFAFC] px-3 py-2 dark:border-border dark:bg-muted"              >                <span className="text-[#838389] font-mono text-xs leading-5 select-none dark:text-muted-foreground">                  {String(i + 1).padStart(2, "0")}                </span>                <span className="flex-1">{note}</span>              </li>            ))}          </ul>        )}      </CardContent>    </Card>  );}

Nothing about this is chat-specific: `useAgent` works in any component under `<CopilotKit>`, so you can render `agent.state` in your main view or canvas, not just inside the chat panel. See **[Render agent state in your app](https://docs.copilotkit.ai/openai-agents-python/shared-state/rendering-in-app)** for the full main-view pattern.

## Streaming partial state updates#

By default, agent state only updates _between_ backend checkpoints, so a long-running tool call appears as one big burst at the end. State streaming forwards a specific tool argument straight into a state key _as it's being generated_ , so the UI can watch the answer assemble token-by-token.

shared_state_streaming.py
    
    
    def _document_so_far(arguments: str) -> str | None:    """The ``document`` argument as far as the model has written it."""    try:        # Unfinished JSON: a string cut off mid-way is kept as it stands.        value = from_json(arguments, allow_partial="trailing-strings")    except ValueError:        return None    document = value.get("document") if isinstance(value, dict) else None    return document if isinstance(document, str) else Noneclass DocumentStreamingAgent(OpenAIAgentsAgent):    """Streams ``write_document``'s ``document`` argument into the state."""    async def run_streamed(self, input: RunAgentInput) -> AsyncIterator[BaseEvent]:        arguments: dict[str, str] = {}  # tool call id -> arguments so far        async with aclosing(super().run_streamed(input)) as events:            async for event in events:                yield event                if (                    event.type == EventType.TOOL_CALL_START                    and event.tool_call_name == write_document.name                ):                    arguments[event.tool_call_id] = ""                elif (                    event.type == EventType.TOOL_CALL_ARGS                    and event.tool_call_id in arguments                ):                    arguments[event.tool_call_id] += event.delta                    document = _document_so_far(arguments[event.tool_call_id])                    if document is not None:                        yield StateDeltaEvent(                            type=EventType.STATE_DELTA,                            delta=[                                {"op": "add", "path": "/document", "value": document}                            ],                        )

See **[State streaming](https://docs.copilotkit.ai/openai-agents-python/shared-state/streaming)** for the full walkthrough, including the corresponding `useAgent` subscription on the frontend.

## Read-only context#

When the value is **UI-owned** and the agent should read it but never write it back, such as current user, selected record, or scroll position, reach for `useAgentContext` instead of full shared state. It publishes values as a one-way UI-to-agent channel that auto-unregisters on unmount.

See **[Agent read-only context](https://docs.copilotkit.ai/openai-agents-python/shared-state/agent-readonly)** for the full pattern.

### On this page

What is shared state?When should I use this?Reading agent stateWriting agent stateRendering shared state in the UIStreaming partial state updatesRead-only context
