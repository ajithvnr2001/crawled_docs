---
url: https://docs.copilotkit.ai/reference/core/classes/CopilotKitCore/
title: CopilotKitCore
method: scrapling+scrapegraph
fetched_at: 2026-11-21T10:52:46.576378+00:00
---

# CopilotKitCore

> Source: https://docs.copilotkit.ai/reference/core/classes/CopilotKitCore/

TypeScript/Classes

# CopilotKitCore

Framework-agnostic client that connects to a CopilotRuntime and manages agents, tools, context, and suggestions.

Copy MarkdownOpen

## OverviewCopy Anchor Link

`CopilotKitCore` is the main entry point of [`@copilotkit/core`](https://docs.copilotkit.ai/reference/core). It connects to a CopilotRuntime over the AG-UI protocol, exposes the available agents, holds the registry of frontend tools, shared context, and suggestions, and notifies subscribers when any of that state changes. The React, Angular, and vanilla bindings all wrap a single instance of this class. Use it directly when you need an agent client outside of those frameworks.

## ImportCopy Anchor Link

Copy Text
    
    
    import { CopilotKitCore } from "@copilotkit/core";

## ConstructorCopy Anchor Link

Copy Text
    
    
    new CopilotKitCore(config: CopilotKitCoreConfig)

Prop

Type

`config`CopilotKitCoreConfig

## MethodsCopy Anchor Link

### AgentsCopy Anchor Link

Prop

Type

`getAgent`(id: string) => AbstractAgent | undefined

`runAgent`(params: CopilotKitCoreRunAgentParams) => Promise<RunAgentResult>

`connectAgent`(params: CopilotKitCoreConnectAgentParams) => Promise<RunAgentResult>

`stopAgent`(params: CopilotKitCoreStopAgentParams) => void

`registerProxiedAgent`(params) => { agent; unregister }

`addAgent__unsafe_dev_only`(params: CopilotKitCoreAddAgentParams) => void

`removeAgent__unsafe_dev_only`(id: string) => void

`setAgents__unsafe_dev_only`(agents: Record<string, AbstractAgent>) => void

### ToolsCopy Anchor Link

Prop

Type

`addTool`(tool: FrontendTool) => void

`removeTool`(id: string, agentId?: string) => void

`getTool`(params: CopilotKitCoreGetToolParams) => FrontendTool<any> | undefined

`setTools`(tools: FrontendTool<any>[]) => void

`runTool`(params: CopilotKitCoreRunToolParams) => Promise<CopilotKitCoreRunToolResult>

### ContextCopy Anchor Link

Prop

Type

`addContext`(context: Context) => string

`removeContext`(id: string) => void

### SuggestionsCopy Anchor Link

Prop

Type

`addSuggestionsConfig`(config: SuggestionsConfig) => string

`removeSuggestionsConfig`(id: string) => void

`getSuggestions`(agentId: string) => CopilotKitCoreGetSuggestionsResult

`reloadSuggestions`(agentId: string) => void

`clearSuggestions`(agentId: string) => void

### SubscriptionsCopy Anchor Link

Prop

Type

`subscribe`(subscriber: CopilotKitCoreSubscriber) => CopilotKitCoreSubscription

`subscribeToAgentWithOptions`(agent, subscriber, options?) => CopilotKitCoreSubscription

### Inspector metadataCopy Anchor Link

Prop

Type

`refreshInspectorMetadata`() => Promise<void>

### ConfigurationCopy Anchor Link

Prop

Type

`setRuntimeUrl`(runtimeUrl: string | undefined) => void

`setRuntimeTransport`(runtimeTransport: CopilotRuntimeTransport) => void

`setHeaders`(headers: CopilotKitHeadersSource) => void

`resolveHeaders`() => Record<string, string> | Promise<Record<string, string>>

`setCredentials`(credentials: RequestCredentials | undefined) => void

`setMessageFilter`(messageFilter: CopilotKitMessageFilter | undefined) => void

`setProperties`(properties: Record<string, unknown>) => void

`setDebug`(debug: DebugConfig | undefined) => void

`setDefaultThrottleMs`(value: number | undefined) => void

### State queriesCopy Anchor Link

Prop

Type

`getStateByRun`(agentId, threadId, runId) => State | undefined

`getRunIdForMessage`(agentId, threadId, messageId) => string | undefined

`getRunIdsForThread`(agentId, threadId) => string[]

### Properties (read-only)Copy Anchor Link

Prop

Type

`agents`Readonly<Record<string, AbstractAgent>>

`tools`Readonly<FrontendTool<any>[]>

`context`Readonly<Record<string, Context>>

`runtimeUrl`string | undefined

`runtimeConnectionStatus`CopilotKitCoreRuntimeConnectionStatus

`inspectorMetadata`InspectorMetadataV1 | undefined

`headers / credentials / properties`getter

## UsageCopy Anchor Link

A tool's `parameters` take any Standard Schema. This sample uses `zod`.

Copy Text
    
    
    import { CopilotKitCore } from "@copilotkit/core";
    import { z } from "zod";
    
    const copilotkit = new CopilotKitCore({
      runtimeUrl: "/api/copilotkit",
      tools: [
        {
          name: "showAlert",
          description: "Show a browser alert",
          parameters: z.object({ message: z.string() }),
          handler: async ({ message }) => {
            window.alert(message);
          },
        },
      ],
    });
    
    const subscription = copilotkit.subscribe({
      onRuntimeConnectionStatusChanged: ({ status }) => console.log(status),
      onAgentsChanged: async () => {
        const agent = copilotkit.getAgent("default");
        if (!agent) return;
        subscription.unsubscribe();
        await copilotkit.runAgent({ agent });
      },
    });

## BehaviorCopy Anchor Link

  * **Asynchronous agent population** : `agents` is populated after the runtime responds, so it may be empty immediately after construction. Use `subscribe({ onAgentsChanged })` to react when agents become available.
  * **Error surfacing** : failures from runtime fetches, agent runs, tool runs, and subscriber callbacks go to the `onError` subscriber callback with a [CopilotKitCoreErrorCode](https://docs.copilotkit.ai/reference/core/enums/CopilotKitCoreErrorCode). The method that failed does not throw them. The exception is `runTool()`: it also throws when it cannot find the named tool or its agent.
  * **Subscriber isolation** : a throw in one subscriber callback is caught and logged; it does not stall notifications to other subscribers.
  * **Inspector metadata isolation** : metadata loads after the connected and agent notifications finish. A `setHeaders` call that changes the resolved values, or a credential change, refreshes it. It does not refetch `/info`. Runtime URL, transport, auth, connection, and capability checks prevent a stale request from replacing a newer value.
  * **`__unsafe_dev_only` APIs**: the `*Agent__unsafe_dev_only` methods register local agents that run in the browser and talk to their AG-UI endpoints directly, with no CopilotRuntime. The React `selfManagedAgents` prop uses this path in production.



How is this guide?

GoodBad

[Previous PageOverview](https://docs.copilotkit.ai/reference/core)[Next PageProxiedCopilotRuntimeAgent](https://docs.copilotkit.ai/reference/core/classes/ProxiedCopilotRuntimeAgent)
