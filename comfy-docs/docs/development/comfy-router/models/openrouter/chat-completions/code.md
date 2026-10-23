---
url: https://docs.comfy.org/development/comfy-router/models/openrouter/chat-completions/code/
title: Use Chat Completions with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:33.769789+00:00
---

# Use Chat Completions with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/openrouter/chat-completions/code/

## On this page

  * Request setup
  * Schema
    * Input
    * Output
  * Examples
    * Output
  * Before you ship



Openrouter

# Use Chat Completions with Comfy Router

Copy pageCopy page

Call openrouter/chat-completions through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `openrouter/chat-completions`, served by Comfy Router from Openrouter. **Input:** Text, Image · **Output:** Text

## 

​

Request setup

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. For Python, run `pip install comfy-sdk`. For TypeScript, run `npm install @comfyorg/sdk`. cURL uses raw HTTP. **Model ID:** `openrouter/chat-completions` **Endpoint:** `POST https://api.comfy.org/v2/models/openrouter/chat-completions`

This model has no runnable request example. Build the body from the input documentation below, then use it with the [Router quickstart](https://docs.comfy.org/development/comfy-router/quickstart).

## 

​

Schema

### 

​

Input

​

cache_control

object

Enable automatic prompt caching. When set at the top level, the system automatically applies cache breakpoints to the last cacheable block in the request. Currently supported for Anthropic Claude models.

​

cache_control.ttl

string

Possible values: `5m`, `1h`

​

cache_control.type

string

required

Possible values: `ephemeral`

​

debug

object

Debug options for inspecting request transformations (streaming only)

​

debug.echo_upstream_body

boolean

If true, includes the transformed upstream request body in a debug chunk at the start of the stream. Only works with streaming mode.

​

frequency_penalty

number

Frequency penalty (-2.0 to 2.0)Format: `double`

​

image_config

object | string | number | object[]

​

logit_bias

object

Token logit bias adjustments

​

logprobs

boolean

Return log probabilities

​

max_completion_tokens

integer

Maximum tokens in completion

​

max_tokens

integer

Maximum tokens (deprecated, use max_completion_tokens). Note: some providers enforce a minimum of 16.

​

messages

object[]

required

List of messages for the conversation

​

metadata

object

Key-value pairs for additional object information (max 16 pairs, 64 char keys, 512 char values)

​

modalities

`text`, `image`, `audio`[]

Output modalities for the response. Supported values are “text”, “image”, and “audio”.

​

model

string

Model to use for completion

​

models

string[]

Models to use for completion

​

parallel_tool_calls

boolean

Whether to enable parallel function calling during tool use. When true, the model may generate multiple tool calls in a single response.

​

plugins

object[]

Plugins you want to enable for this request, including their settings.

​

presence_penalty

number

Presence penalty (-2.0 to 2.0)Format: `double`

​

provider

object

When multiple model providers are available, optionally indicate your routing preference.

​

provider.allow_fallbacks

boolean

Whether to allow backup providers to serve requests

  * true: (default) when the primary provider (or your custom providers in “order”) is unavailable, use the next best provider.
  * false: use only the primary/custom provider, and return the upstream error if it’s unavailable.



​

provider.data_collection

`deny`, `allow`

Data collection setting. If no available model provider meets the requirement, your request will return an error.

  * allow: (default) allow providers which store user data non-transiently and may train on it
  * deny: use only providers which do not collect user data.



​

provider.enforce_distillable_text

boolean

Whether to restrict routing to only models that allow text distillation. When true, only models where the author has allowed distillation will be used.

​

provider.ignore

`AkashML`, `AI21`, `AionLabs`, `Alibaba`, `Ambient`, `Baidu`, `Amazon Bedrock`, `Amazon Nova`, `Anthropic`, `Arcee AI`, `AtlasCloud`, `Avian`, `Azure`, `BaseTen`, `BytePlus`, `Black Forest Labs`, `Cerebras`, `Chutes`, `Cirrascale`, `Clarifai`, `Cloudflare`, `Cohere`, `Crucible`, `Crusoe`, `DeepInfra`, `DeepSeek`, `DekaLLM`, `Featherless`, `Fireworks`, `Friendli`, `GMICloud`, `Google`, `Google AI Studio`, `Groq`, `Hyperbolic`, `Inception`, `Inceptron`, `InferenceNet`, `Ionstream`, `Infermatic`, `Io Net`, `Inflection`, `Liquid`, `Mara`, `Mancer 2`, `Minimax`, `ModelRun`, `Mistral`, `Modular`, `Moonshot AI`, `Morph`, `NCompass`, `Nebius`, `Nex AGI`, `NextBit`, `Novita`, `Nvidia`, `OpenAI`, `OpenInference`, `Parasail`, `Poolside`, `Perceptron`, `Perplexity`, `Phala`, `Recraft`, `Reka`, `Relace`, `SambaNova`, `Seed`, `SiliconFlow`, `Sourceful`, `StepFun`, `Stealth`, `StreamLake`, `Switchpoint`, `Together`, `Upstage`, `Venice`, `WandB`, `Xiaomi`, `xAI`, `Z.AI`, `FakeProvider` | string[]

List of provider slugs to ignore. If provided, this list is merged with your account-wide ignored provider settings for this request.

​

provider.max_price

object

The object specifying the maximum price you want to pay for this request. USD price per million tokens, for prompt and completion.

​

provider.max_price.audio

string

Price per million prompt tokens

​

provider.max_price.completion

string

Price per million prompt tokens

​

provider.max_price.image

string

Price per million prompt tokens

​

provider.max_price.prompt

string

Price per million prompt tokens

​

provider.max_price.request

string

Price per million prompt tokens

​

provider.only

`AkashML`, `AI21`, `AionLabs`, `Alibaba`, `Ambient`, `Baidu`, `Amazon Bedrock`, `Amazon Nova`, `Anthropic`, `Arcee AI`, `AtlasCloud`, `Avian`, `Azure`, `BaseTen`, `BytePlus`, `Black Forest Labs`, `Cerebras`, `Chutes`, `Cirrascale`, `Clarifai`, `Cloudflare`, `Cohere`, `Crucible`, `Crusoe`, `DeepInfra`, `DeepSeek`, `DekaLLM`, `Featherless`, `Fireworks`, `Friendli`, `GMICloud`, `Google`, `Google AI Studio`, `Groq`, `Hyperbolic`, `Inception`, `Inceptron`, `InferenceNet`, `Ionstream`, `Infermatic`, `Io Net`, `Inflection`, `Liquid`, `Mara`, `Mancer 2`, `Minimax`, `ModelRun`, `Mistral`, `Modular`, `Moonshot AI`, `Morph`, `NCompass`, `Nebius`, `Nex AGI`, `NextBit`, `Novita`, `Nvidia`, `OpenAI`, `OpenInference`, `Parasail`, `Poolside`, `Perceptron`, `Perplexity`, `Phala`, `Recraft`, `Reka`, `Relace`, `SambaNova`, `Seed`, `SiliconFlow`, `Sourceful`, `StepFun`, `Stealth`, `StreamLake`, `Switchpoint`, `Together`, `Upstage`, `Venice`, `WandB`, `Xiaomi`, `xAI`, `Z.AI`, `FakeProvider` | string[]

List of provider slugs to allow. If provided, this list is merged with your account-wide allowed provider settings for this request.

​

provider.order

`AkashML`, `AI21`, `AionLabs`, `Alibaba`, `Ambient`, `Baidu`, `Amazon Bedrock`, `Amazon Nova`, `Anthropic`, `Arcee AI`, `AtlasCloud`, `Avian`, `Azure`, `BaseTen`, `BytePlus`, `Black Forest Labs`, `Cerebras`, `Chutes`, `Cirrascale`, `Clarifai`, `Cloudflare`, `Cohere`, `Crucible`, `Crusoe`, `DeepInfra`, `DeepSeek`, `DekaLLM`, `Featherless`, `Fireworks`, `Friendli`, `GMICloud`, `Google`, `Google AI Studio`, `Groq`, `Hyperbolic`, `Inception`, `Inceptron`, `InferenceNet`, `Ionstream`, `Infermatic`, `Io Net`, `Inflection`, `Liquid`, `Mara`, `Mancer 2`, `Minimax`, `ModelRun`, `Mistral`, `Modular`, `Moonshot AI`, `Morph`, `NCompass`, `Nebius`, `Nex AGI`, `NextBit`, `Novita`, `Nvidia`, `OpenAI`, `OpenInference`, `Parasail`, `Poolside`, `Perceptron`, `Perplexity`, `Phala`, `Recraft`, `Reka`, `Relace`, `SambaNova`, `Seed`, `SiliconFlow`, `Sourceful`, `StepFun`, `Stealth`, `StreamLake`, `Switchpoint`, `Together`, `Upstage`, `Venice`, `WandB`, `Xiaomi`, `xAI`, `Z.AI`, `FakeProvider` | string[]

An ordered list of provider slugs. The router will attempt to use the first provider in the subset of this list that supports your requested model, and fall back to the next if it is unavailable. If no providers are available, the request will fail with an error message.

​

provider.preferred_max_latency

number | object

Preferred maximum latency (in seconds). Can be a number (applies to p50) or an object with percentile-specific cutoffs. Endpoints above the threshold(s) may still be used, but are deprioritized in routing. When using fallback models, this may cause a fallback model to be used instead of the primary model if it meets the threshold.

​

provider.preferred_min_throughput

number | object

Preferred minimum throughput (in tokens per second). Can be a number (applies to p50) or an object with percentile-specific cutoffs. Endpoints below the threshold(s) may still be used, but are deprioritized in routing. When using fallback models, this may cause a fallback model to be used instead of the primary model if it meets the threshold.

​

provider.quantizations

`int4`, `int8`, `fp4`, `fp6`, `fp8`, `fp16`, `bf16`, `fp32`, `unknown`[]

A list of quantization levels to filter the provider by.

​

provider.require_parameters

boolean

Whether to filter providers to only those that support the parameters you’ve provided. If this setting is omitted or set to false, then providers will receive only the parameters they support, and ignore the rest.

​

provider.sort

`price`, `throughput`, `latency`, `exacto` | object

The sorting strategy to use for this request, if “order” is not specified. When set, no load balancing is performed.

​

provider.zdr

boolean

Whether to restrict routing to only ZDR (Zero Data Retention) endpoints. When true, only endpoints that do not retain prompts will be used.

​

reasoning

object

Configuration options for reasoning models

​

reasoning.effort

`xhigh`, `high`, `medium`, `low`, `minimal`, `none`

Constrains effort on reasoning for reasoning models

​

reasoning.summary

string

Possible values: `auto`, `concise`, `detailed`

​

response_format

object

Response format configuration

​

route

object

Any type

​

seed

integer

Random seed for deterministic outputs

​

service_tier

`auto`, `default`, `flex`, `priority`, `scale`

The service tier to use for processing this request.

​

session_id

string

A unique identifier for grouping related requests (e.g., a conversation or agent workflow) for observability. If provided in both the request body and the x-session-id header, the body value takes precedence. Maximum of 256 characters.

​

stop

string | string[] | object

Stop sequences (up to 4)

​

stop_server_tools_when

object[]

Stop conditions for the server-tool agent loop. Any condition firing halts the loop (OR logic). When set, this overrides `max_tool_calls`.

​

stream

boolean

default:"false"

Enable streaming response

​

stream_options

object

Streaming configuration options

​

stream_options.include_usage

boolean

Deprecated: This field has no effect. Full usage details are always included.

​

temperature

number

Sampling temperature (0-2)Format: `double`

​

tool_choice

`none` | `auto` | `required` | object

Tool choice configuration

​

tools

object[]

Available tools for function calling

​

top_logprobs

integer

Number of top log probabilities to return (0-20)

​

top_p

number

Nucleus sampling parameter (0-1)Format: `double`

​

trace

object

Metadata for observability and tracing. Known keys (trace_id, trace_name, span_name, generation_name, parent_span_id) have special handling. Additional keys are passed through as custom metadata to configured broadcast destinations.

​

trace.generation_name

string

​

trace.parent_span_id

string

​

trace.span_name

string

​

trace.trace_id

string

​

trace.trace_name

string

​

user

string

Unique user identifier

Generated from the schema Router serves at `GET /v2/models/openrouter/chat-completions/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

choices

object[]

required

List of completion choices

​

choices[].finish_reason

string

required

Possible values: `tool_calls`, `stop`, `length`, `content_filter`, `error`

​

choices[].index

integer

required

Choice index

​

choices[].logprobs

object

Log probabilities for the completion

​

choices[].logprobs.content

object[]

required

Log probabilities for content tokens

​

choices[].logprobs.content[].bytes

integer[]

required

UTF-8 bytes of the token

​

choices[].logprobs.content[].logprob

number

required

Log probability of the tokenFormat: `double`

​

choices[].logprobs.content[].token

string

required

The token

​

choices[].logprobs.content[].top_logprobs

object[]

required

Top alternative tokens with probabilities

​

choices[].logprobs.content[].top_logprobs[].bytes

integer[]

required

​

choices[].logprobs.content[].top_logprobs[].logprob

number

required

Format: `double`

​

choices[].logprobs.content[].top_logprobs[].token

string

required

​

choices[].logprobs.refusal

object[]

Log probabilities for refusal tokens

​

choices[].logprobs.refusal[].bytes

integer[]

required

UTF-8 bytes of the token

​

choices[].logprobs.refusal[].logprob

number

required

Log probability of the tokenFormat: `double`

​

choices[].logprobs.refusal[].token

string

required

The token

​

choices[].logprobs.refusal[].top_logprobs

object[]

required

Top alternative tokens with probabilities

​

choices[].logprobs.refusal[].top_logprobs[].bytes

integer[]

required

​

choices[].logprobs.refusal[].top_logprobs[].logprob

number

required

Format: `double`

​

choices[].logprobs.refusal[].top_logprobs[].token

string

required

​

choices[].message

object

required

Assistant message for requests and responses

​

choices[].message.audio

object

Audio output data or reference

​

choices[].message.audio.data

string

Base64 encoded audio data

​

choices[].message.audio.expires_at

integer

Audio expiration timestamp

​

choices[].message.audio.id

string

Audio output identifier

​

choices[].message.audio.transcript

string

Audio transcript

​

choices[].message.content

string | object[] | object

Assistant message content

​

choices[].message.images

object[]

Generated images from image generation models

​

choices[].message.images[].image_url

object

required

​

choices[].message.images[].image_url.url

string

required

URL or base64-encoded data of the generated image

​

choices[].message.name

string

Optional name for the assistant

​

choices[].message.reasoning

string

Reasoning output

​

choices[].message.reasoning_details

object[]

Reasoning details for extended thinking models

​

choices[].message.refusal

string

Refusal message if content was refused

​

choices[].message.tool_calls

object[]

Tool calls made by the assistant

​

choices[].message.tool_calls[].function

object

required

​

choices[].message.tool_calls[].function.arguments

string

required

Function arguments as JSON string

​

choices[].message.tool_calls[].function.name

string

required

Function name to call

​

choices[].message.tool_calls[].id

string

required

Tool call identifier

​

choices[].message.tool_calls[].type

string

required

Possible values: `function`

​

created

integer

required

Unix timestamp of creation

​

id

string

required

Unique completion identifier

​

model

string

required

Model used for completion

​

object

string

required

Possible values: `chat.completion`

​

openrouter_metadata

object

​

openrouter_metadata.attempt

integer

required

​

openrouter_metadata.attempts

object[]

​

openrouter_metadata.attempts[].model

string

required

​

openrouter_metadata.attempts[].provider

string

required

​

openrouter_metadata.attempts[].status

integer

required

​

openrouter_metadata.endpoints

object

required

​

openrouter_metadata.endpoints.available

object[]

required

​

openrouter_metadata.endpoints.available[].model

string

required

​

openrouter_metadata.endpoints.available[].provider

string

required

​

openrouter_metadata.endpoints.available[].selected

boolean

required

​

openrouter_metadata.endpoints.total

integer

required

​

openrouter_metadata.is_byok

boolean

required

​

openrouter_metadata.params

object

​

openrouter_metadata.params.quality_floor

number

Format: `double`

​

openrouter_metadata.params.throughput_floor

number

Format: `double`

​

openrouter_metadata.params.version_group

string

​

openrouter_metadata.pipeline

object[]

​

openrouter_metadata.pipeline[].cost_usd

number

Format: `double`

​

openrouter_metadata.pipeline[].data

object

​

openrouter_metadata.pipeline[].guardrail_id

string

​

openrouter_metadata.pipeline[].guardrail_scope

string

​

openrouter_metadata.pipeline[].name

string

required

​

openrouter_metadata.pipeline[].summary

string

​

openrouter_metadata.pipeline[].type

string

required

Categorical kind of a pipeline stage. Multiple plugins can share a type (e.g. all guardrail-level plugins emit `guardrail`); the `name` field disambiguates which plugin emitted it.Possible values: `guardrail`, `plugin`, `server_tools`, `response_healing`, `context_compression`

​

openrouter_metadata.region

string

required

​

openrouter_metadata.requested

string

required

​

openrouter_metadata.strategy

string

required

Possible values: `direct`, `auto`, `free`, `latest`, `alias`, `fallback`, `pareto`, `bodybuilder`, `fusion`

​

openrouter_metadata.summary

string

required

​

service_tier

string

The service tier used by the upstream provider for this request

​

system_fingerprint

string

required

System fingerprint

​

usage

object

Token usage statistics

​

usage.completion_tokens

integer

required

Number of tokens in the completion

​

usage.completion_tokens_details

object

Detailed completion token usage

​

usage.cost

number

Cost of the completionFormat: `double`

​

usage.cost_details

object

Breakdown of upstream inference costs

​

usage.cost_details.upstream_inference_completions_cost

number

required

Format: `double`

​

usage.cost_details.upstream_inference_cost

number

Format: `double`

​

usage.cost_details.upstream_inference_prompt_cost

number

required

Format: `double`

​

usage.is_byok

boolean

Whether a request was made using a Bring Your Own Key configuration

​

usage.prompt_tokens

integer

required

Number of tokens in the prompt

​

usage.prompt_tokens_details

object

Detailed prompt token usage

​

usage.total_tokens

integer

required

Total number of tokens

## 

​

Examples

### 

​

Output
    
    
    {
      "choices": [
        {
          "finish_reason": "stop",
          "index": 0,
          "message": {
            "content": "ok"
          }
        }
      ],
      "created": 1750000000,
      "id": "gen-0000000000-examplecompletion",
      "model": "anthropic/claude-sonnet-4.5",
      "object": "chat.completion",
      "system_fingerprint": null,
      "usage": {
        "completion_tokens": 128,
        "cost": 0.00123,
        "prompt_tokens": 42,
        "total_tokens": 170
      }
    }
    

## 

​

Before you ship

The SDKs create an `Idempotency-Key` and reuse it for automatic retries. For manual retries, reuse the original key. Router can hold the connection for up to 10 minutes. When a request fails, Router sends an `X-Comfy-Error-Type` response header explaining why. A `422` means Router rejected the input before calling the provider, and a `413` means the request body was larger than Router accepts. Download generated assets promptly because [result URLs can expire](https://docs.comfy.org/development/comfy-router/reference#result-assets). Any size limit named in a field description above is the provider’s own bound on that field, quoted from the provider’s specification. Router applies a separate cap to the whole request body, which base64-encoded media counts against: see [request body size](https://docs.comfy.org/development/comfy-router/limitations#request-bodies-are-capped). This page documents one partner model called through Comfy Router. The same `comfy-sdk` / `@comfyorg/sdk` package also ships a second client, for running a whole ComfyUI workflow graph on Comfy Cloud: `Comfy(api_key=...)` / `new Comfy({ apiKey })`, with `client.workflows`, `client.assets` and `client.jobs`. See [Comfy SDKs](https://docs.comfy.org/development/api-development/sdks).

## Headers

Authentication, idempotency, request IDs, error buckets, retry pacing, spend limits.

## Using the Router API

Model discovery, validation errors, retries, and billing.

## Limitations

What Router does not do today, and what to use instead.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/openrouter/chat-completions/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/openrouter/chat-completions/code)

[Use o4-mini with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/openai/o4-mini/code)[Use Pika 2.5 Image To Video with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/pika/pika-2-5-image-to-video/code)

⌘I

[ComfyUI home page![light logo](https://mintcdn.com/dripart/WCFdTagRdhtvk9-o/logo/light.svg?fit=max&auto=format&n=WCFdTagRdhtvk9-o&q=85&s=ec112de87239058f5a931a7e4b594965)![dark logo](https://mintcdn.com/dripart/QzWbjSCBG7w61rR3/logo/dark.svg?fit=max&auto=format&n=QzWbjSCBG7w61rR3&q=85&s=62b4d879fb3aadbd7a468d1539032d6f)](https://docs.comfy.org/)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

Resources

[installation](https://docs.comfy.org/installation/system_requirements)[Tutorials](https://docs.comfy.org/tutorials/basic/text-to-image)[Development](https://docs.comfy.org/development/overview)

Products

[Features](https://www.comfy.org/?utm_source=docs)[Gallery](https://www.comfy.org/gallery?utm_source=docs)[Download](https://www.comfy.org/download?utm_source=docs)

Company

[About](https://www.comfy.org/about?utm_source=docs)[Careers](https://www.comfy.org/careers?utm_source=docs)[Terms of Service](https://www.comfy.org/terms-of-service?utm_source=docs)[Privacy Policy](https://www.comfy.org/privacy-policy?utm_source=docs)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=dripart)
