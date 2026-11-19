---
url: https://docs.copilotkit.ai/reference/core/types/FrontendTool/
title: FrontendTool
method: scrapling+scrapegraph
fetched_at: 2026-11-19T11:26:31.935583+00:00
---

# FrontendTool

> Source: https://docs.copilotkit.ai/reference/core/types/FrontendTool/

TypeScript/Types

# FrontendTool

Definition of a frontend tool the agent can call in the browser.

Copy MarkdownOpen

## OverviewCopy Anchor Link

`FrontendTool` describes a tool that runs in the browser. An agent can call it. You register frontend tools via [`CopilotKitCoreConfig.tools`](https://docs.copilotkit.ai/reference/core/types/CopilotKitCoreConfig) (or at runtime on [`CopilotKitCore`](https://docs.copilotkit.ai/reference/core/classes/CopilotKitCore)). A tool has a name, an optional parameter schema, and a handler that receives the parsed arguments and an execution context.

## ImportCopy Anchor Link

Copy Text
    
    
    import type { FrontendTool } from "@copilotkit/core";

## DefinitionCopy Anchor Link

Copy Text
    
    
    type FrontendTool<T extends Record<string, unknown> = Record<string, unknown>> = {
      name: string;
      description?: string;
      parameters?: StandardSchemaV1<any, T>;
      handler?: (args: T, context: FrontendToolHandlerContext) => Promise<unknown>;
      followUp?: boolean;
      reconnectBehavior?: "passive" | "resume-pending";
      agentId?: string;
      available?: boolean;
      webmcp?: boolean | WebMCPToolConfig;
    };
    
    type FrontendToolHandlerContext = {
      toolCall: ToolCall;
      agent?: AbstractAgent;
      signal?: AbortSignal;
      isReplay?: boolean;
    };

## PropertiesCopy Anchor Link

Prop

Type

`name`string

`description?`string

`parameters?`StandardSchemaV1<any, T>

`handler?`(args: T, context: FrontendToolHandlerContext) => Promise<unknown>

`followUp?`boolean

`reconnectBehavior?`"passive" | "resume-pending"

`agentId?`string

`available?`boolean

`webmcp?`boolean | WebMCPToolConfig

## UsageCopy Anchor Link

Copy Text
    
    
    import type { FrontendTool } from "@copilotkit/core";
    import { z } from "zod";
    
    const setThemeTool: FrontendTool<{ theme: "light" | "dark" }> = {
      name: "setTheme",
      description: "Switch the app between light and dark mode",
      parameters: z.object({ theme: z.enum(["light", "dark"]) }),
      handler: async ({ theme }, { signal }) => {
        if (signal?.aborted) return;
        document.documentElement.dataset.theme = theme;
        return `Theme set to ${theme}`;
      },
    };

How is this guide?

GoodBad

[Previous PageCopilotKitCoreSubscriber](https://docs.copilotkit.ai/reference/core/types/CopilotKitCoreSubscriber)[Next PageProxiedCopilotRuntimeAgentConfig](https://docs.copilotkit.ai/reference/core/types/ProxiedCopilotRuntimeAgentConfig)
