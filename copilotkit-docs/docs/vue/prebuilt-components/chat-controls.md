---
url: https://docs.copilotkit.ai/vue/prebuilt-components/chat-controls/
title: Open, close, and feedback
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:46:28.948816+00:00
---

# Open, close, and feedback

> Source: https://docs.copilotkit.ai/vue/prebuilt-components/chat-controls/

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

[Prebuilt Components](https://docs.copilotkit.ai/vue/prebuilt-components)

# Open, close, and feedback

Control a Vue popup or sidebar from your UI and capture assistant-message feedback.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Two common controls for the prebuilt chat are opening it from your own UI and capturing thumbs-up or thumbs-down feedback on assistant messages.

## Programmatically open or close chat#

Use the `toggle-button` scoped slot on `CopilotPopup` or `CopilotSidebar` to replace the launcher with your own UI. The slot receives the current open state and `toggle`, `open`, and `close` actions:

App.vue
    
    
    <script setup lang="ts">
    import { CopilotPopup } from "@copilotkit/vue/v2";
    </script>
    
    <template>
      <CopilotPopup agent-id="my-agent">
        <template #toggle-button="{ isOpen, toggle }">
          <button type="button" @click="toggle">
            {{ isOpen ? "Close chat" : "Ask the assistant" }}
          </button>
        </template>
      </CopilotPopup>
    </template>

Set the initial state declaratively with `:default-open="true"` on `CopilotPopup` or `CopilotSidebar`. These Vue components do not expose a controlled `open` / `onOpenChange`-style API; use the scoped-slot actions to control the surface after it mounts.

## Capture message feedback#

Vue exposes assistant-message feedback as events. To render the default assistant message but observe its actions, provide it through the `assistant-message` slot of `CopilotChatMessageView`:

ChatWithFeedback.vue
    
    
    <script setup lang="ts">
    import {
      CopilotChat,
      CopilotChatAssistantMessage,
      CopilotChatMessageView,
    } from "@copilotkit/vue/v2";
    
    function recordFeedback(message: { id: string }, value: "up" | "down") {
      analytics.track("feedback", { messageId: message.id, value });
    }
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
                @thumbs-up="recordFeedback($event, 'up')"
                @thumbs-down="recordFeedback($event, 'down')"
              />
            </template>
          </CopilotChatMessageView>
        </template>
      </CopilotChat>
    </template>

The buttons are part of `CopilotChatAssistantMessage`; custom `thumbs-up-button` and `thumbs-down-button` slots receive their imperative `onThumbsUp` and `onThumbsDown` actions. Labels are controlled with the chat configuration's `labels` prop.

### On this page

Programmatically open or close chatCapture message feedback
