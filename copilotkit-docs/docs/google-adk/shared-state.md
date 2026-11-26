---
url: https://docs.copilotkit.ai/google-adk/shared-state/
title: Shared State
method: scrapling+scrapegraph
fetched_at: 2026-11-26T12:11:26.463437+00:00
---

# Shared State

> Source: https://docs.copilotkit.ai/google-adk/shared-state/

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

More detail: [Inspector](https://docs.copilotkit.ai/google-adk/inspector).

## When should I use this?Copy Anchor Link

Use shared state when you want the agent and the user to collaborate through the same application state. The UI shows what the agent writes. The agent reads what the user changes in the UI.

[Building stateful agents?Persistent threads ship with CopilotKit Intelligence on the free Developer tier.Get CopilotKit Intelligence free](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=docs_shared_state&utm_frontend=react&utm_backend=google-adk)

## Reading agent stateCopy Anchor Link

### Install the ADK + AG-UI bridgeCopy Anchor Link

Copy Text
    
    
    pip install ag-ui-adk

### Add `AGUIToolset()` to your agentCopy Anchor Link

Shared state in ADK lives in `tool_context.state` — your tools write to it directly and the runtime forwards updates to the UI. Wire your `LlmAgent` with `AGUIToolset()` and CopilotKit takes care of the rest.

shared_state_read_write_agent.py

Copy Text
    
    
    shared_state_read_write_agent = LlmAgent(
        name="SharedStateReadWriteAgent",
        model=get_model(),
        instruction=_INSTRUCTION,
        tools=[set_notes, AGUIToolset()],
        before_model_callback=_inject_preferences,
        after_model_callback=stop_on_terminal_text,
    )

See `src/agents/shared_state_read_write_agent.py` for the bidirectional pattern: a before-model callback reads UI-authored preferences out of session state, and a `set_notes` tool writes agent-authored notes back.

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
      // On the agent's next turn, `_inject_preferences` reads this back out
      // of state and prepends a preferences SystemMessage — so the UI's
      // writes visibly steer the model.
      const handlePreferencesChange = (next: Preferences) => {
        agent.setState({
          ...(agentState as object | undefined),
          preferences: next,
          notes: agentState?.notes ?? [],
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

See [Programmatic control](https://docs.copilotkit.ai/google-adk/programmatic-control) for more ways to run the agent from code.

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

Nothing about this is chat-specific: `useAgent` works in any component under `<CopilotKit>`, so you can render `agent.state` in your main view or canvas, not just inside the chat panel. See **[Render agent state in your app](https://docs.copilotkit.ai/google-adk/shared-state/rendering-in-app)** for the full main-view pattern.

## Streaming partial state updatesCopy Anchor Link

By default, agent state only updates _between_ backend checkpoints, so a long-running tool call appears as one big burst at the end. State streaming copies one tool argument into a state key while the model writes it. The UI shows the answer token by token.

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
    

See **[State streaming](https://docs.copilotkit.ai/google-adk/shared-state/streaming)** for the full walkthrough, including the corresponding `useAgent` subscription on the frontend.

## Read-only contextCopy Anchor Link

When the value is **UI-owned** and the agent should read it but never write it back, such as current user, selected record, or scroll position, reach for `useAgentContext` instead of full shared state. It publishes values as a one-way UI-to-agent channel that auto-unregisters on unmount.

See **[Agent read-only context](https://docs.copilotkit.ai/google-adk/shared-state/agent-readonly)** for the full pattern.

How is this guide?

GoodBad

[Previous PageOpen Generative UI](https://docs.copilotkit.ai/google-adk/generative-ui/open-generative-ui)[Next PageRender agent state in your app](https://docs.copilotkit.ai/google-adk/shared-state/rendering-in-app)
