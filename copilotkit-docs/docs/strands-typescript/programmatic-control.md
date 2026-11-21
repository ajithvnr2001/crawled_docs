---
url: https://docs.copilotkit.ai/strands-typescript/programmatic-control/
title: Programmatic Control
method: scrapling+scrapegraph
fetched_at: 2026-11-21T10:52:44.867887+00:00
---

# Programmatic Control

> Source: https://docs.copilotkit.ai/strands-typescript/programmatic-control/

# Programmatic Control

Drive agent runs directly from code, with no chat UI required.

Copy MarkdownOpen

## What is this?Copy Anchor Link

Programmatic control is what you reach for when you want to drive an agent run from code rather than from a chat composer: a button, a form, a cron job, a keyboard shortcut, a graph callback. CopilotKit exposes three primitives that cover every triggering pattern:

  * `agent.addMessage(...)`: append a message to the conversation without running the agent. Pair with `copilotkit.runAgent({ agent })` when you want the appended message to kick off a turn.
  * `copilotkit.runAgent({ agent })`: the same entry point `<CopilotChat />` calls internally. Orchestrates frontend tools, follow-up runs, and the subscriber lifecycle.
  * `agent.subscribe(subscriber)`: low-level AG-UI event subscription (`onCustomEvent`, `onRunStartedEvent`, `onRunFinalized`, `onRunFailed`, …). Pairs with `copilotkit.runAgent({ agent, resume })` for standard AG-UI interrupts, or `copilotkit.runAgent({ agent, forwardedProps: { command: { resume, interruptEvent } } })` for the `on_interrupt` custom events that the LangGraph adapter emits, to drive interrupt resolution from arbitrary UI.



## When should I use this?Copy Anchor Link

Use programmatic control when you want to:

  * Trigger agent runs from buttons, forms, or other UI elements
  * Execute specific tools directly from UI interactions (without an LLM turn)
  * Build agent features without a chat window (to build your own chat UI, see [Headless UI](https://docs.copilotkit.ai/headless))
  * Access agent state and results programmatically
  * Create fully custom agent-driven workflows



## Sending a message from codeCopy Anchor Link

The canonical pattern is to append a user message with `agent.addMessage`, then call `copilotkit.runAgent({ agent })`. Use `copilotkit.stopAgent({ agent })` to cancel an in-flight run.

frontend/src/app/agent-trigger.tsx

Copy Text
    
    
    "use client";
    
    import { useAgent, useCopilotKit } from "@copilotkit/react-core/v2";
    
    export function AgentTrigger({ agentId }: { agentId: string }) {
      const { agent } = useAgent({ agentId });
      const { copilotkit } = useCopilotKit();
    
      const run = async () => {
        if (agent.isRunning) return;
    
        agent.addMessage({
          id: crypto.randomUUID(),
          role: "user",
          content: "Summarize the latest sales data",
        });
    
        try {
          await copilotkit.runAgent({ agent });
        } catch (error) {
          console.error("CopilotKit runAgent failed:", error);
        }
      };
    
      return (
        <>
          <button onClick={run} disabled={agent.isRunning}>
            Run agent
          </button>
          <button
            onClick={() => copilotkit.stopAgent({ agent })}
            disabled={!agent.isRunning}
          >
            Stop
          </button>
        </>
      );
    }

Click **Run agent**. The agent's reply arrives in `agent.messages`. To see it, render the last message, for example `agent.messages.at(-1)?.content`.

### `copilotkit.runAgent()` vs `agent.runAgent()`Copy Anchor Link

Both methods trigger the agent, but they operate at different levels:

  * **`copilotkit.runAgent({ agent })`** : the recommended default. Orchestrates the full lifecycle: executes frontend tools, handles follow-up runs, and routes errors through the subscriber system.
  * **`agent.runAgent(options)`** : low-level method on the agent instance. Sends the request to the runtime but does **not** execute frontend tools or chain follow-ups. Reach for this only when you need direct control.



## Subscribing to agent eventsCopy Anchor Link

`agent.subscribe(subscriber)` returns `{ unsubscribe }`. The subscriber object accepts every AG-UI lifecycle callback: `onCustomEvent`, `onRunStartedEvent`, `onRunFinalized`, `onRunFailed`, and the streaming deltas. Use it to drive custom progress UI, forward events to analytics, or catch framework pause/resume events and resolve them with a payload (the pattern below).

## Resolving a LangGraph interrupt from a buttonCopy Anchor Link

The `interrupt-headless` demo resolves the interrupt outside the chat, without `useInterrupt`. A plain hook subscribes to `on_interrupt` custom events, buffers the payload until the run finalizes (so the UI doesn't flash mid-stream), and exposes a `resolve(response)` callback that calls `copilotkit.runAgent({ agent, forwardedProps: { command: { resume, interruptEvent } } })` to unblock the graph:

page.tsx

Copy Text
    
    
    import React, { useEffect, useState } from "react";
    import {
      CopilotKit,
      CopilotChat,
      useConfigureSuggestions,
      useInterrupt,
    } from "@copilotkit/react-core/v2";
    import { generateFallbackSlots } from "../_shared/interrupt-fallback-slots";
    import type { TimeSlot } from "../_shared/interrupt-fallback-slots";
    
    type InterruptPayload = {
      topic?: string;
      attendee?: string;
      slots?: TimeSlot[];
    };
    
    // Read the tool's `interrupt()` reason off an AG-UI interrupt.
    //
    // The two bridges expose it on different channels: `ag_ui_strands` (Python)
    // carries the reason object under `metadata.reason`, while the published
    // `@ag-ui/aws-strands` 0.2.3 JSON-encodes it into `message` instead. Both are
    // read so one page serves both, and the legacy event value is read last for
    // adapters that pass the payload through unwrapped.
    /**
     * JSON.parse that never throws and never returns a primitive. Both readers run
     * inside a React render callback, where a throw takes the whole pane down.
     */
    function parseObject(raw: string | undefined): Record<string, unknown> | null {
      if (!raw) return null;
      try {
        const parsed: unknown = JSON.parse(raw);
        return parsed && typeof parsed === "object"
          ? (parsed as Record<string, unknown>)
          : null;
      } catch {
        return null;
      }
    }
    
    function readInterruptPayload(
      interrupt: { metadata?: unknown; message?: string } | null | undefined,
      eventValue: unknown,
    ): InterruptPayload {
      const metadata = interrupt?.metadata as
        | { reason?: InterruptPayload }
        | undefined;
      if (metadata?.reason && typeof metadata.reason === "object") {
        return metadata.reason;
      }
    
      // The published TypeScript bridge JSON-encodes the reason into `message`
      // instead of carrying it on metadata.
      const decoded = parseObject(interrupt?.message);
      if (decoded) {
        const nested = (decoded as { reason?: InterruptPayload }).reason;
        return nested && typeof nested === "object"
          ? nested
          : (decoded as InterruptPayload);
      }
    
      // Legacy channel: some adapters pass the payload through as the event value,
      // JSON-encoded or not.
      const legacy =
        typeof eventValue === "string" ? parseObject(eventValue) : eventValue;
      if (!legacy || typeof legacy !== "object") return {};
      const wrapped = (legacy as { metadata?: { reason?: InterruptPayload } })
        .metadata?.reason;
      if (wrapped && typeof wrapped === "object") return wrapped;
      return legacy as InterruptPayload;
    }
    
    export default function InterruptHeadlessDemo() {
      return (
        <CopilotKit runtimeUrl="/api/copilotkit" agent="interrupt-headless">
          <Layout />
        </CopilotKit>
      );
    }
    
    function Layout() {
      const [resolving, setResolving] = useState(false);
      const interruptElement = useInterrupt({
        agentId: "interrupt-headless",
        renderInChat: false,
        render: ({ event, interrupt, resolve }) => {
          const payload = readInterruptPayload(interrupt, event.value);
          const resumeAfterPaint = (response: unknown) => {
            setResolving(true);
            // A frame boundary lets React paint before resume unmounts the
            // interrupt, but `requestAnimationFrame` never fires in a background
            // tab, so a timer runs whichever comes first and the resume cannot be
            // stranded. Fire-and-forget by design: a rejected resume is re-surfaced
            // globally instead of disappearing.
            let fired = false;
            const resumeOnce = () => {
              if (fired) return;
              fired = true;
              void resolve(response).then(
                () => setResolving(false),
                (error) => {
                  setResolving(false);
                  queueMicrotask(() => {
                    throw error;
                  });
                },
              );
            };
            requestAnimationFrame(resumeOnce);
            window.setTimeout(resumeOnce, 100);
          };
          return (
            <TimeSlotPopup
              payload={payload}
              onPick={(slot) => {
                resumeAfterPaint({
                  chosen_time: slot.iso,
                  chosen_label: slot.label,
                });
              }}
              onCancel={() => {
                resumeAfterPaint({ cancelled: true });
              }}
            />
          );
        },
      });
    
      useEffect(() => {
        if (interruptElement) {
          setResolving(false);
        }
      }, [interruptElement]);
    
      useConfigureSuggestions({
        suggestions: [
          {
            title: "Book a call with sales",
            message: "Book an intro call with the sales team to discuss pricing.",
          },
          {
            title: "Schedule a 1:1 with Alice",
            message: "Schedule a 1:1 with Alice next week to review Q2 goals.",
          },
        ],
        available: "always",
      });
    
      return (
        <div className="grid h-screen grid-cols-[1fr_420px] bg-[#FAFAFC] dark:bg-background">
          <AppSurface interruptElement={interruptElement} resolving={resolving} />
          <div className="border-l border-[#DBDBE5] bg-white dark:border-border dark:bg-background">
            <CopilotChat agentId="interrupt-headless" className="h-full" />
          </div>
        </div>
      );
    }

The excerpt imports `generateFallbackSlots` and `TimeSlot` from a demo helper that makes sample time slots when the interrupt payload has none. Use your own data in their place.

The resulting `{ pending, resolve }` tuple is pure data; any UI can drive it. The demo itself renders a simple button grid, but the same hook would power a modal, a toast, a sidebar form, or a voice UI. To pause inside the chat instead, see [Human-in-the-Loop](https://docs.copilotkit.ai/human-in-the-loop).

How is this guide?

GoodBad
