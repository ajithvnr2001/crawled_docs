---
url: https://docs.comfy.org/development/comfy-router/models/pruna/p-video-2/code/
title: Use P Video 2 with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:34.510863+00:00
---

# Use P Video 2 with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/pruna/p-video-2/code/

## On this page

  * Quick start
  * Schema
    * Input
    * Output
  * Examples
    * Input
    * Output
  * Before you ship



Pruna

# Use P Video 2 with Comfy Router

Copy pageCopy page

Call pruna/p-video-2 through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `pruna/p-video-2`, served by Comfy Router from Pruna. **Input:** Text, Image, Audio · **Output:** Video + Audio

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `pruna/p-video-2` **Endpoint:** `POST https://api.comfy.org/v2/models/pruna/p-video-2`

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
            "pruna/p-video-2",
            {
                "input": {
                    "aspect_ratio": "16:9",
                    "draft": False,
                    "duration": 2,
                    "fps": 24,
                    "prompt": "A single red maple leaf resting on a plain white background.",
                    "resolution": "720p",
                },
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("pruna/p-video-2", {
      input: {
        aspect_ratio: "16:9",
        draft: false,
        duration: 2,
        fps: 24,
        prompt: "A single red maple leaf resting on a plain white background.",
        resolution: "720p",
      },
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/pruna/p-video-2 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input\": {\"aspect_ratio\":\"16:9\",\"draft\":false,\"duration\":2,\"fps\":24,\"prompt\":\"A single red maple leaf resting on a plain white background.\",\"resolution\":\"720p\"}}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/pruna/p-video-2/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "pruna/p-video-2",
                {
                    "input": {
                        "aspect_ratio": "16:9",
                        "draft": False,
                        "duration": 2,
                        "fps": 24,
                        "prompt": "A single red maple leaf resting on a plain white background.",
                        "resolution": "720p",
                    },
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
    const handle = await comfy.models.submit("pruna/p-video-2", {
      input: {
        aspect_ratio: "16:9",
        draft: false,
        duration: 2,
        fps: 24,
        prompt: "A single red maple leaf resting on a plain white background.",
        resolution: "720p",
      },
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
    curl https://api.comfy.org/v2/models/pruna/p-video-2/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input\": {\"aspect_ratio\":\"16:9\",\"draft\":false,\"duration\":2,\"fps\":24,\"prompt\":\"A single red maple leaf resting on a plain white background.\",\"resolution\":\"720p\"}}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/pruna/p-video-2/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/pruna/p-video-2/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Schema

### 

​

Input

​

input

object

required

P-Video-2 generation parameters. The generation is billed per second of the finished video, measured from the returned file, at a rate set by `resolution` and `draft`. The safety filter is always on; a `disable_safety_filter` value in the request is ignored.

​

input.aspect_ratio

string

default:"\"16:9\""

Aspect ratio: 16:9, 9:16, 4:3, 3:4, 3:2, 2:3 or 1:1. Ignored when `image` is set.

​

input.audio

string

Input audio URI to condition the generation (flac, mp3 or wav). The output length follows the audio.

​

input.draft

boolean

default:"false"

Faster, lower-quality preview, billed at the draft rate.

​

input.duration

integer

Duration of the generated video in seconds (1-20). When omitted the model chooses the length from the prompt, up to 20 seconds. Ignored when `audio` is set.Range: `1` to `20`

​

input.fps

integer

default:"24"

Frame rate: 24 or 48.

​

input.image

string

Input image URI for image-to-video (jpg, jpeg, png or webp).

​

input.last_frame_image

string

Reference image URI for the last frame.

​

input.prompt

string

required

Text prompt for video generation.

​

input.prompt_upsampling

boolean

default:"true"

Rewrite the prompt before generation. Disable it when a `seed` must reproduce a result.

​

input.resolution

string

default:"\"720p\""

Output resolution: 720p or 1080p.

​

input.save_audio

boolean

default:"true"

Save the video with audio.

​

input.seed

integer

Random seed for reproducible generation. Random when omitted.

Generated from the schema Router serves at `GET /v2/models/pruna/p-video-2/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

error

string

Error message. Present when status is failed.

​

generation_url

string

URL of the finished video. Present when status is succeeded.

​

message

string

Human-readable progress message.

​

status

string

Prediction status: starting, processing, succeeded, failed or canceled.

## 

​

Examples

### 

​

Input
    
    
    {
      "input": {
        "aspect_ratio": "16:9",
        "draft": false,
        "duration": 2,
        "fps": 24,
        "prompt": "A single red maple leaf resting on a plain white background.",
        "resolution": "720p"
      }
    }
    

### 

​

Output
    
    
    {
      "generation_url": "https://example.invalid/pruna/p-video-2/output.mp4",
      "status": "succeeded"
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/pruna/p-video-2/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/pruna/p-video-2/code)

[Use Pika 2.5 Text To Video with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/pika/pika-2-5-text-to-video/code)[Use Qwen Image 3.0 Pro with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/qwen/qwen-image-3-0-pro/code)

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
