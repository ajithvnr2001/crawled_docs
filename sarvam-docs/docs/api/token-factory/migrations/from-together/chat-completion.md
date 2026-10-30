---
url: https://docs.sarvam.ai/api/token-factory/migrations/from-together/chat-completion/
title: Migrating Chat Completion from Together AI to Sarvam | Sarvam API Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-30T06:37:13.626008+00:00
---

# Migrating Chat Completion from Together AI to Sarvam | Sarvam API Docs

> Source: https://docs.sarvam.ai/api/token-factory/migrations/from-together/chat-completion/

Skip to navigation

On this page

  * Migration checklist
  * Quick start
  * Reasoning
  * Together-only fields to remove
  * Parameter concept map
  * Responses API
  * What’s different by design
  * Platform features without a direct equivalent
  * Full example
  * Common mistakes
  * See also



Scroll to top

[Token Factory (Open-Weight)](https://docs.sarvam.ai/api/token-factory)[Migration Guides](https://docs.sarvam.ai/api/token-factory/migrations/from-openrouter/overview)[From Together AI](https://docs.sarvam.ai/api/token-factory/migrations/from-together/overview)

# Migrating Chat Completion from Together AI to Sarvam

Ask a question|Copy page|[View as Markdown](https://docs.sarvam.ai/api/token-factory/migrations/from-together/chat-completion.md "View this page as plain text")|More actions

This page is for Model APIs.

_Last updated: October 23, 2026_

This guide covers moving Together AI Chat Completions calls for open-weight models to Sarvam’s [`/v2` API](https://docs.sarvam.ai/api/token-factory/chat-completions).

**In short:** change `base_url`, `api_key`, and `model`. Replace `reasoning: {"enabled": false}` with `reasoning_effort: "none"`, send `logprobs` as `true` instead of a number, and remove Together-only fields such as `safety_model`: Sarvam returns `400` for request fields it doesn’t support. Remember that `403` now means an auth error, not a context-length error.

## Migration checklist

  1. Create an API key in the [Sarvam dashboard](https://indus.sarvam.ai/key-management?ref=docs).
  2. Change `base_url` to `https://api.sarvam.ai/v2` and `api_key` to your Sarvam key.
  3. Replace each model ID using the [model ID table](https://docs.sarvam.ai/api/token-factory/migrations/from-together/overview#model-ids).
  4. Replace `reasoning: {"enabled": false}` with `reasoning_effort: "none"` ([Reasoning](https://docs.sarvam.ai/api/token-factory/migrations/from-together/chat-completion#reasoning)).
  5. Remove Together-only fields: `safety_model`, `compliance`, `echo`, and others ([list](https://docs.sarvam.ai/api/token-factory/migrations/from-together/chat-completion#together-only-fields-to-remove)).
  6. Send `logprobs` as `true`, with the count in `top_logprobs`.
  7. Update error handling: `403` now means an invalid key, not a prompt that’s too long.
  8. Set `max_tokens` explicitly, then run your tests and watch for `400` responses that name a field.



## Quick start

| Together AI| Sarvam  
---|---|---  
Base URL| `https://api.together.ai/v1`| `https://api.sarvam.ai/v2`  
Auth header| `Authorization: Bearer <key>`| `api-subscription-key: <key>` or `Authorization: Bearer <key>`  
Model ID| `moonshotai/Kimi-K3`| `kimi-k3` (see the [model ID table](https://docs.sarvam.ai/api/token-factory/migrations/from-together/overview#model-ids))  
  
###### Before (Together AI)

###### After (Sarvam)

Python (Together SDK)JavaScript (Together SDK)cURL
    
    
    from together import Together
    
    client = Together(api_key="YOUR_TOGETHER_API_KEY")
    
    response = client.chat.completions.create(
    
        model="deepseek-ai/DeepSeek-V4-Pro-0813",
    
        messages=[
    
            {"role": "system", "content": "You are a helpful assistant."},
    
            {"role": "user", "content": "Suggest a name for a coffee shop in Bengaluru."},
    
        ],
    
        max_tokens=2000,
    
        reasoning={"enabled": False},
    
    )
    
    print(response.choices[0].message.content)

## Reasoning

Together AI| Sarvam| Note  
---|---|---  
`reasoning_effort: "low"` / `"high"` / `"max"`| Same| Each model’s default is listed under [Reasoning](https://docs.sarvam.ai/api/token-factory/models#reasoning).  
`reasoning_effort: "medium"`| Use `"low"`, `"high"`, or `"max"`| Accepted on some models and returns `400` on others, such as `glm5.3`.  
`reasoning: {"enabled": false}`| `reasoning_effort: "none"`| The `reasoning` object returns `400`. `"none"` turns thinking off on `deepseekv4-pro`, `mimo-v2.6-flash`, and `mimo-v2.6-pro`. `kimi-k3` and `glm5.3-flash` always think.  
`reasoning: {"enabled": true}`| Remove| Reasoning models think by default.  
`chat_template_kwargs`| Same| Passed to the model. `{"enable_thinking": false}` turns thinking off on the MiMo models.  
`choices[].message.reasoning` (DeepSeek V4 Pro)| `choices[].message.reasoning_content`| Sarvam uses `reasoning_content` for every model, and `delta.reasoning_content` when streaming.  
`choices[].message.reasoning_content` (Kimi K3, GLM)| Same|   
  
## Together-only fields to remove

Sarvam validates request fields and returns `400 invalid_request_error` for fields it doesn’t support, so leftover Together options fail loudly instead of being ignored.

Together field| What to do on Sarvam  
---|---  
`reasoning` object| Replace with `reasoning_effort` (see [Reasoning](https://docs.sarvam.ai/api/token-factory/migrations/from-together/chat-completion#reasoning)).  
`safety_model`| Remove. Run moderation as a separate step before or after the call.  
`compliance`| Remove.  
`context_length_exceeded_behavior`| Remove. Sarvam returns an error when the prompt plus `max_tokens` is longer than the context window, as Together does by default.  
`echo`| Remove. Keep the prompt on your side.  
`response_format: {"type": "regex"}`| Use `response_format` with a `json_schema`, and put the pattern in a string property’s `pattern`.  
`logprobs: 5` (a number)| Use `logprobs: true` with `top_logprobs: 5`.  
`functions`, `function_call`| Use `tools` and `tool_choice`. The legacy fields return `400`.  
  
## Parameter concept map

Together AI| Sarvam| Note  
---|---|---  
`messages`, `max_tokens`, `temperature`, `top_p`, `top_k`, `stop`, `seed`| Same| Set `max_tokens` explicitly: when it’s omitted, generation isn’t capped at a small default.  
`repetition_penalty`, `frequency_penalty`, `presence_penalty`| Same|   
`min_p`| Not supported| Remove it. The open-weight models accept only `0`, which is the same as leaving it out.  
`tools`, `tool_choice`, `parallel_tool_calls`| Same| `parallel_tool_calls: false` is enforced on every model; see [V2 feature support](https://docs.sarvam.ai/api/token-factory/chat-completions#v2-feature-support).  
`response_format` (`json_schema`, `json_object`)| Same|   
`n`| Same| Supported on most models. `temperature` must be above `0` when `n` > 1.  
`stream: true`| Same| As on Together, the last chunk before `[DONE]` carries `usage` with an empty `choices` array; keep skipping it.  
`image_url` content parts| Same| Sarvam accepts inline base64 data URIs only, not remote image URLs, on models with image input. See each [model page](https://docs.sarvam.ai/api/token-factory/models).  
`video_url` content parts| Same, as a base64 data URI| On the MiMo models and `kimi-k3` (beta, short clips). Sarvam doesn’t fetch video URLs.  
`input_audio` content parts| Same, on the MiMo models| `wav` or `mp3`. For FLAC, OGG, or Opus, send an `audio_url` part with a data URI. See [Media input](https://docs.sarvam.ai/api/token-factory/migrations/from-together/overview#media-input-and-request-size).  
`finish_reason: "eos"`| `finish_reason: "stop"`|   
  
## Responses API

Together doesn’t offer a Responses API. Sarvam does: if you want the OpenAI Responses format, see the [Responses API guide](https://docs.sarvam.ai/api/token-factory/responses-api). It’s stateless, like Chat Completions.

## What’s different by design

  * **No dedicated endpoints to manage.** Models that are dedicated-only on Together, such as Gemma 4 31B, are called by model ID on Sarvam.
  * **Strict request validation.** Unsupported fields return `400` with the field named, instead of being dropped silently. `gemma4` is less strict: it accepts some fields, such as `prediction` and `logit_bias`, and ignores them.
  * **One reasoning field.** Reasoning comes back in `reasoning_content` for every model.
  * **Different meaning for`403`.** On Sarvam it’s an auth error. See the [status code table](https://docs.sarvam.ai/api/token-factory/migrations/from-together/overview#errors-and-rate-limits).



## Platform features without a direct equivalent

Together feature| On Sarvam  
---|---  
Batch API| Not available. Send requests concurrently within your [rate limits](https://docs.sarvam.ai/api/getting-started/pricing#rate-limits).  
Fine-tuning and LoRA adapters| Not available on the `/v2` API.  
Dedicated endpoints and provisioned throughput| Not needed for these models. Contact [Sarvam](https://docs.sarvam.ai/api/getting-started/help) for capacity needs.  
Llama Guard moderation (`safety_model`)| Not available. Run moderation separately.  
  
## Full example

A wrapper that turns thinking off, asks for log probabilities, and maps status codes:

Before (Together AI)After (OpenAI SDK)After (Sarvam SDK)
    
    
    from together import Together
    
    client = Together(api_key="YOUR_TOGETHER_API_KEY")
    
    def ask(prompt: str) -> str:
    
        response = client.chat.completions.create(
    
            model="deepseek-ai/DeepSeek-V4-Pro-0813",
    
            messages=[{"role": "user", "content": prompt}],
    
            max_tokens=2000,
    
            reasoning={"enabled": False},
    
            logprobs=3,
    
        )
    
        return response.choices[0].message.content

## Common mistakes

###### Treating 403 as a context-length error

On Sarvam, `403` means the API key is missing or invalid. Don’t trim the prompt and retry on `403`; check the key instead.

###### Keeping the organisation prefix in the model ID

`moonshotai/Kimi-K3` returns `404` on Sarvam. Use `kimi-k3`. Model IDs are case-sensitive. See the [model ID table](https://docs.sarvam.ai/api/token-factory/migrations/from-together/overview#model-ids).

###### Sending reasoning: {enabled: false}

Sarvam returns `400`. Use `reasoning_effort: "none"` on models that can turn thinking off.

###### Sending logprobs as a number

Sarvam expects `logprobs: true` and the count in `top_logprobs`.

###### Sending images or video by URL

Sarvam accepts images, audio, and video only as inline base64 data URIs; URLs return `400`. Download the file and encode it before sending. See [Media input](https://docs.sarvam.ai/api/token-factory/migrations/from-together/overview#media-input-and-request-size).

## See also

  * [Migration overview](https://docs.sarvam.ai/api/token-factory/migrations/from-together/overview): base URL, auth, model IDs, and status codes
  * [Chat Completion overview](https://docs.sarvam.ai/api/token-factory/chat-completions)
  * [Responses API guide](https://docs.sarvam.ai/api/token-factory/responses-api)
  * [Open-Weight Models](https://docs.sarvam.ai/api/token-factory/models)
  * [Errors & Troubleshooting](https://docs.sarvam.ai/api/getting-started/errors-troubleshooting)



Was this page helpful?

YesNo

[Previous](https://docs.sarvam.ai/api/token-factory/migrations/from-together/overview)[SaarasNext](https://docs.sarvam.ai/api/api-guides-tutorials/models/saaras)[Built with](https://buildwithfern.com/?utm_source=others&utm_medium=organic&utm_campaign=fern_indocs_url&utm_content=book_demo&utm_term=docs.sarvam.ai)

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

      * From Together AI
        * [Overview](https://docs.sarvam.ai/api/token-factory/migrations/from-together/overview)
        * [Chat Completion](https://docs.sarvam.ai/api/token-factory/migrations/from-together/chat-completion)

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


