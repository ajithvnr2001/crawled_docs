---
url: https://docs.copilotkit.ai/ms-agent-dotnet/shared-state/
title: Shared State
method: scrapling+scrapegraph
fetched_at: 2026-11-26T12:11:23.495962+00:00
---

# Shared State

> Source: https://docs.copilotkit.ai/ms-agent-dotnet/shared-state/

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

More detail: [Inspector](https://docs.copilotkit.ai/ms-agent-dotnet/inspector).

## When should I use this?Copy Anchor Link

Use shared state when you want the agent and the user to collaborate through the same application state. The UI shows what the agent writes. The agent reads what the user changes in the UI.

[Building stateful agents?Persistent threads ship with CopilotKit Intelligence on the free Developer tier.Get CopilotKit Intelligence free](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=docs_shared_state&utm_frontend=react&utm_backend=ms-agent-dotnet)

## Reading agent stateCopy Anchor Link

### Map JSON content to a state snapshotCopy Anchor Link

A .NET agent publishes state as a `DataContent` update with the `application/json` media type. The `MapContent` mapping on `AGUIStreamOptions` is what turns that content into a `STATE_SNAPSHOT` event for the frontend. Register it next to `AddAGUIServer`:

Program.cs

Copy Text
    
    
    using System.Text.Json;
    using AGUI.Abstractions;
    using AGUI.Server;
    using Microsoft.Extensions.AI;
    
    var builder = WebApplication.CreateBuilder(args);
    builder.Services.AddAGUIServer();
    // Turn the wrapper's JSON DataContent into a STATE_SNAPSHOT event
    builder.Services.Configure<AGUIStreamOptions>(options => options.MapContent(content =>
    {
        if (content is not DataContent { MediaType: "application/json" } data) return null;
        try
        {
            using var document = JsonDocument.Parse(data.Data);
            return [new StateSnapshotEvent { Snapshot = document.RootElement.Clone() }];
        }
        catch (JsonException)
        {
            return null;
        }
    }));
    var app = builder.Build();

### Read and write state in an agent wrapperCopy Anchor Link

Wrap your agent in a `DelegatingAIAgent`. The state the UI sent arrives on the AG-UI request, which `TryGetRunAgentInput` recovers from the chat options. To update the UI, yield the new state as JSON `DataContent`:

Program.cs (excerpt)

Copy Text
    
    
    internal sealed class StateStreamingAgent : DelegatingAIAgent
    {
        // ...
    
        protected override async IAsyncEnumerable<AgentResponseUpdate> RunCoreStreamingAsync(
            IEnumerable<AIChatMessage> messages,
            AgentSession? session = null,
            AgentRunOptions? options = null,
            [EnumeratorCancellation] CancellationToken cancellationToken = default)
        {
            // Recover the state sent in the AG-UI request
            JsonElement? currentState = null;
            if (options is ChatClientAgentRunOptions { ChatOptions: { } chatOptions } &&
                chatOptions.TryGetRunAgentInput(out RunAgentInput? input) &&
                input?.State is { ValueKind: JsonValueKind.Object } state)
            {
                currentState = state;
            }
    
            // ... run the inner agent and build the new state snapshot
    
            byte[] stateBytes = JsonSerializer.SerializeToUtf8Bytes(
                parsedStateSnapshot,
                this._jsonSerializerOptions.GetTypeInfo(typeof(JsonElement)));
    
            // Emit state snapshot as DataContent
            yield return new AgentResponseUpdate
            {
                Contents = [new DataContent(stateBytes, "application/json")]
            };
        }
    }

For a full agent that does this, see [`SharedStateAgent.cs`](https://github.com/CopilotKit/CopilotKit/blob/main/showcase/integrations/ms-agent-dotnet/agent/SharedStateAgent.cs), or the [SharedStateAgent sample](https://github.com/microsoft/agent-framework/blob/main/dotnet/samples/05-end-to-end/AGUIClientServer/AGUIDojoServer/SharedState/SharedStateAgent.cs) in the Agent Framework repository.

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

See [Programmatic control](https://docs.copilotkit.ai/ms-agent-dotnet/programmatic-control) for more ways to run the agent from code.

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

Nothing about this is chat-specific: `useAgent` works in any component under `<CopilotKit>`, so you can render `agent.state` in your main view or canvas, not just inside the chat panel. See **[Render agent state in your app](https://docs.copilotkit.ai/ms-agent-dotnet/shared-state/rendering-in-app)** for the full main-view pattern.

## Streaming partial state updatesCopy Anchor Link

By default, agent state only updates _between_ backend checkpoints, so a long-running tool call appears as one big burst at the end. State streaming copies one tool argument into a state key while the model writes it. The UI shows the answer token by token.

Missing snippet

Region `state-streaming-middleware` not found in `ms-agent-dotnet::shared-state-streaming`. Tag the source lines with `// @region[state-streaming-middleware]` / `// @endregion[state-streaming-middleware]`.Available: frontend-use-coagent-state

See **[State streaming](https://docs.copilotkit.ai/ms-agent-dotnet/shared-state/streaming)** for the full walkthrough, including the corresponding `useAgent` subscription on the frontend.

## Read-only contextCopy Anchor Link

When the value is **UI-owned** and the agent should read it but never write it back, such as current user, selected record, or scroll position, reach for `useAgentContext` instead of full shared state. It publishes values as a one-way UI-to-agent channel that auto-unregisters on unmount.

See **[Agent read-only context](https://docs.copilotkit.ai/ms-agent-dotnet/shared-state/agent-readonly)** for the full pattern.

How is this guide?

GoodBad

[Previous PageOpen Generative UI](https://docs.copilotkit.ai/ms-agent-dotnet/generative-ui/open-generative-ui)[Next PageRender agent state in your app](https://docs.copilotkit.ai/ms-agent-dotnet/shared-state/rendering-in-app)
