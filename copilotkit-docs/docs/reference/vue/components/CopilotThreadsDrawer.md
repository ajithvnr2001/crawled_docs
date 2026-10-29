---
url: https://docs.copilotkit.ai/reference/vue/components/CopilotThreadsDrawer/
title: CopilotThreadsDrawer
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:46:06.511162+00:00
---

# CopilotThreadsDrawer

> Source: https://docs.copilotkit.ai/reference/vue/components/CopilotThreadsDrawer/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

🪁VueSDK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Components

[CopilotChat](https://docs.copilotkit.ai/reference/vue/components/CopilotChat)[CopilotChatAssistantMessage](https://docs.copilotkit.ai/reference/vue/components/CopilotChatAssistantMessage)[CopilotChatInput](https://docs.copilotkit.ai/reference/vue/components/CopilotChatInput)[CopilotChatMessageView](https://docs.copilotkit.ai/reference/vue/components/CopilotChatMessageView)[CopilotChatUserMessage](https://docs.copilotkit.ai/reference/vue/components/CopilotChatUserMessage)[CopilotChatView](https://docs.copilotkit.ai/reference/vue/components/CopilotChatView)[CopilotKitProvider](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider)[CopilotPopup](https://docs.copilotkit.ai/reference/vue/components/CopilotPopup)[CopilotSidebar](https://docs.copilotkit.ai/reference/vue/components/CopilotSidebar)[CopilotThreadsDrawer](https://docs.copilotkit.ai/reference/vue/components/CopilotThreadsDrawer)

Hooks

[useAgent](https://docs.copilotkit.ai/reference/vue/hooks/useAgent)[useAgentContext](https://docs.copilotkit.ai/reference/vue/hooks/useAgentContext)[useCapabilities](https://docs.copilotkit.ai/reference/vue/hooks/useCapabilities)[useComponent](https://docs.copilotkit.ai/reference/vue/hooks/useComponent)[useConfigureSuggestions](https://docs.copilotkit.ai/reference/vue/hooks/useConfigureSuggestions)[useCopilotChatConfiguration](https://docs.copilotkit.ai/reference/vue/hooks/useCopilotChatConfiguration)[useCopilotKit](https://docs.copilotkit.ai/reference/vue/hooks/useCopilotKit)[useDefaultRenderTool](https://docs.copilotkit.ai/reference/vue/hooks/useDefaultRenderTool)[useFrontendTool](https://docs.copilotkit.ai/reference/vue/hooks/useFrontendTool)[useHumanInTheLoop](https://docs.copilotkit.ai/reference/vue/hooks/useHumanInTheLoop)[useInterrupt](https://docs.copilotkit.ai/reference/vue/hooks/useInterrupt)[useRenderTool](https://docs.copilotkit.ai/reference/vue/hooks/useRenderTool)[useSuggestions](https://docs.copilotkit.ai/reference/vue/hooks/useSuggestions)[useThreads](https://docs.copilotkit.ai/reference/vue/hooks/useThreads)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[Reference](https://docs.copilotkit.ai/reference)[vue](https://docs.copilotkit.ai/reference/vue)Components

# CopilotThreadsDrawer

Vue 3 threads drawer that lists and manages conversations next to CopilotChat

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`CopilotThreadsDrawer` renders the prebuilt conversation drawer beside [`CopilotChat`](https://docs.copilotkit.ai/reference/vue/components/CopilotChat). It is a thin Vue wrapper around the framework-agnostic `<copilotkit-threads-drawer>` custom element and stays SSR-safe by loading that element only on mount. The drawer reads from [`useThreads`](https://docs.copilotkit.ai/reference/vue/hooks/useThreads), follows the surrounding chat configuration when one is present, and lets the user switch, start, archive, unarchive, delete, and filter threads.

When `onThreadSelect` and `onNewThread` are omitted, the wrapper drives the surrounding chat configuration directly: selecting a row calls `setActiveThreadId(threadId, { explicit: true })`, and the "New Conversation" action resets the chat with `startNewThread()`. Provide those callbacks only if you want to control the active thread yourself.

Thread rename is not exposed in the drawer row menu. Use [`useThreads`](https://docs.copilotkit.ai/reference/vue/hooks/useThreads) for headless rename support.

The threads drawer requires a license. When it is not licensed, the component renders the locked state and keeps the thread store disabled. Visit [copilotkit.ai/pricing](https://copilotkit.ai/pricing) for details.

## Import
    
    
    <script setup lang="ts">
    import { CopilotThreadsDrawer } from "@copilotkit/vue/v2";
    import "@copilotkit/vue/styles.css";
    </script>

## Props

Prop

Type

`agentId?`string

Prop

Type

`onThreadSelect?`(threadId: string) => void

Prop

Type

`onNewThread?`() => void

Prop

Type

`onLicensed?`() => void

Prop

Type

`licenseUrl?`string

Prop

Type

`label?`string

Prop

Type

`recentLabel?`string

Prop

Type

`limit?`number

Prop

Type

`collapsible?`boolean

Prop

Type

`dataTestId?`string

## Events

The Vue wrapper emits the following events.

Event| Payload| Fired when  
---|---|---  
`collapse-change`| `collapsed: boolean`| The desktop collapse state changes  
  
## Slots

Vue uses named slots in place of React render props. `CopilotThreadsDrawer` only defines one scoped Vue slot; everything else is projected into the underlying custom element with a `slot` attribute.

Prop

Type

`row?`{ thread: Thread }

Light-DOM children with these `slot` names are projected into the drawer:

Slot| Replaces  
---|---  
`header`| The drawer header region  
`empty`| The empty-state body  
`footer`| A footer region  
`memories`| The reserved memories surface  
`launcher-icon`| The icon inside the mobile launcher  
`licensed`| The licensed upsell content  
  
Style the shadow DOM with `::part()`. The drawer exposes the usual structural and action parts, including the root, header, list, row, menu, new-thread button, section heading, filter controls, collapse controls, launcher, load-more, fetch-more-error, and licensed surfaces.

## Usage

### Basic usage

Wrap the drawer and `CopilotChat` in a shared `CopilotChatConfigurationProvider` so they operate on the same active thread. This example includes the surrounding `CopilotKitProvider`, so it is runnable as shown.
    
    
    <script setup lang="ts">
    import {
      CopilotChat,
      CopilotChatConfigurationProvider,
      CopilotKitProvider,
      CopilotThreadsDrawer,
    } from "@copilotkit/vue/v2";
    import "@copilotkit/vue/styles.css";
    </script>
    
    <template>
      <CopilotKitProvider runtime-url="http://localhost:8200/api/copilotkit">
        <CopilotChatConfigurationProvider agent-id="support">
          <div class="flex h-full">
            <CopilotThreadsDrawer agent-id="support" />
            <CopilotChat agent-id="support" />
          </div>
        </CopilotChatConfigurationProvider>
      </CopilotKitProvider>
    </template>

### Custom row and projected chrome
    
    
    <script setup lang="ts">
    import { CopilotThreadsDrawer } from "@copilotkit/vue/v2";
    </script>
    
    <template>
      <CopilotThreadsDrawer label="History">
        <span slot="header">My conversations</span>
        <span slot="empty">No threads yet.</span>
    
        <template #row="{ thread }">
          <strong>{{ thread.name ?? "New conversation" }}</strong>
        </template>
      </CopilotThreadsDrawer>
    </template>

### Observing collapse state
    
    
    <script setup lang="ts">
    import { CopilotThreadsDrawer } from "@copilotkit/vue/v2";
    
    function onCollapseChange(collapsed: boolean) {
      console.log("drawer collapsed:", collapsed);
    }
    </script>
    
    <template>
      <CopilotThreadsDrawer @collapse-change="onCollapseChange" />
    </template>

## Behavior

  * The drawer registers itself with the surrounding chat configuration so the mobile launcher can appear.
  * When callbacks are omitted, selecting a row calls `setActiveThreadId` and "New Conversation" calls `startNewThread`.
  * Archive, unarchive, delete, and pagination all flow through `useThreads`.
  * The drawer stays inert while unlicensed, which keeps the thread store from fetching until licensing resolves.
  * Rename is headless only; use `useThreads().renameThread()` if you need that action.
  * The wrapper is SSR-safe because the custom element is imported lazily on the client.



## Related

  * [`CopilotChat`](https://docs.copilotkit.ai/reference/vue/components/CopilotChat) \- the chat surface this drawer usually drives
  * [`CopilotChatConfigurationProvider`](https://docs.copilotkit.ai/reference/vue/hooks/useCopilotChatConfiguration) \- shared configuration context
  * [`useThreads`](https://docs.copilotkit.ai/reference/vue/hooks/useThreads) \- the headless thread data and mutation layer


