---
url: https://docs.comfy.org/development/comfy-router/models/luma_2/ray-3-2/code/
title: Use Ray 3.2 with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-23T16:38:27.109456+00:00
---

# Use Ray 3.2 with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/luma_2/ray-3-2/code/

## On this page

  * Quick start
  * Schema
    * Input
    * Output
  * Examples
    * Input
    * Output
  * Before you ship



Luma 2

# Use Ray 3.2 with Comfy Router

Copy pageCopy page

Call luma_2/ray-3.2 through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `luma_2/ray-3.2`, served by Comfy Router from Luma 2. **Input:** Text, Image, Video · **Output:** Video

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `luma_2/ray-3.2` **Endpoint:** `POST https://api.comfy.org/v2/models/luma_2/ray-3.2`

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
            "luma_2/ray-3.2",
            {
                "prompt": "a paper boat drifting across a plain white background",
                "type": "video",
                "video": {
                    "duration": "5s",
                    "resolution": "360p",
                },
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("luma_2/ray-3.2", {
      prompt: "a paper boat drifting across a plain white background",
      type: "video",
      video: {
        duration: "5s",
        resolution: "360p",
      },
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/luma_2/ray-3.2 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"a paper boat drifting across a plain white background\", \"type\": \"video\", \"video\": {\"duration\":\"5s\",\"resolution\":\"360p\"}}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/luma_2/ray-3.2/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "luma_2/ray-3.2",
                {
                    "prompt": "a paper boat drifting across a plain white background",
                    "type": "video",
                    "video": {
                        "duration": "5s",
                        "resolution": "360p",
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
    const handle = await comfy.models.submit("luma_2/ray-3.2", {
      prompt: "a paper boat drifting across a plain white background",
      type: "video",
      video: {
        duration: "5s",
        resolution: "360p",
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
    curl https://api.comfy.org/v2/models/luma_2/ray-3.2/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"a paper boat drifting across a plain white background\", \"type\": \"video\", \"video\": {\"duration\":\"5s\",\"resolution\":\"360p\"}}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/luma_2/ray-3.2/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/luma_2/ray-3.2/requests/$REQUEST_ID \
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

Output aspect ratio. The ray-3.2 video models support the subset 9:16, 3:4, 1:1, 4:3, 16:9, 21:9.Possible values: `3:1`, `2:1`, `21:9`, `16:9`, `3:2`, `4:3`, `1:1`, `3:4`, `2:3`, `9:16`, `1:2`, `1:3`

​

image_ref

object[]

Reference images for style/content guidance. Up to 9 for type ‘image’, up to 8 for type ‘image_edit’.

​

image_ref[].data

string

Base64-encoded image or video data

​

image_ref[].generation_id

string

UUID of a prior completed generation to reuse as the source. Used by ray-3.2 video_edit / video_reframe.

​

image_ref[].media_type

string

MIME type. Required with data (and with url for video sources, e.g. video/mp4 on video_edit / video_reframe).

​

image_ref[].url

string

Publicly accessible image or video URL

​

model

string

Model to use. uni-1 / uni-1-max for image generation, ray-3.2 for video generation, editing, and reframing.

​

output_format

string

Output image formatPossible values: `png`, `jpeg`

​

prompt

string

required

Text prompt

​

source

object

Reference to an image or video. Used for style/content guidance, guided generation, video-edit/video-reframe sources, and guide keyframes. Provide exactly one of generation_id, url, or data.

​

source.data

string

Base64-encoded image or video data

​

source.generation_id

string

UUID of a prior completed generation to reuse as the source. Used by ray-3.2 video_edit / video_reframe.

​

source.media_type

string

MIME type. Required with data (and with url for video sources, e.g. video/mp4 on video_edit / video_reframe).

​

source.url

string

Publicly accessible image or video URL

​

style

string

Style presetPossible values: `auto`, `manga`

​

type

string

The kind of generation to perform. image/image_edit are produced by the uni-1 / uni-1-max models; video/video_edit/video_reframe are produced by the ray-3.2 model.Possible values: `image`, `image_edit`, `video`, `video_edit`, `video_reframe`

​

video

object

Video output settings for ray-3.2. Only the fields that affect validation and billing are modelled here; additional fields (edit controls, source_position) are forwarded to Luma untouched.

​

video.duration

string

Clip duration for ray-3.2 video / video_edit. Defaults to 5s. HDR generation (type video) is restricted to 5s.Possible values: `5s`, `10s`

​

video.end_frame

object

Reference to an image or video. Used for style/content guidance, guided generation, video-edit/video-reframe sources, and guide keyframes. Provide exactly one of generation_id, url, or data.

​

video.end_frame.data

string

Base64-encoded image or video data

​

video.end_frame.generation_id

string

UUID of a prior completed generation to reuse as the source. Used by ray-3.2 video_edit / video_reframe.

​

video.end_frame.media_type

string

MIME type. Required with data (and with url for video sources, e.g. video/mp4 on video_edit / video_reframe).

​

video.end_frame.url

string

Publicly accessible image or video URL

​

video.exr_export

boolean

Export an EXR file alongside the MP4. Requires hdr true. Rejected for video_reframe.

​

video.hdr

boolean

Render in HDR. Requires 720p/1080p. Rejected for video_reframe.

​

video.keyframe_indexes

integer[]

Output-frame positions for `keyframes`, same length; 0–120 for 5s, 0–240 for 10s. Forwarded untouched.

​

video.keyframes

object[]

Guide-frame images (1–64), mutually exclusive with start_frame/end_frame. Billed at the requested duration; a keyframes request is never a single-keyframe extend.

​

video.keyframes[].data

string

Base64-encoded image or video data

​

video.keyframes[].generation_id

string

UUID of a prior completed generation to reuse as the source. Used by ray-3.2 video_edit / video_reframe.

​

video.keyframes[].media_type

string

MIME type. Required with data (and with url for video sources, e.g. video/mp4 on video_edit / video_reframe).

​

video.keyframes[].url

string

Publicly accessible image or video URL

​

video.loop

boolean

Loop the generated clip. Create-only (type video).

​

video.resolution

string

Output resolution for ray-3.2 video. Defaults to 720p. 360p is the draft tier. HDR requires 720p or 1080p.Possible values: `360p`, `540p`, `720p`, `1080p`

​

video.start_frame

object

Reference to an image or video. Used for style/content guidance, guided generation, video-edit/video-reframe sources, and guide keyframes. Provide exactly one of generation_id, url, or data.

​

video.start_frame.data

string

Base64-encoded image or video data

​

video.start_frame.generation_id

string

UUID of a prior completed generation to reuse as the source. Used by ray-3.2 video_edit / video_reframe.

​

video.start_frame.media_type

string

MIME type. Required with data (and with url for video sources, e.g. video/mp4 on video_edit / video_reframe).

​

video.start_frame.url

string

Publicly accessible image or video URL

​

web_search

boolean

Enable web search grounding

Generated from the schema Router serves at `GET /v2/models/luma_2/ray-3.2/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

created_at

string

Creation timestamp

​

failure_code

string

Machine-readable failure code for programmatic handlingPossible values: `content_moderated`, `generation_failed`, `budget_exhausted`, `output_not_found`

​

failure_reason

string

Human-readable failure description, populated only on a FAILED generation. `null` on a successful one.

​

id

string

Generation identifier

​

model

string

Model used

​

output

object[]

A generated output entry

​

output[].type

string

Media type (e.g. image)

​

output[].url

string

Presigned URL (1hr expiry)

​

state

string

Current state of the generationPossible values: `queued`, `processing`, `completed`, `failed`

​

type

string

The kind of generation to perform. image/image_edit are produced by the uni-1 / uni-1-max models; video/video_edit/video_reframe are produced by the ray-3.2 model.Possible values: `image`, `image_edit`, `video`, `video_edit`, `video_reframe`

## 

​

Examples

### 

​

Input
    
    
    {
      "prompt": "a paper boat drifting across a plain white background",
      "type": "video",
      "video": {
        "duration": "5s",
        "resolution": "360p"
      }
    }
    

### 

​

Output
    
    
    {
      "created_at": "2027-01-01T00:00:00Z",
      "failure_code": null,
      "failure_reason": null,
      "id": "gen-luma-agents-ray32-9c1f3a0e7d52",
      "model": "ray-3.2",
      "output": [
        {
          "type": "video",
          "url": "https://example.invalid/luma_2/ray-3.2/generated.mp4"
        }
      ],
      "state": "completed",
      "type": "video"
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/luma_2/ray-3-2/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/luma_2/ray-3-2/code)

[Ray Flash 2](https://docs.comfy.org/development/comfy-router/models/luma/ray-flash-2/code)[Uni 1 Max](https://docs.comfy.org/development/comfy-router/models/luma_2/uni-1-max/code)
