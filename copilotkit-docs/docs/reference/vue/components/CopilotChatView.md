---
url: https://docs.copilotkit.ai/reference/vue/components/CopilotChatView/
title: CopilotChatView
method: scrapling+scrapegraph
fetched_at: 2026-11-20T11:16:23.625707+00:00
---

# CopilotChatView

> Source: https://docs.copilotkit.ai/reference/vue/components/CopilotChatView/

Vue/Components

# CopilotChatView

Vue 3 layout component that combines a scrollable transcript with the input area

Copy MarkdownOpen

## OverviewCopy Anchor Link

`CopilotChatView` is a Vue 3 component that combines a scrollable message transcript with the chat input area, suggestion pills, a scroll-to-bottom button, an attachment queue, and an optional welcome screen. It is the visual core of the chat interface and is used internally by the higher-level chat components in `@copilotkit/vue`.

Every visual piece of `CopilotChatView` is exposed as a named **slot** , so you can replace, style, or extend any part of the layout (this is the Vue equivalent of React's render-prop sub-component customization). The component drives its own behavior (auto-scroll, mobile keyboard handling, resize observation) and emits events for the actions a parent needs to handle.

## ImportCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotChatView } from "@copilotkit/vue/v2";
    </script>

`CopilotChatView` is a presentational component. You supply messages and agent state and handle its emitted events. Input can be controlled with `inputValue`; when that prop is omitted, the component manages the input value locally.

## ExampleCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { ref } from "vue";
    import { CopilotChatView } from "@copilotkit/vue/v2";
    import type { Message } from "@ag-ui/core";
    
    const messages = ref<Message[]>([]);
    const isRunning = ref(false);
    
    function handleSubmit(value: string) {
      // append the user message, kick off your agent run, etc.
    }
    </script>
    
    <template>
      <CopilotChatView
        :messages="messages"
        :is-running="isRunning"
        auto-scroll="pin-to-bottom"
        @submit-message="handleSubmit"
      />
    </template>

## PropsCopy Anchor Link

Prop

Type

`messages?`Message[]

`autoScroll?`AutoScrollMode | boolean

`isRunning?`boolean

`suggestions?`Suggestion[]

`suggestionLoadingIndexes?`ReadonlyArray<number>

`welcomeScreen?`boolean

`attachments?`Attachment[]

`dragOver?`boolean

`inputValue?`string

`inputMode?`CopilotChatInputMode

`inputToolsMenu?`(ToolsMenuItem | "-")[]

`isConnecting?`boolean

`hasExplicitThreadId?`boolean

`onRemoveAttachment?`(id: string) => void

`onAddFile?`() => void

`onDragOver?`(event: DragEvent) => void

`onDragLeave?`(event: DragEvent) => void

`onDrop?`(event: DragEvent) => void

`onFinishTranscribeWithAudio?`(audioBlob: Blob) => void | Promise<void>

## EventsCopy Anchor Link

`CopilotChatView` emits the following events. Listen with `@event-name` in the template.

Prop

Type

`submit-message?`(value: string) => void

`stop?`() => void

`input-change?`(value: string) => void

`select-suggestion?`(suggestion: Suggestion, index: number) => void

`add-file?`() => void

`start-transcribe?`() => void

`cancel-transcribe?`() => void

`finish-transcribe?`() => void

## SlotsCopy Anchor Link

Each named slot has a sensible default. Override a slot to replace, restyle, or extend that part of the layout. Slots receive scoped props (data and handlers) that the default implementation also consumes, so a replacement can reuse them.

Prop

Type

`message-view?`{ messages: Message[]; isRunning: boolean }

`scroll-view?`{ messages: Message[]; isRunning: boolean; suggestions: Suggestion[]; loadingIndexes: ReadonlyArray<number>; messagePaddingBottom: string; showScrollToBottomButton: boolean; onSelectSuggestion: (suggestion, index) => void; onScroll: () => void; scrollToBottom: () => void }

`feather?`() => unknown

`scroll-to-bottom-button?`{ onClick: () => void }

`interrupt?`{ event: InterruptEvent; result: unknown; resolve: (response: unknown) => void }

`input?`{ modelValue: string; isRunning: boolean; inputMode: CopilotChatInputMode; inputToolsMenu: (ToolsMenuItem | '-')[]; attachments: Attachment[]; canStop: boolean; canAddFile: boolean; canTranscribe: boolean; onUpdateModelValue; onSubmitMessage; onStop; onAddFile; onStartTranscribe; onCancelTranscribe; onFinishTranscribe; onFinishTranscribeWithAudio }

`suggestion-view?`{ suggestions: Suggestion[]; loadingIndexes: ReadonlyArray<number>; onSelectSuggestion: (suggestion, index) => void }

`welcome-screen?`{ suggestions: Suggestion[]; loadingIndexes: ReadonlyArray<number>; attachments: Attachment[]; modelValue: string; isRunning: boolean; inputMode: CopilotChatInputMode; inputToolsMenu: (ToolsMenuItem | '-')[]; canStop: boolean; canAddFile: boolean; canTranscribe: boolean; onUpdateModelValue; onSubmitMessage; onStop; onAddFile; onStartTranscribe; onCancelTranscribe; onFinishTranscribe; onFinishTranscribeWithAudio; onSelectSuggestion }

`welcome-message?`() => unknown

## UsageCopy Anchor Link

### Standalone UsageCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { ref } from "vue";
    import { CopilotChatView } from "@copilotkit/vue/v2";
    import type { Message } from "@ag-ui/core";
    
    const messages = ref<Message[]>([]);
    const isRunning = ref(false);
    </script>
    
    <template>
      <CopilotChatView :messages="messages" :is-running="isRunning" />
    </template>

### Controlling the Input ValueCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { ref } from "vue";
    import { CopilotChatView } from "@copilotkit/vue/v2";
    
    const inputValue = ref("");
    
    function handleInputChange(value: string) {
      inputValue.value = value;
    }
    
    function handleSubmit(value: string) {
      // send the message, then clear the input
      inputValue.value = "";
    }
    </script>
    
    <template>
      <CopilotChatView
        :input-value="inputValue"
        @input-change="handleInputChange"
        @submit-message="handleSubmit"
      />
    </template>

### Replacing a SlotCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotChatView } from "@copilotkit/vue/v2";
    </script>
    
    <template>
      <CopilotChatView :messages="messages" :is-running="isRunning">
        <template #welcome-message>
          <h1 class="text-2xl font-semibold">How can I help you today?</h1>
        </template>
    
        <template #scroll-to-bottom-button="{ onClick }">
          <button type="button" @click="onClick">Jump to latest</button>
        </template>
      </CopilotChatView>
    </template>

### Custom Input via the `input` SlotCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotChatView } from "@copilotkit/vue/v2";
    </script>
    
    <template>
      <CopilotChatView :messages="messages" :is-running="isRunning">
        <template #input="{ modelValue, onUpdateModelValue, onSubmitMessage }">
          <form @submit.prevent="onSubmitMessage(modelValue)">
            <input
              :value="modelValue"
              @input="onUpdateModelValue(($event.target as HTMLInputElement).value)"
            />
            <button type="submit">Send</button>
          </form>
        </template>
      </CopilotChatView>
    </template>

## BehaviorCopy Anchor Link

  * **Auto-scroll** : `pin-to-bottom` keeps the latest message visible while the user is at the bottom; `pin-to-send` anchors the latest user message near the top while the assistant streams. A scroll-to-bottom button appears when the user scrolls up.
  * **Welcome screen** : Rendered when `messages` is empty and the welcome screen is not suppressed by `:welcome-screen="false"`, `isConnecting`, or `hasExplicitThreadId`. The welcome screen embeds the input and suggestion slots.
  * **Input overlay positioning** : The input is rendered in an absolutely positioned overlay at the bottom of the chat, and the scroll content is padded to avoid overlap. The component measures the overlay height with a `ResizeObserver` and keeps the padding in sync.
  * **Mobile keyboard** : The view tracks the on-screen keyboard height so the input can translate above the keyboard on mobile devices.



How is this guide?

GoodBad

[Previous PageCopilotChatUserMessage](https://docs.copilotkit.ai/reference/vue/components/CopilotChatUserMessage)[Next PageCopilotKitProvider](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider)
