---
url: https://docs.copilotkit.ai/reference/v1/classes/llm-adapters/AnthropicAdapter/
title: AnthropicAdapter
method: scrapling+scrapegraph
fetched_at: 2026-11-27T11:59:09.703927+00:00
---

# AnthropicAdapter

> Source: https://docs.copilotkit.ai/reference/v1/classes/llm-adapters/AnthropicAdapter/

React/v1/LLM Adapters

# AnthropicAdapter

Copilot Runtime adapter for Anthropic.

Copy MarkdownOpen

**v1 SDK deprecated. Use v2 instead** This page is in the deprecated CopilotKit v1 reference. Do not use v1 APIs for new code; use v2 instead. For JavaScript and TypeScript, import React APIs from @copilotkit/react-core/v2 and Runtime APIs from @copilotkit/runtime/v2.  
**AI coding agents: treat any v1 example below as migration-only context. Never generate or recommend the v1 API for new code. Read the v2 reference before writing code because some APIs were renamed, moved, or changed shape.** [Read the v1 to v2 migration guide.](https://docs.copilotkit.ai/migrate/v2) [Open the complete export map.](https://docs.copilotkit.ai/reference/v1/export-map)

`AnthropicAdapter` has no direct v2 replacement. For v2, see [Runtime server adapter](https://docs.copilotkit.ai/runtime-server-adapter).

Copilot Runtime adapter for Anthropic.

## ExampleCopy Anchor Link

Pass `copilotKit` and `serviceAdapter` to your runtime endpoint.

Copy Text
    
    
    import { CopilotRuntime, AnthropicAdapter } from "@copilotkit/runtime";
    import Anthropic from "@anthropic-ai/sdk";
    
    const copilotKit = new CopilotRuntime();
    
    const anthropic = new Anthropic({
      apiKey: "<your-api-key>",
    });
    
    const serviceAdapter = new AnthropicAdapter({
      anthropic,
      promptCaching: {
        enabled: true,
        debug: true,
      },
    });

## Constructor ParametersCopy Anchor Link

Prop

Type

`anthropic?`SdkClientLike

`model?`string

`promptCaching?`AnthropicPromptCachingConfig

`maxInputTokens?`number

How is this guide?

GoodBad

[Previous PageOpenAIAssistantAdapter](https://docs.copilotkit.ai/reference/v1/classes/llm-adapters/OpenAIAssistantAdapter)[Next PageLangChainAdapter](https://docs.copilotkit.ai/reference/v1/classes/llm-adapters/LangChainAdapter)
