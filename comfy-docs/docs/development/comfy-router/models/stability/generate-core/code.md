---
url: https://docs.comfy.org/development/comfy-router/models/stability/generate-core/code/
title: Use Generate Core with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-09T17:17:30.050750+00:00
---

# Use Generate Core with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/stability/generate-core/code/

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



Stability

# Use Generate Core with Comfy Router

Copy pageCopy page

Call stability/generate-core through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `stability/generate-core`, served by Comfy Router from Stability. **Input:** Text · **Output:** Image

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `stability/generate-core` **Endpoint:** `POST https://api.comfy.org/v2/models/stability/generate-core`

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
            "stability/generate-core",
            {
                "aspect_ratio": "16:9",
                "prompt": "a lighthouse on a cliff at sunset, oil painting",
                "seed": 12345,
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("stability/generate-core", {
      aspect_ratio: "16:9",
      prompt: "a lighthouse on a cliff at sunset, oil painting",
      seed: 12345,
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/stability/generate-core \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"aspect_ratio\": \"16:9\", \"prompt\": \"a lighthouse on a cliff at sunset, oil painting\", \"seed\": 12345}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/stability/generate-core/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "stability/generate-core",
                {
                    "aspect_ratio": "16:9",
                    "prompt": "a lighthouse on a cliff at sunset, oil painting",
                    "seed": 12345,
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
    const handle = await comfy.models.submit("stability/generate-core", {
      aspect_ratio: "16:9",
      prompt: "a lighthouse on a cliff at sunset, oil painting",
      seed: 12345,
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
    curl https://api.comfy.org/v2/models/stability/generate-core/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"aspect_ratio\": \"16:9\", \"prompt\": \"a lighthouse on a cliff at sunset, oil painting\", \"seed\": 12345}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/stability/generate-core/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/stability/generate-core/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Schema

### 

​

Input

​

aspect_ratio

string

Text-to-image only. Output aspect ratio. Default 1:1.Possible values: `1:1`, `16:9`, `9:16`, `21:9`, `9:21`, `3:2`, `2:3`, `5:4`, `4:5`

​

image

string (uri)

`stability/generate-ultra` only. A Comfy-signed asset URL of a source image; sending it switches to image-to-image and requires `strength`.Format: `uri`

​

negative_prompt

string

What to keep out of the image.

​

output_format

string

Only `png` is returned.Possible values: `png`

​

prompt

string

required

What to generate.

​

seed

integer

0 or omitted picks a random seed.Range: `0` to `4294967294`

​

strength

number

`stability/generate-ultra` image-to-image only. How far to move from the source image; 1 ignores it.Range: `0` to `1`

​

style_preset

string

Stability style preset, for example `photographic`.

Generated from the schema Router serves at `GET /v2/models/stability/generate-core/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

finish_reason

string

required

Always SUCCESS on a 200.

​

image

string (uri)

required

Comfy-signed URL of the (first) PNG image, valid for up to 24 hours.Format: `uri`

​

images

string (uri)[]

SDXL only, when more than one image was returned. Every Comfy-signed image URL, in output order, each valid for up to 24 hours.

​

seed

integer

required

The seed the image was generated with.

## 

​

Examples

### 

​

Input
    
    
    {
      "aspect_ratio": "16:9",
      "prompt": "a lighthouse on a cliff at sunset, oil painting",
      "seed": 12345
    }
    

### 

​

Output
    
    
    {
      "finish_reason": "SUCCESS",
      "image": "https://example.invalid/stability/image.png",
      "seed": 12345
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/stability/generate-core/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/stability/generate-core/code)

[Edit Search And Replace](https://docs.comfy.org/development/comfy-router/models/stability/edit-search-and-replace/code)[Generate Ultra](https://docs.comfy.org/development/comfy-router/models/stability/generate-ultra/code)
