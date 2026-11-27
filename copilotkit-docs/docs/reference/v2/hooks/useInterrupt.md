---
url: https://docs.copilotkit.ai/reference/v2/hooks/useInterrupt/
title: useInterrupt
method: scrapling+scrapegraph
fetched_at: 2026-11-27T11:59:07.937994+00:00
---

# useInterrupt

> Source: https://docs.copilotkit.ai/reference/v2/hooks/useInterrupt/

React/Hooks

# useInterrupt

React hook for handling agent interrupt events and resuming execution with user input

Copy MarkdownOpen

## OverviewCopy Anchor Link

`useInterrupt` shows your UI when the agent pauses for input. Call `resolve(payload)` to resume the run. Call `cancel()` to cancel it. The hook supports the AG-UI standard interrupt flow and the `on_interrupt` custom-event flow. See Behavior.

For a full walkthrough, see [Pausing the Agent for Input](https://docs.copilotkit.ai/human-in-the-loop/useInterrupt). If your agent has no interrupt, use [`useHumanInTheLoop`](https://docs.copilotkit.ai/reference/hooks/useHumanInTheLoop).

By default, interrupt UI is rendered inside `<CopilotChat>` automatically. If you set `renderInChat: false`, the hook returns the element so you can place it manually.

## SignatureCopy Anchor Link

Copy Text
    
    
    import { useInterrupt } from "@copilotkit/react-core/v2";
    
    function useInterrupt<
      TResult = never,
      TRenderInChat extends boolean | undefined = undefined,
    >(
      config: UseInterruptConfig<any, TResult, TRenderInChat>,
    ): TRenderInChat extends false
      ? React.ReactElement | null
      : TRenderInChat extends true | undefined
        ? void
        : React.ReactElement | null | void;

## ParametersCopy Anchor Link

Prop

Type

`config`UseInterruptConfig<any, TResult, TRenderInChat>

## Return ValueCopy Anchor Link

Prop

Type

`element?`Conditional by renderInChat

## UsageCopy Anchor Link

### In-chat interrupt UI (default)Copy Anchor Link

This sample reads a custom-event interrupt whose value holds a `question` field. For a standard interrupt, read `interrupt.message` instead, as in the AG-UI standard sample below.

Copy Text
    
    
    function ApprovalInterrupt() {
      useInterrupt({
        render: ({ event, resolve }) => {
          const value =
            typeof event.value === "string" ? JSON.parse(event.value) : event.value;
          return (
            <div className="p-3 border rounded">
              <p>{value.question}</p>
              <div className="mt-2 flex gap-2">
                <button onClick={() => resolve({ approved: true })}>Approve</button>
                <button onClick={() => resolve({ approved: false })}>Reject</button>
              </div>
            </div>
          );
        },
      });
    
      return null;
    }

### Manual placement with async preprocessingCopy Anchor Link

Copy Text
    
    
    function SidePanelInterrupt() {
      const element = useInterrupt({
        renderInChat: false,
        enabled: (event) => event.value.startsWith("approval:"),
        handler: async ({ event }) => ({ label: event.value.toUpperCase() }),
        render: ({ event, result, resolve }) => (
          <aside className="rounded border p-3">
            <div className="font-medium">{result?.label ?? ""}</div>
            <div className="mt-2">{event.value}</div>
            <button className="mt-2" onClick={() => resolve({ accepted: true })}>
              Continue
            </button>
          </aside>
        ),
      });
    
      return <>{element}</>;
    }

### AG-UI standard interrupt (approve / cancel)Copy Anchor Link

Copy Text
    
    
    function ApprovalInterrupt() {
      useInterrupt({
        render: ({ interrupt, resolve, cancel }) => (
          <div className="p-3 border rounded">
            <p>{interrupt?.message ?? "Approve this action?"}</p>
            <div className="mt-2 flex gap-2">
              <button onClick={() => resolve({ approved: true })}>Approve</button>
              <button onClick={() => cancel()}>Cancel</button>
            </div>
          </div>
        ),
      });
      return null;
    }

## BehaviorCopy Anchor Link

  * Standard interrupts are detected from `RUN_FINISHED` (`outcome.type === "interrupt"`, carrying an `interrupts` array); custom-event interrupts from `on_interrupt` custom events. For standard interrupts, `render` and `handler` receive `interrupt` (the primary one) and `interrupts` (the full open set). Standard takes precedence if both appear in the same run.
  * `resolve`/`cancel` accumulate one response per open interrupt; the resume run starts once every open interrupt is addressed. Standard resumes use a fresh `runId` on the same thread and identify the pending interrupts through `resume[].interruptId`.
  * Expired interrupts (past `expiresAt`) are not resumed. The hook logs an error and clears pending state.
  * Interrupt UI is surfaced when the run finalizes.
  * Starting a new run clears pending interrupt state.
  * `render.result` is inferred from `handler` return type and is always `TResult | null`.
  * If `handler` throws or rejects, `result` is set to `null`.



How is this guide?

GoodBad

[Previous PageuseHumanInTheLoop](https://docs.copilotkit.ai/reference/v2/hooks/useHumanInTheLoop)[Next PageuseRenderTool](https://docs.copilotkit.ai/reference/v2/hooks/useRenderTool)
