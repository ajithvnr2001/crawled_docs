---
url: https://docs.sarvam.ai/api/token-factory/models/sarvam-prism/
title: Sarvam Prism | Sarvam API Docs
method: scrapling+scrapegraph
fetched_at: 2026-11-03T16:23:01.136887+00:00
---

# Sarvam Prism | Sarvam API Docs

> Source: https://docs.sarvam.ai/api/token-factory/models/sarvam-prism/

Skip to navigation

On this page

  * At a Glance
  * Key Features
  * How It Answers
  * Quickstart
  * Request
  * Question types
  * Response
  * Reading answers
  * Acting on confidence
  * Option order
  * Repeatability
  * Limits
  * Token usage
  * Errors
  * Examples
  * Known limitations



Scroll to top

[Token Factory (Open-Weight)](https://docs.sarvam.ai/api/token-factory)[Models](https://docs.sarvam.ai/api/token-factory/models)

# Sarvam Prism

Ask a question|Copy page|[View as Markdown](https://docs.sarvam.ai/api/token-factory/models/sarvam-prism.md "View this page as plain text")|More actions

This page is for Model APIs.

**Sarvam Prism (System-1 Decision Model)**

Sarvam Prism is a **System-1 decision model built on Sarvam 105B** : a model for the fast, intuitive judgements that make up most of an enterprise’s daily work, where each decision is a choice among a known set of options. You send it a **state** (the input to decide on) and a set of **typed questions** , and it returns a calibrated probability for every option of every question in one call. It does not generate text, so there is nothing to parse and no output format to enforce: every answer is already a typed value.

Use it where you would otherwise prompt a chat model to “answer yes or no” or “reply with one of these labels” and then parse the reply: routing, triage, moderation, judging agent runs, security checks, and scoring.

**Highlights:**

  * **71.8** average across three decision indices, including **82.5** on an Indian-language benchmark
  * **Calibrated confidence:** makes fewer mistakes than its confidence promises at every level measured, in English and in Indian languages
  * **Same answer in any order:** options are scored in a fixed internal order, so shuffling them does not change the result



## At a Glance

|   
---|---  
**Model ID**| `sarvam-prism`  
**Built on**| [Sarvam 105B](https://docs.sarvam.ai/api/token-factory/models/sarvam-105b)  
**What it does**|  Answers yes/no (`noul`), pick-one (`choice`) and ordered-scale (`score`) questions about your input, with a probability for every option  
**API**| [Decisions API](https://docs.sarvam.ai/api/token-factory/decisions-api) (`POST /v2/systemone`, [reference](https://docs.sarvam.ai/api-reference/decisions/systemone)), synchronous JSON, no streaming  
**Input**|  Text, or any JSON object or array (rendered as compact JSON). Images are not supported.  
**Languages**|  English, 10 Indian languages, and Hinglish  
**Input limits**|  32,768 tokens per question (state + question + options), 2–255 options per `choice`, 2–10 levels per `score`. No cap on the number of questions. Each request must finish within 60 seconds. [Details](https://docs.sarvam.ai/api/token-factory/models/sarvam-prism#limits)  
**Output**|  Probabilities that sum to 1 for each question, plus the top option and a confidence value.  
**Pricing**|  ₹4 per 1M input tokens and ₹0 per 1M output tokens, on every plan. [Pricing page](https://docs.sarvam.ai/api/getting-started/pricing)  
**Best for**|  Routing, triage, moderation, judging agent runs, security checks (such as prompt injection), and scoring, wherever a confident answer can run on its own  
**Known limitations**| [See below](https://docs.sarvam.ai/api/token-factory/models/sarvam-prism#known-limitations)  
  
## Key Features

Accurate

Scores 71.8 averaged across the Jev Decision Index (67.0), a recreation of the Artificial Analysis Decision Index (65.9), and an Indian-language benchmark (82.5).

Confidence You Can Trust

On answers given with at least 90% confidence, Prism expects 3.3% to be wrong and gets 2.2% wrong across 37 public benchmarks, and expects 5.4% and gets 4.4% in Indian languages. Act on confident answers automatically and send only the uncertain ones to a person.

Same Answer in Any Order

Options often come from code, such as a catalogue, a tool list, or a set of intents, so their order is arbitrary. Prism sorts them into a fixed order before scoring and returns probabilities under your option names, so reordering options changes nothing.

Built for Enterprise Decisions

78.5% accuracy judging recorded agent runs (task success, need for review, the agent responsible for a failure) and 89.0% on a security benchmark that includes prompt-injection and jailbreak checks.

## How It Answers

Prism scores every option of every question and returns one probability per option. It generates no text, so there is no output to parse and output costs nothing. Each option is scored independently of the others, so one option’s wording cannot sway another’s score.

For benchmarks and methodology, see the [Sarvam Prism blog](https://www.sarvam.ai/blogs/sarvam-prism).

## Quickstart

Send one request with three questions about the same support ticket:

The SDK examples need `sarvamai` 0.1.43 or later for Python (`pip install -U "sarvamai>=0.1.43"`) and `sarvamai` 1.1.15 or later for JavaScript (`npm install sarvamai@latest`).

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
    
    answers = response.answers
    
    if answers["urgent"].noul > 0.5:
    
        print("Escalate to", answers["department"].choice)

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

You can also authenticate with `Authorization: Bearer $SARVAM_API_KEY`.

## Request

Field| Type| Required| Description  
---|---|---|---  
`model`| string| Yes| `sarvam-prism`. A request without `model` returns `400`; an unknown ID returns `404`.  
`state`| string, object or array| Yes| The input to decide on. Objects and arrays are rendered as compact JSON. An empty string is allowed; a missing or `null` state returns `422`. Never truncated, see [Limits](https://docs.sarvam.ai/api/token-factory/models/sarvam-prism#limits).  
`questions`| object| Yes| Map of your question ID to a question, at least one. Each answer comes back under the same ID. A missing or empty `questions` returns `422`.  
  
Generation fields such as `temperature`, `max_tokens`, `stream` and `images` are not supported and return `422` (an image URL returns `400`).

### Question types

Every question has a `type` (`noul`, `choice` or `score`, lowercase) and usually an `instructions` string: the question to ask about the state. `instructions` can also be an object or array, rendered as JSON. Only `type`, `instructions` and `criteria` are accepted; any other key in a question, including a misspelling such as `instruction`, returns `422`.

`type`| `criteria`| Answer  
---|---|---  
`noul` (yes/no)| Optional. Object with `true` and `false` keys describing when each answer applies. Send `instructions`, `criteria`, or both.| `noul`: probability of yes  
`choice`| Required. Object of option ID → description, 2 to 255 options| `choice`: the most likely option ID, `confidence`, and `probabilities` for every option  
`score`| Required. List of level descriptions, lowest first, 2 to 10 levels| `score`: expected level, `confidence`, `legend`, and `probabilities` for every level  
  
For `choice`, write each description as the condition under which that option applies. An option whose description is `null` or empty is shown to the model as the bare ID.

## Response

Field| Description  
---|---  
`model`| `sarvam-prism`  
`answers`| One answer per question, keyed by your question ID. Each answer carries its `type`.  
`usage.input_tokens`| Prompt tokens for the request, see [Token usage](https://docs.sarvam.ai/api/token-factory/models/sarvam-prism#token-usage)  
`usage.output_tokens`| Always `0`: Prism returns probabilities, not text  
  
### Reading answers

  * **`noul`** : probability from 0 to 1 that the answer is yes.
  * **`choice`** : the option ID with the highest probability, and `probabilities` keyed by your option IDs. `confidence` is the top probability rescaled so that an even split across all options is 0 and certainty is 1: `(p_top − 1/n) / (1 − 1/n)` for `n` options. With 3 options, a top probability of 0.80 gives a confidence of 0.70.
  * **`score`** : `score` is the expected level, `Σ index × probability` with levels indexed from 0 (lowest first), so it is a float such as `3.83`. Round it if you need an integer level. `probabilities` and `legend` are keyed `"0"`, `"1"`, … in the order you sent the levels, and `legend` maps each key back to your level text. `confidence` runs from 0, when probability is spread across the scale, to 1, when it all sits on one level.



Each question’s probabilities are a softmax over that question’s options only and sum to 1.

### Acting on confidence

Prism’s probabilities are calibrated: an answer given with 90% confidence is wrong about 10% of the time or less. That makes a confidence threshold a safe way to automate:

  * Act on an answer automatically when its top probability (`noul`, or `probabilities[choice]`) is at or above your threshold, for example `0.9`. The calibration figures below refer to this probability, not to the rescaled `confidence` field.
  * Send answers below the threshold to a person.



At a 0.9 threshold, about 68.5% of English answers clear the bar. In Indian languages Prism is more cautious and about 38.4% clear it, so more of those decisions go to a person.

### Option order

For `choice` questions, the order of options in `criteria` does not affect the answer: Prism scores options in a fixed internal order and returns `probabilities` under your option IDs, in the order you sent them. For `score` questions, order **does** matter, because it defines the scale from lowest to highest.

### Repeatability

Probabilities can vary slightly between identical requests; the top answer is stable. Leave a margin around your thresholds rather than relying on an exact value.

## Limits

  * **32,768 tokens per question.** The limit applies to each question separately (state + that question’s text + its options), not to the whole request.
  * **The state is never truncated.** If any one question is over the limit, the whole request fails with `422` and no question is answered, with a message such as `question 'q' encodes to 40026 tokens, over the 32768-token limit of this server`. Check the size of large inputs before you send them.
  * **2 to 255 options per`choice`, 2 to 10 levels per `score`.** Outside these ranges the request fails with `422`.
  * **No cap on the number of questions.** You can send any number of questions per request; the 32,768-token limit applies to each question.
  * **60-second request timeout.** A request that takes longer than 60 seconds fails with `503 model_overloaded`, and no question is answered. Time grows with the number of questions and the size of the state, so split very large batches across several requests.



### Token usage

The state is counted **once per request** , however many questions you ask; each question adds only its own instructions and options. Putting several questions about the same state in one request is cheaper than sending them separately.

Sarvam Prism costs ₹4 per 1M input tokens and ₹0 per 1M output tokens, the same on every plan. For example, 3 short questions about a 1,000-token state use a little over 1,000 input tokens (about ₹0.004). Check `usage.input_tokens` in the response for the exact count.

## Errors

Errors use the standard Sarvam shape. Validation errors also carry `param`, the path to the field at fault. Branch on the HTTP status and `code`, not on the message text.
    
    
    {
    
      "error": {
    
        "message": "questions.urgent.noul.instruction: Extra inputs are not permitted",
    
        "code": "unprocessable_entity_error",
    
        "request_id": "20261103_78f02876-7319-4ef9-935d-adbe287f86a2",
    
        "param": "questions.urgent.noul.instruction"
    
      }
    
    }

Status| `code`| When  
---|---|---  
`400`| `invalid_request_error`| The body is not valid JSON, the body is not a JSON object, `model` is missing or not a string, or `images` contains an image URL. Each case has its own message.  
`402`| `insufficient_quota_error`| Credit balance is empty, see [Errors and troubleshooting](https://docs.sarvam.ai/api/getting-started/errors-troubleshooting)  
`403`| `invalid_api_key_error`| Missing or invalid API key  
`404`| `not_found_error`| Unknown `model`. Model IDs are case-sensitive.  
`422`| `unprocessable_entity_error`| Missing `state` or `questions`, a missing or unsupported `type`, an unknown key, options or levels outside the allowed range, an unsupported field such as `temperature`, or a question over the token limit. `param` names the field.  
`429`| `rate_limit_exceeded_error`| Too many requests per minute, or the token budget is used up  
`500`| `internal_server_error`| An internal error occurred  
`502`| `model_call_failed`| The model backend could not be reached  
`503`| `model_overloaded`| The model is overloaded or starting up, or the request took longer than [60 seconds](https://docs.sarvam.ai/api/token-factory/models/sarvam-prism#limits)  
  
Retry `429`, `502` and `503` with backoff. For a `503` on a large request, split the questions across smaller requests before retrying. Do not retry other `4xx` errors; fix the request instead.

## Examples

**One yes/no question with criteria:**
    
    
    {
    
      "model": "sarvam-prism",
    
      "state": "The customer asked for a refund within the 30-day window.",
    
      "questions": {
    
        "refund": {
    
          "type": "noul",
    
          "instructions": "Should we approve the refund?",
    
          "criteria": {
    
            "true": "The request meets the refund policy",
    
            "false": "The request breaks the refund policy"
    
          }
    
        }
    
      }
    
    }

**Structured state and a score:**
    
    
    {
    
      "model": "sarvam-prism",
    
      "state": { "invoice": { "vendor": "Acme", "total": 1250, "status": "overdue" } },
    
      "questions": {
    
        "follow_up": {
    
          "type": "score",
    
          "instructions": "How urgent is follow-up?",
    
          "criteria": ["Can wait", "This week", "Today"]
    
        }
    
      }
    
    }

The answer maps each level key back to your text in `legend`, for example `{"type": "score", "score": 1.4, "confidence": 0.36, "legend": {"0": "Can wait", "1": "This week", "2": "Today"}, "probabilities": {"0": 0.02, "1": 0.57, "2": 0.41}}`.

## Known limitations

  * **No images.** Sarvam Prism reads text only and does not support images. An `images` field is refused: image URLs return `400` and inline images return `422`.
  * **No streaming.** Every request returns one JSON response.
  * **Lower coverage in Indian languages.** Answers in Indian languages clear a 0.9 confidence threshold less often (about 38.4%, against 68.5% in English), so more of them need a person to review.



Was this page helpful?

YesNo

[Previous](https://docs.sarvam.ai/api/token-factory/models/sarvam-105b)[GLM-5.3Next](https://docs.sarvam.ai/api/token-factory/models/glm-5-3)[Built with](https://buildwithfern.com/?utm_source=others&utm_medium=organic&utm_campaign=fern_indocs_url&utm_content=book_demo&utm_term=docs.sarvam.ai)

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
      * [DeepSeek V4 ProBeta](https://docs.sarvam.ai/api/token-factory/models/deepseek-v4-pro)
      * [Kimi K3Beta](https://docs.sarvam.ai/api/token-factory/models/kimi-k3)
      * [MiMo V2.6 FlashBeta](https://docs.sarvam.ai/api/token-factory/models/mimo-v2.6-flash)
      * [MiMo V2.6 ProBeta](https://docs.sarvam.ai/api/token-factory/models/mimo-v2.6-pro)

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


