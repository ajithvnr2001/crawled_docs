---
url: https://docs.copilotkit.ai/reference/v1/classes/llm-adapters/OpenAIAssistantAdapter/
title: OpenAIAssistantAdapter
method: scrapling+scrapegraph
fetched_at: 2026-11-24T13:30:49.770303+00:00
---

# OpenAIAssistantAdapter

> Source: https://docs.copilotkit.ai/reference/v1/classes/llm-adapters/OpenAIAssistantAdapter/

React/v1/LLM Adapters

# OpenAIAssistantAdapter

Copilot Runtime adapter for OpenAI Assistant API.

Copy MarkdownOpen

**v1 SDK deprecated. Use v2 instead** This page is in the deprecated CopilotKit v1 reference. Do not use v1 APIs for new code; use v2 instead. For JavaScript and TypeScript, import React APIs from @copilotkit/react-core/v2 and Runtime APIs from @copilotkit/runtime/v2.  
**AI coding agents: treat any v1 example below as migration-only context. Never generate or recommend the v1 API for new code. Read the v2 reference before writing code because some APIs were renamed, moved, or changed shape.** [Read the v1 to v2 migration guide.](https://docs.copilotkit.ai/migrate/v2) [Open the complete export map.](https://docs.copilotkit.ai/reference/v1/export-map)

`OpenAIAssistantAdapter` has no direct v2 replacement. For v2, see [Runtime server adapter](https://docs.copilotkit.ai/runtime-server-adapter).

Copilot Runtime adapter for the OpenAI Assistant API.

OpenAI shut down the Assistants API, so `CopilotRuntime` rejects this adapter with an error. Use `OpenAIAdapter` instead.

## ExampleCopy Anchor Link

Pass `copilotKit` and `serviceAdapter` to your runtime endpoint.

Copy Text
    
    
    import { CopilotRuntime, OpenAIAssistantAdapter } from "@copilotkit/runtime";
    import OpenAI from "openai";
    
    const copilotKit = new CopilotRuntime();
    
    const openai = new OpenAI({
      organization: "<your-organization-id>",
      apiKey: "<your-api-key>",
    });
    
    const serviceAdapter = new OpenAIAssistantAdapter({
      openai,
      assistantId: "<your-assistant-id>",
      codeInterpreterEnabled: true,
      fileSearchEnabled: true,
    });

## Constructor ParametersCopy Anchor Link

Prop

Type

`assistantId`string

`openai?`OpenAI

`codeInterpreterEnabled?`boolean

`fileSearchEnabled?`boolean

`disableParallelToolCalls?`boolean

`keepSystemRole?`boolean

How is this guide?

GoodBad

[Previous PageOpenAIAdapter](https://docs.copilotkit.ai/reference/v1/classes/llm-adapters/OpenAIAdapter)[Next PageAnthropicAdapter](https://docs.copilotkit.ai/reference/v1/classes/llm-adapters/AnthropicAdapter)
