---
url: https://docs.comfy.org/development/comfy-router/models/veed/clean-audio/code/
title: Use Clean Audio with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-23T16:38:28.275646+00:00
---

# Use Clean Audio with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/veed/clean-audio/code/

## On this page

  * Quick start
  * Schema
    * Input
    * Output
  * Examples
    * Input
    * Output
  * Before you ship



Veed

# Use Clean Audio with Comfy Router

Copy pageCopy page

Call veed/clean-audio through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `veed/clean-audio`, served by Comfy Router from Veed. **Input:** Audio · **Output:** Audio

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `veed/clean-audio` **Endpoint:** `POST https://api.comfy.org/v2/models/veed/clean-audio`

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
            "veed/clean-audio",
            {
                "audio_url": "https://static-assets.veed.io/api-examples/clean-audio-input.m4a",
                "normalize_loudness": True,
                "output_format": "flac",
                "strength": 0.874,
                "target_lufs": -19,
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("veed/clean-audio", {
      audio_url: "https://static-assets.veed.io/api-examples/clean-audio-input.m4a",
      normalize_loudness: true,
      output_format: "flac",
      strength: 0.874,
      target_lufs: -19,
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/veed/clean-audio \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"audio_url\": \"https://static-assets.veed.io/api-examples/clean-audio-input.m4a\", \"normalize_loudness\": true, \"output_format\": \"flac\", \"strength\": 0.874, \"target_lufs\": -19}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/veed/clean-audio/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "veed/clean-audio",
                {
                    "audio_url": "https://static-assets.veed.io/api-examples/clean-audio-input.m4a",
                    "normalize_loudness": True,
                    "output_format": "flac",
                    "strength": 0.874,
                    "target_lufs": -19,
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
    const handle = await comfy.models.submit("veed/clean-audio", {
      audio_url: "https://static-assets.veed.io/api-examples/clean-audio-input.m4a",
      normalize_loudness: true,
      output_format: "flac",
      strength: 0.874,
      target_lufs: -19,
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
    curl https://api.comfy.org/v2/models/veed/clean-audio/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"audio_url\": \"https://static-assets.veed.io/api-examples/clean-audio-input.m4a\", \"normalize_loudness\": true, \"output_format\": \"flac\", \"strength\": 0.874, \"target_lufs\": -19}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/veed/clean-audio/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/veed/clean-audio/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Schema

### 

​

Input

​

audio_url

string

required

Public http(s) URL of the recording to clean, up to 30 minutes.

​

normalize_loudness

boolean

default:"true"

Set to false to keep the input loudness.

​

output_format

string

default:"\"flac\""

Output container: flac or wav.

​

strength

number

default:"0.874"

How much background noise is removed under speech.Range: `0` to `1`

​

target_lufs

number

default:"-19"

Output loudness in LUFS. Ignored when `normalize_loudness` is false.Range: `-40` to `-8`

Generated from the schema Router serves at `GET /v2/models/veed/clean-audio/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

data

object

​

data.credits_charged

integer

Credits VEED charged for the job. Present once the job is COMPLETED.

​

data.credits_estimated

integer

Credits VEED quoted before the job ran. Present only on the submit response.

​

data.error

object

Failure information. Present once the job has FAILED.

​

data.error.code

string

Machine-readable failure code.

​

data.error.details

object[]

​

data.error.message

string

Human-readable failure message.

​

data.job_id

string

Job id used to poll for status.

​

data.result

object

The produced media. Present once the job is COMPLETED. Video routes answer `video`, Clean Audio answers `audio` and Video Background Removal answers `files`.

​

data.result.audio

object

​

data.result.audio.content_type

string

MIME type of the file.

​

data.result.audio.file_name

string

Name of the file.

​

data.result.audio.file_size

integer

Size of the file in bytes.Format: `int64`

​

data.result.audio.url

string

URL the file can be downloaded from.

​

data.result.files

object[]

Video Background Removal output. One WebM with alpha for `vp9`, or the RGB video and an alpha matte for `h264`.

​

data.result.files[].content_type

string

MIME type of the file.

​

data.result.files[].file_name

string

Name of the file.

​

data.result.files[].file_size

integer

Size of the file in bytes.Format: `int64`

​

data.result.files[].url

string

URL the file can be downloaded from.

​

data.result.video

object

​

data.result.video.content_type

string

MIME type of the file.

​

data.result.video.file_name

string

Name of the file.

​

data.result.video.file_size

integer

Size of the file in bytes.Format: `int64`

​

data.result.video.url

string

URL the file can be downloaded from.

​

data.status

string

Job status: PROCESSING, COMPLETED, FAILED or CANCELLED.

## 

​

Examples

### 

​

Input
    
    
    {
      "audio_url": "https://static-assets.veed.io/api-examples/clean-audio-input.m4a",
      "normalize_loudness": true,
      "output_format": "flac",
      "strength": 0.874,
      "target_lufs": -19
    }
    

### 

​

Output
    
    
    {
      "data": {
        "credits_charged": 1,
        "job_id": "2e3f1c51-a71c-4dc2-9c8d-857c1920a64d",
        "result": {
          "audio": {
            "content_type": "audio/flac",
            "url": "https://example.invalid/veed/clean.flac"
          }
        },
        "status": "COMPLETED"
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/veed/clean-audio/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/veed/clean-audio/code)

[Clean Audio Video](https://docs.comfy.org/development/comfy-router/models/veed/clean-audio-video/code)[Fabric 1.0](https://docs.comfy.org/development/comfy-router/models/veed/fabric-1-0/code)
