---
url: https://docs.copilotkit.ai/mastra/shared-state/streaming/
title: State Streaming
method: scrapling+scrapegraph
fetched_at: 2026-11-26T12:11:23.726986+00:00
---

# State Streaming

> Source: https://docs.copilotkit.ai/mastra/shared-state/streaming/

Shared state

# State Streaming

Stream partial agent state updates to the UI while a tool call is still running.

Copy MarkdownOpen

State Streaming

DemoCode

[](https://showcase-mastra-production.up.railway.app/demos/shared-state-streaming "Open in a new tab")[](https://github.com/CopilotKit/CopilotKit/tree/main/showcase/integrations/mastra/src/app/demos/shared-state-streaming "View the code on GitHub")

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

### Stream working memory through `updateWorkingMemory`Copy Anchor Link

Mastra has no streaming middleware to configure. When working memory is enabled, Mastra gives the agent a built-in `updateWorkingMemory` tool. During a run:

  1. The agent calls `updateWorkingMemory`.
  2. The AG-UI Mastra adapter reads the tool call's arguments while they stream.
  3. It sends one `STATE_SNAPSHOT`, then a `STATE_DELTA` for each new part, against the working-memory schema.
  4. `useAgent` renders again on each delta.



The field you stream is a key in the working-memory schema:

src/mastra/agents/index.ts — streamed state

Copy Text
    
    
    /**
     * Shared-state schema for the Shared State (Streaming) demo.
     *
     * `document` is streamed token-by-token into shared state as the agent
     * writes. Mastra parity for the LangGraph `StateStreamingMiddleware` /
     * predictive-state pattern: instead of a `write_document` tool whose arg is
     * forwarded per-token, this agent calls Mastra's built-in
     * `updateWorkingMemory` tool with the growing document. The AG-UI Mastra
     * adapter intercepts that tool call's STREAMING args (OSS-414) and emits a
     * leading `STATE_SNAPSHOT` followed by incremental `STATE_DELTA`s on the
     * `document` key, so `useAgent({ updates:[OnStateChanged] })` sees
     * `state.document` grow live.
     */
    export const SharedStateStreamingAgentState = z.object({
      document: z.string().default(""),
    });

### Tell the model to write into working memoryCopy Anchor Link

Only `updateWorkingMemory` streams. A custom tool that writes working memory sends a single `STATE_SNAPSHOT` when the run ends. So the prompt must make the model put the whole value in one `updateWorkingMemory` call, and keep it out of the chat message:

src/mastra/agents/index.ts — streaming agent

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

Register the agent in your `Mastra` instance. Its key in the `agents` map is the `agentId` the frontend uses.

### Embed the agent in the runtimeCopy Anchor Link

State streaming works only when the agent runs inside Copilot Runtime through `getLocalAgents`:

app/api/copilotkit/[[...slug]]/route.ts

Copy Text
    
    
    const runtime = new CopilotRuntime({
      agents: MastraAgent.getLocalAgents({ mastra, resourceId: "user-1" }),
    });

The working-memory snapshot at the end of the run replaces the streamed value, so any drift is corrected.

The backend pattern is always the same: map one streaming tool argument to one shared-state key. Each framework does this in its own way:

  * LangGraph Python: `StateStreamingMiddleware` with `StateItem(...)` entries.
  * LangGraph TypeScript: `copilotkitCustomizeConfig` with an `emitIntermediateState` mapping.
  * Direct SDK adapters: parse partial tool arguments in the streaming loop, and emit `STATE_SNAPSHOT` whenever the mapped value changes.
  * LlamaIndex and Pydantic AI: there is no per-token mapping. A backend tool sends a state snapshot after each step or tool call instead (see the setup above).



When the LLM streams that argument, CopilotKit writes every partial value into shared state before the tool even finishes executing.

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

A few things to note:

  * The state key must exist in your agent state (`document` in this demo).
  * The tool and argument names must match the exact LLM-facing tool call you want to forward (`write_document.document` here).
  * Streamed values are previews. When the step ends, the state the agent saves replaces them, so save the final value when the tool finishes. On CrewAI, LlamaIndex and Pydantic AI, write the final value to the agent state yourself, or it is overwritten when the step returns.



## The frontend: useAgent + OnStateChangedCopy Anchor Link

The UI side is the same as any other [shared-state](https://docs.copilotkit.ai/mastra/shared-state) subscription: `useAgent` with `OnStateChanged` gives you a reactive `agent.state`. Add `OnRunStatusChanged` if you want a "LIVE" / "done" indicator.

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

[Previous PageRender agent state in your app](https://docs.copilotkit.ai/mastra/shared-state/rendering-in-app)[Next PageAgent Read-Only Context](https://docs.copilotkit.ai/mastra/shared-state/agent-readonly)
