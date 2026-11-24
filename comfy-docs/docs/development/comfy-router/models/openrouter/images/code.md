---
url: https://docs.comfy.org/development/comfy-router/models/openrouter/images/code/
title: Use Images with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-24T18:44:22.757272+00:00
---

# Use Images with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/openrouter/images/code/

## On this page

Back to top

  * Request setup
  * Schema
    * Input
    * Output
  * Examples
    * Output
  * Before you ship



Openrouter

# Use Images with Comfy Router

Copy pageCopy page

Call openrouter/images through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `openrouter/images`, served by Comfy Router from Openrouter. **Input:** Text, Image · **Output:** Image

## Request setup

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. For Python, run `pip install comfy-sdk`. For TypeScript, run `npm install @comfyorg/sdk`. cURL uses raw HTTP. **Model ID:** `openrouter/images` **Endpoint:** `POST https://api.comfy.org/v2/models/openrouter/images`

This model has no runnable request example. Build the body from the input documentation below, then use it with the [Router quickstart](https://docs.comfy.org/development/comfy-router/quickstart).

## Schema

### Input

aspect_ratio

string

Output aspect ratio

background

string

Background mode

input_references

object[]

Reference images for image-to-image generation, as data URLs or HTTP(S) URLs

input_references[].image_url

object

required

input_references[].image_url.detail

string

Image detail level for vision modelsPossible values: `auto`, `low`, `high`

input_references[].image_url.url

string

required

URL of the image (data: URLs supported)

input_references[].type

string

required

Content part type, always image_url

model

string

The image generation model to use, as an OpenRouter model ID such as `microsoft/mai-image-2.6` or `microsoft/mai-image-2.6-flash`.

n

integer

Number of images to generate

output_compression

integer

Compression level for webp/jpeg output

output_format

string

Output image format

prompt

string

required

Text description of the desired image

provider

object

When multiple model providers are available, optionally indicate your routing preference.

provider.allow_fallbacks

boolean

Whether to allow backup providers to serve requests

  * true: (default) when the primary provider (or your custom providers in “order”) is unavailable, use the next best provider.
  * false: use only the primary/custom provider, and return the upstream error if it’s unavailable.



provider.data_collection

`deny`, `allow`

Data collection setting. If no available model provider meets the requirement, your request will return an error.

  * allow: (default) allow providers which store user data non-transiently and may train on it
  * deny: use only providers which do not collect user data.



provider.enforce_distillable_text

boolean

Whether to restrict routing to only models that allow text distillation. When true, only models where the author has allowed distillation will be used.

provider.ignore

`AkashML`, `AI21`, `AionLabs`, `Alibaba`, `Ambient`, `Baidu`, `Amazon Bedrock`, `Amazon Nova`, `Anthropic`, `Arcee AI`, `AtlasCloud`, `Avian`, `Azure`, `BaseTen`, `BytePlus`, `Black Forest Labs`, `Cerebras`, `Chutes`, `Cirrascale`, `Clarifai`, `Cloudflare`, `Cohere`, `Crucible`, `Crusoe`, `DeepInfra`, `DeepSeek`, `DekaLLM`, `Featherless`, `Fireworks`, `Friendli`, `GMICloud`, `Google`, `Google AI Studio`, `Groq`, `Hyperbolic`, `Inception`, `Inceptron`, `InferenceNet`, `Ionstream`, `Infermatic`, `Io Net`, `Inflection`, `Liquid`, `Mara`, `Mancer 2`, `Minimax`, `ModelRun`, `Mistral`, `Modular`, `Moonshot AI`, `Morph`, `NCompass`, `Nebius`, `Nex AGI`, `NextBit`, `Novita`, `Nvidia`, `OpenAI`, `OpenInference`, `Parasail`, `Poolside`, `Perceptron`, `Perplexity`, `Phala`, `Recraft`, `Reka`, `Relace`, `SambaNova`, `Seed`, `SiliconFlow`, `Sourceful`, `StepFun`, `Stealth`, `StreamLake`, `Switchpoint`, `Together`, `Upstage`, `Venice`, `WandB`, `Xiaomi`, `xAI`, `Z.AI`, `FakeProvider` | string[]

List of provider slugs to ignore. If provided, this list is merged with your account-wide ignored provider settings for this request.

provider.max_price

object

The object specifying the maximum price you want to pay for this request. USD price per million tokens, for prompt and completion.

provider.max_price.audio

string

Price per million prompt tokens

provider.max_price.completion

string

Price per million prompt tokens

provider.max_price.image

string

Price per million prompt tokens

provider.max_price.prompt

string

Price per million prompt tokens

provider.max_price.request

string

Price per million prompt tokens

provider.only

`AkashML`, `AI21`, `AionLabs`, `Alibaba`, `Ambient`, `Baidu`, `Amazon Bedrock`, `Amazon Nova`, `Anthropic`, `Arcee AI`, `AtlasCloud`, `Avian`, `Azure`, `BaseTen`, `BytePlus`, `Black Forest Labs`, `Cerebras`, `Chutes`, `Cirrascale`, `Clarifai`, `Cloudflare`, `Cohere`, `Crucible`, `Crusoe`, `DeepInfra`, `DeepSeek`, `DekaLLM`, `Featherless`, `Fireworks`, `Friendli`, `GMICloud`, `Google`, `Google AI Studio`, `Groq`, `Hyperbolic`, `Inception`, `Inceptron`, `InferenceNet`, `Ionstream`, `Infermatic`, `Io Net`, `Inflection`, `Liquid`, `Mara`, `Mancer 2`, `Minimax`, `ModelRun`, `Mistral`, `Modular`, `Moonshot AI`, `Morph`, `NCompass`, `Nebius`, `Nex AGI`, `NextBit`, `Novita`, `Nvidia`, `OpenAI`, `OpenInference`, `Parasail`, `Poolside`, `Perceptron`, `Perplexity`, `Phala`, `Recraft`, `Reka`, `Relace`, `SambaNova`, `Seed`, `SiliconFlow`, `Sourceful`, `StepFun`, `Stealth`, `StreamLake`, `Switchpoint`, `Together`, `Upstage`, `Venice`, `WandB`, `Xiaomi`, `xAI`, `Z.AI`, `FakeProvider` | string[]

List of provider slugs to allow. If provided, this list is merged with your account-wide allowed provider settings for this request.

provider.order

`AkashML`, `AI21`, `AionLabs`, `Alibaba`, `Ambient`, `Baidu`, `Amazon Bedrock`, `Amazon Nova`, `Anthropic`, `Arcee AI`, `AtlasCloud`, `Avian`, `Azure`, `BaseTen`, `BytePlus`, `Black Forest Labs`, `Cerebras`, `Chutes`, `Cirrascale`, `Clarifai`, `Cloudflare`, `Cohere`, `Crucible`, `Crusoe`, `DeepInfra`, `DeepSeek`, `DekaLLM`, `Featherless`, `Fireworks`, `Friendli`, `GMICloud`, `Google`, `Google AI Studio`, `Groq`, `Hyperbolic`, `Inception`, `Inceptron`, `InferenceNet`, `Ionstream`, `Infermatic`, `Io Net`, `Inflection`, `Liquid`, `Mara`, `Mancer 2`, `Minimax`, `ModelRun`, `Mistral`, `Modular`, `Moonshot AI`, `Morph`, `NCompass`, `Nebius`, `Nex AGI`, `NextBit`, `Novita`, `Nvidia`, `OpenAI`, `OpenInference`, `Parasail`, `Poolside`, `Perceptron`, `Perplexity`, `Phala`, `Recraft`, `Reka`, `Relace`, `SambaNova`, `Seed`, `SiliconFlow`, `Sourceful`, `StepFun`, `Stealth`, `StreamLake`, `Switchpoint`, `Together`, `Upstage`, `Venice`, `WandB`, `Xiaomi`, `xAI`, `Z.AI`, `FakeProvider` | string[]

An ordered list of provider slugs. The router will attempt to use the first provider in the subset of this list that supports your requested model, and fall back to the next if it is unavailable. If no providers are available, the request will fail with an error message.

provider.preferred_max_latency

number | object

Preferred maximum latency (in seconds). Can be a number (applies to p50) or an object with percentile-specific cutoffs. Endpoints above the threshold(s) may still be used, but are deprioritized in routing. When using fallback models, this may cause a fallback model to be used instead of the primary model if it meets the threshold.

provider.preferred_min_throughput

number | object

Preferred minimum throughput (in tokens per second). Can be a number (applies to p50) or an object with percentile-specific cutoffs. Endpoints below the threshold(s) may still be used, but are deprioritized in routing. When using fallback models, this may cause a fallback model to be used instead of the primary model if it meets the threshold.

provider.quantizations

`int4`, `int8`, `fp4`, `fp6`, `fp8`, `fp16`, `bf16`, `fp32`, `unknown`[]

A list of quantization levels to filter the provider by.

provider.require_parameters

boolean

Whether to filter providers to only those that support the parameters you’ve provided. If this setting is omitted or set to false, then providers will receive only the parameters they support, and ignore the rest.

provider.sort

`price`, `throughput`, `latency`, `exacto` | object

The sorting strategy to use for this request, if “order” is not specified. When set, no load balancing is performed.

provider.zdr

boolean

Whether to restrict routing to only ZDR (Zero Data Retention) endpoints. When true, only endpoints that do not retain prompts will be used.

quality

string

Output quality preset

resolution

string

Output resolution preset

seed

integer

Seed for deterministic generation

size

string

Output image size

stream

boolean

Enable SSE streaming for partial images. The `/proxy/` route rejects `stream: true` with a 400. Comfy Router sets it to false and serves the request.

user

string

Stable end-user identifier

Generated from the schema Router serves at `GET /v2/models/openrouter/images/openapi.json`, the same document it validates a call against before the request reaches the provider.

### Output

created

integer

Unix timestamp of creation

data

object[]

Generated images

data[].b64_json

string

Base64-encoded image data. When the response is larger than 1,048,576 bytes, Comfy Router answers `url` in its place. The image stays here when the response is not larger than that, or when its upload to Comfy storage fails.

data[].media_type

string

MIME type of the image

data[].url

string

A Comfy-hosted signed URL of the image, given in place of `b64_json` when the response is larger than 1,048,576 bytes. Comfy Router always asks for it; the `/proxy/` route asks for it only when the request sends `Comfy-Asset-Format: url`. A zero-data-retention workspace never gets it: its images stay in `b64_json`. The URL expires 24 hours after the call.

usage

object

Image generation usage

usage.completion_tokens

integer

Tokens generated

usage.cost

number

Total USD cost of the requestFormat: `double`

usage.prompt_tokens

integer

Tokens used for the input

usage.total_tokens

integer

Total tokens for the request

## Examples

### Output
    
    
    {
      "created": 1767225600,
      "data": [
        {
          "media_type": "image/png",
          "url": "https://storage.googleapis.com/example-bucket/openrouter-images/example.png"
        }
      ],
      "usage": {
        "completion_tokens": 1024,
        "cost": 0.03,
        "prompt_tokens": 12,
        "total_tokens": 1036
      }
    }
    

## Before you ship

The SDKs create an `Idempotency-Key` and reuse it for automatic retries. For manual retries, reuse the original key. Router can hold the connection for up to 10 minutes. When a request fails, Router sends an `X-Comfy-Error-Type` response header explaining why. A `422` means Router rejected the input before calling the provider, and a `413` means the request body was larger than Router accepts. Download generated assets promptly because [result URLs can expire](https://docs.comfy.org/development/comfy-router/reference#result-assets). Any size limit named in a field description above is the provider’s own bound on that field, quoted from the provider’s specification. Router applies a separate cap to the whole request body, which base64-encoded media counts against: see [request body size](https://docs.comfy.org/development/comfy-router/limitations#request-bodies-are-capped). This page documents one partner model called through Comfy Router. The same `comfy-sdk` / `@comfyorg/sdk` package also ships a second client, for running a whole ComfyUI workflow graph on Comfy Cloud: `Comfy(api_key=...)` / `new Comfy({ apiKey })`, with `client.workflows`, `client.assets` and `client.jobs`. See [Comfy SDKs](https://docs.comfy.org/development/api-development/sdks).

## Headers

Authentication, idempotency, request IDs, error buckets, retry pacing, spend limits.

## Using the Router API

Model discovery, validation errors, retries, and billing.

## Limitations

What Router does not do today, and what to use instead.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/openrouter/images/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/openrouter/images/code)

[Chat Completions](https://docs.comfy.org/development/comfy-router/models/openrouter/chat-completions/code)[Pika 2.5 Image To Video](https://docs.comfy.org/development/comfy-router/models/pika/pika-2-5-image-to-video/code)
