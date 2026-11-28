---
url: https://docs.copilotkit.ai/strands/shared-state/
title: Shared State
method: scrapling+scrapegraph
fetched_at: 2026-11-28T11:35:18.594774+00:00
---

# Shared State

> Source: https://docs.copilotkit.ai/strands/shared-state/

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

More detail: [Inspector](https://docs.copilotkit.ai/strands/inspector).

## When should I use this?Copy Anchor Link

Use shared state when you want the agent and the user to collaborate through the same application state. The UI shows what the agent writes. The agent reads what the user changes in the UI.

[Building stateful agents?Persistent threads ship with CopilotKit Intelligence on the free Developer tier.Get CopilotKit Intelligence free](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=docs_shared_state&utm_frontend=react&utm_backend=strands)

## Reading agent stateCopy Anchor Link

Shared state in Strands is prompt-driven

A Strands agent knows only the state that your code copies into its request context. A state key you don't copy never reaches the model, and nothing reports it: the agent answers as if the UI had written nothing. Say in your system prompt what each copied value means.

### Copy UI state into the request contextCopy Anchor Link

The UI writes state with `agent.setState`, and it arrives on the AG-UI run input as `input_data.state`. Copy the parts the model needs into the run's `context`. The adapter shows that context to the model during the run and restores the native history afterward, including on tool continuations:

src/agents/agent.py

Copy Text
    
    
    from ag_ui.core.types import Context
    
    
    def with_state_context(input_data):
        """Copy current UI state into transient AG-UI context, preserving user text.
    
        The adapter supplies context during model calls and restores native history
        afterward, including tool continuations. Never use state_context_builder to
        prepend application instructions to durable user messages.
        """
        context = list(input_data.context)
        state = input_data.state
        if isinstance(state, dict):
            preferences = _format_preferences_block(state.get("preferences") or {})
            if preferences:
                context.append(
                    Context(description="Current user preferences", value=preferences)
                )
        return input_data.model_copy(update={"context": context})

`_format_preferences_block` turns the `preferences` object into a short text block for the prompt. Format your own keys the same way.

### Apply it before every runCopy Anchor Link

Wrap the `StrandsAgent` so every request, including tool continuations, passes through `with_state_context`:

src/agents/agent.py

Copy Text
    
    
    from collections.abc import AsyncIterator
    from contextlib import aclosing
    from typing import Any
    
    from ag_ui_strands import StrandsAgent
    
    
    class _StateContextWrapper:
        """Add transient state context and preserve the adapter's event stream."""
    
        def __init__(self, delegate: StrandsAgent) -> None:
            self._delegate = delegate
    
        def __getattr__(self, name: str) -> Any:
            return getattr(self._delegate, name)
    
        async def run(self, input_data: Any) -> AsyncIterator[Any]:
            # The adapter owns snapshots, including unfinished parallel calls.
            async with aclosing(
                self._delegate.run(with_state_context(input_data))
            ) as events:
                async for event in events:
                    yield event

Do not use `StrandsAgentConfig(state_context_builder=...)` to prepend the state to the user's message. Its output is saved as native message history, so every past message keeps the old state. Existing conversations created that way keep that text; start a new conversation for a clean history.

### Send agent writes back to the UICopy Anchor Link

The agent writes state through a tool. Give the tool a `ToolBehavior` with `state_from_args`, and the adapter emits a state snapshot the moment the tool fires, so the UI re-renders without waiting for the text response:

src/agents/agent.py

Copy Text
    
    
    from ag_ui_strands import StrandsAgent, StrandsAgentConfig, ToolBehavior
    from strands import tool
    
    
    @tool
    def set_notes(notes: list[str]):
        """Replace the notes array in shared state with the full updated list.
    
        Use this whenever the user asks you to remember something, or when
        you have an observation about the user worth surfacing in the UI's
        notes panel. ALWAYS pass the FULL notes list (existing notes + any
        new ones), not a diff. Keep each note short (< 120 chars).
    
        Args:
            notes: The complete updated list of short note strings.
    
        Returns:
            Confirmation string for the LLM to summarise back to the user.
        """
        return f"Notes updated. Tracking {len(notes)} note(s)."
    
    
    shared_state_config = StrandsAgentConfig(
        tool_behaviors={
            "set_notes": ToolBehavior(
                state_from_args=notes_state_from_args,
            ),
        },
    )

`notes_state_from_args` reads the call's `tool_input` (a JSON string or a dict) and returns `{"notes": [...]}`, the snapshot the adapter publishes. Pass `shared_state_config` as `config=` to `StrandsAgent`, then wrap that agent in `_StateContextWrapper`.

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

See [Programmatic control](https://docs.copilotkit.ai/strands/programmatic-control) for more ways to run the agent from code.

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

Nothing about this is chat-specific: `useAgent` works in any component under `<CopilotKit>`, so you can render `agent.state` in your main view or canvas, not just inside the chat panel. See **[Render agent state in your app](https://docs.copilotkit.ai/strands/shared-state/rendering-in-app)** for the full main-view pattern.

## Streaming partial state updatesCopy Anchor Link

By default, agent state only updates _between_ backend checkpoints, so a long-running tool call appears as one big burst at the end. State streaming copies one tool argument into a state key while the model writes it. The UI shows the answer token by token.

State streaming isn't available on this framework yet. The UI gets the agent's state between checkpoints.

## Read-only contextCopy Anchor Link

When the value is **UI-owned** and the agent should read it but never write it back, such as current user, selected record, or scroll position, reach for `useAgentContext` instead of full shared state. It publishes values as a one-way UI-to-agent channel that auto-unregisters on unmount.

See **[Agent read-only context](https://docs.copilotkit.ai/strands/shared-state/agent-readonly)** for the full pattern.

How is this guide?

GoodBad

[Previous PageOpen Generative UI](https://docs.copilotkit.ai/strands/generative-ui/open-generative-ui)[Next PageRender agent state in your app](https://docs.copilotkit.ai/strands/shared-state/rendering-in-app)
