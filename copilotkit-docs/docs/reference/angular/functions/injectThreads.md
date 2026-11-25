---
url: https://docs.copilotkit.ai/reference/angular/functions/injectThreads/
title: injectThreads
method: scrapling+scrapegraph
fetched_at: 2026-11-25T12:31:16.423593+00:00
---

# injectThreads

> Source: https://docs.copilotkit.ai/reference/angular/functions/injectThreads/

Angular/Functions

# injectThreads

Angular function for listing and managing CopilotKit Intelligence threads with signals, pagination, realtime updates, and injector-scoped cleanup.

Copy MarkdownOpen

## OverviewCopy Anchor Link

`injectThreads` returns the thread list and mutations for one agent as Angular signals and stable callbacks. It fetches the runtime-authenticated user's threads from CopilotKit Intelligence, keeps metadata current through realtime updates when available, and sorts the list by most recent agent activity.

Call it from an Angular injection context such as a component field initializer or constructor. The list subscription, realtime connection, and core store registration are removed automatically when the owning injector is destroyed.

For a full walkthrough, see the [Angular Headless Threads guide](https://docs.copilotkit.ai/angular/headless-threads).

## SignatureCopy Anchor Link

Copy Text
    
    
    import { injectThreads } from "@copilotkit/angular";
    
    function injectThreads(input: InjectThreadsInput): InjectThreadsResult;

## InputCopy Anchor Link

Prop

Type

`agentId`string | Signal<string>

`includeArchived?`boolean | Signal<boolean | undefined>

`limit?`number | Signal<number | undefined>

`enabled?`boolean | Signal<boolean | undefined>

## Return valueCopy Anchor Link

The returned `InjectThreadsResult` contains:

Member| Type| Purpose  
---|---|---  
`threads`| `Signal<Thread[]>`| Server-authoritative list, sorted by most recent agent activity  
`isLoading`| `Signal<boolean>`| Initial-list loading state  
`listError`| `Signal<Error | null>`| User-safe list or mutation error  
`error`| `Signal<Error | null>`| Most recent error, including developer configuration errors  
`fetchMoreError`| `Signal<Error | null>`| Error from the most recent next-page request  
`hasMoreThreads`| `Signal<boolean>`| Whether another page is available  
`isFetchingMoreThreads`| `Signal<boolean>`| Whether the next page is loading  
`isMutating`| `Signal<boolean>`| Whether a rename, archive, restore, or delete is in flight  
`fetchMoreThreads()`| `() => void`| Fetch the next page when one exists  
`refetchThreads()`| `() => void`| Refresh without clearing the visible list  
`startNewThread()`| `() => void`| Reset to a fresh client-side thread; persistence starts with its first run  
`renameThread(id, name)`| `Promise<void>`| Rename a thread  
`archiveThread(id)`| `Promise<void>`| Hide a thread through a reversible archive  
`unarchiveThread(id)`| `Promise<void>`| Restore an archived thread  
`deleteThread(id)`| `Promise<void>`| Permanently delete a thread  
  
Each `Thread` has `id`, `agentId`, `name`, `archived`, `createdAt`, `updatedAt`, and an optional `lastRunAt`. Prefer `lastRunAt` for user-facing activity timestamps because metadata-only changes can update `updatedAt`.

## UsageCopy Anchor Link

src/app/thread-list.component.ts

Copy Text
    
    
    import { Component, signal } from "@angular/core";
    import { injectThreads } from "@copilotkit/angular";
    
    @Component({
      selector: "app-thread-list",
      standalone: true,
      template: `
        <button type="button" (click)="threads.startNewThread()">
          New conversation
        </button>
    
        @if (threads.isLoading()) {
          <p>Loading conversations…</p>
        } @else {
          @for (thread of threads.threads(); track thread.id) {
            <button type="button" (click)="selectedThreadId.set(thread.id)">
              {{ thread.name ?? "Untitled conversation" }}
            </button>
          }
        }
    
        @if (threads.listError()) {
          <p>Conversations could not be loaded.</p>
          <button type="button" (click)="threads.refetchThreads()">Retry</button>
        }
    
        @if (threads.hasMoreThreads()) {
          <button
            type="button"
            [disabled]="threads.isFetchingMoreThreads()"
            (click)="threads.fetchMoreThreads()"
          >
            Load more
          </button>
        }
      `,
    })
    export class ThreadListComponent {
      readonly selectedThreadId = signal<string | undefined>(undefined);
      readonly threads = injectThreads({
        agentId: "support",
        limit: 20,
      });
    }

Bind the selected id to a [`CopilotChat`](https://docs.copilotkit.ai/reference/angular/components/CopilotChat) component in the same feature:

Copy Text
    
    
    <copilot-chat agentId="support" [threadId]="selectedThreadId()" />

## Mutation behaviorCopy Anchor Link

Rename, archive, unarchive, and delete update the visible list optimistically and return a promise that settles when the platform confirms the operation. Handle rejection in the calling UI. Deletion is irreversible and rolls back its optimistic removal if the request fails; ask the user for confirmation before calling it.

Use `listError` for end-user messaging. The broader `error` signal can include configuration details such as a missing runtime URL or unavailable thread endpoints and is intended for developer diagnostics.

How is this guide?

GoodBad

[Previous PageinjectInterrupt](https://docs.copilotkit.ai/reference/angular/functions/injectInterrupt)[Next PageprovideCopilotChatLabels](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotChatLabels)
