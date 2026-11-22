---
url: https://docs.copilotkit.ai/reference/vue/components/CopilotThreadsDrawer/
title: CopilotThreadsDrawer
method: scrapling+scrapegraph
fetched_at: 2026-11-22T11:00:19.030410+00:00
---

# CopilotThreadsDrawer

> Source: https://docs.copilotkit.ai/reference/vue/components/CopilotThreadsDrawer/

Vue/Components

# CopilotThreadsDrawer

Vue 3 threads drawer that lists and manages conversations next to CopilotChat

Copy MarkdownOpen

## OverviewCopy Anchor Link

`CopilotThreadsDrawer` renders the prebuilt conversation drawer beside [`CopilotChat`](https://docs.copilotkit.ai/reference/vue/components/CopilotChat). The drawer lists the threads from [`useThreads`](https://docs.copilotkit.ai/reference/vue/hooks/useThreads). The user can switch, start, archive, unarchive, delete, and filter threads. The drawer uses the surrounding chat configuration when one is present. It wraps the `<copilotkit-threads-drawer>` custom element and loads that element only in the browser, so it is safe for SSR.

When `onThreadSelect` and `onNewThread` are omitted, the wrapper drives the surrounding chat configuration directly: selecting a row calls `setActiveThreadId(threadId, { explicit: true })`, and the "New Conversation" action resets the chat with `startNewThread()`. Provide those callbacks only if you want to control the active thread yourself.

Thread rename is not exposed in the drawer row menu. Use [`useThreads`](https://docs.copilotkit.ai/reference/vue/hooks/useThreads) for headless rename support.

The threads drawer requires a license. When it is not licensed, the component renders the locked state and keeps the thread store disabled. Visit [copilotkit.ai/pricing](https://copilotkit.ai/pricing) for details.

## ImportCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotThreadsDrawer } from "@copilotkit/vue/v2";
    import "@copilotkit/vue/styles.css";
    </script>

## PropsCopy Anchor Link

Prop

Type

`agentId?`string

`onThreadSelect?`(threadId: string) => void

`onNewThread?`() => void

`onLicensed?`() => void

`licenseUrl?`string

`label?`string

`recentLabel?`string

`limit?`number

`collapsible?`boolean

`dataTestId?`string

## EventsCopy Anchor Link

The Vue wrapper emits the following events.

Event| Payload| Fired when  
---|---|---  
`collapse-change`| `collapsed: boolean`| The desktop collapse state changes  
  
## SlotsCopy Anchor Link

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
  
Style the shadow DOM with `::part()`, for example `copilotkit-threads-drawer::part(row-active)`. The drawer exposes these parts:

Area| Parts  
---|---  
Drawer| `root`, `header`, `backdrop`, `close-toggle`, `collapse-toggle`  
Launcher| `launcher`, `launcher-cluster`, `launcher-new-thread`  
Thread list| `new-thread-button`, `section-heading`, `list`, `loading`, `empty`, `error`, `retry-button`  
Pagination| `load-more`, `fetching-more`, `fetch-more-error`, `fetch-more-retry`  
Filters| `filter-toggle`, `filter-indicator`, `filters`, `filter-all`, `filter-active`  
Rows| `row`, `row-active`, `row-name`, `row-menu`, `row-menu-popover`, `row-archive`, `row-unarchive`, `row-delete`  
Delete confirmation| `confirm-dialog`, `confirm-cancel`, `confirm-delete`  
Memories, footer, and locked state| `memories`, `footer`, `licensed`, `licensed-cta`  
  
## UsageCopy Anchor Link

### Basic usageCopy Anchor Link

Wrap the drawer and `CopilotChat` in a shared [`CopilotChatConfigurationProvider`](https://docs.copilotkit.ai/reference/vue/hooks/useCopilotChatConfiguration) so they operate on the same active thread. This example includes the surrounding `CopilotKitProvider`, so it is runnable as shown.

Copy Text
    
    
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

### Custom row and projected chromeCopy Anchor Link

Copy Text
    
    
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

### Observing collapse stateCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotThreadsDrawer } from "@copilotkit/vue/v2";
    
    function onCollapseChange(collapsed: boolean) {
      console.log("drawer collapsed:", collapsed);
    }
    </script>
    
    <template>
      <CopilotThreadsDrawer @collapse-change="onCollapseChange" />
    </template>

## BehaviorCopy Anchor Link

  * The drawer registers itself with the surrounding chat configuration so the mobile launcher can appear.
  * When callbacks are omitted, selecting a row calls `setActiveThreadId` and "New Conversation" calls `startNewThread`.
  * Archive, unarchive, delete, and pagination all flow through `useThreads`.
  * The drawer stays inert while unlicensed, which keeps the thread store from fetching until licensing resolves.
  * Rename is headless only; use `useThreads().renameThread()` if you need that action.
  * The wrapper is SSR-safe because the custom element is imported lazily on the client.



How is this guide?

GoodBad

[Previous PageCopilotSidebar](https://docs.copilotkit.ai/reference/vue/components/CopilotSidebar)[Next PageGenerativeUISurface](https://docs.copilotkit.ai/reference/vue/components/GenerativeUISurface)
