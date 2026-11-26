---
url: https://docs.copilotkit.ai/pydantic-ai/shared-state/
title: Shared State
method: scrapling+scrapegraph
fetched_at: 2026-11-26T12:11:21.148974+00:00
---

# Shared State

> Source: https://docs.copilotkit.ai/pydantic-ai/shared-state/

Shared state

# Shared State

Create a two-way connection between your UI and agent state.

Copy MarkdownOpen

## What is shared state?Copy Anchor Link

Agentic Copilots maintain a shared state that connects your UI with the agent's execution. This shared state lets you:

  * Display the agent's current progress and intermediate results
  * Update the agent's state through UI interactions
  * React to state changes in real-time across your application

![Shared State Demo](https://cdn.copilotkit.ai/docs/copilotkit/images/coagents/SharedStateCoAgents.gif)

See this in Inspector

Open Inspector on localhost. Go to **Inspect** , then **Agent**. The **Current State** section shows the agent state as the run proceeds. With Intelligence on, you can also open a thread in **Rich Threads** and click **State** to see its saved state.

More detail: [Inspector](https://docs.copilotkit.ai/pydantic-ai/inspector).

## When should I use this?Copy Anchor Link

Use shared state when you want the agent and the user to collaborate through the same application state. The UI shows what the agent writes. The agent reads what the user changes in the UI.

[Building stateful agents?Persistent threads ship with CopilotKit Intelligence on the free Developer tier.Get CopilotKit Intelligence free](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=docs_shared_state&utm_frontend=react&utm_backend=pydantic-ai)

## Reading agent stateCopy Anchor Link

### Type the agent's deps with `StateDeps`Copy Anchor Link

Declare the shared state as a Pydantic model and set `deps_type=StateDeps[YourState]`. The AG-UI adapter writes the state the UI sent into `ctx.deps.state` at the start of every run.

src/agents/shared_state_read_write.py

Copy Text
    
    
    from pydantic import BaseModel, Field
    from pydantic_ai import Agent, RunContext
    from pydantic_ai.ui import StateDeps
    from pydantic_ai.models.openai import OpenAIResponsesModel
    
    
    class Preferences(BaseModel):
        name: str = ""
        tone: str = "casual"
        language: str = "English"
        interests: list[str] = Field(default_factory=list)
    
    
    class SharedStateRWState(BaseModel):
        preferences: Preferences = Field(default_factory=Preferences)
        notes: list[str] = Field(default_factory=list)
    
    
    agent = Agent(
        model=OpenAIResponsesModel("gpt-6-luna"),
        deps_type=StateDeps[SharedStateRWState],
        system_prompt=_BASE_SYSTEM_PROMPT,
    )

### Read what the UI wroteCopy Anchor Link

A dynamic system prompt reads `ctx.deps.state` on every turn, so values the UI writes with `agent.setState` steer the model:

src/agents/shared_state_read_write.py

Copy Text
    
    
    @agent.system_prompt
    def _inject_preferences(
        ctx: RunContext[StateDeps[SharedStateRWState]],
    ) -> str:
        block = _build_prefs_block(ctx.deps.state.preferences)
        return block or ""

### Write state from a toolCopy Anchor Link

Change `ctx.deps.state`, then return a `StateSnapshotEvent` so the UI receives the new state as soon as the tool returns. Serialize the model with `model_dump()`:

src/agents/shared_state_read_write.py

Copy Text
    
    
    from ag_ui.core import EventType, StateSnapshotEvent
    
    
    @agent.tool
    async def set_notes(
        ctx: RunContext[StateDeps[SharedStateRWState]],
        notes: list[str],
    ) -> StateSnapshotEvent:
        """Replace the notes array in shared state with the full updated list."""
        ctx.deps.state.notes = list(notes)
        return StateSnapshotEvent(
            type=EventType.STATE_SNAPSHOT,
            snapshot=ctx.deps.state.model_dump(),
        )

### Build the deps fresh on every requestCopy Anchor Link

The adapter writes the client's state into `deps.state`, so a shared `StateDeps` instance leaks state between concurrent requests and users:

agent.py

Copy Text
    
    
    from pydantic_ai.ui.ag_ui import AGUIAdapter
    from starlette.applications import Starlette
    from starlette.requests import Request
    from starlette.responses import Response
    from starlette.routing import Route
    
    
    async def run_agent(request: Request) -> Response:
        return await AGUIAdapter.dispatch_request(
            request, agent=agent, deps=StateDeps(SharedStateRWState())
        )
    
    
    app = Starlette(routes=[Route("/", run_agent, methods=["POST"])])

Subscribe a component to the agent's state with `useAgent`. Any time the agent mutates its state, for example via a tool call, the hook fires and your UI re-renders with the new values.

page.tsx

Copy Text
    
    
      // Subscribe the component to agent state changes. Any time the agent
      // mutates its state (e.g. via its `set_notes` tool) this hook fires,
      // we re-render, and the sidebar panels reflect the new values.
      const { agent } = useAgent({
        agentId: "shared-state-read-write",
        updates: [UseAgentUpdate.OnStateChanged],
      });

The returned `agent.state` is just a plain object. Read it like any other piece of React state and render the parts you care about: agent-written notes, structured outputs, progress indicators, anything the agent has put there.

## Writing agent stateCopy Anchor Link

The same `agent` object exposes a `setState` setter. Calling it from a UI event handler pushes the new value into shared state, and the agent reads it back on its next turn. The UI's writes visibly steer the model.

page.tsx

Copy Text
    
    
      // WRITE: every edit in the sidebar goes straight into agent state.
      // On the agent's next turn, `PreferencesInjectorMiddleware` reads this
      // back out of state and adds it to the system prompt — so the UI's
      // writes visibly steer the model.
      const handlePreferencesChange = (next: Preferences) => {
        agent.setState({
          preferences: next,
          notes, // preserve what the agent has written
        } as RWAgentState);
      };

This makes shared state two-way. The UI can also send the agent new inputs, such as preferences, selections, or partial work. These inputs do not go through the chat.

The agent reads the new state on its next run. To run it right away, call `copilotkit.runAgent({ agent })` (from `useCopilotKit`) after `setState`. Running through `copilotkit` also sends your frontend tools and context with the run. To tell the model what changed, add a hint message first:

Copy Text
    
    
    const { copilotkit } = useCopilotKit();
    
    agent.setState({ language: newLanguage });
    agent.addMessage({
      id: crypto.randomUUID(),
      role: "user",
      content: `the language has been updated to ${newLanguage}`,
    });
    await copilotkit.runAgent({ agent });

See [Programmatic control](https://docs.copilotkit.ai/pydantic-ai/programmatic-control) for more ways to run the agent from code.

## Rendering shared state in the UICopy Anchor Link

Because `agent.state` is plain React data, the UI layer is whatever you'd normally build. The demo on this page wires the agent's outputs into a small card component and feeds user edits back through `setState`.

notes-card.tsx

Copy Text
    
    
    // Read-side render: this card reflects the agent-authored `notes` slice
    // of shared state. The parent page passes `state.notes` in; we never
    // touch agent state ourselves — we just render it. The Clear button is
    // a small write-back, exposed as an `onClear` prop.
    export function NotesCard({ notes, onClear }: NotesCardProps) {
      return (
        <Card data-testid="notes-card" className="w-full">
          <CardHeader>
            <div className="flex items-start justify-between gap-3">
              <div className="space-y-1.5">
                <CardTitle>Agent Scratch pad</CardTitle>
                <CardDescription>
                  The agent writes here via its{" "}
                  <code className="font-mono text-[11px] text-[#010507] dark:text-foreground">
                    set_notes
                  </code>{" "}
                  tool. The UI re-renders from shared state.
                </CardDescription>
              </div>
              {notes.length > 0 && (
                <Button
                  type="button"
                  onClick={onClear}
                  data-testid="notes-clear-button"
                  variant="destructive"
                  size="sm"
                  className="uppercase tracking-[0.14em] text-[10px]"
                >
                  Clear
                </Button>
              )}
            </div>
          </CardHeader>
    
          <CardContent>
            {notes.length === 0 ? (
              <div
                data-testid="notes-empty"
                className="text-sm text-[#838389] italic min-h-[160px] flex items-center justify-center text-center px-4 border border-dashed border-[#E9E9EF] rounded-xl bg-[#FAFAFC] dark:text-muted-foreground dark:border-border dark:bg-muted"
              >
                the agent will make observations about you and note them here!
              </div>
            ) : (
              <ul
                data-testid="notes-list"
                className="space-y-2 text-sm text-[#010507] dark:text-foreground"
              >
                {notes.map((note, i) => (
                  <li
                    key={i}
                    data-testid="note-item"
                    className="flex gap-2 rounded-lg border border-[#E9E9EF] bg-[#FAFAFC] px-3 py-2 dark:border-border dark:bg-muted"
                  >
                    <span className="text-[#838389] font-mono text-xs leading-5 select-none dark:text-muted-foreground">
                      {String(i + 1).padStart(2, "0")}
                    </span>
                    <span className="flex-1">{note}</span>
                  </li>
                ))}
              </ul>
            )}
          </CardContent>
        </Card>
      );
    }

Nothing about this is chat-specific: `useAgent` works in any component under `<CopilotKit>`, so you can render `agent.state` in your main view or canvas, not just inside the chat panel. See **[Render agent state in your app](https://docs.copilotkit.ai/pydantic-ai/shared-state/rendering-in-app)** for the full main-view pattern.

## Streaming partial state updatesCopy Anchor Link

By default, agent state only updates _between_ backend checkpoints, so a long-running tool call appears as one big burst at the end. State streaming copies one tool argument into a state key while the model writes it. The UI shows the answer token by token.

State streaming isn't available on this framework yet. The UI gets the agent's state between checkpoints.

## Read-only contextCopy Anchor Link

When the value is **UI-owned** and the agent should read it but never write it back, such as current user, selected record, or scroll position, reach for `useAgentContext` instead of full shared state. It publishes values as a one-way UI-to-agent channel that auto-unregisters on unmount.

See **[Agent read-only context](https://docs.copilotkit.ai/pydantic-ai/shared-state/agent-readonly)** for the full pattern.

How is this guide?

GoodBad

[Previous PageOpen Generative UI](https://docs.copilotkit.ai/pydantic-ai/generative-ui/open-generative-ui)[Next PageRender agent state in your app](https://docs.copilotkit.ai/pydantic-ai/shared-state/rendering-in-app)
