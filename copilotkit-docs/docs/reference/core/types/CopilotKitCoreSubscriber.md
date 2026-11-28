---
url: https://docs.copilotkit.ai/reference/core/types/CopilotKitCoreSubscriber/
title: CopilotKitCoreSubscriber
method: scrapling+scrapegraph
fetched_at: 2026-11-28T11:35:15.470233+00:00
---

# CopilotKitCoreSubscriber

> Source: https://docs.copilotkit.ai/reference/core/types/CopilotKitCoreSubscriber/

TypeScript/Types

# CopilotKitCoreSubscriber

Set of optional callbacks notified of CopilotKitCore lifecycle events.

Copy MarkdownOpen

## OverviewCopy Anchor Link

`CopilotKitCoreSubscriber` is the object passed to [`CopilotKitCore.subscribe`](https://docs.copilotkit.ai/reference/core/classes/CopilotKitCore). Every callback is optional, receives an event object that always includes the `copilotkit` instance, and may return `void` or a `Promise<void>`. Use it to react to connection status, tool execution, suggestions, configuration changes, and errors.

## ImportCopy Anchor Link

Copy Text
    
    
    import type { CopilotKitCoreSubscriber } from "@copilotkit/core";

## DefinitionCopy Anchor Link

The shape below shows one callback, `onRuntimeConnectionStatusChanged`. Properties lists the event shape of each callback.

Copy Text
    
    
    interface CopilotKitCoreSubscriber {
      onRuntimeConnectionStatusChanged?: (event: {
        copilotkit: CopilotKitCore;
        status: CopilotKitCoreRuntimeConnectionStatus;
      }) => void | Promise<void>;
      // ...one optional callback per lifecycle event (tool execution, agents,
      // context, suggestions, properties, headers, Inspector metadata, errors,
      // and thread stores).
      // See the Properties section below for each callback's event shape.
    }

## PropertiesCopy Anchor Link

Prop

Type

`onRuntimeConnectionStatusChanged?`(event) => void | Promise<void>

`onToolExecutionStart?`(event) => void | Promise<void>

`onToolExecutionEnd?`(event) => void | Promise<void>

`onAgentsChanged?`(event) => void | Promise<void>

`onAgentRunStarted?`(event) => void | Promise<void>

`onContextChanged?`(event) => void | Promise<void>

`onCatalogComponentsChanged?`(event) => void | Promise<void>

`onSuggestionsConfigChanged?`(event) => void | Promise<void>

`onSuggestionsChanged?`(event) => void | Promise<void>

`onSuggestionsStartedLoading?`(event) => void | Promise<void>

`onSuggestionsFinishedLoading?`(event) => void | Promise<void>

`onPropertiesChanged?`(event) => void | Promise<void>

`onHeadersChanged?`(event) => void | Promise<void>

`onInspectorMetadataChanged?`(event) => void | Promise<void>

`onError?`(event) => void | Promise<void>

`onThreadStoreRegistered?`(event) => void | Promise<void>

`onThreadStoreUnregistered?`(event) => void | Promise<void>

`onTrajectoryChanged?`(event) => void | Promise<void>

## UsageCopy Anchor Link

Copy Text
    
    
    const subscription = copilotkit.subscribe({
      onRuntimeConnectionStatusChanged: ({ status }) => {
        console.log("connection:", status);
      },
      onError: ({ code, error }) => {
        console.error(code, error);
      },
      onInspectorMetadataChanged: ({ inspectorMetadata }) => {
        console.log("project context:", inspectorMetadata);
      },
    });
    
    // later
    subscription.unsubscribe();

How is this guide?

GoodBad

[Previous PageCopilotKitCoreConfig](https://docs.copilotkit.ai/reference/core/types/CopilotKitCoreConfig)[Next PageFrontendTool](https://docs.copilotkit.ai/reference/core/types/FrontendTool)
