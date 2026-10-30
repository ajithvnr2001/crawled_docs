---
url: https://docs.sarvam.ai/api/token-factory/models/mimo-v2.6-pro
title: MiMo V2.6 Pro | Sarvam API Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-30T06:37:15.880683+00:00
---

# MiMo V2.6 Pro | Sarvam API Docs

> Source: https://docs.sarvam.ai/api/token-factory/models/mimo-v2.6-pro

Skip to navigation

On this page

  * At a glance
  * Key capabilities
  * Quickstart
  * Supported parameters
  * Reasoning
  * Tool calling
  * Structured output
  * Media input
  * Known limitations
  * Limits and errors



Scroll to top

[Token Factory (Open-Weight)](https://docs.sarvam.ai/api/token-factory)[Models](https://docs.sarvam.ai/api/token-factory/models)

# MiMo V2.6 Pro

Beta

Ask a question|Copy page|[View as Markdown](https://docs.sarvam.ai/api/token-factory/models/mimo-v2.6-pro.md "View this page as plain text")|More actions

This page is for Model APIs.

MiMo V2.6 Pro (checkpoint `MiMo-V2.6-Pro-MOPD`) is the larger model in the MiMo V2.6 family (1.02T total parameters, 42B active), served on Sarvam infrastructure as an [open-weight model](https://docs.sarvam.ai/api/token-factory/models). It has a **1,048,576-token context window** and shares its API behaviour with [MiMo V2.6 Flash](https://docs.sarvam.ai/api/token-factory/models/mimo-v2.6-flash).

MiMo V2.6 Pro is in **beta**. Its behaviour, limits, and availability may change before general availability. Beta models must be enabled for your API key; without access, requests return `400 invalid_request_error` (“This model is currently in beta”). [Contact us](https://docs.sarvam.ai/api/getting-started/help) to request access. See [Beta models](https://docs.sarvam.ai/api-reference/beta-apis).

## At a glance

|   
---|---  
**Model ID**| `mimo-v2.6-pro`  
**Parameters**|  1.02T total, 42B active  
**Best for**|  Harder reasoning and agentic tasks over long text  
**Context window**|  1,048,576 tokens  
**Input → output**|  Text + image + audio + video → text (video on chat only). See [Media input](https://docs.sarvam.ai/api/token-factory/models/mimo-v2.6-pro#media-input)  
**Reasoning**|  On by default; can be turned off. See [Reasoning](https://docs.sarvam.ai/api/token-factory/models/mimo-v2.6-pro#reasoning)  
**Tool calling**|  Supported, including `tool_choice: "required"` and parallel tool calls  
**APIs**| [`POST /v2/chat/completions`](https://docs.sarvam.ai/api-reference/chat/chat-completions-v2) and [`POST /v2/responses`](https://docs.sarvam.ai/api-reference/responses/create)  
**Pricing**|  ₹40 input · ₹0.3 cached input · ₹80 output per 1M tokens; reasoning is billed as output ([Pricing](https://docs.sarvam.ai/api/getting-started/pricing))  
  
## Key capabilities

Long context

Process up to 1,048,576 tokens across the prompt, reasoning, and generated output.

Reasoning on or off

Thinks by default; turn thinking off for faster, cheaper direct answers.

Image, audio, and video input

Send base64 images, audio, and video alongside text.

Tool calling

Use OpenAI-compatible `tools` and `tool_choice` for agentic workflows.

Structured output

Constrain answers with `response_format` JSON schemas.

Log probabilities

Request `logprobs` and `top_logprobs`, and `n` > 1 choices.

Moving from [OpenRouter](https://docs.sarvam.ai/api/token-factory/migrations/from-openrouter/overview), [Fireworks AI](https://docs.sarvam.ai/api/token-factory/migrations/from-fireworks/overview), or [Together AI](https://docs.sarvam.ai/api/token-factory/migrations/from-together/overview)? The migration guides map model IDs and request fields to Sarvam.

## Quickstart

PythonJavaScriptcURL
    
    
    from sarvamai import SarvamAI
    
    client = SarvamAI(api_subscription_key="YOUR_SARVAM_API_KEY")
    
    response = client.chat.completions_v2(
    
        model="mimo-v2.6-pro",
    
        messages=[
    
            {
    
                "role": "user",
    
                "content": "List three ways to reduce cold-start latency in a serverless API.",
    
            }
    
        ],
    
        max_tokens=2000,
    
    )
    
    print(response.choices[0].message.content)

## Supported parameters

`model: "mimo-v2.6-pro"` on [Chat Completion V2](https://docs.sarvam.ai/api-reference/chat/chat-completions-v2) and [Responses](https://docs.sarvam.ai/api-reference/responses/create). Full request/response schemas live on those API reference pages; this table covers what’s actually accepted for this model.

Parameter| Chat Completion V2| Responses  
---|---|---  
Streaming (`stream`)| |   
Image input (base64)| `image_url`| `input_image`  
Audio input (base64)| `input_audio` or `audio_url`| `input_audio` only  
Video input (base64)| `video_url`| `400`  
Tool calling (`tools`, `tool_choice`)| |   
`parallel_tool_calls: false` enforced| |   
Structured output (`response_format` / `text.format`)| |   
Log probabilities (`logprobs`, `top_logprobs`)| |  send `top_logprobs` with `include: ["message.output_text.logprobs"]`; `logprobs: true` returns `400`  
Multiple choices (`n` > 1)| | N/A — Responses has no `n`  
Reasoning control| Any value but `"none"` just switches thinking on; doesn’t change effort| Same behaviour via `reasoning.effort`  
Turn reasoning off| `reasoning_effort: "none"`| `reasoning.effort: "none"`  
  
## Reasoning

MiMo V2.6 Pro **thinks by default**. Thinking is either on or off: any effort value other than `"none"` (`low`, `high`, `max`, and so on) only switches thinking on; it doesn’t change how much the model thinks.

Turn thinking off with any of:

Setting| Where  
---|---  
`reasoning_effort: "none"`| [Chat Completion V2](https://docs.sarvam.ai/api-reference/chat/chat-completions-v2); `reasoning.effort: "none"` on [Responses](https://docs.sarvam.ai/api-reference/responses/create)  
`thinking: {"type": "disabled"}`| Through `extra_body` in the SDKs  
`chat_template_kwargs: {"enable_thinking": false}`| Through `extra_body` in the SDKs  
      
    
    response = client.chat.completions_v2(
    
        model="mimo-v2.6-pro",
    
        messages=[{"role": "user", "content": "What is 17 × 23?"}],
    
        extra_body={"thinking": {"type": "disabled"}},
    
        max_tokens=2000,
    
    )

Read the reasoning trace from `choices[].message.reasoning_content` on chat. On Responses, `output` starts with a `reasoning` item; read its `content[0].text` (`summary` is empty). Reasoning tokens are billed as output tokens and count against `max_tokens` / `max_output_tokens`.

## Tool calling

Pass OpenAI-compatible `tools`. `tool_choice` accepts `"auto"`, `"none"`, `"required"`, or a named function (`{"type": "function", "function": {"name": "..."}}`). The model can return several tool calls in one turn; set `parallel_tool_calls: false` to get at most one.

## Structured output

Pass a JSON schema in `response_format`:
    
    
    response = client.chat.completions_v2(
    
        model="mimo-v2.6-pro",
    
        messages=[{"role": "user", "content": "Give a city and its country."}],
    
        response_format={
    
            "type": "json_schema",
    
            "json_schema": {
    
                "name": "city",
    
                "strict": True,
    
                "schema": {
    
                    "type": "object",
    
                    "properties": {
    
                        "city": {"type": "string"},
    
                        "country": {"type": "string"},
    
                    },
    
                    "required": ["city", "country"],
    
                    "additionalProperties": False,
    
                },
    
            },
    
        },
    
        max_tokens=2000,
    
    )

## Media input

MiMo V2.6 Pro accepts **images, audio, and video** alongside text. Send every file **inline as a base64 data URI** ; remote `http(s)` URLs return `400`.

Input| Chat Completion V2| Responses| Formats  
---|---|---|---  
Image| `image_url` part| `input_image` part| PNG, JPEG, WebP, GIF, BMP, TIFF  
Audio| `input_audio` part (`data`, `format`: `wav` or `mp3`), or `audio_url` part with a data URI (WAV, MP3, FLAC, OGG, Opus)| `input_audio` part only (`wav` or `mp3`)| WAV, MP3, FLAC, OGG, Opus  
Video| `video_url` part with a data URI| Not supported| MP4  
      
    
    import base64
    
    def data_uri(path, mime):
    
        with open(path, "rb") as f:
    
            return f"data:{mime};base64," + base64.b64encode(f.read()).decode()
    
    with open("question.wav", "rb") as f:
    
        audio_b64 = base64.b64encode(f.read()).decode()
    
    response = client.chat.completions_v2(
    
        model="mimo-v2.6-pro",
    
        messages=[
    
            {
    
                "role": "user",
    
                "content": [
    
                    {"type": "text", "text": "Answer the question in the audio, using the chart and the clip."},
    
                    {"type": "image_url", "image_url": {"url": data_uri("chart.png", "image/png")}},
    
                    {"type": "input_audio", "input_audio": {"data": audio_b64, "format": "wav"}},
    
                    {"type": "video_url", "video_url": {"url": data_uri("clip.mp4", "video/mp4")}},
    
                ],
    
            }
    
        ],
    
        max_tokens=2000,
    
    )

**Thinking and audio:** when the latest user message contains audio, the model answers without thinking by default. To think anyway, send `chat_template_kwargs: {"enable_thinking": true}` (through `extra_body` in the SDKs). Audio in earlier turns doesn’t change the default.

**Limits:**

  * Request body up to 40 MiB, including base64 media. Base64 adds about 33%, so about 30 MB of raw media fits in one request.
  * Up to 999 files of each type per request.
  * Images are resized to about 8.4 megapixels.
  * Video is sampled to 32 frames. Resolution isn’t capped: higher-resolution video, including 4K, is accepted and uses more tokens.
  * Audio up to 10 minutes per file.



Media tokens are billed as input and reported in `usage.prompt_tokens_details` as `image_tokens`, `audio_tokens`, and `video_tokens`.

## Known limitations

  * Media must be inline base64; remote URLs return `400`. Video works on Chat Completion V2 only.
  * Plain one-colour images are often described as “white” or “black”.
  * Reasoning and the final answer share the **`max_tokens`** / **`max_output_tokens`** budget.
  * `stop` strings match the answer only, not the thinking.
  * Set **`max_tokens`** explicitly. When it’s omitted, generation isn’t capped at a small default and long answers can run to tens of thousands of tokens.



## Limits and errors

Area| Limit or condition| API response| Recommended action  
---|---|---|---  
Output| `max_tokens` exceeds 1,048,576| `400 invalid_request_error`| Set `max_tokens` within the context window.  
Request size| Request body exceeds 40 MiB (41,943,040 bytes)| `413 invalid_request_error`, with the limit in the message| Send smaller or fewer media files. Base64 adds about 33%, so about 30 MB of raw media fits.  
Media URL| An image, audio, or video part uses an `http(s)` URL| `400 invalid_request_error`| Send the file inline as a base64 data URI.  
Video on Responses| A Responses request includes video| `400 invalid_request_error`| Send video on Chat Completion V2.  
Media count| More than 999 files of one type in a request| Request rejected| Split the request.  
Reasoning| Reasoning consumes the full `max_tokens` budget| `200` with `finish_reason: "length"`| Raise `max_tokens` or lower the reasoning effort.  
Authentication| API key is missing or invalid| `403 invalid_api_key_error`| Check the `api-subscription-key` header.  
Model| Model ID is unknown or unavailable| `404 not_found_error`| Check the spelling; model IDs are case-sensitive.  
Quota| No credits remain| `402 insufficient_quota_error`| Add credits in the [dashboard](https://indus.sarvam.ai/billing?ref=docs).  
Rate limit| Request or concurrency limit is exceeded| `429 rate_limit_exceeded_error`| Back off and retry.  
Availability| Model remains overloaded after retries| `503 model_overloaded`| Retry later.  
  
Was this page helpful?

YesNo

[Previous](https://docs.sarvam.ai/api/token-factory/models/mimo-v2.6-flash)[Chat Completion APINext](https://docs.sarvam.ai/api/token-factory/chat-completions)[Built with](https://buildwithfern.com/?utm_source=others&utm_medium=organic&utm_campaign=fern_indocs_url&utm_content=book_demo&utm_term=docs.sarvam.ai)

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


