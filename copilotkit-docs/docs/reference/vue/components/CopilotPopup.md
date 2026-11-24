---
url: https://docs.copilotkit.ai/reference/vue/components/CopilotPopup/
title: CopilotPopup
method: scrapling+scrapegraph
fetched_at: 2026-11-24T13:30:46.566883+00:00
---

# CopilotPopup

> Source: https://docs.copilotkit.ai/reference/vue/components/CopilotPopup/

Vue/Components

# CopilotPopup

Vue 3 popup variant of CopilotChat that renders in a floating panel with a toggle button.

Copy MarkdownOpen

This is the Vue 3 popup component. Import it from `@copilotkit/vue/v2`.

`CopilotPopup` renders a floating chat popup with a toggle button. It wraps [`CopilotChat`](https://docs.copilotkit.ai/reference/vue/components/CopilotChat) and provides popup-specific layout, sizing, and open/close behavior. The popup includes a header with a title and close button, and can optionally be dismissed by clicking outside.

The `"popup"` feature requires a license. When it is not licensed, the component renders an inline warning and logs a console warning; see [copilotkit.ai/pricing](https://copilotkit.ai/pricing).

## ExampleCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotPopup } from "@copilotkit/vue/v2";
    </script>
    
    <template>
      <CopilotPopup
        agent-id="my-agent"
        :labels="{ modalHeaderTitle: 'Assistant' }"
      />
    </template>

## PropsCopy Anchor Link

### Own propsCopy Anchor Link

Prop

Type

`defaultOpen?`boolean

`width?`number | string

`height?`number | string

`clickOutsideToClose?`boolean

### Inherited CopilotChat propsCopy Anchor Link

`CopilotPopup` extends [`CopilotChatProps`](https://docs.copilotkit.ai/reference/vue/components/CopilotChat), so it accepts the same agent-wiring and chat-view props. The most common ones:

Prop

Type

`agentId?`string

`threadId?`string

`labels?`Partial<CopilotChatLabels>

`autoScroll?`AutoScrollMode | boolean

`welcomeScreen?`boolean

`inputValue?`string

`inputMode?`CopilotChatInputMode

`inputToolsMenu?`(ToolsMenuItem | "-")[]

`onError?`(event: { error: Error; code: CopilotKitCoreErrorCode; context: Record<string, any> }) => void | Promise<void>

## SlotsCopy Anchor Link

All slots are forwarded down to the internal `CopilotPopupView`. Each slot receives scoped props you can bind to.

Prop

Type

`header?`(props: CopilotPopupViewHeaderSlotProps) => unknown

`toggle-button?`(props: CopilotPopupViewToggleButtonSlotProps) => unknown

`chat-view?`(props: CopilotChatViewOverrideSlotProps) => unknown

`message-view?`(props: CopilotChatMessageViewSlotProps) => unknown

`input?`(props: CopilotSidebarWelcomeScreenInputSlotProps) => unknown

`suggestion-view?`(props: CopilotSidebarWelcomeScreenSuggestionViewSlotProps) => unknown

`welcome-screen?`(props: CopilotChatWelcomeScreenSlotProps) => unknown

`welcome-message?`() => unknown

`generative-ui-surface?`(props: GenerativeUIChatSurfaceSlotProps) => unknown

## EventsCopy Anchor Link

`CopilotPopup` emits the following events (use kebab-case in templates):

Event| Payload  
---|---  
`submit-message`| `value: string`  
`stop`| (none)  
`input-change`| `value: string`  
`select-suggestion`| `suggestion: Suggestion, index: number`  
`add-file`| (none)  
`start-transcribe`| (none)  
`cancel-transcribe`| (none)  
`finish-transcribe`| (none)  
  
## UsageCopy Anchor Link

### Basic usageCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotPopup } from "@copilotkit/vue/v2";
    </script>
    
    <template>
      <CopilotPopup
        agent-id="my-agent"
        :labels="{ modalHeaderTitle: 'Assistant' }"
      />
    </template>

### Custom size and click-outside-to-closeCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotPopup } from "@copilotkit/vue/v2";
    </script>
    
    <template>
      <CopilotPopup
        agent-id="my-agent"
        :default-open="false"
        :width="450"
        height="80vh"
        :click-outside-to-close="true"
      />
    </template>

### Custom header slotCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotPopup } from "@copilotkit/vue/v2";
    </script>
    
    <template>
      <CopilotPopup agent-id="my-agent">
        <template #header="{ title, onClose }">
          <div class="flex items-center justify-between bg-blue-600 px-4 py-2 text-white">
            <span>{{ title }}</span>
            <button type="button" @click="onClose">Close</button>
          </div>
        </template>
      </CopilotPopup>
    </template>

### Handling eventsCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotPopup } from "@copilotkit/vue/v2";
    
    function onSubmit(value: string) {
      console.log("submitted:", value);
    }
    </script>
    
    <template>
      <CopilotPopup agent-id="my-agent" @submit-message="onSubmit" />
    </template>

## BehaviorCopy Anchor Link

  * **Toggle button** : Renders a floating toggle button that opens and closes the popup. Override it with the `toggle-button` slot.
  * **Modal state** : The initial state is set by `defaultOpen`; after mount, state changes come from user interaction (toggle button, close button, clicking outside).
  * **Click outside** : When `clickOutsideToClose` is `true`, clicking outside the popup panel closes it. The default is `false`.
  * **Layout** : Internally uses `CopilotPopupView`, which provides a popup-specific welcome screen layout.
  * **Agent connection** : All agent wiring (messages, running state, suggestions) is handled by the inner `CopilotChat`.



How is this guide?

GoodBad

[Previous PageCopilotKitProvider](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider)[Next PageCopilotSidebar](https://docs.copilotkit.ai/reference/vue/components/CopilotSidebar)
