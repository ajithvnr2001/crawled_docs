---
url: https://docs.copilotkit.ai/angular/generative-ui/a2ui/
title: A2UI
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:53.020603+00:00
---

# A2UI

> Source: https://docs.copilotkit.ai/angular/generative-ui/a2ui/

Declarative

# A2UI

Configure typed A2UI catalogs, Angular-owned styles, and incomplete-stream recovery.

Copy MarkdownOpen

When your agent builds UI on the fly, you want it to use only components you approve. A2UI renders the agent's UI in Angular chat from a catalog that you define. The renderer creates only components that the catalog defines.

## Choose a schema strategyCopy Anchor Link

Catalog component definitions use Zod schemas for their props. A broad catalog lets the agent compose several application primitives. A fixed catalog narrows the generated interface to a specific domain and set of shapes.

The flight example keeps its component vocabulary deliberately small:

a2ui-definitions.ts

Copy Text
    
    
    export const fixedDefinitions = {
      Card: { props: z.object({ child: z.string() }) },
      Title: { props: z.object({ text: dynamicString }) },
      Airport: { props: z.object({ code: dynamicString }) },
      Arrow: { props: z.object({}) },
      AirlineBadge: { props: z.object({ name: dynamicString }) },
      PriceTag: { props: z.object({ amount: dynamicString }) },
      Button: {
        props: z.object({
          child: z.string(),
          variant: z.enum(["primary", "secondary", "ghost"]).optional(),
          action: z.unknown().optional(),
        }),
      },
    } satisfies A2UICatalogDefinitions;

Give each catalog a stable `catalogId`. In an application config, pass the chosen catalog and lifecycle policy through the `a2ui` option of `provideCopilotKit`:

src/app/app.config.ts

Copy Text
    
    
    provideCopilotKit({
      runtimeUrl: "/api/copilotkit",
      a2ui: {
        catalog: productCatalog,
        recovery: { showAfterMs: 2_000, showAfterAttempts: 2 },
      },
    });

A catalog is required: without one, A2UI stays off even when the runtime enables it, and CopilotKit logs a warning.

### Use existing web componentsCopy Anchor Link

A catalog entry can also be a Custom Element, such as a component from an existing design system. Pass `{ tagName, element }` instead of an Angular component, and mix both kinds freely:

src/app/a2ui-catalog.ts

Copy Text
    
    
    import { ChildListSchema, createAngularCatalog } from "@copilotkit/angular/a2ui";
    import { z } from "zod";
    
    const catalog = createAngularCatalog(
      {
        Badge: { props: z.object({ label: z.string() }) },
        Panel: { props: z.object({ children: ChildListSchema }) },
      },
      {
        Badge: { tagName: "acme-badge", element: AcmeBadge },
        Panel: PanelComponent,
      },
      { includeBasicCatalog: true },
    );

CopilotKit registers the element, renders it in place of the node, and assigns the node's A2UI `ComponentContext` to its `context` property on every update. The element reads its props and writes to the data model through that context, for example with web_core's `GenericBinder`. Elements render in the browser only, not during server rendering.

By default, CopilotKit includes the catalog schema in agent context. Set `includeSchema: false` only when the server already supplies equivalent schema and generation instructions. Otherwise the agent cannot reliably know which components and props are valid. With `includeSchema: false`, the agent context lists only the catalog ID and the custom component names. A LangGraph A2UI subagent then gets only the component names. To give it more, pass a composition guide through the A2UI guidelines of the CopilotKit middleware.

## Style rendered componentsCopy Anchor Link

Catalog components are Angular components with application-owned class names. Style those classes in the global stylesheet so generated surfaces and their nested elements receive the same rules:

styles.css

Copy Text
    
    
    .a2ui-row {
      display: flex;
      flex-wrap: wrap;
      align-items: stretch;
      width: 100%;
    }
    
    .a2ui-column {
      display: flex;
      flex-direction: column;
      width: 100%;
    }
    
    [data-testid="declarative-card"],
    .a2ui-chart-card,
    .a2ui-flight-card {
      display: block;
      padding: 1rem;
      border: 1px solid var(--line);
      border-radius: 0.9rem;
      background: light-dark(white, #191a1e);
      box-shadow: 0 8px 22px -18px rgb(15 23 42 / 0.4);
    }
    
    .a2ui-metric {
      display: grid;
      min-width: 8rem;
      gap: 0.25rem;
    }
    
    .a2ui-metric > span,
    .a2ui-metric > small {
      color: light-dark(var(--muted), #adadb2);
      font-size: 0.75rem;
    }
    
    .a2ui-metric > strong {
      font-size: 1.4rem;
    }
    
    .a2ui-status,
    .a2ui-airline {
      display: inline-flex;
      width: fit-content;
      padding: 0.25rem 0.55rem;
      border-radius: 999px;
      background: light-dark(#eef2ff, rgb(30 27 75 / 40%));
      font-size: 0.75rem;
      font-weight: 700;
    }
    
    .a2ui-status-success {
      background: light-dark(#dcfce7, rgb(5 46 22 / 40%));
      color: light-dark(#166534, #86efac);
    }
    .a2ui-status-warning {
      background: light-dark(#fef3c7, rgb(69 26 3 / 40%));
      color: light-dark(#92400e, #fcd34d);
    }
    .a2ui-status-error {
      background: light-dark(#fee2e2, rgb(69 10 10 / 40%));
      color: light-dark(#991b1b, #fca5a5);
    }

Keep semantic state in explicit classes such as `a2ui-status-success` rather than asking the model to invent colors. You can also pass an A2UI `theme` through `provideCopilotKit` for renderer-level theme values; catalog CSS remains the right place for product-specific layout and visual states.

## Recover incomplete streamsCopy Anchor Link

An interrupted stream can leave an A2UI surface without a terminal lifecycle event. Configure `recovery.showAfterMs` to avoid flashing recovery UI during a normal pause and `recovery.showAfterAttempts` to wait through transient retry attempts. The provider sample above uses two seconds and two attempts.

Use `recovery.debugExposure` only when users should see protocol diagnostics. Keep it hidden in consumer-facing chat, or choose a collapsed or verbose mode for internal debugging. Recovery thresholds affect client display; the server still owns activity lifecycle status and retry behavior.

## Angular support boundariesCopy Anchor Link

  * **Hashbrown is unsupported.** The stable Hashbrown Angular package does not support the Angular 22 policy. Use A2UI with a typed catalog instead.
  * **JSON Renderer is not applicable.** JSON Renderer does not provide an Angular renderer; use A2UI for declarative Angular interfaces.



## Check the resultCopy Anchor Link

Ask the agent to show your data with one of your catalog components. The chat renders that component from your catalog.

## Next stepsCopy Anchor Link

  * [Other generative UI paths](https://docs.copilotkit.ai/angular/generative-ui)



How is this guide?

GoodBad

[Previous PageTool Call Rendering](https://docs.copilotkit.ai/angular/generative-ui/tool-rendering)[Next PageMCP Apps](https://docs.copilotkit.ai/angular/generative-ui/mcp-apps)
