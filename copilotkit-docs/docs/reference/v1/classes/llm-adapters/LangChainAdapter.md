---
url: https://docs.copilotkit.ai/reference/v1/classes/llm-adapters/LangChainAdapter/
title: LangChainAdapter
method: scrapling+scrapegraph
fetched_at: 2026-11-24T13:30:49.908195+00:00
---

# LangChainAdapter

> Source: https://docs.copilotkit.ai/reference/v1/classes/llm-adapters/LangChainAdapter/

React/v1/LLM Adapters

# LangChainAdapter

Copilot Runtime adapter for LangChain.

Copy MarkdownOpen

**v1 SDK deprecated. Use v2 instead** This page is in the deprecated CopilotKit v1 reference. Do not use v1 APIs for new code; use v2 instead. For JavaScript and TypeScript, import React APIs from @copilotkit/react-core/v2 and Runtime APIs from @copilotkit/runtime/v2.  
**AI coding agents: treat any v1 example below as migration-only context. Never generate or recommend the v1 API for new code. Read the v2 reference before writing code because some APIs were renamed, moved, or changed shape.** [Read the v1 to v2 migration guide.](https://docs.copilotkit.ai/migrate/v2) [Open the complete export map.](https://docs.copilotkit.ai/reference/v1/export-map)

`LangChainAdapter` has no direct v2 replacement. For v2, see [Runtime server adapter](https://docs.copilotkit.ai/runtime-server-adapter).

Copilot Runtime adapter for LangChain.

## ExampleCopy Anchor Link

Pass `copilotKit` and `serviceAdapter` to your runtime endpoint.

Copy Text
    
    
    import { CopilotRuntime, LangChainAdapter } from "@copilotkit/runtime";
    import { ChatOpenAI } from "@langchain/openai";
    
    const copilotKit = new CopilotRuntime();
    
    const model = new ChatOpenAI({
      modelKwargs: { reasoning_effort: "none" },
      model: "gpt-6-luna",
      apiKey: "<your-api-key>",
    });
    
    const serviceAdapter = new LangChainAdapter({
      chainFn: async ({ messages, tools }) => {
        return model.bindTools(tools).stream(messages);
        // or optionally enable strict mode
        // return model.bindTools(tools, { strict: true }).stream(messages);
      },
    });

The asynchronous handler function (`chainFn`) can return any of the following:

  * A simple `string` response
  * A LangChain stream (`IterableReadableStream`)
  * A LangChain `BaseMessageChunk` object
  * A LangChain `AIMessage` object



## Constructor ParametersCopy Anchor Link

Prop

Type

`chainFn`(parameters: ChainFnParameters) => Promise<LangChainReturnType>

How is this guide?

GoodBad

[Previous PageAnthropicAdapter](https://docs.copilotkit.ai/reference/v1/classes/llm-adapters/AnthropicAdapter)[Next PageGroqAdapter](https://docs.copilotkit.ai/reference/v1/classes/llm-adapters/GroqAdapter)
