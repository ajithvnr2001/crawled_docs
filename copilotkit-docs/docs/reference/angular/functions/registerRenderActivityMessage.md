---
url: https://docs.copilotkit.ai/reference/angular/functions/registerRenderActivityMessage/
title: registerRenderActivityMessage
method: scrapling+scrapegraph
fetched_at: 2026-11-21T10:52:48.882891+00:00
---

# registerRenderActivityMessage

> Source: https://docs.copilotkit.ai/reference/angular/functions/registerRenderActivityMessage/

Angular/Functions

# registerRenderActivityMessage

Register a typed Angular renderer for AG-UI activity messages.

Copy MarkdownOpen

`registerRenderActivityMessage` registers a standalone component for one AG-UI activity type for the lifetime of the current injector.

Copy Text
    
    
    function registerRenderActivityMessage(
      config: RenderActivityMessageConfig,
    ): void;
    
    interface RenderActivityMessageConfig<TContent = unknown> {
      activityType: string;
      agentId?: string;
      content: AngularActivityContentSchema<TContent>;
      component: Type<ActivityRenderer<TContent>>;
    }

Copy Text
    
    
    import { Component, input } from "@angular/core";
    import type { AbstractAgent, ActivityMessage } from "@ag-ui/client";
    import {
      ActivityRenderer,
      registerRenderActivityMessage,
    } from "@copilotkit/angular";
    import { z } from "zod";
    
    const progressSchema = z.object({ label: z.string(), percent: z.number() });
    
    @Component({
      template: `<progress [value]="content().percent" max="100"></progress>`,
    })
    export class ProgressActivity implements ActivityRenderer<
      z.infer<typeof progressSchema>
    > {
      readonly activityType = input.required<string>();
      readonly content = input.required<z.infer<typeof progressSchema>>();
      readonly message = input.required<ActivityMessage>();
      readonly agent = input<AbstractAgent>();
    }
    
    @Component({ template: `` })
    export class ActivityRegistration {
      constructor() {
        registerRenderActivityMessage({
          activityType: "job-progress",
          content: progressSchema,
          component: ProgressActivity,
        });
      }
    }

  * Call it in an injection context. On destroy, it removes the exact registration.
  * Content must pass `safeParse` before the component renders.
  * `agentId` scopes a renderer to one agent.
  * Application registrations take precedence over CopilotKit built-ins such as A2UI, Open Generative UI, and MCP Apps.
  * Make renderer components standalone and OnPush- or zoneless-compatible.
  * Renderer components must guard their own browser-only work for SSR and hydration.



How is this guide?

GoodBad

[Previous PageregisterHumanInTheLoop](https://docs.copilotkit.ai/reference/angular/functions/registerHumanInTheLoop)[Next PageregisterRenderToolCall](https://docs.copilotkit.ai/reference/angular/functions/registerRenderToolCall)
