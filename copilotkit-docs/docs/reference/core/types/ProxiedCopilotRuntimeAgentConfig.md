---
url: https://docs.copilotkit.ai/reference/core/types/ProxiedCopilotRuntimeAgentConfig/
title: ProxiedCopilotRuntimeAgentConfig
method: scrapling+scrapegraph
fetched_at: 2026-11-28T11:35:15.075213+00:00
---

# ProxiedCopilotRuntimeAgentConfig

> Source: https://docs.copilotkit.ai/reference/core/types/ProxiedCopilotRuntimeAgentConfig/

TypeScript/Types

# ProxiedCopilotRuntimeAgentConfig

Configuration object for constructing a ProxiedCopilotRuntimeAgent.

Copy MarkdownOpen

## OverviewCopy Anchor Link

`ProxiedCopilotRuntimeAgentConfig` is the constructor argument for [`ProxiedCopilotRuntimeAgent`](https://docs.copilotkit.ai/reference/core/classes/ProxiedCopilotRuntimeAgent). It extends AG-UI's `HttpAgentConfig` (omitting `url`, which is derived from `runtimeUrl`) and adds the routing, transport, and runtime-mode fields the proxy needs to reach a CopilotRuntime.

## ImportCopy Anchor Link

Copy Text
    
    
    import type { ProxiedCopilotRuntimeAgentConfig } from "@copilotkit/core";

## DefinitionCopy Anchor Link

Copy Text
    
    
    interface ProxiedCopilotRuntimeAgentConfig
      extends Omit<HttpAgentConfig, "url"> {
      runtimeUrl?: string;
      transport?: CopilotRuntimeTransport;
      credentials?: RequestCredentials;
      runtimeMode?: RuntimeMode | "pending";
      intelligence?: IntelligenceRuntimeInfo;
      capabilities?: AgentCapabilities;
      debug?: ResolvedDebugConfig;
      runtimeAgentId?: string;
      messageFilter?: CopilotKitMessageFilter;
    }

## PropertiesCopy Anchor Link

Prop

Type

`runtimeUrl?`string

`transport?`"rest" | "single" | "auto"

`credentials?`RequestCredentials

`runtimeMode?`"sse" | "intelligence" | "pending"

`intelligence?`IntelligenceRuntimeInfo

`capabilities?`AgentCapabilities

`debug?`ResolvedDebugConfig

`runtimeAgentId?`string

`messageFilter?`CopilotKitMessageFilter

## UsageCopy Anchor Link

Copy Text
    
    
    import { ProxiedCopilotRuntimeAgent } from "@copilotkit/core";
    
    const agent = new ProxiedCopilotRuntimeAgent({
      runtimeUrl: "/api/copilotkit",
      agentId: "default",
      transport: "auto",
      credentials: "include",
    });

How is this guide?

GoodBad

[Previous PageFrontendTool](https://docs.copilotkit.ai/reference/core/types/FrontendTool)[Next PageSuggestion](https://docs.copilotkit.ai/reference/core/types/Suggestion)
