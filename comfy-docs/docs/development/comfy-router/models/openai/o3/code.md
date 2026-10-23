---
url: https://docs.comfy.org/development/comfy-router/models/openai/o3/code/
title: Use o3 with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:32.979492+00:00
---

# Use o3 with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/openai/o3/code/

## On this page

  * Quick start
  * Schema
    * Input
    * Output
  * Examples
    * Input
    * Output
  * Before you ship



OpenAI

# Use o3 with Comfy Router

Copy pageCopy page

Call openai/o3 through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `openai/o3`, served by Comfy Router from OpenAI. **Input:** Text, Image · **Output:** Text

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `openai/o3` **Endpoint:** `POST https://api.comfy.org/v2/models/openai/o3`

  * Wait for the result

  * Queue and collect later




Python

TypeScript

cURL
    
    
    from comfy_sdk import Comfy
    
    # Reads COMFY_API_KEY from the environment.
    # The SDK automatically creates an idempotency key and reuses it for automatic retries.
    with Comfy() as client:
        result = client.models.run(
            "openai/o3",
            {
                "input": "Reply with the single word: ok",
                "max_output_tokens": 1024,
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("openai/o3", {
      input: "Reply with the single word: ok",
      max_output_tokens: 1024,
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/openai/o3 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input\": \"Reply with the single word: ok\", \"max_output_tokens\": 1024}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/openai/o3/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

Python

TypeScript

cURL
    
    
    import asyncio
    from comfy_sdk import AsyncComfy
    
    # Reads COMFY_API_KEY from the environment.
    # Each submit() call mints its own Idempotency-Key and reuses it for automatic retries.
    async def main():
        async with AsyncComfy() as client:
            handle = await client.models.submit(
                "openai/o3",
                {
                    "input": "Reply with the single word: ok",
                    "max_output_tokens": 1024,
                },
            )
            print("request_id:", handle.request_id)  # with the model ID, all another process needs
    
            # Poll until the request completes, waiting the Retry-After the server names.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # The provider's own payload, the same value models.run() returns.
            # A request that failed or was cancelled raises the typed Router error here.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // Each submit() call mints its own Idempotency-Key and reuses it for automatic retries.
    const handle = await comfy.models.submit("openai/o3", {
      input: "Reply with the single word: ok",
      max_output_tokens: 1024,
    });
    console.log("requestId:", handle.requestId); // with the model ID, all another process needs
    
    // Poll until the request completes, waiting the Retry-After the server names.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // The same result models.run() returns. A request that failed or was cancelled rejects here.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Submit. Router answers 201 with request_id, status_url, response_url and cancel_url.
    curl https://api.comfy.org/v2/models/openai/o3/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input\": \"Reply with the single word: ok\", \"max_output_tokens\": 1024}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/openai/o3/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/openai/o3/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Schema

### 

​

Input

​

include

string[]

Additional output data to include in the model response.

​

input

string | object[]

required

Text, image or file inputs to the model, used to generate a response. The one field of this contract Router cannot supply, and the only entry in `required` below.

​

instructions

string

Inserts a system (or developer) message as the first item in the model’s context.

​

max_output_tokens

integer

An upper bound for the number of tokens generated for a response, including visible output tokens and reasoning tokens. On a reasoning id this ceiling is shared with the hidden reasoning tokens, so a small value can consume the whole budget before any visible text — which is why the reasoning smoke cases send 1024 where the chat ones send 16.Range: `1` to `…`

​

model

string

OpenAI model identifier. On Comfy Router this field is OPTIONAL and Router fills it from the `{model}` path segment; an explicit `null` is replaced the same way. Sending a value that disagrees with the path is refused.

​

parallel_tool_calls

boolean

Whether to allow the model to run tool calls in parallel.

​

previous_response_id

string

The ID of a previous response, for multi-turn conversations.

​

reasoning

object

REASONING TIER ONLY. Configuration for reasoning models, e.g. `{"effort": "medium"}`. Forwarded unchanged; see OpenAI’s reasoning guide for the accepted keys. A chat-tier id ignores it.

​

store

boolean

Whether OpenAI stores the generated response for later retrieval.

​

stream

boolean

Declared so a caller who sends it is not refused, but INERT on this surface: Router SETTLES it to `false` before dispatch, because it captures the provider response rather than relaying a `text/event-stream` — which it cannot decode, so a streamed generation would be billed by OpenAI and metered by nobody. No Comfy surface serves the stream: the v1 `POST /proxy/openai/v1/responses` ingress refuses `stream: true` with a 400 and never forwards the request upstream, so omit the field or send `false` on either surface and read the completed response as one JSON body.

​

temperature

number

Sampling temperature. CHAT TIER ONLY: the o-series reasoning ids (`o1`, `o1-pro`, `o3`, `o4-mini`) reject this parameter at OpenAI. Router does not refuse it for them — see this component’s note on why the two tiers share one schema — so a reasoning call that sends it is answered by OpenAI’s own error.Range: `0` to `2`

​

text

object

Output-format configuration, e.g. `{"format": {"type": "json_schema", ...}}` for Structured Outputs. Forwarded unchanged.

​

tool_choice

string | object

How the model should select which tool to use. Either a string mode or an object naming a tool.

​

tools

object[]

Tool definitions the model may call. Router does not narrow the tool taxonomy; see OpenAI’s Responses API reference for the accepted shapes.

​

top_p

number

Nucleus-sampling cutoff. CHAT TIER ONLY, on the same terms as `temperature`.Range: `0` to `1`

​

truncation

string

Truncation strategy when the context exceeds the model’s window. The enum IS enforced here, unlike the three vocabularies above, because these two values are the complete set OpenAI documents and it has not grown. An explicit `null` is still accepted, on the same terms as the fields above it.Possible values: `auto`, `disabled`

​

usage

object

Token-usage envelope. Present on this contract because the v1 operation declares it on the request body; OpenAI populates it on the RESPONSE, so a caller has no reason to send it.

Generated from the schema Router serves at `GET /v2/models/openai/o3/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

instructions

string

Inserts a system (or developer) message as the first item in the model’s context.When using along with `previous_response_id`, the instructions from a previous response will not be carried over to the next response. This makes it simple to swap out system (or developer) messages in new responses.

​

max_output_tokens

integer

An upper bound for the number of tokens that can be generated for a response, including visible output tokens and [reasoning tokens](https://platform.openai.com/docs/guides/reasoning).

​

model

string

The model used to generate the response

​

temperature

number

default:"1"

Controls randomness in the responseRange: `0` to `2`

​

top_p

number

default:"1"

Controls diversity of the response via nucleus samplingRange: `0` to `1`

​

truncation

string

default:"\"disabled\""

The truncation strategy to use for the model response.

  * `auto`: If the context of this response and previous ones exceeds the model’s context window size, the model will truncate the response to fit the context window by dropping input items in the middle of the conversation.
  * `disabled` (default): If a model response will exceed the context window size for a model, the request will fail with a 400 error. Possible values: `auto`, `disabled`



​

previous_response_id

string

The unique ID of the previous response to the model. Use this to create multi-turn conversations. Learn more about [conversation state](https://platform.openai.com/docs/guides/conversation-state).

​

reasoning

object

**o-series models only** Configuration options for [reasoning models](https://platform.openai.com/docs/guides/reasoning).

​

reasoning.context

string

Controls which reasoning items are rendered back to the model on later turns, e.g. `auto`, `current_turn`, or `all_turns`.

​

reasoning.effort

string

default:"\"medium\""

**o-series models only** Constrains effort on reasoning for [reasoning models](https://platform.openai.com/docs/guides/reasoning). Currently supported values are `low`, `medium`, and `high`. Reducing reasoning effort can result in faster responses and fewer tokens used on reasoning in a response.Possible values: `low`, `medium`, `high`

​

reasoning.generate_summary

string

**Deprecated:** use `summary` instead.A summary of the reasoning performed by the model. This can be useful for debugging and understanding the model’s reasoning process. One of `auto`, `concise`, or `detailed`.Possible values: `auto`, `concise`, `detailed`

​

reasoning.mode

string

The reasoning mode used for the response.

​

reasoning.summary

string

A summary of the reasoning performed by the model. This can be useful for debugging and understanding the model’s reasoning process. One of `auto`, `concise`, or `detailed`.Possible values: `auto`, `concise`, `detailed`

​

text

object

​

text.format

object

An object specifying the format that the model must output.Configuring `{ "type": "json_schema" }` enables Structured Outputs, which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).The default format is `{ "type": "text" }` with no additional options.**Not recommended for gpt-4o and newer models:** Setting to `{ "type": "json_object" }` enables the older JSON mode, which ensures the message the model generates is valid JSON. Using `json_schema` is preferred for models that support it.

​

text.verbosity

string

Constrains the verbosity of the model’s response. One of `low`, `medium`, or `high`.

​

tool_choice

`none`, `auto`, `required` | object

How the model should select which tool (or tools) to use when generating a response. See the `tools` parameter to see how to specify which tools the model can call.

​

tools

object[]

​

background

boolean

Whether the model response runs in the background.

​

billing

object

Billing information for the response.

​

billing.payer

string

The party responsible for paying for the response.

​

completed_at

number

Unix timestamp (in seconds) of when this Response was completed. Only present when the status is `completed`.

​

created_at

number

Unix timestamp (in seconds) of when this Response was created.

​

error

object

An error object returned when the model fails to generate a Response.

​

error.code

string

required

The error code for the response.Possible values: `server_error`, `rate_limit_exceeded`, `invalid_prompt`, `vector_store_timeout`, `invalid_image`, `invalid_image_format`, `invalid_base64_image`, `invalid_image_url`, `image_too_large`, `image_too_small`, `image_parse_error`, `image_content_policy_violation`, `invalid_image_mode`, `image_file_too_large`, `unsupported_image_media_type`, `empty_image_file`, `failed_to_download_image`, `image_file_not_found`

​

error.message

string

required

A human-readable description of the error.

​

frequency_penalty

number

Penalizes new tokens based on their existing frequency in the text so far.

​

id

string

Unique identifier for this Response.

​

incomplete_details

object

Details about why the response is incomplete.

​

incomplete_details.reason

string

The reason why the response is incomplete.Possible values: `max_output_tokens`, `content_filter`

​

max_tool_calls

integer

The maximum number of total calls to built-in tools that can be processed in a response.

​

metadata

object

Set of key-value pairs that can be attached to the response.

​

moderation

object

Moderation results for the response input and output, if moderated completions were requested.

​

object

string

The object type of this resource - always set to `response`.Possible values: `response`

​

output

object[]

An array of content items generated by the model.

  * The length and order of items in the `output` array is dependent on the model’s response.
  * Rather than accessing the first item in the `output` array and assuming it’s an `assistant` message with the content generated by the model, you might consider using the `output_text` property where supported in SDKs.



​

output_text

string

SDK-only convenience property that contains the aggregated text output from all `output_text` items in the `output` array, if any are present. Supported in the Python and JavaScript SDKs.

​

parallel_tool_calls

boolean

default:"true"

Whether to allow the model to run tool calls in parallel.

​

presence_penalty

number

Penalizes new tokens based on whether they appear in the text so far.

​

prompt_cache_key

string

Used by OpenAI to cache responses for similar requests to optimize cache hit rates. Replaces the `user` field.

​

prompt_cache_retention

string

The retention policy for the prompt cache, e.g. `in_memory` or `24h`.

​

safety_identifier

string

A stable identifier used to help detect users of your application that may be violating OpenAI’s usage policies.

​

service_tier

string

The processing tier used to serve the request, e.g. `auto`, `default`, `flex`, `scale`, or `priority`.

​

status

string

The status of the response generation. One of `completed`, `failed`, `in_progress`, `cancelled`, `queued`, or `incomplete`.Possible values: `completed`, `failed`, `in_progress`, `cancelled`, `queued`, `incomplete`

​

store

boolean

Whether the response is stored for later retrieval via the API.

​

tool_usage

object

Token and request usage broken down by built-in tool.

​

tool_usage.image_gen

object

Image generation tool token usage.

​

tool_usage.image_gen.input_tokens

integer

​

tool_usage.image_gen.input_tokens_details

object

​

tool_usage.image_gen.input_tokens_details.image_tokens

integer

​

tool_usage.image_gen.input_tokens_details.text_tokens

integer

​

tool_usage.image_gen.output_tokens

integer

​

tool_usage.image_gen.output_tokens_details

object

​

tool_usage.image_gen.output_tokens_details.image_tokens

integer

​

tool_usage.image_gen.output_tokens_details.text_tokens

integer

​

tool_usage.image_gen.total_tokens

integer

​

tool_usage.web_search

object

Web search tool usage.

​

tool_usage.web_search.num_requests

integer

​

top_logprobs

integer

The maximum number of most likely tokens to return at each token position, each with an associated log probability.

​

usage

object

Represents token usage details including input tokens, output tokens, a breakdown of output tokens, and the total tokens used.

​

usage.input_tokens

integer

required

The number of input tokens.

​

usage.input_tokens_details

object

required

A detailed breakdown of the input tokens.

​

usage.input_tokens_details.cache_write_tokens

integer

The number of input tokens that were written to the cache.

​

usage.input_tokens_details.cached_tokens

integer

required

The number of tokens that were retrieved from the cache. [More on prompt caching](https://platform.openai.com/docs/guides/prompt-caching).

​

usage.output_tokens

integer

required

The number of output tokens.

​

usage.output_tokens_details

object

required

A detailed breakdown of the output tokens.

​

usage.output_tokens_details.reasoning_tokens

integer

required

The number of reasoning tokens.

​

usage.total_tokens

integer

required

The total number of tokens used.

​

user

string

Deprecated identifier for the end-user. Replaced by `safety_identifier` and `prompt_cache_key`.

## 

​

Examples

### 

​

Input
    
    
    {
      "input": "Reply with the single word: ok",
      "max_output_tokens": 1024
    }
    

### 

​

Output
    
    
    {
      "completed_at": 1767225601,
      "created_at": 1767225600,
      "id": "resp_0a1b2c3d4e5f6a7b8c9d0e1f",
      "object": "response",
      "output": [
        {
          "content": [
            {
              "annotations": [],
              "text": "ok",
              "type": "output_text"
            }
          ],
          "id": "msg_0a1b2c3d4e5f6a7b8c9d0e1f",
          "role": "assistant",
          "status": "completed",
          "type": "message"
        }
      ],
      "output_text": "ok",
      "status": "completed",
      "usage": {
        "input_tokens": 14,
        "input_tokens_details": {
          "cached_tokens": 0
        },
        "output_tokens": 2,
        "output_tokens_details": {
          "reasoning_tokens": 0
        },
        "total_tokens": 16
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/openai/o3/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/openai/o3/code)

[Use o1 with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/openai/o1/code)[Use o4-mini with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/openai/o4-mini/code)

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
