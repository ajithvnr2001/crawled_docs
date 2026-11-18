---
url: https://docs.copilotkit.ai/react-native/human-in-the-loop/useInterrupt/
title: Pausing the Agent for Input
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:54.765751+00:00
---

# Pausing the Agent for Input

> Source: https://docs.copilotkit.ai/react-native/human-in-the-loop/useInterrupt/

Human-in-the-loop

# Pausing the Agent for Input

Pause an agent run, hand control to a React Native component, and resume with the user's answer.

Copy MarkdownOpen

## What is this?Copy Anchor Link

Some agent steps need a person's answer before the run can continue, such as approving a payment or picking a meeting time. `useInterrupt` pauses the run, shows your React Native component, and resumes the run with the answer. How the pause works depends on your agent framework.

> **Use`useHumanInTheLoop` on this framework.** `useInterrupt` needs an agent that emits an AG-UI interrupt (`RUN_FINISHED` with `outcome.type === "interrupt"`) or an `on_interrupt` custom event, and a working resume path. On the Built-in Agent, interrupts are temporarily unavailable. [`useHumanInTheLoop`](https://docs.copilotkit.ai/react-native/human-in-the-loop) pauses on a tool call instead. It works on every framework that supports frontend tools.

## When should I use this?Copy Anchor Link

Use `useInterrupt` when the pause is a **checkpoint in your agent code** , where the code path _must_ stop and wait for a human. It is not for a tool call the model decides to make. Typical cases:

  * A sensitive action (payments, irreversible writes) must be approved
  * A required value isn't known and only the user can give it
  * The agent reaches an approval step in a longer workflow
  * You want the server-side contract to be an interrupt that resumes with a payload



When the model decides on the fly to ask the user, use [`useHumanInTheLoop`](https://docs.copilotkit.ai/react-native/human-in-the-loop) instead.

## AG-UI standard interrupt flow vs. custom-event flowCopy Anchor Link

This section is a reference for developers who write `render` code for their own agent. The [`useInterrupt` reference](https://docs.copilotkit.ai/reference/react-native/hooks/useInterrupt) lists every option. `useInterrupt` handles two kinds of interrupt, and your agent framework decides which kind it sends.

### Standard flow (`RUN_FINISHED` with `outcome.type === "interrupt"`)Copy Anchor Link

An agent that follows the AG-UI protocol signals an interrupt with a `RUN_FINISHED` event whose outcome carries the interrupts:

Copy Text
    
    
    outcome.type === "interrupt"
    outcome.interrupts  // Interrupt[]

The hook shows the interrupts after the run finalizes. `render` receives:

  * **`interrupt`** : the primary `Interrupt` (`interrupts[0]`), with shape `{ id, reason, message?, toolCallId?, responseSchema?, expiresAt?, metadata? }`.
  * **`interrupts`** : every open interrupt.
  * **`resolve(payload?, interruptId?)`** : records an answer for the targeted interrupt. The run resumes once every open interrupt has an answer.
  * **`cancel(interruptId?)`** : records a cancellation for the targeted interrupt. The run also resumes once every open interrupt is addressed.



### Custom-event flow (`on_interrupt`)Copy Anchor Link

Agents can emit a custom `on_interrupt` event. The LangGraph adapter does this by default. `render` gets its payload in `event.value`, with `interrupt` set to `null` and `interrupts` to `[]`. `resolve(payload)` resumes the run right away, through `forwardedProps.command`. `cancel()` only dismisses the interrupt without resuming, because this flow has no cancel answer.

If both signals arrive on the same run, the standard flow wins.

### Approve / Cancel exampleCopy Anchor Link

Copy Text
    
    
    import { Button, Text, View } from "react-native";
    import { useInterrupt } from "@copilotkit/react-native/headless";
    
    function ApprovalPanel() {
      const element = useInterrupt({
        renderInChat: false,
        render: ({ interrupt, resolve, cancel }) => (
          <View style={{ padding: 12, gap: 8 }}>
            <Text>{interrupt?.message ?? "Approve this action?"}</Text>
            <Button title="Approve" onPress={() => resolve({ approved: true })} />
            <Button title="Cancel" onPress={() => cancel()} />
          </View>
        ),
      });
    
      return element;
    }

Both methods return the run result once the run restarts, or nothing while other open interrupts still wait for an answer.

### More than one open interruptCopy Anchor Link

Some agents issue more than one interrupt in a single run. Each has its own `id`, so answer them one by one:

Copy Text
    
    
    render: ({ interrupts, resolve, cancel }) => (
      <View>
        {interrupts.map((item) => (
          <View key={item.id} style={{ flexDirection: "row", gap: 8 }}>
            <Text>{item.message}</Text>
            <Button title="Approve" onPress={() => resolve({ ok: true }, item.id)} />
            <Button title="Cancel" onPress={() => cancel(item.id)} />
          </View>
        ))}
      </View>
    ),

The run resumes only after **every** open interrupt is addressed. If you leave out `interruptId`, the primary interrupt is targeted, and the hook logs a warning when several are open.

### `responseSchema` is not validatedCopy Anchor Link

An `Interrupt` can carry a `responseSchema`, a JSON Schema that describes the answer the agent expects. `useInterrupt` passes it to `render` as `interrupt.responseSchema`, but it does **not** check your `resolve` payload against it. The agent validates the answer when it resumes.

## Provider setupCopy Anchor Link

The component that calls `useInterrupt` or `useHumanInTheLoop` must be under `CopilotKitProvider`:

App.tsx

Copy Text
    
    
    import { CopilotKitProvider } from "@copilotkit/react-native/headless";
    import { MeetingChat } from "./src/MeetingChat";
    
    const runtimeUrl = "http://localhost:8200/api/copilotkit";
    
    export default function App() {
      return (
        <CopilotKitProvider runtimeUrl={runtimeUrl}>
          <MeetingChat />
        </CopilotKitProvider>
      );
    }

How is this guide?

GoodBad

[Previous PageHITL Overview](https://docs.copilotkit.ai/react-native/human-in-the-loop)[Next PageHeadless Interrupts](https://docs.copilotkit.ai/react-native/human-in-the-loop/headless)
