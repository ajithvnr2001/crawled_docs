---
url: https://docs.copilotkit.ai/angular/headless-threads/
title: Headless Threads
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:53.198498+00:00
---

# Headless Threads

> Source: https://docs.copilotkit.ai/angular/headless-threads/

Threads

# Headless Threads

Reopen saved conversations and build your own Angular thread list with injectThreads.

Copy MarkdownOpen

Reopen a saved conversation, or build your own thread list with Angular signals. For a ready-made list, use the [Threads Drawer](https://docs.copilotkit.ai/angular/prebuilt-components/copilot-threads-drawer).

## Resume a specific threadCopy Anchor Link

Pass `threadId` to connect the chat to an existing conversation:

Copy Text
    
    
    <copilot-chat agentId="support" [threadId]="selectedThreadId()" />

For a custom thread list, use `injectThreads`. Its inputs accept plain values or signals.

src/app/thread-list.component.ts

Copy Text
    
    
    import { Component } from "@angular/core";
    import { injectThreads } from "@copilotkit/angular";
    
    @Component({
      selector: "app-thread-list",
      template: `
        <button type="button" (click)="threads.startNewThread()">
          New conversation
        </button>
    
        @if (threads.isLoading()) {
          <p>Loading conversations…</p>
        } @else {
          @for (thread of threads.threads(); track thread.id) {
            <button type="button" (click)="select(thread.id)">
              {{ thread.name ?? "Untitled conversation" }}
            </button>
          }
        }
    
        @if (threads.listError()) {
          <button type="button" (click)="threads.refetchThreads()">Retry</button>
        }
      `,
    })
    export class ThreadListComponent {
      readonly threads = injectThreads({
        agentId: "support",
        limit: 20,
      });
    
      protected select(threadId: string): void {
        // Store this id and bind it to CopilotChat's threadId input.
        console.log(threadId);
      }
    }

The list is server-authoritative and uses realtime updates when the platform supplies a WebSocket URL. Rename, archive, unarchive, and delete return promises. Deletion is permanent; ask the user before calling `deleteThread`.

## Next stepsCopy Anchor Link

  * [injectThreads API](https://docs.copilotkit.ai/reference/angular/functions/injectThreads)
  * [Threads Drawer](https://docs.copilotkit.ai/angular/prebuilt-components/copilot-threads-drawer)



How is this guide?

GoodBad

[Previous PageThreads Drawer](https://docs.copilotkit.ai/angular/prebuilt-components/copilot-threads-drawer)[Next PageFrontend Tools](https://docs.copilotkit.ai/angular/frontend-tools)
