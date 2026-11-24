---
url: https://docs.copilotkit.ai/reference/vue/components/CopilotChatAssistantMessage/
title: CopilotChatAssistantMessage
method: scrapling+scrapegraph
fetched_at: 2026-11-24T13:30:46.708489+00:00
---

# CopilotChatAssistantMessage

> Source: https://docs.copilotkit.ai/reference/vue/components/CopilotChatAssistantMessage/

Vue/Components

# CopilotChatAssistantMessage

Vue 3 component for displaying assistant messages with Markdown, tool calls, and an action toolbar

Copy MarkdownOpen

## OverviewCopy Anchor Link

`CopilotChatAssistantMessage` is a Vue 3 component that displays assistant messages with Markdown support, tool call rendering, and an action toolbar. [`CopilotChatMessageView`](https://docs.copilotkit.ai/reference/vue/components/CopilotChatMessageView) renders it as the default assistant message. For user messages, see [`CopilotChatUserMessage`](https://docs.copilotkit.ai/reference/vue/components/CopilotChatUserMessage).

Markdown is rendered with `streamdown-vue` (`StreamMarkdown`):

  * GitHub Flavored Markdown tables, with copy and download actions.
  * Math expressions. KaTeX styles load automatically.
  * Code blocks highlighted by Shiki (`github-light` and `github-dark` themes), with copy and download actions.
  * Images, with a download button on hover.



The toolbar provides copy, thumbs up, thumbs down, read aloud, and regenerate buttons. Tooltip and aria labels are sourced from the nearest `CopilotChatConfigurationProvider` (see [`useCopilotChatConfiguration`](https://docs.copilotkit.ai/reference/vue/hooks/useCopilotChatConfiguration)). The thumbs up, thumbs down, read aloud, and regenerate buttons are only rendered when a listener for the corresponding event is attached; the copy button is always shown when the toolbar is visible.

The toolbar is hidden while the latest assistant message is still streaming (when `isRunning` is `true` for the last message) and when the message has no text content. It also respects the `toolbarVisible` prop.

## ImportCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotChatAssistantMessage } from "@copilotkit/vue/v2";
    </script>

## ExampleCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotChatAssistantMessage } from "@copilotkit/vue/v2";
    import type { AssistantMessage } from "@ag-ui/core";
    
    const message: AssistantMessage = {
      id: "1",
      role: "assistant",
      content: "Here is **Markdown** with a `code` sample.",
    };
    </script>
    
    <template>
      <CopilotChatAssistantMessage
        :message="message"
        @thumbs-up="(msg) => console.log('Thumbs up:', msg.id)"
        @thumbs-down="(msg) => console.log('Thumbs down:', msg.id)"
      />
    </template>

## PropsCopy Anchor Link

Prop

Type

`message`AssistantMessage

`messages?`Message[]

`isRunning?`boolean

`toolbarVisible?`boolean

## EventsCopy Anchor Link

Each event emits the current `message` as its payload. Attaching a listener for `thumbs-up`, `thumbs-down`, `read-aloud`, or `regenerate` also causes the matching toolbar button to render; without a listener the button is omitted.

Prop

Type

`thumbs-up?`(message: AssistantMessage) => void

`thumbs-down?`(message: AssistantMessage) => void

`read-aloud?`(message: AssistantMessage) => void

`regenerate?`(message: AssistantMessage) => void

Copying the message to the clipboard is handled internally by the copy button. There is no `copy` event; the copy button is always present when the toolbar is visible.

## SlotsCopy Anchor Link

The component exposes named slots so you can override individual pieces of the default layout. Each slot receives scoped props (shown below) that wire its behavior to the message and toolbar handlers.

Prop

Type

`layout?`slot

`message-renderer?`slot

`tool-calls-view?`slot

`toolbar?`slot

`copy-button?`slot

`thumbs-up-button?`slot

`thumbs-down-button?`slot

`read-aloud-button?`slot

`regenerate-button?`slot

`toolbar-items?`slot

## UsageCopy Anchor Link

### Basic assistant messageCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotChatAssistantMessage } from "@copilotkit/vue/v2";
    import type { AssistantMessage } from "@ag-ui/core";
    
    defineProps<{ message: AssistantMessage }>();
    </script>
    
    <template>
      <CopilotChatAssistantMessage
        :message="message"
        @thumbs-up="(msg) => console.log('Thumbs up:', msg.id)"
        @thumbs-down="(msg) => console.log('Thumbs down:', msg.id)"
      />
    </template>

### Adding regenerate and read aloudCopy Anchor Link

Attaching the listeners makes the corresponding buttons appear automatically.

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotChatAssistantMessage } from "@copilotkit/vue/v2";
    import type { AssistantMessage } from "@ag-ui/core";
    
    defineProps<{ message: AssistantMessage }>();
    
    function handleRegenerate(msg: AssistantMessage) {
      // re-run the agent for this message
    }
    
    function handleReadAloud(msg: AssistantMessage) {
      // speak msg.content
    }
    </script>
    
    <template>
      <CopilotChatAssistantMessage
        :message="message"
        @regenerate="handleRegenerate"
        @read-aloud="handleReadAloud"
      />
    </template>

### Adding custom toolbar itemsCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotChatAssistantMessage } from "@copilotkit/vue/v2";
    import type { AssistantMessage } from "@ag-ui/core";
    
    defineProps<{ message: AssistantMessage }>();
    </script>
    
    <template>
      <CopilotChatAssistantMessage :message="message">
        <template #toolbar-items>
          <button type="button" @click="shareMessage(message)">Share</button>
        </template>
      </CopilotChatAssistantMessage>
    </template>

### Hiding the toolbarCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotChatAssistantMessage } from "@copilotkit/vue/v2";
    import type { AssistantMessage } from "@ag-ui/core";
    
    defineProps<{ message: AssistantMessage }>();
    </script>
    
    <template>
      <CopilotChatAssistantMessage :message="message" :toolbar-visible="false" />
    </template>

### Custom Markdown rendererCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotChatAssistantMessage } from "@copilotkit/vue/v2";
    import type { AssistantMessage } from "@ag-ui/core";
    
    defineProps<{ message: AssistantMessage }>();
    </script>
    
    <template>
      <CopilotChatAssistantMessage :message="message">
        <template #message-renderer="{ content }">
          <div class="custom-markdown">{{ content }}</div>
        </template>
      </CopilotChatAssistantMessage>
    </template>

### Customizing a toolbar buttonCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotChatAssistantMessage } from "@copilotkit/vue/v2";
    import type { AssistantMessage } from "@ag-ui/core";
    
    defineProps<{ message: AssistantMessage }>();
    </script>
    
    <template>
      <CopilotChatAssistantMessage
        :message="message"
        @regenerate="(msg) => regenerate(msg)"
      >
        <template #regenerate-button="{ onRegenerate, label }">
          <button type="button" :title="label" @click="onRegenerate">
            Regenerate
          </button>
        </template>
      </CopilotChatAssistantMessage>
    </template>

How is this guide?

GoodBad

[Previous PageCopilotChat](https://docs.copilotkit.ai/reference/vue/components/CopilotChat)[Next PageCopilotChatInput](https://docs.copilotkit.ai/reference/vue/components/CopilotChatInput)
