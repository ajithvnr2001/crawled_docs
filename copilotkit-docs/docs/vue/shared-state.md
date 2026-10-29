---
url: https://docs.copilotkit.ai/vue/shared-state/
title: Shared State
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:46:29.379639+00:00
---

# Shared State

> Source: https://docs.copilotkit.ai/vue/shared-state/

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

Shared State

InteractivityShared state

# Shared State

Create a two-way connection between your UI and agent state.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is shared state?#

Agentic Copilots maintain a shared state that seamlessly connects your UI with the agent's execution. This shared state system allows you to:

  * Display the agent's current progress and intermediate results
  * Update the agent's state through UI interactions
  * React to state changes in real-time across your application

![Shared State Demo](https://cdn.copilotkit.ai/docs/copilotkit/images/coagents/SharedStateCoAgents.gif)

## When should I use this?#

Use shared state when you want the agent and the user to collaborate through the same application state. The agent's outputs are reflected in the UI, and user updates in the UI are reflected in the agent's execution.

[Building stateful agents?Persistent threads ship with CopilotKit Intelligence on the free Developer tier.Get CopilotKit Intelligence free](https://ssr-placeholder.invalid/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=docs_shared_state&utm_frontend=vue)

## Reading agent state#

Subscribe a component to the agent's state with `useAgent`. Any time the agent mutates its state, for example via a tool call, the composable updates its reactive `agent` ref and your UI re-renders with the new values.

src/components/SharedWorkspace.vue
    
    
    <script setup lang="ts">
    import { computed } from "vue";
    import { useAgent, UseAgentUpdate } from "@copilotkit/vue/v2";
    
    type WorkspaceState = {
      notes?: string[];
      preferences?: { tone?: string };
    };
    
    const { agent } = useAgent({
      agentId: "workspace",
      updates: [UseAgentUpdate.OnStateChanged],
    });
    const state = computed(
      () => (agent.value?.state ?? {}) as WorkspaceState,
    );
    </script>
    
    <template>
      <ul>
        <li v-for="note in state.notes ?? []" :key="note">{{ note }}</li>
      </ul>
    </template>

The returned `agent.value.state` is a plain object. Read it like any other reactive application data and render the parts you care about: agent-written notes, structured outputs, progress indicators, or anything else the agent has put there.

## Writing agent state#

The same agent object exposes `setState`. Calling it from a UI event handler pushes the new value into shared state, and the agent reads it back on its next turn. The UI's writes visibly steer the model.

src/components/SharedWorkspace.vue
    
    
    <script setup lang="ts">
    function setTone(tone: string) {
      const current = agent.value;
      if (!current) return;
    
      const previous = (current.state ?? {}) as WorkspaceState;
      current.setState({
        ...previous,
        preferences: { ...previous.preferences, tone },
      });
    }
    </script>
    
    <template>
      <button @click="setTone('concise')">Prefer concise answers</button>
    </template>

This is what makes the channel two-way: the UI doesn't just observe the agent, it can hand the agent fresh inputs — preferences, selections, or partial work — without going through the chat thread.

## Rendering shared state in the UI#

Because `agent.state` is plain data exposed through a Vue ref, the UI layer is ordinary Vue. The example above wires the agent's outputs into a list and feeds user edits back through `setState`.

Nothing about this is chat-specific: `useAgent` works in any component under `CopilotKitProvider`, so you can render agent state in your main view or canvas, not just inside the chat panel. See **[Render agent state in your app](https://docs.copilotkit.ai/vue/shared-state/rendering-in-app)** for the full main-view pattern.

src/App.vue
    
    
    <script setup lang="ts">
    import { CopilotChat, CopilotKitProvider } from "@copilotkit/vue/v2";
    import SharedWorkspace from "./components/SharedWorkspace.vue";
    </script>
    
    <template>
      <CopilotKitProvider runtime-url="/api/copilotkit">
        <SharedWorkspace />
        <CopilotChat agent-id="workspace" />
      </CopilotKitProvider>
    </template>

## Streaming partial state updates#

By default, agent state only updates _between_ backend checkpoints, so a long-running tool call appears as one big burst at the end. State streaming forwards a specific tool argument straight into a state key _as it's being generated_ , so the UI can watch the answer assemble token-by-token.

Select an AI backend above to see this code example.

See **[State streaming](https://docs.copilotkit.ai/vue/shared-state/streaming)** for the full walkthrough, including the corresponding `useAgent` subscription on the frontend.

## Read-only context#

When a value is **UI-owned** and the agent should read it but never write it back, such as current user, selected record, or scroll position, reach for `useAgentContext` instead of full shared state. It publishes values as a one-way UI-to-agent channel that auto-unregisters on unmount.

`useAgentContext` is a separate read-only capability; it does not replace the bidirectional `agent.state` / `agent.setState(...)` contract above.

See **[Agent read-only context](https://docs.copilotkit.ai/vue/shared-state/agent-readonly)** for the full pattern.

## Choose your AI backend

See [Integrations](https://ssr-placeholder.invalid//integrations) for all available frameworks (shared-state).

### On this page

What is shared state?When should I use this?Reading agent stateWriting agent stateRendering shared state in the UIStreaming partial state updatesRead-only context
