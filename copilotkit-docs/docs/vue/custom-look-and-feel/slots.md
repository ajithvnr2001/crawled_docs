---
url: https://docs.copilotkit.ai/vue/custom-look-and-feel/slots/
title: Slots (Subcomponents)
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:46:22.479031+00:00
---

# Slots (Subcomponents)

> Source: https://docs.copilotkit.ai/vue/custom-look-and-feel/slots/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendVueAgent backendCopilotKit

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Quickstart](https://docs.copilotkit.ai/vue)[Using these docs](https://docs.copilotkit.ai/vue/using-these-docs)[Build with agents](https://docs.copilotkit.ai/vue/build-with-agents)[Intelligence](https://docs.copilotkit.ai/vue/intelligence/overview)

Basics

Chat

[Prebuilt Components](https://docs.copilotkit.ai/vue/prebuilt-components)

Custom Look and Feel

[Slots](https://docs.copilotkit.ai/vue/custom-look-and-feel/slots)[Headless UI](https://docs.copilotkit.ai/vue/custom-look-and-feel/headless-ui)

[Programmatic Control](https://docs.copilotkit.ai/vue/programmatic-control)

Threads

[Frontend-tools](https://docs.copilotkit.ai/vue/frontend-tools)

Generative UI

Controlled

Open-ended

Interactivity

Shared state

Human-in-the-loop

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

Slots

BasicsChatCustom Look and Feel

# Slots (Subcomponents)

Customize Vue chat surfaces with named and scoped slots.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

Every CopilotKit Vue chat component is composed from named slots. Use them to replace one visible piece while retaining the runtime connection, reactive message state, streaming behavior, and the rest of the prebuilt surface.

Vue offers three practical levels of slot customization:

  1. **Classes and attributes on public leaves** — compose a leaf such as `CopilotChatMessageView` and pass `class` or other attributes to it.
  2. **Scoped-slot composition** — consume the slot's data and actions while replacing only that part of the template.
  3. **Custom components** — render your own Vue component inside the slot.



Slots are recursive: a root `message-view` slot can render the public message view, whose `assistant-message` slot can render the public assistant leaf, whose `copy-button` slot can replace one toolbar control. This is Vue's native equivalent of the React slot-object hierarchy; React-style component or props-override objects are not Vue APIs.

## What it looks like in code#

The examples below replace the same three surfaces as the root guide: the welcome screen, assistant message card, and input disclaimer.

### Welcome screen slot#

The `welcome-screen` slot replaces the empty state shown before the first message. Its scoped props include the input and suggestion actions, so a custom screen can still submit a message through the existing chat:

SupportChat.vue
    
    
    <script setup lang="ts">
    import { CopilotChat } from "@copilotkit/vue/v2";
    </script>
    
    <template>
      <CopilotChat>
        <template #welcome-screen="{ onSubmitMessage }">
          <section class="welcome-card">
            <h2>How can we help?</h2>
            <button type="button" @click="onSubmitMessage('Show my open tickets')">
              Show my open tickets
            </button>
          </section>
        </template>
      </CopilotChat>
    </template>

### Assistant message slot#

Use the `message-view` slot to compose the public message leaf components, then customize their own slots or events. This keeps the component hierarchy and provider ancestry intact:

SupportChat.vue
    
    
    <script setup lang="ts">
    import {
      CopilotChat,
      CopilotChatAssistantMessage,
      CopilotChatMessageView,
    } from "@copilotkit/vue/v2";
    </script>
    
    <template>
      <CopilotChat>
        <template #message-view="{ messages, isRunning }">
          <CopilotChatMessageView :messages="messages" :is-running="isRunning">
            <template #assistant-message="{ message, messages: allMessages, isRunning: running }">
              <CopilotChatAssistantMessage
                :message="message"
                :messages="allMessages"
                :is-running="running"
              >
                <template #toolbar-items>
                  <span class="reviewed-badge">Reviewed</span>
                </template>
              </CopilotChatAssistantMessage>
            </template>
          </CopilotChatMessageView>
        </template>
      </CopilotChat>
    </template>

The message components expose further named slots for user messages, assistant toolbars and buttons, tool calls, reasoning messages, and activity messages. For activity rendering, `CopilotChatMessageView` first looks for `activity-<activityType>`, then `activity-message`.

### Disclaimer slot#

The input's `disclaimer` slot replaces the text below the composer while leaving the textarea, send button, attachments, and transcription controls alone:
    
    
    <CopilotChat>
      <template #input="inputProps">
        <CopilotChatInput v-bind="inputProps">
          <template #disclaimer>
            <p class="support-disclaimer">Responses may be inaccurate.</p>
          </template>
        </CopilotChatInput>
      </template>
    </CopilotChat>

## Tailwind Classes#

Vue does not accept a Tailwind string in place of a slot. Add `class` to the public leaf you compose inside the scoped slot, or add classes to your own markup:
    
    
    <CopilotChat>
      <template #message-view="{ messages, isRunning }">
        <CopilotChatMessageView
          class="rounded-xl bg-gray-50 p-4 dark:bg-gray-900"
          :messages="messages"
          :is-running="isRunning"
        />
      </template>
    </CopilotChat>

## Props Override#

React's slot-object props override has no direct Vue equivalent. Bind props, listeners, and attributes to the public Vue leaf rendered inside the slot:
    
    
    <CopilotChat>
      <template #message-view="slotProps">
        <CopilotChatMessageView
          v-bind="slotProps"
          class="my-custom-messages"
          data-testid="message-view"
        />
      </template>
    </CopilotChat>

## Custom Components#

For full control, render your own component. It receives the scoped data you choose to pass through:
    
    
    <CopilotChat>
      <template #message-view="{ messages, isRunning }">
        <CustomMessageView :messages="messages" :is-running="isRunning" />
      </template>
    </CopilotChat>

Once you replace a complete slot, your component owns that part's rendering. Compose public leaves when you want to preserve CopilotKit's default behavior.

## Nested Slots (Drill-Down)#

Named slots nest through public Vue leaves instead of nested configuration objects.

### Two levels deep#

Override the assistant toolbar while keeping the default message renderer:
    
    
    <CopilotChat>
      <template #message-view="{ messages, isRunning }">
        <CopilotChatMessageView :messages="messages" :is-running="isRunning">
          <template #assistant-message="assistantProps">
            <CopilotChatAssistantMessage v-bind="assistantProps">
              <template #toolbar-items>
                <CustomToolbarAction />
              </template>
            </CopilotChatAssistantMessage>
          </template>
        </CopilotChatMessageView>
      </template>
    </CopilotChat>

### Three levels deep#

Replace a specific toolbar button and keep its imperative action attached:
    
    
    <CopilotChatAssistantMessage v-bind="assistantProps">
      <template #copy-button="{ onCopy }">
        <button type="button" @click="onCopy">Copy response</button>
      </template>
    </CopilotChatAssistantMessage>

## Labels#

Use the `labels` prop on a prebuilt surface for text-only changes:
    
    
    <CopilotChat
      :labels="{
        chatInputPlaceholder: 'Ask your agent anything…',
        welcomeMessageText: 'How can I help you today?',
        chatDisclaimerText: 'AI responses may be inaccurate.',
      }"
    />

Use slots for structure and behavior, and labels for the existing user-facing copy.

## Available Slots#

### `CopilotChat` / `CopilotSidebar` / `CopilotPopup`#

The chat surfaces expose these root slots. Most are scoped with the state and actions needed to preserve the default behavior:

Slot| Description  
---|---  
`chat-view`| Complete chat view, including message, input, suggestion, attachment, and transcription state.  
`message-view`| Message-list composition; receives `messages` and `isRunning`.  
`scroll-view`| Scroll container, scroll actions, suggestions, and bottom-button state.  
`input`| Composer state plus submit, stop, attachment, and transcription actions.  
`suggestion-view`| Suggestion collection, loading indexes, and selection action.  
`welcome-screen`| Initial empty state with input and suggestion data.  
`welcome-message`| Only the default welcome copy area.  
`interrupt`| A pending interrupt and its resolver.  
  
`CopilotSidebar` and `CopilotPopup` additionally expose:

Slot| Description  
---|---  
`header`| Modal header with open state and close actions.  
`toggle-button`| Launcher with `isOpen`, `toggle`, `open`, and `close`.  
  
### `CopilotChatMessageView`#

Slot| Description  
---|---  
`assistant-message`| Assistant message plus the full message list and run state.  
`user-message`| User message.  
`reasoning-message`| Reasoning message plus message list and run state.  
`tool-call-<name>`| One named tool-call renderer.  
`tool-call`| Fallback tool-call renderer.  
`activity-<type>`| One named activity-message renderer.  
`activity-message`| Fallback activity-message renderer.  
`message-before` / `message-after`| Metadata-aware content around each message.  
`cursor`| Streaming cursor.  
  
### Public message and input leaves#

  * `CopilotChatAssistantMessage` exposes `layout`, `message-renderer`, `tool-calls-view`, `toolbar`, `toolbar-items`, and individual copy, feedback, read-aloud, and regenerate button slots.
  * `CopilotChatUserMessage` exposes `layout`, `message-renderer`, `toolbar`, `toolbar-items`, copy/edit buttons, and branch navigation.
  * `CopilotChatInput` exposes `layout`, `text-area`, `disclaimer`, `add-menu-button`, `audio-recorder`, and the send/transcription controls.



Use the narrowest slot that expresses the change. It preserves more built-in behavior and reduces the amount of state and accessibility wiring you own.

### On this page

What is this?What it looks like in codeWelcome screen slotAssistant message slotDisclaimer slotTailwind ClassesProps OverrideCustom ComponentsNested Slots (Drill-Down)Two levels deepThree levels deepLabelsAvailable SlotsCopilotChat / CopilotSidebar / CopilotPopupCopilotChatMessageViewPublic message and input leaves
