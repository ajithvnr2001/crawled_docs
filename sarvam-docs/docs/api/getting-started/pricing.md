---
url: https://docs.sarvam.ai/api/getting-started/pricing/
title: Pricing, Credits & Rate Limits | Sarvam API Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-31T06:34:15.232557+00:00
---

# Pricing, Credits & Rate Limits | Sarvam API Docs

> Source: https://docs.sarvam.ai/api/getting-started/pricing/

Skip to navigation

On this page

  * Plans
  * Credits
  * Prices by API
  * Language Models
  * Sarvam Models
  * Open-Weight Models
  * Speech to Text
  * Text to Speech
  * Text Processing
  * Document Intelligence
  * Document Translation
  * Dubbing
  * Rate Limits
  * Speech to Text limits
  * Real-time REST
  * WebSocket Streaming
  * Batch
  * Text to Speech limits
  * Real-time REST and HTTP Streaming
  * WebSocket Streaming
  * Instant Voice Cloning limits
  * Translation & Text Services limits
  * Text translation (POST /translate)
  * Document Translation
  * Language model limits
  * Default models
  * Sarvam-105B model
  * Dubbing limits
  * Document AI limits
  * Exceeding Your Limits
  * REST rate limits (429 / 503)
  * Exhausted credits (402)
  * WebSocket connection limits
  * Upgrading Your Limits



Scroll to top

[Getting Started](https://docs.sarvam.ai/api/getting-started/welcome)

# Pricing, Credits & Rate Limits

Ask a question|Copy page|[View as Markdown](https://docs.sarvam.ai/api/getting-started/pricing.md "View this page as plain text")|More actions

This page is for Model APIs.

What you pay and how much you can use, on one page: plans, credits, per-API prices, and per-API rate limits. All prices are in Indian Rupees (₹) and exclude GST. Usage is rounded as described in the billing notes for each service.

## Plans

| Pay as you go| Pro| Growth| Business| Enterprise  
---|---|---|---|---|---  
**Monthly fee**|  None| ₹9,999| ₹49,999| ₹1,99,999| Custom  
**Support**|  Community| Email| Email| Priority| Dedicated  
**Best for**|  Prototyping & testing| Startups & POCs| Production workloads| Sustained high-volume production| Scale deployments  
  
Business includes everything in Growth, plus ₹1,99,999 worth of credits included and the best public API rates.

Choose or change a plan from the [Sarvam Dashboard](https://indus.sarvam.ai/pricing/?ref=docs). For Enterprise pricing, [contact us](https://docs.sarvam.ai/api/getting-started/help).

* * *

## Credits

Sarvam offers **₹100 worth of free credits** for every verified user on signup. These credits can be used across any of our APIs, explore, prototype, and build without upfront cost.

Credits are universal and never expire. Once exhausted, add more credits or upgrade your plan from the [Sarvam Dashboard](https://indus.sarvam.ai/billing?ref=docs).

For commercial production rights when you ship generated audio (Bulbul v3, Content Studio exports, cloned voices), see [Commercial Licensing](https://docs.sarvam.ai/api/getting-started/commercial-licensing).

If your credits are exhausted, API requests fail with `402` (`insufficient_quota_error`), which is separate from a `429` rate limit. You can add credits at any time, adding credits does **not** change your plan or rate limits.

  1. **Add Credits** : Top up from the [Billing page](https://indus.sarvam.ai/billing?ref=docs) at any time. Credits never expire.
  2. **Upgrade Your Plan** : Higher plans include bonus credits and increased rate limits.
  3. **Enterprise** : For volume discounts and custom billing arrangements, email [support@sarvam.ai](mailto:support@sarvam.ai?subject=Enterprise%20API%20Access%20Request&body=Hi%20Sarvam%20Team%2C%0A%0AI'm%20reaching%20out%20from%20%5BYour%20Company%20Name%5D%20to%20explore%20enterprise%20access%20to%20Sarvam%20AI%20APIs.%0A%0ACompany%20Details%3A%0A-%20Company%20Name%3A%20%5BYour%20Company%5D%0A-%20Industry%3A%20%5BYour%20Industry%5D%0A-%20Website%3A%20%5BYour%20Website%5D%0A%0AUse%20Case%3A%0A%5BDescribe%20your%20use%20case%20and%20how%20you%20plan%20to%20use%20our%20APIs%5D%0A%0AAPIs%20of%20Interest%3A%0A%5B%5D%20Speech-to-Text%0A%5B%5D%20Text-to-Speech%0A%5B%5D%20Translation%0A%5B%5D%20Chat%20Completion%0A%5B%5D%20Other%20\(please%20specify\)%0A%0AExpected%20Usage%3A%0A-%20Estimated%20API%20calls%20per%20month%3A%20%5BNumber%5D%0A-%20Expected%20audio%20duration%2Ftext%20volume%3A%20%5BDetails%5D%0A-%20Languages%20needed%3A%20%5BList%20languages%5D%0A%0ASpecific%20Requirements%3A%0A%5BShare%20any%20specific%20features%2C%20SLAs%2C%20or%20support%20needs%5D%0A%0ATimeline%3A%0A%5BWhen%20do%20you%20plan%20to%20start%20testing%2Fdeployment%3F%5D%0A%0ALooking%20forward%20to%20discussing%20this%20further.%0A%0ABest%20regards%2C%0A%5BYour%20Name%5D%0A%5BYour%20Title%5D%0A%5BContact%20Information%5D).



* * *

## Prices by API

Rates are listed for each self-serve plan.

### Language Models

The open-weight models (Gemma, GLM, DeepSeek, Kimi, MiMo) are served by [Token Factory](https://docs.sarvam.ai/api/token-factory).

All prices are ₹ per 1M tokens and are the same on every plan. Reasoning tokens, where applicable, are billed as output tokens.

### Sarvam Models

Model| Input| Cached input| Output| Status  
---|---|---|---|---  
Sarvam 105B (`sarvam-105b`)| ₹15| ₹5| ₹60| Available  
Sarvam 105B Chat (`sarvam-105b-conversations`)| ₹15| ₹5| ₹60| Available  
  
### Open-Weight Models

Model| Input| Cached input| Output| Status  
---|---|---|---|---  
GLM-5.3 (`glm5.3`)| ₹126| ₹20| ₹390| Available  
GLM-5.3 Flash (`glm5.3-flash`)| ₹13.5| ₹2.5| ₹45| Available  
Gemma 4 31B (`gemma4`)| ₹35| ₹10| ₹90| Available  
DeepSeek V4.1 Flash 1017 (`deepseekv4.1-flash-1017`)| ₹25| ₹0.5| ₹105| Available  
DeepSeek V4 Pro (`deepseekv4-pro`)| ₹115| ₹4| ₹350| Beta  
Kimi K3 (`kimi-k3`)| ₹270| ₹27| ₹1,350| Beta  
MiMo V2.6 Flash (`mimo-v2.6-flash`)| ₹12.5| ₹0.25| ₹25| Beta  
MiMo V2.6 Pro (`mimo-v2.6-pro`)| ₹40| ₹0.3| ₹80| Beta  
  
DeepSeek V4 Pro, Kimi K3, MiMo V2.6 Flash, and MiMo V2.6 Pro are [in beta](https://docs.sarvam.ai/api-reference/beta-apis).

### Speech to Text

Priced per minute, billed per second.

Service| Pay as you go| Pro| Growth  
---|---|---|---  
Speech to Text (real-time, streaming, batch)| ₹0.49| ₹0.45| ₹0.41  
Speech to Text with Diarization (batch)| ₹0.59| ₹0.54| ₹0.50  
  
### Text to Speech

Priced per 1,000 characters, rounded to the nearest character. Rates apply to REST, HTTP streaming, and WebSocket streaming.

Service| Pay as you go| Pro| Growth  
---|---|---|---  
Bulbul v4 Flash| ₹1.00| ₹0.925| ₹0.85  
Bulbul v3| ₹3.00| ₹2.85| ₹2.70  
Instant Voice Cloning| ₹2.00| ₹2.00| ₹2.00  
  
### Text Processing

Priced per 1,000 characters, rounded to the nearest character.

Service| Pay as you go| Pro| Growth  
---|---|---|---  
Translate (formal and colloquial)| ₹2.00| ₹1.70| ₹1.50  
Transliteration| ₹2.00| ₹2.00| ₹1.80  
Language Identification| ₹0.35| ₹0.35| ₹0.31  
  
### Document Intelligence

Priced per page.

Service| Pay as you go| Pro| Growth  
---|---|---|---  
Document Digitization API| ₹0.50| ₹0.50| ₹0.50  
Document Extraction API| ₹1.00| ₹1.00| ₹1.00  
  
### Document Translation

Priced per 1,000 billable characters, per target language. Character count is computed after parsing; each target language in a job is billed separately. Charges round up to the nearest rupee; minimum ₹1 when any billable text is present.

Service| Pay as you go| Pro| Growth  
---|---|---|---  
Document Translation API| ₹5.00| ₹5.00| ₹4.50  
  
### Dubbing

Priced per minute of source media, multiplied by the number of target languages. Duration is rounded to whole seconds before billing.

Service| Pay as you go| Pro| Growth  
---|---|---|---  
Dubbing API (`editor_flow: false`)| ₹40| ₹40| ₹38  
Dubbing with Editor Flow (`editor_flow: true`)| ₹80| ₹80| ₹75  
  
Editor Flow costs about twice the standard API rate and should only be enabled when the interactive editor workflow is required. See the [Dubbing overview](https://docs.sarvam.ai/api/api-guides-tutorials/dubbing/overview).

* * *

## Rate Limits

Rate limits restrict the number of API requests your account can make within a given time window. Key points:

  * **Per-account enforcement** : limits apply to your account as a whole, not individual API keys. All keys share the same rate limit pool.
  * **Continuous replenishment** : capacity refills steadily over the window period rather than resetting all at once (token bucket model).
  * **Per-API granularity** : each API has its own independent rate limits. WebSocket, Document AI, and LLM APIs have different limits from standard REST APIs. Check your specific API below.



Your current limits are on the [Dashboard → Rate Limits](https://indus.sarvam.ai/rate-limits?ref=docs) page.

Rate limits vary significantly by API type and plan. Review the limits for each API below before building your integration.

### Speech to Text limits

#### Real-time REST

| Pay as you go| Pro| Growth  
---|---|---|---  
**Rate Limit**|  60 req/min| 100 req/min| 4,000 req/min  
  
#### WebSocket Streaming

| Pay as you go| Pro| Growth  
---|---|---|---  
**Rate Limit**|  20 concurrent| 100 concurrent| 100 concurrent  
  
#### Batch

| Pay as you go| Pro| Growth  
---|---|---|---  
**Rate Limit**|  20 req/min| 100 req/min| 500 req/min  
  
For batch endpoints, avoid tight polling loops. Poll no faster than your plan’s rate limit allows, for example every 3 seconds on Pay as you go’s 20 req/min.

The SDK’s `wait_until_complete()` uses safe defaults out of the box:

  * **Batch STT / Speech-to-Text-Translate:** 5-second poll interval. See [Polling Defaults](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/batch-api#polling-defaults).
  * **Document Digitization (legacy`document_intelligence`):** 2-second poll interval.



[Document AI](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/overview) has no `wait_until_complete()` helper. You poll `get_status()` yourself, so pick your own interval (the examples use 5 seconds).

If you poll manually instead of using the SDK helper, match or exceed these intervals.

* * *

### Text to Speech limits

Limits are the same for Bulbul v3 and Bulbul v4 Flash.

#### Real-time REST and HTTP Streaming

| Pay as you go| Pro| Growth  
---|---|---|---  
**Rate Limit**|  60 req/min| 200 req/min| 1,000 req/min  
  
#### WebSocket Streaming

| Pay as you go| Pro| Growth  
---|---|---|---  
**Rate Limit**|  60 concurrent| 200 concurrent| 1,000 concurrent  
  
### Instant Voice Cloning limits

| Pay as you go| Pro| Growth  
---|---|---|---  
**Sustained**|  60 req/min| 200 req/min| 1,000 req/min  
**Burst**|  100 req| 300 req| 1,200 req  
  
The sustained figure is the steady-state rate; short spikes are allowed up to the burst figure before requests are rejected with a `429`. Limits are subject to change.

* * *

### Translation & Text Services limits

#### Text translation (`POST /translate`)

| Pay as you go| Pro| Growth  
---|---|---|---  
**Rate Limit**|  60 req/min| 200 req/min| 1,000 req/min  
  
Transliteration and Language Identification share the same limits.

#### Document Translation

Job lifecycle endpoints (`POST /translate/document/jobs`, `start`, `live-status`, `export`, `export/status`):

| Pay as you go| Pro| Growth  
---|---|---|---  
**Rate Limit**|  200 req/min| 500 req/min| 1,000 req/min  
  
Document Translation is asynchronous. Poll `live-status` every **10–15 seconds** (see the [overview](https://docs.sarvam.ai/api/api-guides-tutorials/doc-translation/overview#how-it-works)) rather than tight loops that burn your per-minute quota.

* * *

### Language model limits

#### Default models

| Pay as you go| Pro| Growth  
---|---|---|---  
**Rate Limit**|  50 req/min| 200 req/min| 1,000 req/min  
  
Applies to: `gemma4`, `glm5.3`, `deepseekv4.1-flash-1017`

#### Sarvam-105B model

This large model has lower limits due to its compute requirements.

| Pay as you go| Pro| Growth  
---|---|---|---  
**Rate Limit**|  60 req/min| 200 req/min| 300 req/min  
  
Applies to: `sarvam-105b`, `sarvam-105b-conversations`

* * *

### Dubbing limits

| Pay as you go| Pro| Growth  
---|---|---|---  
**Rate Limit**|  5 req/min| 50 req/min| 300 req/min  
  
* * *

### Document AI limits

Document AI limits are set per operation and scale with your plan. Each limit assumes the number of pages per request shown below.

Operation| Pages per request| Pay as you go| Pro| Growth  
---|---|---|---|---  
**Parse**|  20| 200 req/min| 300 req/min| 400 req/min  
**Extract**|  30| 30 req/min| 50 req/min| 60 req/min  
**Split**|  500| 60 req/min| 120 req/min| 180 req/min  
**Classify**|  20| 100 req/min| 150 req/min| 200 req/min  
  
## Exceeding Your Limits

### REST rate limits (429 / 503)

When your account exceeds a rate limit, the API returns a `429 Too Many Requests` response:
    
    
    {
    
      "error": {
    
        "message": "Rate limit exceeded",
    
        "code": "rate_limit_exceeded_error"
    
      }
    
    }

A `503 Service Unavailable` can also occur under high backend load. Retry it the same way you would a 429, using a fixed exponential backoff. See [Retry with exponential backoff](https://docs.sarvam.ai/api/getting-started/errors-troubleshooting#retry-with-exponential-backoff) for a reference implementation.

### Exhausted credits (402)

A `402 Payment Required` is **not** a rate limit. It means the organisation’s credit balance is empty, and no retry will clear it. Add credits on **Settings → Billing** and the account resumes immediately, with no key rotation or redeploy. See [Billing & payments](https://docs.sarvam.ai/api/platform/billing) and [Out of credits](https://docs.sarvam.ai/api/getting-started/errors-troubleshooting).

### WebSocket connection limits

The limiter reacts to how fast new connections are opened, not how many are held open at once:

  * Connections opened in a fast burst can be rejected well below the concurrent ceilings listed above.
  * The same number of connections opened gradually (for example, 300ms apart) and held open simultaneously can succeed past those ceilings.



A rejected connection is closed, not queued. The close code is `1003`, with this reason text:
    
    
    Rate limit exceeded. Visit the API Dashboard to review and manage your subscription.

This differs from the `4xxx` range described elsewhere on this site for application-specific closures.

The burst threshold is not a fixed number and can vary between runs at the same burst size. Space out new connections rather than relying on a specific count.

* * *

## Upgrading Your Limits

[1](https://docs.sarvam.ai/api/getting-started/pricing#check-your-current-limits)

### Check your current limits

Visit the [Dashboard → Rate Limits](https://indus.sarvam.ai/rate-limits?ref=docs) to see your exact per-API limits.

[2](https://docs.sarvam.ai/api/getting-started/pricing#upgrade-your-plan)

### Upgrade your plan

Purchase a higher plan directly from the dashboard. Your rate limits increase immediately after upgrade, no downtime.

[3](https://docs.sarvam.ai/api/getting-started/pricing#need-custom-limits)

### Need custom limits?

For limits beyond the Growth plan, contact our team for an Enterprise arrangement.

[Upgrade PlanView plans and upgrade directly from the dashboard. Rate limits update instantly.](https://indus.sarvam.ai/pricing/?ref=docs)[Enterprise & Custom LimitsNeed higher rate limits, dedicated infrastructure, or custom SLAs? Talk to our team.](https://docs.sarvam.ai/api/getting-started/help)

Was this page helpful?

YesNo

[Previous](https://docs.sarvam.ai/api/getting-started/sdks)[Talk to usNext](https://docs.sarvam.ai/api/getting-started/help)[Built with](https://buildwithfern.com/?utm_source=others&utm_medium=organic&utm_campaign=fern_indocs_url&utm_content=book_demo&utm_term=docs.sarvam.ai)

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


