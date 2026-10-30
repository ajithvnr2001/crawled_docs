---
url: https://docs.sarvam.ai/api/token-factory/migrations/from-fireworks/chat-completion/
title: Migrating Chat Completion from Fireworks AI to Sarvam | Sarvam API Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-30T06:37:12.456072+00:00
---

# Migrating Chat Completion from Fireworks AI to Sarvam | Sarvam API Docs

> Source: https://docs.sarvam.ai/api/token-factory/migrations/from-fireworks/chat-completion/

Skip to navigation

On this page

  * Migration checklist
  * Quick start
  * Reasoning
  * Fireworks-only fields to remove
  * Parameter concept map
  * Responses API
  * What’s different by design
  * Platform features without a direct equivalent
  * Full example
  * Common mistakes
  * See also



Scroll to top

[Token Factory (Open-Weight)](https://docs.sarvam.ai/api/token-factory)[Migration Guides](https://docs.sarvam.ai/api/token-factory/migrations/from-openrouter/overview)[From Fireworks AI](https://docs.sarvam.ai/api/token-factory/migrations/from-fireworks/overview)

# Migrating Chat Completion from Fireworks AI to Sarvam

Ask a question|Copy page|[View as Markdown](https://docs.sarvam.ai/api/token-factory/migrations/from-fireworks/chat-completion.md "View this page as plain text")|More actions

This page is for Model APIs.

_Last updated: October 23, 2026_

This guide covers moving Fireworks AI Chat Completions and Responses calls for open-weight models to Sarvam’s [`/v2` API](https://docs.sarvam.ai/api/token-factory/chat-completions).

**In short:** change `base_url`, `api_key`, and `model`. Reasoning comes back in `reasoning_content` on both platforms. Remove Fireworks-only fields such as `prompt_truncate_len` and `perf_metrics_in_response`, because Sarvam returns `400` for request fields it doesn’t support. Set `max_tokens` explicitly, and send the full history on every Responses call.

## Migration checklist

  1. Create an API key in the [Sarvam dashboard](https://indus.sarvam.ai/key-management?ref=docs).
  2. Change `base_url` to `https://api.sarvam.ai/v2` and `api_key` to your Sarvam key.
  3. Replace each model ID using the [model ID table](https://docs.sarvam.ai/api/token-factory/migrations/from-fireworks/overview#model-ids). Fast, US, and deployment IDs map to the same Sarvam ID.
  4. Use string values for `reasoning_effort` (`low`, `high`, `max`, or `none`) ([Reasoning](https://docs.sarvam.ai/api/token-factory/migrations/from-fireworks/chat-completion#reasoning)).
  5. Remove Fireworks-only fields: `prompt_truncate_len`, `context_length_exceeded_behavior`, `perf_metrics_in_response`, and others ([list](https://docs.sarvam.ai/api/token-factory/migrations/from-fireworks/chat-completion#fireworks-only-fields-to-remove)).
  6. Set `max_tokens` explicitly: only `glm5.3` defaults to `2048` on Sarvam.
  7. Trim long conversations yourself: Sarvam doesn’t truncate prompts.
  8. If you use the Responses API, follow [Migrating the Responses API](https://docs.sarvam.ai/api/token-factory/migrations/from-fireworks/responses-api).
  9. Run your tests and watch for `400` responses that name a field.



## Quick start

| Fireworks AI| Sarvam  
---|---|---  
Base URL| `https://api.fireworks.ai/inference/v1`| `https://api.sarvam.ai/v2`  
Auth header| `Authorization: Bearer <key>`| `api-subscription-key: <key>` or `Authorization: Bearer <key>`  
Model ID| `accounts/fireworks/models/kimi-k3`| `kimi-k3` (see the [model ID table](https://docs.sarvam.ai/api/token-factory/migrations/from-fireworks/overview#model-ids))  
  
###### Before (Fireworks)

###### After (Sarvam)

Python (OpenAI SDK)JavaScript (OpenAI SDK)cURL
    
    
    from openai import OpenAI
    
    client = OpenAI(
    
        api_key="YOUR_FIREWORKS_API_KEY",
    
        base_url="https://api.fireworks.ai/inference/v1",
    
    )
    
    response = client.chat.completions.create(
    
        model="accounts/fireworks/models/kimi-k3",
    
        messages=[
    
            {"role": "system", "content": "You are a helpful assistant."},
    
            {"role": "user", "content": "Suggest a name for a coffee shop in Bengaluru."},
    
        ],
    
        reasoning_effort="low",
    
        extra_body={"prompt_truncate_len": 100000},
    
    )
    
    print(response.choices[0].message.content)

## Reasoning

Fireworks| Sarvam| Note  
---|---|---  
`reasoning_effort: "low"` / `"high"` / `"max"`| Same| Each model’s default is listed under [Reasoning](https://docs.sarvam.ai/api/token-factory/models#reasoning).  
`reasoning_effort: "medium"` / `"xhigh"`| Use `"low"`, `"high"`, or `"max"`| Accepted on some models and returns `400` on others, such as `glm5.3`.  
`reasoning_effort: "none"` or `false`| `reasoning_effort: "none"`| Turns thinking off on `deepseekv4-pro`, `mimo-v2.6-flash`, and `mimo-v2.6-pro`. `kimi-k3` and `glm5.3-flash` always think.  
`reasoning_effort` as a token budget (`1024` or more)| Use an effort level| Integer budgets above `100` return `400`.  
`thinking: {"type": "disabled"}`| Same, via `extra_body`| Works on the models that can turn thinking off. To control depth, use `reasoning_effort`.  
`reasoning_history`| Remove| To keep reasoning across turns, send the earlier assistant `reasoning_content` back in `messages`.  
`choices[].message.reasoning_content`| Same| Also `delta.reasoning_content` when streaming.  
  
On Fireworks, a `json_schema` response format turns reasoning off. On Sarvam, reasoning models keep reasoning when you use `response_format`, so leave room in `max_tokens`, or turn thinking off on models that support it.

## Fireworks-only fields to remove

Sarvam validates request fields and returns `400 invalid_request_error` with `Unsupported parameter(s)` for fields it doesn’t support, so leftover Fireworks options fail loudly instead of being ignored.

Fireworks field| What to do on Sarvam  
---|---  
`prompt_truncate_len`| Remove. Trim old messages yourself before sending.  
`context_length_exceeded_behavior`| Remove. Sarvam returns an error when the prompt plus `max_tokens` is longer than the context window, instead of truncating.  
`perf_metrics_in_response`| Remove. Measure latency on your side. Sarvam returns token counts in `usage`.  
`response_format: {"type": "grammar"}`| Use `response_format` with a `json_schema`. Sarvam supports `text`, `json_object`, and `json_schema`.  
`typical_p`, `mirostat_target`, `mirostat_lr`| Remove. Use `temperature`, `top_p`, or `top_k`.  
`raw_output`, `echo`, `return_token_ids`, `prompt_token_ids`, `safe_tokenization`| Remove. Not available.  
`prediction`, `logit_bias`| Remove. Not supported.  
`reasoning_history`| Remove (see [Reasoning](https://docs.sarvam.ai/api/token-factory/migrations/from-fireworks/chat-completion#reasoning)).  
Model IDs with `accounts/.../deployments/...`| Use the Sarvam model ID. There are no deployments to manage.  
  
## Parameter concept map

Fireworks| Sarvam| Note  
---|---|---  
`messages`, `temperature`, `top_p`, `top_k`, `stop`, `seed`| Same|   
`max_tokens` (defaults to `2048`)| `max_tokens`| Set it explicitly. When it’s omitted on Sarvam, generation isn’t capped at `2048` (except on `glm5.3`).  
`frequency_penalty`, `presence_penalty`, `repetition_penalty`| Same|   
`min_p`| Not supported| Remove it. The open-weight models accept only `0`, which is the same as leaving it out.  
`tools`, `tool_choice`, `parallel_tool_calls`| Same| `tool_choice: "any"` is Fireworks-only; use `"required"`.  
`response_format` (`json_object`, `json_schema`)| Same|   
`logprobs`, `top_logprobs`| Same| `logprobs` must be `true` or `false`. Not supported on `glm5.3`.  
`n`| Same| Supported on most models. `temperature` must be above `0` when `n` > 1.  
`prompt_cache_key`, `user`| Accepted, except `prompt_cache_key` on `gemma4`, which returns `400`| For multi-turn caching on `gemma4`, send the [`x-session-affinity`](https://docs.sarvam.ai/api/token-factory/chat-completions#session-affinity-for-multi-turn-conversations) header.  
`service_tier: "priority"`, Fast routers| Not needed| Sarvam has a single tier per model.  
`stream: true`| Same| Usage arrives in the final chunk.  
`image_url` content parts| Same| Inline base64 data URIs only, on models with image input. See each [model page](https://docs.sarvam.ai/api/token-factory/models).  
`input_audio` content parts| Same, on the MiMo models| `wav` or `mp3`. For FLAC, OGG, or Opus, send an `audio_url` part with a data URI. See [Media input](https://docs.sarvam.ai/api/token-factory/migrations/from-fireworks/overview#media-input-and-request-size).  
`video_url` content parts| Same, as a base64 data URI| On the MiMo models and `kimi-k3` (beta, short clips). Sarvam doesn’t fetch video URLs.  
  
## Responses API

Fireworks stores responses and chains them with `previous_response_id`; Sarvam’s Responses API is stateless, so you send the history in `input` instead. For base URL and field changes, reasoning items, function tools, and server-side tools, see [Migrating the Responses API from Fireworks](https://docs.sarvam.ai/api/token-factory/migrations/from-fireworks/responses-api).

## What’s different by design

  * **No deployments to manage.** Models that need an on-demand deployment on Fireworks, such as Gemma 4 31B and DeepSeek V4 Pro, are called by model ID on Sarvam.
  * **Strict request validation.** Unsupported fields return `400` with the field named, instead of being dropped silently. `gemma4` is less strict: it accepts some fields, such as `prediction` and `logit_bias`, and ignores them.
  * **No silent truncation.** Sarvam rejects a prompt that doesn’t fit, rather than cutting old messages or lowering `max_tokens` for you.
  * **Stateless Responses.** Your app keeps the conversation history, as with Chat Completions.



## Platform features without a direct equivalent

Fireworks feature| On Sarvam  
---|---  
Batch inference jobs| Not available. Send requests concurrently within your [rate limits](https://docs.sarvam.ai/api/getting-started/pricing#rate-limits).  
Fine-tuned and LoRA models| Not available on the `/v2` API.  
On-demand deployments| Not needed. Every model is served by ID.  
US-only endpoint| Not available.  
  
## Full example

A wrapper with retries on `429` and `503`, which Fireworks returns when it sheds load and Sarvam returns when a model is overloaded:

Before (Fireworks)After (OpenAI SDK)After (Sarvam SDK)
    
    
    from openai import OpenAI
    
    client = OpenAI(
    
        api_key="YOUR_FIREWORKS_API_KEY",
    
        base_url="https://api.fireworks.ai/inference/v1",
    
    )
    
    def ask(prompt: str) -> str:
    
        response = client.chat.completions.create(
    
            model="accounts/fireworks/models/deepseek-v4p1-flash",
    
            messages=[{"role": "user", "content": prompt}],
    
            reasoning_effort="low",
    
            extra_body={"context_length_exceeded_behavior": "truncate"},
    
        )
    
        return response.choices[0].message.content

## Common mistakes

###### Keeping the accounts/fireworks/models/ prefix

`accounts/fireworks/models/kimi-k3` returns `404` on Sarvam. Use `kimi-k3`. See the [model ID table](https://docs.sarvam.ai/api/token-factory/migrations/from-fireworks/overview#model-ids).

###### Relying on the 2048-token max_tokens default

Fireworks caps output at `2048` tokens when `max_tokens` is omitted. On Sarvam only `glm5.3` does, so long answers can run much longer. Set `max_tokens` explicitly, leaving room for reasoning tokens.

###### Expecting long prompts to be truncated

Sarvam returns an error instead of truncating. Trim the conversation before sending.

###### Chaining Responses calls with previous_response_id

Sarvam doesn’t store responses. Keep the history in your app and send it in `input`, as in the [Responses example](https://docs.sarvam.ai/api/token-factory/migrations/from-fireworks/chat-completion#responses-api).

###### Leaving Fireworks fields in extra_body

Fields like `prompt_truncate_len` and `perf_metrics_in_response` are often passed through `extra_body`. Sarvam returns `400` with the field name; remove each one it names.

## See also

  * [Migration overview](https://docs.sarvam.ai/api/token-factory/migrations/from-fireworks/overview): base URL, auth, and model IDs
  * [Chat Completion overview](https://docs.sarvam.ai/api/token-factory/chat-completions)
  * [Responses API guide](https://docs.sarvam.ai/api/token-factory/responses-api)
  * [Open-Weight Models](https://docs.sarvam.ai/api/token-factory/models)
  * [Errors & Troubleshooting](https://docs.sarvam.ai/api/getting-started/errors-troubleshooting)



Was this page helpful?

YesNo

[Previous](https://docs.sarvam.ai/api/token-factory/migrations/from-fireworks/overview)[Migrating the Responses API from Fireworks AI to SarvamNext](https://docs.sarvam.ai/api/token-factory/migrations/from-fireworks/responses-api)[Built with](https://buildwithfern.com/?utm_source=others&utm_medium=organic&utm_campaign=fern_indocs_url&utm_content=book_demo&utm_term=docs.sarvam.ai)

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


