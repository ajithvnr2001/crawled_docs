---
url: https://docs.copilotkit.ai/angular/shared-state/agent-readonly/
title: Agent Read-Only Context
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:53.590308+00:00
---

# Agent Read-Only Context

> Source: https://docs.copilotkit.ai/angular/shared-state/agent-readonly/

Shared state

# Agent Read-Only Context

Send application-owned values to the agent with connectAgentContext or CopilotKitAgentContext.

Copy MarkdownOpen

Use agent context when the application owns a value and the agent only reads it. For values that the agent and application both change, use [Shared State](https://docs.copilotkit.ai/angular/shared-state).

## Send read-only application contextCopy Anchor Link

Use `connectAgentContext` for values such as the signed-in user's name, selected record, timezone, or current screen. Pass an accessor so signal reads stay reactive.

src/app/account-context.component.ts

Copy Text
    
    
    import { Component, signal } from "@angular/core";
    import { connectAgentContext } from "@copilotkit/angular";
    
    @Component({
      selector: "app-account-context",
      template: `
        <button type="button" (click)="timezone.set('Europe/London')">
          Use London time
        </button>
      `,
    })
    export class AccountContextComponent {
      readonly userName = signal("Ada");
      readonly timezone = signal("America/Los_Angeles");
    
      constructor() {
        connectAgentContext(() => ({
          description: "Current account and timezone",
          value: JSON.stringify({
            userName: this.userName(),
            timezone: this.timezone(),
          }),
        }));
      }
    }

The internal effect removes the old context and registers the new value when a read signal changes. It removes the final registration when the owning injector is destroyed. If you already have an `Injector`, pass it as `{ injector }`; that injector takes precedence over the ambient one.

## Bind context in a templateCopy Anchor Link

Use `CopilotKitAgentContext` when the context is already shaped in the template.

src/app/selection-context.component.ts

Copy Text
    
    
    import { Component, computed, signal } from "@angular/core";
    import { CopilotKitAgentContext } from "@copilotkit/angular";
    
    @Component({
      selector: "app-selection-context",
      imports: [CopilotKitAgentContext],
      template: `
        <div [copilotkitAgentContext]="selectionContext()"></div>
      `,
    })
    export class SelectionContextComponent {
      readonly selectedId = signal("record-42");
      readonly selectionContext = computed(() => ({
        description: "The record selected in the application",
        value: this.selectedId(),
      }));
    }

Render the directive only after you have a complete context. If it starts without one, later input changes do not create the first registration.

## Next stepsCopy Anchor Link

  * [connectAgentContext API](https://docs.copilotkit.ai/reference/angular/functions/connectAgentContext)
  * [CopilotKitAgentContext API](https://docs.copilotkit.ai/reference/angular/directives/CopilotKitAgentContext)
  * [Shared State](https://docs.copilotkit.ai/angular/shared-state)



How is this guide?

GoodBad

[Previous PageShared State](https://docs.copilotkit.ai/angular/shared-state)[Next PageHITL Overview](https://docs.copilotkit.ai/angular/human-in-the-loop)
