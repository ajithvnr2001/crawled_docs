---
url: https://docs.copilotkit.ai/reference/core/classes/ProxiedCopilotRuntimeAgent/
title: ProxiedCopilotRuntimeAgent
method: scrapling+scrapegraph
fetched_at: 2026-11-25T12:31:12.020373+00:00
---

# ProxiedCopilotRuntimeAgent

> Source: https://docs.copilotkit.ai/reference/core/classes/ProxiedCopilotRuntimeAgent/

TypeScript/Classes

# ProxiedCopilotRuntimeAgent

AG-UI agent that proxies a CopilotRuntime agent over REST, single-route, or Intelligence transports.

Copy MarkdownOpen

## OverviewCopy Anchor Link

`ProxiedCopilotRuntimeAgent` is the AG-UI [`AbstractAgent`](https://docs.ag-ui.com/sdk/js/client/abstract-agent) implementation (extending `HttpAgent`) that `CopilotKitCore` uses to talk to a CopilotRuntime. You rarely construct this class. `CopilotKitCore` creates one for each runtime agent. To mount several frontend agents against one runtime agent, call [`registerProxiedAgent`](https://docs.copilotkit.ai/reference/core/classes/CopilotKitCore).

The agent builds the correct runtime URLs, picks the transport (`rest`, `single`, or auto-detected), and transparently delegates to an Intelligence agent when the runtime is in Intelligence mode.

## ImportCopy Anchor Link

Copy Text
    
    
    import { ProxiedCopilotRuntimeAgent } from "@copilotkit/core";

## ConstructorCopy Anchor Link

Copy Text
    
    
    new ProxiedCopilotRuntimeAgent(config: ProxiedCopilotRuntimeAgentConfig)

Prop

Type

`config`ProxiedCopilotRuntimeAgentConfig

## MethodsCopy Anchor Link

Prop

Type

`run`(input: RunAgentInput) => Observable<BaseEvent>

`connect`(input: RunAgentInput) => Observable<BaseEvent>

`connectAgent`(parameters?, subscriber?) => Promise<RunAgentResult>

`abortRun`() => void

`detachActiveRun`() => Promise<void>

`getCapabilities`() => Promise<AgentCapabilities>

`clearReplayCursor`(threadId: string) => void

`clone`() => ProxiedCopilotRuntimeAgent

`capabilities`AgentCapabilities | undefined

`runtimeAgentId`string | undefined

## UsageCopy Anchor Link

Copy Text
    
    
    import { CopilotKitCore } from "@copilotkit/core";
    
    const copilotkit = new CopilotKitCore({ runtimeUrl: "/api/copilotkit" });
    
    // Mount a second frontend agent against the same runtime agent.
    const { agent, unregister } = copilotkit.registerProxiedAgent({
      agentId: "chat-1",
      runtimeAgentId: "default",
    });
    
    await copilotkit.runAgent({ agent });
    
    // On cleanup:
    unregister();

## BehaviorCopy Anchor Link

  * **Transport auto-detection** : with `transport: "auto"`, the agent issues `GET /info`; a 2xx response selects REST, otherwise it falls back to single-route (`POST { method: "info" }`).
  * **Lazy mode resolution** : a `"pending"` runtime mode is resolved by a runtime-info fetch before the first `run()` or `connect()`. The agent then takes the HTTP path or the Intelligence path.
  * **Intelligence delegation** : in Intelligence mode the proxy creates an internal `IntelligenceAgent` delegate (websocket) and mirrors its messages, state, and `isRunning` back onto itself.
  * **Immutable routing id** : `runtimeAgentId` is `readonly`; the REST run URL is baked at construction, so mutating it would desync routing.
  * **Abort/Zod errors are swallowed** : `AbortError` and Zod validation errors complete the stream silently rather than propagating, so cancelling a run does not surface as an error.



How is this guide?

GoodBad

[Previous PageCopilotKitCore](https://docs.copilotkit.ai/reference/core/classes/CopilotKitCore)[Next PageCopilotKitCoreErrorCode](https://docs.copilotkit.ai/reference/core/enums/CopilotKitCoreErrorCode)
