---
url: https://docs.copilotkit.ai/vue/prebuilt-components/chat/
title: CopilotChat
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:46:28.829671+00:00
---

# CopilotChat

> Source: https://docs.copilotkit.ai/vue/prebuilt-components/chat/

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

# CopilotChat

Inline Vue chat component that you can place anywhere and size as needed.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

`<CopilotChat>` is the base prebuilt Vue chat surface. Place it in any layout and size its container to fit. `CopilotSidebar` and `CopilotPopup` compose the same chat primitives with docked and overlay chrome.

## When should I use this?#

Choose `CopilotChat` for a dedicated chat page, an inline pane next to other content, or any layout where you do not need a launcher. Choose [CopilotSidebar](https://docs.copilotkit.ai/vue/prebuilt-components/sidebar) for a collapsible docked surface and [CopilotPopup](https://docs.copilotkit.ai/vue/prebuilt-components/popup) for an overlay.

## Basic setup#

Import the components from `@copilotkit/vue/v2`, import the package stylesheet, and keep the chat below `CopilotKitProvider`:

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

`runtime-url` identifies the runtime that serves the configured agent. The current Vue Showcase demonstrates this base `agentic-chat` surface.

## Common props and events#

Surface| Purpose  
---|---  
`agent-id`| The runtime agent to use.  
`thread-id`| An explicit thread to connect to.  
`labels`| User-facing strings such as the title, placeholder, welcome text, and disclaimer.  
`welcome-screen`| Set to `false` to disable the empty state.  
`attachments`| Enable and configure file attachments.  
`auto-scroll`| Use `"pin-to-bottom"`, `"pin-to-send"`, `"none"`, or the legacy boolean shorthand.  
`@submit-message`, `@input-change`, `@select-suggestion`| Observe the corresponding chat interactions.  
`@stop`| Observe a stop action.  
`:on-error`| Bind a handler for CopilotKit runtime errors for this agent.  
  
## Styling and composition#

Customize the surface with [CSS](https://docs.copilotkit.ai/vue/custom-look-and-feel/css), named/scoped [slots](https://docs.copilotkit.ai/vue/custom-look-and-feel/slots), or a [headless UI](https://docs.copilotkit.ai/vue/custom-look-and-feel/headless-ui).

### On this page

What is this?When should I use this?Basic setupCommon props and eventsStyling and composition
