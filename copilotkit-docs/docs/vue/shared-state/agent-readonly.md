---
url: https://docs.copilotkit.ai/vue/shared-state/agent-readonly/
title: Agent Read-Only Context
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:46:29.324915+00:00
---

# Agent Read-Only Context

> Source: https://docs.copilotkit.ai/vue/shared-state/agent-readonly/

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

[Shared State](https://docs.copilotkit.ai/vue/shared-state)[Render agent state in your app](https://docs.copilotkit.ai/vue/shared-state/rendering-in-app)[State Streaming](https://docs.copilotkit.ai/vue/shared-state/streaming)[Agent Read-Only Context](https://docs.copilotkit.ai/vue/shared-state/agent-readonly)

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

InteractivityShared state

# Agent Read-Only Context

Publish UI values to the agent as a one-way read-only channel via useAgentContext.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

Sometimes you want the agent to _know_ something about the current UI, like the logged-in user, the current page, or a recent activity log, but you don't want the agent to be able to modify it. That's what `useAgentContext` is for: a one-way **UI → agent** channel for read-only context.

Unlike full shared state, where the UI and agent can both mutate the same state contract, `useAgentContext` values are pure inputs. The agent sees them on every turn through the runtime's context injection, but the context API exposes no setter or mutation tool.

## When should I use this?#

Reach for `useAgentContext` instead of full shared state when:

  * The value is **UI-owned** and has no meaning to the agent beyond what the user is looking at right now.
  * The agent should read but never write, for example user identity, feature flags, selected record, or scroll position.
  * You want the value to unregister automatically when the component unmounts.



Think of it as "props for the agent."

## How it works in code#

Call `useAgentContext({ description, value })` once per value you want to publish. Each call registers a reactive context entry with the runtime that is:

  * Refreshed whenever the supplied ref or getter changes.
  * Automatically removed when the component unmounts.
  * Surfaced to the agent through the backend's CopilotKit middleware on every turn.



src/components/WorkspaceContext.vue
    
    
    <script setup lang="ts">
    import { ref } from "vue";
    import { useAgentContext } from "@copilotkit/vue/v2";
    
    const workspaceId = ref("northstar");
    
    useAgentContext({
      description: "Active workspace",
      value: workspaceId,
    });
    </script>
    
    <template>
      <p>Workspace: {{ workspaceId }}</p>
    </template>

The `description` is important: it is the human-readable label the agent sees alongside the value, so it knows what to do with it. Treat it like a parameter docstring. Keep secrets out of this channel; anything published here is intended for the agent to read.

## Wire it to your own state#

`useAgentContext` does not care where the value comes from: a local ref, a computed value, a router getter, Pinia, or another domain store. Pass a ref or getter and Vue re-registers the serialized context when the value changes.

src/App.vue
    
    
    <script setup lang="ts">
    import { CopilotChat, CopilotKitProvider } from "@copilotkit/vue/v2";
    import WorkspaceContext from "./components/WorkspaceContext.vue";
    </script>
    
    <template>
      <CopilotKitProvider runtime-url="/api/copilotkit">
        <WorkspaceContext />
        <CopilotChat />
      </CopilotKitProvider>
    </template>

## Read-only, by design#

Because the agent never sees a setter or mutation tool for these values, the context registration itself cannot update them. That makes `useAgentContext` the right tool whenever the value is an input rather than a shared workspace both sides edit.

When you need both reads _and_ writes, use full **[Shared State](https://docs.copilotkit.ai/vue/shared-state)** : `useAgent()` exposes `agent.state` and the same agent's `setState(...)` mutation path when the runtime supports shared state.

## Related#

  * **[Shared State (overview)](https://docs.copilotkit.ai/vue/shared-state)** — bidirectional reads and writes.
  * **[State streaming](https://docs.copilotkit.ai/vue/shared-state/streaming)** — stream agent-written state back to the UI during a run.


