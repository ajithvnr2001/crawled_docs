---
url: https://docs.comfy.org/development/comfy-router/models/pruna/p-video-upscale/code/
title: Use P Video Upscale with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-27T17:19:26.416244+00:00
---

# Use P Video Upscale with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/pruna/p-video-upscale/code/

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



Pruna

# Use P Video Upscale with Comfy Router

Copy pageCopy page

Call pruna/p-video-upscale through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `pruna/p-video-upscale`, served by Comfy Router from Pruna. **Input:** Video · **Output:** Video + Audio

## Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `pruna/p-video-upscale` **Endpoint:** `POST https://api.comfy.org/v2/models/pruna/p-video-upscale`

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
            "pruna/p-video-upscale",
            {
                "input": {
                    "target": "1080p",
                    "video": "https://example.com/source.mp4",
                },
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("pruna/p-video-upscale", {
      input: {
        target: "1080p",
        video: "https://example.com/source.mp4",
      },
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/pruna/p-video-upscale \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input\": {\"target\":\"1080p\",\"video\":\"https://example.com/source.mp4\"}}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/pruna/p-video-upscale/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "pruna/p-video-upscale",
                {
                    "input": {
                        "target": "1080p",
                        "video": "https://example.com/source.mp4",
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
    const handle = await comfy.models.submit("pruna/p-video-upscale", {
      input: {
        target: "1080p",
        video: "https://example.com/source.mp4",
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
    curl https://api.comfy.org/v2/models/pruna/p-video-upscale/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input\": {\"target\":\"1080p\",\"video\":\"https://example.com/source.mp4\"}}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/pruna/p-video-upscale/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/pruna/p-video-upscale/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## Schema

### Input

input

object

required

P-Video-Upscale parameters. The job is billed per second of the returned video, measured from the returned file and rounded up to a whole second. The rate is set by `target` and by whether the output frame rate is above 30 fps. When `fps` is omitted, the output keeps the frame rate of `video`, so that rate decides the tier. A `turbo` job bills at the turbo rate for its `target`, at any frame rate. The safety filter is always on; an `enable_safety_filter` value in the request is ignored.

input.fps

integer

Output frame rate (16-60). A rate above the source rate is interpolated. When omitted, the output keeps the source rate.Range: `16` to `60`

input.target

string

default:"\"1080p\""

Output resolution preset: 720p, 1080p, 2k or 4k. The preset sets the pixel area; a video that is not 16:9 keeps its aspect ratio. A video already larger than the target is not downscaled.Possible values: `720p`, `1080p`, `2k`, `4k`

input.turbo

boolean

default:"false"

Faster job with slightly lower quality, billed at the turbo rate (about a third of the standard rate) at any frame rate.

input.video

string

required

Input video URI, at most 512 MiB. It must be a publicly readable http(s) URL when `fps` is omitted, because its frame rate is read before the job is sent.

Generated from the schema Router serves at `GET /v2/models/pruna/p-video-upscale/openapi.json`, the same document it validates a call against before the request reaches the provider.

### Output

error

string

Error message. Present when status is failed.

generation_url

string

URL of the finished video. Present when status is succeeded.

message

string

Human-readable progress message.

moderation

object

Pruna’s safety-checker verdict. Present on a failed status when content moderation blocked the prediction.

moderation.blocked

boolean

Whether the safety checker blocked the prediction.

moderation.can_disable

boolean

Whether the block comes from a safety filter the request could disable.

moderation.categories

string[]

Content-policy categories that triggered the block, for example sexual.

moderation.message

string

Human-readable summary of the block.

moderation.phase

string

What was screened: input (the submitted request) or output (the generated video).

moderation.reason

string

Human-readable reason for the block.

status

string

Prediction status: starting, processing, succeeded, failed or canceled.

## Examples

### Input
    
    
    {
      "input": {
        "target": "1080p",
        "video": "https://example.com/source.mp4"
      }
    }
    

### Output
    
    
    {
      "generation_url": "https://example.invalid/pruna/p-video-2/output.mp4",
      "status": "succeeded"
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/pruna/p-video-upscale/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/pruna/p-video-upscale/code)

[P Video 2](https://docs.comfy.org/development/comfy-router/models/pruna/p-video-2/code)[Arrow 2 Telos](https://docs.comfy.org/development/comfy-router/models/quiver/arrow-2-telos/code)
