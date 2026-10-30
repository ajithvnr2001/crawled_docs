---
url: https://docs.sarvam.ai/api/token-factory/models/
title: Open-Weight Models | Sarvam API Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-30T06:37:14.315015+00:00
---

# Open-Weight Models | Sarvam API Docs

> Source: https://docs.sarvam.ai/api/token-factory/models/

Skip to navigation

On this page

  * Choose a model
  * Quickstart
  * Common patterns
  * Reasoning
  * Troubleshooting
  * Production tips
  * Platform details
  * Next steps



Scroll to top

[Token Factory (Open-Weight)](https://docs.sarvam.ai/api/token-factory)

# Open-Weight Models

Ask a question|Copy page|[View as Markdown](https://docs.sarvam.ai/api/token-factory/models.md "View this page as plain text")|More actions

This page is for Model APIs.

Run leading **open-weight models** on Sarvam infrastructure through the same OpenAI-compatible `/v2` API, with your existing Sarvam API key and credits. Switching models is a one-line change to the `model` field.

GLM-5.3, GLM-5.3 Flash, and Gemma 4 31B are generally available. DeepSeek V4.1 Flash 1017, DeepSeek V4 Pro, Kimi K3, MiMo V2.6 Flash, and MiMo V2.6 Pro are in [beta](https://docs.sarvam.ai/api-reference/beta-apis).

## Choose a model

Pick a use case, or filter by status and input type. Click a model ID to copy it.

I needCoding and agentsLowest costFastest answersReasoning on images

AllGenerally availableBeta

AcceptsImageVideoAudio

Showing 8 of 8 models

Sort by price

[GLM-5.3 →](https://docs.sarvam.ai/api/token-factory/models/glm-5-3)GA`glm5.3`Copy

Software engineering and long-horizon agents.

Context
    1M

Reasoning
    On, can't turn off

Input
    Text

₹ per 1M in / out
    ₹126 / ₹390

[GLM-5.3 Flash →](https://docs.sarvam.ai/api/token-factory/models/glm-5-3-flash)GA`glm5.3-flash`Copy

Faster GLM-5.3 with image input.

Context
    1M

Reasoning
    On, can't turn off

Input
    TextImage

₹ per 1M in / out
    ₹13.5 / ₹45

[Gemma 4 31B →](https://docs.sarvam.ai/api/token-factory/models/gemma-4-31b)GA`gemma4`Copy

Fast direct answers and image understanding.

Context
    256K

Reasoning
    Off by default

Input
    TextImage

₹ per 1M in / out
    ₹35 / ₹90

[DeepSeek V4.1 Flash 1017 →](https://docs.sarvam.ai/api/token-factory/models/deepseek-v4.1-flash-1017)Beta`deepseekv4.1-flash-1017`Copy

Low-cost reasoning for long documents and agents.

Context
    1M

Reasoning
    On, can turn off

Input
    TextImage

₹ per 1M in / out
    ₹25 / ₹105

[DeepSeek V4 Pro →](https://docs.sarvam.ai/api/token-factory/models/deepseek-v4-pro)Beta`deepseekv4-pro`Copy

Larger DeepSeek V4 for harder text reasoning.

Context
    1M

Reasoning
    On, can turn off

Input
    Text

₹ per 1M in / out
    ₹115 / ₹350

[Kimi K3 →](https://docs.sarvam.ai/api/token-factory/models/kimi-k3)Beta`kimi-k3`Copy

Always-on reasoning with image and video input.

Context
    1M

Reasoning
    On, can't turn off

Input
    TextImageVideo

₹ per 1M in / out
    ₹270 / ₹1,350

[MiMo V2.6 Flash →](https://docs.sarvam.ai/api/token-factory/models/mimo-v2.6-flash)Beta`mimo-v2.6-flash`Copy

Lowest-cost reasoning across text, image, audio, and video.

Context
    1M

Reasoning
    On, can turn off

Input
    TextImageAudioVideo

₹ per 1M in / out
    ₹12.5 / ₹25

[MiMo V2.6 Pro →](https://docs.sarvam.ai/api/token-factory/models/mimo-v2.6-pro)Beta`mimo-v2.6-pro`Copy

Larger MiMo V2.6 for harder multimodal tasks.

Context
    1M

Reasoning
    On, can turn off

Input
    TextImageAudioVideo

₹ per 1M in / out
    ₹40 / ₹80

Prices are in ₹ per 1M tokens; reasoning is billed as output. See [Pricing](https://docs.sarvam.ai/api/getting-started/pricing). Each model’s reasoning default, and how to turn it off, is under [Reasoning](https://docs.sarvam.ai/api/token-factory/models#reasoning).

Every model supports tool calling, streaming, and structured output (`response_format`). Support for log probabilities, multiple choices (`n` > 1), and other parameters varies by model — see each model’s own Supported Parameters table, or [V2 feature support](https://docs.sarvam.ai/api/token-factory/chat-completions#v2-feature-support) for the full matrix.

###### All models as a table

Model| Context| Input| ₹ per 1M in / out  
---|---|---|---  
[GLM-5.3](https://docs.sarvam.ai/api/token-factory/models/glm-5-3)  
`glm5.3`| 1M| Text| 126 / 390  
[GLM-5.3 Flash](https://docs.sarvam.ai/api/token-factory/models/glm-5-3-flash)  
`glm5.3-flash`| 1M| Text, image| 13.5 / 45  
[Gemma 4 31B](https://docs.sarvam.ai/api/token-factory/models/gemma-4-31b)  
`gemma4`| 256K| Text, image| 35 / 90  
[DeepSeek V4.1 Flash 1017](https://docs.sarvam.ai/api/token-factory/models/deepseek-v4.1-flash-1017) (beta)  
`deepseekv4.1-flash-1017`| 1M| Text, image| 25 / 105  
[DeepSeek V4 Pro](https://docs.sarvam.ai/api/token-factory/models/deepseek-v4-pro) (beta)  
`deepseekv4-pro`| 1M| Text| 115 / 350  
[Kimi K3](https://docs.sarvam.ai/api/token-factory/models/kimi-k3) (beta)  
`kimi-k3`| 1M| Text, image, video| 270 / 1,350  
[MiMo V2.6 Flash](https://docs.sarvam.ai/api/token-factory/models/mimo-v2.6-flash) (beta)  
`mimo-v2.6-flash`| 1M| Text, image, audio, video| 12.5 / 25  
[MiMo V2.6 Pro](https://docs.sarvam.ai/api/token-factory/models/mimo-v2.6-pro) (beta)  
`mimo-v2.6-pro`| 1M| Text, image, audio, video| 40 / 80  
  
  * **Coding and agents:** `glm5.3`, the strongest reasoning
  * **Lowest cost:** `mimo-v2.6-flash`, the lowest per-token price
  * **Fastest answers, with image input:** `gemma4`, which skips reasoning by default
  * **Reasoning on images:** `glm5.3-flash` or `kimi-k3`



## Quickstart

[1](https://docs.sarvam.ai/api/token-factory/models#get-an-api-key)

### Get an API key

Create an API key in the [dashboard](https://indus.sarvam.ai/key-management?ref=docs).

[2](https://docs.sarvam.ai/api/token-factory/models#set-your-key)

### Set your key
    
    
    export SARVAM_API_KEY="your-api-key"

[3](https://docs.sarvam.ai/api/token-factory/models#make-your-first-call)

### Make your first call

Open-weight models are served on `POST /v2/chat/completions`. Pick your SDK:

###### Python (Sarvam SDK)

###### Python (OpenAI SDK)

###### JavaScript

###### cURL
    
    
    import os
    
    from sarvamai import SarvamAI
    
    client = SarvamAI(api_subscription_key=os.environ["SARVAM_API_KEY"])
    
    response = client.chat.completions_v2(
    
        model="glm5.3",  # or "gemma4", "deepseekv4.1-flash-1017", "kimi-k3", ...
    
        messages=[
    
            {"role": "user", "content": "Summarise the causes of the 2008 financial crisis."}
    
        ],
    
        max_tokens=1000,
    
    )
    
    print(response.choices[0].message.content)

**Already use the OpenAI SDK?** Point `base_url` at `https://api.sarvam.ai/v2` and pass your Sarvam key as `api_key`. The endpoint also accepts `Authorization: Bearer <key>`. Native Sarvam clients use the `api-subscription-key` header. See [Authentication](https://docs.sarvam.ai/api-reference/authentication).

## Common patterns

###### Streaming

###### Reasoning

###### Tool calling

###### Images (Gemma)

Set `stream=True` to receive server-sent events. Reasoning models stream `reasoning_content` deltas first, then the final `content`.
    
    
    stream = client.chat.completions.create(
    
        model="glm5.3",
    
        messages=[{"role": "user", "content": "What is 17 * 23?"}],
    
        reasoning_effort="low",
    
        max_tokens=1000,
    
        stream=True,
    
    )
    
    for chunk in stream:
    
        if not chunk.choices:
    
            continue
    
        delta = chunk.choices[0].delta
    
        if getattr(delta, "reasoning_content", None):
    
            print(delta.reasoning_content, end="", flush=True)  # thinking
    
        if delta.content:
    
            print(delta.content, end="", flush=True)  # answer

## Reasoning

Most models think before answering; Gemma 4 does only when you set an effort. Defaults, and whether thinking can be turned off, differ by model:

Model| Default effort| Turn thinking off  
---|---|---  
`glm5.3`| `max`| Not supported  
`glm5.3-flash`| `high`| Not supported  
`gemma4`| Off; turn it on with `reasoning_effort` (`low` or `high` on Responses)| Off by default  
`deepseekv4.1-flash-1017`| `high`| `reasoning_effort: "none"`  
`deepseekv4-pro`| `high`| `reasoning_effort: "none"` or `thinking: {"type": "disabled"}`  
`kimi-k3`| `max`| Not supported; thinking is always on  
`mimo-v2.6-flash`, `mimo-v2.6-pro`| On| `reasoning_effort: "none"`, `thinking: {"type": "disabled"}`, or `chat_template_kwargs.enable_thinking: false`. Other effort values only switch thinking on  
  
Send `thinking` and `chat_template_kwargs` through `extra_body` in the SDKs. Accepted effort values are listed on each [model page](https://docs.sarvam.ai/api/token-factory/models).

On the Responses API, do **not** send the string `"max"` to `glm5.3` or `glm5.3-flash`. It returns `400`. Omit `reasoning.effort` instead: that gives `max` on `glm5.3` and `high` on `glm5.3-flash`.

Reasoning tokens count toward `max_tokens` and are billed as output. If you see empty `content` with `finish_reason: "length"`, the model spent the whole budget thinking. Raise `max_tokens` or lower the effort. On `glm5.3`, `max_tokens` defaults to `2048`.

## Troubleshooting

Symptom| Likely cause| Fix  
---|---|---  
`403 invalid_api_key_error`| Missing or wrong key header| Check `api-subscription-key` or the Bearer token  
`404 not_found_error`| Unknown or wrongly cased model ID| IDs are case-sensitive. List the models enabled for your key with [`GET /v2/models`](https://docs.sarvam.ai/api-reference/chat/models-v2)  
`400` “This model is currently in beta”| Your key doesn’t have beta access| [Contact us](https://docs.sarvam.ai/api/getting-started/help) to enable beta models for your key  
Empty `content`, `finish_reason: "length"`| Reasoning used the token budget| Raise `max_tokens` or lower `reasoning_effort`  
`400 invalid_request_error` on a specific parameter| Parameter unsupported by this model| Check the model’s own Supported Parameters table  
`402 insufficient_quota_error`| No credits left| Add credits in the [dashboard](https://indus.sarvam.ai/billing?ref=docs)  
`429 rate_limit_exceeded_error` / `model_rate_limit_exceeded_error`, or `503 model_overloaded`| Rate limit, model capacity, or overload| Retry with exponential backoff  
  
## Production tips

###### Retry on 429 and 503

Rate limits and temporary overload are retryable. The OpenAI SDK retries these automatically with backoff when you raise `max_retries`:
    
    
    client = OpenAI(
    
        base_url="https://api.sarvam.ai/v2",
    
        api_key=os.environ["SARVAM_API_KEY"],
    
        max_retries=4,
    
        timeout=120,  # reasoning at high effort can take a while
    
    )

###### Budget tokens for reasoning

Set `max_tokens` well above your expected answer length, at least a few thousand for `high` or `max` effort, because thinking tokens share the same budget.

###### Match effort to the task

Use `low` for extraction, classification and chat. Reserve `high` and `max` for math, debugging and multi-step planning, where extra thinking improves quality at higher latency and cost.

###### Switch models without code changes

Read the model ID from configuration, for example `model=os.environ.get("SARVAM_MODEL", "glm5.3")`, so you can compare models on your own prompts. Only change parameters the target model supports, see the comparison table above.

## Platform details

###### Endpoints and model discovery

  * **Chat:** `POST https://api.sarvam.ai/v2/chat/completions`, see the [API reference](https://docs.sarvam.ai/api-reference/chat/chat-completions-v2).
  * **Responses:** `POST https://api.sarvam.ai/v2/responses`, see the [API reference](https://docs.sarvam.ai/api-reference/responses/create).
  * **Models:** [`GET /v2/models`](https://docs.sarvam.ai/api-reference/chat/models-v2) lists the models enabled for your key. Beta models appear only for keys that have beta access.



###### Billing and rate limits

Usage is metered per token against your Sarvam credits, see [Pricing](https://docs.sarvam.ai/api/getting-started/pricing). Reasoning is billed as output. Limits apply per API key, see [Credits & Rate Limits](https://docs.sarvam.ai/api/getting-started/pricing#rate-limits).

###### Beta models

DeepSeek V4.1 Flash 1017, DeepSeek V4 Pro, Kimi K3, MiMo V2.6 Flash, and MiMo V2.6 Pro are in beta. See [Beta models](https://docs.sarvam.ai/api-reference/beta-apis).

## Next steps

[Chat Completions guideStreaming, tool calling and structured outputs.](https://docs.sarvam.ai/api/token-factory/chat-completions)[Responses APIStateless responses with reasoning and tools.](https://docs.sarvam.ai/api-reference/responses/create)[PricingPer-token rates for every model.](https://docs.sarvam.ai/api/getting-started/pricing)[Migrate from another providerMove from OpenRouter, Fireworks AI, or Together AI.](https://docs.sarvam.ai/api/token-factory/migrations/from-openrouter/overview)

Was this page helpful?

YesNo

[Previous](https://docs.sarvam.ai/api/token-factory)[GLM-5.3Next](https://docs.sarvam.ai/api/token-factory/models/glm-5-3)[Built with](https://buildwithfern.com/?utm_source=others&utm_medium=organic&utm_campaign=fern_indocs_url&utm_content=book_demo&utm_term=docs.sarvam.ai)

  * Getting Started

    * [Welcome](https://docs.sarvam.ai/api/getting-started/welcome)
    * [Quickstart](https://docs.sarvam.ai/api/getting-started/quickstart)
    * [SDKs & Libraries](https://docs.sarvam.ai/api/getting-started/sdks)
    * [Pricing, Credits & Rate Limits](https://docs.sarvam.ai/api/getting-started/pricing)
    * [Talk to us](https://docs.sarvam.ai/api/getting-started/help)
  * [Token Factory (Open-Weight)](https://docs.sarvam.ai/api/token-factory)
    * [Models](https://docs.sarvam.ai/api/token-factory/models)
      * [GLM-5.3](https://docs.sarvam.ai/api/token-factory/models/glm-5-3)
      * [GLM-5.3 Flash](https://docs.sarvam.ai/api/token-factory/models/glm-5-3-flash)
      * [Gemma 4 31B](https://docs.sarvam.ai/api/token-factory/models/gemma-4-31b)
      * [DeepSeek V4.1 Flash 1017Beta](https://docs.sarvam.ai/api/token-factory/models/deepseek-v4.1-flash-1017)
      * [DeepSeek V4 ProBeta](https://docs.sarvam.ai/api/token-factory/models/deepseek-v4-pro)
      * [Kimi K3Beta](https://docs.sarvam.ai/api/token-factory/models/kimi-k3)
      * [MiMo V2.6 FlashBeta](https://docs.sarvam.ai/api/token-factory/models/mimo-v2.6-flash)
      * [MiMo V2.6 ProBeta](https://docs.sarvam.ai/api/token-factory/models/mimo-v2.6-pro)

    * [Chat Completions](https://docs.sarvam.ai/api/token-factory/chat-completions)
    * [Responses API](https://docs.sarvam.ai/api/token-factory/responses-api)
    * How-to

    * Migration Guides

  * Sarvam Models

    * Models

    * Speech to Text

    * Text to Speech

    * Text Processing

    * Document Intelligence

    * Document Translation

    * Dubbing

    * Instant Voice CloningBeta

    * Self-Hosted Deployments

  *     * Integration

    * Developer Tools

  * Cookbook

    * Guides

    * Example Voice Agents

  *     * Migrations

  * Resources

    * [Building for Indian Languages](https://docs.sarvam.ai/api/getting-started/building-for-india)
    * [All Models](https://docs.sarvam.ai/api/getting-started/models)
    * [Errors & Troubleshooting](https://docs.sarvam.ai/api/getting-started/errors-troubleshooting)
    * [Commercial Licensing](https://docs.sarvam.ai/api/getting-started/commercial-licensing)
    * Account & Billing




  * [Welcome](https://docs.sarvam.ai/api/getting-started/welcome)
  * [Quickstart](https://docs.sarvam.ai/api/getting-started/quickstart)
  * [SDKs & Libraries](https://docs.sarvam.ai/api/getting-started/sdks)
  * [Pricing, Credits & Rate Limits](https://docs.sarvam.ai/api/getting-started/pricing)
  * [Talk to us](https://docs.sarvam.ai/api/getting-started/help)
  * [Token Factory (Open-Weight)](https://docs.sarvam.ai/api/token-factory)
  * [Models](https://docs.sarvam.ai/api/token-factory/models)
  * [GLM-5.3](https://docs.sarvam.ai/api/token-factory/models/glm-5-3)
  * [GLM-5.3 Flash](https://docs.sarvam.ai/api/token-factory/models/glm-5-3-flash)
  * [Gemma 4 31B](https://docs.sarvam.ai/api/token-factory/models/gemma-4-31b)
  * [DeepSeek V4.1 Flash 1017](https://docs.sarvam.ai/api/token-factory/models/deepseek-v4.1-flash-1017)
  * [DeepSeek V4 Pro](https://docs.sarvam.ai/api/token-factory/models/deepseek-v4-pro)
  * [Kimi K3](https://docs.sarvam.ai/api/token-factory/models/kimi-k3)
  * [MiMo V2.6 Flash](https://docs.sarvam.ai/api/token-factory/models/mimo-v2.6-flash)
  * [MiMo V2.6 Pro](https://docs.sarvam.ai/api/token-factory/models/mimo-v2.6-pro)
  * [Chat Completions](https://docs.sarvam.ai/api/token-factory/chat-completions)
  * [Responses API](https://docs.sarvam.ai/api/token-factory/responses-api)
  * [List your chat messages](https://docs.sarvam.ai/api/token-factory/how-to/list-your-chat-messages)
  * [Control response randomness](https://docs.sarvam.ai/api/token-factory/how-to/control-response-randomness)
  * [Control response diversity](https://docs.sarvam.ai/api/token-factory/how-to/control-response-diversity)
  * [Adjust the model's thinking level](https://docs.sarvam.ai/api/token-factory/how-to/adjust-the-models-thinking-level)
  * [Encourage new topics in response](https://docs.sarvam.ai/api/token-factory/how-to/encourage-new-topics-in-response)
  * [Reduce repetition words or phrases in response](https://docs.sarvam.ai/api/token-factory/how-to/reduce-repetition-words-or-phrases-in-response)
  * [Get repeatable results](https://docs.sarvam.ai/api/token-factory/how-to/get-repeatable-results)
  * [Control the response length](https://docs.sarvam.ai/api/token-factory/how-to/control-the-response-length)
  * [Control where the model stops](https://docs.sarvam.ai/api/token-factory/how-to/control-where-the-model-stops)
  * [Overview](https://docs.sarvam.ai/api/token-factory/migrations/from-openrouter/overview)
  * [Chat Completion](https://docs.sarvam.ai/api/token-factory/migrations/from-openrouter/chat-completion)
  * [Responses API](https://docs.sarvam.ai/api/token-factory/migrations/from-openrouter/responses-api)
  * [Overview](https://docs.sarvam.ai/api/token-factory/migrations/from-fireworks/overview)
  * [Chat Completion](https://docs.sarvam.ai/api/token-factory/migrations/from-fireworks/chat-completion)
  * [Responses API](https://docs.sarvam.ai/api/token-factory/migrations/from-fireworks/responses-api)
  * [Overview](https://docs.sarvam.ai/api/token-factory/migrations/from-together/overview)
  * [Chat Completion](https://docs.sarvam.ai/api/token-factory/migrations/from-together/chat-completion)
  * [Saaras](https://docs.sarvam.ai/api/api-guides-tutorials/models/saaras)
  * [Bulbul](https://docs.sarvam.ai/api/api-guides-tutorials/models/bulbul)
  * [Sarvam 105B](https://docs.sarvam.ai/api/api-guides-tutorials/models/sarvam-105b)
  * [Mayura](https://docs.sarvam.ai/api/api-guides-tutorials/models/mayura)
  * [Sarvam Translate](https://docs.sarvam.ai/api/api-guides-tutorials/models/sarvam-translate)
  * [Sarvam Vision](https://docs.sarvam.ai/api/api-guides-tutorials/models/sarvam-vision)
  * [Saarika (Deprecated)](https://docs.sarvam.ai/api/getting-started/models/saarika)
  * [Sarvam 30B (Deprecated)](https://docs.sarvam.ai/api/getting-started/models/sarvam-30b)
  * [Sarvam M (Deprecated)](https://docs.sarvam.ai/api/getting-started/models/sarvam-m)
  * [Overview](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/overview)
  * [Which API to Use](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/which-api-to-use)
  * [Rest API](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/rest-api)
  * [Batch API](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/batch-api)
  * [Realtime Streaming](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/realtime-streaming)
  * [Best Practices](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/best-practices)
  * [FAQs](https://docs.sarvam.ai/api/speech-to-text/faq)
  * [Select Output Mode](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/how-to/select-output-mode)
  * [Specify Language Codes](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/how-to/specify-language-codes)
  * [Enable Speaker Diarization](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/how-to/enable-speaker-diarization)
  * [Keyterm Prompting](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/how-to/keyterms)
  * [IVR & Contact Center](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/use-cases/ivr-contact-center)
  * [BFSI Voice Bots](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/use-cases/bfsi-voice-bots)
  * [EdTech](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/use-cases/edtech)
  * [Government Services](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/use-cases/government-services)
  * [Agri & Rural](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/use-cases/agri-rural)
  * [Streaming API](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/streaming-api)
  * [Overview](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/overview)
  * [Voices](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/voices)
  * [Which API to Use](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/which-api-to-use)
  * [Rest API](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/rest-api)
  * [HTTP Stream](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/streaming-api/http-stream)
  * [WebSocket](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/streaming-api/web-socket)
  * [Pronunciation Dictionary](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/pronunciation-dictionary)
  * [Best Practice Guide for Bulbul v4 Flash](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/best-practices)
  * [Best Practices (Bulbul v3)](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/bulbul-v3-best-practices)
  * [Set the Language](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/how-to/set-the-language)
  * [Change the Speaker Voice](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/how-to/change-the-speaker-voice)
  * [Adjust the Tone](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/how-to/adjust-the-tone)
  * [Adjust the Speed](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/how-to/adjust-the-speed)
  * [Adjust the Loudness](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/how-to/adjust-the-loudness)
  * [Set the Sample rate](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/how-to/set-the-sample-rate)
  * [Enable Text Preprocessing](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/how-to/enable-text-preprocessing)
  * [Set audio format for output](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/how-to/set-audio-format-for-output)
  * [Set bitrate for output](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/how-to/set-bitrate-for-output)
  * [Set maximum length for sentence splitting](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/how-to/set-maximum-length-for-sentence-splitting)
  * [Set buffer size to start processing](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/how-to/set-buffer-size-to-start-processing)
  * [IVR & Contact Center](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/use-cases/ivr-contact-center)
  * [BFSI Voice Bots](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/use-cases/bfsi-voice-bots)
  * [EdTech](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/use-cases/edtech)
  * [Government Services](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/use-cases/government-services)
  * [Agri & Rural](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/use-cases/agri-rural)
  * [Overview](https://docs.sarvam.ai/api/api-guides-tutorials/text-processing/overview)
  * [Text Translation](https://docs.sarvam.ai/api/api-guides-tutorials/text-processing/translation)
  * [Transliteration](https://docs.sarvam.ai/api/api-guides-tutorials/text-processing/transliteration)
  * [Language Detection](https://docs.sarvam.ai/api/api-guides-tutorials/text-processing/language-detection)
  * [Overview](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/overview)
  * [Parse](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/how-to/parse)
  * [Extract](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/how-to/extract)
  * [Split](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/how-to/split)
  * [Classify](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/how-to/classify)
  * [Jobs & Errors](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/job-lifecycle)
  * [Languages, Formats & Limits](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/languages-formats-limits)
  * [Overview](https://docs.sarvam.ai/api/api-guides-tutorials/doc-translation/overview)
  * [Set Style Guidelines](https://docs.sarvam.ai/api/api-guides-tutorials/doc-translation/how-to/style-guidelines)
  * [Pick a Genre](https://docs.sarvam.ai/api/api-guides-tutorials/doc-translation/how-to/genre-and-model-tier)
  * [Use Native Numerals](https://docs.sarvam.ai/api/api-guides-tutorials/doc-translation/how-to/native-numerals)
  * [Poll Status and Export Results](https://docs.sarvam.ai/api/api-guides-tutorials/doc-translation/how-to/poll-and-export)
  * [FAQs](https://docs.sarvam.ai/api/api-guides-tutorials/doc-translation/faq)
  * [Use Cases](https://docs.sarvam.ai/api/api-guides-tutorials/doc-translation/use-cases)
  * [Translate a PDF](https://docs.sarvam.ai/api/api-guides-tutorials/doc-translation/guides/translate-a-pdf)
  * [Overview](https://docs.sarvam.ai/api/api-guides-tutorials/dubbing/overview)
  * [Job Lifecycle](https://docs.sarvam.ai/api/api-guides-tutorials/dubbing/job-lifecycle)
  * [Specify Language Codes](https://docs.sarvam.ai/api/api-guides-tutorials/dubbing/how-to/specify-language-codes)
  * [Control Translation Tone](https://docs.sarvam.ai/api/api-guides-tutorials/dubbing/how-to/control-translation-tone)
  * [Choose a Voice](https://docs.sarvam.ai/api/api-guides-tutorials/dubbing/how-to/choose-a-voice)
  * [Choose Export Formats](https://docs.sarvam.ai/api/api-guides-tutorials/dubbing/how-to/choose-export-formats)
  * [FAQs](https://docs.sarvam.ai/api/api-guides-tutorials/dubbing/faq)
  * [Overview](https://docs.sarvam.ai/api/api-guides-tutorials/voice-cloning/overview)
  * [Prepare Reference Audio](https://docs.sarvam.ai/api/api-guides-tutorials/voice-cloning/how-to/prepare-reference-audio)
  * [Clone Across Languages](https://docs.sarvam.ai/api/api-guides-tutorials/voice-cloning/how-to/clone-across-languages)
  * [Choose Audio Formats](https://docs.sarvam.ai/api/api-guides-tutorials/voice-cloning/how-to/choose-audio-formats)
  * [Use Quality Control](https://docs.sarvam.ai/api/api-guides-tutorials/voice-cloning/how-to/use-quality-control)
  * [HTTP Streaming](https://docs.sarvam.ai/api/api-guides-tutorials/voice-cloning/how-to/http-streaming)
  * [WebSocket Streaming](https://docs.sarvam.ai/api/api-guides-tutorials/voice-cloning/how-to/websocket-streaming)
  * [Supported Languages](https://docs.sarvam.ai/api/api-guides-tutorials/voice-cloning/supported-languages)
  * [FAQs](https://docs.sarvam.ai/api/api-guides-tutorials/voice-cloning/faq)
  * [Introduction](https://docs.sarvam.ai/api/self-hosted/introduction)
  * [Managed vs Self-Hosted](https://docs.sarvam.ai/api/self-hosted/hosted-vs-self-hosted)
  * [How it works](https://docs.sarvam.ai/api/self-hosted/architecture)
  * [Get started](https://docs.sarvam.ai/api/self-hosted/sagemaker/get-started)
  * [Speech-to-Text (Saaras v3)](https://docs.sarvam.ai/api/self-hosted/sagemaker/deploy-saaras)
  * [Sarvam Vision](https://docs.sarvam.ai/api/self-hosted/sagemaker/deploy-vision)
  * [Text-to-Speech (Bulbul v3)](https://docs.sarvam.ai/api/self-hosted/sagemaker/deploy-bulbul)
  * [Deploy with Terraform](https://docs.sarvam.ai/api/self-hosted/sagemaker/terraform)
  * [Speech-to-Text](https://docs.sarvam.ai/api/self-hosted/sagemaker/api-saaras)
  * [Sarvam Vision](https://docs.sarvam.ai/api/self-hosted/sagemaker/api-vision)
  * [Text-to-Speech](https://docs.sarvam.ai/api/self-hosted/sagemaker/api-bulbul)
  * [Error handling](https://docs.sarvam.ai/api/self-hosted/sagemaker/errors)
  * [Configure & tune](https://docs.sarvam.ai/api/self-hosted/sagemaker/configure)
  * [Operations](https://docs.sarvam.ai/api/self-hosted/sagemaker/operations)
  * [Limitations](https://docs.sarvam.ai/api/self-hosted/sagemaker/limitations)
  * [Troubleshooting](https://docs.sarvam.ai/api/self-hosted/sagemaker/troubleshooting)
  * [LiveKit](https://docs.sarvam.ai/api/integration/build-voice-agent-with-live-kit)
  * [Pipecat](https://docs.sarvam.ai/api/integration/build-voice-agent-with-pipecat)
  * [Twilio](https://docs.sarvam.ai/api/integration/build-voice-agent-with-twilio)
  * [Exotel](https://docs.sarvam.ai/api/integration/build-voice-agent-with-exotel)
  * [Vobiz](https://docs.sarvam.ai/api/integration/build-voice-agent-with-vobiz)
  * [Vapi](https://docs.sarvam.ai/api/integration/build-voice-agent-with-vapi)
  * [n8n](https://docs.sarvam.ai/api/integration/n8n)
  * [Vercel AI SDK](https://docs.sarvam.ai/api/integration/vercel-ai-sdk)
  * [LangChain](https://docs.sarvam.ai/api/integration/langchain)
  * [LiveKit in Production](https://docs.sarvam.ai/api/integration/livekit-production-best-practices)
  * [Pipecat in Production](https://docs.sarvam.ai/api/integration/pipecat-production-guide)
  * [MCP Server](https://docs.sarvam.ai/api/developer-tools/mcp)
  * [Markdown & llms.txt](https://docs.sarvam.ai/api/developer-tools/llms-txt)
  * [Context7](https://docs.sarvam.ai/api/developer-tools/context7)
  * [Agent Skills](https://docs.sarvam.ai/api/developer-tools/agent-skills)
  * [Call Analytics Pipeline](https://docs.sarvam.ai/api/cookbook/guides/call-analytics-pipeline)
  * [Live Video Transcription](https://docs.sarvam.ai/api/cookbook/guides/live-video-transcription)
  * [Podcast Generator](https://docs.sarvam.ai/api/cookbook/guides/podcast-generator)
  * [WhatsApp Bot](https://docs.sarvam.ai/api/cookbook/guides/whats-app-bot)
  * [Support Voice Notes](https://docs.sarvam.ai/api/cookbook/guides/support-voice-notes)
  * [Collection Agent](https://docs.sarvam.ai/api/cookbook/example-voice-agents/collection-agent)
  * [Government Scheme Agent](https://docs.sarvam.ai/api/cookbook/example-voice-agents/government-scheme-agent)
  * [Tutor Agent](https://docs.sarvam.ai/api/cookbook/example-voice-agents/tutor-agent)
  * [Loan Advisory Agent](https://docs.sarvam.ai/api/cookbook/example-voice-agents/loan-advisory-agent)
  * [Overview](https://docs.sarvam.ai/api/migrations/from-elevenlabs/overview)
  * [Text to Speech](https://docs.sarvam.ai/api/migrations/from-elevenlabs/text-to-speech)
  * [Speech to Text](https://docs.sarvam.ai/api/migrations/from-elevenlabs/speech-to-text)
  * [Instant Voice Cloning](https://docs.sarvam.ai/api/migrations/from-elevenlabs/voice-cloning)
  * [Overview](https://docs.sarvam.ai/api/migrations/from-cartesia/overview)
  * [Text to Speech](https://docs.sarvam.ai/api/migrations/from-cartesia/text-to-speech)
  * [Speech to Text](https://docs.sarvam.ai/api/migrations/from-cartesia/speech-to-text)
  * [Overview](https://docs.sarvam.ai/api/migrations/from-deepgram/overview)
  * [Text to Speech](https://docs.sarvam.ai/api/migrations/from-deepgram/text-to-speech)
  * [Speech to Text](https://docs.sarvam.ai/api/migrations/from-deepgram/speech-to-text)
  * [Overview](https://docs.sarvam.ai/api/migrations/from-gemini/overview)
  * [Chat Completion](https://docs.sarvam.ai/api/migrations/from-gemini/chat-completion)
  * [Text to Speech](https://docs.sarvam.ai/api/migrations/from-gemini/text-to-speech)
  * [Speech to Text](https://docs.sarvam.ai/api/migrations/from-gemini/speech-to-text)
  * [Building for Indian Languages](https://docs.sarvam.ai/api/getting-started/building-for-india)
  * [All Models](https://docs.sarvam.ai/api/getting-started/models)
  * [Errors & Troubleshooting](https://docs.sarvam.ai/api/getting-started/errors-troubleshooting)
  * [Commercial Licensing](https://docs.sarvam.ai/api/getting-started/commercial-licensing)
  * [Organisations & workspaces](https://docs.sarvam.ai/api/platform/organisations-and-workspaces)
  * [Create an organisation](https://docs.sarvam.ai/api/platform/create-an-organisation)
  * [Create a workspace](https://docs.sarvam.ai/api/platform/create-a-workspace)
  * [Invite your team](https://docs.sarvam.ai/api/platform/invite-your-team)
  * [Billing & payments](https://docs.sarvam.ai/api/platform/billing)
  * [Platform FAQ](https://docs.sarvam.ai/api/platform/faq)



  * [Model APIs](https://docs.sarvam.ai/api)
  * [Voice Agents](https://docs.sarvam.ai/voice-agents)
  * [Doc Agents](https://docs.sarvam.ai/docai)
  * [Content Studio](https://docs.sarvam.ai/creative)
  * [Cowork](https://docs.sarvam.ai/cowork)
  * [API Reference](https://docs.sarvam.ai/api-reference)
  * [Changelog](https://docs.sarvam.ai/changelog)


