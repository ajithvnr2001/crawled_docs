---
url: https://docs.sarvam.ai/api/token-factory/responses-api/
title: Responses API | Sarvam API Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-30T06:37:16.059838+00:00
---

# Responses API | Sarvam API Docs

> Source: https://docs.sarvam.ai/api/token-factory/responses-api/

Skip to navigation

On this page

  * Create a response
  * Stream a response (optional)
  * Continue a conversation
  * Reasoning
  * Defaults when omitted (glm5.3)
  * Parameters
  * Refused or unsupported on this route



Scroll to top

[Token Factory (Open-Weight)](https://docs.sarvam.ai/api/token-factory)

# Responses API

Ask a question|Copy page|[View as Markdown](https://docs.sarvam.ai/api/token-factory/responses-api.md "View this page as plain text")|More actions

This page is for Model APIs.

The Responses API provides an OpenAI-compatible interface for text generation, reasoning, structured output, and tool calling. **Streaming is optional** : the same pattern as [Chat Completion V2](https://docs.sarvam.ai/api-reference/chat/chat-completions-v2): omit `stream` or set it to `false` for one JSON response (default).

The Responses API supports `sarvam-105b`, `glm5.3`, `glm5.3-flash`, and `gemma4`, plus the [beta models](https://docs.sarvam.ai/api-reference/beta-apis) `deepseekv4.1-flash-1017`, `deepseekv4-pro`, `kimi-k3`, `mimo-v2.6-flash`, and `mimo-v2.6-pro`.

Moving Responses API code from [OpenRouter](https://docs.sarvam.ai/api/token-factory/migrations/from-openrouter/responses-api) or [Fireworks AI](https://docs.sarvam.ai/api/token-factory/migrations/from-fireworks/responses-api)? See the Responses API migration guides.

## Create a response

Use [`POST /v2/responses`](https://docs.sarvam.ai/api-reference/responses/create). The endpoint is **stateless** : send the complete conversation in `input` on every request. Omit `store` or set it to `false` (`true` returns **`400`**).

Nothing is stored for later retrieval, `GET /v2/responses/{id}` returns **`404`**. `GET /v2/responses` and `DELETE /v2/responses/{id}` return **`405`** (documented in the [API Reference](https://docs.sarvam.ai/api-reference/responses/create) alongside `POST /v2/responses`).

PythonJavaScriptcURL
    
    
    from sarvamai import SarvamAI
    
    client = SarvamAI(api_subscription_key="YOUR_SARVAM_API_KEY")
    
    response = client.responses.create(
    
        model="glm5.3",
    
        input="Explain database indexing in three short points.",
    
        store=False,
    
    )
    
    print(response.output)

The examples above do **not** set `stream`. That returns a single JSON body (**HTTP 200**), same as Chat Completion V2 when `stream` is omitted. Only add `"stream": true` when you want server-sent events.

## Stream a response (optional)

Set `stream` to `true` when you want named server-sent events instead of one JSON body. Streams end with `response.completed`, `response.incomplete`, or `response.failed`; they do **not** emit a `[DONE]` sentinel. On `glm5.3`, streamed items can **nest** : pair events by `item_id`. Usage appears on the terminal event (there is no `stream_options`).

PythonJavaScriptcURL
    
    
    from sarvamai import SarvamAI
    
    client = SarvamAI(api_subscription_key="YOUR_SARVAM_API_KEY")
    
    stream = client.responses.create(
    
        model="glm5.3",
    
        input="Explain database indexing in three short points.",
    
        store=False,
    
        stream=True,
    
    )
    
    for event in stream:
    
        print(event.type)

## Continue a conversation

The endpoint does not store response state. To continue a conversation, send the prior messages and outputs again in `input`. Do not use `previous_response_id` or `conversation` , both return **`400`**.
    
    
    from sarvamai import SarvamAI
    
    client = SarvamAI(api_subscription_key="YOUR_SARVAM_API_KEY")
    
    response = client.responses.create(
    
        model="gemma4",
    
        input=[
    
            {"role": "user", "content": "Name one advantage of a B-tree index."},
    
            {"role": "assistant", "content": "It keeps lookups efficient as data grows."},
    
            {"role": "user", "content": "When should I avoid one?"},
    
        ],
    
        store=False,
    
    )

For message parts in `input`, text uses `{"type": "input_text", "text": "…"}` (not chat completions’ `{"type": "text"}`).

## Reasoning

The reasoning models (`glm5.3`, `glm5.3-flash`, `gemma4`, `deepseekv4.1-flash-1017`, `deepseekv4-pro`, `kimi-k3`, `mimo-v2.6-flash`, and `mimo-v2.6-pro`) support three modes, `low`, `high`, and `max`, and Chat Completion V2 accepts all three directly. `gemma4` reasons only when you set an effort. On this route (Responses), the models differ:

Model| Accepted `reasoning.effort` values on this route  
---|---  
`glm5.3`, `glm5.3-flash`| `"low"` or `"high"` only; the literal string `"max"` returns `400`. Omitting the field gives `max` on `glm5.3` and `high` on `glm5.3-flash`.  
`gemma4`| `"low"` or `"high"`. No reasoning when the field is omitted.  
`deepseekv4.1-flash-1017`| `"low"`, `"high"`, or `"max"`, all three work directly, same as on chat. Default `high`. `"none"` turns thinking off.  
`deepseekv4-pro`| `"low"`, `"high"`, or `"max"`; default `high`. `"none"` turns thinking off.  
`kimi-k3`| `"low"`, `"high"`, or `"max"`; default `max`. Thinking is always on.  
`mimo-v2.6-flash`, `mimo-v2.6-pro`| Thinking is on by default. `"none"` turns it off; any other value only switches it on.  
  
**Chat trace:** `choices[].message.reasoning_content`.

**Responses trace:** reasoning models return a **`reasoning` item** in `output` when they reason. Read the trace from its **`content[0].text`**. Its `summary` is empty unless you set the optional **`reasoning.summary`** to `auto` or `detailed`. At `low` effort, `glm5.3` often skips reasoning on simple prompts and returns no reasoning item. `gemma4` reasons when you set an effort but doesn’t return a reasoning item; its reasoning shows only in `usage.output_tokens_details.reasoning_tokens`.

Reasoning tokens count toward **`max_output_tokens`** , which has **no default cap** on this route, omitting it means unbounded generation. On chat, the equivalent budget is **`max_tokens`** , which defaults to `2048` on `glm5.3` only. Set it explicitly. See the [Chat Completion V2 API Reference](https://docs.sarvam.ai/api-reference/chat/chat-completions-v2).

## Defaults when omitted (`glm5.3`)

Field| Default when omitted  
---|---  
`temperature`| `1`  
`top_p`| `0.95`  
`max_output_tokens`| No default, unbounded generation  
`stream`| `false`  
  
## Parameters

Parameter| Required| Description  
---|---|---  
`model`| Yes| `sarvam-105b`, `glm5.3`, `glm5.3-flash`, `gemma4`, `deepseekv4.1-flash-1017`, `deepseekv4-pro`, `kimi-k3`, `mimo-v2.6-flash`, or `mimo-v2.6-pro`.  
`input`| Yes| A prompt string or the complete conversation as input items.  
`stream`| No| Optional, omit or `false` for one JSON body (default **`false`** on `glm5.3`); `true` for named SSE events, same pattern as chat completions.  
`max_output_tokens`| No| Cap on generated tokens including reasoning. **No default** : omitting it means unbounded generation. Always set this explicitly in production.  
`temperature`| No| `0`–`2`; default **`1`** on `glm5.3`.  
`top_p`| No| Default **`0.95`** on `glm5.3`; must be > `0`.  
`top_k`| No| Not supported on `glm5.3`; any value returns `400`.  
`reasoning`| No| Optional on reasoning models. `effort` accepts `"low"` or `"high"` on `glm5.3` (omit for `max`, the string `"max"` is `400`), or all three values directly on `deepseekv4.1-flash-1017` (omit for `high`). `summary` accepts `"auto"` or `"detailed"`.  
`text`| No| Output format in `text.format` (`text`, `json_object`, `json_schema`).  
`tools`| No| **Flat** function tools (`name` at the top level). Nested chat tool shape is **`400`**.  
`tool_choice`| No| `auto`, `none`, `required`, or a named function.  
`parallel_tool_calls`| No| **`false`** limits a turn to one tool call on every open-weight model. `sarvam-105b` ignores it on this route.  
`n`| No| Not supported on the open-weight models: any value, even `1`, returns `400`.  
`store`| No| Must be omitted or `false`.  
  
### Refused or unsupported on this route

These return **`400`** (the error names the field): `store: true`, `background: true`, `previous_response_id`, `conversation`, `max_tool_calls`, `prompt`, `item_reference`.

On Responses, the open-weight models return `400` for `logprobs` and `repetition_penalty`. For log probabilities on `glm5.3-flash` and `deepseekv4.1-flash-1017`, send `top_logprobs` with `include: ["message.output_text.logprobs"]` instead; `glm5.3` and `gemma4` don’t support them on this route. On Chat Completion V2, `logprobs` and `top_logprobs` are supported on every model except `glm5.3`, which returns a clean `400`. See [Chat Completion V2](https://docs.sarvam.ai/api-reference/chat/chat-completions-v2) for details.

See the [Responses API Reference](https://docs.sarvam.ai/api-reference/responses/create) for the complete request, response, error, and streaming-event schemas. Model-specific limits for `glm5.3` are also summarized on the [GLM-5.3 model page](https://docs.sarvam.ai/api/token-factory/models/glm-5-3).

Was this page helpful?

YesNo

[Previous](https://docs.sarvam.ai/api/token-factory/chat-completions)[How to list your chat messagesNext](https://docs.sarvam.ai/api/token-factory/how-to/list-your-chat-messages)[Built with](https://buildwithfern.com/?utm_source=others&utm_medium=organic&utm_campaign=fern_indocs_url&utm_content=book_demo&utm_term=docs.sarvam.ai)

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


