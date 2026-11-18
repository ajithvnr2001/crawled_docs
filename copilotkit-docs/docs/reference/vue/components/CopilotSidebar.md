---
url: https://docs.copilotkit.ai/reference/vue/components/CopilotSidebar/
title: CopilotSidebar
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:56.780340+00:00
---

# CopilotSidebar

> Source: https://docs.copilotkit.ai/reference/vue/components/CopilotSidebar/

Vue/Components

# CopilotSidebar

Sidebar variant of CopilotChat that renders in a fixed side panel

Copy MarkdownOpen

## OverviewCopy Anchor Link

`CopilotSidebar` renders a fixed sidebar panel for chat interaction. It wraps [`CopilotChat`](https://docs.copilotkit.ai/reference/vue/components/CopilotChat) and provides sidebar-specific layout and open/close behavior. The sidebar includes a header with a title and a close button, and can be toggled via a floating toggle button.

Because it builds on `CopilotChat`, it resolves the agent, subscribes to messages and running state, manages suggestions, and wires input and transcription for you. You typically only need to pick the agent and, optionally, set the initial open state, width, or override one of the named slots.

The `sidebar` feature requires a license. When it is not licensed, the component renders an inline warning and logs a console warning. Visit [copilotkit.ai/pricing](https://copilotkit.ai/pricing) for details.

## ImportCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotSidebar } from "@copilotkit/vue/v2";
    import "@copilotkit/vue/styles.css";
    </script>

## PropsCopy Anchor Link

`CopilotSidebar` extends the `CopilotChat` props (and through them the inherited `CopilotChatView` props) and adds two of its own.

### Own propsCopy Anchor Link

Prop

Type

`defaultOpen?`boolean

`width?`number | string

### Inherited CopilotChat propsCopy Anchor Link

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

`inputMode?`"input" | "transcribe" | "processing"

`inputToolsMenu?`(ToolsMenuItem | "-")[]

`onFinishTranscribeWithAudio?`(audioBlob: Blob) => void | Promise<void>

## EventsCopy Anchor Link

`CopilotSidebar` re-emits the chat events from `CopilotChat` (listen with `@event-name` in templates). These fire in addition to the component's internal handling.

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

Vue uses named slots in place of React's render props and sub-component props. Provide a slot to replace the corresponding piece of the sidebar. Each slot receives scoped props you can destructure with `v-slot`.

Prop

Type

`header?`{ title: string; onClose: () => void; isOpen: boolean }

`toggle-button?`{ isOpen: boolean; toggle: () => void; open: () => void; close: () => void }

`chat-view?`CopilotChatViewOverrideSlotProps

`message-view?`{ messages: Message[]; isRunning: boolean }

`input?`CopilotSidebarWelcomeScreenInputSlotProps

`suggestion-view?`CopilotSidebarWelcomeScreenSuggestionViewSlotProps

`welcome-screen?`CopilotChatWelcomeScreenSlotProps

`welcome-message?`() => unknown

`generative-ui-surface?`GenerativeUIChatSurfaceSlotProps

The sidebar welcome screen shows the welcome message in the middle, and the suggestions and the input at the bottom. Override the `welcome-screen` slot to replace this layout entirely, or `welcome-message` to change just the greeting.

## UsageCopy Anchor Link

### Basic usageCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotSidebar } from "@copilotkit/vue/v2";
    import "@copilotkit/vue/styles.css";
    </script>
    
    <template>
      <CopilotSidebar
        agent-id="my-agent"
        :labels="{ chatInputPlaceholder: 'Ask me anything...' }"
      />
    </template>

### Closed on mount with a custom widthCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotSidebar } from "@copilotkit/vue/v2";
    </script>
    
    <template>
      <CopilotSidebar agent-id="my-agent" :default-open="false" :width="500" />
    </template>

### Custom headerCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotSidebar } from "@copilotkit/vue/v2";
    </script>
    
    <template>
      <CopilotSidebar agent-id="my-agent">
        <template #header="{ title, onClose }">
          <div class="flex items-center justify-between bg-indigo-700 px-4 py-3 text-white">
            <span>{{ title }}</span>
            <button @click="onClose">Close</button>
          </div>
        </template>
      </CopilotSidebar>
    </template>

### Custom toggle buttonCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotSidebar } from "@copilotkit/vue/v2";
    </script>
    
    <template>
      <CopilotSidebar agent-id="my-agent">
        <template #toggle-button="{ isOpen, toggle }">
          <button class="fixed bottom-6 right-6" @click="toggle">
            {{ isOpen ? "Close chat" : "Open chat" }}
          </button>
        </template>
      </CopilotSidebar>
    </template>

### Observing eventsCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotSidebar } from "@copilotkit/vue/v2";
    
    function onSubmit(value: string) {
      console.log("user submitted:", value);
    }
    </script>
    
    <template>
      <CopilotSidebar agent-id="my-agent" @submit-message="onSubmit" />
    </template>

How is this guide?

GoodBad

[Previous PageCopilotPopup](https://docs.copilotkit.ai/reference/vue/components/CopilotPopup)[Next PageCopilotThreadsDrawer](https://docs.copilotkit.ai/reference/vue/components/CopilotThreadsDrawer)
