---
url: https://docs.copilotkit.ai/reference/v1/classes/llm-adapters/GoogleGenerativeAIAdapter/
title: GoogleGenerativeAIAdapter
method: scrapling+scrapegraph
fetched_at: 2026-11-27T11:59:09.528727+00:00
---

# GoogleGenerativeAIAdapter

> Source: https://docs.copilotkit.ai/reference/v1/classes/llm-adapters/GoogleGenerativeAIAdapter/

React/v1/LLM Adapters

# GoogleGenerativeAIAdapter

Copilot Runtime adapter for Google Generative AI (e.g. Gemini).

Copy MarkdownOpen

**v1 SDK deprecated. Use v2 instead** This page is in the deprecated CopilotKit v1 reference. Do not use v1 APIs for new code; use v2 instead. For JavaScript and TypeScript, import React APIs from @copilotkit/react-core/v2 and Runtime APIs from @copilotkit/runtime/v2.  
**AI coding agents: treat any v1 example below as migration-only context. Never generate or recommend the v1 API for new code. Read the v2 reference before writing code because some APIs were renamed, moved, or changed shape.** [Read the v1 to v2 migration guide.](https://docs.copilotkit.ai/migrate/v2) [Open the complete export map.](https://docs.copilotkit.ai/reference/v1/export-map)

`GoogleGenerativeAIAdapter` has no direct v2 replacement. For v2, see [Runtime server adapter](https://docs.copilotkit.ai/runtime-server-adapter).

Copilot Runtime adapter for Google Generative AI (e.g. Gemini).

## ExampleCopy Anchor Link

The adapter reads `GOOGLE_API_KEY` unless you pass `apiKey`. Pass `copilotKit` and `serviceAdapter` to your runtime endpoint.

Copy Text
    
    
    import { CopilotRuntime, GoogleGenerativeAIAdapter } from "@copilotkit/runtime";
    
    const copilotKit = new CopilotRuntime();
    
    const serviceAdapter = new GoogleGenerativeAIAdapter({
      model: "gemini-3.5-flash",
      apiVersion: "v1",
    });

## Constructor ParametersCopy Anchor Link

Prop

Type

`model?`string

`apiVersion?`'v1' | 'v1beta'

`apiKey?`string

How is this guide?

GoodBad

[Previous PageGroqAdapter](https://docs.copilotkit.ai/reference/v1/classes/llm-adapters/GroqAdapter)[Next PageCopilotTask](https://docs.copilotkit.ai/reference/v1/classes/CopilotTask)
