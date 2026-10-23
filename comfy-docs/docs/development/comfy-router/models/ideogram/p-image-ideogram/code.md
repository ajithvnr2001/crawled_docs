---
url: https://docs.comfy.org/development/comfy-router/models/ideogram/p-image-ideogram/code/
title: Use P Image Ideogram with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:12.345404+00:00
---

# Use P Image Ideogram with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/ideogram/p-image-ideogram/code/

## On this page

  * Quick start
  * Schema
    * Input
    * Output
  * Examples
    * Input
    * Output
  * Before you ship



Ideogram

# Use P Image Ideogram with Comfy Router

Copy pageCopy page

Call ideogram/p-image-ideogram through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `ideogram/p-image-ideogram`, served by Comfy Router from Ideogram. **Input:** Text · **Output:** Image

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `ideogram/p-image-ideogram` **Endpoint:** `POST https://api.comfy.org/v2/models/ideogram/p-image-ideogram`

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
            "ideogram/p-image-ideogram",
            {
                "prompt": "A beautiful mountain landscape",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("ideogram/p-image-ideogram", {
      prompt: "A beautiful mountain landscape",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/ideogram/p-image-ideogram \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"A beautiful mountain landscape\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/ideogram/p-image-ideogram/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "ideogram/p-image-ideogram",
                {
                    "prompt": "A beautiful mountain landscape",
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
    const handle = await comfy.models.submit("ideogram/p-image-ideogram", {
      prompt: "A beautiful mountain landscape",
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
    curl https://api.comfy.org/v2/models/ideogram/p-image-ideogram/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"A beautiful mountain landscape\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/ideogram/p-image-ideogram/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/ideogram/p-image-ideogram/requests/$REQUEST_ID \
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

Aspect ratio in format WxH. Supported values: 1x3, 3x1, 1x2, 2x1, 9x16, 16x9, 10x16, 16x10, 2x3, 3x2, 3x4, 4x3, 4x5, 5x4, 1x1. Defaults to 1x1.

​

enable_copyright_detection

boolean

Opt into post-generation copyright detection (Hive likeness and logo checks).

​

prompt

string

required

The prompt for image generation, either natural language or an Ideogram 4.0 JSON structured prompt.

​

prompt_upsampling

string

Prompt upsampling mode. Supported values are AUTO, ON, and OFF. Defaults to AUTO.

​

quality

string

Generation quality level. Supported values are VERY_LOW, LOW, MEDIUM, and HIGH. Defaults to MEDIUM.

​

resolution

string

Output resolution. Supported values are 1K and 2K. Defaults to 1K.

​

seed

integer

Seed value for reproducible generation

Generated from the schema Router serves at `GET /v2/models/ideogram/p-image-ideogram/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

created

string (date-time)

Timestamp when the generation was created.Format: `date-time`

​

data

object[]

Array of generated image information.

​

data[].is_image_safe

boolean

Indicates whether the image is considered safe.

​

data[].prompt

string

The prompt used to generate this image.

​

data[].resolution

string

The resolution of the generated image (e.g., ‘1024x1024’).

​

data[].seed

integer

The seed value used for this generation.

​

data[].style_type

string

The style type used for generation (e.g., ‘REALISTIC’, ‘ANIME’).

​

data[].url

string

URL to the generated image.

## 

​

Examples

### 

​

Input
    
    
    {
      "prompt": "A beautiful mountain landscape"
    }
    

### 

​

Output
    
    
    {
      "created": "2026-01-01T00:00:00Z",
      "data": [
        {
          "is_image_safe": true,
          "prompt": "A poster for a jazz festival, bold typography, warm colours",
          "resolution": "1024x1024",
          "seed": 918273645,
          "style_type": "REALISTIC",
          "url": "https://example.invalid/ideogram/p-image-ideogram/generated.png"
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/ideogram/p-image-ideogram/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/ideogram/p-image-ideogram/code)

[Use Ideogram 4.0 with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/ideogram/ideogram-v4/code)[Use Kling 3.0 Turbo with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/kling/kling-3-0-turbo/code)

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
