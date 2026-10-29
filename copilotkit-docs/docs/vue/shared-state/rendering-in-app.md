---
url: https://docs.copilotkit.ai/vue/shared-state/rendering-in-app/
title: Render agent state in your app
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:46:29.437084+00:00
---

# Render agent state in your app

> Source: https://docs.copilotkit.ai/vue/shared-state/rendering-in-app/

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

Render agent state in your app

InteractivityShared state

# Render agent state in your app

Read agent.state with useAgent and render it in your main view or canvas.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

[Shared state](https://docs.copilotkit.ai/vue/shared-state) is most powerful when the agent's state shows up in your application UI, such as a dashboard, document canvas, map, or table. Because `agent.state` is plain data exposed through a Vue ref, you can subscribe from any descendant component and render it however you like.

## The pattern#

`useAgent` works in any component under `CopilotKitProvider`; it does not have to be near the chat. Call it in your main-view component, read `agent.value.state`, and render:

src/components/Canvas.vue
    
    
    <script setup lang="ts">
    import { computed, watchEffect } from "vue";
    import { useAgent, UseAgentUpdate } from "@copilotkit/vue/v2";
    
    type CanvasState = {
      title: string;
      items: { id: string; label: string; done: boolean }[];
    };
    
    const initialState: CanvasState = {
      title: "Project launch",
      items: [
        { id: "research", label: "Research user needs", done: true },
        { id: "prototype", label: "Build a prototype", done: false },
      ],
    };
    
    const { agent } = useAgent({
      updates: [UseAgentUpdate.OnStateChanged],
    });
    const state = computed(
      () => (agent.value?.state ?? {}) as Partial<CanvasState>,
    );
    
    watchEffect(() => {
      const currentAgent = agent.value;
      if (!currentAgent) return;
    
      const current = (currentAgent.state ?? {}) as Partial<CanvasState>;
      const updates: Partial<CanvasState> = {};
      if (current.title === undefined) updates.title = initialState.title;
      if (current.items === undefined) updates.items = initialState.items;
    
      if (Object.keys(updates).length > 0) {
        currentAgent.setState({ ...current, ...updates });
      }
    });
    </script>
    
    <template>
      <main class="canvas">
        <h1>{{ state.title ?? "Untitled" }}</h1>
        <ul>
          <li
            v-for="item in state.items ?? []"
            :key="item.id"
            :data-done="item.done"
          >
            {{ item.label }}
          </li>
        </ul>
      </main>
    </template>

The `initialState` value is UI-owned initial state for this example. It makes the canvas visible before the agent writes state. The effect sets only `undefined` fields and preserves all other state. If the backend owns the initial state, define it in the shared-state setup for that framework.

Every time the agent mutates its state, whether from a tool call, node transition, or [streamed update](https://docs.copilotkit.ai/vue/shared-state/streaming), `useAgent` updates the ref and Vue re-renders this component. The chat can be in a sidebar, a popup, or absent entirely; your canvas updates the same way.

## Put it anywhere in your layout#

The agent lives on `CopilotKitProvider`, so the chat surface and your main-view components are two consumers of the same agent. A typical layout renders the canvas as the primary content and the chat alongside it:

src/App.vue
    
    
    <script setup lang="ts">
    import { CopilotChat, CopilotKitProvider } from "@copilotkit/vue/v2";
    import Canvas from "./components/Canvas.vue";
    </script>
    
    <template>
      <CopilotKitProvider runtime-url="/api/copilotkit">
        <div class="app-shell">
          <Canvas />
          <CopilotChat />
        </div>
      </CopilotKitProvider>
    </template>

`<Canvas>` and `<CopilotChat>` resolve the same default agent, so they share one agent instance and one state object. There is nothing chat-specific about reading `agent.state`; the chat is just another consumer.

## Writing back from the main view#

The same agent exposes `setState`, so your canvas can be interactive rather than a read-only mirror. A click handler can push a new value that the agent reads on its next turn:
    
    
    function toggleItem(id: string) {
      const currentAgent = agent.value;
      if (!currentAgent) return;
    
      const current = (currentAgent.state ?? {}) as Partial<CanvasState>;
      currentAgent.setState({
        ...current,
        items: (current.items ?? []).map((item) =>
          item.id === id ? { ...item, done: !item.done } : item,
        ),
      });
    }

This is the same two-way channel described in [Shared State](https://docs.copilotkit.ai/vue/shared-state). The only difference is that the reads and writes happen in your application's main surface rather than in the chat.

## Tips#

  * **Target a specific agent** with `useAgent({ agentId: "research-agent" })` when you have more than one. The default is the agent named `"default"`.
  * **Throttle high-frequency updates** with `useAgent({ throttleMs })` if a streaming run re-renders a heavy canvas too often.
  * **Treat`agent.state` as possibly partial** while a run is in progress. Guard with defaults so half-streamed state does not crash your render.



## Related#

  * [Shared State](https://docs.copilotkit.ai/vue/shared-state): the full read/write model and the underlying `useAgent` subscription.
  * [State streaming](https://docs.copilotkit.ai/vue/shared-state/streaming): stream a tool argument into a state key so the canvas fills in token-by-token.
  * [Agent read-only context](https://docs.copilotkit.ai/vue/shared-state/agent-readonly): push UI values _to_ the agent without letting it write back.
  * [`useAgent` reference](https://docs.copilotkit.ai/reference/vue/hooks/useAgent): full composable signature and options.



### On this page

The patternPut it anywhere in your layoutWriting back from the main viewTipsRelated
