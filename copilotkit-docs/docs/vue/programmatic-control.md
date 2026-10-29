---
url: https://docs.copilotkit.ai/vue/programmatic-control/
title: Programmatic Control
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:46:29.004158+00:00
---

# Programmatic Control

> Source: https://docs.copilotkit.ai/vue/programmatic-control/

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

# Programmatic Control

Drive agent runs directly from code — no chat UI required.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

Programmatic control is what you reach for when you want to drive an agent run from code rather than from a chat composer: a button, a form, a cron job, a keyboard shortcut, or a graph callback. CopilotKit exposes three primitives that cover every triggering pattern:

  * `agent.addMessage(...)` — append a message to the conversation without running the agent. Pair it with `copilotkit.runAgent({ agent })` when the message should kick off a turn.
  * `copilotkit.runAgent({ agent })` — the same entry point `<CopilotChat />` calls under the hood. It orchestrates frontend tools, follow-up runs, and the subscriber lifecycle.
  * `agent.subscribe(subscriber)` — low-level AG-UI event subscription (`onCustomEvent`, `onRunStartedEvent`, `onRunFinalized`, `onRunFailed`, and streaming deltas).



## When should I use this?#

Use programmatic control when you want to:

  * Trigger agent runs from buttons, forms, or other UI elements
  * Execute specific tools directly from UI interactions without an LLM turn
  * Build agent features without a chat window
  * Access agent state and results programmatically
  * Create fully custom agent-driven workflows



## Sending a message from code#

The canonical pattern is to append a user message with `agent.addMessage`, then call `copilotkit.runAgent({ agent })`. Use `copilotkit.stopAgent({ agent })` to cancel an in-flight run.

src/components/AgentTrigger.vue
    
    
    <script setup lang="ts">
    import { toRaw } from "vue";
    import { useAgent, useCopilotKit } from "@copilotkit/vue/v2";
    
    const { agent } = useAgent({ agentId: "sales" });
    const { copilotkit } = useCopilotKit();
    
    async function run() {
      const current = agent.value;
      if (!current || current.isRunning) return;
    
      current.addMessage({
        id: crypto.randomUUID(),
        role: "user",
        content: "Summarize the latest sales data",
      });
    
      try {
        await copilotkit.value.runAgent({ agent: toRaw(current) });
      } catch (error) {
        console.error("CopilotKit runAgent failed:", error);
      }
    }
    
    function stop() {
      const current = agent.value;
      if (!current) return;
      copilotkit.value.stopAgent({ agent: toRaw(current) });
    }
    </script>
    
    <template>
      <button :disabled="agent?.isRunning" @click="run">Run agent</button>
      <button :disabled="!agent?.isRunning" @click="stop">Stop</button>
    </template>

src/App.vue
    
    
    <script setup lang="ts">
    import { CopilotKitProvider } from "@copilotkit/vue/v2";
    import AgentTrigger from "./components/AgentTrigger.vue";
    </script>
    
    <template>
      <CopilotKitProvider runtime-url="/api/copilotkit">
        <AgentTrigger />
      </CopilotKitProvider>
    </template>

### `copilotkit.runAgent()` vs `agent.runAgent()`#

Both methods trigger the agent, but they operate at different levels:

  * **`copilotkit.runAgent({ agent })`** — the recommended default. It orchestrates the full lifecycle, executes frontend tools, handles follow-up runs, and routes errors through the subscriber system.
  * **`agent.runAgent(options)`** — a low-level method on the agent instance. It sends the request to the runtime but does **not** execute frontend tools or chain follow-ups. Reach for it only when you need direct control.



## Subscribing to agent events#

`agent.subscribe(subscriber)` returns `{ unsubscribe }`. The subscriber accepts every AG-UI lifecycle callback: `onCustomEvent`, `onRunStartedEvent`, `onRunFinalized`, `onRunFailed`, and the streaming deltas. Use it to drive progress UI, forward events to analytics, or inspect framework pause/resume events.
    
    
    import { watch } from "vue";
    
    watch(
      agent,
      (current, _previous, onCleanup) => {
        if (!current) return;
        const subscription = current.subscribe({
          onRunStartedEvent: () => console.log("started"),
          onRunFinalized: () => console.log("done"),
          onRunFailed: ({ error }) => console.error(error),
        });
        onCleanup(() => subscription.unsubscribe());
      },
      { immediate: true },
    );

## See also#

  * [Headless UI](https://docs.copilotkit.ai/vue/custom-look-and-feel/headless-ui) — build your own chat surface from lower-level components.
  * [Human-in-the-Loop](https://docs.copilotkit.ai/human-in-the-loop) — compare `useHumanInTheLoop` and `useInterrupt` for paused runs.



## Choose your AI backend

See [Integrations](https://ssr-placeholder.invalid//integrations) for all available frameworks (programmatic-control).
