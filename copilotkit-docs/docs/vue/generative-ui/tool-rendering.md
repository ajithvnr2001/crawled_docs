---
url: https://docs.copilotkit.ai/vue/generative-ui/tool-rendering/
title: Tool Call Rendering
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:46:23.972275+00:00
---

# Tool Call Rendering

> Source: https://docs.copilotkit.ai/vue/generative-ui/tool-rendering/

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

Tool Call Rendering

Generative UIControlled

# Tool Call Rendering

Render your agent's tool calls with custom UI components.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

Tools are how an LLM invokes predefined, typically-deterministic functions. Tool rendering lets you decide how each of those tool calls appears in the chat. Instead of showing raw JSON, you register a Vue component that draws a branded card for the call (arguments, live status, and the eventual result). This is the **Generative UI** variant CopilotKit calls **tool rendering**.

**Free course:** See this pattern built end-to-end in [Build Interactive Agents with Generative UI](https://www.deeplearning.ai/short-courses/build-interactive-agents-with-generative-ui/) — a free DeepLearning.AI short course taught by CopilotKit's CEO covering the full Generative UI spectrum (Controlled, Declarative, and Open-Ended).

## When should I use this?#

Render tool calls when you want to:

  * Show users exactly what tools the agent is invoking and with what arguments
  * Display live progress indicators while a tool executes
  * Render rich, polished results once a tool completes
  * Give tool-heavy agents a transparent, on-brand chat experience



## Default tool rendering (zero-config)#

The simplest entry point is `useDefaultRenderTool()` with no arguments. CopilotKit registers its built-in default renderer as the `*` wildcard: every tool call renders as a status card (tool name, live **Running → Done** state, collapsible arguments/result) without you writing any UI.

Without this composable the runtime has no `*` renderer and tool calls are invisible; the user only sees the assistant's final text summary.

src/components/AgentExperience.vue
    
    
    <script setup lang="ts">
    import { CopilotChat, useDefaultRenderTool } from "@copilotkit/vue/v2";
    
    useDefaultRenderTool();
    </script>
    
    <template><CopilotChat /></template>

## Custom catch-all#

Once you want on-brand chrome, pass a `render` component or function to `useDefaultRenderTool`. It's a convenience wrapper around `useRenderTool({ name: "*", ... })`: one wildcard renderer handles every tool call, named or not.

src/components/AgentExperience.vue
    
    
    useDefaultRenderTool({ render: BrandedToolCard });

## Per-tool renderers#

The most expressive path is one renderer per tool name. Each renderer receives the tool's parsed arguments, a live `status`, and, once the agent returns, the `result`.

src/components/WeatherToolCard.vue
    
    
    <script setup lang="ts">
    defineProps<{
      parameters: { city?: string };
      status: "inProgress" | "executing" | "complete";
      result?: string;
    }>();
    </script>
    
    <template>
      <p v-if="status !== 'complete'">Checking {{ parameters.city ?? "…" }}</p>
      <article v-else>
        <strong>{{ parameters.city }}</strong>
        <pre>{{ result }}</pre>
      </article>
    </template>

src/components/AgentExperience.vue
    
    
    <script setup lang="ts">
    import { z } from "zod";
    import { CopilotChat, useDefaultRenderTool, useRenderTool } from "@copilotkit/vue/v2";
    import WeatherToolCard from "./WeatherToolCard.vue";
    
    useRenderTool({
      name: "get_weather",
      parameters: z.object({ city: z.string() }),
      render: WeatherToolCard,
    });
    
    useDefaultRenderTool(); // wildcard fallback for every other tool
    </script>
    
    <template><CopilotChat /></template>

`parameters` is partial while arguments stream. Read required fields only after the status advances from `inProgress`. The result is a string when status is `complete`; parse it only if your backend deliberately returns a documented serialized shape.

The `name` you pass to `useRenderTool` must match the tool name the agent exposes; that's how the runtime routes the call to your component.

Per-tool renderers compose with a catch-all: named renderers claim the "interesting" tools and a wildcard handles everything else. The example registers the built-in wildcard after the named `get_weather` renderer.

If the renderer closes over reactive values, pass Vue watch sources as the second argument:
    
    
    useRenderTool({ name: "get_weather", parameters, render: WeatherToolCard }, [locale]);

Finally, mount the registration component beneath the provider:

src/App.vue
    
    
    <script setup lang="ts">
    import { CopilotKitProvider } from "@copilotkit/vue/v2";
    import AgentExperience from "./components/AgentExperience.vue";
    </script>
    
    <template>
      <CopilotKitProvider runtime-url="/api/copilotkit"><AgentExperience /></CopilotKitProvider>
    </template>

## The backend tool definition#

The frontend renderer only sees what the agent sends down. The matching backend must expose a tool named `get_weather`, return structured data, and let the frontend renderer with the same name paint the card. The Vue renderer does not create or execute that backend tool.

Select an AI backend above to see this code example.

## Choose your AI backend

See [Integrations](https://ssr-placeholder.invalid//integrations) for all available frameworks (generative-ui/tool-rendering).

### On this page

What is this?When should I use this?Default tool rendering (zero-config)Custom catch-allPer-tool renderersThe backend tool definition
