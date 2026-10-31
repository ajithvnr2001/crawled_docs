---
url: https://docs.sarvam.ai/api/token-factory/migrations/from-fireworks/overview/
title: Migrating from Fireworks AI: Overview | Sarvam API Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-31T06:34:16.605787+00:00
---

# Migrating from Fireworks AI: Overview | Sarvam API Docs

> Source: https://docs.sarvam.ai/api/token-factory/migrations/from-fireworks/overview/

Skip to navigation

On this page

  * Quick start
  * Zero-code switch
  * Base URL and auth
  * Model IDs
  * Models not on Sarvam
  * Media input and request size
  * Errors and rate limits
  * See also



Scroll to top

[Token Factory (Open-Weight)](https://docs.sarvam.ai/api/token-factory)[Migration Guides](https://docs.sarvam.ai/api/token-factory/migrations/from-openrouter/overview)[From Fireworks AI](https://docs.sarvam.ai/api/token-factory/migrations/from-fireworks/overview)

# Migrating from Fireworks AI: Overview

Ask a question|Copy page|[View as Markdown](https://docs.sarvam.ai/api/token-factory/migrations/from-fireworks/overview.md "View this page as plain text")|More actions

This page is for Model APIs.

_Last updated: October 23, 2026_

Fireworks AI and Sarvam’s `/v2` API both speak the OpenAI Chat Completions format, so most migrations are a base URL, key, and model ID change. This page covers those setup changes. The [Chat Completion](https://docs.sarvam.ai/api/token-factory/migrations/from-fireworks/chat-completion) and [Responses API](https://docs.sarvam.ai/api/token-factory/migrations/from-fireworks/responses-api) guides cover request fields, reasoning, tools, and the Fireworks-only features to remove.

## Quick start

Change the client and the model ID. Use the `openai` package you already have, or Sarvam’s own SDK ([SDKs & Libraries](https://docs.sarvam.ai/api/getting-started/sdks)). If you use the Fireworks SDK, the **Before (Fireworks SDK)** option shows that version; the request shape is the same, so you can move to either the `openai` package or Sarvam’s SDK.

###### Python

###### JavaScript

Before (Fireworks)Before (Fireworks SDK)After (OpenAI SDK)After (Sarvam SDK)
    
    
    from openai import OpenAI
    
    client = OpenAI(
    
        api_key="YOUR_FIREWORKS_API_KEY",
    
        base_url="https://api.fireworks.ai/inference/v1",
    
    )
    
    response = client.chat.completions.create(
    
        model="accounts/fireworks/models/kimi-k3",
    
        messages=[{"role": "user", "content": "Hello!"}],
    
    )

For requests made directly over HTTP, change the URL, the auth header, and the model ID:

Before (Fireworks)After (Sarvam)
    
    
    curl https://api.fireworks.ai/inference/v1/chat/completions \
    
      -H "Authorization: Bearer YOUR_FIREWORKS_API_KEY" \
    
      -H "Content-Type: application/json" \
    
      -d '{
    
        "model": "accounts/fireworks/models/glm-5p3-flash",
    
        "messages": [{"role": "user", "content": "Explain UPI in two sentences."}],
    
        "max_tokens": 1000
    
      }'

Sarvam also accepts `Authorization: Bearer <key>`, which is what the `openai` package sends, so you don’t need to change how your client authenticates. Create a key in the [Sarvam dashboard](https://indus.sarvam.ai/key-management?ref=docs).

## Zero-code switch

The `openai` package for Python and JavaScript reads its endpoint and key from the `OPENAI_BASE_URL` and `OPENAI_API_KEY` environment variables when you create the client without them. If your app does that, and reads the model ID from configuration, you can switch without changing code:
    
    
    export OPENAI_BASE_URL="https://api.sarvam.ai/v2"
    
    export OPENAI_API_KEY="YOUR_SARVAM_API_KEY"
    
    
    from openai import OpenAI
    
    client = OpenAI()  # picks up OPENAI_BASE_URL and OPENAI_API_KEY

Then set your configured model to a [Sarvam model ID](https://docs.sarvam.ai/api/token-factory/migrations/from-fireworks/overview#model-ids). If your requests send Fireworks-only fields, remove them as described in the [Chat Completion guide](https://docs.sarvam.ai/api/token-factory/migrations/from-fireworks/chat-completion).

This works with the `openai` package only. If your code uses the Fireworks SDK, switch to the `openai` package first, as in the [quick start](https://docs.sarvam.ai/api/token-factory/migrations/from-fireworks/overview#quick-start).

## Base URL and auth

| Fireworks AI| Sarvam  
---|---|---  
Base URL| `https://api.fireworks.ai/inference/v1` (or `https://us.api.fireworks.ai/inference/v1`)| `https://api.sarvam.ai/v2`  
Chat Completions| `POST /chat/completions`| `POST /chat/completions`  
Responses| `POST /responses`| `POST /responses` (stateless)  
Auth header| `Authorization: Bearer <key>`| `api-subscription-key: <key>` or `Authorization: Bearer <key>`  
Auth failure status| `401`| `403`  
  
## Model IDs

Sarvam has one ID per model. Fireworks’ Fast and US router variants, and your own dedicated deployments of these models, map to the same Sarvam ID.

Fireworks `model`| Sarvam `model`| Status on Sarvam  
---|---|---  
`accounts/fireworks/models/glm-5p3` (also `routers/glm-5p3-fast`, `routers/glm-5p3-us`)| [`glm5.3`](https://docs.sarvam.ai/api/token-factory/models/glm-5-3)| GA  
`accounts/fireworks/models/glm-5p3-flash` (also `routers/glm-5p3-flash-us`)| [`glm5.3-flash`](https://docs.sarvam.ai/api/token-factory/models/glm-5-3-flash)| GA  
`accounts/fireworks/models/gemma-4-31b-it` (on-demand deployment on Fireworks)| [`gemma4`](https://docs.sarvam.ai/api/token-factory/models/gemma-4-31b)| GA  
`accounts/fireworks/models/deepseek-v4p1-flash` (also `routers/deepseek-v4p1-flash-us`)| [`deepseekv4.1-flash-1017`](https://docs.sarvam.ai/api/token-factory/models/deepseek-v4.1-flash-1017)| GA  
`accounts/fireworks/routers/deepseek-v4p1-flash-1017-us` (US-only router on Fireworks)| [`deepseekv4.1-flash-1017`](https://docs.sarvam.ai/api/token-factory/models/deepseek-v4.1-flash-1017)| GA  
`accounts/fireworks/models/deepseek-v4-pro` (April 2026 snapshot; on-demand deployment on Fireworks)| [`deepseekv4-pro`](https://docs.sarvam.ai/api/token-factory/models/deepseek-v4-pro) (0813 snapshot)| Beta  
`accounts/fireworks/models/kimi-k3` (also `routers/kimi-k3-fast`, `routers/kimi-k3-us`)| [`kimi-k3`](https://docs.sarvam.ai/api/token-factory/models/kimi-k3)| Beta  
Not offered on Fireworks| [`mimo-v2.6-flash`](https://docs.sarvam.ai/api/token-factory/models/mimo-v2.6-flash)| Beta  
Not offered on Fireworks (only the MiMo V2.6 Pro-RL variant is listed)| [`mimo-v2.6-pro`](https://docs.sarvam.ai/api/token-factory/models/mimo-v2.6-pro)| Beta  
  
Sarvam’s `deepseekv4-pro` is the newer 0813 snapshot of DeepSeek V4 Pro, so outputs can differ from the April 2026 snapshot on Fireworks.

Gemma 4 31B and DeepSeek V4 Pro need a dedicated deployment on Fireworks. On Sarvam, call them by model ID like any other model, with no deployment to create or manage.

Model IDs are case-sensitive. An unknown ID returns `404 not_found_error`. [`GET /v2/models`](https://docs.sarvam.ai/api-reference/chat/models-v2) lists the available models. Beta models need per-key access: without it, they return `400 invalid_request_error`, even though the list shows them. [Contact us](https://docs.sarvam.ai/api/getting-started/help) to request access.

## Models not on Sarvam

If you use a model that Sarvam doesn’t serve, start with the closest one below, then test it on your own prompts before switching traffic. These are suggestions, not drop-in equivalents.

If you use| Try on Sarvam| Why  
---|---|---  
GLM-5.3 Prime| [`glm5.3`](https://docs.sarvam.ai/api/token-factory/models/glm-5-3)| Same GLM-5.3 generation.  
GLM-5.3 FlashX| [`glm5.3-flash`](https://docs.sarvam.ai/api/token-factory/models/glm-5-3-flash)| Same fast GLM-5.3 variant family, with image input.  
Earlier GLM (GLM-5.2, GLM-5.1, GLM-5, GLM-4.x)| [`glm5.3`](https://docs.sarvam.ai/api/token-factory/models/glm-5-3)| Newer generation of the same family. For image input, use `glm5.3-flash`.  
DeepSeek V4 Flash (any snapshot), DeepSeek V3.x| [`deepseekv4.1-flash-1017`](https://docs.sarvam.ai/api/token-factory/models/deepseek-v4.1-flash-1017)| The DeepSeek Flash model Sarvam serves.  
DeepSeek V4 Pro (April 2026 snapshot), DeepSeek R1| [`deepseekv4-pro`](https://docs.sarvam.ai/api/token-factory/models/deepseek-v4-pro)| Sarvam serves the newer 0813 snapshot.  
Kimi K2, K2.5, K2.6, K2.7 Code, K2 Thinking| [`kimi-k3`](https://docs.sarvam.ai/api/token-factory/models/kimi-k3)| Newer Kimi generation, with a longer 1M context.  
MiMo V2.5, MiMo V2.6 Pro UltraSpeed, MiMo V2.6 Pro-RL| [`mimo-v2.6-pro`](https://docs.sarvam.ai/api/token-factory/models/mimo-v2.6-pro) or [`mimo-v2.6-flash`](https://docs.sarvam.ai/api/token-factory/models/mimo-v2.6-flash)| Current MiMo generation, with image, audio, and video input.  
Gemma 3, Gemma 4 26B| [`gemma4`](https://docs.sarvam.ai/api/token-factory/models/gemma-4-31b)| Gemma 4 31B: image input, a 256K context window, and reasoning (off by default).  
  
For other model families, such as Qwen, Llama, gpt-oss, or MiniMax, choose by what you need:

If you need| Try on Sarvam  
---|---  
Indian-language quality| [`sarvam-105b`](https://docs.sarvam.ai/api/token-factory/models/sarvam-105b)  
The lowest cost| [`mimo-v2.6-flash`](https://docs.sarvam.ai/api/token-factory/models/mimo-v2.6-flash)  
Image input| [`glm5.3-flash`](https://docs.sarvam.ai/api/token-factory/models/glm-5-3-flash), [`kimi-k3`](https://docs.sarvam.ai/api/token-factory/models/kimi-k3), [`gemma4`](https://docs.sarvam.ai/api/token-factory/models/gemma-4-31b), or the MiMo models  
Audio input| [`mimo-v2.6-flash`](https://docs.sarvam.ai/api/token-factory/models/mimo-v2.6-flash) or [`mimo-v2.6-pro`](https://docs.sarvam.ai/api/token-factory/models/mimo-v2.6-pro)  
Video input| [`mimo-v2.6-flash`](https://docs.sarvam.ai/api/token-factory/models/mimo-v2.6-flash) or [`mimo-v2.6-pro`](https://docs.sarvam.ai/api/token-factory/models/mimo-v2.6-pro) (chat only)  
The hardest coding and agent tasks| [`glm5.3`](https://docs.sarvam.ai/api/token-factory/models/glm-5-3) or [`deepseekv4-pro`](https://docs.sarvam.ai/api/token-factory/models/deepseek-v4-pro)  
Fast answers without reasoning| [`mimo-v2.6-flash`](https://docs.sarvam.ai/api/token-factory/models/mimo-v2.6-flash) with thinking off, or [`gemma4`](https://docs.sarvam.ai/api/token-factory/models/gemma-4-31b)  
  
## Media input and request size

Sarvam accepts images, audio, and video only as **inline base64 data URIs**. Remote `http(s)` URLs return `400` on every model, even where your current provider fetches them for you, so download the file and encode it before sending.

Media| Models| Chat Completions| Responses  
---|---|---|---  
Image| Models with image input, such as `gemma4`, `glm5.3-flash`, `kimi-k3`, and the MiMo models| `image_url` part| `input_image` part  
Audio| `mimo-v2.6-flash`, `mimo-v2.6-pro`| `input_audio` part (`wav` or `mp3`), or an `audio_url` part with a data URI (WAV, MP3, FLAC, OGG, Opus)| `input_audio` part (`wav` or `mp3`)  
Video| `mimo-v2.6-flash`, `mimo-v2.6-pro`, and `kimi-k3` (beta, short clips)| `video_url` part| Not supported  
      
    
    import base64
    
    def data_uri(path: str, mime: str) -> str:
    
        with open(path, "rb") as f:
    
            return f"data:{mime};base64," + base64.b64encode(f.read()).decode()
    
    image_part = {"type": "image_url", "image_url": {"url": data_uri("chart.png", "image/png")}}
    
    video_part = {"type": "video_url", "video_url": {"url": data_uri("clip.mp4", "video/mp4")}}

Request bodies, including base64 media, are limited to **40 MiB** on `kimi-k3` and the MiMo models, and **10 MiB** on other models. Larger requests return `413` with the limit in the message. Base64 adds about 33%, so about 30 MB of raw media fits in a 40 MiB request.

## Errors and rate limits

Sarvam returns `403` (not `401`) for a missing or invalid key, `429` when you exceed a rate limit, and `503` when a model is overloaded. Retry `429` and `503` with backoff. Limits apply per API key, as requests per minute rather than Fireworks’ adaptive tokens-per-minute limits. See [Errors & Troubleshooting](https://docs.sarvam.ai/api/getting-started/errors-troubleshooting) and [Credits & Rate Limits](https://docs.sarvam.ai/api/getting-started/pricing#rate-limits).

## See also

  * [Migrating Chat Completion from Fireworks](https://docs.sarvam.ai/api/token-factory/migrations/from-fireworks/chat-completion)
  * [Migrating the Responses API from Fireworks](https://docs.sarvam.ai/api/token-factory/migrations/from-fireworks/responses-api)
  * [Open-Weight Models](https://docs.sarvam.ai/api/token-factory/models)
  * [Beta models](https://docs.sarvam.ai/api-reference/beta-apis)
  * [Errors & Troubleshooting](https://docs.sarvam.ai/api/getting-started/errors-troubleshooting)



Was this page helpful?

YesNo

[Previous](https://docs.sarvam.ai/api/token-factory/migrations/from-openrouter/responses-api)[Migrating Chat Completion from Fireworks AI to SarvamNext](https://docs.sarvam.ai/api/token-factory/migrations/from-fireworks/chat-completion)[Built with](https://buildwithfern.com/?utm_source=others&utm_medium=organic&utm_campaign=fern_indocs_url&utm_content=book_demo&utm_term=docs.sarvam.ai)

  * Getting Started

    * [Welcome](https://docs.sarvam.ai/api/getting-started/welcome)
    * [Quickstart](https://docs.sarvam.ai/api/getting-started/quickstart)
    * [SDKs & Libraries](https://docs.sarvam.ai/api/getting-started/sdks)
    * [Pricing, Credits & Rate Limits](https://docs.sarvam.ai/api/getting-started/pricing)
    * [Talk to us](https://docs.sarvam.ai/api/getting-started/help)
  * [Token Factory (Open-Weight)](https://docs.sarvam.ai/api/token-factory)
    * [Models](https://docs.sarvam.ai/api/token-factory/models)

    * [Chat Completions](https://docs.sarvam.ai/api/token-factory/chat-completions)
    * [Responses API](https://docs.sarvam.ai/api/token-factory/responses-api)
    * How-to

    * Migration Guides
      * From OpenRouter

      * From Fireworks AI
        * [Overview](https://docs.sarvam.ai/api/token-factory/migrations/from-fireworks/overview)
        * [Chat Completion](https://docs.sarvam.ai/api/token-factory/migrations/from-fireworks/chat-completion)
        * [Responses API](https://docs.sarvam.ai/api/token-factory/migrations/from-fireworks/responses-api)

      * From Together AI

      * From Gemini

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
  * [Sarvam 105B](https://docs.sarvam.ai/api/token-factory/models/sarvam-105b)
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


