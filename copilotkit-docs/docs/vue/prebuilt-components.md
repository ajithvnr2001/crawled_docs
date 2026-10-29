---
url: https://docs.copilotkit.ai/vue/prebuilt-components/
title: Prebuilt Components
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:46:28.783790+00:00
---

# Prebuilt Components

> Source: https://docs.copilotkit.ai/vue/prebuilt-components/

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

BasicsChat

# Prebuilt Components

Drop-in Vue chat components with a customization path from CSS to headless composition.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Prebuilt components for agentic chat#

`@copilotkit/vue/v2` ships three chat surfaces: [**CopilotChat**](https://docs.copilotkit.ai/vue/prebuilt-components/chat), [**CopilotSidebar**](https://docs.copilotkit.ai/vue/prebuilt-components/sidebar), and [**CopilotPopup**](https://docs.copilotkit.ai/vue/prebuilt-components/popup). They share the same chat primitives while choosing different layouts. Pick the surface that fits the product; each handles streaming messages, tool rendering, suggestions, and Vue slot customization.

Use `CopilotThreadsDrawer` beside a supported surface when you need a conversation-history drawer, or use `useThreads` to build your own switcher.

## The customization ladder#

  1. **Drop in a surface.** Render `CopilotChat`, `CopilotSidebar`, or `CopilotPopup` below `CopilotKitProvider`.
  2. **Re-skin with CSS.** Import the Vue stylesheet and override the `[data-copilotkit]` design tokens.
  3. **Recompose with slots.** Replace an empty state, message list, composer, header, or launcher using Vue named and scoped slots.
  4. **Go headless.** Build your layout from `useAgent`, `useCopilotKit`, and the public chat leaf components where needed.



These layers are incremental. A custom welcome-screen slot and CSS token overrides can coexist; moving to a custom surface does not require copying the runtime connection logic.

## Drop-in chat#

Import the Vue CSS once, wrap the application in `CopilotKitProvider`, and put the chat surface in the provider's default slot:

App.vue
    
    
    <script setup lang="ts">
    import { CopilotChat, CopilotKitProvider } from "@copilotkit/vue/v2";
    import "@copilotkit/vue/styles.css";
    </script>
    
    <template>
      <CopilotKitProvider runtime-url="/api/copilotkit">
        <CopilotChat agent-id="my-agent" />
      </CopilotKitProvider>
    </template>

The Vue Showcase currently exposes this `agentic-chat` surface. Other prebuilt-component variations do not have a runnable Vue Showcase route yet.

## Starter suggestions#

Call `useConfigureSuggestions` inside a child component of `CopilotKitProvider`. Its reactive configuration is then available to the nearest chat surface.

## Pick a surface#

  * [`<CopilotChat>`](https://docs.copilotkit.ai/vue/prebuilt-components/chat): an inline pane that fills the container you give it.
  * [`<CopilotSidebar>`](https://docs.copilotkit.ai/vue/prebuilt-components/sidebar): a collapsible, docked surface.
  * [`<CopilotPopup>`](https://docs.copilotkit.ai/vue/prebuilt-components/popup): a floating launcher and overlay chat.



For controlling a popup or sidebar from your own UI, and for feedback actions, see [Open, close, and feedback](https://docs.copilotkit.ai/vue/prebuilt-components/chat-controls).
