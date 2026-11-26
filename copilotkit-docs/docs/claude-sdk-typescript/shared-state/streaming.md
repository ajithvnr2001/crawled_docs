---
url: https://docs.copilotkit.ai/claude-sdk-typescript/shared-state/streaming/
title: State Streaming
method: scrapling+scrapegraph
fetched_at: 2026-11-26T12:11:30.708211+00:00
---

# State Streaming

> Source: https://docs.copilotkit.ai/claude-sdk-typescript/shared-state/streaming/

Shared state

# State Streaming

Stream partial agent state updates to the UI while a tool call is still running.

Copy MarkdownOpen

State Streaming

DemoCode

[](https://showcase-claude-sdk-typescript-production.up.railway.app/demos/shared-state-streaming "Open in a new tab")[](https://github.com/CopilotKit/CopilotKit/tree/main/showcase/integrations/claude-sdk-typescript/src/app/demos/shared-state-streaming "View the code on GitHub")

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

### Stream partial state updates while Claude respondsCopy Anchor Link

For streaming state, parse the agent's structured deltas as they arrive and emit CopilotKit state updates before the final message is complete. This branch runs inside the streamed tool-argument handler.

agent_server.ts

Copy Text
    
    
                    if (activeToolCallName === "write_document") {
                      const streamedDocument = partialJsonStringProperty(
                        activeToolArgs,
                        "document",
                      );
                      if (
                        streamedDocument !== null &&
                        streamedDocument !== lastStreamedDocument
                      ) {
                        state = { ...state, document: streamedDocument };
                        lastStreamedDocument = streamedDocument;
                        emit({ type: EventType.STATE_SNAPSHOT, snapshot: state });
                      }
                    }

The backend pattern is always the same: map one streaming tool argument to one shared-state key. Each framework does this in its own way:

  * LangGraph Python: `StateStreamingMiddleware` with `StateItem(...)` entries.
  * LangGraph TypeScript: `copilotkitCustomizeConfig` with an `emitIntermediateState` mapping.
  * Direct SDK adapters: parse partial tool arguments in the streaming loop, and emit `STATE_SNAPSHOT` whenever the mapped value changes.
  * LlamaIndex and Pydantic AI: there is no per-token mapping. A backend tool sends a state snapshot after each step or tool call instead (see the setup above).



When the LLM streams that argument, CopilotKit writes every partial value into shared state before the tool even finishes executing.

state-streaming-backend.ts

Copy Text
    
    
    import { EventType } from "@ag-ui/core";
    import type Anthropic from "@anthropic-ai/sdk";
    
    type StreamingState = {
      document?: string;
    };
    
    type ToolDeltaEvent = {
      type: string;
      content_block?: { type: string; name?: string };
      delta?: { type: string; partial_json?: string };
    };
    
    export const WRITE_DOCUMENT_TOOL_SCHEMA: Anthropic.Tool = {
      name: "write_document",
      description: "Write a document into shared agent state.",
      input_schema: {
        type: "object",
        properties: {
          document: {
            type: "string",
            description: "The full document text to render in shared state.",
          },
        },
        required: ["document"],
      },
    };
    
    function partialJsonStringProperty(source: string, key: string): string | null {
      // Hand-rolled partial-JSON string extraction with no external dependency
      // (mirrors the Python sibling snippet). Reads the current value of a string
      // property from a partial buffer, tolerating truncation mid-value.
      const marker = JSON.stringify(key);
      const keyPos = source.indexOf(marker);
      if (keyPos < 0) return null;
      const colonPos = source.indexOf(":", keyPos + marker.length);
      if (colonPos < 0) return null;
      const valueStart = source.indexOf('"', colonPos + 1);
      if (valueStart < 0) return null;
    
      const rawChars: string[] = [];
      let escaped = false;
      for (const char of source.slice(valueStart + 1)) {
        if (escaped) {
          rawChars.push("\\" + char);
          escaped = false;
        } else if (char === "\\") {
          escaped = true;
        } else if (char === '"') {
          break;
        } else {
          rawChars.push(char);
        }
      }
      // A buffer truncated mid-escape drops the dangling backslash (matching the
      // Python sibling) so the partial value still parses instead of forcing null.
    
      try {
        return JSON.parse(`"${rawChars.join("")}"`) as string;
      } catch {
        return null;
      }
    }
    
    export function emitStreamingDocumentState(
      event: ToolDeltaEvent,
      tracker: { toolName: string | null; argsJson: string; lastDocument: string },
      state: StreamingState,
      emit: (event: object) => void,
    ) {
      if (
        event.type === "content_block_start" &&
        event.content_block?.type === "tool_use"
      ) {
        tracker.toolName = event.content_block.name ?? null;
        tracker.argsJson = "";
        return;
      }
    
      if (
        event.type !== "content_block_delta" ||
        event.delta?.type !== "input_json_delta"
      ) {
        return;
      }
    
      tracker.argsJson += event.delta.partial_json ?? "";
      if (tracker.toolName !== "write_document") {
        return;
      }
    
      const streamedDocument = partialJsonStringProperty(
        tracker.argsJson,
        "document",
      );
      if (streamedDocument === null || streamedDocument === tracker.lastDocument) {
        return;
      }
    
      // Mutate `state` in place but emit a fresh copy each delta, so a consumer
      // that retains a snapshot doesn't see earlier snapshots mutate to the final
      // text as streaming continues. (Mirrors the Python sibling snippet.)
      const snapshot: StreamingState = { ...state, document: streamedDocument };
      state.document = streamedDocument;
      tracker.lastDocument = streamedDocument;
      emit({ type: EventType.STATE_SNAPSHOT, snapshot });
    }

A few things to note:

  * The state key must exist in your agent state (`document` in this demo).
  * The tool and argument names must match the exact LLM-facing tool call you want to forward (`write_document.document` here).
  * Streamed values are previews. When the step ends, the state the agent saves replaces them, so save the final value when the tool finishes. On CrewAI, LlamaIndex and Pydantic AI, write the final value to the agent state yourself, or it is overwritten when the step returns.



## The frontend: useAgent + OnStateChangedCopy Anchor Link

The UI side is the same as any other [shared-state](https://docs.copilotkit.ai/claude-sdk-typescript/shared-state) subscription: `useAgent` with `OnStateChanged` gives you a reactive `agent.state`. Add `OnRunStatusChanged` if you want a "LIVE" / "done" indicator.

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

[Previous PageRender agent state in your app](https://docs.copilotkit.ai/claude-sdk-typescript/shared-state/rendering-in-app)[Next PageAgent Read-Only Context](https://docs.copilotkit.ai/claude-sdk-typescript/shared-state/agent-readonly)
