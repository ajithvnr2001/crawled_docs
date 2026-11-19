---
url: https://docs.copilotkit.ai/reference/core/enums/CopilotKitCoreRuntimeConnectionStatus/
title: CopilotKitCoreRuntimeConnectionStatus
method: scrapling+scrapegraph
fetched_at: 2026-11-19T11:26:32.402317+00:00
---

# CopilotKitCoreRuntimeConnectionStatus

> Source: https://docs.copilotkit.ai/reference/core/enums/CopilotKitCoreRuntimeConnectionStatus/

TypeScript/Enums

# CopilotKitCoreRuntimeConnectionStatus

Connection states between CopilotKitCore and the CopilotRuntime.

Copy MarkdownOpen

## OverviewCopy Anchor Link

`CopilotKitCoreRuntimeConnectionStatus` represents the state of the connection between `CopilotKitCore` and its runtime. You encounter it via [`copilotkit.runtimeConnectionStatus`](https://docs.copilotkit.ai/reference/core/classes/CopilotKitCore) and the [`onRuntimeConnectionStatusChanged`](https://docs.copilotkit.ai/reference/core/types/CopilotKitCoreSubscriber) subscriber callback.

**The status reports the outcome of the last actual contact with the runtime.** It is not a claim about the present moment. A failed runtime request moves it to `Error`, and a successful one moves it back. Nothing else moves it. There is no polling and no heartbeat, so an outage that begins while your application is idle is not noticed until something is sent.

## ImportCopy Anchor Link

Copy Text
    
    
    import { CopilotKitCoreRuntimeConnectionStatus } from "@copilotkit/core";

## DefinitionCopy Anchor Link

Copy Text
    
    
    enum CopilotKitCoreRuntimeConnectionStatus {
      Disconnected = "disconnected",
      Connected = "connected",
      Connecting = "connecting",
      Error = "error",
    }

## MembersCopy Anchor Link

Prop

Type

`Disconnected?`disconnected

`Connected?`connected

`Connecting?`connecting

`Error?`error

## UsageCopy Anchor Link

Copy Text
    
    
    copilotkit.subscribe({
      onRuntimeConnectionStatusChanged: ({ status }) => {
        if (status === CopilotKitCoreRuntimeConnectionStatus.Connected) {
          enableChat();
          return;
        }
    
        if (status === CopilotKitCoreRuntimeConnectionStatus.Error) {
          showConnectionError();
          if (Object.keys(copilotkit.agents).length === 0) {
            disableChat();
          }
        }
      },
    });

How is this guide?

GoodBad

[Previous PageCopilotKitCoreErrorCode](https://docs.copilotkit.ai/reference/core/enums/CopilotKitCoreErrorCode)[Next PageToolCallStatus](https://docs.copilotkit.ai/reference/core/enums/ToolCallStatus)
