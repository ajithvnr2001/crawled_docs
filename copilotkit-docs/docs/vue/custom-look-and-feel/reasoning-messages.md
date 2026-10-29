---
url: https://docs.copilotkit.ai/vue/custom-look-and-feel/reasoning-messages/
title: Reasoning Messages
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:46:22.340937+00:00
---

# Reasoning Messages

> Source: https://docs.copilotkit.ai/vue/custom-look-and-feel/reasoning-messages/

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

On this page

Custom Look and Feel

# Reasoning Messages

Customize the Vue display for reasoning messages emitted by an agent.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Some models emit reasoning tokens before their final response. CopilotKit surfaces the corresponding AG-UI reasoning messages automatically with a collapsible `CopilotChatReasoningMessage` card.

## Default Behavior#

When reasoning events arrive, the built-in Vue card:

  * Shows **Thinking…** with a pulsating indicator while reasoning is active.
  * Expands automatically while the latest reasoning message streams.
  * Collapses and switches to **Thought for X seconds** when streaming finishes.
  * Renders the content as Markdown.
  * Provides a chevron toggle so the user can review the content later.



No extra chat prop is required. If the selected agent emits reasoning messages, the default message view renders them.

## Customizing the Reasoning Message#

Compose a custom reasoning leaf in the `reasoning-message` slot of `CopilotChatMessageView`. The leaf itself provides scoped `header`, `content-view`, `toggle`, and `layout` slots.

Sub-component| Vue slot| Description  
---|---|---  
Header| `header`| Clickable bar with label and expand/collapse action.  
Content| `content-view`| Raw reasoning content and streaming state.  
Toggle| `toggle`| Expand/collapse wrapper data.  
Complete layout| `layout`| All message and subcomponent state for a full rearrangement.  
  
### Custom Header#

Replace the header to change its icon, label, or styling. It receives:

Prop| Type| Description  
---|---|---  
`isOpen`| `boolean`| Whether the content is expanded.  
`label`| `string`| `Thinking…` while streaming, then `Thought for X seconds`.  
`hasContent`| `boolean`| Whether reasoning text has arrived.  
`isStreaming`| `boolean`| Whether this latest reasoning message is streaming.  
`onClick`| `() => void` or `undefined`| Toggle action, present only when content exists.  
  
ChatWithReasoning.vue
    
    
    <script setup lang="ts">
    import {
      CopilotChat,
      CopilotChatMessageView,
      CopilotChatReasoningMessage,
    } from "@copilotkit/vue/v2";
    </script>
    
    <template>
      <CopilotChat>
        <template #message-view="{ messages, isRunning }">
          <CopilotChatMessageView :messages="messages" :is-running="isRunning">
            <template #reasoning-message="{ message, messages: allMessages, isRunning: running }">
              <CopilotChatReasoningMessage
                :message="message"
                :messages="allMessages"
                :is-running="running"
              >
                <template #header="{ label, isOpen, hasContent, onClick }">
                  <button type="button" :disabled="!hasContent" @click="onClick?.()">
                    {{ label }} {{ isOpen ? "Hide" : "Show" }}
                  </button>
                </template>
                <template #content-view="{ content, isStreaming }">
                  <pre>{{ content }}{{ isStreaming ? ' ▊' : '' }}</pre>
                </template>
              </CopilotChatReasoningMessage>
            </template>
          </CopilotChatMessageView>
        </template>
      </CopilotChat>
    </template>

Keep `onClick` attached when replacing the header; it owns the open/close transition and is intentionally absent when there is nothing to reveal.

### Custom Content#

Replace only the content area when the default header and toggle behavior are correct but the body needs a different presentation:
    
    
    <CopilotChatReasoningMessage
      :message="message"
      :messages="messages"
      :is-running="isRunning"
    >
      <template #content-view="{ content, hasContent, isStreaming }">
        <pre v-if="hasContent || isStreaming" class="reasoning-log">
          {{ content }}{{ isStreaming ? " ▊" : "" }}
        </pre>
      </template>
    </CopilotChatReasoningMessage>

The Vue slot uses `content` for the raw string; React's `children` prop is not part of this API.

## Fully Custom Reasoning Message#

For complete control, replace `reasoning-message` without composing the built-in leaf. The slot receives the same top-level state as the default component:

Prop| Type| Description  
---|---|---  
`message`| `ReasoningMessage`| Reasoning message; `.content` contains the text.  
`messages`| `Message[]`| All messages in the conversation.  
`isRunning`| `boolean`| Whether the agent is currently running.  
      
    
    <CopilotChatMessageView :messages="messages" :is-running="isRunning">
      <template #reasoning-message="{ message, isRunning: running }">
        <aside class="reasoning-banner" :data-streaming="running">
          <strong>Reasoning</strong>
          <pre>{{ message.content }}</pre>
        </aside>
      </template>
    </CopilotChatMessageView>

This replacement owns expansion, Markdown rendering, duration labels, and accessibility; none of the built-in card behavior is retained automatically.

## Layout Slot#

Vue does not use React's render-prop children pattern. The built-in reasoning leaf exposes a `layout` scoped slot with the message plus structured `header`, `contentView`, and `toggle` state:
    
    
    <CopilotChatReasoningMessage
      :message="message"
      :messages="messages"
      :is-running="isRunning"
    >
      <template #layout="{ header, contentView, toggle }">
        <section class="reasoning-card">
          <button type="button" :disabled="!header.hasContent" @click="header.onClick?.()">
            {{ header.label }}
          </button>
          <pre v-if="toggle.isOpen">{{ contentView.content }}</pre>
        </section>
      </template>
    </CopilotChatReasoningMessage>

Use `layout` only when you need to rearrange the whole card. The narrower `header`, `content-view`, and `toggle` slots preserve more of the default structure and behavior.

### On this page

Default BehaviorCustomizing the Reasoning MessageCustom HeaderCustom ContentFully Custom Reasoning MessageLayout Slot
