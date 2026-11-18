---
url: https://docs.copilotkit.ai/reference/vue/components/CopilotChatUserMessage/
title: CopilotChatUserMessage
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:57.092930+00:00
---

# CopilotChatUserMessage

> Source: https://docs.copilotkit.ai/reference/vue/components/CopilotChatUserMessage/

Vue/Components

# CopilotChatUserMessage

Vue 3 component for displaying user-authored messages with copy, edit, and branch navigation.

Copy MarkdownOpen

This is the Vue 3 component. Import it from `@copilotkit/vue/v2`.

## OverviewCopy Anchor Link

`CopilotChatUserMessage` renders a user-authored message aligned to the right of the chat. The default message renderer flattens the message content to text and displays it with `white-space: pre-wrap` so line breaks and spacing are preserved.

Below the message it renders a toolbar containing a copy-to-clipboard button, an optional edit button, and optional branch navigation controls. The toolbar becomes visible on hover. The edit button is only shown when an `@edit-message` listener is attached, and the branch navigation is only shown when `numberOfBranches` is greater than 1 and a `@switch-to-branch` listener is attached.

## ExampleCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotChatUserMessage } from "@copilotkit/vue/v2";
    import "@copilotkit/vue/styles.css";
    import type { UserMessage } from "@ag-ui/core";
    
    const message: UserMessage = {
      id: "1",
      role: "user",
      content: "What is the capital of France?",
    };
    </script>
    
    <template>
      <CopilotChatUserMessage :message="message" />
    </template>

## PropsCopy Anchor Link

Prop

Type

`message`UserMessage

`branchIndex?`number

`numberOfBranches?`number

## EventsCopy Anchor Link

The action callbacks are emitted as Vue events. Attaching a listener for an event also enables the corresponding control: the edit button only renders when an `@edit-message` listener is present, and the branch navigation only renders when a `@switch-to-branch` listener is present (and `numberOfBranches` is greater than 1).

Prop

Type

`edit-message?`(payload: { message: UserMessage }) => void

`switch-to-branch?`(payload: { message: UserMessage; branchIndex: number; numberOfBranches: number }) => void

## SlotsCopy Anchor Link

Each slot exposes scoped slot props (handlers and state) and falls back to the default rendering when not provided. Use a named template (`<template #slot-name="...">`) to override a slot.

Prop

Type

`message-renderer?`{ message: UserMessage; content: string; isMultiline: boolean }

`toolbar?`{ message: UserMessage; showBranchNavigation: boolean; hasEditAction: boolean }

`toolbar-items?`(no props)

`copy-button?`{ onCopy: () => Promise<void>; copied: boolean; label: string }

`edit-button?`{ onEdit: () => void; label: string }

`branch-navigation?`{ branchIndex: number; numberOfBranches: number; canGoPrev: boolean; canGoNext: boolean; goPrev: () => void; goNext: () => void }

`layout?`{ message; content; isMultiline; showBranchNavigation; hasEditAction; branchIndex; numberOfBranches; canGoPrev; canGoNext; onCopy; onEdit; goPrev; goNext; copied }

## UsageCopy Anchor Link

### Basic user messageCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotChatUserMessage } from "@copilotkit/vue/v2";
    import type { UserMessage } from "@ag-ui/core";
    
    defineProps<{ message: UserMessage }>();
    </script>
    
    <template>
      <CopilotChatUserMessage :message="message" />
    </template>

### With edit supportCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotChatUserMessage } from "@copilotkit/vue/v2";
    import type { UserMessage } from "@ag-ui/core";
    
    defineProps<{ message: UserMessage }>();
    
    function handleEdit(payload: { message: UserMessage }) {
      console.log("Edit", payload.message.id);
    }
    </script>
    
    <template>
      <CopilotChatUserMessage :message="message" @edit-message="handleEdit" />
    </template>

### With branch navigationCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { ref } from "vue";
    import { CopilotChatUserMessage } from "@copilotkit/vue/v2";
    import type { UserMessage } from "@ag-ui/core";
    
    defineProps<{ message: UserMessage; branches: UserMessage[] }>();
    
    const currentBranch = ref(0);
    
    function handleSwitch(payload: { branchIndex: number }) {
      currentBranch.value = payload.branchIndex;
    }
    </script>
    
    <template>
      <CopilotChatUserMessage
        :message="message"
        :branch-index="currentBranch"
        :number-of-branches="branches.length"
        @switch-to-branch="handleSwitch"
      />
    </template>

### Customizing appearance with slotsCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotChatUserMessage } from "@copilotkit/vue/v2";
    import type { UserMessage } from "@ag-ui/core";
    
    defineProps<{ message: UserMessage }>();
    </script>
    
    <template>
      <CopilotChatUserMessage
        :message="message"
        @edit-message="({ message }) => console.log('Edit:', message.id)"
      >
        <template #message-renderer="{ content }">
          <div class="rounded-2xl bg-blue-600 px-4 py-2 text-white">
            {{ content }}
          </div>
        </template>
        <template #toolbar-items>
          <button @click="$emit('pin')">Pin</button>
        </template>
      </CopilotChatUserMessage>
    </template>

### Full edit and branch workflowCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { ref } from "vue";
    import { CopilotChatUserMessage } from "@copilotkit/vue/v2";
    import type { UserMessage } from "@ag-ui/core";
    
    defineProps<{ message: UserMessage; branches: UserMessage[] }>();
    
    const currentBranch = ref(0);
    
    function openEditModal(message: UserMessage) {
      // open your edit modal
    }
    </script>
    
    <template>
      <CopilotChatUserMessage
        :message="message"
        :branch-index="currentBranch"
        :number-of-branches="branches.length"
        @switch-to-branch="({ branchIndex }) => (currentBranch = branchIndex)"
        @edit-message="({ message }) => openEditModal(message)"
      />
    </template>

## BehaviorCopy Anchor Link

  * **Right-aligned layout** : User messages are rendered with right-aligned positioning to visually distinguish them from assistant messages.
  * **Content flattening** : When `message.content` is an array of parts, the default renderer joins the `text` parts with newlines. String content is rendered as-is.
  * **Whitespace preservation** : The default message renderer uses `white-space: pre-wrap`, so line breaks and spacing are preserved. The bubble gets extra vertical padding when the content is multiline.
  * **Hover-revealed toolbar** : The toolbar is invisible by default and becomes visible when the message is hovered.
  * **Transient copied state** : After a successful copy, the copy button shows a check icon for 2 seconds before reverting.
  * **Conditional edit button** : The edit button only appears when an `@edit-message` listener is attached.
  * **Conditional branch navigation** : The branch navigation only appears when `numberOfBranches` is greater than 1 and a `@switch-to-branch` listener is attached.
  * **Localized labels** : Toolbar button tooltips are sourced from the nearest configuration provider. See [`useCopilotChatConfiguration`](https://docs.copilotkit.ai/reference/vue/hooks/useCopilotChatConfiguration) for available label keys.



How is this guide?

GoodBad

[Previous PageCopilotChatMessageView](https://docs.copilotkit.ai/reference/vue/components/CopilotChatMessageView)[Next PageCopilotChatView](https://docs.copilotkit.ai/reference/vue/components/CopilotChatView)
