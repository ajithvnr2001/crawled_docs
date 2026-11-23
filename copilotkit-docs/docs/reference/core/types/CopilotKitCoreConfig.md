---
url: https://docs.copilotkit.ai/reference/core/types/CopilotKitCoreConfig/
title: CopilotKitCoreConfig
method: scrapling+scrapegraph
fetched_at: 2026-11-23T12:09:21.146067+00:00
---

# CopilotKitCoreConfig

> Source: https://docs.copilotkit.ai/reference/core/types/CopilotKitCoreConfig/

TypeScript/Types

# CopilotKitCoreConfig

Configuration object passed to the CopilotKitCore constructor.

Copy MarkdownOpen

## OverviewCopy Anchor Link

`CopilotKitCoreConfig` is the configuration object accepted by the [`CopilotKitCore`](https://docs.copilotkit.ai/reference/core/classes/CopilotKitCore) constructor. It wires the core to a CopilotRuntime endpoint and seeds it with frontend tools, suggestions, request headers, and forwarded properties.

## ImportCopy Anchor Link

Copy Text
    
    
    import type { CopilotKitCoreConfig } from "@copilotkit/core";

## DefinitionCopy Anchor Link

Copy Text
    
    
    interface CopilotKitCoreConfig {
      runtimeUrl?: string;
      runtimeTransport?: CopilotRuntimeTransport;
      deferInitialConnection?: boolean;
      agents__unsafe_dev_only?: Record<string, AbstractAgent>;
      headers?: CopilotKitHeadersSource;
      credentials?: RequestCredentials;
      messageFilter?: CopilotKitMessageFilter;
      properties?: Record<string, unknown>;
      tools?: FrontendTool<any>[];
      suggestionsConfig?: SuggestionsConfig[];
      debug?: DebugConfig;
      learning?: LearningConfig;
    }

## PropertiesCopy Anchor Link

Prop

Type

`runtimeUrl?`string

`runtimeTransport?`"rest" | "single" | "auto"

`deferInitialConnection?`boolean

`agents__unsafe_dev_only?`Record<string, AbstractAgent>

`headers?`CopilotKitHeadersSource

`credentials?`RequestCredentials

`messageFilter?`CopilotKitMessageFilter

`properties?`Record<string, unknown>

`tools?`FrontendTool<any>[]

`suggestionsConfig?`SuggestionsConfig[]

`debug?`DebugConfig

`learning?`LearningConfig

## UsageCopy Anchor Link

Copy Text
    
    
    import { CopilotKitCore } from "@copilotkit/core";
    import { z } from "zod";
    
    const copilotkit = new CopilotKitCore({
      runtimeUrl: "/api/copilotkit",
      headers: { Authorization: "Bearer token" },
      properties: { userId: "user_123" },
      tools: [
        {
          name: "sayHello",
          description: "Greet the user",
          parameters: z.object({ name: z.string() }),
          handler: async ({ name }) => `Hello, ${name}!`,
        },
      ],
    });

How is this guide?

GoodBad

[Previous PageToolCallStatus](https://docs.copilotkit.ai/reference/core/enums/ToolCallStatus)[Next PageCopilotKitCoreSubscriber](https://docs.copilotkit.ai/reference/core/types/CopilotKitCoreSubscriber)
