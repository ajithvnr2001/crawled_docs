---
url: https://docs.copilotkit.ai/vue/human-in-the-loop/headless/
title: Headless Interrupts
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:46:23.870347+00:00
---

# Headless Interrupts

> Source: https://docs.copilotkit.ai/vue/human-in-the-loop/headless/

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

[HITL Overview](https://docs.copilotkit.ai/vue/human-in-the-loop)[Pausing the Agent for Input](https://docs.copilotkit.ai/vue/human-in-the-loop/useInterrupt)[Headless Interrupts](https://docs.copilotkit.ai/vue/human-in-the-loop/headless)[Governed Action Approval UI](https://docs.copilotkit.ai/vue/human-in-the-loop/governed-actions)

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

InteractivityHuman-in-the-loop

# Headless Interrupts

Resolve agent interrupts from any UI, without a chat interrupt slot.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

The `#interrupt` slot is the 80% path: it keeps the UI attached to a `<CopilotChat>` transcript and handles when to show the picker. This page covers the escape hatch: set `renderInChat: false` and render the reactive interrupt state anywhere in your Vue tree. The UI can take any shape — button grid, form, modal, keyboard shortcut — and no chat needs to be mounted.

## When should I use this?#

  * **Testing / Playwright fixtures** — a deterministic, chat-less button grid is easier to drive than a picker that appears after an LLM call.
  * **Non-chat UIs** — dashboards, side panels, inspector surfaces, or any place where you want the agent's interrupt without the transcript.
  * **Custom flow control** — when you need to know exactly when the interrupt arrived and when it was resolved.
  * **Research / debugging** — when you want to observe raw interrupt state without the chat abstraction.



If you just want a picker in chat, use [`useInterrupt`](https://docs.copilotkit.ai/useInterrupt) with the default `renderInChat: true` and the `#interrupt` slot.

## Provider setup#

The component calling these composables must be below `CopilotKitProvider`:

src/App.vue
    
    
    <script setup lang="ts">
    import { CopilotKitProvider } from "@copilotkit/vue/v2";
    import HeadlessInterruptPanel from "./components/HeadlessInterruptPanel.vue";
    </script>
    
    <template>
      <CopilotKitProvider runtime-url="/api/copilotkit">
        <HeadlessInterruptPanel />
      </CopilotKitProvider>
    </template>

## Going further#

  * [Tool-based HITL with `useHumanInTheLoop`](https://docs.copilotkit.ai/human-in-the-loop) — for LLM-initiated pauses where the model decides to ask the user.
  * [`useInterrupt`](https://docs.copilotkit.ai/useInterrupt) — the chat-slot path, with `enabled` gating, handler preprocessing, and standard interrupt details.


