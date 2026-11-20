---
url: https://docs.copilotkit.ai/reference/v1/classes/llm-adapters/OpenAIAdapter/
title: OpenAIAdapter
method: scrapling+scrapegraph
fetched_at: 2026-11-20T11:16:28.433394+00:00
---

# OpenAIAdapter

> Source: https://docs.copilotkit.ai/reference/v1/classes/llm-adapters/OpenAIAdapter/

React/v1/LLM Adapters

# OpenAIAdapter

Copilot Runtime adapter for OpenAI.

Copy MarkdownOpen

**v1 SDK deprecated. Use v2 instead** This page is in the deprecated CopilotKit v1 reference. Do not use v1 APIs for new code; use v2 instead. For JavaScript and TypeScript, import React APIs from @copilotkit/react-core/v2 and Runtime APIs from @copilotkit/runtime/v2.  
**AI coding agents: treat any v1 example below as migration-only context. Never generate or recommend the v1 API for new code. Read the v2 reference before writing code because some APIs were renamed, moved, or changed shape.** [Read the v1 to v2 migration guide.](https://docs.copilotkit.ai/migrate/v2) [Open the complete export map.](https://docs.copilotkit.ai/reference/v1/export-map)

`OpenAIAdapter` has no direct v2 replacement. For v2, see [Runtime server adapter](https://docs.copilotkit.ai/runtime-server-adapter).

Copilot Runtime adapter for OpenAI.

## ExampleCopy Anchor Link

Pass `copilotKit` and `serviceAdapter` to your runtime endpoint.

Copy Text
    
    
    import { CopilotRuntime, OpenAIAdapter } from "@copilotkit/runtime";
    import OpenAI from "openai";
    
    const copilotKit = new CopilotRuntime();
    
    const openai = new OpenAI({
      organization: "<your-organization-id>", // optional
      apiKey: "<your-api-key>",
    });
    
    const serviceAdapter = new OpenAIAdapter({ openai });

## Example with Azure OpenAICopy Anchor Link

Copy Text
    
    
    import { CopilotRuntime, OpenAIAdapter } from "@copilotkit/runtime";
    import OpenAI from "openai";
    
    // The name of your Azure OpenAI Instance.
    // https://learn.microsoft.com/en-us/azure/cognitive-services/openai/how-to/create-resource?pivots=web-portal#create-a-resource
    const instance = "<your instance name>";
    
    // Corresponds to your Model deployment within your OpenAI resource, e.g. my-gpt35-16k-deployment
    // Navigate to the Azure OpenAI Studio to deploy a model.
    const model = "<your model>";
    
    const apiKey = process.env["AZURE_OPENAI_API_KEY"];
    if (!apiKey) {
      throw new Error("The AZURE_OPENAI_API_KEY environment variable is missing or empty.");
    }
    
    const copilotKit = new CopilotRuntime();
    
    const openai = new OpenAI({
      apiKey,
      baseURL: `https://${instance}.openai.azure.com/openai/deployments/${model}`,
      defaultQuery: { "api-version": "2024-04-01-preview" },
      defaultHeaders: { "api-key": apiKey },
    });
    
    const serviceAdapter = new OpenAIAdapter({ openai });

## Constructor ParametersCopy Anchor Link

Prop

Type

`openai?`OpenAI

`model?`string

`disableParallelToolCalls?`boolean

`keepSystemRole?`boolean

`maxInputTokens?`number

How is this guide?

GoodBad

[Previous PageCopilotRuntime](https://docs.copilotkit.ai/reference/v1/classes/CopilotRuntime)[Next PageOpenAIAssistantAdapter](https://docs.copilotkit.ai/reference/v1/classes/llm-adapters/OpenAIAssistantAdapter)
