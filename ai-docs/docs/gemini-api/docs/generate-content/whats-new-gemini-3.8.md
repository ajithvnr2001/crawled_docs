---
url: https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.8
title: What's new in Gemini 3.8 Flash
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:43:56.491864+00:00
---

# What's new in Gemini 3.8 Flash

> Source: https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.8

[Latest model](https://ai.google.dev/gemini-api/docs/generate-content/latest-model) Other models

Gemini 3.8 Flash (`gemini-3.8-flash`) is our most intelligent Flash model, engineered for long-horizon software engineering, autonomous agents, and complex enterprise workflows.

This guide explains what's new in Gemini 3.8 Flash, API changes, code examples, and migration guidance.

## New model

Model | Model ID | Default thinking level | Pricing | Description  
---|---|---|---|---  
Gemini 3.8 Flash | `gemini-3.8-flash` | `medium` | 3.8 Flash is available through the end of year at an introductory price of $0.75/1M input tokens and $3.75/1M output tokens; see [pricing](https://ai.google.dev/gemini-api/docs/pricing) for more details. | Our most intelligent Flash model, engineered for long-horizon software engineering, autonomous agents, and complex enterprise workflows.  
  
Gemini 3.8 Flash supports a 1M token context window, 64k max output tokens, tunable thinking levels (`low`, `medium`, `high`), and the same suite of built-in tools.

For complete specs, see the [Gemini 3.8 Flash model page](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash). For introductory pricing details, see the pricing section later on this page or the [pricing page](https://ai.google.dev/gemini-api/docs/pricing#gemini-3.8-flash).

## Quickstart

### Python
    
    
    from google import genai
    
    client = genai.Client()
    
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents="Write a three.js script that renders a realistic 3D black hole."
    )
    
    print(response.text)
    

### JavaScript
    
    
    import { GoogleGenAI } from "@google/genai";
    
    const ai = new GoogleGenAI({});
    
    const response = await ai.models.generateContent({
      model: "gemini-3.8-flash",
      contents: "Write a three.js script that renders a realistic 3D black hole.",
    });
    
    console.log(response.text);
    

### REST
    
    
    curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
      -H "x-goog-api-key: $GEMINI_API_KEY" \
      -H 'Content-Type: application/json' \
      -X POST \
      -d '{
        "contents": [{
          "parts": [{"text": "Write a three.js script that renders a realistic 3D black hole."}]
        }]
      }'
    

## What's new in Gemini 3.8 Flash

  * **Long-horizon software engineering:** Delivers strong results on real-world coding benchmarks, complex multi-file refactoring, and deterministic tool execution. See the [evaluation methodology](https://deepmind.google/models/evals-methodology/gemini-3-8-flash/) for details.
  * **Autonomous agents:** Lets you build resilient multi-step planning and tool orchestration workflows, substantially reducing failed loops and errors.
  * **Complex enterprise workflows:** Delivers superior accuracy, deep reasoning, and high factual rigor across demanding domain tasks and large-scale data pipelines.
  * **Default model for Managed Agents:** The default agent for managed agents: the [Antigravity agent](https://ai.google.dev/gemini-api/docs/antigravity-agent), now uses Gemini 3.8 Flash. The [Antigravity SDK](https://antigravity.google/docs/sdk/overview/) also uses Gemini 3.8 Flash by default.
  * **Introductory pricing:** Gemini 3.8 Flash is available at an introductory rate of $0.75/1M input tokens and $3.75/1M output tokens through December 31, 2026. Standard pricing of $1.50/1M input tokens and $7.50/1M output tokens takes effect January 1, 2027.



Gemini 3.8 Flash can use more tokens on longer running and complex tasks, by design. To deliver higher-quality results on difficult, multi-step goals, the model takes smaller reasoning steps, calls tools iteratively, and verifies its work along the way. Not every workflow needs this level of verification. For everyday tasks, you can lower the reasoning effort to reduce token consumption. Alternatively, Gemini 3.6 Flash remains supported.

## Understanding reasoning levels

Gemini 3.8 Flash gives you flexible control over latency and intelligence by adjusting the model's thinking level:

  * **Low thinking effort** : Reduces time-to-answer for latency-critical tasks like incident response pipelines, real-time chat, writing drafts, and fast data analysis.
  * **Medium (default):** Best quality for most tasks. Recommended for complex code and agentic use cases, providing higher first-pass accuracy.
  * **High thinking effort** : Maximizes the model's reasoning and tool orchestration capabilities. Best for deep reasoning, mathematics, and difficult multi-step tasks.



The following example sets `thinking_level` to `medium` for a complex code analysis request:

### Python
    
    
    from google import genai
    from google.genai import types
    
    client = genai.Client()
    
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents="Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(
                thinking_level="medium"  # Balanced reasoning effort for complex tasks
            ),
        ),
    )
    
    print(response.text)
    

### JavaScript
    
    
    import { GoogleGenAI } from "@google/genai";
    
    const ai = new GoogleGenAI({});
    
    const response = await ai.models.generateContent({
      model: "gemini-3.8-flash",
      contents: "Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
      config: {
        thinkingConfig: {
          thinkingLevel: "medium", // Balanced reasoning effort for complex tasks
        },
      },
    });
    
    console.log(response.text);
    

### REST
    
    
    curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
      -H "x-goog-api-key: $GEMINI_API_KEY" \
      -H 'Content-Type: application/json' \
      -X POST \
      -d '{
        "contents": [{
          "parts": [{"text": "Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely."}]
        }],
        "generationConfig": {
          "thinkingConfig": {
            "thinkingLevel": "medium"
          }
        }
      }'
    

## Updated Antigravity agent

## Migration checklist
    
    
      `/gemini-api-dev migrate my app to Gemini 3.8 Flash`
    

### Migrate to gemini-3.8-flash

  * **Update Model ID:** Change your target model string to `gemini-3.8-flash`.
  * **Configure thinking level:** Replace `thinking_budget` with the string enum `thinking_level`. Note that `minimal` is not supported on Gemini 3.8 Flash; choose `low`, `medium` (default), or `high`.
  * **Apply Gemini 3 API parameter changes:** Remove deprecated sampling parameters (`temperature`, `top_p`, `top_k`), `candidate_count` (unsupported in Gemini 3 and later), and prefilled model turns. See [Gemini 3.6 API changes and parameter updates](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.6#api-changes-and-parameter-updates).
  * **Enforce turn validation rules:** Remove prefilled model turns and ensure the final user turn contains non-empty text.
  * **Audit function calling:**
    * Place multimodal assets inside the response payload.
    * Format inline instructions using `\n\n`.
    * If you see `Malformed_Function_Call` errors tied to pre-tool text, see [Workarounds for pre-tool text requirements](https://ai.google.dev/gemini-api/docs/generate-content/function-calling#workarounds-for-pre-tool-text-requirements).
    * Only if using generateContent API: Ensure all `FunctionResponse` objects include `call_id` and `name`.
  * **Baseline Gemini 3 requirements:** For SDK updates and thought signature preservation, see [Thought signatures](https://ai.google.dev/gemini-api/docs/generate-content/thinking#signatures).



## Pricing

Take advantage of introductory pricing across Google AI Studio and Gemini Enterprise Agent Platform through December 31, 2026 for Gemini 3.8 Flash and Gemini 3.6 Flash. Standard pricing takes effect January 1, 2027. For complete pricing tiers, see the [pricing page](https://ai.google.dev/gemini-api/docs/pricing#gemini-3.8-flash).

## Other models

  * [Gemini 4 Argon (Latest)](https://ai.google.dev/gemini-api/docs/generate-content/latest-model)
  * [Gemini 3.6 Flash and 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.6)
  * [See all models](https://ai.google.dev/gemini-api/docs/models)



## What's next

  * Review API specs on the [Models Overview](https://ai.google.dev/gemini-api/docs/models).
  * Explore multi-agent orchestration in the [Interactions API Overview](https://ai.google.dev/gemini-api/docs/interactions-overview).
  * Test and refine prompts in [Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash).


