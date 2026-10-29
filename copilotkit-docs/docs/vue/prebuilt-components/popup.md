---
url: https://docs.copilotkit.ai/vue/prebuilt-components/popup/
title: CopilotPopup
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:46:28.866208+00:00
---

# CopilotPopup

> Source: https://docs.copilotkit.ai/vue/prebuilt-components/popup/

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

# CopilotPopup

Floating Vue chat launcher that opens an overlay window.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

`<CopilotPopup>` is a floating launcher that opens a chat window over the page. It is the compact way to add a copilot without dedicating layout space to an always-visible panel.

## When should I use this?#

Use the popup for task-focused chats that users open on demand. Use [CopilotSidebar](https://docs.copilotkit.ai/vue/prebuilt-components/sidebar) when the chat belongs beside the workspace, or [`<CopilotChat>`](https://docs.copilotkit.ai/vue/prebuilt-components/chat) when it belongs in the document flow.

## Basic setup#

App.vue
    
    
    <script setup lang="ts">
    import { CopilotKitProvider, CopilotPopup } from "@copilotkit/vue/v2";
    import "@copilotkit/vue/styles.css";
    </script>
    
    <template>
      <CopilotKitProvider runtime-url="/api/copilotkit">
        <main><!-- Your application --></main>
        <CopilotPopup agent-id="my-agent" :default-open="false" />
      </CopilotKitProvider>
    </template>

## Configuring the popup#

Alongside the shared chat props, `CopilotPopup` accepts `width`, `height`, `default-open`, and `click-outside-to-close`. Its `header` and `toggle-button` scoped slots receive the popup state and open/close actions. The component also forwards the regular chat interaction events.

## Styling#

See [CSS customization](https://docs.copilotkit.ai/vue/custom-look-and-feel/css) for token overrides and [slots](https://docs.copilotkit.ai/vue/custom-look-and-feel/slots) for template-level replacement of popup pieces.

### On this page

What is this?When should I use this?Basic setupConfiguring the popupStyling
