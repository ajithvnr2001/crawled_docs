---
url: https://docs.comfy.org/development/comfy-router/models/pika/pika-2-5-text-to-video/code/
title: Use Pika 2.5 Text To Video with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:34.243580+00:00
---

# Use Pika 2.5 Text To Video with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/pika/pika-2-5-text-to-video/code/

## On this page

  * Quick start
  * Schema
    * Input
    * Output
  * Examples
    * Input
    * Output
  * Before you ship



Pika

# Use Pika 2.5 Text To Video with Comfy Router

Copy pageCopy page

Call pika/pika-2.5-text-to-video through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `pika/pika-2.5-text-to-video`, served by Comfy Router from Pika. **Input:** Text · **Output:** Video

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `pika/pika-2.5-text-to-video` **Endpoint:** `POST https://api.comfy.org/v2/models/pika/pika-2.5-text-to-video`

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
            "pika/pika-2.5-text-to-video",
            {
                "duration_s": 5,
                "prompt": "A paper boat drifting down a rain-soaked city street at dusk",
                "resolution": "720p",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("pika/pika-2.5-text-to-video", {
      duration_s: 5,
      prompt: "A paper boat drifting down a rain-soaked city street at dusk",
      resolution: "720p",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/pika/pika-2.5-text-to-video \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"duration_s\": 5, \"prompt\": \"A paper boat drifting down a rain-soaked city street at dusk\", \"resolution\": \"720p\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/pika/pika-2.5-text-to-video/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "pika/pika-2.5-text-to-video",
                {
                    "duration_s": 5,
                    "prompt": "A paper boat drifting down a rain-soaked city street at dusk",
                    "resolution": "720p",
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
    const handle = await comfy.models.submit("pika/pika-2.5-text-to-video", {
      duration_s: 5,
      prompt: "A paper boat drifting down a rain-soaked city street at dusk",
      resolution: "720p",
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
    curl https://api.comfy.org/v2/models/pika/pika-2.5-text-to-video/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"duration_s\": 5, \"prompt\": \"A paper boat drifting down a rain-soaked city street at dusk\", \"resolution\": \"720p\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/pika/pika-2.5-text-to-video/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/pika/pika-2.5-text-to-video/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Schema

### 

​

Input

​

duration_s

integer

default:"5"

Video length in seconds. Text-to-video produces five-second clips only.Possible values: `5`

​

negative_prompt

string

Text describing what to avoid in the video.

​

prompt

string

required

Text prompt describing the video to generate.

​

resolution

string

default:"\"1080p\""

Output resolution.Possible values: `720p`, `1080p`

​

seed

integer

Seed for reproducible generation. Omit it (or send null) for a random seed.

Generated from the schema Router serves at `GET /v2/models/pika/pika-2.5-text-to-video/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

error

object

Pika’s structured failure record, set on a `failed` job. Router answers a failed job with its own error response, so a body Router returns does not carry it; it is declared because it is part of Pika’s job document.

​

error.code

string

required

Possible values: `invalid_input`, `content_moderation`, `provider_error`, `provider_timeout`, `provider_unavailable`, `rate_limited`, `insufficient_balance`, `membership_required`, `cycle_limit_exceeded`, `admission_suspended`, `usage_limit_exceeded`, `timed_out`, `internal`

​

error.message

string

required

​

id

string

required

Pika’s job id.

​

model_id

string

The Pika catalog entry the job ran.

​

output

object

The finished job’s media, set when `status` is `completed`. `media_type` says which field carries it: `image` fills `images`, `video` fills `video`, and `videos` fills `videos`.

​

output.images

object[]

Generated images, for an image model.

​

output.images[].content_type

string

MIME type of the file.

​

output.images[].height

integer

Height in pixels.

​

output.images[].url

string

Download URL of the generated file.

​

output.images[].width

integer

Width in pixels.

​

output.media_type

string

Possible values: `image`, `video`, `videos`

​

output.seed

integer

The seed the video job actually used, when reported.

​

output.video

object

One generated media file.

​

output.video.content_type

string

MIME type of the file.

​

output.video.height

integer

Height in pixels.

​

output.video.url

string

Download URL of the generated file.

​

output.video.width

integer

Width in pixels.

​

output.videos

object[]

Generated videos, for a multi-video delivery.

​

output.videos[].content_type

string

MIME type of the file.

​

output.videos[].height

integer

Height in pixels.

​

output.videos[].url

string

Download URL of the generated file.

​

output.videos[].width

integer

Width in pixels.

​

runtime_s

number

Seconds the generation took, from dispatch to terminal. Best-effort; may be null.

​

status

string

required

Lifecycle state. A body Router returns always reads `completed`; a `failed` job is answered with Router’s error response instead.Possible values: `queued`, `running`, `completed`, `failed`

​

usage

object

Provider-reported units for the job. Keys are sparse; only the units the job reports are present.

## 

​

Examples

### 

​

Input
    
    
    {
      "duration_s": 5,
      "prompt": "A paper boat drifting down a rain-soaked city street at dusk",
      "resolution": "720p"
    }
    

### 

​

Output
    
    
    {
      "id": "6f1c2a9e-3b47-4d8a-9e21-7c5b0f4d8a13",
      "model_id": "pika/pika-2.5/text-to-video",
      "output": {
        "media_type": "video",
        "seed": 42,
        "video": {
          "content_type": "video/mp4",
          "height": 720,
          "url": "https://example.invalid/pika/pika-2.5-text-to-video/generated.mp4",
          "width": 1280
        }
      },
      "status": "completed"
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/pika/pika-2-5-text-to-video/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/pika/pika-2-5-text-to-video/code)

[Use Pika 2.5 Image To Video with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/pika/pika-2-5-image-to-video/code)[Use P Video 2 with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/pruna/p-video-2/code)

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
