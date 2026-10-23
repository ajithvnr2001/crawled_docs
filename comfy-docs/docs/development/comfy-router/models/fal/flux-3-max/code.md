---
url: https://docs.comfy.org/development/comfy-router/models/fal/flux-3-max/code/
title: Use FLUX 3 Max with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-23T16:38:27.332708+00:00
---

# Use FLUX 3 Max with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/fal/flux-3-max/code/

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

# Use FLUX 3 Max with Comfy Router

Copy pageCopy page

Call fal/flux-3-max through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `fal/flux-3-max`, served by Comfy Router from fal. **Input:** Text, Image · **Output:** Video + Audio

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `fal/flux-3-max` **Endpoint:** `POST https://api.comfy.org/v2/models/fal/flux-3-max`

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
            "fal/flux-3-max",
            {
                "duration": 5,
                "prompt": "A red panda walks along a mossy log in a sunlit forest. Ambient birdsong.",
                "resolution": "720p",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("fal/flux-3-max", {
      duration: 5,
      prompt: "A red panda walks along a mossy log in a sunlit forest. Ambient birdsong.",
      resolution: "720p",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/fal/flux-3-max \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"duration\": 5, \"prompt\": \"A red panda walks along a mossy log in a sunlit forest. Ambient birdsong.\", \"resolution\": \"720p\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/fal/flux-3-max/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "fal/flux-3-max",
                {
                    "duration": 5,
                    "prompt": "A red panda walks along a mossy log in a sunlit forest. Ambient birdsong.",
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
    const handle = await comfy.models.submit("fal/flux-3-max", {
      duration: 5,
      prompt: "A red panda walks along a mossy log in a sunlit forest. Ambient birdsong.",
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
    curl https://api.comfy.org/v2/models/fal/flux-3-max/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"duration\": 5, \"prompt\": \"A red panda walks along a mossy log in a sunlit forest. Ambient birdsong.\", \"resolution\": \"720p\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/fal/flux-3-max/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/fal/flux-3-max/requests/$REQUEST_ID \
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

Aspect ratio of the generated video. auto is 16:9 for a text prompt and follows the first image otherwise.Possible values: `auto`, `21:9`, `2:1`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`

​

duration

integer

default:"5"

Duration of the generated video in seconds, 5 to 20. fal bills per second of this value.Range: `5` to `20`

​

generate_audio

boolean

default:"true"

Generate synchronized audio. The price is the same.

​

prompt

string

required

Text prompt that describes the video and its sound.

​

reasoning_level

string

default:"\"high\""

How much the model reasons about and expands the prompt before generation. high is slower. The price is the same.Possible values: `low`, `high`

​

resolution

string

default:"\"720p\""

Resolution of the generated video. 1080p costs more per second than 720p.Possible values: `720p`, `1080p`

​

seed

integer

Random seed. A random seed is selected when omitted.

Generated from the schema Router serves at `GET /v2/models/fal/flux-3-max/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

seed

integer

The seed used for the generation.

​

timings

object

Timing breakdown in seconds.

​

video

object

required

The generated video file.

​

video.content_type

string

MIME type of the video file.

​

video.duration

number

Duration of the video in seconds.

​

video.file_name

string

Name of the video file.

​

video.file_size

integer

Size of the video file in bytes.

​

video.fps

number

Frame rate of the video.

​

video.height

integer

Height of the video in pixels.

​

video.num_frames

integer

Number of frames in the video.

​

video.url

string

required

URL of the generated video.

​

video.width

integer

Width of the video in pixels.

## 

​

Examples

### 

​

Input
    
    
    {
      "duration": 5,
      "prompt": "A red panda walks along a mossy log in a sunlit forest. Ambient birdsong.",
      "resolution": "720p"
    }
    

### 

​

Output
    
    
    {
      "seed": 42,
      "video": {
        "content_type": "video/mp4",
        "duration": 5.041666666666667,
        "file_name": "video.mp4",
        "file_size": 4404019,
        "fps": 24,
        "height": 704,
        "num_frames": 121,
        "url": "https://example.invalid/fal/flux-3-max/video.mp4",
        "width": 1280
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/fal/flux-3-max/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/fal/flux-3-max/code)

[Crystal Video Upscaler](https://docs.comfy.org/development/comfy-router/models/fal/crystal-video-upscaler/code)[H3 Max Turbo](https://docs.comfy.org/development/comfy-router/models/fal/h3-max-turbo/code)
