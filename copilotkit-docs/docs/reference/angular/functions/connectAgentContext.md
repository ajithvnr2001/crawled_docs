---
url: https://docs.copilotkit.ai/reference/angular/functions/connectAgentContext/
title: connectAgentContext
method: scrapling+scrapegraph
fetched_at: 2026-11-25T12:31:17.481005+00:00
---

# connectAgentContext

> Source: https://docs.copilotkit.ai/reference/angular/functions/connectAgentContext/

Angular/Functions

# connectAgentContext

Angular function that adds reactive context for the agent and cleans it up automatically for @copilotkit/angular.

Copy MarkdownOpen

## OverviewCopy Anchor Link

`connectAgentContext` registers [context](https://docs.ag-ui.com/concepts/context) with the agent so it can read your application state. It accepts a static `Context` object or a zero-argument accessor. The internal Angular `effect` tracks any signals read by the accessor and updates the context when they change.

The registration is wrapped in an Angular `effect`, so the context is cleaned up automatically when the owning component or service is destroyed.

For a template-driven alternative, use the [`CopilotKitAgentContext`](https://docs.copilotkit.ai/reference/angular/directives/CopilotKitAgentContext) directive.

Call this from an Angular injection context, such as a constructor or field initializer. To call it from other code, pass `{ injector }` as the second argument.

## SignatureCopy Anchor Link

Copy Text
    
    
    import { connectAgentContext } from "@copilotkit/angular";
    import type { Injector } from "@angular/core";
    import type { Context } from "@ag-ui/client";
    
    interface ConnectAgentContextConfig {
      injector?: Injector;
    }
    
    function connectAgentContext(
      context: Context | (() => Context),
      config?: ConnectAgentContextConfig,
    ): void;

## ParametersCopy Anchor Link

Prop

Type

`context`Context | (() => Context)

`config?`ConnectAgentContextConfig

## UsageCopy Anchor Link

### Static contextCopy Anchor Link

src/app/preferences.component.ts

Copy Text
    
    
    import { Component } from "@angular/core";
    import { connectAgentContext } from "@copilotkit/angular";
    
    @Component({
      selector: "app-preferences",
      standalone: true,
      template: `<!-- ... -->`,
    })
    export class PreferencesComponent {
      constructor() {
        connectAgentContext({
          description: "User preferences",
          value: JSON.stringify({ theme: "dark", locale: "en-US" }),
        });
      }
    }

### Reactive context with an accessorCopy Anchor Link

Pass an accessor that reads signals so the agent always sees the current value.

src/app/cart.component.ts

Copy Text
    
    
    import { Component, signal } from "@angular/core";
    import { connectAgentContext } from "@copilotkit/angular";
    
    @Component({
      selector: "app-cart",
      standalone: true,
      template: `<button (click)="add()">Add item</button>`,
    })
    export class CartComponent {
      readonly items = signal<string[]>([]);
    
      constructor() {
        // Re-registers with the agent whenever the cart changes.
        connectAgentContext(() => ({
          description: "Current shopping cart",
          value: JSON.stringify(this.items()),
        }));
      }
    
      add() {
        this.items.update((items) => [...items, "Item"]);
      }
    }

## BehaviorCopy Anchor Link

  * **Reactive updates.** When an accessor reads signals, the context is removed and re-added whenever one of those signals changes.
  * **Automatic cleanup.** Registration runs inside an Angular `effect`; the context is removed when the effect is torn down, which happens when the owning component, service, or injector is destroyed.
  * **Injection context.** Without `config.injector`, Angular throws `NG0203` when you call the function outside an injection context.



How is this guide?

GoodBad

[Previous PageCopilotKitAgentContext](https://docs.copilotkit.ai/reference/angular/directives/CopilotKitAgentContext)[Next PageinjectAgentStore](https://docs.copilotkit.ai/reference/angular/functions/injectAgentStore)
