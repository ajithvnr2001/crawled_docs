---
url: https://docs.copilotkit.ai/reference/core/types/Suggestion/
title: Suggestion
method: scrapling+scrapegraph
fetched_at: 2026-11-25T12:31:11.150458+00:00
---

# Suggestion

> Source: https://docs.copilotkit.ai/reference/core/types/Suggestion/

TypeScript/Types

# Suggestion

A single suggested prompt presented to the user.

Copy MarkdownOpen

## OverviewCopy Anchor Link

`Suggestion` represents one suggested prompt shown to the user (typically as a clickable pill). Suggestions are produced from a [`SuggestionsConfig`](https://docs.copilotkit.ai/reference/core/types/SuggestionsConfig) and surfaced through [`CopilotKitCoreSubscriber.onSuggestionsChanged`](https://docs.copilotkit.ai/reference/core/types/CopilotKitCoreSubscriber).

## ImportCopy Anchor Link

Copy Text
    
    
    import type { Suggestion } from "@copilotkit/core";

## DefinitionCopy Anchor Link

Copy Text
    
    
    type Suggestion = {
      title: string;
      message: string;
      isLoading: boolean;
      className?: string;
    };

## PropertiesCopy Anchor Link

Prop

Type

`title`string

`message`string

`isLoading`boolean

`className?`string

## UsageCopy Anchor Link

Copy Text
    
    
    import type { Suggestion } from "@copilotkit/core";
    
    const suggestion: Suggestion = {
      title: "Summarize",
      message: "Summarize the current document",
      isLoading: false,
    };

How is this guide?

GoodBad

[Previous PageProxiedCopilotRuntimeAgentConfig](https://docs.copilotkit.ai/reference/core/types/ProxiedCopilotRuntimeAgentConfig)[Next PageSuggestionsConfig](https://docs.copilotkit.ai/reference/core/types/SuggestionsConfig)
