---
url: https://docs.comfy.org/development/comfy-router/models/fal/crystal-upscaler/code/
title: Use Crystal Upscaler with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:04.433354+00:00
---

# Use Crystal Upscaler with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/fal/crystal-upscaler/code/

## On this page

  * Quick start
  * Schema
    * Input
    * Output
  * Examples
    * Input
    * Output
  * Before you ship



fal

# Use Crystal Upscaler with Comfy Router

Copy pageCopy page

Call fal/crystal-upscaler through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `fal/crystal-upscaler`, served by Comfy Router from fal. **Input:** Image · **Output:** Image

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `fal/crystal-upscaler` **Endpoint:** `POST https://api.comfy.org/v2/models/fal/crystal-upscaler`

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
            "fal/crystal-upscaler",
            {
                "image_url": "https://storage.googleapis.com/falserverless/gallery/patina-blog-hero-render.png",
                "scale_factor": 2,
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("fal/crystal-upscaler", {
      image_url: "https://storage.googleapis.com/falserverless/gallery/patina-blog-hero-render.png",
      scale_factor: 2,
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/fal/crystal-upscaler \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"image_url\": \"https://storage.googleapis.com/falserverless/gallery/patina-blog-hero-render.png\", \"scale_factor\": 2}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/fal/crystal-upscaler/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "fal/crystal-upscaler",
                {
                    "image_url": "https://storage.googleapis.com/falserverless/gallery/patina-blog-hero-render.png",
                    "scale_factor": 2,
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
    const handle = await comfy.models.submit("fal/crystal-upscaler", {
      image_url: "https://storage.googleapis.com/falserverless/gallery/patina-blog-hero-render.png",
      scale_factor: 2,
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
    curl https://api.comfy.org/v2/models/fal/crystal-upscaler/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"image_url\": \"https://storage.googleapis.com/falserverless/gallery/patina-blog-hero-render.png\", \"scale_factor\": 2}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/fal/crystal-upscaler/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/fal/crystal-upscaler/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Schema

### 

​

Input

​

creativity

number

default:"0"

How much new detail the model may invent. 0 keeps closest to the input.Range: `0` to `10`

​

image_url

string

required

URL of the input image (JPEG, PNG, WebP, GIF or AVIF, at most 100 MB).

​

output_format

string

default:"\"jpg\""

Output image format: png or jpg.

​

scale_factor

number

default:"2"

Factor applied to each side of the input image. fal bills per output megapixel, so the price grows with the square of this value.Range: `1` to `200`

Generated from the schema Router serves at `GET /v2/models/fal/crystal-upscaler/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

images

object[]

required

The upscaled images.

​

images[].content_type

string

MIME type of the image file.

​

images[].file_name

string

Name of the image file.

​

images[].file_size

integer

Size of the image file in bytes.

​

images[].height

integer

Height of the image in pixels. fal sends null.

​

images[].url

string

required

URL of the upscaled image.

​

images[].width

integer

Width of the image in pixels. fal sends null.

## 

​

Examples

### 

​

Input
    
    
    {
      "image_url": "https://storage.googleapis.com/falserverless/gallery/patina-blog-hero-render.png",
      "scale_factor": 2
    }
    

### 

​

Output
    
    
    {
      "images": [
        {
          "content_type": "image/png",
          "file_name": "upscaled.png",
          "file_size": 1412332,
          "height": null,
          "url": "https://example.invalid/fal/crystal-upscaler/upscaled.png",
          "width": null
        }
      ]
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/fal/crystal-upscaler/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/fal/crystal-upscaler/code)

[Use Eleven V4 with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/elevenlabs/eleven-v4/code)[Use H3 Max Turbo with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/fal/h3-max-turbo/code)

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
