---
url: https://docs.copilotkit.ai/reference/core/enums/ToolCallStatus/
title: ToolCallStatus
method: scrapling+scrapegraph
fetched_at: 2026-11-23T12:09:21.024679+00:00
---

# ToolCallStatus

> Source: https://docs.copilotkit.ai/reference/core/enums/ToolCallStatus/

TypeScript/Enums

# ToolCallStatus

Lifecycle states of a tool call as it streams in and executes.

Copy MarkdownOpen

## OverviewCopy Anchor Link

`ToolCallStatus` describes where a tool call is in its lifecycle, from arguments still streaming in to a fully executed result. You receive it as the `status` prop of a tool call render component, for example in [`useRenderTool`](https://docs.copilotkit.ai/reference/hooks/useRenderTool) or the `render` option of [`useFrontendTool`](https://docs.copilotkit.ai/reference/hooks/useFrontendTool).

## ImportCopy Anchor Link

Copy Text
    
    
    import { ToolCallStatus } from "@copilotkit/core";

## DefinitionCopy Anchor Link

Copy Text
    
    
    enum ToolCallStatus {
      InProgress = "inProgress",
      Executing = "executing",
      Complete = "complete",
    }

## MembersCopy Anchor Link

Prop

Type

`InProgress?`inProgress

`Executing?`executing

`Complete?`complete

## UsageCopy Anchor Link

Copy Text
    
    
    import { ToolCallStatus } from "@copilotkit/core";
    
    function renderToolCall(status: ToolCallStatus) {
      switch (status) {
        case ToolCallStatus.InProgress:
          return "Receiving arguments…";
        case ToolCallStatus.Executing:
          return "Running…";
        case ToolCallStatus.Complete:
          return "Done";
      }
    }

How is this guide?

GoodBad

[Previous PageCopilotKitCoreRuntimeConnectionStatus](https://docs.copilotkit.ai/reference/core/enums/CopilotKitCoreRuntimeConnectionStatus)[Next PageCopilotKitCoreConfig](https://docs.copilotkit.ai/reference/core/types/CopilotKitCoreConfig)
