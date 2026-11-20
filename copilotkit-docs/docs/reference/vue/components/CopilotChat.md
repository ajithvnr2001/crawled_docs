---
url: https://docs.copilotkit.ai/reference/vue/components/CopilotChat/
title: CopilotChat
method: scrapling+scrapegraph
fetched_at: 2026-11-20T11:16:23.762783+00:00
---

# CopilotChat

> Source: https://docs.copilotkit.ai/reference/vue/components/CopilotChat/

Vue/Components

# CopilotChat

Vue 3 component that connects an agent to a chat view

Copy MarkdownOpen

## OverviewCopy Anchor Link

`CopilotChat` is a high-level chat container that wires an agent into [`CopilotChatView`](https://docs.copilotkit.ai/reference/vue/components/CopilotChatView) while providing configuration context. `CopilotChat` handles these for you:

  * Resolves the agent with [`useAgent`](https://docs.copilotkit.ai/reference/vue/hooks/useAgent).
  * Shows the messages and running state of the agent.
  * Manages suggestions.
  * Handles the input value and audio transcription.
  * Manages file attachments.
  * Clears the input after a message is sent.



You typically only need to specify which agent to connect and, optionally, customize labels or override one of the named slots.

`CopilotChat` also exposes the underlying layout component as `CopilotChat.View`, which is the same component documented at [`CopilotChatView`](https://docs.copilotkit.ai/reference/vue/components/CopilotChatView). Use it directly when you want the layout without the agent wiring.

## ImportCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotChat } from "@copilotkit/vue/v2";
    import "@copilotkit/vue/styles.css";
    </script>

## PropsCopy Anchor Link

All reactive props are declared with `defineProps`. `CopilotChat` extends `CopilotChatView` props but omits the ones it manages internally (`messages`, `isRunning`, `suggestions`, `suggestionLoadingIndexes`, `attachments`, `onRemoveAttachment`, `onAddFile`, `dragOver`, `onDragOver`, `onDragLeave`, `onDrop`).

### Own propsCopy Anchor Link

Prop

Type

`agentId?`string

`threadId?`string

`throttleMs?`number

`labels?`Partial<CopilotChatLabels>

`attachments?`AttachmentsConfig

`onError?`(event: { error: Error; code: CopilotKitCoreErrorCode; context: Record<string, any> }) => void | Promise<void>

### Inherited CopilotChatView propsCopy Anchor Link

Prop

Type

`autoScroll?`AutoScrollMode | boolean

`welcomeScreen?`boolean

`inputValue?`string

`inputToolsMenu?`(ToolsMenuItem | "-")[]

`onFinishTranscribeWithAudio?`(audioBlob: Blob) => void | Promise<void>

## EventsCopy Anchor Link

`CopilotChat` emits the following events (listen with `@event-name` in templates). These fire in addition to the component's internal handling, so you can observe interactions without disabling default behavior.

Event| Payload| Fired when  
---|---|---  
`submit-message`| `value: string`| A message is submitted  
`stop`| none| The stop button is pressed  
`input-change`| `value: string`| The input value changes  
`select-suggestion`| `suggestion: Suggestion, index: number`| A suggestion pill is selected  
`add-file`| none| The add-file action is triggered  
`start-transcribe`| none| Audio transcription starts  
`cancel-transcribe`| none| Audio transcription is cancelled  
`finish-transcribe`| none| Audio transcription finishes  
  
## SlotsCopy Anchor Link

Vue uses named slots in place of React's render props and sub-component props. Provide a slot to replace the corresponding piece of the chat. Each slot receives scoped props you can destructure with `v-slot`. Any slot not listed below is forwarded down through `CopilotChatView` to the message view.

Prop

Type

`chat-view?`CopilotChatViewOverrideSlotProps

`message-view?`{ messages: Message[]; isRunning: boolean }

`input?`CopilotChatInputSlotProps

`suggestion-view?`CopilotChatSuggestionViewSlotProps

`welcome-screen?`CopilotChatWelcomeScreenSlotProps

`welcome-message?`() => unknown

`interrupt?`CopilotChatInterruptSlotProps

`generative-ui-surface?`GenerativeUIChatSurfaceSlotProps

Slots forwarded to the message view (for example custom assistant- or user-message slots) are passed straight through and rendered by `CopilotChatMessageView`. See [`CopilotChatView`](https://docs.copilotkit.ai/reference/vue/components/CopilotChatView) for the full set of layout-level slots such as `scroll-view`, `feather`, and `scroll-to-bottom-button`.

## UsageCopy Anchor Link

### Basic usageCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotChat } from "@copilotkit/vue/v2";
    import "@copilotkit/vue/styles.css";
    </script>
    
    <template>
      <CopilotChat
        agent-id="my-agent"
        :labels="{ chatInputPlaceholder: 'Ask me anything...' }"
      />
    </template>

### Custom welcome screenCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotChat } from "@copilotkit/vue/v2";
    </script>
    
    <template>
      <CopilotChat agent-id="my-agent">
        <template #welcome-screen="{ onSubmitMessage, suggestions, onSelectSuggestion }">
          <div class="flex h-full flex-col items-center justify-center gap-4">
            <h2>Welcome to the assistant</h2>
            <button
              v-for="(suggestion, index) in suggestions"
              :key="index"
              @click="onSelectSuggestion(suggestion, index)"
            >
              {{ suggestion.title }}
            </button>
          </div>
        </template>
      </CopilotChat>
    </template>

### Custom generative UI cardCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotChat } from "@copilotkit/vue/v2";
    </script>
    
    <template>
      <CopilotChat agent-id="my-agent">
        <template #generative-ui-surface="{ isStreaming, error, children }">
          <section class="my-card" :aria-busy="isStreaming">
            <p v-if="error" role="alert">{{ error.message }}</p>
            <component :is="children" v-if="children" />
          </section>
        </template>
      </CopilotChat>
    </template>

### Observing eventsCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotChat } from "@copilotkit/vue/v2";
    
    function onSubmit(value: string) {
      console.log("user submitted:", value);
    }
    </script>
    
    <template>
      <CopilotChat agent-id="my-agent" @submit-message="onSubmit" />
    </template>

### Using the layout directlyCopy Anchor Link

`CopilotChat.View` is the layout component without agent wiring. Use it when you manage `messages` and handlers yourself.

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotChat } from "@copilotkit/vue/v2";
    import { ref } from "vue";
    
    // Vue SFC templates cannot resolve dotted tags like `<CopilotChat.View>`,
    // so alias the layout to a local component first.
    const ChatView = CopilotChat.View;
    
    const messages = ref([]);
    
    function handleSubmit(value: string) {
      // manage your own message state
    }
    </script>
    
    <template>
      <ChatView :messages="messages" @submit-message="handleSubmit" />
    </template>

How is this guide?

GoodBad

[Previous PageOverview](https://docs.copilotkit.ai/reference/vue)[Next PageCopilotChatAssistantMessage](https://docs.copilotkit.ai/reference/vue/components/CopilotChatAssistantMessage)
