---
url: https://docs.copilotkit.ai/reference/vue/components/CopilotChatMessageView/
title: CopilotChatMessageView
method: scrapling+scrapegraph
fetched_at: 2026-11-27T11:59:06.410767+00:00
---

# CopilotChatMessageView

> Source: https://docs.copilotkit.ai/reference/vue/components/CopilotChatMessageView/

Vue/Components

# CopilotChatMessageView

Vue 3 component for rendering a list of chat messages

Copy MarkdownOpen

## OverviewCopy Anchor Link

`CopilotChatMessageView` renders a list of chat messages and, optionally, a typing cursor while the agent is running. It dispatches each message to a default child component based on its `role` (assistant, user, or reasoning) and exposes named slots so you can replace or wrap that rendering. A pulsing cursor is shown after the last message while `isRunning` is `true`. [`CopilotChatView`](https://docs.copilotkit.ai/reference/vue/components/CopilotChatView) uses this component to render its messages.

Unlike the React reference component, customization in Vue is driven entirely through named slots rather than render props or a slot-prop system. The component also surfaces slots for interrupts, activity messages, tool calls, and custom message renderers registered on the CopilotKit instance.

## ImportCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotChatMessageView } from "@copilotkit/vue/v2";
    import "@copilotkit/vue/styles.css";
    </script>

## ExampleCopy Anchor Link

This example reads `messages` and `isRunning` from [`useAgent`](https://docs.copilotkit.ai/reference/vue/hooks/useAgent).

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotChatMessageView } from "@copilotkit/vue/v2";
    import { useAgent } from "@copilotkit/vue/v2";
    
    const { agent } = useAgent();
    </script>
    
    <template>
      <copilot-chat-message-view
        :messages="agent?.messages ?? []"
        :is-running="agent?.isRunning ?? false"
      />
    </template>

## PropsCopy Anchor Link

Prop

Type

`messages?`Message[]

`isRunning?`boolean

Attributes that are not declared props (such as `class`, `style`, or `data-*`) are forwarded to the component's root `<div>` via `v-bind="$attrs"`.

## SlotsCopy Anchor Link

Each slot below is named. Use a `<template #slot-name="slotProps">` block to override or wrap the default rendering. Where a slot has a default, omitting it falls back to the built-in child component.

Prop

Type

`assistant-message?`{ message: AssistantMessage; messages: Message[]; isRunning: boolean }

`user-message?`{ message: UserMessage }

`reasoning-message?`{ message: ReasoningMessage; messages: Message[]; isRunning: boolean }

`cursor?`() => unknown

`interrupt?`{ event: InterruptEvent, interrupt: Interrupt | null, interrupts: Interrupt[], result: unknown, resolve: (payload?: unknown, interruptId?: string) => Promise<RunAgentResult | void>, cancel: (interruptId?: string) => Promise<RunAgentResult | void> }

`message-before?`{ message: Message; position: 'before'; runId: string; messageIndex: number; messageIndexInRun: number; numberOfMessagesInRun: number; agentId: string; stateSnapshot: unknown }

`message-after?`{ message: Message; position: 'after'; runId: string; messageIndex: number; messageIndexInRun: number; numberOfMessagesInRun: number; agentId: string; stateSnapshot: unknown }

`activity-message?`{ activityType: string; content: unknown; message: ActivityMessage; agent: unknown }

`tool-call?`{ name: string; args: unknown; status: string; result: string | undefined; toolCall: unknown; toolMessage: ToolMessage | undefined }

## UsageCopy Anchor Link

### Basic message listCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotChatMessageView } from "@copilotkit/vue/v2";
    import { useAgent } from "@copilotkit/vue/v2";
    
    const { agent } = useAgent();
    </script>
    
    <template>
      <copilot-chat-message-view
        :messages="agent?.messages ?? []"
        :is-running="agent?.isRunning ?? false"
      />
    </template>

### Customizing assistant and user messagesCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotChatMessageView } from "@copilotkit/vue/v2";
    import { useAgent } from "@copilotkit/vue/v2";
    
    const { agent } = useAgent();
    </script>
    
    <template>
      <copilot-chat-message-view
        :messages="agent?.messages ?? []"
        :is-running="agent?.isRunning ?? false"
      >
        <template #assistant-message="{ message }">
          <div class="bg-blue-50 p-4 rounded-xl">{{ message.content }}</div>
        </template>
    
        <template #user-message="{ message }">
          <div class="bg-gray-100 p-4 rounded-xl">{{ message.content }}</div>
        </template>
      </copilot-chat-message-view>
    </template>

### Custom typing indicatorCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotChatMessageView } from "@copilotkit/vue/v2";
    import { useAgent } from "@copilotkit/vue/v2";
    
    const { agent } = useAgent();
    </script>
    
    <template>
      <copilot-chat-message-view
        :messages="agent?.messages ?? []"
        :is-running="agent?.isRunning ?? false"
      >
        <template #cursor>
          <div class="animate-pulse text-gray-400">Thinking...</div>
        </template>
      </copilot-chat-message-view>
    </template>

### Rendering a specific tool callCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotChatMessageView } from "@copilotkit/vue/v2";
    import { useAgent } from "@copilotkit/vue/v2";
    
    const { agent } = useAgent();
    </script>
    
    <template>
      <copilot-chat-message-view
        :messages="agent?.messages ?? []"
        :is-running="agent?.isRunning ?? false"
      >
        <template #tool-call-get_weather="{ args, status, result }">
          <div class="rounded-lg border p-3">
            <p>Status: {{ status }}</p>
            <p v-if="result">Result: {{ result }}</p>
          </div>
        </template>
      </copilot-chat-message-view>
    </template>

## BehaviorCopy Anchor Link

  * **Message rendering** : Each message is dispatched to the matching default child component based on its `role` (assistant, user, reasoning, or activity), unless the corresponding named slot is provided.
  * **Deduplication** : Messages sharing an `id` are deduplicated; assistant fragments with the same id are merged (content and tool calls combined). In development, a console warning is logged when duplicates are dropped.
  * **Cursor display** : The `cursor` slot is rendered only when `isRunning` is `true` and the last message is not a reasoning message. It appears after the last message.
  * **Slot forwarding** : Slots passed to `CopilotChatMessageView` (including `tool-call` and `tool-call-<name>`) are forwarded to the default assistant and user message children, so tool rendering works without re-implementing those components.
  * **Custom and activity renderers** : When `message-before`, `message-after`, or `activity-message` slots are omitted, the component falls back to renderers registered on the CopilotKit instance, scoped to the active `agentId` when applicable.



How is this guide?

GoodBad

[Previous PageCopilotChatInput](https://docs.copilotkit.ai/reference/vue/components/CopilotChatInput)[Next PageCopilotChatUserMessage](https://docs.copilotkit.ai/reference/vue/components/CopilotChatUserMessage)
