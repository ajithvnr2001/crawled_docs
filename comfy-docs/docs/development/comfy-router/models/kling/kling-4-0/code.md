---
url: https://docs.comfy.org/development/comfy-router/models/kling/kling-4-0/code/
title: Use Kling 4.0 with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-13T15:12:17.956674+00:00
---

# Use Kling 4.0 with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/kling/kling-4-0/code/

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



Kling

# Use Kling 4.0 with Comfy Router

Copy pageCopy page

Call kling/kling-4.0 through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `kling/kling-4.0`, served by Comfy Router from Kling. **Input:** Text, Image, Video · **Output:** Video

## Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `kling/kling-4.0` **Endpoint:** `POST https://api.comfy.org/v2/models/kling/kling-4.0`

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
            "kling/kling-4.0",
            {
                "contents": [
                    {
                        "text": "The fox turns toward the camera.",
                        "type": "prompt",
                    },
                    {
                        "type": "first_frame",
                        "url": "https://example.com/fox.png",
                    },
                ],
                "settings": {
                    "duration": 3,
                    "resolution": "720p",
                },
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("kling/kling-4.0", {
      contents: [
        {
          text: "The fox turns toward the camera.",
          type: "prompt",
        },
        {
          type: "first_frame",
          url: "https://example.com/fox.png",
        },
      ],
      settings: {
        duration: 3,
        resolution: "720p",
      },
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/kling/kling-4.0 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"contents\": [{\"text\":\"The fox turns toward the camera.\",\"type\":\"prompt\"},{\"type\":\"first_frame\",\"url\":\"https://example.com/fox.png\"}], \"settings\": {\"duration\":3,\"resolution\":\"720p\"}}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/kling/kling-4.0/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "kling/kling-4.0",
                {
                    "contents": [
                        {
                            "text": "The fox turns toward the camera.",
                            "type": "prompt",
                        },
                        {
                            "type": "first_frame",
                            "url": "https://example.com/fox.png",
                        },
                    ],
                    "settings": {
                        "duration": 3,
                        "resolution": "720p",
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
    const handle = await comfy.models.submit("kling/kling-4.0", {
      contents: [
        {
          text: "The fox turns toward the camera.",
          type: "prompt",
        },
        {
          type: "first_frame",
          url: "https://example.com/fox.png",
        },
      ],
      settings: {
        duration: 3,
        resolution: "720p",
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
    curl https://api.comfy.org/v2/models/kling/kling-4.0/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"contents\": [{\"text\":\"The fox turns toward the camera.\",\"type\":\"prompt\"},{\"type\":\"first_frame\",\"url\":\"https://example.com/fox.png\"}], \"settings\": {\"duration\":3,\"resolution\":\"720p\"}}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/kling/kling-4.0/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/kling/kling-4.0/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## Schema

### Input

contents

object[]

The prompt and the input media. Holding only “prompt”, “first_frame”, “middle_frame” and “last_frame” items selects image-to-video (a prompt and up to 10 frames); holding any “refer_image”, “feature_video”, “base_video”, “element” or “voice” selects omni video (up to 15 inputs, with at most 10 images, 5 videos, 7 elements and 3 voices). A request with a “feature_video”, a “base_video” or a video character element bills at the video-input rate.

contents[].element_id

string

Element ID, when type is “element”.

contents[].id

string

Reference ID for this input, used as @id in the prompt. Must be unique within the task. Required for “element” and “voice”.

contents[].text

string

Text prompt, when type is “prompt”. Up to 26,000 English characters or 11,000 non-English characters; comfy-api enforces 1 to 26,000 characters, and Kling itself refuses longer non-English text. Reference other inputs as @id.

contents[].type

string

required

Input type. Image-to-video accepts only “prompt”, “first_frame”, “middle_frame” and “last_frame”, and refuses any other type. Omni video also accepts “refer_image”, “feature_video” (a reference video), “base_video” (the video to edit, at most one), “element” and “voice”.Possible values: `prompt`, `first_frame`, `middle_frame`, `last_frame`, `refer_image`, `feature_video`, `base_video`, `element`, `voice`

contents[].url

string

Image or video URL, when type is a frame, “refer_image”, “feature_video” or “base_video”. Images may also be Base64. Images are .jpg, .jpeg or .png up to 30MB, at least 300px per side, with an aspect ratio between 2:5 and 5:2. Videos are .mp4 or .mov up to 300MB and 3 to 30 seconds long.

contents[].voice_id

string

Voice ID, when type is “voice”. A Kling preset voice or a custom voice.

options

object

General configuration such as watermark options. `options.callback_url` and `options.external_task_id` are not supported on Kling 4.0; Comfy Router refuses a request that sets either inside `options`. A top-level `callback_url` or `external_task_id` is not part of this schema and is removed before the request reaches Kling.

options.watermark_info

object

Whether to generate watermarked results simultaneously. Custom watermarks are not supported. An explicit null is treated as absent, as the /proxy Kling 4.0 check and Kling do.

options.watermark_info.enabled

boolean

true means generate watermarked result, false means do not generate. Default false.

prompt

string

Text-to-video prompt. Required when `contents` is absent or empty, and refused alongside a non-empty `contents`. Up to 26,000 English characters or 11,000 non-English characters; comfy-api enforces 1 to 26,000 characters, and Kling itself refuses longer non-English text.

settings

object

required

Output configuration such as resolution, aspect ratio and duration.

settings.aspect_ratio

string

Aspect ratio (width:height) of the generated frames. One of “21:9”, “16:9”, “9:16” or “1:1” for text-to-video (default “16:9”), those or “adaptive” for omni video (default “adaptive”). Image-to-video follows the images. An explicit null is treated as absent, as the /proxy Kling 4.0 check and Kling do.Possible values: `21:9`, `16:9`, `9:16`, `1:1`, `adaptive`

settings.duration

integer

Video length in seconds, 3 through 30. Required unless `contents` holds a “base_video”, where an edit may omit it to keep the base video’s length. Such a call is held and estimated at the 30-second maximum at the requested resolution, an upper bound rather than the price, and is billed from the price Kling reports for the finished task.Range: `3` to `30`

settings.resolution

string

required

Resolution of the generated video. One of “720p” or “1080p”. Required.Possible values: `720p`, `1080p`

Generated from the schema Router serves at `GET /v2/models/kling/kling-4.0/openapi.json`, the same document it validates a call against before the request reaches the provider.

### Output

code

integer

Error code. 0 indicates success.

data

object[]

Tasks matching the query.

data[].billing

object[]

Billing details for the task.

data[].billing[].amount

string

Consumption amount, accurate to two decimal places.

data[].billing[].cash_type

string

Cash account the charge was drawn from (only present when charge_type is “cash”), for example “balance”. Some tasks return it; others may omit it.

data[].billing[].charge_type

string

Consumption account type. “cash” for balance, “unit” for a resource package.

data[].billing[].currency

string

ISO 4217 currency code of `amount` and `list_price`, for example “USD”. Some tasks return it; others may omit it.

data[].billing[].list_price

string

List price of the task before any discount, as a decimal string. Some tasks return it; others may omit it.

data[].billing[].package_type

string

Consumable resource bundle type (only present when charge_type is “unit”). One of “video”, “image” or “audio”.

data[].create_time

integer

Task creation time. Unix timestamp in milliseconds.Format: `int64`

data[].external_id

string

The custom task ID for this task, if any.

data[].id

string

The task ID.

data[].message

string

Task status information, displaying the failure reason when the task fails.

data[].outputs

object[]

Generated outputs for the task.

data[].outputs[].duration

string

Duration of the generated video in seconds.

data[].outputs[].group_id

string

Grouping marker, present only for grouped images.

data[].outputs[].id

string

Output ID generated by the system.

data[].outputs[].mp3_duration

string

Duration of the generated MP3 audio in seconds.

data[].outputs[].mp3_url

string

MP3 URL of the generated audio (hotlink-protected).

data[].outputs[].name

string

Name of the generated material.

data[].outputs[].owned_by

string

Source of the material. “kling” denotes the official library; numbers are creator IDs.

data[].outputs[].status

string

Status of the material. One of “succeeded” or “deleted”.

data[].outputs[].type

string

Output content type. One of “video”, “image”, “audio”, “voice” or “element”.

data[].outputs[].url

string

URL of the generated result (hotlink-protected). Cleared after 30 days.

data[].outputs[].watermark_url

string

URL of the watermarked result (hotlink-protected).

data[].outputs[].wav_duration

string

Duration of the generated WAV audio in seconds.

data[].outputs[].wav_url

string

WAV URL of the generated audio (hotlink-protected).

data[].status

string

Task status. One of “submitted”, “processing”, “succeeded” or “failed”.

data[].update_time

integer

Task update time. Unix timestamp in milliseconds.Format: `int64`

message

string

Error message.

request_id

string

Request ID generated by the system.

## Examples

### Input
    
    
    {
      "contents": [
        {
          "text": "The fox turns toward the camera.",
          "type": "prompt"
        },
        {
          "type": "first_frame",
          "url": "https://example.com/fox.png"
        }
      ],
      "settings": {
        "duration": 3,
        "resolution": "720p"
      }
    }
    

### Output
    
    
    {
      "code": 0,
      "data": [
        {
          "create_time": 1798761600000,
          "id": "kling-v2-task-7c8d9e0f1a2b",
          "message": "",
          "outputs": [
            {
              "duration": "5",
              "id": "kling-v2-output-2b1a0f9e8d7c",
              "type": "video",
              "url": "https://example.invalid/kling/v2/generated.mp4"
            }
          ],
          "status": "succeeded",
          "update_time": 1798761820000
        }
      ],
      "message": "SUCCEED",
      "request_id": "3d7e5c91-0b42-4f68-9a13-8e2c6d4b0a75"
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/kling/kling-4-0/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/kling/kling-4-0/code)

[Kling 3.0 Turbo](https://docs.comfy.org/development/comfy-router/models/kling/kling-3-0-turbo/code)[Kling Image O1](https://docs.comfy.org/development/comfy-router/models/kling/kling-image-o1/code)
