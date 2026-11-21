---
url: https://docs.copilotkit.ai/reference/angular/functions/registerRenderToolCall/
title: registerRenderToolCall
method: scrapling+scrapegraph
fetched_at: 2026-11-21T10:52:48.956384+00:00
---

# registerRenderToolCall

> Source: https://docs.copilotkit.ai/reference/angular/functions/registerRenderToolCall/

Angular/Functions

# registerRenderToolCall

Angular function for registering a renderer component for a tool call with CopilotKit, with access to streaming arguments, status, and result

Copy MarkdownOpen

## OverviewCopy Anchor Link

`registerRenderToolCall` registers a renderer for a tool call. It does not run a handler. It tells CopilotKit which standalone Angular component to render whenever a tool call with a matching `name` appears in the conversation. Use it to visualize tool calls that execute somewhere other than the browser, for example a server-side tool or an agentic (long-running) tool, where you only want to show progress and results in the chat.

You call `registerRenderToolCall` inside an Angular injection context (a component or service constructor, or a field initializer). The renderer registers immediately. When the owning injector is destroyed, CopilotKit removes tool and renderer registrations with the same name and optional agent id.

If you want to run a browser handler and render UI, use [`registerFrontendTool`](https://docs.copilotkit.ai/reference/angular/functions/registerFrontendTool) with its `component` field instead. If the agent does not already have the tool and you only want it to display one of your components, use [`registerComponent`](https://docs.copilotkit.ai/reference/angular/functions/registerComponent), which declares the tool from the frontend so nothing has to be added on the agent side. To wait for a user decision, use [`registerHumanInTheLoop`](https://docs.copilotkit.ai/reference/angular/functions/registerHumanInTheLoop).

Import from the package root, `@copilotkit/angular`. There is no `/v2` subpath. `registerRenderToolCall` must run in an injection context that has [`provideCopilotKit`](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotKit) in scope.

## SignatureCopy Anchor Link

Copy Text
    
    
    import { registerRenderToolCall } from "@copilotkit/angular";
    
    function registerRenderToolCall<Args extends Record<string, unknown>>(
      renderToolCall: RenderToolCallConfig<Args>,
    ): void;

## ParametersCopy Anchor Link

Prop

Type

`renderToolCall`RenderToolCallConfig<Args>

## Return ValueCopy Anchor Link

`registerRenderToolCall` returns `void`. It registers the renderer as a side effect and wires up name-and-agent-id cleanup for the owning injector. Frontend tools, human-in-the-loop tools, and renderer registrations sharing that key are removed together.

## The renderer componentCopy Anchor Link

Your `component` implements the `ToolRenderer<Args>` interface. CopilotKit binds the inputs by name, so declare them with Angular's `input()`:

Copy Text
    
    
    import { Signal } from "@angular/core";
    import { AbstractAgent } from "@ag-ui/client";
    
    interface ToolRenderer<Args extends Record<string, unknown>> {
      // Required: the current state of the tool call.
      toolCall: Signal<AngularToolCall<Args>>;
      // Bound only when the config sets passAgent: true.
      agent?: Signal<AbstractAgent | undefined>;
    }

### AngularToolCallCopy Anchor Link

`toolCall()` returns a discriminated union keyed on `status`. The shape of `args` and `result` depends on the status:

Copy Text
    
    
    type AngularToolCall<Args extends Record<string, unknown>> =
      | {
          name?: string;
          args: Partial<Args>; // streaming, may be incomplete
          status: "in-progress";
          result: undefined;
        }
      | {
          name?: string;
          args: Args; // fully parsed
          status: "executing";
          result: undefined;
        }
      | {
          name?: string;
          args: Args; // fully parsed
          status: "complete";
          result: string; // the tool result, as a string
        };

  * **`in-progress`** means the agent run is still active and the tool has no result yet. `args` is `Partial<Args>` because the arguments can still be streaming, and `result` is `undefined`.
  * **`executing`** means the run has stopped and the tool has no result yet, for example while a frontend tool's handler runs. `args` is the complete `Args` and `result` is still `undefined`. A server-side tool usually goes from `in-progress` straight to `complete`.
  * **`complete`** means the tool finished, so `args` is complete and `result` holds the string result.



## UsageCopy Anchor Link

### A renderer component for a server-side toolCopy Anchor Link

This renderer shows a spinner while the tool runs and then renders the result. It narrows on `status` so the template only reads `result` once it is available.

src/app/search-tool-view.component.ts

Copy Text
    
    
    import { Component, input } from "@angular/core";
    import { AngularToolCall, ToolRenderer } from "@copilotkit/angular";
    
    type SearchArgs = { query: string };
    
    @Component({
      selector: "app-search-tool-view",
      standalone: true,
      template: `
        @let call = toolCall();
        @switch (call.status) {
          @case ("in-progress") {
            <div class="text-sm opacity-70">Searching for "{{ call.args.query }}"...</div>
          }
          @case ("complete") {
            <pre class="rounded border p-3 text-sm">{{ call.result }}</pre>
          }
        }
      `,
    })
    export class SearchToolViewComponent implements ToolRenderer<SearchArgs> {
      readonly toolCall = input.required<AngularToolCall<SearchArgs>>();
    }

Register it for the tool name your agent emits:

src/app/chat.component.ts

Copy Text
    
    
    import { Component } from "@angular/core";
    import { z } from "zod";
    import { registerRenderToolCall } from "@copilotkit/angular";
    import { SearchToolViewComponent } from "./search-tool-view.component";
    
    @Component({
      selector: "app-chat",
      standalone: true,
      template: ``,
    })
    export class ChatComponent {
      constructor() {
        registerRenderToolCall({
          name: "searchDocuments",
          args: z.object({ query: z.string() }),
          component: SearchToolViewComponent,
        });
      }
    }

### Receiving the agent instanceCopy Anchor Link

Set `passAgent: true` to have CopilotKit bind the `agent` signal input as well. Declare it on the component as an optional `input()`.

src/app/handoff-tool-view.component.ts

Copy Text
    
    
    import { Component, input } from "@angular/core";
    import { AbstractAgent } from "@ag-ui/client";
    import { AngularToolCall, ToolRenderer } from "@copilotkit/angular";
    
    type HandoffArgs = { target: string };
    
    @Component({
      selector: "app-handoff-tool-view",
      standalone: true,
      template: `<div>Handing off to {{ toolCall().args.target }}</div>`,
    })
    export class HandoffToolViewComponent implements ToolRenderer<HandoffArgs> {
      readonly toolCall = input.required<AngularToolCall<HandoffArgs>>();
      readonly agent = input<AbstractAgent | undefined>();
    }

src/app/chat.component.ts

Copy Text
    
    
    registerRenderToolCall({
      name: "handoff",
      args: z.object({ target: z.string() }),
      component: HandoffToolViewComponent,
      passAgent: true,
    });

How is this guide?

GoodBad

[Previous PageregisterRenderActivityMessage](https://docs.copilotkit.ai/reference/angular/functions/registerRenderActivityMessage)[Next PageCopilotKit](https://docs.copilotkit.ai/reference/angular/services/CopilotKit)
