---
url: https://docs.comfy.org/development/comfy-router/models/pika/pika-h3-flex-reference-to-video/code/
title: Use Pika H3 Flex Reference To Video with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-09T17:17:28.056601+00:00
---

# Use Pika H3 Flex Reference To Video with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/pika/pika-h3-flex-reference-to-video/code/

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



Pika

# Use Pika H3 Flex Reference To Video with Comfy Router

Copy pageCopy page

Call pika/pika-h3-flex-reference-to-video through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `pika/pika-h3-flex-reference-to-video`, served by Comfy Router from Pika. **Input:** Text, Image, Video, Audio · **Output:** Video + Audio

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `pika/pika-h3-flex-reference-to-video` **Endpoint:** `POST https://api.comfy.org/v2/models/pika/pika-h3-flex-reference-to-video`

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
            "pika/pika-h3-flex-reference-to-video",
            {
                "duration": 5,
                "prompt": "The woman from the first image walks through the market from the video, humming the tune from the audio",
                "references": [
                    {
                        "type": "image",
                        "url": "https://example.invalid/pika/character.png",
                    },
                ],
                "resolution": "480p",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("pika/pika-h3-flex-reference-to-video", {
      duration: 5,
      prompt: "The woman from the first image walks through the market from the video, humming the tune from the audio",
      references: [
        {
          type: "image",
          url: "https://example.invalid/pika/character.png",
        },
      ],
      resolution: "480p",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/pika/pika-h3-flex-reference-to-video \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"duration\": 5, \"prompt\": \"The woman from the first image walks through the market from the video, humming the tune from the audio\", \"references\": [{\"type\":\"image\",\"url\":\"https://example.invalid/pika/character.png\"}], \"resolution\": \"480p\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/pika/pika-h3-flex-reference-to-video/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "pika/pika-h3-flex-reference-to-video",
                {
                    "duration": 5,
                    "prompt": "The woman from the first image walks through the market from the video, humming the tune from the audio",
                    "references": [
                        {
                            "type": "image",
                            "url": "https://example.invalid/pika/character.png",
                        },
                    ],
                    "resolution": "480p",
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
    const handle = await comfy.models.submit("pika/pika-h3-flex-reference-to-video", {
      duration: 5,
      prompt: "The woman from the first image walks through the market from the video, humming the tune from the audio",
      references: [
        {
          type: "image",
          url: "https://example.invalid/pika/character.png",
        },
      ],
      resolution: "480p",
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
    curl https://api.comfy.org/v2/models/pika/pika-h3-flex-reference-to-video/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"duration\": 5, \"prompt\": \"The woman from the first image walks through the market from the video, humming the tune from the audio\", \"references\": [{\"type\":\"image\",\"url\":\"https://example.invalid/pika/character.png\"}], \"resolution\": \"480p\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/pika/pika-h3-flex-reference-to-video/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/pika/pika-h3-flex-reference-to-video/requests/$REQUEST_ID \
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

Output aspect ratio. `auto` picks one from the prompt and the media inputs. Omit it to let Pika choose: `auto` when `rewrite` is on, else the first media input’s ratio, else 16:9.Possible values: `auto`, `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16`, `9:21`

​

channel_mode

string

default:"\"mono\""

Audio stems only. `mono` downmixes before separation; `stereo` keeps both channels. The video’s audio does not change.Possible values: `stereo`, `mono`

​

duration

integer

default:"5"

Video length in whole seconds, 5 to 15.Range: `5` to `15`

​

output_mode

string

default:"\"video\""

`video` returns the video only. `audio-stems` also returns Dialogue, Music and Effect WAV stems in `output.stems`, and adds Pika’s per-second stem separation charge.Possible values: `video`, `audio-stems`

​

prompt

string

required

Text prompt describing the video and its audio.

​

references

object[]

required

Ordered reference media: up to 9 images, 3 videos and 3 audio files, 12 in total. At least one image or video is required. Each file is at most 24 MiB. Video and audio clips are 2 to 15 seconds, and at most 15 seconds in total per type. Pika bills reference video seconds in addition to output seconds.

​

references[].type

string

required

The media kind of the file.Possible values: `image`, `video`, `audio`

​

references[].url

string

required

URL of the reference file. Images are PNG, JPEG or WebP.

​

resolution

string

default:"\"768p\""

Output resolution. 480p and 768p are native. 1080p, 2k and 4k generate at 768p and then upscale, keeping the audio and frame rate.Possible values: `480p`, `768p`, `1080p`, `2k`, `4k`

​

rewrite

boolean

default:"true"

Improve the prompt before generation. Set it to false to use the prompt as written.

​

seed

integer

default:"0"

Seed for the video, 0 or more.Range: `0` to `…`Format: `int64`

Generated from the schema Router serves at `GET /v2/models/pika/pika-h3-flex-reference-to-video/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

error

object

Set on a `failed` job.

​

error.code

string

Machine-readable failure code, such as invalid_input, content_moderation or provider_error.

​

error.message

string

Diagnostic text.

​

id

string

Job id used to poll for status.

​

model_id

string

The Pika catalog entry the job ran.

​

output

object

The finished job’s media, set when `status` is `completed`.

​

output.audio

object

One generated media file.

​

output.audio.content_type

string

MIME type of the file.

​

output.audio.url

string

Download URL of the generated file.

​

output.media_type

string

Which field carries the file: video or audio.

​

output.video

object

One generated media file.

​

output.video.content_type

string

MIME type of the file.

​

output.video.url

string

Download URL of the generated file.

​

status

string

Job status: queued, running, completed or failed.

​

usage

object

Units Pika reported for the job.

## 

​

Examples

### 

​

Input
    
    
    {
      "duration": 5,
      "prompt": "The woman from the first image walks through the market from the video, humming the tune from the audio",
      "references": [
        {
          "type": "image",
          "url": "https://example.invalid/pika/character.png"
        }
      ],
      "resolution": "480p"
    }
    

### 

​

Output
    
    
    {
      "id": "media_8f3a2c91-5b7d-4e0a-9c26-31d4f2a8e6b0",
      "output": {
        "media_type": "video",
        "video": {
          "content_type": "video/mp4",
          "url": "https://example.invalid/pika/video.mp4"
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/pika/pika-h3-flex-reference-to-video/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/pika/pika-h3-flex-reference-to-video/code)

[Pika H3 Flex Image To Video](https://docs.comfy.org/development/comfy-router/models/pika/pika-h3-flex-image-to-video/code)[Pika H3 Flex Text To Video](https://docs.comfy.org/development/comfy-router/models/pika/pika-h3-flex-text-to-video/code)
