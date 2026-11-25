---
url: https://docs.copilotkit.ai/reference/core/
title: @copilotkit/core
method: scrapling+scrapegraph
fetched_at: 2026-11-25T12:31:12.225198+00:00
---

# @copilotkit/core

> Source: https://docs.copilotkit.ai/reference/core/

TypeScript

# @copilotkit/core

Framework-agnostic TypeScript client for CopilotKit. Runs anywhere JavaScript runs.

Copy MarkdownOpen

`@copilotkit/core` is the framework-agnostic TypeScript client at the heart of CopilotKit. It connects to a CopilotRuntime over the AG-UI protocol, manages agents, frontend tools, shared context, and suggestions, and emits state changes to subscribers. It has no UI or React dependency, so it runs in browsers, Node, workers, and inside the React, Angular, and vanilla bindings.

## InstallCopy Anchor Link

Copy Text
    
    
    npm install @copilotkit/core zod

## Quick startCopy Anchor Link

Copy Text
    
    
    import { CopilotKitCore } from "@copilotkit/core";
    import { z } from "zod";
    
    const copilotkit = new CopilotKitCore({
      runtimeUrl: "/api/copilotkit",
    });
    
    // Register a frontend tool the agent can call.
    copilotkit.addTool({
      name: "showAlert",
      parameters: z.object({ message: z.string() }),
      handler: async ({ message }) => {
        window.alert(message);
        return "Alert shown";
      },
    });
    
    // Agents load after the runtime responds.
    const sub = copilotkit.subscribe({
      onAgentsChanged: async ({ agents }) => {
        const agent = agents["default"];
        if (!agent) return;
        sub.unsubscribe();
        agent.addMessage({
          id: crypto.randomUUID(),
          role: "user",
          content: "Show an alert that says hi",
        });
        await copilotkit.runAgent({ agent });
      },
    });

## ReferenceCopy Anchor Link

  * [CopilotKitCore](https://docs.copilotkit.ai/reference/core/classes/CopilotKitCore): the main client class.
  * [ProxiedCopilotRuntimeAgent](https://docs.copilotkit.ai/reference/core/classes/ProxiedCopilotRuntimeAgent): AG-UI agent that proxies a CopilotRuntime agent.
  * [CopilotKitCoreConfig](https://docs.copilotkit.ai/reference/core/types/CopilotKitCoreConfig): options accepted by the `CopilotKitCore` constructor.
  * [ProxiedCopilotRuntimeAgentConfig](https://docs.copilotkit.ai/reference/core/types/ProxiedCopilotRuntimeAgentConfig): options accepted by the `ProxiedCopilotRuntimeAgent` constructor.
  * [FrontendTool](https://docs.copilotkit.ai/reference/core/types/FrontendTool): shape of a tool registered with `addTool`.
  * [CopilotKitCoreSubscriber](https://docs.copilotkit.ai/reference/core/types/CopilotKitCoreSubscriber): callbacks passed to `subscribe`.
  * [Suggestion](https://docs.copilotkit.ai/reference/core/types/Suggestion) / [SuggestionsConfig](https://docs.copilotkit.ai/reference/core/types/SuggestionsConfig): suggestion data and configuration.
  * [ToolCallStatus](https://docs.copilotkit.ai/reference/core/enums/ToolCallStatus): tool-call lifecycle states.
  * [CopilotKitCoreErrorCode](https://docs.copilotkit.ai/reference/core/enums/CopilotKitCoreErrorCode): error codes surfaced through `onError`.
  * [CopilotKitCoreRuntimeConnectionStatus](https://docs.copilotkit.ai/reference/core/enums/CopilotKitCoreRuntimeConnectionStatus): runtime connection states.



How is this guide?

GoodBad

[Previous PageCopilotKit](https://docs.copilotkit.ai/reference/angular/services/CopilotKit)[Next PageCopilotKitCore](https://docs.copilotkit.ai/reference/core/classes/CopilotKitCore)
