---
url: https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.5
title: What's new in Gemini 3.5 Flash
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:43:55.329621+00:00
---

# What's new in Gemini 3.5 Flash

> Source: https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.5

[Latest model](https://ai.google.dev/gemini-api/docs/generate-content/latest-model) Other models

Gemini 3.5 Flash (`gemini-3.5-flash`) is a deprecated earlier-generation Flash model in the Gemini 3 series. Requests to `gemini-3.5-flash` are automatically routed to [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.6). For our newest Flash model, see [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/generate-content/latest-model).

This guide is preserved for historical reference and documents the baseline Gemini 3.x API changes and parameter recommendations.

## Model overview

Model | Model ID | Status  
---|---|---  
Gemini 3.5 Flash | `gemini-3.5-flash` | **Deprecated** (automatically routed to [`gemini-3.6-flash`](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.6)).  
  
Gemini 3.5 Flash supported the 1M token context window, 65k max output tokens, thinking, and the same set of tools and platform features as Gemini 3 Flash, including [Computer Use (Preview)](https://ai.google.dev/gemini-api/docs/computer-use). For complete specs, see the [models overview](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash).

## Quickstart

All examples in this guide use the GenerateContent API. The Interactions API is also supported; the same configuration options and recommendations apply.

### Python
    
    
    from google import genai
    
    client = genai.Client()
    
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents="Explain how parallel agentic execution works in three sentences.",
    )
    print(response.text)
    

### JavaScript
    
    
    import { GoogleGenAI } from "@google/genai";
    
    const ai = new GoogleGenAI({});
    
    async function main() {
      const response = await ai.models.generateContent({
        model: "gemini-3.5-flash",
        contents: "Explain how parallel agentic execution works in three sentences.",
      });
      console.log(response.text);
    }
    
    main();
    

### REST
    
    
    curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
      -H "x-goog-api-key: $GEMINI_API_KEY" \
      -H 'Content-Type: application/json' \
      -X POST \
      -d '{
        "contents": [{
          "parts": [{"text": "Explain how parallel agentic execution works in three sentences."}]
        }]
      }'
    

## What's new

  * **Sustained performance:** Optimized for agentic and coding tasks at scale.
  * **Agentic execution:** Sub-agent deployment, problem solving, and rapid agentic loops at scale.
  * **Coding:** Iterative coding cycles, rapid exploration, and prototyping to test alternate paths and dynamically explore solutions.
  * **Long horizon:** Multi-step workflows and tool use at scale.
  * **Thought preservation:** The model maintains intermediate reasoning across multi-turn conversations automatically. No API changes needed.
  * **New default effort level:** Default thinking effort changed from `high` to `medium`. See New default effort level for details.
  * **Improved`low` thinking:** `low` is significantly improved for code and agentic tasks that require fewer steps, offering strong quality at lower latency and cost.



### Choosing the right Flash model

Since `gemini-3.5-flash` is deprecated and automatically routed to `gemini-3.6-flash`, we recommend migrating to one of the following active models:

  * **Gemini 3.8 Flash** : Our latest and most intelligent Flash model for complex coding and agentic workflows. See the [Gemini 3.8 Flash guide](https://ai.google.dev/gemini-api/docs/generate-content/latest-model).
  * **Gemini 3.6 Flash** : Direct replacement for `gemini-3.5-flash` with reduced token usage and lower output pricing. See the [Gemini 3.6 Flash and 3.5 Flash-Lite guide](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.6).
  * **Gemini 3.5 Flash-Lite / Gemini 3.1 Flash-Lite** : For low-cost, high-volume tasks that don't require full Flash reasoning depth, use [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite) or [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite).



## Behavioral changes

### New default effort level: `medium`

The default thinking effort is now **`medium`** , changed from `high` in Gemini 3 Flash Preview. `medium` yields very good results across a wide range of tasks while being faster and more cost-efficient. For complex problems, `high` encourages the model to think more deeply.

Effort level | When to use  
---|---  
`minimal` | Optimized for response speed. Chat-like use cases, quick factual answers, simpler tool calls.  
`low` | Code and agentic tasks that require lower latency and fewer steps. Also works well for analysis and writing tasks that require some thinking.  
**`medium` (default)** | **Best quality for most tasks. Recommended for complex code and agentic use cases.**  
`high` | Maximizes the model's ability to think and use tools. Best for complex reasoning, hard math, and the most difficult code or agent tasks. Allows extended thoughts and function calls.  
  
To override the default, set `thinking_level` in your config:

### Python
    
    
    from google import genai
    from google.genai import types
    
    client = genai.Client()
    
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents="Prove that the square root of 2 is irrational.",
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_level="high")
        ),
    )
    
    print(response.text)
    

### JavaScript
    
    
    import { GoogleGenAI } from "@google/genai";
    
    const ai = new GoogleGenAI({});
    
    async function main() {
      const response = await ai.models.generateContent({
        model: "gemini-3.5-flash",
        contents: "Prove that the square root of 2 is irrational.",
        config: {
          thinkingConfig: {
            thinkingLevel: "HIGH",
          },
        },
      });
      console.log(response.text);
    }
    
    main();
    

### REST
    
    
    curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
      -H "x-goog-api-key: $GEMINI_API_KEY" \
      -H 'Content-Type: application/json' \
      -X POST \
      -d '{
        "contents": [{
          "parts": [{"text": "Prove that the square root of 2 is irrational."}]
        }],
        "generationConfig": {
          "thinkingConfig": {
            "thinkingLevel": "HIGH"
          }
        }
      }'
    

The following table shows which thinking levels are supported per model:

Thinking Level | Gemini 3.5 Flash | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | Description  
---|---|---|---|---|---  
**`minimal`** | Supported | Not supported | Supported (Default) | Supported | Matches the "no thinking" setting for most queries. Note, `minimal` does not guarantee that thinking is off, the model may reason very minimally for complex tasks.  
**`low`** | Supported | Supported | Supported | Supported | Minimizes latency and cost.  
**`medium`** | Supported (Default) | Supported | Supported | Supported | Balanced thinking for most tasks.  
**`high`** | Supported (Dynamic) | Supported (Default, Dynamic) | Supported (Dynamic) | Supported (Default, Dynamic) | Maximizes reasoning depth.  
  
### Thought preservation

The model maintains intermediate reasoning across multi-turn conversations automatically. When present in the conversation history, reasoning context carries forward, which improves performance on complex multi-step tasks like iterative debugging and code refactoring. No API changes needed:

  * **Interactions API** : Thoughts are already preserved automatically. No change in behavior.
  * **GenerateContent API** : Beginning with Gemini 3.5 Flash, the model uses reasoning context from all previous turns when thought signatures are present in the conversation history. To enable this, pass the full, unmodified conversation history (including [thought signatures](https://ai.google.dev/gemini-api/docs/thought-signatures)) in `contents`. The SDKs handle this automatically.



## Parameter updates and best practices in Gemini 3.x

The following apply to **all Gemini 3.x models** , including Gemini 3.5 Flash.

  * **`temperature`, `top_p`, `top_k`**: we strongly recommend not changing the default values. Gemini 3's reasoning capabilities are optimized for the default settings.
  * Use `thinking_level` instead of `thinking_budget`.
  * **Function calling response matching** : `id`, `name`, and response count must match the preceding calls.
  * **Multimodal function responses** : include multimodal content inside the function response, not outside it.
  * **Inline instructions in function responses** : append to the function response text, not as separate parts.
  * **Reduce unnecessary tool calls** : Use lower thinking levels or experiment with system instructions to reduce tool calls in agentic workflows.



See the sections below for how to update your code.

### Sampling parameters (no longer recommended)

`temperature`, `top_p`, and `top_k` are no longer recommended for all Gemini 3.x models. Gemini 3's reasoning capabilities are optimized for the default settings. **Remove these parameters from all requests.**
    
    
    # ⚠️ Remove these parameters (not recommended)
    config = types.GenerateContentConfig(
        temperature=0.7,
        top_p=0.9,
        top_k=40
    )
    

To ensure determinism, we recommend defining a system instruction with explicit rules for your specific use case.

### `thinking_budget` (no longer recommended)

The raw numeric `thinking_budget` parameter is no longer recommended across all Gemini 3.x models. Use the `thinking_level` string enum instead.
    
    
    # ⚠️ Before (not recommended)
    config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=7500)
    )
    
    # ✅ After
    config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="medium")
    )
    

Available values: `minimal`, `low`, `medium` (default), and `high`.

### Function calling: strict response matching

The Interactions API already errors on mismatched function responses. The GenerateContent API does not yet error, but mismatched responses cause the model to return empty responses with `finish_reason: STOP` in most cases. Always follow these conventions:

Requirement | Details  
---|---  
Include `id` | Every `FunctionResponse` must include the `id` from the corresponding `FunctionCall`  
Match `name` | The `name` in the response must match the `name` in the call  
Match counts | Return exactly one `FunctionResponse` for each `FunctionCall` received  
  
### Python
    
    
    # ✅ Include matching id and name in the function response
    final_response = client.models.generate_content(
        model="gemini-3.5-flash",
        config=config,
        contents=[
            *previous_contents,
            response.candidates[0].content,
            types.Content(role="user", parts=[
                types.Part.from_function_response(
                    name=tool_call.name,
                    response={"result": result},
                    id=tool_call.id,
                )
            ]),
        ],
    )
    

### JavaScript
    
    
    // ✅ Include matching id and name in the function response
    const functionResponsePart = {
      functionResponse: {
        name: toolCall.name,
        response: { result: result },
        id: toolCall.id,
      },
    };
    
    const finalResponse = await ai.models.generateContent({
      model: "gemini-3.5-flash",
      contents: [
        ...previousContents,
        { role: "model", parts: [{ functionCall: toolCall }] },
        { role: "user", parts: [functionResponsePart] },
      ],
      config: config,
    });
    

### REST
    
    
    curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
      -H "x-goog-api-key: $GEMINI_API_KEY" \
      -H 'Content-Type: application/json' \
      -X POST \
      -d '{
        "contents": [
          {"role": "user", "parts": [{"text": "..."}]},
          {"role": "model", "parts": [{"functionCall": {"name": "my_function", "args": {...}}}]},
          {"role": "user", "parts": [{"functionResponse": {"name": "my_function", "id": "call_id", "response": {"result": "..."}}}]}
        ]
      }'
    

### Multimodal function responses

We often see clients provide images outside function response. This can lead to unexpected model behavior (e.g. thought leakage) and result in lower quality outputs. Follow the recommendation in [Multimodal Function Responses API docs](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting#multimodal) instead and include multimodal content in the function response parts that you send to the model. The model can process this multimodal content in its next turn to produce a more informed response.

### Python
    
    
    # ✅ Include multimodal content in the function response
    final_response = client.models.generate_content(
        model="gemini-3.5-flash",
        config=config,
        contents=[
            *previous_contents,
            response.candidates[0].content,
            types.Content(role="user", parts=[
                types.Part.from_function_response(
                    name=tool_call.name,
                    response={
                        "result": "instrument.jpg",
                        "image": base64_image_data,
                    },
                    id=tool_call.id,
                )
            ]),
        ],
    )
    

### JavaScript
    
    
    // ✅ Include multimodal content in the function response
    const finalResponse = await ai.models.generateContent({
      model: "gemini-3.5-flash",
      contents: [
        ...previousContents,
        { role: "model", parts: [{ functionCall: toolCall }] },
        {
          role: "user",
          parts: [{
            functionResponse: {
              name: toolCall.name,
              id: toolCall.id,
              response: {
                result: "instrument.jpg",
                image: base64ImageData,
              },
            },
          }],
        },
      ],
      config: config,
    });
    

### Inline instructions in function responses

We often see clients provide additional instructions along with function responses as subsequent `Parts`. This can lead to unexpected model behavior (e.g. thought leakage) and result in lower quality outputs. Instead, append any extra instructions to the end of the function response text separated by two newlines.

### Python
    
    
    # ✅ Append inline instructions to the end of the function response separated by two newlines
    result_text = f"{json.dumps(result)}\n\n<your inline instructions>"
    
    final_response = client.models.generate_content(
        model="gemini-3.5-flash",
        config=config,
        contents=[
            *previous_contents,
            response.candidates[0].content,
            types.Content(role="user", parts=[
                types.Part.from_function_response(
                    name=tool_call.name,
                    response={"result": result_text},
                    id=tool_call.id,
                )
            ]),
        ],
    )
    

### JavaScript
    
    
    // ✅ Append inline instructions to the end of the function response separated by two newlines
    const resultText = `${JSON.stringify(result)}\n\n<your inline instructions>`;
    
    const finalResponse = await ai.models.generateContent({
      model: "gemini-3.5-flash",
      contents: [
        ...previousContents,
        { role: "model", parts: [{ functionCall: toolCall }] },
        {
          role: "user",
          parts: [{
            functionResponse: {
              name: toolCall.name,
              id: toolCall.id,
              response: { result: resultText },
            },
          }],
        },
      ],
      config: config,
    });
    

### Reducing unnecessary tool calls

If you experience an overuse of tool calls, two techniques help minimize them:

  1. **Start by reducing the thinking level** (`medium`, `low`, or `minimal`): Higher thinking levels encourage the model to use more tools to explore and verify, so lowering the level can reduce tool calls.

  2. **Add a system instruction:** If overuse persists after adjusting the thinking level, consider a prompt that restricts tool usage. For example:
         
         You have a limited action budget of <n> tool calls. Use them efficiently.
         




## Gemini 3 family features

Gemini 3.5 Flash inherits all Gemini 3 family capabilities, including Computer Use. Features introduced in Gemini 3 that carry forward:

  * [**Thinking**](https://ai.google.dev/gemini-api/docs/thinking)**:** Encrypted reasoning context preserved across API calls. Automatic in the Interactions API; implicit in GenerateContent.
  * [**Structured outputs with tools**](https://ai.google.dev/gemini-api/docs/structured-output)**:** Combine JSON mode with built-in tools (Search, URL context, code execution, function calling).
  * [**Multimodal function responses**](https://ai.google.dev/gemini-api/docs/function-calling#multimodal)**:** Return images, audio, and other media in function call results.
  * [**Code execution with images**](https://ai.google.dev/gemini-api/docs/code-execution#images)**:** Execute code that processes and generates images.
  * [**Combined tool use**](https://ai.google.dev/gemini-api/docs/tool-combination)**:** Use built-in tools and custom function calling in the same request.
  * [**Media resolution**](https://ai.google.dev/gemini-api/docs/media-resolution)**:** Fine-grained control over token allocation for image, video, and PDF inputs. Gemini 3 models support per-content-item resolution settings (`low`, `medium`, `high`, `ultra_high`) for mixed-fidelity prompts.
  * [**Thought signatures**](https://ai.google.dev/gemini-api/docs/thought-signatures)**:** Encrypted representations of the model's internal reasoning. Required for multi-turn function calling; managed automatically by the official SDKs.



## Prompting best practices

Gemini 3.x models are reasoning models, which changes how you should prompt.

  * **Precise instructions:** Be concise. Gemini 3.x responds best to direct, clear instructions. Verbose or complex prompt engineering techniques designed for older models may cause the model to over-analyze.
  * **Output verbosity:** By default, Gemini 3.x is less verbose and prefers direct, efficient answers. If your use case requires a conversational tone, steer the model explicitly in your prompt (for example, "Explain this as a friendly, talkative assistant").
  * **Context management:** When working with large datasets (such as entire books, codebases, or long videos), place your specific instructions or questions at the end of the prompt, after the data context. Anchor the model's reasoning by starting your question with a phrase like, "Based on the preceding information...".



Learn more about prompt design strategies in the [prompt engineering guide](https://ai.google.dev/gemini-api/docs/prompting-strategies).

## Limitations

  * Image segmentation is not supported in Gemini 3.x. For segmentation workloads, continue using Gemini 2.5 Flash with thinking off, or [Gemini Robotics ER 2](https://ai.google.dev/gemini-api/docs/robotics-overview).



## FAQ

  1. **What is the knowledge cutoff for Gemini 3.5 Flash?** Gemini 3.5 Flash has a knowledge cutoff of January 2025. For more recent information, use the [Search Grounding](https://ai.google.dev/gemini-api/docs/google-search) tool.

  2. **What are the context window limits?** Gemini 3.5 Flash supports a 1 million token input context window and up to 65k output tokens.

  3. **Will my old`thinking_budget` code still work?** Yes, `thinking_budget` is still supported for backward compatibility, but we recommend migrating to `thinking_level` for more predictable performance. Don't use both in the same request.

  4. **Does Gemini 3.5 Flash support the Batch API?** Yes. See the [Batch API](https://ai.google.dev/gemini-api/docs/batch-api) guide for details.

  5. **Is Context Caching supported?** Yes, [Context Caching](https://ai.google.dev/gemini-api/docs/caching) is supported.

  6. **Which tools are supported?** Gemini 3.5 Flash supports [Google Search](https://ai.google.dev/gemini-api/docs/google-search), [Grounding with Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding), [File Search](https://ai.google.dev/gemini-api/docs/file-search), [Code Execution](https://ai.google.dev/gemini-api/docs/code-execution), [URL Context](https://ai.google.dev/gemini-api/docs/url-context), and standard [Function Calling](https://ai.google.dev/gemini-api/docs/function-calling), including [combined tool use](https://ai.google.dev/gemini-api/docs/tool-combination), and [Computer Use](https://ai.google.dev/gemini-api/docs/computer-use).




## Other models

  * [Gemini 3.8 Flash (Latest)](https://ai.google.dev/gemini-api/docs/generate-content/latest-model)
  * [Gemini 3.6 Flash and 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.6)
  * [See all models](https://ai.google.dev/gemini-api/docs/models)



## What's next

  * Learn more about prompt design strategies in the [prompt engineering guide](https://ai.google.dev/gemini-api/docs/prompting-strategies).
  * Get started with the [Gemini 3 Cookbook](https://github.com/google-gemini/cookbook)
  * Learn about [Gemini API optimization and inference](https://ai.google.dev/gemini-api/docs/optimization)


