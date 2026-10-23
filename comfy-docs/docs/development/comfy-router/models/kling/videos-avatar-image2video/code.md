---
url: https://docs.comfy.org/development/comfy-router/models/kling/videos-avatar-image2video/code/
title: Use Videos Avatar Image 2video with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:15.170020+00:00
---

# Use Videos Avatar Image 2video with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/kling/videos-avatar-image2video/code/

## On this page

  * Quick start
  * Schema
    * Input
    * Output
  * Examples
    * Input
    * Output
  * Before you ship



Kling

# Use Videos Avatar Image 2video with Comfy Router

Copy pageCopy page

Call kling/videos-avatar-image2video through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `kling/videos-avatar-image2video`, served by Comfy Router from Kling. **Input:** Image, Audio · **Output:** Video

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `kling/videos-avatar-image2video` **Endpoint:** `POST https://api.comfy.org/v2/models/kling/videos-avatar-image2video`

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
            "kling/videos-avatar-image2video",
            {
                "image": "https://example.invalid/kling/avatar.png",
                "mode": "std",
                "prompt": "The presenter smiles and gestures towards the camera.",
                "sound_file": "https://example.invalid/kling/voice.mp3",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("kling/videos-avatar-image2video", {
      image: "https://example.invalid/kling/avatar.png",
      mode: "std",
      prompt: "The presenter smiles and gestures towards the camera.",
      sound_file: "https://example.invalid/kling/voice.mp3",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/kling/videos-avatar-image2video \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"image\": \"https://example.invalid/kling/avatar.png\", \"mode\": \"std\", \"prompt\": \"The presenter smiles and gestures towards the camera.\", \"sound_file\": \"https://example.invalid/kling/voice.mp3\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/kling/videos-avatar-image2video/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "kling/videos-avatar-image2video",
                {
                    "image": "https://example.invalid/kling/avatar.png",
                    "mode": "std",
                    "prompt": "The presenter smiles and gestures towards the camera.",
                    "sound_file": "https://example.invalid/kling/voice.mp3",
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
    const handle = await comfy.models.submit("kling/videos-avatar-image2video", {
      image: "https://example.invalid/kling/avatar.png",
      mode: "std",
      prompt: "The presenter smiles and gestures towards the camera.",
      sound_file: "https://example.invalid/kling/voice.mp3",
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
    curl https://api.comfy.org/v2/models/kling/videos-avatar-image2video/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"image\": \"https://example.invalid/kling/avatar.png\", \"mode\": \"std\", \"prompt\": \"The presenter smiles and gestures towards the camera.\", \"sound_file\": \"https://example.invalid/kling/voice.mp3\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/kling/videos-avatar-image2video/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/kling/videos-avatar-image2video/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Schema

### 

​

Input

​

audio_id

string

Audio ID Generated via TTS API. Only supports 2-300 second audio generated within the last 30 days. Either audio_id or sound_file must be provided (mutually exclusive).

​

callback_url

string (uri)

The callback notification address for the result of this task.Format: `uri`

​

external_task_id

string

Customized Task ID. Must be unique within a single user account.

​

image

string

required

Avatar Reference Image. Supports Base64 encoding or image URL. Supported formats: .jpg/.jpeg/.png. Max 10MB, min 300px width/height, aspect ratio between 1:2.5 and 2.5:1.

​

mode

string

default:"\"std\""

Video generation mode. std: Standard Mode (cost-effective), pro: Professional Mode (longer duration, higher quality).Possible values: `std`, `pro`

​

prompt

string

Positive text prompt. Can define avatar actions, emotions, and camera movements.

​

sound_file

string

Sound File. Supports Base64-encoded audio or accessible audio URL. Accepted formats: .mp3/.wav/.m4a/.aac (max 5MB), 2-300 seconds. Either audio_id or sound_file must be provided (mutually exclusive).

​

watermark_info

object

​

watermark_info.enabled

boolean

Whether to generate watermarked results simultaneously.

Generated from the schema Router serves at `GET /v2/models/kling/videos-avatar-image2video/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

code

integer

Error code

​

data

object

​

data.created_at

integer

Task creation time, Unix timestamp in milliseconds

​

data.final_unit_deduction

string

The deduction units of task

​

data.task_id

string

Task ID

​

data.task_info

object

​

data.task_info.external_task_id

string

​

data.task_result

object

​

data.task_result.videos

object[]

​

data.task_result.videos[].duration

string

Total video duration in seconds

​

data.task_result.videos[].id

string

Generated video ID

​

data.task_result.videos[].url

string (uri)

URL for generated videoFormat: `uri`

​

data.task_result.videos[].watermark_url

string (uri)

URL for generated video with watermark, hotlink protection formatFormat: `uri`

​

data.task_status

string

Task StatusPossible values: `submitted`, `processing`, `succeed`, `failed`

​

data.task_status_msg

string

Task status information, displaying the failure reason when the task fails

​

data.updated_at

integer

Task update time, Unix timestamp in milliseconds

​

data.watermark_info

object

​

data.watermark_info.enabled

boolean

​

message

string

Error message

​

request_id

string

Request ID

## 

​

Examples

### 

​

Input
    
    
    {
      "image": "https://example.invalid/kling/avatar.png",
      "mode": "std",
      "prompt": "The presenter smiles and gestures towards the camera.",
      "sound_file": "https://example.invalid/kling/voice.mp3"
    }
    

### 

​

Output
    
    
    {
      "code": 0,
      "data": {
        "created_at": 1798761600000,
        "task_id": "kling-avatar-task-8b7a6c5d4e3f",
        "task_result": {
          "videos": [
            {
              "duration": "10",
              "id": "kling-video-1c2d3e4f5a6b",
              "url": "https://example.invalid/kling/videos-avatar-image2video/generated.mp4"
            }
          ]
        },
        "task_status": "succeed",
        "task_status_msg": "",
        "updated_at": 1798761900000
      },
      "message": "SUCCEED",
      "request_id": "b41d7c58-9e26-4f03-a7d1-5c8e0b3f2a69"
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/kling/videos-avatar-image2video/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/kling/videos-avatar-image2video/code)

[Use Kling Video O1 with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/kling/kling-video-o1/code)[Use Videos Lip Sync with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/kling/videos-lip-sync/code)

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
