---
url: https://docs.comfy.org/development/comfy-router/models/byteplus/seed-2-0-mini-260215/code/
title: Use Seed 2.0 Mini 260215 with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:58.862033+00:00
---

# Use Seed 2.0 Mini 260215 with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/byteplus/seed-2-0-mini-260215/code/

## On this page

  * Quick start
  * Schema
    * Input
    * Output
  * Examples
    * Input
    * Output
  * Before you ship



BytePlus

# Use Seed 2.0 Mini 260215 with Comfy Router

Copy pageCopy page

Call byteplus/seed-2-0-mini-260215 through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `byteplus/seed-2-0-mini-260215`, served by Comfy Router from BytePlus. **Input:** Text, Image · **Output:** Text

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `byteplus/seed-2-0-mini-260215` **Endpoint:** `POST https://api.comfy.org/v2/models/byteplus/seed-2-0-mini-260215`

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
            "byteplus/seed-2-0-mini-260215",
            {
                "input": "Reply with the single word: ok",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("byteplus/seed-2-0-mini-260215", {
      input: "Reply with the single word: ok",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/byteplus/seed-2-0-mini-260215 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input\": \"Reply with the single word: ok\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/byteplus/seed-2-0-mini-260215/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "byteplus/seed-2-0-mini-260215",
                {
                    "input": "Reply with the single word: ok",
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
    const handle = await comfy.models.submit("byteplus/seed-2-0-mini-260215", {
      input: "Reply with the single word: ok",
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
    curl https://api.comfy.org/v2/models/byteplus/seed-2-0-mini-260215/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input\": \"Reply with the single word: ok\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/byteplus/seed-2-0-mini-260215/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/byteplus/seed-2-0-mini-260215/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Schema

### 

​

Input

​

caching

object

Context-cache configuration.

​

caching.prefix

boolean

default:"false"

When true, only create the public prefix cache; the model does not respond.

​

caching.type

string

Possible values: `enabled`, `disabled`

​

context_management

object

Context-management strategies (`clear_thinking`, `clear_tool_uses`) applied to keep the context window manageable.

​

context_management.edits

object[]

A single context-edit strategy, discriminated by `type`.

​

expire_at

integer

Unix timestamp (seconds, UTC) at which the stored response and cache expire. Range (creation_time, creation_time + 604800]. Default: creation_time + 259200 (3 days).

​

include

string[]

Additional output fields to include. Currently supported: `reasoning.encrypted_content` (encrypted+compressed reasoning for manual multi-turn reuse).

​

input

string | object[]

required

Text content or list of input items provided to the model.

​

instructions

string

System/developer message prepended as the first instruction. Not compatible with `caching` — if `caching.type` is `enabled`, setting `instructions` returns an error.

​

max_output_tokens

integer

Maximum output tokens (response + chain-of-thought).

​

max_tool_calls

integer

Range: `1` to `10`

​

model

string

Model ID or Endpoint ID. See <https://docs.byteplus.com/en/docs/ModelArk/1330310> for the model list and <https://docs.byteplus.com/en/docs/ModelArk/1099522> for Endpoint IDs. A direct v1 call to POST /proxy/byteplus/api/v3/responses MUST supply it — the proxy refuses any value outside its own allowlist, and an omitted one, with a 400. It is NOT in the Comfy Router input schemas’ `required` lists because Router fills it from the `{model}` path segment of /v2/models/byteplus/{model}, so a Router caller omits it.

​

previous_response_id

string

ID of the previous response, used to continue a multi-turn conversation. Insert ~100ms between requests to avoid failures.

​

reasoning

object

Limits the workload of deep thinking.

​

reasoning.effort

string

`minimal` disables thinking entirely. With `thinking.type = disabled`, only `minimal` is allowed.Possible values: `minimal`, `low`, `medium`, `high`

​

store

boolean

default:"true"

When true, the response is persisted and retrievable by ID for multi-turn use.

​

temperature

number

default:"1"

Range: `0` to `2`Format: `float`

​

text

object

Output-format configuration.

​

text.format

object

Text-output format discriminated by `type`. `text` returns natural language, `json_object` returns a free-form JSON object, `json_schema` constrains output to a caller-supplied JSON Schema.

​

thinking

object

Controls deep-thinking mode.

​

thinking.type

string

`enabled`: always reason before responding. `disabled`: respond without additional reasoning. `auto`: model decides per-query.Possible values: `enabled`, `disabled`, `auto`

​

tool_choice

`none`, `auto`, `required` | object

Tool-selection mode. Only seed-1-6 models support this field.

​

tools

object[]

A tool the model may invoke. Currently only `function` is supported.

​

tools[].description

string

​

tools[].name

string

required

​

tools[].parameters

object

required

JSON Schema describing the function’s parameters.

​

tools[].type

string

default:"\"function\""

required

Possible values: `function`

​

top_p

number

default:"0.7"

Range: `0` to `1`Format: `float`

Generated from the schema Router serves at `GET /v2/models/byteplus/seed-2-0-mini-260215/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

caching

object

​

caching.prefix

boolean

​

caching.type

string

Possible values: `enabled`, `disabled`

​

context_management

object

Context-management strategies that were actually applied during this response. Unlike the request-side `BytePlusResponseContextManagement` (which configures strategies), this echoes the strategies the server invoked, with counts of what was cleared.

​

context_management.applied_edits

object[]

One applied context-edit, discriminated by `type`.

​

created_at

integer

required

Unix timestamp (seconds) when the response was created.

​

error

object

Error details. Null when the response succeeded.

​

error.code

string

required

​

error.message

string

required

​

expire_at

integer

Unix timestamp (seconds) when the stored response expires.

​

id

string

required

Unique ID of the response. Use as `previous_response_id` to continue the conversation.

​

incomplete_details

object

Populated when `status` is `incomplete`.

​

incomplete_details.reason

string

e.g. `max_output_tokens`, `content_filter`.

​

instructions

string

Echo of the request’s `instructions` field.

​

max_output_tokens

integer

​

max_tool_calls

integer

​

metadata

object

​

model

string

required

Model ID that generated the response.

​

object

string

default:"\"response\""

required

Possible values: `response`

​

output

object[]

required

Ordered output items produced by the model.

​

previous_response_id

string

​

reasoning

object

​

reasoning.effort

string

Possible values: `minimal`, `low`, `medium`, `high`

​

service_tier

string

TPM-guarantee-package usage. `default` means none.Possible values: `default`

​

status

string

required

Possible values: `in_progress`, `completed`, `incomplete`, `failed`, `cancelled`

​

store

boolean

​

stream

boolean

​

temperature

number

Format: `float`

​

text

object

Echo of the request’s `text` field.

​

text.format

object

Text-output format discriminated by `type`. `text` returns natural language, `json_object` returns a free-form JSON object, `json_schema` constrains output to a caller-supplied JSON Schema.

​

thinking

object

​

thinking.type

string

Possible values: `enabled`, `disabled`, `auto`

​

tool_choice

`none`, `auto`, `required` | object

​

tools

object[]

A tool the model may invoke. Currently only `function` is supported.

​

tools[].description

string

​

tools[].name

string

required

​

tools[].parameters

object

required

JSON Schema describing the function’s parameters.

​

tools[].type

string

default:"\"function\""

required

Possible values: `function`

​

top_p

number

Format: `float`

​

usage

object

Token-usage breakdown for billing and observability.

​

usage.input_tokens

integer

required

Total tokens in the request.

​

usage.input_tokens_details

object

Breakdown of input tokens (cache hits, etc).

​

usage.input_tokens_details.cached_tokens

integer

Tokens served from the context cache.

​

usage.output_tokens

integer

required

Total tokens generated by the model.

​

usage.output_tokens_details

object

Breakdown of output tokens (reasoning, etc).

​

usage.output_tokens_details.reasoning_tokens

integer

Tokens consumed by chain-of-thought.

​

usage.tool_usage

object

Per-tool invocation counts.

​

usage.tool_usage.image_process

integer

Number of image-processing tool calls.

​

usage.tool_usage.mcp

integer

Number of MCP tool calls.

​

usage.tool_usage.web_search

integer

Number of web-search tool invocations.

​

usage.tool_usage_details

object

Per-tool breakdown of sub-tool invocation counts.

​

usage.tool_usage_details.image_process

object

e.g. `{"zoom":1,"point":1,"grounding":1}`.

​

usage.tool_usage_details.mcp

object

e.g. `{"mcp_server_tos":1,"mcp_server_tls":1}`.

​

usage.tool_usage_details.web_search

object

e.g. `{"toutiao":1,"moji":1,"search_engine":1}`.

​

usage.total_tokens

integer

required

input_tokens + output_tokens.

## 

​

Examples

### 

​

Input
    
    
    {
      "input": "Reply with the single word: ok"
    }
    

### 

​

Output
    
    
    {
      "created_at": 1767225600,
      "id": "resp_0a1b2c3d4e5f6a7b8c9d0e1f",
      "model": "seed-2-0-mini-260215",
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
      "status": "completed",
      "usage": {
        "input_tokens": 14,
        "input_tokens_details": {
          "cached_tokens": 0
        },
        "output_tokens": 2,
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/byteplus/seed-2-0-mini-260215/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/byteplus/seed-2-0-mini-260215/code)

[Use Seed 2.0 Lite 260228 with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/byteplus/seed-2-0-lite-260228/code)[Use Seed 2.0 Pro 260328 with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/byteplus/seed-2-0-pro-260328/code)

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
