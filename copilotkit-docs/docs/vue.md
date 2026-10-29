---
url: https://docs.copilotkit.ai/vue/
title: Vue quickstart
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:46:34.104814+00:00
---

# Vue quickstart

> Source: https://docs.copilotkit.ai/vue/

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

# Vue

Connect a Vue app to Copilot Runtime with CopilotKit.

`@copilotkit/vue` provides Vue 3 components and composables for CopilotKit. This guide gets you to a working Vue app with a chat UI backed by a local [Copilot Runtime](https://docs.copilotkit.ai/backend/copilot-runtime) and `BuiltInAgent`.

The runtime runs on your server, keeps model credentials out of the browser, and exposes the `default` agent that `CopilotChat` uses automatically.

## Start with your coding agent#

Use this prompt to connect your Vue app to Copilot Runtime with the selected agent backend, then verify a working conversation. You can also follow the manual steps below.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Prerequisites#

  * An OpenAI API key (or another model provider supported by [Model Selection](https://docs.copilotkit.ai/model-selection))
  * Vue 3.3+
  * Node.js 20+



## Getting started#

### Create your Vue app#

If you don't have one already:
    
    
    npm create vue@latest my-copilot-app
    cd my-copilot-app
    npm install

### Install CopilotKit#

Install the Vue frontend package and `@copilotkit/runtime` for your local Copilot Runtime server:

npmpnpmyarn
    
    
    npm install @copilotkit/vue @copilotkit/runtime
    npm install -D tsx typescript @types/node
    
    
    pnpm add @copilotkit/vue @copilotkit/runtime
    pnpm add -D tsx typescript @types/node
    
    
    yarn add @copilotkit/vue @copilotkit/runtime
    yarn add -D tsx typescript @types/node

### Create the Copilot Runtime#

Add a small Node server that hosts Copilot Runtime at `/api/copilotkit` and registers a `default` built-in agent:

Already have an agent? Do not use BuiltInAgent

`BuiltInAgent` is CopilotKit's own agent — it calls the model directly. Registering it as `default` means chat talks to it, not to an agent you already wrote. It replaces your agent rather than connecting to it.

If you already have a LangGraph, CrewAI, Mastra, ADK, Pydantic AI, or other agent, use your framework's quickstart for the runtime wiring so it registers your agent instead. You can still use the Vue frontend steps on this page.

server.ts
    
    
    import { createServer } from "node:http";
    import { BuiltInAgent, CopilotRuntime } from "@copilotkit/runtime/v2";
    import { createCopilotNodeListener } from "@copilotkit/runtime/v2/node";
    
    const runtime = new CopilotRuntime({
      agents: {
        default: new BuiltInAgent({
          model: "openai:gpt-5-mini",
          prompt: "You are a helpful assistant for a Vue app.",
        }),
      },
    });
    
    const port = Number(process.env.PORT ?? 8200);
    
    createServer(
      createCopilotNodeListener({
        runtime,
        basePath: "/api/copilotkit",
        cors: true,
      }),
    ).listen(port, () => {
      console.log(
        `Copilot Runtime listening at http://localhost:${port}/api/copilotkit`,
      );
    });

Vite and Copilot Runtime run on separate origins

Vite serves the Vue app (usually on `http://localhost:5173`) while this Node server runs on `http://localhost:8200`. Because the browser calls across those origins, `cors: true` is required for local development; the Node listener does not enable CORS by default.

### Import the styles#

Import the package stylesheet once in your app entry. It's self-contained, so the chat renders without any other CSS.

src/main.ts
    
    
    import { createApp } from "vue";
    import App from "./App.vue";
    import "@copilotkit/vue/styles.css"; 
    
    createApp(App).mount("#app");

### Connect to Copilot Runtime#

Point `CopilotKitProvider` at the runtime endpoint and drop in `CopilotChat`. Because the runtime registers an agent named `default`, the chat picks it up automatically.

src/App.vue
    
    
    <script setup lang="ts">
    import { CopilotKitProvider, CopilotChat } from "@copilotkit/vue/v2"; 
    </script>
    
    <template>
      <CopilotKitProvider
        runtime-url="http://localhost:8200/api/copilotkit"
      >
        <div style="height: 100vh">
          <CopilotChat />
        </div>
      </CopilotKitProvider>
    </template>

Pick your chat layout

`CopilotChat` is the full-height chat surface. Use `CopilotSidebar` for a fixed side panel with open/close behavior, or `CopilotPopup` for a floating panel with a toggle button. They share core agent and chat wiring, but each surface also has layout-specific props and behavior.

### Run the runtime and app#

Start Copilot Runtime in one terminal:
    
    
    export OPENAI_API_KEY=sk-...
    npx tsx server.ts

Start the Vue app in another terminal:
    
    
    npm run dev

Open the dev server URL (Vite prints it, usually `http://localhost:5173`), send a message, and you'll see it stream back through Copilot Runtime.

Troubleshooting

  * **Chat renders unstyled** : Make sure you imported `@copilotkit/vue/styles.css` in your app entry.
  * **No response from the agent** : Confirm the runtime server is running and `http://localhost:8200/api/copilotkit/info` returns agent information.
  * **CORS errors** : The Vite app and Node runtime use different origins. Keep `cors: true` in `createCopilotNodeListener` for local development; the Node listener is CORS-disabled by default. Configure an explicit allowed origin before deploying.
  * **Model auth errors** : Confirm `OPENAI_API_KEY` is set in the terminal running `npx tsx server.ts`.



### Open Inspector and confirm setup#

On localhost, click the Inspector button in the corner of the app.

  1. Open **Agents** , then **Agent**. Your agent is listed.
  2. Send a chat message. Open **Agents** , then **AG-UI Events**. Events are moving.
  3. Open **Rich Threads**. The list is unlocked (Intelligence is on), or locked with Enable Intelligence (Intelligence is off).



More detail: [Inspector](https://docs.copilotkit.ai/inspector).

## Where to go next#

  * [Copilot Runtime](https://docs.copilotkit.ai/backend/copilot-runtime): the backend layer this frontend connects to.
  * [Built-in Agent quickstart](https://docs.copilotkit.ai/quickstart): a framework-neutral path if you want CopilotKit to own the agent too.
  * [Generative UI](https://docs.copilotkit.ai/vue/generative-ui/tool-based): render a tool result as a card or another interactive surface instead of plain text.
  * [AG-UI Streams](https://docs.copilotkit.ai/vue/AG-UI-Streams): persist conversations and work with the thread API directly.
  * [Threads Drawer](https://docs.copilotkit.ai/vue/prebuilt-components/copilot-threads-drawer): add a ready-made thread switcher beside the chat.
  * [Vue API reference](https://docs.copilotkit.ai/reference/vue): find the current `@copilotkit/vue/v2` component and composable APIs.



The Vue reference also covers slot-based customization, thread management, interrupts, and lazy-loaded custom elements for SSR.
