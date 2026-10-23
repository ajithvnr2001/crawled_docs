---
url: https://docs.comfy.org/development/comfy-router/models/xai/grok-imagine-video-1-5-lite/code/
title: Use Grok Imagine Video 1.5 Lite with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:51.846684+00:00
---

# Use Grok Imagine Video 1.5 Lite with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/xai/grok-imagine-video-1-5-lite/code/

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

# Use Grok Imagine Video 1.5 Lite with Comfy Router

Copy pageCopy page

Call xai/grok-imagine-video-1.5-lite through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `xai/grok-imagine-video-1.5-lite`, served by Comfy Router from xAI. **Input:** Text, Image · **Output:** Video

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `xai/grok-imagine-video-1.5-lite` **Endpoint:** `POST https://api.comfy.org/v2/models/xai/grok-imagine-video-1.5-lite`

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
            "xai/grok-imagine-video-1.5-lite",
            {
                "duration": 4,
                "prompt": "a single red maple leaf falling onto still water, slow motion",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("xai/grok-imagine-video-1.5-lite", {
      duration: 4,
      prompt: "a single red maple leaf falling onto still water, slow motion",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/xai/grok-imagine-video-1.5-lite \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"duration\": 4, \"prompt\": \"a single red maple leaf falling onto still water, slow motion\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/xai/grok-imagine-video-1.5-lite/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "xai/grok-imagine-video-1.5-lite",
                {
                    "duration": 4,
                    "prompt": "a single red maple leaf falling onto still water, slow motion",
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
    const handle = await comfy.models.submit("xai/grok-imagine-video-1.5-lite", {
      duration: 4,
      prompt: "a single red maple leaf falling onto still water, slow motion",
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
    curl https://api.comfy.org/v2/models/xai/grok-imagine-video-1.5-lite/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"duration\": 4, \"prompt\": \"a single red maple leaf falling onto still water, slow motion\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/xai/grok-imagine-video-1.5-lite/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/xai/grok-imagine-video-1.5-lite/requests/$REQUEST_ID \
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

default:"\"16:9\""

Aspect ratio of the generated videoPossible values: `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `3:2`, `2:3`

​

duration

integer

default:"8"

Video duration in seconds. Range [1, 15]. Default 8.Range: `1` to `15`

​

image

object

Input image object for xAI endpoints

​

image.type

string

Type of the image inputPossible values: `image_url`

​

image.url

string

required

URL of the input image (public URL or base64-encoded data URI)

​

model

string

Model to be used. Supported: grok-imagine-video (default), grok-imagine-video-1.5-preview, grok-imagine-video-1.5, grok-imagine-video-1.5-lite. The deprecated grok-imagine-video-beta id is aliased to grok-imagine-video.

​

output

object

Optional output destination for generated video

​

prompt

string

required

Prompt for video generation. Maximum 4,096 characters.

​

reference_images

object[]

One or more reference images to guide the video generation (reference-to-video mode). Mutually exclusive with image. Router forwards application/json only and neither this object nor XAIImageObject accepts a file_id, so file-backed image inputs are not supported on this route.

​

reference_images[].url

string

required

URL of the reference image. Supports HTTPS URLs (public) or base64-encoded data URLs (e.g., data:image/jpeg;base64,…).

​

resolution

string

Resolution of the output video

​

size

string

Size of the output video

​

user

string

A unique identifier representing your end-user

Generated from the schema Router serves at `GET /v2/models/xai/grok-imagine-video-1.5-lite/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

block_reason

string

Never carries a reason on this document: a non-empty block reason is an input-moderation refusal, which Router answers as a Comfy Router error rather than with this body. Absent, null or empty here.

​

model

string

The model used to generate the video

​

status

string

Absent or `done` on this document. `pending` is the body of a poll Router has not finished and is never returned as a `200`; Router accepts a missing status when `video.url` is populated, so a caller must not require it.Possible values: `done`

​

usage

object

Usage information for the video generation request

​

usage.cost_in_usd_ticks

integer

The cost of this request expressed in USD ticks. One USD cent equals 100,000,000 ticks, so one US dollar equals 10,000,000,000 ticks.

​

video

object

required

The finished generation. Required here, unlike on the poll document: a terminal result with no `video.url` is answered as a Comfy Router error, so a `200` always carries it.

​

video.duration

integer

Duration of the generated video in seconds

​

video.respect_moderation

boolean

Whether the video generated by the model respects moderation rules

​

video.url

string

required

Non-empty on this document. Router reports success only when this leaf is populated; it is the re-hosted Comfy-signed URL described above, or xAI’s own short-lived URL when the re-host could not be performed.

## 

​

Examples

### 

​

Input
    
    
    {
      "duration": 4,
      "prompt": "a single red maple leaf falling onto still water, slow motion"
    }
    

### 

​

Output
    
    
    {
      "model": "grok-imagine-video-1.5-lite",
      "status": "done",
      "usage": {
        "cost_in_usd_ticks": 3500000000
      },
      "video": {
        "duration": 4,
        "respect_moderation": true,
        "url": "https://example.invalid/xai/grok-imagine-video/generated.mp4"
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/xai/grok-imagine-video-1-5-lite/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/xai/grok-imagine-video-1-5-lite/code)

[Use Grok Imagine Image with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/xai/grok-imagine-image/code)[Use Grok Imagine Video 1.5 Preview with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/xai/grok-imagine-video-1-5-preview/code)

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
