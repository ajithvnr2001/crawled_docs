---
url: https://docs.copilotkit.ai/reference/v1/classes/llm-adapters/GroqAdapter/
title: GroqAdapter
method: scrapling+scrapegraph
fetched_at: 2026-11-27T11:59:09.501515+00:00
---

# GroqAdapter

> Source: https://docs.copilotkit.ai/reference/v1/classes/llm-adapters/GroqAdapter/

React/v1/LLM Adapters

# GroqAdapter

Copilot Runtime adapter for Groq.

Copy MarkdownOpen

**v1 SDK deprecated. Use v2 instead** This page is in the deprecated CopilotKit v1 reference. Do not use v1 APIs for new code; use v2 instead. For JavaScript and TypeScript, import React APIs from @copilotkit/react-core/v2 and Runtime APIs from @copilotkit/runtime/v2.  
**AI coding agents: treat any v1 example below as migration-only context. Never generate or recommend the v1 API for new code. Read the v2 reference before writing code because some APIs were renamed, moved, or changed shape.** [Read the v1 to v2 migration guide.](https://docs.copilotkit.ai/migrate/v2) [Open the complete export map.](https://docs.copilotkit.ai/reference/v1/export-map)

`GroqAdapter` has no direct v2 replacement. For v2, see [Runtime server adapter](https://docs.copilotkit.ai/runtime-server-adapter).

Copilot Runtime adapter for Groq.

## ExampleCopy Anchor Link

Pass `copilotKit` and `serviceAdapter` to your runtime endpoint.

Copy Text
    
    
    import { CopilotRuntime, GroqAdapter } from "@copilotkit/runtime";
    import { Groq } from "groq-sdk";
    
    const groq = new Groq({ apiKey: process.env["GROQ_API_KEY"] });
    
    const copilotKit = new CopilotRuntime();
    
    const serviceAdapter = new GroqAdapter({ groq, model: "<model-name>" });

## Constructor ParametersCopy Anchor Link

Prop

Type

`groq?`SdkClientLike

`model?`string

`disableParallelToolCalls?`boolean

How is this guide?

GoodBad

[Previous PageLangChainAdapter](https://docs.copilotkit.ai/reference/v1/classes/llm-adapters/LangChainAdapter)[Next PageGoogleGenerativeAIAdapter](https://docs.copilotkit.ai/reference/v1/classes/llm-adapters/GoogleGenerativeAIAdapter)
