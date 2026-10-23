---
url: https://docs.comfy.org/development/comfy-router/models/wavespeed/flashvsr/code/
title: Use Flashvsr with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:49.938542+00:00
---

# Use Flashvsr with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/wavespeed/flashvsr/code/

## On this page

  * Quick start
  * Schema
    * Input
    * Output
  * Examples
    * Input
    * Output
  * Before you ship



WaveSpeed

# Use Flashvsr with Comfy Router

Copy pageCopy page

Call wavespeed/flashvsr through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `wavespeed/flashvsr`, served by Comfy Router from WaveSpeed. **Input:** Video · **Output:** Video

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `wavespeed/flashvsr` **Endpoint:** `POST https://api.comfy.org/v2/models/wavespeed/flashvsr`

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
            "wavespeed/flashvsr",
            {
                "duration": 4,
                "target_resolution": "1080p",
                "video": "https://samplelib.com/mp4/sample-30s.mp4",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("wavespeed/flashvsr", {
      duration: 4,
      target_resolution: "1080p",
      video: "https://samplelib.com/mp4/sample-30s.mp4",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/wavespeed/flashvsr \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"duration\": 4, \"target_resolution\": \"1080p\", \"video\": \"https://samplelib.com/mp4/sample-30s.mp4\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/wavespeed/flashvsr/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "wavespeed/flashvsr",
                {
                    "duration": 4,
                    "target_resolution": "1080p",
                    "video": "https://samplelib.com/mp4/sample-30s.mp4",
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
    const handle = await comfy.models.submit("wavespeed/flashvsr", {
      duration: 4,
      target_resolution: "1080p",
      video: "https://samplelib.com/mp4/sample-30s.mp4",
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
    curl https://api.comfy.org/v2/models/wavespeed/flashvsr/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"duration\": 4, \"target_resolution\": \"1080p\", \"video\": \"https://samplelib.com/mp4/sample-30s.mp4\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/wavespeed/flashvsr/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/wavespeed/flashvsr/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Schema

### 

​

Input

​

duration

number

required

Duration of the video in seconds

​

target_resolution

string

default:"\"1080p\""

Target resolution to upscale to.Possible values: `720p`, `1080p`, `2k`, `4k`

​

video

string

required

The video to upscale. Can be a URL to the video file or a base64-encoded video.

Generated from the schema Router serves at `GET /v2/models/wavespeed/flashvsr/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

code

integer

WavespeedAI’s own envelope status code, mirroring an HTTP status (200 on the document this schema describes). Wavespeed reports some failures here rather than in the transport status.

​

data

object

required

​

data.created_at

string

ISO-8601 timestamp of when Wavespeed created the prediction.

​

data.error

string

Wavespeed’s free-text failure reason, an empty string when there is none. A prediction that genuinely failed reaches a Router caller as a Comfy Router error rather than as this document.

​

data.id

string

Wavespeed’s identifier for the prediction Router submitted and polled.

​

data.model

string

The Wavespeed model id the prediction ran on.

​

data.outputs

string[]

required

The finished generation. Present and non-empty on the document Router returns; this list IS the result. Each element is a URL to the generated content - an MP4 for `wavespeed/flashvsr`, an image for the two upscalers - or, for the two image ids when the request set `enable_base64_output`, the base64-encoded bytes themselves. The links are Wavespeed’s own and expire.

​

data.status

string

required

The prediction’s terminal state as Wavespeed spelled it. Not narrowed to an enum here: Router forwards the value unchanged and the poll classifier lower-cases before comparing, so a success can legitimately arrive as `completed`, `succeeded`, `success` or `done`, in any case.

​

data.timings

object

Wavespeed’s own timing measurements.

​

data.timings.inference

integer

Inference time in milliseconds. Wavespeed’s number, not the Comfy charge.

​

data.urls

object

Wavespeed’s own links for the prediction.

​

data.urls.get

string

The prediction-result URL Router polled.

​

message

string

Envelope status message, for example `success`.

## 

​

Examples

### 

​

Input
    
    
    {
      "duration": 4,
      "target_resolution": "1080p",
      "video": "https://samplelib.com/mp4/sample-30s.mp4"
    }
    

### 

​

Output
    
    
    {
      "code": 200,
      "data": {
        "created_at": "2027-01-01T00:00:00Z",
        "error": "",
        "id": "3f6c1a90-2b47-4d18-9a55-7c0e8b21d4f3",
        "outputs": [
          "https://example.invalid/wavespeed/flashvsr/upscaled.mp4"
        ],
        "status": "completed",
        "timings": {
          "inference": 128000
        }
      },
      "message": "success"
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/wavespeed/flashvsr/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/wavespeed/flashvsr/code)

[Use Wan 3.0 Video with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/wan/wan3-0-video/code)[Use Seedvr 2 with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/wavespeed/seedvr2/code)

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
