---
url: https://docs.copilotkit.ai/vue/generative-ui/reasoning/
title: Reasoning
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:46:22.936829+00:00
---

# Reasoning

> Source: https://docs.copilotkit.ai/vue/generative-ui/reasoning/

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

[Build Generative UI](https://docs.copilotkit.ai/vue/generative-ui)

# Reasoning

Surface the agent's thinking chain in the chat — default or fully custom.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

Some models emit **reasoning tokens** , internal reasoning traces that explain how the model is working toward its answer. CopilotKit surfaces these as first-class messages: when a `REASONING_MESSAGE_*` event arrives from the agent, the chat renders it inline so the user can follow the agent's thinking.

Reasoning isn't a custom-renderer plumb-in; it's a dedicated message type on the chat view. You can either accept the built-in rendering or override the `reasoning-message` scoped slot with your own component.

## When should I use this?#

Expose reasoning in the UI when you want to:

  * Give users real-time insight into the agent's thought process
  * Show progress on long or multi-step problems
  * Debug prompt behavior during development
  * Brand the reasoning card to match the rest of your product



## Default reasoning rendering (zero-config)#

Out of the box, reasoning events render inside CopilotKit's built-in `CopilotChatReasoningMessage` card:

  * A **"Thinking…"** label with a pulsing indicator while the model reasons.
  * Auto-expanded content so users can follow the reasoning live.
  * Collapses to **"Thought for X seconds"** once reasoning finishes, with a chevron to re-expand.
  * Reasoning text rendered as Markdown.



No configuration is needed; if your model emits reasoning tokens, the card appears automatically:

src/App.vue
    
    
    <script setup lang="ts">
    import { CopilotChat, CopilotKitProvider } from "@copilotkit/vue/v2";
    </script>
    
    <template>
      <CopilotKitProvider runtime-url="/api/copilotkit">
        <main style="height: 100dvh"><CopilotChat /></main>
      </CopilotKitProvider>
    </template>

## Custom reasoning rendering#

For full control over the reasoning card, use the `reasoning-message` scoped slot. The slot receives the `ReasoningMessage` object (`.content` holds the streaming text), the full `messages` list, and `isRunning`, enough to decide whether this block is still streaming and whether it's the active trailing message:

src/AgentChat.vue
    
    
    <script setup lang="ts">
    import { CopilotChat } from "@copilotkit/vue/v2";
    </script>
    
    <template>
      <CopilotChat>
        <template #reasoning-message="{ message, isRunning }">
          <aside class="reasoning" aria-live="polite">
            <strong>{{ isRunning ? "Thinking…" : "Reasoning" }}</strong>
            <p>{{ message.content }}</p>
          </aside>
        </template>
      </CopilotChat>
    </template>

Render `AgentChat` as a descendant of the provider from the first example. Swap in your own component or markup to match your product's tone.

The Vue customization boundary is the `reasoning-message` scoped slot. React `messageView.reasoningMessage` component and sub-slot objects are not Vue APIs.

Reasoning is produced by the model and forwarded by your agent/runtime. The Vue frontend cannot make a model emit reasoning; select a reasoning-capable model and make sure your adapter forwards AG-UI reasoning events. Only emit reasoning content that is safe for the end user to see.

## Choose your AI backend

See [Integrations](https://ssr-placeholder.invalid//integrations) for all available frameworks (generative-ui/reasoning).
