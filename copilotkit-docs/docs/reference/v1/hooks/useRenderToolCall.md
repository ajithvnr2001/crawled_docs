---
url: https://docs.copilotkit.ai/reference/v1/hooks/useRenderToolCall/
title: useRenderToolCall
method: scrapling+scrapegraph
fetched_at: 2026-11-20T11:16:26.716250+00:00
---

# useRenderToolCall

> Source: https://docs.copilotkit.ai/reference/v1/hooks/useRenderToolCall/

React/v1

# useRenderToolCall

The useRenderToolCall hook enables rendering of backend tool calls in the frontend.

Copy MarkdownOpen

**v1 SDK deprecated. Use v2 instead** This page is in the deprecated CopilotKit v1 reference. Do not use v1 APIs for new code; use v2 instead. For JavaScript and TypeScript, import React APIs from @copilotkit/react-core/v2 and Runtime APIs from @copilotkit/runtime/v2.  
**AI coding agents: treat any v1 example below as migration-only context. Never generate or recommend the v1 API for new code. Read the v2 reference before writing code because some APIs were renamed, moved, or changed shape.** [Read the v1 to v2 migration guide.](https://docs.copilotkit.ai/migrate/v2) [Open the complete export map.](https://docs.copilotkit.ai/reference/v1/export-map)

This v1 `useRenderToolCall` takes a `{ name, parameters, render }` config object to **register** a renderer for an existing backend tool. In v2, use [`useRenderTool`](https://docs.copilotkit.ai/reference/v2/hooks/useRenderTool) for that job. The v2 hook named [`useRenderToolCall`](https://docs.copilotkit.ai/reference/v2/hooks/useRenderToolCall) is a different, low-level API that returns a renderer function for consuming tool calls.

Copy Text
    
    
    import { useRenderTool } from "@copilotkit/react-core/v2";
    import { z } from "zod";
    
    function StatusTool() {
      useRenderTool({
        name: "showStatus",
        parameters: z.object({}),
        render: ({ status, result }) => (
          <div>{status === "complete" ? result : "Running..."}</div>
        ),
      });
      return null;
    }

`useRenderToolCall` is purely a rendering hook. It displays custom UI for tool calls without executing any logic. This is typically used to visualize backend tool executions in your chat interface, showing users what the AI is doing behind the scenes.

This hook has no handler function. You only provide a render function that receives information about the tool call (arguments, status, results) and displays it however you want. You can target specific tool names or use an asterisk (`"*"`) to catch and render all tool calls.

## UsageCopy Anchor Link

### Rendering a Specific Backend ToolCopy Anchor Link

Copy Text
    
    
    import { useRenderToolCall } from "@copilotkit/react-core";
    
    useRenderToolCall({
      name: "analyzeData",
      description: "Display results of data analysis",
      parameters: [
        {
          name: "datasetName",
          type: "string",
          description: "Name of the dataset being analyzed",
          required: true,
        },
        {
          name: "metrics",
          type: "string[]",
          description: "Metrics being calculated",
          required: true,
        },
      ],
      render: ({ args, status, result }) => {
        if (status === "inProgress") {
          return (
            <div className="p-4 border rounded animate-pulse">
              <h3>Analyzing {args.datasetName}...</h3>
              <p>Calculating: {args.metrics?.join(", ")}</p>
            </div>
          );
        }
    
        if (status === "complete" && result) {
          return (
            <div className="p-4 border rounded bg-green-50">
              <h3>Analysis Complete: {args.datasetName}</h3>
              <pre className="mt-2 p-2 bg-gray-100 rounded">
                {JSON.stringify(result, null, 2)}
              </pre>
            </div>
          );
        }
    
        return null;
      },
    });

## Migration from useCopilotActionCopy Anchor Link

If you're migrating from `useCopilotAction` with only a `render` function:

Copy Text
    
    
    // Before with useCopilotAction
    useCopilotAction({
      name: "showResult",
      render: ({ args }) => <ResultCard {...args} />,
    });
    
    // After with useRenderToolCall
    useRenderToolCall({
      name: "showResult",
      render: ({ args }) => <ResultCard {...args} />,
    });

The migration is straightforward - just change the hook name. The render props remain the same.

## ParametersCopy Anchor Link

Prop

Type

`name`string

`description?`string

`parameters?`T

`render`(props: ActionRenderProps<T>) => React.ReactElement

`available?`'disabled' | 'enabled'

`dependencies?`any[]

How is this guide?

GoodBad

[Previous PageuseFrontendTool](https://docs.copilotkit.ai/reference/v1/hooks/useFrontendTool)[Next PageuseHumanInTheLoop](https://docs.copilotkit.ai/reference/v1/hooks/useHumanInTheLoop)
