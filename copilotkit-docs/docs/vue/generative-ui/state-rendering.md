---
url: https://docs.copilotkit.ai/vue/generative-ui/state-rendering/
title: State Rendering
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:46:24.020698+00:00
---

# State Rendering

> Source: https://docs.copilotkit.ai/vue/generative-ui/state-rendering/

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

State Rendering

Generative UIControlled

# State Rendering

Render your agent's state with custom UI components in real-time.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

State rendering lets you build UI that reflects your agent's state in real-time. As your agent progresses through nodes and emits state updates, your frontend renders those changes, showing progress, drafts, or intermediate results.

**Free course:** See this pattern built end-to-end in [Build Interactive Agents with Generative UI](https://www.deeplearning.ai/short-courses/build-interactive-agents-with-generative-ui/) — a free DeepLearning.AI short course taught by CopilotKit's CEO covering the full Generative UI spectrum (Controlled, Declarative, and Open-Ended).

## When should I use this?#

Use state rendering when you want to:

  * Show real-time progress (e.g. "Researching... 2/5 complete")
  * Display drafts that update as the agent works
  * Build dashboards that reflect agent state
  * Render structured output outside of the chat



## How it works in code#

On the frontend, subscribe to the agent's state. Each time the backend forwards a fresh value, your component re-renders with the latest partial output. `useAgent` returns an `agent` ref; read `agent.value?.state` in script or let templates unwrap the ref. Keep the provider in an ancestor SFC.

src/components/ResearchProgress.vue
    
    
    <script setup lang="ts">
    import { computed } from "vue";
    import { useAgent, UseAgentUpdate } from "@copilotkit/vue/v2";
    
    type ResearchState = { status?: string; draft?: string; completed?: number; total?: number };
    
    const { agent } = useAgent({
      agentId: "researcher",
      updates: [UseAgentUpdate.OnStateChanged, UseAgentUpdate.OnRunStatusChanged],
    });
    
    const state = computed(() => (agent.value?.state ?? {}) as ResearchState);
    </script>
    
    <template>
      <section aria-live="polite">
        <p>{{ state.status ?? "Idle" }}</p>
        <progress :value="state.completed ?? 0" :max="state.total ?? 1" />
        <article v-if="state.draft">{{ state.draft }}</article>
      </section>
    </template>

src/App.vue
    
    
    <script setup lang="ts">
    import { CopilotChat, CopilotKitProvider } from "@copilotkit/vue/v2";
    import ResearchProgress from "./components/ResearchProgress.vue";
    </script>
    
    <template>
      <CopilotKitProvider runtime-url="/api/copilotkit">
        <ResearchProgress />
        <CopilotChat agent-id="researcher" />
      </CopilotKitProvider>
    </template>

On the backend, a state-streaming mapping forwards a specific tool argument straight into a state key _as it's being generated_. Some frameworks provide that as middleware; direct SDK adapters can emit `STATE_SNAPSHOT` events from their streaming loop. Either way, the UI can watch the answer assemble token-by-token rather than appearing in one burst between checkpoints.

Select an AI backend above to see this code example.

Treat agent state as untrusted external data. Validate it before using it for privileged actions, and avoid putting secrets in state that is streamed to the browser.

## Choose your AI backend

See [Integrations](https://ssr-placeholder.invalid//integrations) for all available frameworks (generative-ui/state-rendering).

### On this page

What is this?When should I use this?How it works in code
