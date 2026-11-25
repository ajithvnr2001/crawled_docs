---
url: https://docs.copilotkit.ai/strands-typescript/shared-state/
title: Shared State
method: scrapling+scrapegraph
fetched_at: 2026-11-25T12:31:17.308607+00:00
---

# Shared State

> Source: https://docs.copilotkit.ai/strands-typescript/shared-state/

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

More detail: [Inspector](https://docs.copilotkit.ai/strands-typescript/inspector).

## When should I use this?Copy Anchor Link

Use shared state when you want the agent and the user to collaborate through the same application state. The UI shows what the agent writes. The agent reads what the user changes in the UI.

[Building stateful agents?Persistent threads ship with CopilotKit Intelligence on the free Developer tier.Get CopilotKit Intelligence free](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=docs_shared_state&utm_frontend=react&utm_backend=strands-typescript)

## Reading agent stateCopy Anchor Link

Shared state in Strands is prompt-driven

A Strands agent knows only the state that your code copies into its request context. A state key you don't copy never reaches the model, and nothing reports it: the agent answers as if the UI had written nothing. Say in your system prompt what each copied value means.

### Copy UI state into the request contextCopy Anchor Link

The UI writes state with `agent.setState`, and it arrives on the AG-UI run input as `inputData.state`. Copy the parts the model needs into a copy of the run's `context`. The adapter shows that context to the model during the run without saving it as user text:

src/agent/state.ts

Copy Text
    
    
    export function withStateContext(inputData: RunAgentInput): RunAgentInput {
      const state =
        inputData.state && typeof inputData.state === "object"
          ? (inputData.state as Record<string, unknown>)
          : {};
      const context = [...inputData.context];
      const preferences = formatPreferencesBlock(state.preferences);
      if (preferences) {
        context.push({
          description: "Current user preferences",
          value: preferences,
        });
      }
      if ("todos" in state) {
        context.push({
          description: "Current sales pipeline",
          value: JSON.stringify(state.todos, null, 2),
        });
      }
      return { ...inputData, context };
    }

### Apply it before every runCopy Anchor Link

Subclass the agent so every request, including tool continuations, passes through `withStateContext`:

src/agent/agent.ts

Copy Text
    
    
    export class ShowcaseStrandsAgent extends BoardStateStrandsAgent {
      override async *run(inputData: RunAgentInput) {
        // The adapter exposes context during model calls and restores history afterward.
        yield* super.run(withStateContext(inputData));
      }
    }

Do not use `stateContextBuilder` to prepend the state to the user's message. Its output is saved as native message history, so every past message keeps the old state. Existing conversations created that way keep that text; start a new conversation for a clean history.

### Send agent writes back to the UICopy Anchor Link

The agent writes state through a tool. Give the tool a `stateFromArgs` behavior, and the adapter emits a state snapshot the moment the tool fires, so the UI re-renders without waiting for the text response:

src/agent/agent.ts

Copy Text
    
    
    import type { StrandsAgentConfig } from "@ag-ui/aws-strands";
    import { notesStateFromArgs } from "./state";
    
    const config: StrandsAgentConfig = {
      toolBehaviors: {
        // Shared State (Read + Write) — notes panel.
        set_notes: { stateFromArgs: notesStateFromArgs },
      },
    };

src/agent/state.ts

Copy Text
    
    
    export async function notesStateFromArgs(
      ctx: ToolCallContext,
    ): Promise<StatePayload | null> {
      const input = parseToolInput(ctx.toolInput);
      let notes: unknown;
      if (input && typeof input === "object" && !Array.isArray(input)) {
        notes = (input as Record<string, unknown>).notes;
      } else if (Array.isArray(input)) {
        notes = input;
      }
      if (!Array.isArray(notes)) return null;
      return { notes: notes.map((n) => String(n)) };
    }

`parseToolInput` parses the call's input when it arrives as a JSON string. Pass `config` to `ShowcaseStrandsAgent` with your Strands `Agent`.

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

See [Programmatic control](https://docs.copilotkit.ai/strands-typescript/programmatic-control) for more ways to run the agent from code.

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

Nothing about this is chat-specific: `useAgent` works in any component under `<CopilotKit>`, so you can render `agent.state` in your main view or canvas, not just inside the chat panel. See **[Render agent state in your app](https://docs.copilotkit.ai/strands-typescript/shared-state/rendering-in-app)** for the full main-view pattern.

## Streaming partial state updatesCopy Anchor Link

By default, agent state only updates _between_ backend checkpoints, so a long-running tool call appears as one big burst at the end. State streaming copies one tool argument into a state key while the model writes it. The UI shows the answer token by token.

State streaming isn't available on this framework yet. The UI gets the agent's state between checkpoints.

## Read-only contextCopy Anchor Link

When the value is **UI-owned** and the agent should read it but never write it back, such as current user, selected record, or scroll position, reach for `useAgentContext` instead of full shared state. It publishes values as a one-way UI-to-agent channel that auto-unregisters on unmount.

See **[Agent read-only context](https://docs.copilotkit.ai/strands-typescript/shared-state/agent-readonly)** for the full pattern.

How is this guide?

GoodBad

[Previous PageOpen Generative UI](https://docs.copilotkit.ai/strands-typescript/generative-ui/open-generative-ui)[Next PageRender agent state in your app](https://docs.copilotkit.ai/strands-typescript/shared-state/rendering-in-app)
