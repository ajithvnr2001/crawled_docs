---
url: https://docs.copilotkit.ai/angular/generative-ui/tool-based/
title: Components as Tools
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:53.123486+00:00
---

# Components as Tools

> Source: https://docs.copilotkit.ai/angular/generative-ui/tool-based/

Controlled

# Components as Tools

Register a standalone Angular component as a tool the agent calls to show it in chat.

Copy MarkdownOpen

## Let the agent display one of your componentsCopy Anchor Link

`registerComponent` is the simplest generative UI, and you do not change your agent for it. It registers a standalone component as a tool the agent can call to show it. The agent decides when, and fills the props.

src/app/incident-card.component.ts

Copy Text
    
    
    import { Component, input } from "@angular/core";
    import { AngularToolCall, ToolRenderer } from "@copilotkit/angular";
    
    type IncidentArgs = { id: string; severity: string };
    
    @Component({
      selector: "app-incident-card",
      standalone: true,
      template: `
        @let call = toolCall();
        @if (call.status === "in-progress") {
          <p>Loading incident…</p>
        } @else {
          <article>
            <strong>{{ call.args.id }}</strong>
            <span>{{ call.args.severity }}</span>
          </article>
        }
      `,
    })
    export class IncidentCardComponent implements ToolRenderer<IncidentArgs> {
      readonly toolCall = input.required<AngularToolCall<IncidentArgs>>();
    }

Copy Text
    
    
    registerComponent({
      name: "show_incident",
      description: "Show one incident from the incident table.",
      parameters: z.object({
        id: z.string().describe("The incident id, such as INC-4711"),
        severity: z.string().describe("One of sev1, sev2, sev3"),
      }),
      component: IncidentCardComponent,
    });

There is no `handler`, and nothing changes in your agent. The tool is declared by the frontend and forwarded over AG-UI, so this works the same behind a Python agent as a TypeScript one.

A well-formed component is not a correct one

The model fills these props from what it knows. A card rendered over records your application does not hold looks the same in the browser, in a screenshot, and in a video as a correct one. Share the page's data with the agent using [`CopilotKitAgentContext`](https://docs.copilotkit.ai/reference/angular/directives/CopilotKitAgentContext), then read the rendered fields against the records you hold.

## Next stepsCopy Anchor Link

  * [registerComponent API](https://docs.copilotkit.ai/reference/angular/functions/registerComponent)
  * [Other generative UI paths](https://docs.copilotkit.ai/angular/generative-ui)



How is this guide?

GoodBad

[Previous PageOverview](https://docs.copilotkit.ai/angular/generative-ui)[Next PageTool Call Rendering](https://docs.copilotkit.ai/angular/generative-ui/tool-rendering)
