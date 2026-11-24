---
url: https://docs.comfy.org/development/comfy-router/models/pruna/p-video-2-pro-avatar/code/
title: Use P Video 2 Pro Avatar with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-24T18:44:23.161671+00:00
---

# Use P Video 2 Pro Avatar with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/pruna/p-video-2-pro-avatar/code/

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

# Use P Video 2 Pro Avatar with Comfy Router

Copy pageCopy page

Call pruna/p-video-2-pro-avatar through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `pruna/p-video-2-pro-avatar`, served by Comfy Router from Pruna. **Input:** Image, Audio, Text · **Output:** Video + Audio

## Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `pruna/p-video-2-pro-avatar` **Endpoint:** `POST https://api.comfy.org/v2/models/pruna/p-video-2-pro-avatar`

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
            "pruna/p-video-2-pro-avatar",
            {
                "input": {
                    "audio": "https://example.com/speech.mp3",
                    "image": "https://example.com/portrait.png",
                    "resolution": "768p",
                },
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("pruna/p-video-2-pro-avatar", {
      input: {
        audio: "https://example.com/speech.mp3",
        image: "https://example.com/portrait.png",
        resolution: "768p",
      },
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/pruna/p-video-2-pro-avatar \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input\": {\"audio\":\"https://example.com/speech.mp3\",\"image\":\"https://example.com/portrait.png\",\"resolution\":\"768p\"}}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/pruna/p-video-2-pro-avatar/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "pruna/p-video-2-pro-avatar",
                {
                    "input": {
                        "audio": "https://example.com/speech.mp3",
                        "image": "https://example.com/portrait.png",
                        "resolution": "768p",
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
    const handle = await comfy.models.submit("pruna/p-video-2-pro-avatar", {
      input: {
        audio: "https://example.com/speech.mp3",
        image: "https://example.com/portrait.png",
        resolution: "768p",
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
    curl https://api.comfy.org/v2/models/pruna/p-video-2-pro-avatar/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input\": {\"audio\":\"https://example.com/speech.mp3\",\"image\":\"https://example.com/portrait.png\",\"resolution\":\"768p\"}}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/pruna/p-video-2-pro-avatar/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/pruna/p-video-2-pro-avatar/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## Schema

### Input

input

object

required

P-Video-2-Pro Avatar parameters. The job is billed per second of the returned video, measured from the returned file and rounded down to a whole second, at the rate for `resolution`. The safety filter is always on; an `enable_safety_filter` value in the request is ignored.

input.audio

string

Speech audio URI, 1 second to 3 minutes, at most 64 MiB. It sets the output length. When set, `voice_script` is ignored.

input.image

string

required

Portrait URI, used as the first frame. jpg, png or webp, at most 20 MiB. It sets the aspect ratio.

input.prompt

string

default:"\"The person is talking.\""

What the video shows.

input.prompt_upsampling

boolean

default:"true"

Adds the scene’s motion from the portrait to `prompt`.

input.resolution

string

default:"\"768p\""

Output resolution: 480p, 768p, 1080p, 2k or 4k. 1080p, 2k and 4k upscale the 768p video.

input.seed

integer

Seed for reproducible generation.

input.voice

string

Text-to-speech voice for `voice_script`, for example `Zephyr (Female)`.

input.voice_language

string

Text-to-speech language for `voice_script`, for example `English (US)`.

input.voice_prompt

string

Delivery instructions for `voice_script` (tone, pacing, accent). Not spoken.

input.voice_script

string

Words to speak with text-to-speech when `audio` is not set.

Generated from the schema Router serves at `GET /v2/models/pruna/p-video-2-pro-avatar/openapi.json`, the same document it validates a call against before the request reaches the provider.

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
        "audio": "https://example.com/speech.mp3",
        "image": "https://example.com/portrait.png",
        "resolution": "768p"
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/pruna/p-video-2-pro-avatar/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/pruna/p-video-2-pro-avatar/code)

[V6](https://docs.comfy.org/development/comfy-router/models/pixverse/v6/code)[P Video 2 Pro Reference](https://docs.comfy.org/development/comfy-router/models/pruna/p-video-2-pro-reference/code)
