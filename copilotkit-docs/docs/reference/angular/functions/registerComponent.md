---
url: https://docs.copilotkit.ai/reference/angular/functions/registerComponent/
title: registerComponent
method: scrapling+scrapegraph
fetched_at: 2026-11-28T11:35:17.428764+00:00
---

# registerComponent

> Source: https://docs.copilotkit.ai/reference/angular/functions/registerComponent/

Angular/Functions

# registerComponent

Angular function for registering a standalone component the agent can call as a tool to display it in the chat, with no handler and nothing to add on the agent side

Copy MarkdownOpen

## OverviewCopy Anchor Link

`registerComponent` registers a standalone Angular component as a tool the agent can call to display it. When the agent calls the tool, CopilotKit renders your component in the chat with the tool call's arguments. There is no handler, no user interaction, and no server-side execution: the agent decides when to show the component and populates its data. For a component that waits for the user, use [`registerHumanInTheLoop`](https://docs.copilotkit.ai/reference/angular/functions/registerHumanInTheLoop).

It needs nothing on the agent side. The tool is declared by the frontend and forwarded to the agent over AG-UI, so it behaves the same behind a Python agent as a TypeScript one. Contrast [`registerRenderToolCall`](https://docs.copilotkit.ai/reference/angular/functions/registerRenderToolCall), which draws a tool the agent already has and therefore requires that tool to exist in the agent.

You call `registerComponent` inside an Angular injection context (a component or service constructor, or a field initializer). The registration happens immediately and is removed when the owning injector is destroyed.

`registerComponent` is the Angular counterpart of `useComponent` in `@copilotkit/react-core/v2` and `@copilotkit/vue/v2`. It builds the same model-facing tool description, so the tool reads identically to the model whichever frontend registered the component.

Import from the package root, `@copilotkit/angular`. There is no `/v2` subpath. `registerComponent` must run in an injection context that has [`provideCopilotKit`](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotKit) in scope.

## SignatureCopy Anchor Link

Copy Text
    
    
    import { registerComponent } from "@copilotkit/angular";
    
    function registerComponent<Args extends Record<string, unknown>>(
      config: RegisterComponentConfig<Args>,
    ): void;

## ParametersCopy Anchor Link

Prop

Type

`config`RegisterComponentConfig<Args>

There is no `handler` field. A display-only component runs no application code, and CopilotKit completes the agent's turn with an empty tool result rather than an invented one. If you want to run browser code as well as render, use [`registerFrontendTool`](https://docs.copilotkit.ai/reference/angular/functions/registerFrontendTool) with both `handler` and `component`.

## Return ValueCopy Anchor Link

`registerComponent` returns `void`. It registers the tool and its renderer as a side effect, and removes both when the owning injector is destroyed.

## The componentCopy Anchor Link

Your `component` implements the `ToolRenderer<Args>` interface, the same contract every other Angular renderer uses. Declare the `toolCall` input with Angular's `input.required()` and read `toolCall().args`:

Copy Text
    
    
    import { Signal } from "@angular/core";
    
    interface ToolRenderer<Args extends Record<string, unknown>> {
      toolCall: Signal<AngularToolCall<Args>>;
    }

`toolCall()` is a discriminated union keyed on `status`. While the model is still streaming the payload the status is `in-progress` and `args` is `Partial<Args>`, so narrow on `status` before reading a field you require. See [`registerRenderToolCall`](https://docs.copilotkit.ai/reference/angular/functions/registerRenderToolCall#angulartoolcall) for the full union.

## UsageCopy Anchor Link

### Display a card the agent fills inCopy Anchor Link

src/app/incident-card.component.ts

Copy Text
    
    
    import { Component, input } from "@angular/core";
    import { AngularToolCall, ToolRenderer } from "@copilotkit/angular";
    
    type IncidentArgs = { id: string; severity: string; summary: string };
    
    @Component({
      selector: "app-incident-card",
      standalone: true,
      template: `
        @let call = toolCall();
        @if (call.status === "in-progress") {
          <div class="text-sm opacity-70">Loading incident…</div>
        } @else {
          <article class="rounded-lg border p-4">
            <header class="flex items-baseline justify-between">
              <strong>{{ call.args.id }}</strong>
              <span class="text-xs uppercase">{{ call.args.severity }}</span>
            </header>
            <p class="text-sm">{{ call.args.summary }}</p>
          </article>
        }
      `,
    })
    export class IncidentCardComponent implements ToolRenderer<IncidentArgs> {
      readonly toolCall = input.required<AngularToolCall<IncidentArgs>>();
    }

Register it once, anywhere under `provideCopilotKit`:

src/app/chat.component.ts

Copy Text
    
    
    import { Component } from "@angular/core";
    import { z } from "zod";
    import { registerComponent } from "@copilotkit/angular";
    import { IncidentCardComponent } from "./incident-card.component";
    
    @Component({
      selector: "app-chat",
      standalone: true,
      template: ``,
    })
    export class ChatComponent {
      constructor() {
        registerComponent({
          name: "show_incident",
          description: "Show one incident from the incident table.",
          parameters: z.object({
            id: z.string().describe("The incident id, such as INC-4711"),
            severity: z.string().describe("One of sev1, sev2, sev3"),
            summary: z.string().describe("One sentence on what happened"),
          }),
          component: IncidentCardComponent,
        });
      }
    }

Nothing is added to the agent. The tool reaches it in the run's tool list, and the agent calls it by name.

### Scoping to one agentCopy Anchor Link

Copy Text
    
    
    registerComponent({
      name: "show_incident",
      parameters: incidentSchema,
      component: IncidentCardComponent,
      agentId: "support-agent",
    });

## Grounding the component in your own dataCopy Anchor Link

The agent fills the component's arguments. If your data never reached the agent, the agent invents the values, and the component still looks correct.

Registering the component is the rendering half. Give the agent the data it should describe with [`CopilotKitAgentContext`](https://docs.copilotkit.ai/reference/angular/directives/CopilotKitAgentContext) or [`connectAgentContext`](https://docs.copilotkit.ai/reference/angular/functions/connectAgentContext), then check the rendered fields against the records your application holds.

How is this guide?

GoodBad

[Previous PageprovideMCPApps](https://docs.copilotkit.ai/reference/angular/functions/provideMCPApps)[Next PageregisterFrontendTool](https://docs.copilotkit.ai/reference/angular/functions/registerFrontendTool)
