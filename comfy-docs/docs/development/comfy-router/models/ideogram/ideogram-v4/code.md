---
url: https://docs.comfy.org/development/comfy-router/models/ideogram/ideogram-v4/code/
title: Use Ideogram 4.0 with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:12.151545+00:00
---

# Use Ideogram 4.0 with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/ideogram/ideogram-v4/code/

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

# Use Ideogram 4.0 with Comfy Router

Copy pageCopy page

Python, TypeScript and cURL snippets for generating images with Ideogram 4.0 over HTTP through Comfy Router, plus the request fields and the result shape

Copy pageCopy page

API Reference for Ideogram 4.0. Ideogram 4.0 is Ideogram’s text-to-image model, which renders legible text inside generated images. **Input:** Text · **Output:** Image

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `ideogram/ideogram-v4` **Endpoint:** `POST https://api.comfy.org/v2/models/ideogram/ideogram-v4`

  * Wait for the result

  * Queue and collect later




Python

TypeScript

cURL
    
    
    import asyncio
    from comfy_sdk import AsyncComfy
    
    # Reads COMFY_API_KEY from the environment.
    # The SDK automatically creates an idempotency key and reuses it for automatic retries.
    async def main():
        async with AsyncComfy() as client:
            result = await client.models.run(
                "ideogram/ideogram-v4",
                {
                    "text_prompt": "a single red maple leaf on a plain white background, studio lighting",
                    "resolution": "1024x1024",
                    "rendering_speed": "DEFAULT",
                },
            )
    
        print("image:", result["data"][0]["url"])
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    type Result = { data: { url: string }[] };
    const result = await comfy.models.run<Result>("ideogram/ideogram-v4", {
      text_prompt: "a single red maple leaf on a plain white background, studio lighting",
      resolution: "1024x1024",
      rendering_speed: "DEFAULT",
    });
    if (result.kind !== "json") throw new Error("expected a JSON result");
    
    console.log("image:", result.data.data[0].url);
    
    
    
    curl https://api.comfy.org/v2/models/ideogram/ideogram-v4 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"text_prompt\": \"a single red maple leaf on a plain white background, studio lighting\", \"resolution\": \"1024x1024\", \"rendering_speed\": \"DEFAULT\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/ideogram/ideogram-v4/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "ideogram/ideogram-v4",
                {
                    "text_prompt": "a single red maple leaf on a plain white background, studio lighting",
                    "resolution": "1024x1024",
                    "rendering_speed": "DEFAULT",
                },
            )
            print("request_id:", handle.request_id)  # with the model ID, all another process needs
    
            # Poll until the request completes, waiting the Retry-After the server names.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # The provider's own payload, the same value models.run() returns.
            # A request that failed or was cancelled raises the typed Router error here.
            result = await handle.get()
    
        print("image:", result["data"][0]["url"])
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // Each submit() call mints its own Idempotency-Key and reuses it for automatic retries.
    type Result = { data: { url: string }[] };
    const handle = await comfy.models.submit<Result>("ideogram/ideogram-v4", {
      text_prompt: "a single red maple leaf on a plain white background, studio lighting",
      resolution: "1024x1024",
      rendering_speed: "DEFAULT",
    });
    console.log("requestId:", handle.requestId); // with the model ID, all another process needs
    
    // Poll until the request completes, waiting the Retry-After the server names.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // The same result models.run() returns. A request that failed or was cancelled rejects here.
    const result = await handle.get();
    if (result.kind !== "json") throw new Error("expected a JSON result");
    
    console.log("image:", result.data.data[0].url);
    
    
    
    # 1. Submit. Router answers 201 with request_id, status_url, response_url and cancel_url.
    curl https://api.comfy.org/v2/models/ideogram/ideogram-v4/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"text_prompt\": \"a single red maple leaf on a plain white background, studio lighting\", \"resolution\": \"1024x1024\", \"rendering_speed\": \"DEFAULT\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/ideogram/ideogram-v4/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/ideogram/ideogram-v4/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Schema

### 

​

Input

​

enable_copyright_detection

boolean

Opt into post-generation copyright detection (Hive likeness and logo checks).

​

json_prompt

object

Structured V4 prompt. Disables Magic Prompt; consumed directly. Supply exactly one of text_prompt or json_prompt.

​

rendering_speed

string

default:"\"DEFAULT\""

The rendering speed setting that controls the trade-off between generation speed and qualityPossible values: `DEFAULT`, `TURBO`, `QUALITY`

​

resolution

string

Output resolution in WIDTHxHEIGHT. Omit to let the model pick an aspect ratio. Supported 2K values: 2048x2048, 1440x2880, 2880x1440, 1664x2496, 2496x1664, 1792x2240, 2240x1792, 1440x2560, 2560x1440, 1600x2560, 2560x1600, 1728x2304, 2304x1728, 1296x3168, 3168x1296, 1152x2944, 2944x1152, 1248x3328, 3328x1248, 1280x3072, 3072x1280.

​

text_prompt

string

Natural-language prompt. Enables Magic Prompt automatically. Supply exactly one of text_prompt or json_prompt.

Generated from the schema Router serves at `GET /v2/models/ideogram/ideogram-v4/openapi.json`, the same document it validates a call against before the request reaches the provider.

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
      "text_prompt": "a single red maple leaf on a plain white background, studio lighting",
      "resolution": "1024x1024",
      "rendering_speed": "DEFAULT"
    }
    

### 

​

Output
    
    
    {
      "response_type": "url",
      "created": "2026-08-27T21:00:00Z",
      "data": [
        {
          "url": "https://.../image.png",
          "prompt": "a single red maple leaf on a plain white background, studio lighting",
          "resolution": "1024x1024",
          "seed": 1234567890,
          "is_image_safe": true
        }
      ]
    }
    

The URL is temporary. Download the image promptly if you need to keep it.

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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/ideogram/ideogram-v4/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/ideogram/ideogram-v4/code)

[Use Ideogram V3 with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/ideogram/ideogram-v3/code)[Use P Image Ideogram with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/ideogram/p-image-ideogram/code)

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
