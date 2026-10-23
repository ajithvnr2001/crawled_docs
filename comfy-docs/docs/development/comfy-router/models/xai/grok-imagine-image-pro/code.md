---
url: https://docs.comfy.org/development/comfy-router/models/xai/grok-imagine-image-pro/code/
title: Use Grok Imagine Image Pro with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:50.826063+00:00
---

# Use Grok Imagine Image Pro with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/xai/grok-imagine-image-pro/code/

## On this page

  * Quick start
  * Schema
    * Input
    * Output
  * Examples
    * Input
    * Output
  * Before you ship



xAI

# Use Grok Imagine Image Pro with Comfy Router

Copy pageCopy page

Call xai/grok-imagine-image-pro through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `xai/grok-imagine-image-pro`, served by Comfy Router from xAI. **Input:** Text · **Output:** Image

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `xai/grok-imagine-image-pro` **Endpoint:** `POST https://api.comfy.org/v2/models/xai/grok-imagine-image-pro`

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
            "xai/grok-imagine-image-pro",
            {
                "n": 1,
                "prompt": "A single red maple leaf on a plain white background.",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("xai/grok-imagine-image-pro", {
      n: 1,
      prompt: "A single red maple leaf on a plain white background.",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/xai/grok-imagine-image-pro \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"n\": 1, \"prompt\": \"A single red maple leaf on a plain white background.\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/xai/grok-imagine-image-pro/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "xai/grok-imagine-image-pro",
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
    const handle = await comfy.models.submit("xai/grok-imagine-image-pro", {
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
    curl https://api.comfy.org/v2/models/xai/grok-imagine-image-pro/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"n\": 1, \"prompt\": \"A single red maple leaf on a plain white background.\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/xai/grok-imagine-image-pro/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/xai/grok-imagine-image-pro/requests/$REQUEST_ID \
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

default:"\"auto\""

Aspect ratio of the generated image. Defaults to auto for automatically selecting the best ratio for the prompt.Possible values: `1:1`, `3:4`, `4:3`, `9:16`, `16:9`, `2:3`, `3:2`, `9:19.5`, `19.5:9`, `9:20`, `20:9`, `1:2`, `2:1`, `auto`

​

model

string

default:"\"grok-imagine-image\""

Model to be used. Supported: grok-imagine-image (default), grok-imagine-image-pro, grok-imagine-image-quality, grok-imagine-image-2.0. Deprecated -beta ids are aliased to their GA model.

​

n

integer

default:"1"

Number of images to be generatedRange: `1` to `10`

​

prompt

string

required

Prompt for image generation

​

quality

string

Quality of the output image. For grok-imagine-image-2.0 this selects the price tier (low/medium; medium is the default); other models currently ignore it.Possible values: `low`, `medium`, `high`

​

resolution

string

default:"\"1k\""

Resolution of the generated image. Defaults to 1k.Possible values: `1k`, `2k`

​

response_format

string

default:"\"url\""

Response format to return the image in. Can be url or b64_json. Comfy coerces this to `url` on the outbound request — on the Comfy Router dispatch (`POST /v2/models/xai/{model}`) and on this `/proxy/` route too — because image results are served as re-hosted URLs either way. A value IN the enum is therefore accepted and ignored; send `url` or `b64_json` or omit the field, and the answer is the same. A value OUTSIDE the enum — excluding the UNSET spellings each surface recognises, described next — is REJECTED rather than coerced on BOTH surfaces, and only the shape of the refusal differs: this `/proxy/` route answers a `400` at ingress, and the `POST /v2/models/xai/{model}` Router dispatch answers the per-field `422` it owes the enum published here, before any partner call is made. The two surfaces differ on what counts as UNSET. On this `/proxy/` route an omitted field, an explicit `null` and `""` all mean unset and are coerced like any accepted value. The Router dispatch enforces the enum exactly as published, so `null` and `""` are non-members there like any other: OMIT the field to leave it unset on that surface.Possible values: `url`, `b64_json`

​

size

string

Size of the image (not supported)

​

style

string

Style of the image (not supported)

​

user

string

A unique identifier representing your end-user, which can help xAI to monitor and detect abuse

Generated from the schema Router serves at `GET /v2/models/xai/grok-imagine-image-pro/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

block_reason

string

If the request was blocked by input moderation, contains the block reason

​

data

object[]

A list of generated image objects

​

data[].b64_json

string

A base64-encoded string representation of the generated image in jpeg encoding (if response_format is b64_json)

​

data[].mime_type

string

The MIME type of the generated image (e.g. image/png, image/jpeg, image/webp).

​

data[].url

string

A url to the generated image (if response_format is url)

​

usage

object

Usage information for the image generation request

​

usage.cost_in_usd_ticks

integer

Accurate cost of this request in USD ticks (10,000,000,000 ticks = 1 USD)

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
      "data": [
        {
          "mime_type": "image/jpeg",
          "url": "https://example.invalid/xai/grok-imagine-image/generated.jpg"
        },
        {
          "mime_type": "image/jpeg",
          "url": "https://example.invalid/xai/grok-imagine-image/generated-2.jpg"
        }
      ],
      "usage": {
        "cost_in_usd_ticks": 200000000
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/xai/grok-imagine-image-pro/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/xai/grok-imagine-image-pro/code)

[Use Grok Imagine Image 2.0 with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/xai/grok-imagine-image-2-0/code)[Use Grok Imagine Image Quality with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/xai/grok-imagine-image-quality/code)

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
