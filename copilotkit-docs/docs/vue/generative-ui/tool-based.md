---
url: https://docs.copilotkit.ai/vue/generative-ui/tool-based/
title: Components as Tools
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:46:24.068686+00:00
---

# Components as Tools

> Source: https://docs.copilotkit.ai/vue/generative-ui/tool-based/

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

[Components as Tools](https://docs.copilotkit.ai/vue/generative-ui/tool-based)[Tool Call Rendering](https://docs.copilotkit.ai/vue/generative-ui/tool-rendering)[State Rendering](https://docs.copilotkit.ai/vue/generative-ui/state-rendering)

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

Components as Tools

Generative UIControlled

# Components as Tools

Let your agent render rich Vue components directly in the chat by calling them as tools.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

Tool-based Generative UI is the simplest form of Generative UI: you register a Vue component with `useComponent`, and CopilotKit exposes it to the agent as a tool. When the agent calls the tool, CopilotKit renders your component inline in the chat, passing the tool's arguments straight through as typed props.

Unlike [tool rendering](https://docs.copilotkit.ai/vue/generative-ui/tool-rendering), which wraps a real backend tool in a custom UI, tool-based GenUI is the component. There is no handler, no user interaction, no server-side execution. The agent decides when to show it, populates the data, and CopilotKit paints it.

## When should I use this?#

Use `useComponent` when you want to:

  * Display rich UI (cards, charts, tables, dashboards) inline in the chat
  * Show structured data the agent has derived from its reasoning
  * Render previews, status indicators, or visual summaries
  * Let the agent present information beyond plain text



For components that need user interaction, see [Human-in-the-loop](https://docs.copilotkit.ai/vue/human-in-the-loop). For operational transparency around a real backend tool, see [Tool rendering](https://docs.copilotkit.ai/vue/generative-ui/tool-rendering).

## How it works in code#

`useComponent` takes a name, a Zod schema for its props, and the component to render. The runtime advertises that schema when it registers the frontend tool, and TypeScript infers the component props from it. Runtime arguments are JSON-parsed but are not validated against the schema.

src/components/WeatherCard.vue
    
    
    <script setup lang="ts">
    defineProps<{ city: string; temperature: number; condition: string }>();
    </script>
    
    <template>
      <article>
        <strong>{{ city }}</strong>
        <p>{{ temperature }}° · {{ condition }}</p>
      </article>
    </template>

Vue composables execute during component setup, so the component calling `useComponent` must be a descendant of `CopilotKitProvider`.

src/components/AgentExperience.vue
    
    
    <script setup lang="ts">
    import { z } from "zod";
    import { CopilotChat, useComponent } from "@copilotkit/vue/v2";
    import WeatherCard from "./WeatherCard.vue";
    
    useComponent({
      name: "show_weather",
      description: "Display the weather for one city.",
      parameters: z.object({
        city: z.string(),
        temperature: z.number(),
        condition: z.string(),
      }),
      render: WeatherCard,
    });
    </script>
    
    <template><CopilotChat /></template>

src/App.vue
    
    
    <script setup lang="ts">
    import { CopilotKitProvider } from "@copilotkit/vue/v2";
    import AgentExperience from "./components/AgentExperience.vue";
    </script>
    
    <template>
      <CopilotKitProvider runtime-url="/api/copilotkit">
        <AgentExperience />
      </CopilotKitProvider>
    </template>

The component itself is ordinary Vue: it reads only its props and can stream in as the agent fills the payload. It doesn't know anything about CopilotKit.

The `name` you pass to `useComponent` is what the agent sees as the tool name. Make it a verb like `render_bar_chart` or `show_weather` so the LLM reliably picks it when the user asks for that visualization.

The model supplies the props, so validate consequential data against application state rather than treating a well-formed card as proof that the values are authorized or current.

## Choose your AI backend

See [Integrations](https://ssr-placeholder.invalid//integrations) for all available frameworks (generative-ui/tool-based).

### On this page

What is this?When should I use this?How it works in code
