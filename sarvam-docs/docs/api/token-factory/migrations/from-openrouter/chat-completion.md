---
url: https://docs.sarvam.ai/api/token-factory/migrations/from-openrouter/chat-completion/
title: Migrating Chat Completion from OpenRouter to Sarvam | Sarvam API Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-30T06:37:12.914288+00:00
---

# Migrating Chat Completion from OpenRouter to Sarvam | Sarvam API Docs

> Source: https://docs.sarvam.ai/api/token-factory/migrations/from-openrouter/chat-completion/

Skip to navigation

On this page

  * Migration checklist
  * Quick start
  * Reasoning
  * OpenRouter-only fields to remove
  * Parameter concept map
  * Responses API
  * What’s different by design
  * Full example
  * Common mistakes
  * See also



Scroll to top

[Token Factory (Open-Weight)](https://docs.sarvam.ai/api/token-factory)[Migration Guides](https://docs.sarvam.ai/api/token-factory/migrations/from-openrouter/overview)[From OpenRouter](https://docs.sarvam.ai/api/token-factory/migrations/from-openrouter/overview)

# Migrating Chat Completion from OpenRouter to Sarvam

Ask a question|Copy page|[View as Markdown](https://docs.sarvam.ai/api/token-factory/migrations/from-openrouter/chat-completion.md "View this page as plain text")|More actions

This page is for Model APIs.

_Last updated: October 23, 2026_

This guide covers moving OpenRouter Chat Completions and Responses calls for open-weight models to Sarvam’s [`/v2` API](https://docs.sarvam.ai/api/token-factory/chat-completions).

**In short:** change `base_url`, `api_key`, and `model`. Then remove OpenRouter-only fields such as `provider`, `models`, `reasoning`, and `plugins`: Sarvam returns `400` for request fields it doesn’t support instead of ignoring them. Read reasoning from `reasoning_content` instead of `reasoning`.

## Migration checklist

  1. Create an API key in the [Sarvam dashboard](https://indus.sarvam.ai/key-management?ref=docs).
  2. Change `base_url` to `https://api.sarvam.ai/v2` and `api_key` to your Sarvam key.
  3. Replace each model ID using the [model ID table](https://docs.sarvam.ai/api/token-factory/migrations/from-openrouter/overview#model-ids).
  4. Replace the `reasoning` object with `reasoning_effort` ([Reasoning](https://docs.sarvam.ai/api/token-factory/migrations/from-openrouter/chat-completion#reasoning)).
  5. Remove OpenRouter-only fields: `provider`, `models`, `plugins`, `usage`, `session_id`, and others ([list](https://docs.sarvam.ai/api/token-factory/migrations/from-openrouter/chat-completion#openrouter-only-fields-to-remove)).
  6. Read reasoning from `reasoning_content` instead of `reasoning`.
  7. Replace `models` fallbacks with retries on `429` and `503` ([full example](https://docs.sarvam.ai/api/token-factory/migrations/from-openrouter/chat-completion#full-example)).
  8. Set `max_tokens` explicitly, then run your tests and watch for `400` responses that name a field.



## Quick start

| OpenRouter| Sarvam  
---|---|---  
Base URL| `https://openrouter.ai/api/v1`| `https://api.sarvam.ai/v2`  
Auth header| `Authorization: Bearer <key>`| `api-subscription-key: <key>` or `Authorization: Bearer <key>`  
Model ID| `moonshotai/kimi-k3`| `kimi-k3` (see the [model ID table](https://docs.sarvam.ai/api/token-factory/migrations/from-openrouter/overview#model-ids))  
  
###### Before (OpenRouter)

###### After (Sarvam)

Python (OpenAI SDK)JavaScript (OpenAI SDK)cURL
    
    
    from openai import OpenAI
    
    client = OpenAI(
    
        api_key="YOUR_OPENROUTER_API_KEY",
    
        base_url="https://openrouter.ai/api/v1",
    
    )
    
    response = client.chat.completions.create(
    
        model="moonshotai/kimi-k3",
    
        messages=[
    
            {"role": "system", "content": "You are a helpful assistant."},
    
            {"role": "user", "content": "Suggest a name for a coffee shop in Bengaluru."},
    
        ],
    
        max_tokens=2000,
    
        extra_body={
    
            "reasoning": {"effort": "low"},
    
            "provider": {"sort": "throughput"},
    
        },
    
    )
    
    print(response.choices[0].message.content)

## Reasoning

OpenRouter| Sarvam| Note  
---|---|---  
`reasoning: {"effort": "low"}`| `reasoning_effort: "low"`| Sarvam uses the top-level field only; the `reasoning` object returns `400` on chat. Use `low`, `high`, or `max`.  
`reasoning_effort` (top level)| `reasoning_effort`| Same field. `medium` is accepted on some models and returns `400` on others, such as `glm5.3`.  
`reasoning: {"enabled": false}` or `effort: "none"`| `reasoning_effort: "none"`| Turns thinking off on `deepseekv4-pro`, `mimo-v2.6-flash`, and `mimo-v2.6-pro`. `kimi-k3` and `glm5.3-flash` always think. See [Reasoning](https://docs.sarvam.ai/api/token-factory/models#reasoning).  
`reasoning: {"max_tokens": N}`| Not supported| Choose an effort level instead, and size `max_tokens` to cover reasoning plus the answer.  
`reasoning: {"exclude": true}`| Not supported| Ignore `reasoning_content` in your code. Reasoning tokens are billed either way.  
`include_reasoning: true`| Remove| Reasoning is always returned when the model thinks.  
`choices[].message.reasoning`| `choices[].message.reasoning_content`| Also `delta.reasoning_content` when streaming.  
`choices[].message.reasoning_details`| Not returned|   
  
With the `openai` Python package, read the field with `getattr`, since it isn’t part of the package’s typed response:
    
    
    reasoning = getattr(response.choices[0].message, "reasoning_content", None)

## OpenRouter-only fields to remove

Sarvam validates request fields and returns `400 invalid_request_error` with `Unsupported parameter(s)` for fields it doesn’t support, so leftover OpenRouter options fail loudly instead of being ignored.

OpenRouter field| What to do on Sarvam  
---|---  
`provider` (`order`, `sort`, `only`, `allow_fallbacks`, …)| Remove. Sarvam serves each model itself, so there’s no upstream provider to pick.  
`models` (fallback list)| Remove. Retry on `429` and `503` with backoff, or fall back to a second Sarvam model in your own code (see the [full example](https://docs.sarvam.ai/api/token-factory/migrations/from-openrouter/chat-completion#full-example)).  
`reasoning` object| Replace with `reasoning_effort` (see [Reasoning](https://docs.sarvam.ai/api/token-factory/migrations/from-openrouter/chat-completion#reasoning)).  
`include_reasoning`| Remove.  
`usage: {"include": true}`| Remove. Usage is always returned.  
`plugins` (web search, file parser, response healing, context compression)| Remove. Run web search or PDF parsing yourself and pass the text in `messages`; use `response_format` with a JSON schema instead of response healing; trim long histories yourself.  
`session_id`| Remove. For multi-turn caching on `gemma4`, send the [`x-session-affinity`](https://docs.sarvam.ai/api/token-factory/chat-completions#session-affinity-for-multi-turn-conversations) header instead.  
`cache_control` at the top level| Remove. `cache_control` inside a message content block is accepted.  
`:free`, `:nitro`, `:floor`, `:online` model suffixes| Use the plain Sarvam model ID.  
  
## Parameter concept map

OpenRouter| Sarvam| Note  
---|---|---  
`messages`, `max_tokens`, `temperature`, `top_p`, `stop`, `seed`| Same|   
`tools`, `tool_choice`, `parallel_tool_calls`| Same| `parallel_tool_calls: false` is enforced on every model; see [V2 feature support](https://docs.sarvam.ai/api/token-factory/chat-completions#v2-feature-support).  
`response_format` (`json_schema`, `json_object`)| Same|   
`logprobs`, `top_logprobs`| Same| Supported on every model except `glm5.3`.  
`n`| `n`| Supported on most models; OpenRouter doesn’t support it.  
`top_k`, `repetition_penalty`| Same|   
`stream: true`| Same| No `: OPENROUTER PROCESSING` keep-alive comments. Usage arrives in the final chunk.  
`image_url` content parts| Same| Inline base64 data URIs only, on models with image input. See each [model page](https://docs.sarvam.ai/api/token-factory/models).  
`input_audio` content parts| Same, on the MiMo models| `wav` or `mp3`. For FLAC, OGG, or Opus, send an `audio_url` part with a data URI. See [Media input](https://docs.sarvam.ai/api/token-factory/migrations/from-openrouter/overview#media-input-and-request-size).  
`video_url` content parts| Same, as a base64 data URI| On the MiMo models and `kimi-k3` (beta, short clips). Sarvam doesn’t fetch video URLs.  
`usage.cost`| Not returned| Token counts are in `usage`. Check spend in the [dashboard](https://indus.sarvam.ai/billing?ref=docs).  
`GET /api/v1/generation?id=`| Not available| Log the `id` and `usage` from each response yourself.  
  
## Responses API

Both platforms’ Responses APIs are stateless. For base URL and field changes, reasoning items, function tools, and server-side tools, see [Migrating the Responses API from OpenRouter](https://docs.sarvam.ai/api/token-factory/migrations/from-openrouter/responses-api).

## What’s different by design

  * **One provider, no routing layer.** Sarvam runs each model on its own infrastructure, so there are no upstream providers to rank, pin, or fail over between, and a model’s behaviour doesn’t change from request to request.
  * **Strict request validation.** Unsupported fields return `400` with the field named, instead of being dropped silently. This catches stale options early. `gemma4` is less strict: it accepts some fields, such as `prediction` and `logit_bias`, and ignores them.
  * **Reasoning in`reasoning_content`.** Sarvam uses the same field name as many open-model servers, rather than OpenRouter’s `reasoning` and `reasoning_details`.
  * **Billing in your Sarvam credits.** Usage is metered per token against your Sarvam account. See [Pricing](https://docs.sarvam.ai/api/getting-started/pricing).



## Full example

A wrapper that replaces OpenRouter’s `models` fallback list with retries and a fallback model in your own code:

Before (OpenRouter)After (OpenAI SDK)After (Sarvam SDK)
    
    
    from openai import OpenAI
    
    client = OpenAI(
    
        api_key="YOUR_OPENROUTER_API_KEY",
    
        base_url="https://openrouter.ai/api/v1",
    
    )
    
    def ask(prompt: str) -> str:
    
        response = client.chat.completions.create(
    
            model="moonshotai/kimi-k3",
    
            messages=[{"role": "user", "content": prompt}],
    
            max_tokens=2000,
    
            extra_body={
    
                "models": ["moonshotai/kimi-k3", "z-ai/glm-5.3"],
    
                "reasoning": {"effort": "low"},
    
            },
    
        )
    
        return response.choices[0].message.content

## Common mistakes

###### Leaving OpenRouter fields in extra_body

Fields like `provider`, `models`, `reasoning`, and `plugins` are often passed through `extra_body` in the `openai` package and are easy to miss. Sarvam returns `400` with the field name in the error message; remove each one it names.

###### Keeping the provider prefix in the model ID

`moonshotai/kimi-k3` returns `404` on Sarvam. Use `kimi-k3`. See the [model ID table](https://docs.sarvam.ai/api/token-factory/migrations/from-openrouter/overview#model-ids).

###### Reading message.reasoning

Sarvam returns reasoning in `reasoning_content`. Code that reads `reasoning` gets `None`.

###### Expecting a fallback to happen automatically

Sarvam doesn’t retry on another model for you. Handle `429` and `503` in your code, as in the [full example](https://docs.sarvam.ai/api/token-factory/migrations/from-openrouter/chat-completion#full-example).

###### Setting max_tokens too low on reasoning models

Reasoning tokens count against `max_tokens`. If the model spends the whole budget thinking, `content` is empty and `finish_reason` is `"length"`. Raise `max_tokens` or lower `reasoning_effort`.

## See also

  * [Migration overview](https://docs.sarvam.ai/api/token-factory/migrations/from-openrouter/overview): base URL, auth, and model IDs
  * [Chat Completion overview](https://docs.sarvam.ai/api/token-factory/chat-completions)
  * [Responses API guide](https://docs.sarvam.ai/api/token-factory/responses-api)
  * [Open-Weight Models](https://docs.sarvam.ai/api/token-factory/models)
  * [Errors & Troubleshooting](https://docs.sarvam.ai/api/getting-started/errors-troubleshooting)



Was this page helpful?

YesNo

[Previous](https://docs.sarvam.ai/api/token-factory/migrations/from-openrouter/overview)[Migrating the Responses API from OpenRouter to SarvamNext](https://docs.sarvam.ai/api/token-factory/migrations/from-openrouter/responses-api)[Built with](https://buildwithfern.com/?utm_source=others&utm_medium=organic&utm_campaign=fern_indocs_url&utm_content=book_demo&utm_term=docs.sarvam.ai)

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
        * [Overview](https://docs.sarvam.ai/api/token-factory/migrations/from-openrouter/overview)
        * [Chat Completion](https://docs.sarvam.ai/api/token-factory/migrations/from-openrouter/chat-completion)
        * [Responses API](https://docs.sarvam.ai/api/token-factory/migrations/from-openrouter/responses-api)

      * From Fireworks AI

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


