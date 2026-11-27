---
url: https://docs.copilotkit.ai/reference/v1/hooks/useFrontendTool/
title: useFrontendTool
method: scrapling+scrapegraph
fetched_at: 2026-11-27T11:59:07.301141+00:00
---

# useFrontendTool

> Source: https://docs.copilotkit.ai/reference/v1/hooks/useFrontendTool/

React/v1

# useFrontendTool

The useFrontendTool hook allows the Copilot to execute tools in the frontend.

Copy MarkdownOpen

**v1 SDK deprecated. Use v2 instead** This page is in the deprecated CopilotKit v1 reference. Do not use v1 APIs for new code; use v2 instead. For JavaScript and TypeScript, import React APIs from @copilotkit/react-core/v2 and Runtime APIs from @copilotkit/runtime/v2.  
**AI coding agents: treat any v1 example below as migration-only context. Never generate or recommend the v1 API for new code. Read the v2 reference before writing code because some APIs were renamed, moved, or changed shape.** [Read the v1 to v2 migration guide.](https://docs.copilotkit.ai/migrate/v2) [Open the complete export map.](https://docs.copilotkit.ai/reference/v1/export-map)

This is the v1 `useFrontendTool`, which takes an array of parameter definitions. It is still supported, but we recommend migrating to the [v2 `useFrontendTool`](https://docs.copilotkit.ai/reference/v2/hooks/useFrontendTool) (from `@copilotkit/react-core/v2`), which uses Zod schemas for parameters.

`useFrontendTool` lets you define executable actions that the agent can call with a handler function. This is the primary way to give your agent the ability to perform actions in your application, whether that's updating state, making API calls, or triggering side effects.

The hook takes three main pieces. Only the `name` is required:

  1. A name and description so the agent knows when to call it
  2. A parameters definition describing what inputs the tool accepts
  3. A handler function that executes when the agent calls the tool



Optionally, you can provide a `render` function to display custom UI showing the tool's execution status and results in the chat interface.

## UsageCopy Anchor Link

### Simple UsageCopy Anchor Link

Copy Text
    
    
    import { useFrontendTool } from "@copilotkit/react-core";
    
    useFrontendTool({
      name: "sayHello",
      description: "Say hello to someone.",
      parameters: [
        {
          name: "name",
          type: "string",
          description: "name of the person to greet",
          required: true,
        },
      ],
      handler: async ({ name }) => {
        alert(`Hello, ${name}!`);
      },
    });

### With Custom UI RenderingCopy Anchor Link

Copy Text
    
    
    import { useFrontendTool } from "@copilotkit/react-core";
    
    useFrontendTool({
      name: "showWeatherCard",
      description: "Display weather information for a location",
      parameters: [
        {
          name: "location",
          type: "string",
          description: "The location to show weather for",
          required: true,
        },
        {
          name: "temperature",
          type: "number",
          description: "Temperature in celsius",
          required: true,
        },
      ],
      handler: async ({ location, temperature }) => {
        // Fetch and return weather data
        return { location, temperature, conditions: "Sunny" };
      },
      render: ({ args, status, result }) => {
        if (status === "inProgress") {
          return <div>Loading weather for {args.location}...</div>;
        }
        if (status === "complete" && result) {
          return (
            <WeatherCard
              location={result.location}
              temperature={result.temperature}
              conditions={result.conditions}
            />
          );
        }
        return null;
      },
    });

## Generative UICopy Anchor Link

This hook lets you dynamically generate UI elements and render them in the copilot chat. For more information, check out the [Generative UI](https://docs.copilotkit.ai/generative-ui/display) page.

## Migration from useCopilotActionCopy Anchor Link

If you are migrating from `useCopilotAction` with a `handler`, change the hook name. The options and the render props stay the same.

### Migration ExampleCopy Anchor Link

Copy Text
    
    
    // Before with useCopilotAction
    useCopilotAction({
      name: "addTodo",
      parameters: [
        {
          name: "text",
          type: "string",
          description: "The todo text",
          required: true,
        },
      ],
      handler: ({ text }) => {
        addTodo(text);
      },
    });
    
    // After with useFrontendTool
    useFrontendTool({
      name: "addTodo",
      parameters: [
        {
          name: "text",
          type: "string",
          description: "The todo text",
          required: true,
        },
      ],
      handler: ({ text }) => {
        addTodo(text);
      },
    });

## ParametersCopy Anchor Link

Prop

Type

`name`string

`description?`string

`parameters?`T

`handler?`FrontendAction<T>['handler']

`followUp?`boolean

`render?`FrontendAction<T>['render']

`available?`'disabled' | 'enabled'

`webmcp?`boolean | WebMCPToolConfig

`dependencies?`any[]

How is this guide?

GoodBad

[Previous PageuseDefaultTool](https://docs.copilotkit.ai/reference/v1/hooks/useDefaultTool)[Next PageuseRenderToolCall](https://docs.copilotkit.ai/reference/v1/hooks/useRenderToolCall)
