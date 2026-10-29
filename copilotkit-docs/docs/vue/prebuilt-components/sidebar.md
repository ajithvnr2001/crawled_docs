---
url: https://docs.copilotkit.ai/vue/prebuilt-components/sidebar/
title: CopilotSidebar
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:46:28.902993+00:00
---

# CopilotSidebar

> Source: https://docs.copilotkit.ai/vue/prebuilt-components/sidebar/

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

# CopilotSidebar

Drop-in collapsible sidebar chat for Vue applications.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

`<CopilotSidebar>` is a prebuilt Vue chat surface that docks to the side of an app and can slide open on demand. It is a good fit for an in-app copilot that must remain accessible without replacing the main workspace.

## When should I use this?#

Use the sidebar for persistent, collapsible chat next to your application content. Use [CopilotPopup](https://docs.copilotkit.ai/vue/prebuilt-components/popup) for an overlay launcher or [`<CopilotChat>`](https://docs.copilotkit.ai/vue/prebuilt-components/chat) for a fully embedded pane.

## Basic setup#

App.vue
    
    
    <script setup lang="ts">
    import { CopilotKitProvider, CopilotSidebar } from "@copilotkit/vue/v2";
    import "@copilotkit/vue/styles.css";
    </script>
    
    <template>
      <CopilotKitProvider runtime-url="/api/copilotkit">
        <main><!-- Your application --></main>
        <CopilotSidebar agent-id="my-agent" :default-open="false" />
      </CopilotKitProvider>
    </template>

## Configuring the sidebar#

`CopilotSidebar` accepts the chat props plus `width` and `default-open`. Use the `header` scoped slot to replace the header and `toggle-button` to replace the launcher. Their slot props include the current open state and actions such as `toggle`, `open`, and `close`.

The component reports the same chat interaction events as `CopilotChat`, including `@submit-message`, `@input-change`, and `@select-suggestion`.

## Styling#

Use [CSS customization](https://docs.copilotkit.ai/vue/custom-look-and-feel/css) for design tokens or [slots](https://docs.copilotkit.ai/vue/custom-look-and-feel/slots) to replace the header, launcher, message list, composer, and welcome state.

### On this page

What is this?When should I use this?Basic setupConfiguring the sidebarStyling
