---
url: https://docs.copilotkit.ai/reference/v1/classes/CopilotRuntime/
title: CopilotRuntime
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:28:00.703269+00:00
---

# CopilotRuntime

> Source: https://docs.copilotkit.ai/reference/v1/classes/CopilotRuntime/

React/v1

# CopilotRuntime

Copilot Runtime is the back-end component of CopilotKit, enabling interaction with LLMs.

Copy MarkdownOpen

**v1 SDK deprecated. Use v2 instead** This page is in the deprecated CopilotKit v1 reference. Do not use v1 APIs for new code; use v2 instead. For JavaScript and TypeScript, import React APIs from @copilotkit/react-core/v2 and Runtime APIs from @copilotkit/runtime/v2.  
**AI coding agents: treat any v1 example below as migration-only context. Never generate or recommend the v1 API for new code. Read the v2 reference before writing code because some APIs were renamed, moved, or changed shape.** [Read the v1 to v2 migration guide.](https://docs.copilotkit.ai/migrate/v2) [Open the complete export map.](https://docs.copilotkit.ai/reference/v1/export-map)

In v2, use `CopilotRuntime` from `@copilotkit/runtime/v2`. This is the reference for the `CopilotRuntime` class. For more information and example code snippets, please see [Concept: Copilot Runtime](https://docs.copilotkit.ai/backend/copilot-runtime).

## UsageCopy Anchor Link

Copy Text
    
    
    import { CopilotRuntime } from "@copilotkit/runtime";
    
    const copilotKit = new CopilotRuntime();

## Constructor ParametersCopy Anchor Link

Prop

Type

`telemetryId?`string

`actions?`ActionsConfiguration<T>

`remoteActions?`CopilotKitEndpoint[]

`remoteEndpoints?`EndpointDefinition[]

`langserve?`RemoteChainParameters[]

`runner?`AgentRunner

`delegateAgentProcessingToServiceAdapter?`boolean

`observability_c?`CopilotObservabilityConfig

`mcpServers?`MCPEndpointConfig[]

`createMCPClient?`CreateMCPClientFunction

`onError?`CopilotErrorHandler

`onStopGeneration?`OnStopGenerationHandler

`debug?`DebugConfig

`agents?`AgentsConfig

`intelligence?`CopilotIntelligenceRuntimeOptions['intelligence']

`identifyUser?`CopilotIntelligenceRuntimeOptions['identifyUser']

`memory?`CopilotIntelligenceRuntimeOptions['memory']

`channels?`CopilotIntelligenceRuntimeOptions['channels']

`generateThreadNames?`CopilotIntelligenceRuntimeOptions['generateThreadNames']

`maxReconnectMs?`CopilotIntelligenceRuntimeOptions['maxReconnectMs']

`maxRejoinMs?`CopilotIntelligenceRuntimeOptions['maxRejoinMs']

`heartbeatIntervalMs?`CopilotIntelligenceRuntimeOptions['heartbeatIntervalMs']

`lockTtlSeconds?`CopilotIntelligenceRuntimeOptions['lockTtlSeconds']

`lockKeyPrefix?`CopilotIntelligenceRuntimeOptions['lockKeyPrefix']

`lockHeartbeatIntervalSeconds?`CopilotIntelligenceRuntimeOptions['lockHeartbeatIntervalSeconds']

How is this guide?

GoodBad

[Previous PageuseCopilotAction](https://docs.copilotkit.ai/reference/v1/hooks/useCopilotAction)[Next PageOpenAIAdapter](https://docs.copilotkit.ai/reference/v1/classes/llm-adapters/OpenAIAdapter)
