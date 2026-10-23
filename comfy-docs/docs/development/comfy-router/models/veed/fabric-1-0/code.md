---
url: https://docs.comfy.org/development/comfy-router/models/veed/fabric-1-0/code/
title: Use Fabric 1.0 with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-23T16:38:28.955481+00:00
---

# Use Fabric 1.0 with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/veed/fabric-1-0/code/

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

# Use Fabric 1.0 with Comfy Router

Copy pageCopy page

Call veed/fabric-1.0 through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `veed/fabric-1.0`, served by Comfy Router from Veed. **Input:** Image, Audio · **Output:** Video + Audio

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `veed/fabric-1.0` **Endpoint:** `POST https://api.comfy.org/v2/models/veed/fabric-1.0`

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
            "veed/fabric-1.0",
            {
                "audio_url": "https://static-assets.veed.io/api-examples/fabric-input.mp3",
                "image_url": "https://static-assets.veed.io/api-examples/fabric-input.png",
                "resolution": "480p",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("veed/fabric-1.0", {
      audio_url: "https://static-assets.veed.io/api-examples/fabric-input.mp3",
      image_url: "https://static-assets.veed.io/api-examples/fabric-input.png",
      resolution: "480p",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/veed/fabric-1.0 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"audio_url\": \"https://static-assets.veed.io/api-examples/fabric-input.mp3\", \"image_url\": \"https://static-assets.veed.io/api-examples/fabric-input.png\", \"resolution\": \"480p\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/veed/fabric-1.0/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "veed/fabric-1.0",
                {
                    "audio_url": "https://static-assets.veed.io/api-examples/fabric-input.mp3",
                    "image_url": "https://static-assets.veed.io/api-examples/fabric-input.png",
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
    const handle = await comfy.models.submit("veed/fabric-1.0", {
      audio_url: "https://static-assets.veed.io/api-examples/fabric-input.mp3",
      image_url: "https://static-assets.veed.io/api-examples/fabric-input.png",
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
    curl https://api.comfy.org/v2/models/veed/fabric-1.0/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"audio_url\": \"https://static-assets.veed.io/api-examples/fabric-input.mp3\", \"image_url\": \"https://static-assets.veed.io/api-examples/fabric-input.png\", \"resolution\": \"480p\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/veed/fabric-1.0/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/veed/fabric-1.0/requests/$REQUEST_ID \
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

Public http(s) URL of the speech track to lip-sync to. The video is as long as the audio.

​

image_url

string

required

Public http(s) URL of the image to animate.

​

resolution

string

required

Output resolution: 480p or 720p.

Generated from the schema Router serves at `GET /v2/models/veed/fabric-1.0/openapi.json`, the same document it validates a call against before the request reaches the provider.

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
      "audio_url": "https://static-assets.veed.io/api-examples/fabric-input.mp3",
      "image_url": "https://static-assets.veed.io/api-examples/fabric-input.png",
      "resolution": "480p"
    }
    

### 

​

Output
    
    
    {
      "data": {
        "credits_charged": 31,
        "job_id": "33250068-033e-4aa6-a4b5-a0de6e3bdc95",
        "result": {
          "video": {
            "content_type": "video/mp4",
            "url": "https://example.invalid/veed/video.mp4"
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/veed/fabric-1-0/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/veed/fabric-1-0/code)

[Clean Audio](https://docs.comfy.org/development/comfy-router/models/veed/clean-audio/code)[Lipsync 2.0](https://docs.comfy.org/development/comfy-router/models/veed/lipsync-2-0/code)
