---
url: https://docs.sarvam.ai/api/token-factory/models/qwen-3-8-27b/
title: Qwen 3.8 27B | Sarvam API Docs
method: scrapling+scrapegraph
fetched_at: 2026-11-08T01:52:36.524621+00:00
---

# Qwen 3.8 27B | Sarvam API Docs

> Source: https://docs.sarvam.ai/api/token-factory/models/qwen-3-8-27b/

Skip to navigation

On this page

  * At a glance
  * Key capabilities
  * Quickstart
  * Reasoning
  * Structured output
  * Image input
  * Supported parameters
  * Known limitations
  * Limits and errors



Scroll to top

[Token Factory (Open-Weight)](https://docs.sarvam.ai/api/token-factory)[Models](https://docs.sarvam.ai/api/token-factory/models)

# Qwen 3.8 27B

Ask a question|Copy page|[View as Markdown](https://docs.sarvam.ai/api/token-factory/models/qwen-3-8-27b.md "View this page as plain text")|More actions

This page is for Model APIs.

Qwen 3.8 27B is a 27B-parameter open-weight reasoning model served on Sarvam infrastructure. It accepts **text and images** and has a **262,144-token context window**. It thinks before answering by default, and you can turn thinking off for direct answers (see [Reasoning](https://docs.sarvam.ai/api/token-factory/models/qwen-3-8-27b#reasoning)).

Qwen 3.8 27B is available on **Provisioned Throughput** : capacity is set up for your workload and enabled for your organisation. Without access, requests return `404 not_found_error` and the model isn’t listed in [`GET /v2/models`](https://docs.sarvam.ai/api-reference/chat/models-v2). [Contact us](https://docs.sarvam.ai/api/getting-started/help) to request access. See [Provisioned Throughput](https://docs.sarvam.ai/api/token-factory/models#provisioned-throughput).

## At a glance

|   
---|---  
**Model ID**| `qwen38-27b`  
**Best for**|  Mid-size reasoning, tool calling, and image understanding at dedicated capacity  
**Context window**|  262,144 tokens  
**Input → output**|  Text and images → text  
**Reasoning**|  On by default; turn it off with `reasoning_effort: "none"`. See [Reasoning](https://docs.sarvam.ai/api/token-factory/models/qwen-3-8-27b#reasoning)  
**Tool calling**|  Supported, including `tool_choice: "required"`, named functions, and parallel tool calls  
**Log probabilities**|  Supported on [Chat Completion V2](https://docs.sarvam.ai/api-reference/chat/chat-completions-v2) and [Responses](https://docs.sarvam.ai/api-reference/responses/create)  
**APIs**| [`POST /v2/chat/completions`](https://docs.sarvam.ai/api-reference/chat/chat-completions-v2) and [`POST /v2/responses`](https://docs.sarvam.ai/api-reference/responses/create)  
**Pricing**|  ₹18 input · ₹5 cached input · ₹230 output per 1M tokens; reasoning is billed as output ([Pricing](https://docs.sarvam.ai/api/getting-started/pricing))  
  
## Key capabilities

Image understanding

Send one or more base64 images alongside text in the same message.

Thinking on or off

Reasons by default; set `reasoning_effort: "none"` for direct, low-latency answers.

Tool calling

Use OpenAI-compatible `tools` and `tool_choice`, including parallel calls.

Streaming

Receive reasoning and answer deltas as server-sent events.

## Quickstart

PythonJavaScriptcURL
    
    
    from sarvamai import SarvamAI
    
    client = SarvamAI(api_subscription_key="YOUR_SARVAM_API_KEY")
    
    response = client.chat.completions_v2(
    
        model="qwen38-27b",
    
        messages=[
    
            {"role": "user", "content": "Explain the difference between TCP and UDP in three bullet points."}
    
        ],
    
        max_tokens=2000,
    
    )
    
    print(response.choices[0].message.content.strip())

The answer in `content` can start with blank lines (`"\n\n"`) when the model has reasoned first, so trim it before display.

## Reasoning

Qwen 3.8 27B thinks by default. Read the trace from `choices[].message.reasoning_content` on chat, or from the `reasoning` output item on Responses.

Value| Effect  
---|---  
Omitted, or `"minimal"`, `"low"`, `"medium"`, `"high"`, `"xhigh"`, `"max"`| Thinking on. The levels are accepted but don’t change how much it thinks.  
`"none"`| Turns thinking off; the model answers directly.  
  
Set the value with `reasoning_effort` on [Chat Completion V2](https://docs.sarvam.ai/api-reference/chat/chat-completions-v2) or `reasoning.effort` on [Responses](https://docs.sarvam.ai/api-reference/responses/create). You can also turn thinking off with `chat_template_kwargs: {"enable_thinking": false}`, sent through `extra_body` in the SDKs.

Reasoning tokens are billed as output tokens and count against `max_tokens` / `max_output_tokens`.

## Structured output

Turn thinking off when you use structured output. With thinking on, the JSON is written into the reasoning trace and `content` comes back `null` on chat (on Responses, the output has only a `reasoning` item).
    
    
    response = client.chat.completions_v2(
    
        model="qwen38-27b",
    
        reasoning_effort="none",
    
        response_format={"type": "json_object"},
    
        messages=[
    
            {"role": "user", "content": "Return JSON with keys city and country for the capital of Japan."}
    
        ],
    
    )

## Image input

Send images as **base64 data URIs** in `image_url` content parts on chat, or `input_image` parts on Responses. Remote `http(s)` image URLs return `400`. Several images can go in one message; the model reads them in order.

## Supported parameters

Parameter| Chat Completion V2| Responses  
---|---|---  
Streaming (`stream`)| |   
Image input (base64)| |   
Tool calling (`tools`, `tool_choice`)| `auto`, `none`, `required`, or named|   
Structured output (`response_format` / `text.format`)|  with thinking off ([details](https://docs.sarvam.ai/api/token-factory/models/qwen-3-8-27b#structured-output))|  with thinking off  
Log probabilities (`logprobs`, `top_logprobs`)| |  send `top_logprobs` with `include: ["message.output_text.logprobs"]`  
Multiple choices (`n` > 1)| `400`| N/A — Responses has no `n`  
`top_k`| | `400`  
Reasoning control| `reasoning_effort`; `"none"` turns thinking off| `reasoning.effort`; `"none"` turns thinking off  
Stateful fields (`store`, `previous_response_id`)| N/A| `400`; replay the conversation in `input`  
  
`400` is `invalid_request_error`.

## Known limitations

  * Text and image input only. Video and audio parts return `400`.
  * On Chat Completion V2, a `developer` message returns `400 invalid_request_error`. Use a `system` message instead. Responses accepts `developer` input items.
  * With thinking on, structured output lands in the reasoning trace instead of `content`. Set `reasoning_effort: "none"` (see [Structured output](https://docs.sarvam.ai/api/token-factory/models/qwen-3-8-27b#structured-output)).
  * Reasoning and the final answer share the **`max_tokens`** / **`max_output_tokens`** budget.



## Limits and errors

Area| Limit or condition| API response| Recommended action  
---|---|---|---  
Access| Your organisation does not have Provisioned Throughput for this model| `404 not_found_error`; the model isn’t listed in `GET /v2/models`| [Contact us](https://docs.sarvam.ai/api/getting-started/help) to request access.  
Context| Prompt tokens plus `max_tokens` exceed 262,144| `400 invalid_request_error`| Shorten the prompt, send fewer images, or reduce `max_tokens`.  
Output| `max_tokens` exceeds 262,144| `400 invalid_request_error`| Set `max_tokens` within the context window.  
Media URL| An image part uses an `http(s)` URL| `400 invalid_request_error`| Inline the image as a base64 data URI.  
Modality| Request includes video or audio input| `400 invalid_request_error`| Send text or image input.  
Messages| A `developer` message on Chat Completion V2| `400 invalid_request_error`: “The ‘developer’ role is not supported for this model; send these instructions with the ‘system’ role.”| Send the instructions as a `system` message.  
Choices| `n` > 1| `400 invalid_request_error`| Send one request per completion.  
Reasoning| Reasoning consumes the full `max_tokens` budget| `200` with `finish_reason: "length"`| Raise `max_tokens` or turn thinking off.  
Authentication| API key is missing or invalid| `403 invalid_api_key_error`| Check the `api-subscription-key` header.  
Model| Model ID is unknown or unavailable| `404 not_found_error`| Confirm the ID with [`GET /v2/models`](https://docs.sarvam.ai/api-reference/chat/models-v2).  
Quota| No credits remain| `402 insufficient_quota_error`| Add credits in the [dashboard](https://indus.sarvam.ai/billing?ref=docs).  
Rate limit| Request or concurrency limit is exceeded| `429 rate_limit_exceeded_error`| Back off and retry.  
  
Was this page helpful?

YesNo

[Previous](https://docs.sarvam.ai/api/token-factory/models/kimi-k3.1-pro)[ClefNext](https://docs.sarvam.ai/api/token-factory/models/clef)[Built with](https://buildwithfern.com/?utm_source=others&utm_medium=organic&utm_campaign=fern_indocs_url&utm_content=book_demo&utm_term=docs.sarvam.ai)

  * Getting Started

    * [Welcome](https://docs.sarvam.ai/api/getting-started/welcome)
    * [Quickstart](https://docs.sarvam.ai/api/getting-started/quickstart)
    * [SDKs & Libraries](https://docs.sarvam.ai/api/getting-started/sdks)
    * [Pricing, Credits & Rate Limits](https://docs.sarvam.ai/api/getting-started/pricing)
    * [Talk to us](https://docs.sarvam.ai/api/getting-started/help)
  * [Token Factory (Open-Weight)](https://docs.sarvam.ai/api/token-factory)
    * [Models](https://docs.sarvam.ai/api/token-factory/models)
      * [Sarvam 105B](https://docs.sarvam.ai/api/token-factory/models/sarvam-105b)
      * [Sarvam 105B Conversations](https://docs.sarvam.ai/api/token-factory/models/sarvam-105b#conversational-variant "Sarvam 105B Conversations")
      * [Sarvam Prism](https://docs.sarvam.ai/api/token-factory/models/sarvam-prism)
      * [GLM-5.3](https://docs.sarvam.ai/api/token-factory/models/glm-5-3)
      * [GLM-5.3 Flash](https://docs.sarvam.ai/api/token-factory/models/glm-5-3-flash)
      * [Gemma 4 31B](https://docs.sarvam.ai/api/token-factory/models/gemma-4-31b)
      * [DeepSeek V4.1 Flash 1017](https://docs.sarvam.ai/api/token-factory/models/deepseek-v4.1-flash-1017)
      * [DeepSeek V4 Pro](https://docs.sarvam.ai/api/token-factory/models/deepseek-v4-pro)
      * [Kimi K3.1 Pro](https://docs.sarvam.ai/api/token-factory/models/kimi-k3.1-pro)
      * [Qwen 3.8 27B](https://docs.sarvam.ai/api/token-factory/models/qwen-3-8-27b)
      * [Clef](https://docs.sarvam.ai/api/token-factory/models/clef)
      * [EmbeddingGemma 2](https://docs.sarvam.ai/api/token-factory/models/embeddinggemma-2)

    * [Chat Completions](https://docs.sarvam.ai/api/token-factory/chat-completions)
    * [Responses API](https://docs.sarvam.ai/api/token-factory/responses-api)
    * [Decisions API](https://docs.sarvam.ai/api/token-factory/decisions-api)
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
  * [Sarvam 105B](https://docs.sarvam.ai/api/token-factory/models/sarvam-105b)
  * [Sarvam Prism](https://docs.sarvam.ai/api/token-factory/models/sarvam-prism)
  * [GLM-5.3](https://docs.sarvam.ai/api/token-factory/models/glm-5-3)
  * [GLM-5.3 Flash](https://docs.sarvam.ai/api/token-factory/models/glm-5-3-flash)
  * [Gemma 4 31B](https://docs.sarvam.ai/api/token-factory/models/gemma-4-31b)
  * [DeepSeek V4.1 Flash 1017](https://docs.sarvam.ai/api/token-factory/models/deepseek-v4.1-flash-1017)
  * [DeepSeek V4 Pro](https://docs.sarvam.ai/api/token-factory/models/deepseek-v4-pro)
  * [Kimi K3.1 Pro](https://docs.sarvam.ai/api/token-factory/models/kimi-k3.1-pro)
  * [Qwen 3.8 27B](https://docs.sarvam.ai/api/token-factory/models/qwen-3-8-27b)
  * [Clef](https://docs.sarvam.ai/api/token-factory/models/clef)
  * [EmbeddingGemma 2](https://docs.sarvam.ai/api/token-factory/models/embeddinggemma-2)
  * [Chat Completions](https://docs.sarvam.ai/api/token-factory/chat-completions)
  * [Responses API](https://docs.sarvam.ai/api/token-factory/responses-api)
  * [Decisions API](https://docs.sarvam.ai/api/token-factory/decisions-api)
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
  * [Document AI](https://docs.sarvam.ai/doc-ai)
  * [Content Studio](https://docs.sarvam.ai/creative)
  * [Cowork](https://docs.sarvam.ai/cowork)
  * [API Reference](https://docs.sarvam.ai/api-reference)
  * [Changelog](https://docs.sarvam.ai/changelog)


