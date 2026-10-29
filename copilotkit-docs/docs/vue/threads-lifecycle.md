---
url: https://docs.copilotkit.ai/vue/threads-lifecycle/
title: Thread & History Lifecycle
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:46:29.888111+00:00
---

# Thread & History Lifecycle

> Source: https://docs.copilotkit.ai/vue/threads-lifecycle/

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

[Overview](https://docs.copilotkit.ai/vue/AG-UI-Streams)[Bring your own thread system](https://docs.copilotkit.ai/vue/intelligence/bring-your-own-thread-system)[Add to Existing Threads](https://docs.copilotkit.ai/vue/threads-import)[Thread & History Lifecycle](https://docs.copilotkit.ai/vue/threads-lifecycle)[Streams & Framework Threads](https://docs.copilotkit.ai/vue/intelligence/threads-explained)

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

Thread & History Lifecycle

IntelligenceFeaturesAG-UI Streams

# Thread & History Lifecycle

How a threadId is created, how conversation history is restored, how to switch or start threads, and how CopilotKit threads relate to your agent framework's own persistence.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

Every CopilotKit conversation is scoped to a **thread** , identified by a `threadId`. This page explains the full client lifecycle: how the id is created, how prior history is restored, how to switch or start threads, and where CopilotKit's threads end and your agent framework's own persistence begins.

This page describes the current Vue v2 composables and components imported from `@copilotkit/vue/v2`.

## The lifecycle at a glance#

  1. **Mint.** When a chat mounts without an explicit `threadId`, the client generates a UUID v4.
  2. **Run.** Messages and tool calls stream under that id. If a server-side store is configured, they are persisted as they happen; a runtime with no persistence layer keeps nothing server-side.
  3. **Hydrate.** When a chat mounts with a known id, the client connects and replays persisted history into the UI.
  4. **Switch / start.** You select a known thread and restore it, or start a fresh one and clear the view.



## How the threadId is created#

When you do not supply one, CopilotKit mints a `threadId` on the client during component setup. The value is resolved by this precedence, highest first:

  1. An explicit `threadId` prop on `<CopilotChat>` or `<CopilotChatConfigurationProvider>`; this is authoritative and drives replay.
  2. An active-thread override from `setActiveThreadId(...)`, a picked drawer row, or `startNewThread()`.
  3. A `threadId` inherited from a parent configuration provider.
  4. A non-authoritative `threadId` seed.
  5. Otherwise, a freshly minted UUID.



Explicit threadId (recommended when you own persistence)
    
    
    <CopilotChat agent-id="my-agent" :thread-id="myThreadId" />

**Auto-minted ids survive reactive re-renders but re-mint when the component remounts.** If a changed `:key`, route transition, or parent unmount/remount recreates the chat configuration, the fallback id changes and a new conversation begins. Mint and persist the id yourself when continuity must survive remounts.

## How history is restored (hydration)#

CopilotKit Vue v2 does **not** use an `initialMessages` prop to seed a conversation. History is restored in one of two ways.

**1\. Server-side replay.** When a chat mounts with an explicit `threadId`, the client assigns `agent.threadId` and connects the agent. Persisted event history replays into the UI without manual message wiring:
    
    
    <CopilotChat agent-id="my-agent" :thread-id="existingThreadId" />

Replay requires a **server-side store to replay from** , such as CopilotKit Intelligence or a persisting `AgentRunner`. A self-hosted runtime with no persistence layer has nothing to replay, so the connection returns an empty stream. If history is not restoring, check the server-side store before the Vue code.

For a fresh non-explicit thread, such as one created by `startNewThread()`, there is nothing to replay, so the view is cleared instead.

**2\. Manual hydration.** For non-platform or custom cases, read messages from your store and set them directly on the agent:

src/components/RestoreHistory.vue
    
    
    <script setup lang="ts">
    import { watch } from "vue";
    import { useAgent } from "@copilotkit/vue/v2";
    
    const props = defineProps<{ threadId: string }>();
    const { agent } = useAgent({ agentId: "my-agent" });
    
    watch(
      [() => agent.value, () => props.threadId],
      async ([current, threadId], _previous, onCleanup) => {
        if (!current) return;
        let cancelled = false;
        onCleanup(() => { cancelled = true; });
    
        const messages = await myApi.getMessages(threadId);
        if (!cancelled) current.setMessages(messages);
      },
      { immediate: true },
    );
    </script>
    
    <template />

Read the current conversation from `agent.value.messages`; replace or append with `setMessages(...)` and `addMessage(...)`.

## Scope Rich Threads to the signed-in user#

Your application owns end-user authentication. For an Intelligence-enabled runtime, implement `identifyUser(request)` with the server-verified session or token and return a stable user id and name:

server.ts
    
    
    import { CopilotKitIntelligence, CopilotRuntime } from "@copilotkit/runtime/v2";
    
    const runtime = new CopilotRuntime({
      agents: { default: agent },
      intelligence: new CopilotKitIntelligence({
        apiKey: process.env.CPK_INTELLIGENCE_API_KEY!,
      }),
      identifyUser: async (request) => {
        const session = await verifyAppSession(request);
        if (!session?.user) throw new Error("Unauthorized");
        return { id: session.user.id, name: session.user.name };
      },
    });

CopilotKit Intelligence combines that application user identity with the project when it scopes lists, subscriptions, history, rename, archive, unarchive, and delete operations. The project runtime key is a separate server credential; do not treat the developer who created it as the application user.

A static `identifyUser` value is suitable only for a single-user demo. In a multi-user application, every request must resolve the authenticated application user or those users will share a thread scope.

See [Authentication](https://docs.copilotkit.ai/auth) for forwarding and verifying auth context, and [Connect your runtime to Intelligence](https://docs.copilotkit.ai/intelligence/connect-your-runtime) for the full Intelligence configuration.

## Switching threads and starting new ones#

Set the active thread to restore its history, or start a fresh conversation:

src/components/ThreadControls.vue
    
    
    <script setup lang="ts">
    import { useCopilotChatConfiguration } from "@copilotkit/vue/v2";
    
    const { existingId } = defineProps<{ existingId: string }>();
    const config = useCopilotChatConfiguration();
    </script>
    
    <template>
      <button
        @click="config?.setActiveThreadId(existingId, { explicit: true })"
      >
        Open conversation
      </button>
      <button @click="config?.startNewThread()">New chat</button>
    </template>

  * `setActiveThreadId(threadId, { explicit })`: `explicit: true`, the default, treats it as a known thread and replays history. `explicit: false` shows the welcome screen.
  * `startNewThread()`: resets to a freshly minted, non-explicit id. Custom sidebars must call this configuration method to mint and switch the active thread. To reproduce the built-in drawer's behavior, also call `useThreads().startNewThread()` to clear stale thread-store error state.



Both methods no-op and warn when the `threadId` is prop-controlled. If you drive threads imperatively, do not also pass an authoritative `threadId` prop. Pick one source of truth.

## Creating a thread with your own API on the first message#

A common ask is to intercept the first message, create a row through your own backend, and use its id before the conversation starts.

**On the built-in`<CopilotChat>`, the `submit-message` event is observational.** The component emits it and then continues its own add-message/run flow; it is not an async interception seam that can delay that same run.

**Recommended: mint up front and drive the id.** Create the thread before rendering the chat, or from the New chat action, then pass it through the configuration:
    
    
    async function startConversation() {
      const { id } = await myApi.createThread();
      config.value?.setActiveThreadId(id, { explicit: true });
    }

**At submit-time, use a headless input.** Compose your own input and handler, set the id on the agent before adding the message, then run the agent:
    
    
    async function submit(text: string) {
      const current = agent.value;
      if (!current) return;
    
      const { id } = await myApi.createThread();
      current.threadId = id;
      current.addMessage({ id: crypto.randomUUID(), role: "user", content: text });
      await copilotkit.value.runAgent({ agent: current });
    }

For a run fired in the same handler, set the id on the **agent**. `setActiveThreadId(id)` updates configuration reactively and reaches the agent later, so an immediate run could still use the prior thread.

## CopilotKit threads vs. your framework's checkpointer#

These are two different layers, correlated only by the shared `threadId`:

Layer| What it stores| Managed by  
---|---|---  
**CopilotKit threads**|  Conversation list and AG-UI event history, with realtime sync| CopilotKit Intelligence, through `useThreads`  
**Framework-native persistence**|  Framework-internal state and checkpoints| Your agent, such as a LangGraph checkpointer  
  
A LangGraph checkpointer creates LangGraph's own checkpoint tables. It does not create a CopilotKit threads table. Conversely, CopilotKit rename/archive/delete actions do not reach into LangGraph, ADK, or other native stores unless your backend explicitly bridges them.

The bridge is the `threadId`: CopilotKit forwards an explicit id to the backend as the AG-UI `threadId`, which the framework can use directly or map to its own identifier.

### Future runs can remain durable in both places#

After historical import, future conversations run through CopilotKit can be written to CopilotKit Intelligence while the agent continues using its durable native checkpointer or session service. Users get AG-UI replay, generative UI, multimodal history, and realtime continuity while the framework retains its own storage and analytics.

This is coordinated persistence during future CopilotKit-mediated runs, not general database replication. CopilotKit lifecycle actions still apply only to the CopilotKit thread unless you build a bridge.

## MCP Apps activity and history#

MCP Apps render through activity messages, and rendering is a client-side concern. The visible iframe is re-derived from the replayed conversation when it loads; it is not a separately stored artifact.

If the server-side store replays the thread's tool-call and activity history, the Vue renderer runs again during hydration. There is no separate MCP Apps store to configure.

## See also#

  * [Headless Threads](https://docs.copilotkit.ai/vue/headless-threads) — the full Vue `useThreads` API.
  * [Threads & Persistence Architecture](https://docs.copilotkit.ai/intelligence/threads-explained) — server-side replay, resume, and realtime sync.
  * [Multi-conversation chat](https://docs.copilotkit.ai/tutorials/multi-conversation-chat) — build a history sidebar.
  * [Importing and synchronizing thread history](https://docs.copilotkit.ai/threads-import) — bring existing framework conversations into the platform.



### On this page

What is this?The lifecycle at a glanceHow the threadId is createdHow history is restored (hydration)Scope Rich Threads to the signed-in userSwitching threads and starting new onesCreating a thread with your own API on the first messageCopilotKit threads vs. your framework's checkpointerFuture runs can remain durable in both placesMCP Apps activity and historySee also
