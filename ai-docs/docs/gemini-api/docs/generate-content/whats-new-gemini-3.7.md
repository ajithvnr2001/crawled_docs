---
url: https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.7
title: What's new in Gemini 3.7 Flash
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:43:56.038013+00:00
---

# What's new in Gemini 3.7 Flash

> Source: https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.7

[Latest model](https://ai.google.dev/gemini-api/docs/generate-content/latest-model) Other models

Gemini 3.7 Flash (`gemini-3.7-flash`) is a previous-generation Flash model in the Gemini 3 series, now deprecated and automatically routed to [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.8).

This guide is preserved for reference and documents the capabilities and changes introduced in Gemini 3.7 Flash.

## Model overview

Model | Model ID | Default thinking level | Description  
---|---|---|---  
Gemini 3.7 Flash (Deprecated) | `gemini-3.7-flash` | `medium` | Previous-generation Flash model built for coding, agentic workflows, and multi-step execution. Replaced by [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.8).  
  
Gemini 3.7 Flash supports a 1M token context window, 64k max output tokens, tunable thinking levels (`low`, `medium`, `high`), and the same suite of built-in tools as 3.6 Flash.

For complete specs, see the [Gemini 3.7 Flash model page](https://ai.google.dev/gemini-api/docs/models/gemini-3.7-flash).

## Quickstart

### Python
    
    
    from google import genai
    
    client = genai.Client()
    
    response = client.models.generate_content(
        model="gemini-3.7-flash",
        contents="Write a responsive navigation component in React with smooth animations and dark mode toggle."
    )
    
    print(response.text)
    

### JavaScript
    
    
    import { GoogleGenAI } from "@google/genai";
    
    const ai = new GoogleGenAI({});
    
    const response = await ai.models.generateContent({
      model: "gemini-3.7-flash",
      contents: "Write a responsive navigation component in React with smooth animations and dark mode toggle.",
    });
    
    console.log(response.text);
    

### REST
    
    
    curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.7-flash:generateContent" \
      -H "x-goog-api-key: $GEMINI_API_KEY" \
      -H 'Content-Type: application/json' \
      -X POST \
      -d '{
        "contents": [{
          "parts": [{"text": "Write a responsive navigation component in React with smooth animations and dark mode toggle."}]
        }]
      }'
    

## What's new in Gemini 3.7 Flash

  * **Coding and agentic tasks:** Significantly higher quality on real-world software engineering and agentic benchmarks, improving issue resolution and reducing failed agent loops.
  * **Web development and stronger design parity:** Generates higher-fidelity desktop and web application code directly from design mocks, with strong gains in design adherence and in auditing existing codebases against mocks to verify 1:1 design parity.



## Understanding reasoning levels

Gemini 3.7 Flash gives developers flexible control over latency and intelligence by adjusting the model's thinking level:

  * **Low thinking effort** : Reduces time-to-answer for latency-critical tasks like incident response pipelines, real-time chat, writing drafts, and fast data analysis.
  * **Medium (default):** Best quality for most tasks. Recommended for complex code and agentic use cases, with higher first-pass accuracy.
  * **High thinking effort** : Maximizes the model's ability to think and use tools. Best for complex reasoning, hard math, and difficult coding and agent tasks. Allows extended thoughts and function calls, with higher token consumption and cost.



To configure thinking levels in Gemini 3.7 Flash:

### Python
    
    
    from google import genai
    from google.genai import types
    
    client = genai.Client()
    
    response = client.models.generate_content(
        model="gemini-3.7-flash",
        contents="Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(
                thinking_level="medium"  # Balanced reasoning effort for complex tasks
            ),
        ),
    )
    
    print(response.text)
    

For multi-language code examples (JavaScript, REST) and in-depth reasoning concepts, see [Understanding reasoning levels in Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.8#understanding-reasoning-levels).

## Antigravity agent support

## Other models

  * [Gemini 4 Argon (Latest)](https://ai.google.dev/gemini-api/docs/generate-content/latest-model)
  * [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.8)
  * [Gemini 3.6 Flash and 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.6)
  * [See all models](https://ai.google.dev/gemini-api/docs/models)



## What's next

  * Review API specs on the [Models Overview](https://ai.google.dev/gemini-api/docs/models).
  * Explore multi-agent orchestration in the [Interactions API Guide](https://ai.google.dev/gemini-api/docs/interactions).
  * Test and refine prompts in [Google AI Studio](https://aistudio.google.com/).


