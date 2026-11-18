---
url: https://docs.copilotkit.ai/angular/human-in-the-loop/headless/
title: Headless Interrupts
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:53.313390+00:00
---

# Headless Interrupts

> Source: https://docs.copilotkit.ai/angular/human-in-the-loop/headless/

Human-in-the-loop

# Headless Interrupts

Resolve a backend interrupt from any Angular component through the agent store's interrupt controller.

Copy MarkdownOpen

When the backend agent emits an AG-UI interrupt, the agent store already holds the pending decision. Read it and resume the run from any component. For the patterns side by side, see the [HITL Overview](https://docs.copilotkit.ai/angular/human-in-the-loop).

## Handle an interrupt from the storeCopy Anchor Link

An interrupt is a state of one conversation: this agent, this thread, this run is waiting for a decision. The store that already exposes that conversation's messages and state exposes its pending interrupt too, so a component that holds a store needs nothing else:

src/app/ticket-approval.component.ts

Copy Text
    
    
    import { Component } from "@angular/core";
    import { injectAgentStore } from "@copilotkit/angular";
    
    @Component({
      selector: "app-ticket-approval",
      template: `
        @let interrupts = store().interruptController;
    
        @if (interrupts.hasInterrupt()) {
          <section>
            <p>{{ interrupts.interrupt()?.message }}</p>
            <button type="button" (click)="interrupts.resolve({ approved: true })">
              Approve
            </button>
            <button type="button" (click)="interrupts.cancel()">Reject</button>
          </section>
        }
      `,
    })
    export class TicketApprovalComponent {
      protected readonly store = injectAgentStore("ticketing");
    }

The controller is created and connected with the store, then destroyed when the store is torn down or replaced. Standard AG-UI interrupts already retained by the agent are visible immediately, and legacy `on_interrupt` events are observed for the store's full lifetime.

## Next stepsCopy Anchor Link

  * [Pausing the Agent for Input](https://docs.copilotkit.ai/angular/human-in-the-loop/useInterrupt): a typed controller with filtering and a handler.
  * [injectAgentStore API](https://docs.copilotkit.ai/reference/angular/functions/injectAgentStore)



How is this guide?

GoodBad

[Previous PagePausing the Agent for Input](https://docs.copilotkit.ai/angular/human-in-the-loop/useInterrupt)[Next PageWebMCP](https://docs.copilotkit.ai/angular/webmcp)
