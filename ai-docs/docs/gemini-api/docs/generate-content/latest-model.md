---
url: https://ai.google.dev/gemini-api/docs/generate-content/latest-model/
title: What's new in Gemini 4 Argon
method: scrapling+scrapegraph
fetched_at: 2026-10-27T09:34:32.579970+00:00
---

# What's new in Gemini 4 Argon

> Source: https://ai.google.dev/gemini-api/docs/generate-content/latest-model/

Gemini 4 Argon (`gemini-4-argon`) is our latest, most capable model. It can reason longer on hard problems for better results on complex coding, agentic, math, and science tasks. Gemini 4 Argon is available through the Gemini API and in Google AI Studio.

Gemini 4 Argon supports a unified 1M input-output token limit, long decode up to 1M tokens, and tunable thinking levels (`low`, `medium`, `high`).

[ experiment Try it in AI Studio Build apps from scratch with Gemini 4 Argon and AI Studio.  ](https://aistudio.google.com/apps?model=gemini-4-argon) [ smart_toy App Gallery Play and remix apps, built with Gemini 4 Argon.  ](https://aistudio.google.com/learn/gemini-4-argon-showcase) [ rocket_launch Get started Get started with Gemini 4 Argon with starter prompts.  ](https://aistudio.google.com/learn/gemini-4-argon)

This guide explains what's new in Gemini 4 Argon, API changes, code examples, and migration guidance.

## New model

Model | Model ID | Default thinking level | Pricing | Description  
---|---|---|---|---  
Gemini 4 Argon | `gemini-4-argon` | `medium` | Available through Nov 30, 2026 at an introductory price of $2/1M input tokens and $10/1M output tokens ($4/1M input and $20/1M output thereafter). See [pricing](https://ai.google.dev/gemini-api/docs/pricing) for details. | Our most capable model, built to solve the hardest problems with depth and precision across real-world software engineering and knowledge work tasks.  
  
## Quickstart

Use the following example to send a request to `gemini-4-argon` with the recommended default `thinking_level` (`medium`) and a 64K output token limit:

### Python
    
    
    pip install -U "google-genai>=2.30.1"
    
    
    
    from google import genai
    from google.genai import types
    
    client = genai.Client()
    
    response = client.models.generate_content(
        model="gemini-4-argon",
        contents="Write a three.js script that renders a realistic 3D black hole with gravitational lensing.",
        config=types.GenerateContentConfig(
            max_output_tokens=65536,
            thinking_config=types.ThinkingConfig(thinking_level="medium"),
        ),
    )
    
    print(response.text)
    

### JavaScript
    
    
    npm install "@google/genai@>=2.29.1"
    
    
    
    import { GoogleGenAI } from "@google/genai";
    
    const ai = new GoogleGenAI({});
    
    const response = await ai.models.generateContent({
      model: "gemini-4-argon",
      contents: "Write a three.js script that renders a realistic 3D black hole with gravitational lensing.",
      config: {
        maxOutputTokens: 65536,
        thinkingConfig: {
          thinkingLevel: "medium",
        },
      },
    });
    
    console.log(response.text);
    

### REST
    
    
    curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-4-argon:generateContent" \
      -H "x-goog-api-key: $GEMINI_API_KEY" \
      -H 'Content-Type: application/json' \
      -X POST \
      -d '{
        "contents": [{
          "parts": [{"text": "Write a three.js script that renders a realistic 3D black hole with gravitational lensing."}]
        }],
        "generationConfig": {
          "maxOutputTokens": 65536,
          "thinkingConfig": {
            "thinkingLevel": "medium"
          }
        }
      }'
    

## What's new in Gemini 4 Argon

  * **Unified 1M input-output token limit:** Input, thinking, and output tokens share a single 1M-token window, with a 32K per-request cap for non-streaming calls and a 64K per-stream cap for streaming calls.
  * **Long decode up to 1M tokens:** The model can generate past the per-request cap, up to 1M tokens minus your input. The latest Google GenAI SDKs continue for you by default.
  * **Agentic video understanding (GA):** [Agentic video understanding](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding#agentic-video-understanding) is now generally available.
  * **Supported in Managed Agents:** The [Antigravity agent](https://ai.google.dev/gemini-api/docs/antigravity-agent) in Gemini Managed Agents now supports Gemini 4 Argon.



For more details, see the [Gemini 4 Argon model page](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon). For pricing details, see the [pricing page](https://ai.google.dev/gemini-api/docs/pricing#gemini-4-argon).

## Larger output and long decode

When a task requires deep reasoning, Gemini 4 Argon can think longer and work harder to finish complex math, science, and coding problems in a single generation.

  * **Unified 1M input-output token limit:** Argon can use up to 1M tokens, minus your input tokens, for thinking and output combined.
  * **Thinking tokens count toward`max_output_tokens`:** On hard tasks, the model uses more of your `max_output_tokens` budget to reach a better answer. Use `thinking_level` to control token use.
  * **Per-request caps (64K streaming / 32K non-streaming):** One streaming request returns up to 65,536 tokens. One non-streaming request returns up to 32,768 tokens, down from 65,536 on Gemini 3.x. For REST calls, these caps are also the defaults.



The latest Google GenAI SDKs run long decode for you by default. Use Python `google-genai` 2.30.1 or higher, or JavaScript `@google/genai` 2.29.1 or higher.

In these versions, `automatic_continuation` is `True` by default, so you do not need to set it. When you set `max_output_tokens` above the per-request cap, `generate_content` and `generate_content_stream` automatically continue across requests until the model finishes or reaches `max_output_tokens`, returning one combined response.
    
    
    response = client.models.generate_content(
        model="gemini-4-argon",
        contents="Write a complete, rigorous proof of the prime number theorem.",
        config=types.GenerateContentConfig(
            max_output_tokens=262144,
            thinking_config=types.ThinkingConfig(thinking_level="high"),
            automatic_continuation=True,  # Default.
        ),
    )
    

To run the loop yourself, set `automatic_continuation=False`. If you call REST or use an older SDK, requests stop at the per-request cap. For REST loops, third-party frameworks, token counting, and when to use long decode, see the [long decode guide](https://ai.google.dev/gemini-api/docs/generate-content/long-decode).

### Setting output token limits

`max_output_tokens` sets the total thinking and output tokens for a generation, including all continuation requests. Set it high enough that thinking does not cut the answer short. Set it low enough to limit spend when a hard prompt uses all of it.

Use the following guidance as a starting point:

  * **Standard tasks:** Keep the default.
  * **Existing apps with a limit lower than 32K:** Raise `max_output_tokens` to 32,768. To use fewer tokens, lower `thinking_level`.
  * **Tasks that used more than 32K tokens before:** Set `max_output_tokens` to 65,536.
  * **Complex reasoning and coding:** Set `max_output_tokens` to 131,072 or 262,144, up to 1,048,576 minus your input tokens.



If a request uses all of `max_output_tokens`, it returns `finish_reason: "MAX_TOKENS"` and includes a `continuation_token`. You can resume or start again.

  * **Resume from the checkpoint:** Send the original request with the latest `continuation_token` and a higher `max_output_tokens`. If you do not raise `max_output_tokens`, the request returns `400 INVALID_ARGUMENT`.
  * **Start again:** Send the original request with a higher `max_output_tokens` and no `continuation_token`.



### Understanding thinking levels

The [thinking level](https://ai.google.dev/gemini-api/docs/generate-content/thinking) is your main control over quality, latency, and token use in Gemini 4 Argon:

Thinking level | Token use | When to use  
---|---|---  
`low` | Fewest tokens, lowest latency | Simpler tasks and cost-sensitive work. Also works for analysis and writing tasks that need light thinking. Quality can drop on hard tasks.  
`medium` (default) | Balanced | Recommended for most tasks, including complex code and agentic use cases.  
`high` | Most tokens, slowest first token | Complex reasoning, hard math and science, and the most difficult code or agent tasks. Pairs well with long decode for long outputs.  
  
Run your evaluations at all three levels with a high `max_output_tokens` so the limit doesn't cut answers short. Then pick the lowest `thinking_level` that meets your quality bar.

## Migration checklist
    
    
      `/gemini-api-dev migrate my app to Gemini 4 Argon`
    

### Migrate to gemini-4-argon

  * **Update the model ID:** Change your model string to `gemini-4-argon`.
  * **Set`max_output_tokens` explicitly:** The default is 64K for streaming and SDK calls, and 32K for non-streaming REST calls.
  * **Raise caps lower than 32K:** Raise any cap lower than 32K to at least 32,768. Use `thinking_level` to reduce token spend.
  * **Plan for long decode:** For tasks above the per-request cap, use the latest SDK or add a `continuation_token` loop.
  * **Replace`thinking_budget` with `thinking_level`:** `thinking_budget` still works and maps to the nearest `thinking_level`, but it returns a warning. Test your workload at `low`, `medium`, and `high`.
  * **Move off explicit context caching:** Explicit caching (`cachedContents` / `caches.create`) is not supported on Gemini 4 Argon and returns an error. Remove calls that create or pass `cached_content` in `GenerateContentConfig`. [Implicit caching](https://ai.google.dev/gemini-api/docs/generate-content/caching) is enabled by default for prompts of at least 4,096 tokens and discounts cached input tokens by 95% on cache hits.
  * **Remove deprecated parameters:** Remove `temperature`, `top_p`, `top_k`, and `candidate_count` from requests. If provided, sampling parameters are ignored.
  * **Increase client timeouts:** Set HTTP client timeouts to at least 20 minutes per call.
  * **Preserve thought signatures:** Pass the full conversation history, including [thought signatures](https://ai.google.dev/gemini-api/docs/generate-content/thinking#signatures), in multi-turn and function-calling requests.
  * **Review your cost estimates:** Every token the model processes is billed, including internal tool system instructions and function declarations when using grounding (see Pricing).



## Pricing

Gemini 4 Argon is available at introductory pricing through November 30, 2026:

  * **Input tokens:** $2.00 per 1M tokens ($4.00 starting December 1, 2026) 
    * **Cached input tokens:** Implicit caching discounts cached input by 95%, to $0.10 per 1M tokens ($0.20 starting December 1, 2026).
  * **Output tokens, including thinking tokens:** $10.00 per 1M tokens ($20.00 starting December 1, 2026)



Every token the model processes is counted and billed, including thinking tokens and internal tool system instructions and function declarations when using grounding. Grounding with Google Search also remains billed per query.

Gemini 4 Argon is not available on the Free tier. For complete pricing tiers, see the [pricing page](https://ai.google.dev/gemini-api/docs/pricing#gemini-4-argon).

## Other models

  * [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.8)
  * [Gemini 3.6 Flash and 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.6)
  * [See all models](https://ai.google.dev/gemini-api/docs/models)



## What's next

  * Read the [long decode developer guide](https://ai.google.dev/gemini-api/docs/generate-content/long-decode) for full streaming, reconnection, and token-counting patterns.
  * Learn how thinking levels and thought summaries work in the [thinking guide](https://ai.google.dev/gemini-api/docs/generate-content/thinking).
  * Test Gemini 4 Argon in [Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon).


