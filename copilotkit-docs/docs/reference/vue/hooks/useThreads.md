---
url: https://docs.copilotkit.ai/reference/vue/hooks/useThreads/
title: useThreads
method: scrapling+scrapegraph
fetched_at: 2026-11-22T11:00:18.094180+00:00
---

# useThreads

> Source: https://docs.copilotkit.ai/reference/vue/hooks/useThreads/

Vue/Hooks

# useThreads

Vue 3 composable for listing and mutating CopilotKit threads

Copy MarkdownOpen

[Thread rename, archive, and delete need a CopilotKit Intelligence projectConnect your runtime to a cloud-hosted project to start syncing threads.Start cloud-hosted setup](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=docs_reference_vue_use_threads&utm_frontend=react)

## OverviewCopy Anchor Link

`useThreads` is a Vue 3 composable for reading the active thread list for an agent and mutating that list from the client. It accepts reactive inputs for a required agent id, archived filter, page size, and an `enabled` flag. When `enabled` is `false`, the hook clears its thread-store context and skips `/threads` entirely; that is how [the threads drawer](https://docs.copilotkit.ai/reference/vue/components/CopilotThreadsDrawer) stays idle while unlicensed.

`useThreads` activates when the connected runtime (see [`CopilotKitProvider`](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider)) provides the thread endpoints it needs. It stays idle when the runtime explicitly reports that thread listing is unavailable.

The hook returns normalized thread records with only the fields the Vue UI consumes: `id`, `agentId`, `name`, `archived`, `createdAt`, `updatedAt`, and optional `lastRunAt`. Threads are ordered by `lastRunAt`, then `updatedAt`, then `createdAt`.

`error` includes runtime and configuration problems such as a missing runtime URL or unsupported thread endpoints. `listError` only reports genuine list and mutation failures from the thread store.

## SignatureCopy Anchor Link

Copy Text
    
    
    import { useThreads } from "@copilotkit/vue/v2";
    
    function useThreads(input: UseThreadsInput): UseThreadsResult;

## ParametersCopy Anchor Link

Prop

Type

`input?`UseThreadsInput

## Return ValueCopy Anchor Link

Prop

Type

`object?`UseThreadsResult

## UsageCopy Anchor Link

### Listing threadsCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { computed } from "vue";
    import { useThreads } from "@copilotkit/vue/v2";
    
    const { threads, isLoading, listError, refetchThreads } = useThreads({
      agentId: "support-agent",
      includeArchived: true,
      limit: 20,
    });
    
    const activeThreads = computed(() =>
      threads.value.filter((thread) => !thread.archived),
    );
    </script>

### Paginating manuallyCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { useThreads } from "@copilotkit/vue/v2";
    
    const { hasMoreThreads, fetchMoreThreads, fetchMoreError } = useThreads({
      agentId: "support-agent",
      limit: 20,
    });
    </script>

## BehaviorCopy Anchor Link

  * The hook stays reactive to `agentId`, `includeArchived`, `limit`, and `enabled`.
  * When the runtime URL is missing or the runtime reports thread endpoints as unsupported, `error` is set and `listError` stays focused on store failures.
  * `enabled: false` clears the thread-store context and skips `/threads`; that is what keeps unlicensed thread drawers from fetching.
  * Mutations are optimistic in the core store. Delete rolls back if the request fails.
  * On a runtime without Intelligence, `renameThread`, `archiveThread`, `unarchiveThread`, and `deleteThread` reject with `Thread mutations are not available on this CopilotKit runtime`.
  * `fetchMoreError` is tracked separately so a failed "load more" request can show inline without losing the loaded list.
  * Threads are sorted by `lastRunAt`, then `updatedAt`, then `createdAt`.



How is this guide?

GoodBad

[Previous PageuseSuggestions](https://docs.copilotkit.ai/reference/vue/hooks/useSuggestions)[Next PageOverview](https://docs.copilotkit.ai/reference/angular)
