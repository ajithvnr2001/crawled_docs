---
url: https://docs.comfy.org/development/comfy-router/models/viggle/video-remix/code/
title: Use Video Remix with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-24T18:44:25.510358+00:00
---

# Use Video Remix with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/viggle/video-remix/code/

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



Viggle

# Use Video Remix with Comfy Router

Copy pageCopy page

Call viggle/video-remix through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `viggle/video-remix`, served by Comfy Router from Viggle. **Input:** Image, Video · **Output:** Video

## Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `viggle/video-remix` **Endpoint:** `POST https://api.comfy.org/v2/models/viggle/video-remix`

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
            "viggle/video-remix",
            {
                "background_mode": "original",
                "image_url": "https://example.invalid/viggle/character.png",
                "motion_video_url": "https://example.invalid/viggle/dance.mp4",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("viggle/video-remix", {
      background_mode: "original",
      image_url: "https://example.invalid/viggle/character.png",
      motion_video_url: "https://example.invalid/viggle/dance.mp4",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/viggle/video-remix \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"background_mode\": \"original\", \"image_url\": \"https://example.invalid/viggle/character.png\", \"motion_video_url\": \"https://example.invalid/viggle/dance.mp4\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/viggle/video-remix/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "viggle/video-remix",
                {
                    "background_mode": "original",
                    "image_url": "https://example.invalid/viggle/character.png",
                    "motion_video_url": "https://example.invalid/viggle/dance.mp4",
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
    const handle = await comfy.models.submit("viggle/video-remix", {
      background_mode: "original",
      image_url: "https://example.invalid/viggle/character.png",
      motion_video_url: "https://example.invalid/viggle/dance.mp4",
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
    curl https://api.comfy.org/v2/models/viggle/video-remix/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"background_mode\": \"original\", \"image_url\": \"https://example.invalid/viggle/character.png\", \"motion_video_url\": \"https://example.invalid/viggle/dance.mp4\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/viggle/video-remix/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/viggle/video-remix/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## Schema

### Input

background_mode

string

original (the default), solid or transparent. `transparent` adds an alpha matte video, `alpha_url`.

bg_color

string

Solid background colour as `R,G,B`. Only with `background_mode=solid`.

image_url

string

required

Public http(s) URL of the character image.

model

string

Optional render model: V3 or V4.

motion_video_url

string

required

Public http(s) URL of the driving video, up to 100 MiB.

Generated from the schema Router serves at `GET /v2/models/viggle/video-remix/openapi.json`, the same document it validates a call against before the request reaches the provider.

### Output

alpha_url

string

The alpha matte video of a transparent render, once ready.

completed_at

string

created_at

string

credits_used

number

Viggle credits the job is charged, set once it is ready.Format: `double`

duration_seconds

number

Length in seconds the charge is based on, set once the job is ready.Format: `double`

error

object

Viggle’s error object, set when the job failed.

error.code

string

error.message

string

error.request_id

string

error.retryable

boolean

id

string

Render id (`render_` prefix). Poll it on the videos route.

progress

integer

Progress from 0 to 100, when known.

stage

string

Coarse progress stage while the render runs.

status

string

Status: queued, processing, ready, failed or cancelled.

video_url

string

The finished video, once ready. The URL lasts one hour.

## Examples

### Input
    
    
    {
      "background_mode": "original",
      "image_url": "https://example.invalid/viggle/character.png",
      "motion_video_url": "https://example.invalid/viggle/dance.mp4"
    }
    

### Output
    
    
    {
      "alpha_url": null,
      "credits_used": 5.04,
      "duration_seconds": 5.04,
      "error": null,
      "id": "render_job_38d67fcfb717e8d4",
      "progress": 100,
      "status": "ready",
      "video_url": "https://example.invalid/viggle/output.mp4"
    }
    

## Before you ship

The SDKs create an `Idempotency-Key` and reuse it for automatic retries. For manual retries, reuse the original key. Router can hold the connection for up to 10 minutes. When a request fails, Router sends an `X-Comfy-Error-Type` response header explaining why. A `422` means Router rejected the input before calling the provider, and a `413` means the request body was larger than Router accepts. Download generated assets promptly because [result URLs can expire](https://docs.comfy.org/development/comfy-router/reference#result-assets). Any size limit named in a field description above is the provider’s own bound on that field, quoted from the provider’s specification. Router applies a separate cap to the whole request body, which base64-encoded media counts against: see [request body size](https://docs.comfy.org/development/comfy-router/limitations#request-bodies-are-capped). This page documents one partner model called through Comfy Router. The same `comfy-sdk` / `@comfyorg/sdk` package also ships a second client, for running a whole ComfyUI workflow graph on Comfy Cloud: `Comfy(api_key=...)` / `new Comfy({ apiKey })`, with `client.workflows`, `client.assets` and `client.jobs`. See [Comfy SDKs](https://docs.comfy.org/development/api-development/sdks).

## Headers

Authentication, idempotency, request IDs, error buckets, retry pacing, spend limits.

## Using the Router API

Model discovery, validation errors, retries, and billing.

## Limitations

What Router does not do today, and what to use instead.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/viggle/video-remix/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/viggle/video-remix/code)

[Text To Motion](https://docs.comfy.org/development/comfy-router/models/viggle/text-to-motion/code)[HappyHorse 1.0 I2V](https://docs.comfy.org/development/comfy-router/models/wan/happyhorse-1-0-i2v/code)
