---
url: https://docs.comfy.org/development/comfy-router/models/luma_2/uni-1/code/
title: Use Uni 1 with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:19.386197+00:00
---

# Use Uni 1 with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/luma_2/uni-1/code/

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

# Use Uni 1 with Comfy Router

Copy pageCopy page

Call luma_2/uni-1 through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `luma_2/uni-1`, served by Comfy Router from Luma 2. **Input:** Text, Image · **Output:** Image

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `luma_2/uni-1` **Endpoint:** `POST https://api.comfy.org/v2/models/luma_2/uni-1`

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
            "luma_2/uni-1",
            {
                "prompt": "a red circle on a plain white background",
                "type": "image",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("luma_2/uni-1", {
      prompt: "a red circle on a plain white background",
      type: "image",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/luma_2/uni-1 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"a red circle on a plain white background\", \"type\": \"image\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/luma_2/uni-1/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "luma_2/uni-1",
                {
                    "prompt": "a red circle on a plain white background",
                    "type": "image",
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
    const handle = await comfy.models.submit("luma_2/uni-1", {
      prompt: "a red circle on a plain white background",
      type: "image",
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
    curl https://api.comfy.org/v2/models/luma_2/uni-1/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"a red circle on a plain white background\", \"type\": \"image\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/luma_2/uni-1/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/luma_2/uni-1/requests/$REQUEST_ID \
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

Video output settings for ray-3.2. Only the fields that affect validation and billing are modelled here; additional fields (edit controls, end_frame, loop, source_position) are forwarded to Luma untouched.

​

video.duration

string

Clip duration for ray-3.2 video / video_edit. Defaults to 5s. HDR generation (type video) is restricted to 5s.Possible values: `5s`, `10s`

​

video.exr_export

boolean

Export an EXR file alongside the MP4. Requires hdr true. Rejected for video_reframe.

​

video.hdr

boolean

Render in HDR. Requires 720p/1080p. Rejected for video_reframe.

​

video.keyframes

object[]

Guide-frame images. A single keyframe makes a type “video” request a single-keyframe extend, which always bills as one 5s block.

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

Generated from the schema Router serves at `GET /v2/models/luma_2/uni-1/openapi.json`, the same document it validates a call against before the request reaches the provider.

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
      "prompt": "a red circle on a plain white background",
      "type": "image"
    }
    

### 

​

Output
    
    
    {
      "created_at": "2027-01-01T00:00:00Z",
      "failure_code": null,
      "failure_reason": null,
      "id": "gen-luma-agents-3f2a7c1e8b40",
      "model": "uni-1",
      "output": [
        {
          "type": "image",
          "url": "https://example.invalid/luma_2/uni-1/generated.png"
        }
      ],
      "state": "completed",
      "type": "image"
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/luma_2/uni-1/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/luma_2/uni-1/code)

[Use Uni 1 Max with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/luma_2/uni-1-max/code)[Use Animations with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/meshy/animations/code)

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
