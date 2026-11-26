---
url: https://docs.copilotkit.ai/mastra/shared-state/
title: Shared State
method: scrapling+scrapegraph
fetched_at: 2026-11-26T12:11:24.878546+00:00
---

# Shared State

> Source: https://docs.copilotkit.ai/mastra/shared-state/

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

More detail: [Inspector](https://docs.copilotkit.ai/mastra/inspector).

## When should I use this?Copy Anchor Link

Use shared state when you want the agent and the user to collaborate through the same application state. The UI shows what the agent writes. The agent reads what the user changes in the UI.

[Building stateful agents?Persistent threads ship with CopilotKit Intelligence on the free Developer tier.Get CopilotKit Intelligence free](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=docs_shared_state&utm_frontend=react&utm_backend=mastra)

## Reading agent stateCopy Anchor Link

### Make the state your agent's working memoryCopy Anchor Link

On Mastra, the shared state is the agent's [working memory](https://mastra.ai/en/docs/memory/working-memory). Give the agent a `Memory` with working memory enabled and a Zod schema. The schema is the shape of `agent.state` in the UI.

src/mastra/agents/index.ts — state schema

Copy Text
    
    
    /**
     * Shared-state schema for the Shared State (Read + Write) demo.
     *
     * - `preferences` is WRITTEN by the UI via `agent.setState({ preferences })`.
     *   The AG-UI Mastra adapter merges `input.state` into the thread's
     *   `workingMemory` metadata before each run, so the LLM sees the latest UI
     *   preferences as part of working memory on every turn.
     * - `notes` is WRITTEN by the agent (via the `set_notes` tool) and READ by
     *   the UI via `useAgent({ updates: [OnStateChanged] })`. Mastra emits a
     *   `STATE_SNAPSHOT` after each run with the working-memory contents.
     */
    export const SharedStateRWAgentState = z.object({
      preferences: z
        .object({
          name: z.string().default(""),
          tone: z.enum(["formal", "casual", "playful"]).default("casual"),
          language: z.string().default("English"),
          interests: z.array(z.string()).default([]),
        })
        .default({
          name: "",
          tone: "casual",
          language: "English",
          interests: [],
        }),
      notes: z.array(z.string()).default([]),
    });

The AG-UI Mastra adapter merges the state that the UI writes with `agent.setState` into working memory before each run. After a run that changed working memory, it sends the new contents to the UI as a `STATE_SNAPSHOT`.

src/mastra/agents/index.ts — agent with working memory

Copy Text
    
    
    /**
     * Mastra agent backing the Shared State (Read + Write) demo.
     *
     * Bidirectional shared-state pattern:
     *   - UI -> agent: the UI writes `preferences` via `agent.setState(...)`.
     *     The AG-UI Mastra adapter merges that into working memory before each
     *     run, so the LLM reads it as part of its system context.
     *   - agent -> UI: the LLM calls `set_notes` to update the `notes` array.
     *     Mastra includes the `notes` field in its working-memory schema, so
     *     after each run the AG-UI adapter emits a `STATE_SNAPSHOT` and the UI
     *     re-renders.
     *
     * Note on the system prompt: rather than a static string, this is a
     * function so we can reaffirm — every turn — that the LLM should respect
     * whatever `preferences` are sitting in working memory. Mastra exposes
     * working memory to the LLM automatically; the prompt just nudges it to
     * actually USE those preferences instead of ignoring them.
     */
    export const sharedStateReadWriteAgent = new Agent({
      id: "shared-state-read-write",
      name: "Shared State Read+Write Agent",
      tools: { setNotesTool },
      model: openai("gpt-6-luna"),
      instructions: `You are a helpful, concise assistant wired to a UI that owns the user's preferences and an agent-authored notes panel.
    
    PREFERENCES (READ from working memory every turn):
    The UI writes a \`preferences\` object into shared state. It contains:
      - name: how to address the user
      - tone: "formal" | "casual" | "playful"
      - language: the language to reply in
      - interests: a list of topics the user cares about
    Always tailor your reply to these preferences. Address the user by name when one is set. Reply in their preferred language and tone. Lean on their interests when suggesting examples or topics.
    
    NOTES (WRITE via the \`set_notes\` tool):
    The UI also renders an "Agent notes" panel sourced from the \`notes\` array in shared state. Whenever the user asks you to remember something, OR when you make a useful observation about the user worth surfacing, call the \`set_notes\` tool with the FULL updated list of short note strings (existing notes + new ones). Always pass the entire list — never a diff. Keep each note short (< 120 chars).
    
    The \`set_notes\` tool persists the notes to working memory itself — you do NOT need to also call \`updateWorkingMemory\`. Just call \`set_notes\` and the UI will update.`,
      memory: new Memory({
        storage: new LibSQLStore({
          id: "shared-state-rw-agent-memory",
          url: WORKING_MEMORY_DB_URL,
        }),
        options: {
          workingMemory: {
            enabled: true,
            schema: SharedStateRWAgentState,
          },
        },
      }),
    });

### Tell the agent to use the stateCopy Anchor Link

Mastra shared state is prompt-driven. The model only acts on a value the UI wrote, or writes a value back, when its `instructions` tell it to. Name the state fields in `instructions` and say what to do with them, as the agent above does for `preferences` and `notes`.

The agent can write state with Mastra's built-in `updateWorkingMemory` tool. The demo's `set_notes` tool writes working memory itself, so the UI updates even when the model does not call `updateWorkingMemory`:

src/mastra/tools/shared-state-read-write.ts

Copy Text
    
    
    /**
     * Backend-side tool the LLM calls to update the `notes` slot in shared state.
     *
     * Mirrors the LangGraph-Python `set_notes` reference: the tool always receives
     * the FULL updated notes list (existing notes + any new ones).
     *
     * Determinism: this tool writes the new notes array to the agent's working
     * memory DIRECTLY (`writeNotesToWorkingMemory`), instead of relying on the
     * LLM to remember to call Mastra's `updateWorkingMemory` in addition to this
     * tool. The AG-UI Mastra adapter emits a `STATE_SNAPSHOT` event whenever
     * working memory changes, which drives the live re-render of the notes card —
     * so as long as the write here lands, the UI updates regardless of whether
     * the LLM remembers anything.
     *
     * The returned JSON is what the LLM sees: notes echoed back plus an
     * `updated: true` flag confirming the write attempt completed (best-effort —
     * see `working-memory.ts` for the failure semantics).
     */
    export const setNotesTool = createTool({
      id: "set_notes",
      description:
        "Replace the notes array in shared state with the FULL updated list of short note strings (existing notes + any new ones). Each note should be < 120 chars. Call this whenever the user asks you to remember something, or when you have an observation worth surfacing in the UI's notes panel. The tool persists the notes to working memory directly — you do not need to also call updateWorkingMemory.",
      inputSchema: z.object({
        notes: z
          .array(z.string())
          .describe(
            "Full updated notes list (existing notes plus any new ones). NOT a diff.",
          ),
      }),
      execute: async (inputData, executionContext) => {
        const notes = inputData.notes ?? [];
        await writeNotesToWorkingMemory(executionContext, notes);
        return JSON.stringify({ notes, updated: true as const });
      },
    });

`writeNotesToWorkingMemory` is the demo's helper in `src/mastra/tools/working-memory.ts`.

### Embed the agent in the runtimeCopy Anchor Link

Shared state works when the Mastra agent runs inside Copilot Runtime through `getLocalAgents` (or `getLocalAgent`):

app/api/copilotkit/[[...slug]]/route.ts

Copy Text
    
    
    const runtime = new CopilotRuntime({
      agents: MastraAgent.getLocalAgents({ mastra, resourceId: "user-1" }),
    });

It does **not** work through a remote Mastra agent from `MastraAgent.getRemoteAgents`. That bridge does not carry working memory, so the UI never receives the state and nothing reports an error.

### Use the agent's registered keyCopy Anchor Link

The `agentId` you pass to `useAgent` must exactly match the key the runtime registers the agent under. With `getLocalAgents`, that is the key in your Mastra `agents` map, for example `searchAgent` in `agents: { searchAgent }`.

Working memory starts empty. To show a default before the agent writes anything, set the missing value with `agent.setState` once `isReady` is true:

app/page.tsx

Copy Text
    
    
    import { useEffect } from "react";
    import { useAgent } from "@copilotkit/react-core/v2";
    import type { AgentState } from "@/mastra/agents/language-agent";
    
    // inside your component
    const { agent, isReady } = useAgent({ agentId: "languageAgent" });
    const state = (agent.state ?? {}) as Partial<AgentState>;
    
    useEffect(() => {
      if (!isReady || state.language !== undefined) return;
      agent.setState({ ...(agent.state ?? {}), language: "english" });
    }, [agent, isReady, state.language]);

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

See [Programmatic control](https://docs.copilotkit.ai/mastra/programmatic-control) for more ways to run the agent from code.

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

Nothing about this is chat-specific: `useAgent` works in any component under `<CopilotKit>`, so you can render `agent.state` in your main view or canvas, not just inside the chat panel. See **[Render agent state in your app](https://docs.copilotkit.ai/mastra/shared-state/rendering-in-app)** for the full main-view pattern.

## Streaming partial state updatesCopy Anchor Link

By default, agent state only updates _between_ backend checkpoints, so a long-running tool call appears as one big burst at the end. State streaming copies one tool argument into a state key while the model writes it. The UI shows the answer token by token.

index.ts

Copy Text
    
    
    /**
     * Mastra agent backing the Shared State (Streaming) demo.
     *
     * Per-token state streaming. When asked to write, draft, or revise text the
     * agent calls the built-in `updateWorkingMemory` tool with the FULL document
     * text under the `document` key. Because working memory is enabled with the
     * `SharedStateStreamingAgentState` schema, Mastra streams that tool call's
     * args as `tool-call-delta` frames; the AG-UI Mastra adapter accumulates
     * them, re-parses the growing prefix, and emits a leading `STATE_SNAPSHOT`
     * plus incremental `STATE_DELTA`s on `/document` (OSS-414). The frontend
     * renders `state.document` live as it fills in.
     *
     * NOTE: unlike `sharedStateReadWriteAgent`/`genUiAgent` (which use a custom
     * `set_*` tool that yields a single end-of-run `STATE_SNAPSHOT`), this demo
     * deliberately drives the built-in `updateWorkingMemory` tool — that is the
     * only path that streams progressive per-token deltas rather than one blob
     * at run end. So the prompt tells the model to write the document straight
     * into working memory instead of via a bespoke tool.
     */
    export const sharedStateStreamingAgent = new Agent({
      id: "shared-state-streaming",
      name: "Shared State Streaming Agent",
      tools: {},
      model: openai("gpt-6-luna"),
      instructions: `You are a collaborative writing assistant wired to a live Document panel.
    
    Whenever the user asks you to write, draft, revise, or explain anything of any length (a poem, an email, an essay, a summary, an explanation, etc.), you MUST call the \`updateWorkingMemory\` tool with the FULL content as a single string under the \`document\` field, e.g. { "document": "<the full text>" }.
    
    Rules:
      - NEVER paste the document body into a chat message. The document belongs in shared state — the UI renders it live from working memory as you stream it.
      - Always send the ENTIRE document in one \`updateWorkingMemory\` call (not a diff, not chunks across multiple calls).
      - After the document is written, reply with ONE short chat sentence confirming what you wrote (e.g. "Done — I've drafted your poem in the document panel."). Keep the document text itself out of that message.`,
      memory: new Memory({
        storage: new LibSQLStore({
          id: "shared-state-streaming-agent-memory",
          url: WORKING_MEMORY_DB_URL,
        }),
        options: {
          workingMemory: {
            enabled: true,
            schema: SharedStateStreamingAgentState,
          },
        },
      }),
    });

See **[State streaming](https://docs.copilotkit.ai/mastra/shared-state/streaming)** for the full walkthrough, including the corresponding `useAgent` subscription on the frontend.

## Read-only contextCopy Anchor Link

When the value is **UI-owned** and the agent should read it but never write it back, such as current user, selected record, or scroll position, reach for `useAgentContext` instead of full shared state. It publishes values as a one-way UI-to-agent channel that auto-unregisters on unmount.

See **[Agent read-only context](https://docs.copilotkit.ai/mastra/shared-state/agent-readonly)** for the full pattern.

How is this guide?

GoodBad

[Previous PageOpen Generative UI](https://docs.copilotkit.ai/mastra/generative-ui/open-generative-ui)[Next PageRender agent state in your app](https://docs.copilotkit.ai/mastra/shared-state/rendering-in-app)
