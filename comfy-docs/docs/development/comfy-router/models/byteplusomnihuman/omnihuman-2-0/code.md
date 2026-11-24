---
url: https://docs.comfy.org/development/comfy-router/models/byteplusomnihuman/omnihuman-2-0/code/
title: Use Omnihuman 2.0 with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-24T18:44:22.248873+00:00
---

# Use Omnihuman 2.0 with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/byteplusomnihuman/omnihuman-2-0/code/

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



Byteplusomnihuman

# Use Omnihuman 2.0 with Comfy Router

Copy pageCopy page

Call byteplusomnihuman/omnihuman-2.0 through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `byteplusomnihuman/omnihuman-2.0`, served by Comfy Router from Byteplusomnihuman. **Input:** Image, Audio, Text · **Output:** Video + Audio

## Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `byteplusomnihuman/omnihuman-2.0` **Endpoint:** `POST https://api.comfy.org/v2/models/byteplusomnihuman/omnihuman-2.0`

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
            "byteplusomnihuman/omnihuman-2.0",
            {
                "audio_url": "https://example.com/speech.mp3",
                "enable_watermark": False,
                "image_urls": ["https://example.com/portrait.jpg"],
                "prompt": "The person speaks calmly to the camera.",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("byteplusomnihuman/omnihuman-2.0", {
      audio_url: "https://example.com/speech.mp3",
      enable_watermark: false,
      image_urls: ["https://example.com/portrait.jpg"],
      prompt: "The person speaks calmly to the camera.",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/byteplusomnihuman/omnihuman-2.0 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"audio_url\": \"https://example.com/speech.mp3\", \"enable_watermark\": false, \"image_urls\": [\"https://example.com/portrait.jpg\"], \"prompt\": \"The person speaks calmly to the camera.\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/byteplusomnihuman/omnihuman-2.0/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "byteplusomnihuman/omnihuman-2.0",
                {
                    "audio_url": "https://example.com/speech.mp3",
                    "enable_watermark": False,
                    "image_urls": ["https://example.com/portrait.jpg"],
                    "prompt": "The person speaks calmly to the camera.",
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
    const handle = await comfy.models.submit("byteplusomnihuman/omnihuman-2.0", {
      audio_url: "https://example.com/speech.mp3",
      enable_watermark: false,
      image_urls: ["https://example.com/portrait.jpg"],
      prompt: "The person speaks calmly to the camera.",
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
    curl https://api.comfy.org/v2/models/byteplusomnihuman/omnihuman-2.0/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"audio_url\": \"https://example.com/speech.mp3\", \"enable_watermark\": false, \"image_urls\": [\"https://example.com/portrait.jpg\"], \"prompt\": \"The person speaks calmly to the camera.\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/byteplusomnihuman/omnihuman-2.0/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/byteplusomnihuman/omnihuman-2.0/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## Schema

### Input

audio_url

string

required

Public HTTP or HTTPS URL of the speech audio. WAV or MP3, under 15 MB, 4 to 300 seconds. The output video is as long as this audio.

enable_watermark

boolean

Whether BytePlus adds a watermark to the video. BytePlus defaults to true when this is omitted.

image_urls

string[]

required

Exactly one public HTTP or HTTPS URL of an image of a person. JPEG, PNG, WEBP, BMP, TIFF, GIF, HEIC or HEIF; under 30 MB; aspect ratio (width/height) 0.4 to 2.5; 300 to 6000 px per side.

prompt

string

Optional text that controls the scene, movement and camera. Chinese, English, Japanese, Korean, Spanish (Mexican) or Indonesian.

Generated from the schema Router serves at `GET /v2/models/byteplusomnihuman/omnihuman-2.0/openapi.json`, the same document it validates a call against before the request reaches the provider.

### Output

code

integer

10000 on success. Any other value is an error.

data

object

data.resp_data

string

Extra result data from BytePlus as a JSON string. It can be empty; the output length is not reported here.

data.status

string

The task state. in_queue and generating are in progress; done is finished; not_found, expired, failed and canceled are terminal failures.

data.video_url

string

URL of the output MP4 when status is done, valid for one hour.

message

string

request_id

string

time_elapsed

string

## Examples

### Input
    
    
    {
      "audio_url": "https://example.com/speech.mp3",
      "enable_watermark": false,
      "image_urls": [
        "https://example.com/portrait.jpg"
      ],
      "prompt": "The person speaks calmly to the camera."
    }
    

### Output
    
    
    {
      "code": 10000,
      "data": {
        "resp_data": "",
        "status": "done",
        "video_url": "https://example.invalid/omnihuman/output.mp4"
      },
      "message": "Success"
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/byteplusomnihuman/omnihuman-2-0/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/byteplusomnihuman/omnihuman-2-0/code)

[Seedream 5.5 261028](https://docs.comfy.org/development/comfy-router/models/byteplus/seedream-5-5-261028/code)[Eleven Multilingual V2](https://docs.comfy.org/development/comfy-router/models/elevenlabs/eleven-multilingual-v2/code)
