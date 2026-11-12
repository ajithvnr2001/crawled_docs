---
url: https://docs.comfy.org/development/comfy-router/models/ltx/ltx-video-alpha-gen/code/
title: Use LTX Video Alpha Gen with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-12T15:52:10.531256+00:00
---

# Use LTX Video Alpha Gen with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/ltx/ltx-video-alpha-gen/code/

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



LTX

# Use LTX Video Alpha Gen with Comfy Router

Copy pageCopy page

Call ltx/ltx-video-alpha-gen through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `ltx/ltx-video-alpha-gen`, served by Comfy Router from LTX. **Input:** Video · **Output:** Video

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `ltx/ltx-video-alpha-gen` **Endpoint:** `POST https://api.comfy.org/v2/models/ltx/ltx-video-alpha-gen`

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
            "ltx/ltx-video-alpha-gen",
            {
                "video_uri": "https://test-videos.co.uk/vids/sintel/mp4/h264/720/Sintel_720_10s_1MB.mp4",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("ltx/ltx-video-alpha-gen", {
      video_uri: "https://test-videos.co.uk/vids/sintel/mp4/h264/720/Sintel_720_10s_1MB.mp4",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/ltx/ltx-video-alpha-gen \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"video_uri\": \"https://test-videos.co.uk/vids/sintel/mp4/h264/720/Sintel_720_10s_1MB.mp4\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/ltx/ltx-video-alpha-gen/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "ltx/ltx-video-alpha-gen",
                {
                    "video_uri": "https://test-videos.co.uk/vids/sintel/mp4/h264/720/Sintel_720_10s_1MB.mp4",
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
    const handle = await comfy.models.submit("ltx/ltx-video-alpha-gen", {
      video_uri: "https://test-videos.co.uk/vids/sintel/mp4/h264/720/Sintel_720_10s_1MB.mp4",
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
    curl https://api.comfy.org/v2/models/ltx/ltx-video-alpha-gen/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"video_uri\": \"https://test-videos.co.uk/vids/sintel/mp4/h264/720/Sintel_720_10s_1MB.mp4\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/ltx/ltx-video-alpha-gen/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/ltx/ltx-video-alpha-gen/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Schema

### 

​

Input

​

video_uri

string

required

Input video as a publicly accessible HTTPS URL or a base64 data URI. H.264 or HEVC in MP4, MOV or MKV, up to 200 MB by URL. At most 3840 pixels on the long side and 2160 on the short side.

Generated from the schema Router serves at `GET /v2/models/ltx/ltx-video-alpha-gen/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

completed_at

string

Job completion timestamp (ISO 8601)

​

created_at

string

Job creation timestamp (ISO 8601)

​

error

object

Present when status is failed

​

error.message

string

​

error.type

string

​

id

string

Unique job identifier

​

result

object

Present when status is completed; output URLs expire 24 hours after completion

​

result.cutout_video_url

string

URL of the input video with the matte as its alpha channel, a ProRes 4444 MOV

​

result.matte_video_url

string

URL of the grayscale alpha matte, an MP4 in which white is foreground

​

status

string

Job status (pending, processing, completed, failed)

## 

​

Examples

### 

​

Input
    
    
    {
      "video_uri": "https://test-videos.co.uk/vids/sintel/mp4/h264/720/Sintel_720_10s_1MB.mp4"
    }
    

### 

​

Output
    
    
    {
      "completed_at": "2026-01-01T00:00:50Z",
      "created_at": "2026-01-01T00:00:00Z",
      "id": "3f7a1b28-5c0d-4e91-8a6f-1b2c3d4e5f60",
      "result": {
        "cutout_video_url": "https://example.invalid/ltx/cutout.mov",
        "matte_video_url": "https://example.invalid/ltx/matte.mp4"
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/ltx/ltx-video-alpha-gen/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/ltx/ltx-video-alpha-gen/code)

[LTX 2.5 Pro](https://docs.comfy.org/development/comfy-router/models/ltx/ltx-2-5-pro/code)[LTX Video To Video Hdr](https://docs.comfy.org/development/comfy-router/models/ltx/ltx-video-to-video-hdr/code)
