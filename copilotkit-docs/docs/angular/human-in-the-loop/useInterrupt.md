---
url: https://docs.copilotkit.ai/angular/human-in-the-loop/useInterrupt/
title: Pausing the Agent for Input
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:53.282128+00:00
---

# Pausing the Agent for Input

> Source: https://docs.copilotkit.ai/angular/human-in-the-loop/useInterrupt/

Human-in-the-loop

# Pausing the Agent for Input

Handle a backend interrupt in Angular with the typed injectInterrupt controller, then resume the run.

Copy MarkdownOpen

When the backend agent pauses for input, `injectInterrupt` gives you a typed controller for the pending decision. For the default controller on the agent store, see [Headless Interrupts](https://docs.copilotkit.ai/angular/human-in-the-loop/headless).

## Handle an interrupt with a typed controllerCopy Anchor Link

`injectInterrupt` subscribes to one agent and exposes the pending decision as signals. It supports standard AG-UI interrupts and the legacy `on_interrupt` custom event. Use it when the store default is not enough. For example, you need a typed payload, an `enabled` filter, or a `handler` that prepares data for the view.

Do not render an `injectInterrupt` controller and `store().interruptController` for the same decision. Both independently observe the agent, so the same interrupt becomes visible in both and two UI actions could attempt to resume it. Render only the specialized controller when you need filtering or typed handling.

src/app/interrupt-panel.component.ts

Copy Text
    
    
    import { Component } from "@angular/core";
    import { injectInterrupt } from "@copilotkit/angular";
    
    type ReviewRequest = {
      title?: string;
      choices?: Array<{ id: string; label: string }>;
    };
    
    @Component({
      selector: "app-interrupt-panel",
      template: `
        @if (controller.event(); as event) {
          @let request = asReviewRequest(event.value);
          <section aria-labelledby="review-title">
            <h2 id="review-title">{{ request.title ?? "Review required" }}</h2>
    
            @for (choice of request.choices ?? []; track choice.id) {
              <button type="button" (click)="resolve(choice.id)">
                {{ choice.label }}
              </button>
            }
    
            <button type="button" (click)="cancel()">Cancel</button>
          </section>
        }
    
        @if (controller.error()) {
          <p role="alert">The decision could not be submitted.</p>
        }
      `,
    })
    export class InterruptPanelComponent {
      protected readonly controller =
        injectInterrupt<ReviewRequest>("default");
    
      protected asReviewRequest(value: unknown): ReviewRequest {
        return typeof value === "object" && value !== null
          ? (value as ReviewRequest)
          : {};
      }
    
      protected resolve(choiceId: string): void {
        this.controller.resolve({ choiceId }).catch(() => undefined);
      }
    
      protected cancel(): void {
        this.controller.cancel().catch(() => undefined);
      }
    }

The controller clears stale decisions when the thread changes. Calls to `resolve` or `cancel` share one in-flight resume promise, so a double click does not start two resume runs.

Use the controller's `enabled` option when several components listen to the same agent and each should accept only certain interrupt payloads. Use `handler` when the view needs async data prepared before it appears.

## Next stepsCopy Anchor Link

  * [injectInterrupt API](https://docs.copilotkit.ai/reference/angular/functions/injectInterrupt)
  * [HITL Overview](https://docs.copilotkit.ai/angular/human-in-the-loop)



How is this guide?

GoodBad

[Previous PageHITL Overview](https://docs.copilotkit.ai/angular/human-in-the-loop)[Next PageHeadless Interrupts](https://docs.copilotkit.ai/angular/human-in-the-loop/headless)
