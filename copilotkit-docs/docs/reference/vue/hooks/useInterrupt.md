---
url: https://docs.copilotkit.ai/reference/vue/hooks/useInterrupt/
title: useInterrupt
method: scrapling+scrapegraph
fetched_at: 2026-11-24T13:30:44.723826+00:00
---

# useInterrupt

> Source: https://docs.copilotkit.ai/reference/vue/hooks/useInterrupt/

Vue/Hooks

# useInterrupt

Vue 3 composable for handling agent interrupt events and resuming execution with user input

Copy MarkdownOpen

## OverviewCopy Anchor Link

`useInterrupt` is a Vue 3 composable for handling agent interrupts. It supports both the AG-UI standard interrupt flow and the `on_interrupt` custom-event flow, then exposes the active interrupt as reactive state plus `resolve` and `cancel` methods for resuming execution.

By default, the composable publishes its state into [`CopilotChat`](https://docs.copilotkit.ai/reference/vue/components/CopilotChat) so you can render the interrupt through the chat's `#interrupt` slot. Set `renderInChat: false` if you want to place the UI yourself.

For an `on_interrupt` custom event, `event.value` is the event value, typed by the `TValue` type parameter, which defaults to `unknown`. For a standard AG-UI interrupt, `event.value` is the first `Interrupt` object (`{ id, reason, message?, metadata? }`), the same object as `interrupt`. Read the agent's data from `interrupt.message` or `interrupt.metadata`. Narrow `event.value` in your `handler` and `enabled` callbacks, or pass an explicit `TValue` when you call the composable.

`resolve` and `cancel` are the primary methods. `resolveInterrupt` and `cancelInterrupt` remain as aliases for back-compat.

## SignatureCopy Anchor Link

Copy Text
    
    
    import { useInterrupt } from "@copilotkit/vue/v2";
    
    function useInterrupt<TValue = unknown, TResult = never>(
      config?: UseInterruptConfig<TValue, TResult>,
    ): UseInterruptResult<TValue, TResult>;

## ParametersCopy Anchor Link

Prop

Type

`config?`UseInterruptConfig<TValue, TResult>

## Return ValueCopy Anchor Link

Prop

Type

`object?`UseInterruptResult<TValue, TResult>

## UsageCopy Anchor Link

### In-chat interrupt UICopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotChat, useInterrupt } from "@copilotkit/vue/v2";
    
    interface Approval {
      question: string;
    }
    
    useInterrupt<Approval>();
    </script>
    
    <template>
      <CopilotChat>
        <template #interrupt="{ event, resolve }">
          <div class="rounded border p-3">
            <p>{{ (event.value as Approval).question }}</p>
            <div class="mt-2 flex gap-2">
              <button @click="resolve({ approved: true })">Approve</button>
              <button @click="resolve({ approved: false })">Reject</button>
            </div>
          </div>
        </template>
      </CopilotChat>
    </template>

### Manual placement with async preprocessingCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { useInterrupt } from "@copilotkit/vue/v2";
    
    const { interrupt, result, hasInterrupt, resolve } = useInterrupt<
      string,
      { label: string }
    >({
      renderInChat: false,
      enabled: (event) =>
        typeof event.value === "string" && event.value.startsWith("approval:"),
      handler: async ({ event }) => ({ label: event.value.toUpperCase() }),
    });
    </script>
    
    <template>
      <aside v-if="hasInterrupt" class="rounded border p-3">
        <div class="font-medium">{{ result?.label ?? "" }}</div>
        <div class="mt-2">{{ interrupt?.value }}</div>
        <button class="mt-2" @click="resolve({ accepted: true })">Continue</button>
      </aside>
    </template>

### Reading reactive state in scriptCopy Anchor Link

Copy Text
    
    
    import { useInterrupt } from "@copilotkit/vue/v2";
    
    const { interrupt, hasInterrupt, result, cancel, resolve } = useInterrupt({
      handler: ({ event }) => ({ label: String(event.value) }),
    });
    
    // `interrupt` and `result` are reactive refs; `hasInterrupt` is a computed.
    // Call `resolve(response)` or `cancel()` to address the interrupt.

## BehaviorCopy Anchor Link

  * Interrupts are collected from AG-UI standard interrupt events and from `on_interrupt` custom events.
  * Standard interrupts win if both flows appear for the same run.
  * The pending interrupt is surfaced when the run finalizes.
  * Starting a new run clears pending interrupt state, and a failed run discards the in-flight interrupt.
  * When multiple standard interrupts are open, `resolve(payload, interruptId)` and `cancel(interruptId)` accumulate responses until every interrupt is addressed, then resume once.
  * Omitting `interruptId` while multiple standard interrupts are open defaults to the first interrupt and logs a warning.
  * Expired standard interrupts are not resumed.
  * `result` is inferred from the `handler` return type and is always `TResult | null`.
  * When `enabled` returns `false`, the interrupt is ignored: `result` and `slotProps` stay `null` and nothing is published to chat.
  * With `renderInChat` omitted or `true`, `slotProps` is published into `<CopilotChat>` for the `#interrupt` slot. With `renderInChat: false`, no chat publishing occurs and you render from the returned refs.
  * `cancel()` on custom-event interrupts just dismisses without resuming.



How is this guide?

GoodBad

[Previous PageuseHumanInTheLoop](https://docs.copilotkit.ai/reference/vue/hooks/useHumanInTheLoop)[Next PageuseRenderTool](https://docs.copilotkit.ai/reference/vue/hooks/useRenderTool)
