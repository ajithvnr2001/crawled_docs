---
url: https://docs.comfy.org/development/comfy-router/models/kling/videos-lip-sync/code/
title: Use Videos Lip Sync with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:16.258479+00:00
---

# Use Videos Lip Sync with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/kling/videos-lip-sync/code/

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

# Use Videos Lip Sync with Comfy Router

Copy pageCopy page

Call kling/videos-lip-sync through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `kling/videos-lip-sync`, served by Comfy Router from Kling. **Input:** Video, Audio · **Output:** Video

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `kling/videos-lip-sync` **Endpoint:** `POST https://api.comfy.org/v2/models/kling/videos-lip-sync`

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
            "kling/videos-lip-sync",
            {
                "input": {
                    "mode": "text2video",
                    "text": "Welcome to Comfy Cloud.",
                    "video_id": "kling-video-6f5e4d3c2b1a",
                    "voice_id": "genshin_vindi2",
                    "voice_language": "en",
                    "voice_speed": 1,
                },
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("kling/videos-lip-sync", {
      input: {
        mode: "text2video",
        text: "Welcome to Comfy Cloud.",
        video_id: "kling-video-6f5e4d3c2b1a",
        voice_id: "genshin_vindi2",
        voice_language: "en",
        voice_speed: 1,
      },
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/kling/videos-lip-sync \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input\": {\"mode\":\"text2video\",\"text\":\"Welcome to Comfy Cloud.\",\"video_id\":\"kling-video-6f5e4d3c2b1a\",\"voice_id\":\"genshin_vindi2\",\"voice_language\":\"en\",\"voice_speed\":1}}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/kling/videos-lip-sync/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "kling/videos-lip-sync",
                {
                    "input": {
                        "mode": "text2video",
                        "text": "Welcome to Comfy Cloud.",
                        "video_id": "kling-video-6f5e4d3c2b1a",
                        "voice_id": "genshin_vindi2",
                        "voice_language": "en",
                        "voice_speed": 1,
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
    const handle = await comfy.models.submit("kling/videos-lip-sync", {
      input: {
        mode: "text2video",
        text: "Welcome to Comfy Cloud.",
        video_id: "kling-video-6f5e4d3c2b1a",
        voice_id: "genshin_vindi2",
        voice_language: "en",
        voice_speed: 1,
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
    curl https://api.comfy.org/v2/models/kling/videos-lip-sync/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input\": {\"mode\":\"text2video\",\"text\":\"Welcome to Comfy Cloud.\",\"video_id\":\"kling-video-6f5e4d3c2b1a\",\"voice_id\":\"genshin_vindi2\",\"voice_language\":\"en\",\"voice_speed\":1}}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/kling/videos-lip-sync/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/kling/videos-lip-sync/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Schema

### 

​

Input

​

callback_url

string (uri)

The callback notification address. Server will notify when the task status changes.Format: `uri`

​

input

object

required

​

input.audio_file

string

Local Path of Audio File. Supported formats: .mp3/.wav/.m4a/.aac, maximum file size of 5MB. Base64 code.

​

input.audio_type

string

Method of Transmitting Audio Files for Lip-Sync. Required when mode is audio2video.Possible values: `file`, `url`

​

input.audio_url

string

Audio File Download URL. Supported formats: .mp3/.wav/.m4a/.aac, maximum file size of 5MB.

​

input.mode

string

required

Video Generation Mode. text2video: Text-to-video generation mode; audio2video: Audio-to-video generation modePossible values: `text2video`, `audio2video`

​

input.text

string

Text Content for Lip-Sync Video Generation. Required when mode is text2video. Maximum length is 120 characters.

​

input.video_id

string

The ID of the video generated by Kling AI. Only supports 5-second and 10-second videos generated within the last 30 days.

​

input.video_url

string

Get link for uploaded video. Video files support .mp4/.mov, file size does not exceed 100MB, video length between 2-10s.

​

input.voice_id

string

Voice ID. Required when mode is text2video. The system offers a variety of voice options to choose from.

​

input.voice_language

string

default:"\"en\""

The voice language corresponds to the Voice ID.Possible values: `zh`, `en`

​

input.voice_speed

number

default:"1"

Speech Rate. Valid range: 0.8~2.0, accurate to one decimal place.Range: `0.8` to `2`

Generated from the schema Router serves at `GET /v2/models/kling/videos-lip-sync/openapi.json`, the same document it validates a call against before the request reaches the provider.

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

Task creation time

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

data.updated_at

integer

Task update time

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
      "input": {
        "mode": "text2video",
        "text": "Welcome to Comfy Cloud.",
        "video_id": "kling-video-6f5e4d3c2b1a",
        "voice_id": "genshin_vindi2",
        "voice_language": "en",
        "voice_speed": 1
      }
    }
    

### 

​

Output
    
    
    {
      "code": 0,
      "data": {
        "created_at": 1798761600000,
        "final_unit_deduction": "1.00",
        "task_id": "kling-lip-sync-task-4f3e2d1c0b9a",
        "task_result": {
          "videos": [
            {
              "duration": "8",
              "id": "kling-video-9a8b7c6d5e4f",
              "url": "https://example.invalid/kling/videos-lip-sync/generated.mp4"
            }
          ]
        },
        "task_status": "succeed",
        "updated_at": 1798761780000
      },
      "message": "SUCCEED",
      "request_id": "5e0a9b17-6d3c-42f8-91b4-7a2c8d6e0f35"
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/kling/videos-lip-sync/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/kling/videos-lip-sync/code)

[Use Videos Avatar Image 2video with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/kling/videos-avatar-image2video/code)[Use Videos Video Extend with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/kling/videos-video-extend/code)

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
