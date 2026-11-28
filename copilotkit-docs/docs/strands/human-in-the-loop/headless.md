---
url: https://docs.copilotkit.ai/strands/human-in-the-loop/headless/
title: Headless Interrupts
method: scrapling+scrapegraph
fetched_at: 2026-11-28T11:35:20.377800+00:00
---

# Headless Interrupts

> Source: https://docs.copilotkit.ai/strands/human-in-the-loop/headless/

Human-in-the-loop

# Headless Interrupts

Resolve agent interrupts from any UI, without a useInterrupt render slot.

Copy MarkdownOpen

Headless Interrupt (testing)

DemoCode

[](https://showcase-strands-production.up.railway.app/demos/interrupt-headless "Open in a new tab")[](https://github.com/CopilotKit/CopilotKit/tree/main/showcase/integrations/strands/src/app/demos/interrupt-headless "View the code on GitHub")

Waking up the demo

## What is this?Copy Anchor Link

Sometimes the agent's question belongs outside the chat, in a dashboard, a side panel, or a modal. A headless interrupt lets any component show the question and resume the run with the answer. No chat needs to be mounted.

This page shows how to resolve an interrupt without the chat. You build the resolver from the same hooks that `useInterrupt` uses. It can be a button grid, a form, a modal, or a keyboard shortcut.

The underlying primitive is the interrupt call of your agent framework. How it reaches the client depends on the agent framework, and there are two headless shapes to match:

  * An agent framework that surfaces the pause as an `on_interrupt` custom event (LangGraph): subscribe to that event and resume the run by calling `copilotkit.runAgent({...})` with the matching `resume` payload.
  * An agent framework that finishes the run with a standard AG-UI interrupt outcome (AWS Strands): the run's final `RUN_FINISHED` carries `outcome: { type: "interrupt", interrupts: [...] }`. Call `useInterrupt` with `renderInChat: false` and place the element it returns wherever you like; `resolve(...)` resumes the run.



Either way, no chat surface is required.

## When should I use this?Copy Anchor Link

  * **Testing / Playwright fixtures** : a deterministic, chat-less button grid is easier to drive than a chat surface where the picker only appears after an LLM call.
  * **Non-chat UIs** : dashboards, side panels, inspector surfaces, or any place where you want the _agent's interrupt_ without the _chat transcript_.
  * **Custom flow control** : when you need to know exactly when the interrupt arrived (e.g. to gate other UI) and when it was resolved.
  * **Research / debugging** : when you want to observe the raw AG-UI custom events without the abstraction layer.



If you just want "a picker in chat", just use [`useInterrupt`](https://docs.copilotkit.ai/useInterrupt). For pauses that the model decides on, use [`useHumanInTheLoop`](https://docs.copilotkit.ai/human-in-the-loop).

## Use `useInterrupt` without the chatCopy Anchor Link

The simplest headless pattern uses `useInterrupt` with `renderInChat: false`. Instead of publishing the element into `<CopilotChat>`, the hook returns the interrupt element directly so you can place it anywhere in your tree. This panel starts the run itself and shows the slot buttons while the agent waits:

Copy Text
    
    
    const SLOTS = [
      { iso: "2026-11-03T15:00:00Z", label: "Tue 3 PM" },
      { iso: "2026-11-04T10:00:00Z", label: "Wed 10 AM" },
    ];
    
    function HeadlessInterruptPanel() {
      const { copilotkit } = useCopilotKit();
      const { agent } = useAgent({ agentId: "interrupt-headless" });
    
      const kickOff = (prompt: string) => {
        agent.addMessage({ id: crypto.randomUUID(), role: "user", content: prompt });
        void copilotkit.runAgent({ agent });
      };
    
      const interruptElement = useInterrupt({
        renderInChat: false,
        render: ({ interrupt, resolve, cancel }) => (
          <div>
            <p>Pick a slot for {interrupt?.message ?? "a call"}:</p>
            {SLOTS.map((s) => (
              <button key={s.iso} onClick={() => resolve({ chosen_time: s.iso, chosen_label: s.label })}>
                {s.label}
              </button>
            ))}
            <button onClick={() => cancel()}>Cancel</button>
          </div>
        ),
      });
    
      if (interruptElement) {
        return interruptElement;
      }
    
      return <button onClick={() => kickOff("Book a call with sales.")}>Book call</button>;
    }

`interrupt` carries the primary AG-UI `Interrupt` object (`{ id, reason, message?, responseSchema?, expiresAt?, ... }`). `resolve(payload)` submits the user's response and resumes the agent. `cancel()` cancels the interrupt and resumes. Both return a `Promise<RunAgentResult | void>`. They resolve to void while waiting on further interrupts when more than one is open.

Click **Book call**. When the agent pauses, the slot buttons replace the button. Pick a slot. The run resumes, and the **Book call** button comes back.

## Subscribe to the interrupt yourselfCopy Anchor Link

Internally, `useInterrupt` composes two public APIs:

  1. **`agent.subscribe({ onCustomEvent, onRunStartedEvent, onRunFinishedEvent, onRunFinalized, onRunFailed })`** : every `AbstractAgent` exposes an AG-UI event subscription. Standard interrupts arrive on `onRunFinishedEvent` with `{ outcome: { type: "interrupt", interrupts: [...] } }`. Custom-event interrupts (the LangGraph default) arrive as a custom event named `on_interrupt`.
  2. **`copilotkit.runAgent({ agent, resume })`** (standard) or **`copilotkit.runAgent({ agent, forwardedProps: { command: { resume, interruptEvent } } })`** (custom event): the same call `useInterrupt`'s `resolve()` / `cancel()` makes to resume a paused run.



The code below depends on how your agent pauses. Where the agent framework pauses with a custom event, it is a hand-rolled hook over the raw subscription; where it pauses with a standard AG-UI interrupt, the same `useInterrupt` call with `renderInChat: false` is all that is needed, and the snippet shows that instead. Either way, the raw primitives remain available when you want full control (testing fixtures, custom accumulation logic):

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

A few things the hand-rolled variant is careful about:

  * It stages the incoming event in a local ref and only commits it to React state on `onRunFinalized`, mirroring `useInterrupt`, which doesn't surface the interrupt until the run has actually paused (not just when the event fires mid-stream).
  * `onRunStartedEvent` clears any stale pending state, so kicking off a new turn always starts from a clean slate.
  * `onRunFailed` drops the staged event so a transport hiccup doesn't leave the UI stuck showing a picker for a run that never paused.



The same panel, built on the `useHeadlessInterrupt` hook from the snippet:

Copy Text
    
    
    // SLOTS is the list from the previous sample.
    function HeadlessInterruptPanelRaw() {
      const { copilotkit } = useCopilotKit();
      const { agent } = useAgent({ agentId: "interrupt-headless" });
      const { pending, resolve } = useHeadlessInterrupt("interrupt-headless");
    
      const kickOff = (prompt: string) => {
        agent.addMessage({ id: crypto.randomUUID(), role: "user", content: prompt });
        void copilotkit.runAgent({ agent });
      };
    
      if (pending) {
        return (
          <div>
            <p>Pick a slot for {pending.value.topic ?? "a call"}:</p>
            {SLOTS.map((s) => (
              <button key={s.iso} onClick={() => resolve({ chosen_time: s.iso, chosen_label: s.label })}>
                {s.label}
              </button>
            ))}
            <button onClick={() => resolve({ cancelled: true })}>Cancel</button>
          </div>
        );
      }
    
      return <button onClick={() => kickOff("Book a call with sales.")}>Book call</button>;
    }

How is this guide?

GoodBad

[Previous PagePausing the Agent for Input](https://docs.copilotkit.ai/strands/human-in-the-loop/useInterrupt)[Next PageGoverned Action Approval UI](https://docs.copilotkit.ai/strands/human-in-the-loop/governed-actions)
