---
url: https://docs.comfy.org/development/comfy-router/models/quiver/arrow-2/code/
title: Use Arrow 2 with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-12T15:52:11.843552+00:00
---

# Use Arrow 2 with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/quiver/arrow-2/code/

## On this page

Back to top

  * Quick start
  * Schema
    * Input
    * Output
  * Examples
    * Input
    * Output
  * Before you ship



Quiver

# Use Arrow 2 with Comfy Router

Copy pageCopy page

Call quiver/arrow-2 through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `quiver/arrow-2`, served by Comfy Router from Quiver. **Input:** Text, Image · **Output:** Image

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `quiver/arrow-2` **Endpoint:** `POST https://api.comfy.org/v2/models/quiver/arrow-2`

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
            "quiver/arrow-2",
            {
                "n": 1,
                "prompt": "A single red maple leaf on a plain white background.",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("quiver/arrow-2", {
      n: 1,
      prompt: "A single red maple leaf on a plain white background.",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/quiver/arrow-2 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"n\": 1, \"prompt\": \"A single red maple leaf on a plain white background.\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/quiver/arrow-2/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "quiver/arrow-2",
                {
                    "n": 1,
                    "prompt": "A single red maple leaf on a plain white background.",
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
    const handle = await comfy.models.submit("quiver/arrow-2", {
      n: 1,
      prompt: "A single red maple leaf on a plain white background.",
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
    curl https://api.comfy.org/v2/models/quiver/arrow-2/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"n\": 1, \"prompt\": \"A single red maple leaf on a plain white background.\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/quiver/arrow-2/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/quiver/arrow-2/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Schema

### 

​

Input

​

instructions

string

Additional style or formatting guidance

​

max_output_tokens

integer

Maximum number of output tokensRange: `1` to `131072`

​

model

string

Model identifier for SVG generation

​

n

integer

default:"1"

Number of SVGs to generateRange: `1` to `16`

​

presence_penalty

number

default:"0"

Penalty for tokens already present in prior output. Ignored by `arrow-2-telos`, which does not accept sampling parameters; the field is removed from the request before it is forwarded, without an error.Range: `-2` to `2`

​

prompt

string

required

Text description of the desired SVG output

​

references

object | string (uri)[]

Optional reference images to guide style/composition. Accepts URL object, base64 object, or URL string shorthand. Runtime limits are model-specific.

​

temperature

number

default:"1"

Sampling temperature. Ignored by `arrow-2-telos`, which does not accept sampling parameters; the field is removed from the request before it is forwarded, without an error.Range: `0` to `2`

​

top_p

number

default:"1"

Nucleus sampling probability. Ignored by `arrow-2-telos`, which does not accept sampling parameters; the field is removed from the request before it is forwarded, without an error.Range: `0` to `1`

Generated from the schema Router serves at `GET /v2/models/quiver/arrow-2/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

created

integer

required

Unix timestamp of creation

​

credits

integer

Credit cost for fixed-credit models such as arrow-1.1. Omitted for token-priced models such as arrow-2, which report measured token totals in usage.Range: `0` to `…`

​

data

object[]

required

​

data[].mime_type

string

required

MIME type of the outputPossible values: `image/svg+xml`

​

data[].svg

string

required

Raw SVG markup

​

id

string

required

Unique identifier for the generation

​

usage

object

Token totals for token-priced models such as arrow-2. Fixed-credit models may report zeros here.

​

usage.input_tokens

integer

Input token count for token-priced models.Range: `0` to `…`

​

usage.output_tokens

integer

Output token count for token-priced models.Range: `0` to `…`

​

usage.total_tokens

integer

Total token count for token-priced models.Range: `0` to `…`

## 

​

Examples

### 

​

Input
    
    
    {
      "n": 1,
      "prompt": "A single red maple leaf on a plain white background."
    }
    

### 

​

Output
    
    
    {
      "created": 1767225600,
      "data": [
        {
          "mime_type": "image/svg+xml",
          "svg": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 64 64\"><path d=\"M32 4 44 28 60 30 48 42 52 60 32 50 12 60 16 42 4 30 20 28Z\"/></svg>"
        }
      ],
      "id": "svg_018f2c7a4b1e7c3d9a056e2f8b41d0c9",
      "usage": {
        "input_tokens": 180,
        "output_tokens": 240,
        "total_tokens": 420
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/quiver/arrow-2/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/quiver/arrow-2/code)

[Arrow 2 Telos](https://docs.comfy.org/development/comfy-router/models/quiver/arrow-2-telos/code)[Qwen Image 3.0 Pro](https://docs.comfy.org/development/comfy-router/models/qwen/qwen-image-3-0-pro/code)
