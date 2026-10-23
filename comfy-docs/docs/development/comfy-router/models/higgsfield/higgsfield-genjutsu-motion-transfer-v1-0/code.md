---
url: https://docs.comfy.org/development/comfy-router/models/higgsfield/higgsfield-genjutsu-motion-transfer-v1-0/code/
title: Use Higgsfield Genjutsu Motion Transfer V1.0 with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:10.231215+00:00
---

# Use Higgsfield Genjutsu Motion Transfer V1.0 with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/higgsfield/higgsfield-genjutsu-motion-transfer-v1-0/code/

## On this page

  * Quick start
  * Schema
    * Input
    * Output
  * Examples
    * Input
    * Output
  * Before you ship



Higgsfield

# Use Higgsfield Genjutsu Motion Transfer V1.0 with Comfy Router

Copy pageCopy page

Call higgsfield/higgsfield-genjutsu-motion-transfer-v1.0 through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `higgsfield/higgsfield-genjutsu-motion-transfer-v1.0`, served by Comfy Router from Higgsfield. **Input:** Video, Image, Text · **Output:** Video

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `higgsfield/higgsfield-genjutsu-motion-transfer-v1.0` **Endpoint:** `POST https://api.comfy.org/v2/models/higgsfield/higgsfield-genjutsu-motion-transfer-v1.0`

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
            "higgsfield/higgsfield-genjutsu-motion-transfer-v1.0",
            {
                "image_urls": ["https://cdn.example.com/character.jpg"],
                "prompt": "Keep the camera move and recast the dancer as the character in the reference image",
                "resolution": "720p",
                "video_url": "https://cdn.example.com/source.mp4",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("higgsfield/higgsfield-genjutsu-motion-transfer-v1.0", {
      image_urls: ["https://cdn.example.com/character.jpg"],
      prompt: "Keep the camera move and recast the dancer as the character in the reference image",
      resolution: "720p",
      video_url: "https://cdn.example.com/source.mp4",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/higgsfield/higgsfield-genjutsu-motion-transfer-v1.0 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"image_urls\": [\"https://cdn.example.com/character.jpg\"], \"prompt\": \"Keep the camera move and recast the dancer as the character in the reference image\", \"resolution\": \"720p\", \"video_url\": \"https://cdn.example.com/source.mp4\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/higgsfield/higgsfield-genjutsu-motion-transfer-v1.0/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "higgsfield/higgsfield-genjutsu-motion-transfer-v1.0",
                {
                    "image_urls": ["https://cdn.example.com/character.jpg"],
                    "prompt": "Keep the camera move and recast the dancer as the character in the reference image",
                    "resolution": "720p",
                    "video_url": "https://cdn.example.com/source.mp4",
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
    const handle = await comfy.models.submit("higgsfield/higgsfield-genjutsu-motion-transfer-v1.0", {
      image_urls: ["https://cdn.example.com/character.jpg"],
      prompt: "Keep the camera move and recast the dancer as the character in the reference image",
      resolution: "720p",
      video_url: "https://cdn.example.com/source.mp4",
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
    curl https://api.comfy.org/v2/models/higgsfield/higgsfield-genjutsu-motion-transfer-v1.0/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"image_urls\": [\"https://cdn.example.com/character.jpg\"], \"prompt\": \"Keep the camera move and recast the dancer as the character in the reference image\", \"resolution\": \"720p\", \"video_url\": \"https://cdn.example.com/source.mp4\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/higgsfield/higgsfield-genjutsu-motion-transfer-v1.0/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/higgsfield/higgsfield-genjutsu-motion-transfer-v1.0/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Schema

### 

​

Input

​

image_urls

string[]

required

URLs of 1 to 8 reference images for the cast, location and style.

​

prompt

string

Optional guidance for the recast.

​

resolution

string

default:"\"720p\""

Output resolution: 480p, 720p or 1080p.

​

video_url

string

required

URL of the source video whose motion, camera and timing are kept. Minimum 4 seconds; a longer video is trimmed to 30 seconds.

Generated from the schema Router serves at `GET /v2/models/higgsfield/higgsfield-genjutsu-motion-transfer-v1.0/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

cancel_url

string

Absolute URL used to cancel a request before processing starts.

​

error

string

Failure detail, set when `status` is `failed`.

​

request_id

string

required

Stable identifier used for polling, cancellation and support.

​

status

string

required

Current request state.Possible values: `queued`, `in_progress`, `nsfw`, `failed`, `completed`, `canceled`

​

status_url

string

Absolute URL to poll until the request reaches a terminal state.

​

video

object

One Higgsfield media output.

​

video.url

string

required

Download URL of the generated media.

## 

​

Examples

### 

​

Input
    
    
    {
      "image_urls": [
        "https://cdn.example.com/character.jpg"
      ],
      "prompt": "Keep the camera move and recast the dancer as the character in the reference image",
      "resolution": "720p",
      "video_url": "https://cdn.example.com/source.mp4"
    }
    

### 

​

Output
    
    
    {
      "cancel_url": "https://api.higgsfield.ai/requests/2e9b7c44-81d3-4f0a-a6e5-3b9d0c71f5a8/cancel",
      "request_id": "2e9b7c44-81d3-4f0a-a6e5-3b9d0c71f5a8",
      "status": "completed",
      "status_url": "https://api.higgsfield.ai/requests/2e9b7c44-81d3-4f0a-a6e5-3b9d0c71f5a8/status",
      "video": {
        "url": "https://example.invalid/higgsfield/higgsfield-genjutsu-motion-transfer-v1.0/generated.mp4"
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/higgsfield/higgsfield-genjutsu-motion-transfer-v1-0/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/higgsfield/higgsfield-genjutsu-motion-transfer-v1-0/code)

[Use Starfish with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/heygen/starfish/code)[Use Higgsfield Kling 3.4k with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/higgsfield/higgsfield-kling-3-4k/code)

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
