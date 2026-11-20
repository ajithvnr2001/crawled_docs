---
url: https://docs.copilotkit.ai/reference/react-native/hooks/useInterrupt/
title: useInterrupt
method: scrapling+scrapegraph
fetched_at: 2026-11-20T11:16:29.251662+00:00
---

# useInterrupt

> Source: https://docs.copilotkit.ai/reference/react-native/hooks/useInterrupt/

React Native/Hooks

# useInterrupt

React hook for handling agent interrupt events and resuming execution with user input

Copy MarkdownOpen

## OverviewCopy Anchor Link

`useInterrupt` handles agent interrupts and resumes execution with user input. It supports two interrupt flows:

  * **AG-UI standard** : `RUN_FINISHED` with `outcome.type === "interrupt"`, carrying an `interrupts` array.
  * **Custom event** : an `on_interrupt` custom event.



In your `render` callback, call `resolve(payload)` to resume or `cancel()` to cancel. See `render` for every prop it receives. For a pause that is a tool call, use [`useHumanInTheLoop`](https://docs.copilotkit.ai/reference/react-native/hooks/useHumanInTheLoop).

Re-exported from `@copilotkit/react-core/v2`. It is identical to the [React (V2) `useInterrupt`](https://docs.copilotkit.ai/reference/v2/hooks/useInterrupt); only the import path differs.

The prebuilt [`CopilotChat`](https://docs.copilotkit.ai/reference/react-native/components/CopilotChat#prebuilt-ui) and [`CopilotModal`](https://docs.copilotkit.ai/reference/react-native/components/CopilotModal) from `@copilotkit/react-native/components` draw the in-chat interrupt element after the last message. The headless `CopilotChat`, `CopilotPopup`, and `CopilotSidebar` do not. With those, pass `renderInChat: false`, and the hook returns the element so you can render it in your own view. The element returned by `render` is a React Native element.

`event.value` is typed as `any` since the interrupt payload shape depends on your agent. Type-narrow it in your callbacks (e.g. `handler`, `enabled`, `render`) as needed.

## SignatureCopy Anchor Link

Copy Text
    
    
    import { useInterrupt } from "@copilotkit/react-native";
    
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

### Interrupt UI in your chat viewCopy Anchor Link

Copy Text
    
    
    import { Text, TouchableOpacity, View } from "react-native";
    import { useInterrupt } from "@copilotkit/react-native";
    
    function ApprovalInterrupt() {
      const element = useInterrupt({
        renderInChat: false,
        render: ({ event, resolve }) => (
          <View style={{ padding: 12, borderWidth: 1, borderRadius: 8 }}>
            <Text>{event.value.question}</Text>
            <View style={{ marginTop: 8, flexDirection: "row", gap: 8 }}>
              <TouchableOpacity onPress={() => resolve({ approved: true })}>
                <Text>Approve</Text>
              </TouchableOpacity>
              <TouchableOpacity onPress={() => resolve({ approved: false })}>
                <Text>Reject</Text>
              </TouchableOpacity>
            </View>
          </View>
        ),
      });
    
      return <>{element}</>;
    }

### AG-UI standard interrupt (approve / cancel)Copy Anchor Link

Copy Text
    
    
    import { Text, TouchableOpacity, View } from "react-native";
    import { useInterrupt } from "@copilotkit/react-native";
    
    function ApprovalInterrupt() {
      const element = useInterrupt({
        renderInChat: false,
        render: ({ interrupt, resolve, cancel }) => (
          <View style={{ padding: 12, borderWidth: 1, borderRadius: 8 }}>
            <Text>{interrupt?.message ?? "Approve this action?"}</Text>
            <View style={{ marginTop: 8, flexDirection: "row", gap: 8 }}>
              <TouchableOpacity onPress={() => resolve({ approved: true })}>
                <Text>Approve</Text>
              </TouchableOpacity>
              <TouchableOpacity onPress={() => cancel()}>
                <Text>Cancel</Text>
              </TouchableOpacity>
            </View>
          </View>
        ),
      });
    
      return <>{element}</>;
    }

### Manual placement with async preprocessingCopy Anchor Link

Copy Text
    
    
    import { Text, TouchableOpacity, View } from "react-native";
    import { useInterrupt } from "@copilotkit/react-native";
    
    function SidePanelInterrupt() {
      const element = useInterrupt({
        renderInChat: false,
        enabled: (event) => event.value.startsWith("approval:"),
        handler: async ({ event }) => ({ label: event.value.toUpperCase() }),
        render: ({ event, result, resolve }) => (
          <View style={{ borderWidth: 1, borderRadius: 8, padding: 12 }}>
            <Text style={{ fontWeight: "500" }}>{result?.label ?? ""}</Text>
            <Text style={{ marginTop: 8 }}>{event.value}</Text>
            <TouchableOpacity style={{ marginTop: 8 }} onPress={() => resolve({ accepted: true })}>
              <Text>Continue</Text>
            </TouchableOpacity>
          </View>
        ),
      });
    
      return <>{element}</>;
    }

## BehaviorCopy Anchor Link

  * Standard interrupts are detected from `RUN_FINISHED` (`outcome.type === "interrupt"`); custom-event interrupts from `on_interrupt` events.
  * `resolve`/`cancel` accumulate one response per open interrupt; the resume run starts once every open interrupt is addressed.
  * Expired interrupts (past `expiresAt`) are not resumed.
  * Interrupt UI is surfaced when the run finalizes.
  * Starting a new run clears pending interrupt state.
  * `event.value` is `any`; type-narrow in your callbacks as needed. For standard interrupts, `event.value` is the primary `Interrupt`.
  * `render.result` is inferred from `handler` return type and is always `TResult | null`.
  * If `handler` throws or rejects, `result` is set to `null`.



How is this guide?

GoodBad

[Previous PageuseHumanInTheLoop](https://docs.copilotkit.ai/reference/react-native/hooks/useHumanInTheLoop)[Next PageuseRenderTool](https://docs.copilotkit.ai/reference/react-native/hooks/useRenderTool)
