---
url: https://docs.copilotkit.ai/ag2/shared-state/
title: Shared State
method: scrapling+scrapegraph
fetched_at: 2026-11-26T12:11:31.268755+00:00
---

# Shared State

> Source: https://docs.copilotkit.ai/ag2/shared-state/

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

More detail: [Inspector](https://docs.copilotkit.ai/ag2/inspector).

## When should I use this?Copy Anchor Link

Use shared state when you want the agent and the user to collaborate through the same application state. The UI shows what the agent writes. The agent reads what the user changes in the UI.

[Building stateful agents?Persistent threads ship with CopilotKit Intelligence on the free Developer tier.Get CopilotKit Intelligence free](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=docs_shared_state&utm_frontend=react&utm_backend=ag2)

## Reading agent stateCopy Anchor Link

### Keep the state in conversation variablesCopy Anchor Link

On AG2, shared state is the agent's **conversation variables** (`context.variables`). `AGUIStream` syncs them in both directions, so you do not build state events yourself:

  * State that the UI writes with `agent.setState` arrives on `RunAgentInput.state` and merges into the variables for the run.
  * At the start of the run, `AGUIStream` sends a `STATE_SNAPSHOT` if the merged variables differ from the state the client sent.
  * At the end of the run, it sends another `STATE_SNAPSHOT` if a tool changed `context.variables`.



A snapshot replaces the client's state as a whole, so each one carries the client's keys and the server's variables together.

agent.py

Copy Text
    
    
    from typing import Annotated
    
    from fastapi import FastAPI, Header
    from fastapi.responses import StreamingResponse
    from pydantic import Field
    
    from ag2 import Agent, Context, tool
    from ag2.ag_ui import AGUIStream, RunAgentInput
    from ag2.config import OpenAIResponsesConfig
    
    @tool
    def set_language(
        language: Annotated[str, Field(description="language such as english or spanish")],
        context: Context,
    ) -> str:
        """Update the language in shared state."""
        context.variables["language"] = language.lower()
        return f"Language set to {language}"
    
    agent = Agent(
        name="assistant",
        prompt=(
            "You are a helpful assistant for tracking language. "
            "Always respond in the current language."
        ),
        config=OpenAIResponsesConfig(model="gpt-6-luna"),
        tools=[set_language],
    )
    
    stream = AGUIStream(agent)
    app = FastAPI()
    
    @app.post("/chat")
    async def run_agent(
        message: RunAgentInput,
        accept: str | None = Header(None),
    ) -> StreamingResponse:
        return StreamingResponse(
            stream.dispatch(message, accept=accept),
            media_type=accept or "text/event-stream",
        )

Everything in the variables is sent to the browser. Do not put secrets there. Pass them with `dispatch(dependencies=...)`, which never leaves the server.

### Do not seed state with `Agent(variables=...)`Copy Anchor Link

Agent variables take precedence over the incoming `RunAgentInput.state` on every run. A default set with `Agent(variables={"language": "english"})` overwrites whatever the UI wrote with `agent.setState`, and resets a value the agent changed on the previous turn. Nothing reports an error. Provide defaults in the UI instead, or with `context.variables.setdefault` inside a tool.

### Send intermediate snapshots from long toolsCopy Anchor Link

The automatic snapshots only arrive at the start and the end of a run. To update the UI while a long tool runs, send a snapshot from an async tool with `context.send`:

agent.py

Copy Text
    
    
    from ag_ui.core import StateSnapshotEvent
    
    from ag2 import Context, tool
    from ag2.ag_ui import AGUIEvent
    
    @tool
    async def long_running_task(context: Context) -> str:
        """A long task that streams state updates as it progresses."""
        for step in range(3):
            context.variables["progress"] = step
            await context.send(
                AGUIEvent(StateSnapshotEvent(snapshot=dict(context.variables)))
            )
        return "Done"

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

See [Programmatic control](https://docs.copilotkit.ai/ag2/programmatic-control) for more ways to run the agent from code.

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

Nothing about this is chat-specific: `useAgent` works in any component under `<CopilotKit>`, so you can render `agent.state` in your main view or canvas, not just inside the chat panel. See **[Render agent state in your app](https://docs.copilotkit.ai/ag2/shared-state/rendering-in-app)** for the full main-view pattern.

## Streaming partial state updatesCopy Anchor Link

By default, agent state only updates _between_ backend checkpoints, so a long-running tool call appears as one big burst at the end. State streaming copies one tool argument into a state key while the model writes it. The UI shows the answer token by token.

State streaming isn't available on this framework yet. The UI gets the agent's state between checkpoints.

## Read-only contextCopy Anchor Link

When the value is **UI-owned** and the agent should read it but never write it back, such as current user, selected record, or scroll position, reach for `useAgentContext` instead of full shared state. It publishes values as a one-way UI-to-agent channel that auto-unregisters on unmount.

See **[Agent read-only context](https://docs.copilotkit.ai/ag2/shared-state/agent-readonly)** for the full pattern.

How is this guide?

GoodBad

[Previous PageOpen Generative UI](https://docs.copilotkit.ai/ag2/generative-ui/open-generative-ui)[Next PageRender agent state in your app](https://docs.copilotkit.ai/ag2/shared-state/rendering-in-app)
