---
url: https://docs.copilotkit.ai/angular/generative-ui/tool-rendering/
title: Tool Call Rendering
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:53.058618+00:00
---

# Tool Call Rendering

> Source: https://docs.copilotkit.ai/angular/generative-ui/tool-rendering/

Controlled

# Tool Call Rendering

Render a frontend or backend tool call in Angular chat with a standalone component.

Copy MarkdownOpen

## Render a tool resultCopy Anchor Link

A renderer is a standalone component with a required `toolCall` signal input. Its status moves through `"in-progress"`, `"executing"`, and `"complete"`.

src/app/weather-card.component.ts

Copy Text
    
    
    import { Component, input } from "@angular/core";
    import {
      type AngularToolCall,
      type ToolRenderer,
    } from "@copilotkit/angular";
    
    type WeatherArgs = { city: string };
    
    @Component({
      selector: "app-weather-card",
      template: `
        @let call = toolCall();
        @if (call.status === "complete") {
          <article>
            <strong>{{ call.args.city }}</strong>
            <p>{{ call.result }}</p>
          </article>
        } @else {
          <p>Loading weather for {{ call.args.city ?? "…" }}</p>
        }
      `,
    })
    export class WeatherCardComponent implements ToolRenderer<WeatherArgs> {
      readonly toolCall = input.required<AngularToolCall<WeatherArgs>>();
    }

Pass the class as `component` when the tool runs in the browser:

Copy Text
    
    
    registerFrontendTool({
      name: "getWeather",
      description: "Get the current weather for a city",
      parameters: z.object({ city: z.string() }),
      component: WeatherCardComponent,
      handler: async ({ city }, { signal }) => {
        const response = await fetch(`/api/weather?city=${encodeURIComponent(city)}`, {
          signal,
        });
        return response.text();
      },
    });

Use `registerRenderToolCall` instead when the tool runs on the server and the browser only renders its call:

Copy Text
    
    
    registerRenderToolCall({
      name: "getWeather",
      args: z.object({ city: z.string() }),
      component: WeatherCardComponent,
    });

Ask the agent for the weather in Paris. The weather card shows "Loading weather for Paris", then the city and the tool result.

## Next stepsCopy Anchor Link

  * [registerFrontendTool API](https://docs.copilotkit.ai/reference/angular/functions/registerFrontendTool)
  * [registerRenderToolCall API](https://docs.copilotkit.ai/reference/angular/functions/registerRenderToolCall)
  * [Frontend Tools](https://docs.copilotkit.ai/angular/frontend-tools)
  * [Other generative UI paths](https://docs.copilotkit.ai/angular/generative-ui)



How is this guide?

GoodBad

[Previous PageComponents as Tools](https://docs.copilotkit.ai/angular/generative-ui/tool-based)[Next PageA2UI](https://docs.copilotkit.ai/angular/generative-ui/a2ui)
