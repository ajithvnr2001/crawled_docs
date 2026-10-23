---
url: https://docs.comfy.org/development/comfy-router/models/anthropic/claude-sonnet-5/code/
title: Use Claude Sonnet 5 with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:48.542640+00:00
---

# Use Claude Sonnet 5 with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/anthropic/claude-sonnet-5/code/

## On this page

  * Quick start
  * Schema
    * Input
    * Output
  * Examples
    * Input
    * Output
  * Before you ship



Anthropic

# Use Claude Sonnet 5 with Comfy Router

Copy pageCopy page

Call anthropic/claude-sonnet-5 through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `anthropic/claude-sonnet-5`, served by Comfy Router from Anthropic. **Input:** Text, Image · **Output:** Text

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `anthropic/claude-sonnet-5` **Endpoint:** `POST https://api.comfy.org/v2/models/anthropic/claude-sonnet-5`

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
            "anthropic/claude-sonnet-5",
            {
                "max_tokens": 16,
                "messages": [
                    {
                        "content": "Reply with the single word: ok",
                        "role": "user",
                    },
                ],
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("anthropic/claude-sonnet-5", {
      max_tokens: 16,
      messages: [
        {
          content: "Reply with the single word: ok",
          role: "user",
        },
      ],
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/anthropic/claude-sonnet-5 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"max_tokens\": 16, \"messages\": [{\"content\":\"Reply with the single word: ok\",\"role\":\"user\"}]}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/anthropic/claude-sonnet-5/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "anthropic/claude-sonnet-5",
                {
                    "max_tokens": 16,
                    "messages": [
                        {
                            "content": "Reply with the single word: ok",
                            "role": "user",
                        },
                    ],
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
    const handle = await comfy.models.submit("anthropic/claude-sonnet-5", {
      max_tokens: 16,
      messages: [
        {
          content: "Reply with the single word: ok",
          role: "user",
        },
      ],
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
    curl https://api.comfy.org/v2/models/anthropic/claude-sonnet-5/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"max_tokens\": 16, \"messages\": [{\"content\":\"Reply with the single word: ok\",\"role\":\"user\"}]}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/anthropic/claude-sonnet-5/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/anthropic/claude-sonnet-5/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Schema

### 

​

Input

​

max_tokens

integer

required

Maximum number of tokens to generate before stopping.

​

messages

object[]

required

Conversation turns. See Anthropic Messages API docs for the full content-block taxonomy.

​

messages[].content

object

required

Either a string shorthand or an array of content blocks (text, image, document, tool_use, tool_result, …).

​

messages[].role

string

required

Possible values: `user`, `assistant`

​

model

string

Anthropic model identifier (e.g. `claude-sonnet-4-5`, `claude-opus-4-7`).

​

stream

boolean

When true, the response is a `text/event-stream` of Anthropic message events instead of a single JSON body.

​

system

object

Top-level system prompt. Either a string or an array of content blocks; both reach Anthropic unchanged.

Generated from the schema Router serves at `GET /v2/models/anthropic/claude-sonnet-5/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

id

string

​

model

string

​

role

string

​

stop_reason

string

​

stop_sequence

string

​

type

string

​

usage

object

Token usage for an Anthropic Messages API call.

​

usage.cache_creation

object

Per-TTL breakdown of cache-write input tokens for an Anthropic Messages API call.

​

usage.cache_creation.ephemeral_1h_input_tokens

integer

​

usage.cache_creation.ephemeral_5m_input_tokens

integer

​

usage.cache_creation_input_tokens

integer

​

usage.cache_read_input_tokens

integer

​

usage.input_tokens

integer

​

usage.output_tokens

integer

​

content

object[]

required

The reply’s content blocks, in order. Present on every completed message; empty when the turn produced nothing.

​

content[].text

string

The block’s text. Present on `text` blocks and absent on every other kind.

​

content[].type

string

The block kind. `text` is the one that carries `text`; `thinking`, `redacted_thinking`, `tool_use`, `server_tool_use` and the tool-result blocks are the others Anthropic sends today, and the list is open.

## 

​

Examples

### 

​

Input
    
    
    {
      "max_tokens": 16,
      "messages": [
        {
          "content": "Reply with the single word: ok",
          "role": "user"
        }
      ]
    }
    

### 

​

Output
    
    
    {
      "content": [
        {
          "text": "ok",
          "type": "text"
        }
      ],
      "id": "msg_01ExampleInvalidPlaceholder",
      "model": "claude-sonnet-5",
      "role": "assistant",
      "stop_reason": "end_turn",
      "stop_sequence": null,
      "type": "message",
      "usage": {
        "input_tokens": 16,
        "output_tokens": 3
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/anthropic/claude-sonnet-5/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/anthropic/claude-sonnet-5/code)

[Use Claude Sonnet 5.5 with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/anthropic/claude-sonnet-5-5/code)[Use SwitchX with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/beeble/switchx/code)

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
