---
url: https://docs.copilotkit.ai/vue/frontend-tools/
title: Frontend Tools
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:46:22.887234+00:00
---

# Frontend Tools

> Source: https://docs.copilotkit.ai/vue/frontend-tools/

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

Frontend-tools

Basics

# Frontend Tools

Let your agent interact with and update your application's UI.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

Frontend tools let your agent define and invoke client-side functions that run entirely in the user's browser. Because the handler executes on the frontend, it has direct access to component state, browser APIs, and any third-party UI library the page already uses. That's how an agent can "reach into" the app: update Vue state, trigger animations, read `localStorage`, pop a toast, or steer the user's view.

This page covers the "agent drives the UI" shape of frontend tools. The same primitive also powers Generative UI and Human-in-the-loop; see those pages for interaction patterns.

## When should I use this?#

Use frontend tools when your agent needs to:

  * Read or modify Vue component state
  * Access browser APIs like `localStorage`, `sessionStorage`, or cookies
  * Trigger UI updates, animations, or transitions
  * Show alerts, toasts, or notifications
  * Interact with third-party frontend libraries
  * Perform anything that requires the user's immediate browser context



## How it works in code#

Register a frontend tool with `useFrontendTool`. Give it a name, a Zod schema for parameters, and a handler. The agent can then call it like any other tool and your frontend runs it in the browser.

src/components/DashboardAgent.vue
    
    
    <script setup lang="ts">
    import { ref } from "vue";
    import { z } from "zod";
    import { CopilotChat, useFrontendTool } from "@copilotkit/vue/v2";
    
    const severity = ref("all");
    
    useFrontendTool(
      {
        name: "filter_incidents",
        description: "Filter the visible incident list by severity.",
        parameters: z.object({
          severity: z.enum(["all", "sev1", "sev2", "sev3"]),
        }),
        handler: async ({ severity: nextSeverity }) => {
          severity.value = nextSeverity;
          return { applied: true, severity: nextSeverity };
        },
      },
      [severity],
    );
    </script>
    
    <template>
      <p>Current filter: {{ severity }}</p>
      <CopilotChat />
    </template>

The handler receives the parsed, type-safe parameters and can do anything the browser can: update state, call an API, or touch the DOM. Its return value is sent back to the agent as the tool result so the model can reason about what happened.

The second argument is an array of Vue watch sources. Include refs or getters read by the registration so the handler sees current values.

src/App.vue
    
    
    <script setup lang="ts">
    import { CopilotKitProvider } from "@copilotkit/vue/v2";
    import DashboardAgent from "./components/DashboardAgent.vue";
    </script>
    
    <template>
      <CopilotKitProvider runtime-url="/api/copilotkit">
        <DashboardAgent />
      </CopilotKitProvider>
    </template>

Your agent discovers the name, description, and parameter schema through the runtime connection. Make descriptions narrow, validate inputs, and ask for explicit confirmation before irreversible actions. Privileged mutations, secret-bearing API calls, and authorization decisions belong on a trusted backend. For a tool that must wait for a user's answer, use `useHumanInTheLoop` instead.

## Choose your AI backend

See [Integrations](https://ssr-placeholder.invalid//integrations) for all available frameworks (frontend-tools).

### On this page

What is this?When should I use this?How it works in code
