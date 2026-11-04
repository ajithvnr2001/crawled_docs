---
url: https://docs.sarvam.ai/api/token-factory/decisions-api/
title: Decisions API | Sarvam API Docs
method: scrapling+scrapegraph
fetched_at: 2026-11-03T16:23:02.803403+00:00
---

# Decisions API | Sarvam API Docs

> Source: https://docs.sarvam.ai/api/token-factory/decisions-api/

Skip to navigation

On this page

  * Make a decision
  * Question types
  * Yes/no with criteria
  * Choice
  * Score
  * Ask several questions at once
  * Read the answers
  * Act on confidence
  * Send structured state
  * Parameters
  * Refused or unsupported on this route
  * Limits and billing



Scroll to top

[Token Factory (Open-Weight)](https://docs.sarvam.ai/api/token-factory)

# Decisions API

Ask a question|Copy page|[View as Markdown](https://docs.sarvam.ai/api/token-factory/decisions-api.md "View this page as plain text")|More actions

This page is for Model APIs.

The Decisions API answers typed questions about an input. You send a **state** (the input to decide on) and a map of **questions** , and every answer comes back as a typed value with a probability for every option. Nothing is generated, so there is no text to parse and no output format to enforce.

Use it wherever you would otherwise prompt a chat model to “answer yes or no” or “reply with one of these labels”: routing, triage, moderation, judging agent runs, and scoring.

The Decisions API serves [Sarvam Prism](https://docs.sarvam.ai/api/token-factory/models/sarvam-prism) (`sarvam-prism`). The SDK examples need `sarvamai` 0.1.43 or later for Python (`pip install -U "sarvamai>=0.1.43"`) and `sarvamai` 1.1.15 or later for JavaScript (`npm install sarvamai@latest`).

## Make a decision

Use [`POST /v2/systemone`](https://docs.sarvam.ai/api-reference/decisions/systemone). One request answers every question in `questions`, and each answer comes back under the same ID.

PythonJavaScriptcURL
    
    
    from sarvamai import SarvamAI
    
    client = SarvamAI(api_subscription_key="YOUR_SARVAM_API_KEY")
    
    response = client.decisions.create(
    
        model="sarvam-prism",
    
        state="The customer asked for a refund within the 30-day window.",
    
        questions={
    
            "refund": {
    
                "type": "noul",
    
                "instructions": "Should we approve the refund?",
    
            },
    
        },
    
    )
    
    print(response.answers["refund"].noul)

Response:
    
    
    {
    
      "model": "sarvam-prism",
    
      "answers": {
    
        "refund": { "type": "noul", "noul": 0.8646 }
    
      },
    
      "usage": { "input_tokens": 45, "output_tokens": 0 }
    
    }

`noul` is the probability that the answer is yes. `output_tokens` is always `0`.

## Question types

Every question has a `type`. Its `criteria` define the options, and its answer has a matching shape.

`type`| Asks| `criteria`| Answer fields  
---|---|---|---  
`noul`| Yes or no| Optional. `{"true": "…", "false": "…"}`| `noul`  
`choice`| Pick one option| Required. Object of option ID → description, 2 to 255 options| `choice`, `confidence`, `probabilities`  
`score`| Rate on an ordered scale| Required. List of levels, lowest first, 2 to 10 levels| `score`, `confidence`, `legend`, `probabilities`  
  
`instructions` is the question to ask about the state: a string, or an object or array rendered as JSON. A `noul` needs `instructions`, `criteria`, or both. For `choice` and `score`, `instructions` is optional but usually makes the question clearer.

### Yes/no with criteria

Describe when each answer applies in `criteria`:
    
    
    {
    
      "type": "noul",
    
      "instructions": "Should we approve the refund?",
    
      "criteria": {
    
        "true": "The request meets the refund policy",
    
        "false": "The request breaks the refund policy"
    
      }
    
    }

### Choice

Write each option’s description as the condition under which it applies. Option IDs come back verbatim as the keys of `probabilities`, and the order you list them in does not affect the answer.
    
    
    {
    
      "type": "choice",
    
      "instructions": "Which team should handle this?",
    
      "criteria": {
    
        "billing": "Payments or invoices",
    
        "technical": "Bugs or outages",
    
        "sales": "New business enquiries"
    
      }
    
    }

### Score

List the levels from lowest to highest. The answer keys them `"0"`, `"1"`, … in your order, and `legend` maps each key back to your text.
    
    
    {
    
      "type": "score",
    
      "instructions": "Rate the severity.",
    
      "criteria": ["trivial", "minor", "moderate", "major", "critical"]
    
    }

## Ask several questions at once

Put every question about the same state in one request. The state is counted once per request, so extra questions add only their own tokens.

PythonJavaScriptcURL
    
    
    from sarvamai import SarvamAI
    
    client = SarvamAI(api_subscription_key="YOUR_SARVAM_API_KEY")
    
    response = client.decisions.create(
    
        model="sarvam-prism",
    
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
    
    for question_id, answer in response.answers.items():
    
        if answer.type == "noul":
    
            print(question_id, "yes" if answer.noul > 0.5 else "no", answer.noul)
    
        elif answer.type == "choice":
    
            print(question_id, answer.choice, answer.probabilities[answer.choice])
    
        elif answer.type == "score":
    
            print(question_id, answer.score, answer.legend[str(round(answer.score))])

Response:
    
    
    {
    
      "model": "sarvam-prism",
    
      "answers": {
    
        "urgent": { "type": "noul", "noul": 0.9782 },
    
        "department": {
    
          "type": "choice",
    
          "choice": "billing",
    
          "confidence": 0.7065,
    
          "probabilities": { "billing": 0.8044, "technical": 0.1869, "sales": 0.0087 }
    
        },
    
        "severity": {
    
          "type": "score",
    
          "score": 3.832,
    
          "confidence": 0.916,
    
          "legend": { "0": "trivial", "1": "minor", "2": "moderate", "3": "major", "4": "critical" },
    
          "probabilities": { "0": 0.0026, "1": 0.0034, "2": 0.0115, "3": 0.1245, "4": 0.8581 }
    
        }
    
      },
    
      "usage": { "input_tokens": 153, "output_tokens": 0 }
    
    }

Every answer carries its `type`, so switching on it narrows the answer to the right shape in the typed SDKs.

## Read the answers

Field| Type| Description  
---|---|---  
`noul`| number| Probability from 0 to 1 that the answer is yes.  
`choice`| string| The option ID with the highest probability.  
`score`| number| Expected level, `Σ index × probability` with levels indexed from 0. A float such as `3.83`: round it if you need a level.  
`probabilities`| object| Probability for every option or level, keyed by option ID (`choice`) or `"0"`, `"1"`, … (`score`). Sums to 1.  
`confidence`| number| How decisive the answer is, from 0 to 1. For `choice`, the top probability rescaled so that an even split is 0 and certainty is 1: `(p_top − 1/n) / (1 − 1/n)` for `n` options. For `score`, 0 when probability is spread across the scale and 1 when it all sits on one level.  
`legend`| object| `score` only. Your level text, keyed the same way as `probabilities`.  
  
Probabilities can vary slightly between identical requests; the top answer is stable.

## Act on confidence

Sarvam Prism’s probabilities are calibrated: an answer given with 90% probability is wrong about 10% of the time or less. Act on confident answers automatically and send the rest to a person.
    
    
    from sarvamai import SarvamAI
    
    client = SarvamAI(api_subscription_key="YOUR_SARVAM_API_KEY")
    
    THRESHOLD = 0.9
    
    response = client.decisions.create(
    
        model="sarvam-prism",
    
        state="I was charged twice for my last order.",
    
        questions={
    
            "department": {
    
                "type": "choice",
    
                "instructions": "Which team should handle this?",
    
                "criteria": {
    
                    "billing": "Payments or invoices",
    
                    "technical": "Bugs or outages",
    
                    "sales": "New business enquiries",
    
                },
    
            },
    
        },
    
    )
    
    answer = response.answers["department"]
    
    if answer.probabilities[answer.choice] >= THRESHOLD:
    
        print("Route to", answer.choice)
    
    else:
    
        print("Send to a person")

Set the threshold on the top probability (`noul`, or `probabilities[choice]`), not on `confidence`: the calibration figures on the [Sarvam Prism page](https://docs.sarvam.ai/api/token-factory/models/sarvam-prism#acting-on-confidence) refer to the probability.

## Send structured state

`state` can be a string, an object, or an array. Objects and arrays are rendered as compact JSON, so you can pass a record as it is.
    
    
    from sarvamai import SarvamAI
    
    client = SarvamAI(api_subscription_key="YOUR_SARVAM_API_KEY")
    
    response = client.decisions.create(
    
        model="sarvam-prism",
    
        state={"invoice": {"vendor": "Acme", "total": 1250, "status": "overdue"}},
    
        questions={
    
            "follow_up": {
    
                "type": "choice",
    
                "instructions": "When should we follow up?",
    
                "criteria": {
    
                    "later": "Can wait",
    
                    "this_week": "This week",
    
                    "today": "Today",
    
                },
    
            },
    
        },
    
    )
    
    print(response.answers["follow_up"].choice)

## Parameters

Parameter| Required| Description  
---|---|---  
`model`| Yes| `sarvam-prism`. A request without `model` returns `400`; an unknown ID returns `404`.  
`state`| Yes| A string, object, or array. An empty string is allowed; a missing or `null` state returns `422`. Never truncated.  
`questions`| Yes| Map of your question ID to a question, at least one. There is no cap on the number of questions.  
  
Each question accepts only these keys:

Key| Required| Description  
---|---|---  
`type`| Yes| `noul`, `choice`, or `score` (lowercase).  
`instructions`| `noul`: if no `criteria`| The question to ask about the state. A string, or an object or array rendered as JSON.  
`criteria`| `choice`, `score`| The options, see [Question types](https://docs.sarvam.ai/api/token-factory/decisions-api#question-types).  
  
### Refused or unsupported on this route

The Decisions API returns probabilities only, so generation settings don’t apply:

  * `temperature`, `max_tokens`, `stream`, and other generation fields return `422`.
  * Images are not supported. An image URL in `images` returns `400`; an inline image returns `422`.
  * Any key in a question other than `type`, `instructions`, and `criteria` returns `422`, including misspellings such as `instruction`.
  * A `choice` outside 2–255 options or a `score` outside 2–10 levels returns `422`.



## Limits and billing

  * **32,768 tokens per question** (state + that question’s instructions and options). If any one question is over, the whole request fails with `422` and names the question.
  * **60 seconds per request.** A longer request fails with `503 model_overloaded`; split very large batches of questions across several requests.
  * **Pricing:** ₹4 per 1M input tokens and ₹0 per 1M output tokens, on every plan. Check `usage.input_tokens` for the exact count.



Errors return `message`, `code` and `request_id`; validation errors also return `param`, the path to the field at fault, such as `questions.urgent.noul.instruction`. See the [Sarvam Prism page](https://docs.sarvam.ai/api/token-factory/models/sarvam-prism#errors) for the error table and the [Decisions API Reference](https://docs.sarvam.ai/api-reference/decisions/systemone) for the complete request and response schemas.

Was this page helpful?

YesNo

[Previous](https://docs.sarvam.ai/api/token-factory/responses-api)[How to list your chat messagesNext](https://docs.sarvam.ai/api/token-factory/how-to/list-your-chat-messages)[Built with](https://buildwithfern.com/?utm_source=others&utm_medium=organic&utm_campaign=fern_indocs_url&utm_content=book_demo&utm_term=docs.sarvam.ai)

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
  * [Kimi K3](https://docs.sarvam.ai/api/token-factory/models/kimi-k3)
  * [MiMo V2.6 Flash](https://docs.sarvam.ai/api/token-factory/models/mimo-v2.6-flash)
  * [MiMo V2.6 Pro](https://docs.sarvam.ai/api/token-factory/models/mimo-v2.6-pro)
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
  * [Doc Agents](https://docs.sarvam.ai/docai)
  * [Content Studio](https://docs.sarvam.ai/creative)
  * [Cowork](https://docs.sarvam.ai/cowork)
  * [API Reference](https://docs.sarvam.ai/api-reference)
  * [Changelog](https://docs.sarvam.ai/changelog)


