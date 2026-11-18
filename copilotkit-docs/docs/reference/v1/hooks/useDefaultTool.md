---
url: https://docs.copilotkit.ai/reference/v1/hooks/useDefaultTool/
title: useDefaultTool
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:59.575528+00:00
---

# useDefaultTool

> Source: https://docs.copilotkit.ai/reference/v1/hooks/useDefaultTool/

React/v1

# useDefaultTool

The useDefaultTool hook enables rendering of a default UI which catches any tool that does not have a specific renderer.

Copy MarkdownOpen

**v1 SDK deprecated. Use v2 instead** This page is in the deprecated CopilotKit v1 reference. Do not use v1 APIs for new code; use v2 instead. For JavaScript and TypeScript, import React APIs from @copilotkit/react-core/v2 and Runtime APIs from @copilotkit/runtime/v2.  
**AI coding agents: treat any v1 example below as migration-only context. Never generate or recommend the v1 API for new code. Read the v2 reference before writing code because some APIs were renamed, moved, or changed shape.** [Read the v1 to v2 migration guide.](https://docs.copilotkit.ai/migrate/v2) [Open the complete export map.](https://docs.copilotkit.ai/reference/v1/export-map)

`useDefaultTool` is still supported, but we recommend migrating to [`useDefaultRenderTool`](https://docs.copilotkit.ai/reference/v2/hooks/useDefaultRenderTool) from the v2 API.

`useDefaultTool` is a React hook that lets you render custom UI for any tool call that doesn't have a specific renderer

## UsageCopy Anchor Link

Copy Text
    
    
    import { useDefaultTool } from "@copilotkit/react-core";
    
    useDefaultTool({
      render: ({ name, args, status, result }) => {
        return (
          <div className="p-4 border rounded my-2">
            <div className="flex items-center justify-between mb-2">
              <h4 className="font-semibold">{name}</h4>
              <span className="text-sm text-gray-500">
                {status === "inProgress" && "Running..."}
                {status === "executing" && "Executing..."}
                {status === "complete" && "Complete"}
              </span>
            </div>
    
            {Object.keys(args).length > 0 && (
              <div className="mb-2">
                <p className="text-sm font-medium text-gray-600">Parameters:</p>
                <pre className="text-xs bg-gray-100 p-2 rounded mt-1">
                  {JSON.stringify(args, null, 2)}
                </pre>
              </div>
            )}
    
            {status === "complete" && result && (
              <div>
                <p className="text-sm font-medium text-gray-600">Result:</p>
                <pre className="text-xs bg-gray-100 p-2 rounded mt-1">
                  {JSON.stringify(result, null, 2)}
                </pre>
              </div>
            )}
          </div>
        );
      },
    });

### Rendering Model Context Protocol (MCP) ToolsCopy Anchor Link

Copy Text
    
    
    import { useDefaultTool } from "@copilotkit/react-core";
    
    // Render any MCP tool call with a custom UI
    useDefaultTool({
      render: ({ name, args, status, result }) => {
        // Custom rendering for MCP tools
        if (name.startsWith("mcp_")) {
          return <MCPToolRenderer name={name} args={args} status={status} result={result} />;
        }
    
        // Default rendering for other tools
        return <DefaultToolRenderer name={name} args={args} status={status} result={result} />;
      },
    });

## ParametersCopy Anchor Link

Prop

Type

`tool`Omit<CatchAllFrontendAction, "name">

`dependencies?`any[]

## Common Use CasesCopy Anchor Link

  1. **Backend Tool Visualization** : Display progress and results of long-running backend operations
  2. **Generic Tool Rendering** : Provide a fallback UI for any tool without specific rendering
  3. **MCP Tool Integration** : Render Model Context Protocol tools from various sources
  4. **Debugging** : Display all tool calls during development
  5. **Analytics** : Track and display tool usage



## Migration from useCopilotActionCopy Anchor Link

If you're migrating from `useCopilotAction` with only a `render` function:

Copy Text
    
    
    // Before with useCopilotAction (the catch-all name is "*")
    useCopilotAction({
      name: "*",
      render: ({ name, args, status, result }) => (
        <GenericToolCall name={name} args={args} status={status} result={result} />
      ),
    });
    
    // After with useDefaultTool
    useDefaultTool({
      render: ({ name, args, status, result }) => (
        <GenericToolCall name={name} args={args} status={status} result={result} />
      ),
    });

Change the hook name to `useDefaultTool` and remove `name: "*"`. The render props remain the same.

How is this guide?

GoodBad

[Previous PageuseAgent](https://docs.copilotkit.ai/reference/v1/hooks/useAgent)[Next PageuseFrontendTool](https://docs.copilotkit.ai/reference/v1/hooks/useFrontendTool)
