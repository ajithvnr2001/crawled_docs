---
url: https://docs.copilotkit.ai/vue/headless-threads/
title: Headless Threads
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:46:24.186783+00:00
---

# Headless Threads

> Source: https://docs.copilotkit.ai/vue/headless-threads/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendVueAgent backendCopilotKit

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Quickstart](https://docs.copilotkit.ai/vue)[Using these docs](https://docs.copilotkit.ai/vue/using-these-docs)[Build with agents](https://docs.copilotkit.ai/vue/build-with-agents)[Intelligence](https://docs.copilotkit.ai/vue/intelligence/overview)

Basics

Chat

Threads

[Threads Drawer](https://docs.copilotkit.ai/vue/prebuilt-components/copilot-threads-drawer)[Headless Threads](https://docs.copilotkit.ai/vue/headless-threads)

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

Headless Threads

BasicsThreads

# Headless Threads

Build a custom thread UI with useThreads while CopilotKit handles persistence, replay, synchronization, and lifecycle infrastructure.

## What is this?#

CopilotKit Rich Threads enable persistent, resumable multi-turn conversations. The `useThreads` composable lists, creates, renames, archives, and deletes CopilotKit Intelligence threads with realtime synchronization. Threads work with any agent framework because CopilotKit Intelligence stores conversation history server-side, so users can close their browser and pick up where they left off. It does not list or mutate native LangGraph, ADK, or other framework stores unless your backend explicitly bridges those systems.

## Conversations that never lose context.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

CopilotKit Intelligence AG-UI Streams keep messages, generative UI, and tool activity available across sessions and devices. Build a new agent or bring one you already have. Any frontend, any backend. 

Prebuilt thread UI: Threads Drawer

If your app came from a CopilotKit CLI starter, it may already include the prebuilt **[Threads Drawer](https://docs.copilotkit.ai/vue/prebuilt-components/copilot-threads-drawer)**. Keep it for the shortest path to a production thread switcher. Use the `useThreads` steps below when adding custom thread UI or replacing the Drawer with your own layout and interactions, including thread rename.

## When should I use this?#

  * Your app needs multiple saved conversations per user, like a chat-history sidebar.
  * Users should be able to resume a prior conversation across sessions or devices.
  * You want realtime sync so threads created on one tab appear on another.
  * You need to let users organize conversations by renaming or archiving them.



## Prerequisites#

  * A CopilotKit application connected to CopilotKit Intelligence
  * The current `@copilotkit/vue` v2 package
  * A model provider key supported by your runtime



For multi-user applications, configure the runtime to [scope Rich Threads to the signed-in user](https://docs.copilotkit.ai/vue/threads-lifecycle#scope-rich-threads-to-the-signed-in-user) before exposing thread lists or lifecycle actions.

## Implementation#

Migrating existing history?

Threads capture new CopilotKit conversations once your app is connected to CopilotKit Intelligence. To move historical Google ADK or LangGraph conversations into the same store, start with [Import & Synchronize Thread History](https://docs.copilotkit.ai/threads-import), or the framework-specific synchronization guide.

### Configure your Runtime with CopilotKit Intelligence#

Your `CopilotRuntime` must be connected to CopilotKit Intelligence before the thread UI can list and resume conversations. CLI-created starters generate this setup; otherwise follow [Connect your runtime to Intelligence](https://docs.copilotkit.ai/intelligence/connect-your-runtime).

server.ts
    
    
    import {
      CopilotKitIntelligence,
      CopilotRuntime,
    } from "@copilotkit/runtime/v2";
    
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
      // generateThreadNames: false,
      // lockTtlSeconds: 20,
      // lockHeartbeatIntervalSeconds: 15,
      // lockKeyPrefix: "my-app",
    });

Keep the project-scoped `CPK_INTELLIGENCE_API_KEY` on the server. Existing Intelligence-enabled apps should retain their current runtime configuration.

Option| Default| Max| Description  
---|---|---|---  
`lockTtlSeconds`| `20`| `3600`| How long a run lock is held before it expires.  
`lockHeartbeatIntervalSeconds`| `15`| `3000`| How often the runtime renews the lock.  
`lockKeyPrefix`| —| —| Optional Redis prefix when several apps share one instance.  
  
### List and manage threads with useThreads#

`useThreads` returns reactive refs for the thread list and loading state, plus mutation methods.

src/components/ThreadSidebar.vue
    
    
    <script setup lang="ts">
    import {
      useCopilotChatConfiguration,
      useThreads,
    } from "@copilotkit/vue/v2";
    
    const config = useCopilotChatConfiguration();
    const {
      threads,
      isLoading,
      renameThread,
      archiveThread,
      deleteThread,
    } = useThreads({ agentId: "my-agent" });
    </script>
    
    <template>
      <p v-if="isLoading">Loading…</p>
      <ul v-else>
        <li v-for="thread in threads" :key="thread.id">
          <button
            @click="config?.setActiveThreadId(thread.id, { explicit: true })"
          >
            {{ thread.name ?? "New conversation" }}
          </button>
          <button @click="renameThread(thread.id, 'Renamed')">Rename</button>
          <button @click="archiveThread(thread.id)">Archive</button>
          <button @click="deleteThread(thread.id)">Delete</button>
        </li>
      </ul>
    </template>

The array is sorted by recent activity and stays synchronized in realtime. `archiveThread` is a soft delete hidden from the default list; pass `includeArchived: true` to include archived threads. `deleteThread` is permanent and irreversible. Neither method shows a confirmation dialog, so add one where appropriate.

### Switch between threads#

Keep the list and chat inside one `CopilotChatConfigurationProvider`. Selecting a row with `setActiveThreadId(..., { explicit: true })` clears the current view, connects the chat to the selected thread, and replays its history. If a run is still active, the chat rejoins its stream.

src/App.vue
    
    
    <script setup lang="ts">
    import {
      CopilotChat,
      CopilotChatConfigurationProvider,
      CopilotKitProvider,
    } from "@copilotkit/vue/v2";
    import ThreadSidebar from "./components/ThreadSidebar.vue";
    </script>
    
    <template>
      <CopilotKitProvider runtime-url="/api/copilotkit">
        <CopilotChatConfigurationProvider agent-id="my-agent">
          <div class="flex" style="height: 100dvh">
            <ThreadSidebar />
            <CopilotChat />
          </div>
        </CopilotChatConfigurationProvider>
      </CopilotKitProvider>
    </template>

### Add pagination for large thread lists#

Pass `limit` for cursor-based pagination and render `fetchMoreThreads` while more pages remain:
    
    
    <script setup lang="ts">
    const {
      threads,
      hasMoreThreads,
      isFetchingMoreThreads,
      fetchMoreThreads,
    } = useThreads({ agentId: "my-agent", limit: 20 });
    </script>
    
    <template>
      <button
        v-if="hasMoreThreads"
        :disabled="isFetchingMoreThreads"
        @click="fetchMoreThreads"
      >
        {{ isFetchingMoreThreads ? "Loading…" : "Load more" }}
      </button>
    </template>

## Next steps#

  * **Prebuilt UI:** [Threads Drawer](https://docs.copilotkit.ai/vue/prebuilt-components/copilot-threads-drawer) — the drop-in Vue thread switcher.
  * **Thread architecture:** [Threads & Persistence Architecture](https://docs.copilotkit.ai/intelligence/threads-explained) — event replay and realtime sync.
  * **Production self-hosting:** [Self-host CopilotKit Intelligence](https://docs.copilotkit.ai/intelligence/self-hosting).
  * **API reference:** [`useThreads`](https://docs.copilotkit.ai/reference/vue/hooks/useThreads) — parameters, return values, and types.



### On this page

What is this?When should I use this?PrerequisitesImplementationNext steps
