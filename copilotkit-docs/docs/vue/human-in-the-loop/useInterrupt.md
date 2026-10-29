---
url: https://docs.copilotkit.ai/vue/human-in-the-loop/useInterrupt/
title: Pausing the Agent for Input
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:46:24.120766+00:00
---

# Pausing the Agent for Input

> Source: https://docs.copilotkit.ai/vue/human-in-the-loop/useInterrupt/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendVueAgent backendCopilotKit

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Quickstart](https://docs.copilotkit.ai/vue)[Using these docs](https://docs.copilotkit.ai/vue/using-these-docs)[Build with agents](https://docs.copilotkit.ai/vue/build-with-agents)[Intelligence](https://docs.copilotkit.ai/vue/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/vue/frontend-tools)

Generative UI

Controlled

Open-ended

Interactivity

Shared state

Human-in-the-loop

[HITL Overview](https://docs.copilotkit.ai/vue/human-in-the-loop)[Pausing the Agent for Input](https://docs.copilotkit.ai/vue/human-in-the-loop/useInterrupt)[Headless Interrupts](https://docs.copilotkit.ai/vue/human-in-the-loop/headless)[Governed Action Approval UI](https://docs.copilotkit.ai/vue/human-in-the-loop/governed-actions)

[WebMCP](https://docs.copilotkit.ai/vue/webmcp)

Agent capabilities

[Sub-agents](https://docs.copilotkit.ai/vue/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/vue/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/vue/learning)

[User Memories](https://docs.copilotkit.ai/vue/intelligence/memories)

[Trajectories](https://docs.copilotkit.ai/vue/intelligence/trajectories)

[Standalone collector](https://docs.copilotkit.ai/vue/intelligence/standalone-collector)[Product Analytics](https://docs.copilotkit.ai/vue/intelligence/analytics)[Channels](https://docs.copilotkit.ai/vue/intelligence/channels)

Hosting

Backend

Runtime

Deployment

Debugging

Learn

Concepts

Other

Troubleshooting

[Community frameworks](https://docs.copilotkit.ai/vue/community-frameworks)[Reference docs](https://docs.copilotkit.ai/reference/vue)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

InteractivityHuman-in-the-loop

# Pausing the Agent for Input

Pause an agent run, hand control to a custom Vue component, and resume with the user's answer.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

`useInterrupt` lets your agent pause mid-run, hand control to the user through custom Vue UI, and resume with whatever the user returns. How that pause is implemented depends on the framework's runtime.

## When should I use this?#

Reach for `useInterrupt` when the pause is a **graph-enforced checkpoint** where the code path _must_ stop and wait for a human, not an LLM-initiated tool call. Typical cases:

  * A sensitive action (payments, irreversible writes) must be approved
  * A required piece of state isn't known and can only be collected from the user
  * The agent explicitly reaches an approval node in a longer workflow
  * You want the server-side contract to be `interrupt(...)` and resume with a payload



For LLM-initiated pauses where the model decides on the fly to ask the user, prefer [`useHumanInTheLoop`](https://docs.copilotkit.ai/human-in-the-loop).

## AG-UI standard interrupt flow vs. legacy#

`useInterrupt` supports two interrupt transports. Understanding which one your agent uses helps you write the right UI.

### Standard flow (`RUN_FINISHED` with `outcome.type === "interrupt"`)#

When the agent backend conforms to the AG-UI protocol, it signals an interrupt by emitting a `RUN_FINISHED` event whose outcome carries the interrupts array:
    
    
    outcome.type === "interrupt"
    outcome.interrupts  // Interrupt[]

The composable detects this on `onRunFinishedEvent` and exposes the interrupts after `onRunFinalized` fires. `slotProps.value` contains:

  * **`interrupt`** — the primary `Interrupt` (`interrupts[0]`), with shape `{ id, reason, message?, toolCallId?, responseSchema?, expiresAt?, metadata? }`.
  * **`interrupts`** — the full open set.
  * **`resolve(payload?, interruptId?)`** — records a resolved response for the targeted interrupt. The run resumes once every open interrupt has a response.
  * **`cancel(interruptId?)`** — records a cancelled response for the targeted interrupt. The same accumulate-then-submit logic applies.



### Legacy flow (`on_interrupt` custom event)#

Older agents may emit a custom `on_interrupt` event. The composable exposes its payload in `event.value`, with `interrupt` set to `null` and `interrupts` to `[]`. Calling `resolve(payload)` resumes via `forwardedProps.command`, the legacy mechanism. `cancel()` dismisses the interrupt without resuming because the legacy transport has no cancel response.

### Priority#

If both signals appear on the same run, the standard flow wins.

### Approve / Cancel example#

src/components/ApprovalPanel.vue
    
    
    <script setup lang="ts">
    import { useInterrupt } from "@copilotkit/vue/v2";
    
    const { slotProps } = useInterrupt({ renderInChat: false });
    </script>
    
    <template>
      <section v-if="slotProps">
        <p>{{ slotProps.interrupt?.message ?? "Approve this action?" }}</p>
        <button @click="slotProps.resolve({ approved: true })">Approve</button>
        <button @click="slotProps.cancel()">Cancel</button>
      </section>
    </template>

Both methods return the `RunAgentResult` once the run restarts, or `void` while waiting for responses to other open interrupts.

### Multi-interrupt behavior#

Some agents issue more than one interrupt in a single run. Each interrupt has its own `id`; address them individually:
    
    
    <template>
      <ul v-if="slotProps">
        <li v-for="item in slotProps.interrupts" :key="item.id">
          {{ item.message }}
          <button @click="slotProps.resolve({ ok: true }, item.id)">Approve</button>
          <button @click="slotProps.cancel(item.id)">Cancel</button>
        </li>
      </ul>
    </template>

The agent run resumes only after **every** open interrupt has been addressed. If you omit `interruptId`, the primary interrupt is targeted; Vue warns when several are open.

### `responseSchema` — surface only, no client-side validation#

The `Interrupt` type exposes a `responseSchema` JSON Schema that the agent can use to describe the expected payload. `useInterrupt` surfaces it on `interrupt.responseSchema` for your UI to read, but it does **not** validate `resolve` payloads against it. Validation is the agent's responsibility on resume.

## Provider setup#

The component calling `useInterrupt` must be a descendant of `CopilotKitProvider`:

src/App.vue
    
    
    <script setup lang="ts">
    import { CopilotKitProvider } from "@copilotkit/vue/v2";
    import MeetingChat from "./components/MeetingChat.vue";
    </script>
    
    <template>
      <CopilotKitProvider runtime-url="/api/copilotkit">
        <MeetingChat />
      </CopilotKitProvider>
    </template>

## Going further#

  * [Tool-based HITL with `useHumanInTheLoop`](https://docs.copilotkit.ai/human-in-the-loop) — for LLM-initiated pauses.
  * [Headless interrupts](https://docs.copilotkit.ai/headless) — render and resolve interrupts outside a chat surface.


