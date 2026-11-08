---
url: https://docs.sarvam.ai/api/token-factory/models/clef/
title: Clef | Sarvam API Docs
method: scrapling+scrapegraph
fetched_at: 2026-11-08T01:52:35.667411+00:00
---

# Clef | Sarvam API Docs

> Source: https://docs.sarvam.ai/api/token-factory/models/clef/

Skip to navigation

On this page

  * At a glance
  * Quickstart
  * Questions about images
  * Question rules
  * Limits
  * Differences from Sarvam Prism
  * Errors



Scroll to top

[Token Factory (Open-Weight)](https://docs.sarvam.ai/api/token-factory)[Models](https://docs.sarvam.ai/api/token-factory/models)

# Clef

Ask a question|Copy page|[View as Markdown](https://docs.sarvam.ai/api/token-factory/models/clef.md "View this page as plain text")|More actions

This page is for Model APIs.

Clef is a 27B open-weight **decision model**. Like [Sarvam Prism](https://docs.sarvam.ai/api/token-factory/models/sarvam-prism), it answers typed questions about an input on the [Decisions API](https://docs.sarvam.ai/api/token-factory/decisions-api): you send a **state** and a map of **questions** , and it returns a probability for every option of every question in one pass. It generates no text, so there is nothing to parse.

Unlike Sarvam Prism, Clef also reads **images** , and it takes up to 65,536 tokens per request.

Clef is available on **Provisioned Throughput** : capacity is set up for your workload and enabled for your organisation. Without access, requests return `404 not_found_error` and the model isn’t listed in [`GET /v2/models`](https://docs.sarvam.ai/api-reference/chat/models-v2). [Contact us](https://docs.sarvam.ai/api/getting-started/help) to request access. See [Provisioned Throughput](https://docs.sarvam.ai/api/token-factory/models#provisioned-throughput).

## At a glance

|   
---|---  
**Model ID**| `clef`  
**What it does**|  Answers yes/no (`noul`), pick-one (`choice`) and ordered-scale (`score`) questions about your input, with a probability for every option  
**API**| [Decisions API](https://docs.sarvam.ai/api/token-factory/decisions-api) (`POST /v2/systemone`, [reference](https://docs.sarvam.ai/api-reference/decisions/systemone)), synchronous JSON, no streaming  
**Input**|  Text, or any JSON object or array (rendered as JSON), plus optional base64 images  
**Input limits**|  65,536 tokens per request (state, all questions and options, and images), 1–255 options per `choice`, 1–10 levels per `score`. [Details](https://docs.sarvam.ai/api/token-factory/models/clef#limits)  
**Output**|  Probabilities that sum to 1 for each question, plus the top option, a confidence value, and (for `score`) a legend  
**Repeatability**|  The same request returns the same probabilities  
**Pricing**|  ₹20 per 1M input tokens; no output tokens are billed ([Pricing](https://docs.sarvam.ai/api/getting-started/pricing)). Check `usage.input_tokens` for the exact count  
  
## Quickstart

PythoncURL
    
    
    from sarvamai import SarvamAI
    
    client = SarvamAI(api_subscription_key="YOUR_SARVAM_API_KEY")
    
    response = client.decisions.create(
    
        model="clef",
    
        state="My Stripe integration stopped working and all checkout payments are failing.",
    
        questions={
    
            "urgent": {
    
                "type": "noul",
    
                "instructions": "Is this urgent and revenue-impacting?",
    
            },
    
            "department": {
    
                "type": "choice",
    
                "instructions": "Which team should handle this?",
    
                "criteria": {
    
                    "billing": "Payments or invoices",
    
                    "technical": "Bugs or outages",
    
                    "sales": "New business enquiries",
    
                },
    
            },
    
            "severity": {
    
                "type": "score",
    
                "instructions": "Rate the severity.",
    
                "criteria": ["trivial", "minor", "moderate", "major", "critical"],
    
            },
    
        },
    
    )
    
    answers = response.answers
    
    if answers["urgent"].noul > 0.5:
    
        print("Escalate to", answers["department"].choice)

Response:
    
    
    {
    
      "model": "clef",
    
      "answers": {
    
        "urgent": {"type": "noul", "noul": 0.9926},
    
        "department": {
    
          "type": "choice",
    
          "choice": "billing",
    
          "confidence": 0.3099,
    
          "probabilities": {"billing": 0.5400, "technical": 0.4476, "sales": 0.0124}
    
        },
    
        "severity": {
    
          "type": "score",
    
          "score": 3.8746,
    
          "confidence": 0.8955,
    
          "legend": {"0": "trivial", "1": "minor", "2": "moderate", "3": "major", "4": "critical"},
    
          "probabilities": {"0": 0.0071, "1": 0.0068, "2": 0.0089, "3": 0.0587, "4": 0.9184}
    
        }
    
      },
    
      "usage": {"input_tokens": 357, "output_tokens": 0}
    
    }

Probabilities are rounded here; the API returns full floats. For what each field means, see [Read the answers](https://docs.sarvam.ai/api/token-factory/decisions-api#read-the-answers).

## Questions about images

Send images in `images`, as base64 data URIs. The questions are answered about the state and the images together. Remote `http(s)` image URLs return `400`.

The `sarvamai` SDK’s `decisions.create` doesn’t have an `images` argument yet, so pass the images as an extra body field:
    
    
    import base64
    
    with open("receipt.jpg", "rb") as f:
    
        image = "data:image/jpeg;base64," + base64.b64encode(f.read()).decode()
    
    response = client.decisions.create(
    
        model="clef",
    
        state="Review the attached receipt.",
    
        questions={"legible": {"type": "noul", "instructions": "Is the receipt total legible?"}},
    
        request_options={"additional_body_parameters": {"images": [image]}},
    
    )
    
    print(response.answers["legible"].noul)

In the JavaScript SDK, put `images` directly in the request object: `client.decisions.create({ model: "clef", state, questions, images: [image] })`. Its `requestOptions` can’t add body fields.

Over HTTP, send `images` in the request body:
    
    
    {
    
      "model": "clef",
    
      "state": "Review the attached receipt.",
    
      "images": ["data:image/jpeg;base64,/9j/4AAQ..."],
    
      "questions": {
    
        "legible": {"type": "noul", "instructions": "Is the receipt total legible?"}
    
      }
    
    }

## Question rules

The question types are the same as on Sarvam Prism ([Question types](https://docs.sarvam.ai/api/token-factory/decisions-api#question-types)), with these rules on Clef:

`type`| `criteria`| Rules  
---|---|---  
`noul`| Optional `{"true": "...", "false": "..."}`| Needs `instructions`, or at least one of `criteria.true` and `criteria.false`.  
`choice`| Required object `{option_id: description or null}`| 1–255 options.  
`score`| Required **array** of level descriptions, lowest first| 1–10 levels, numbered from 0. An object returns `422`.  
  
  * Always send `instructions` (or `noul` criteria). The question ID is not used as the question.
  * Any key in a question other than `type`, `instructions`, and `criteria` returns `422`, including misspellings such as `instruction`.
  * `temperature` returns `422`. `max_tokens` and `stream` are accepted and ignored: Clef always answers in one JSON response.
  * `chat_template_kwargs` must be empty or absent; a non-empty value returns `400`.
  * `videos` and other unknown top-level fields are ignored.



## Limits

  * **65,536 tokens per request** , counting the state, every question and its options, and images. The state is counted once, however many questions you ask.
  * **The state is never truncated.** A request over the limit fails with `400 invalid_request_error`, and the message gives the count, such as “the prompt needs 70141 tokens (70001 for the state), but holds at most 65536”. Shorten the state, or split a long document across requests.
  * Ask several questions about the same state in one request: they are answered together, in one pass.



## Differences from Sarvam Prism

| Clef| Sarvam Prism  
---|---|---  
Images| Supported (`images`, base64)| Not supported  
Token limit| 65,536 per request| 32,768 per question  
Over-long state| Rejected with `400`| Rejected with `422`  
`choice` options| 1–255| 2–255  
`score` levels| 1–10, array only| 2–10  
Repeatability| Identical probabilities for identical requests| Can vary slightly; the top answer is stable  
Access| Provisioned Throughput| Serverless  
  
## Errors

Status| When| Recommended action  
---|---|---  
`404 not_found_error`| Your organisation does not have Provisioned Throughput for Clef| [Contact us](https://docs.sarvam.ai/api/getting-started/help) to request access.  
`400 invalid_request_error`| The prompt is over 65,536 tokens, an image is a remote URL, or an image can’t be read| Shorten the state, or send images as base64 data URIs.  
`400 invalid_request_error`| Clef is called on another endpoint, such as `/v2/chat/completions` (“served only on /v2/systemone”)| Send decisions to `POST /v2/systemone`.  
`422 unprocessable_entity_error`| Missing `state` or `questions`, empty `questions`, unknown `type`, unknown key in a question, too many options or levels, a `noul` with nothing to decide, or `temperature`| Fix the request. `param` names the field at fault.  
`403 invalid_api_key_error`| API key is missing or invalid| Check the `api-subscription-key` header.  
`429 rate_limit_exceeded_error`| Request or concurrency limit is exceeded| Back off and retry.  
`5xx`| Server or capacity error| Retry with backoff.  
  
Every error carries `message`, `code`, and `request_id`; validation errors also carry `param`.

Was this page helpful?

YesNo

[Previous](https://docs.sarvam.ai/api/token-factory/models/qwen-3-8-27b)[EmbeddingGemma 2Next](https://docs.sarvam.ai/api/token-factory/models/embeddinggemma-2)[Built with](https://buildwithfern.com/?utm_source=others&utm_medium=organic&utm_campaign=fern_indocs_url&utm_content=book_demo&utm_term=docs.sarvam.ai)

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


