---
url: https://docs.comfy.org/development/comfy-router/models/kling/kling-v3-omni/code/
title: Use Kling V3 Omni with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:14.456350+00:00
---

# Use Kling V3 Omni with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/kling/kling-v3-omni/code/

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

# Use Kling V3 Omni with Comfy Router

Copy pageCopy page

Call kling/kling-v3-omni through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `kling/kling-v3-omni`, served by Comfy Router from Kling. **Input:** Text, Image, Video · **Output:** Video

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `kling/kling-v3-omni` **Endpoint:** `POST https://api.comfy.org/v2/models/kling/kling-v3-omni`

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
            "kling/kling-v3-omni",
            {
                "aspect_ratio": "16:9",
                "duration": "5",
                "mode": "pro",
                "prompt": "A paper boat drifting down a rain-soaked street at dusk.",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("kling/kling-v3-omni", {
      aspect_ratio: "16:9",
      duration: "5",
      mode: "pro",
      prompt: "A paper boat drifting down a rain-soaked street at dusk.",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/kling/kling-v3-omni \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"aspect_ratio\": \"16:9\", \"duration\": \"5\", \"mode\": \"pro\", \"prompt\": \"A paper boat drifting down a rain-soaked street at dusk.\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/kling/kling-v3-omni/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "kling/kling-v3-omni",
                {
                    "aspect_ratio": "16:9",
                    "duration": "5",
                    "mode": "pro",
                    "prompt": "A paper boat drifting down a rain-soaked street at dusk.",
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
    const handle = await comfy.models.submit("kling/kling-v3-omni", {
      aspect_ratio: "16:9",
      duration: "5",
      mode: "pro",
      prompt: "A paper boat drifting down a rain-soaked street at dusk.",
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
    curl https://api.comfy.org/v2/models/kling/kling-v3-omni/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"aspect_ratio\": \"16:9\", \"duration\": \"5\", \"mode\": \"pro\", \"prompt\": \"A paper boat drifting down a rain-soaked street at dusk.\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/kling/kling-v3-omni/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/kling/kling-v3-omni/requests/$REQUEST_ID \
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

The aspect ratio of the generated video frame (width:height). Required when first-frame reference or video editing features are not used.Possible values: `16:9`, `9:16`, `1:1`

​

callback_url

string (uri)

The callback notification address for the result of this task. If configured, the server will actively notify when the task status changes.Format: `uri`

​

duration

string

default:"\"5\""

Video Length in seconds. When using video editing function (refer_type: base), output duration is the same as input video and this parameter is invalid.Possible values: `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`

​

element_list

object[]

Reference Element List based on element ID configuration.

​

element_list[].element_id

integer

required

Element IDFormat: `int64`

​

external_task_id

string

Customized Task ID. Must be unique within a single user account.

​

image_list

object[]

Reference Image List. Can include reference images of the element, scene, style, etc., or be used as the first or last frame to generate videos.

​

image_list[].image_url

string

Image Base64 encoding or image URL (ensure accessibility). Supported formats include .jpg/.jpeg/.png. File size cannot exceed 10MB. Width and height dimensions shall not be less than 300px, aspect ratio between 1:2.5 ~ 2.5:1.

​

image_list[].type

string

Whether the image is in the first or last frame. first_frame is the first frame, end_frame is the last frame. Currently does not support only the end frame.Possible values: `first_frame`, `end_frame`

​

mode

string

default:"\"pro\""

Video generation mode. std: Standard Mode, generating 720P videos, cost-effective. pro: Professional Mode, generating 1080P videos, higher quality video output.Possible values: `pro`, `std`

​

model_name

string

Model name. Omit it or send null when using Comfy Router; the model is selected by the request path. A supplied name must match that path.

​

multi_prompt

object[]

Information about each storyboard, such as prompts and duration. Supports up to 6 storyboards, with a minimum of 1. Required when multi_shot is true and shot_type is customize.

​

multi_prompt[].duration

string

Duration of this storyboard in seconds. Must not exceed total task duration and must not be less than 1. Sum of all storyboard durations equals total task duration.

​

multi_prompt[].index

integer

Shot sequence number

​

multi_prompt[].prompt

string

Prompt word for this storyboard. Maximum length 512 characters.

​

multi_shot

boolean

default:"false"

Whether to generate multi-shot video. When true, the prompt parameter is invalid. When false, the shot_type and multi_prompt parameters are invalid.

​

prompt

string

Text prompt words, which can include positive and negative descriptions. Must not exceed 2,500 characters. Can specify elements, images, or videos in the format <<<>>> such as <<element_1>>, <<<image_1>>>, <<<video_1>>>.

​

shot_type

string

Storyboard method. Required when the multi_shot parameter is set to true.Possible values: `customize`, `intelligence`

​

sound

string

default:"\"off\""

Whether sound is generated simultaneously when generating videos.Possible values: `on`, `off`

​

video_list

object[]

Reference Video list. Can be used as a reference video for feature or as a video to be edited, with the default being the video to be edited.

​

video_list[].keep_original_sound

string

Whether to keep the video original sound. yes indicates retention, no indicates non retention.Possible values: `yes`, `no`

​

video_list[].refer_type

string

Reference video type. feature is the feature reference video, base is the video to be edited.Possible values: `feature`, `base`

​

video_list[].video_url

string

required

URL of uploaded video. Only .mp4/.mov formats are supported. Duration between 3-10 seconds. Resolution must be between 720px and 2160px. Frame rates of 24-60 fps supported. Only 1 video can be uploaded, with size not exceeding 200MB.

​

watermark_info

object

Whether to generate watermarked results simultaneously. Custom watermark is not supported at this time.

​

watermark_info.enabled

boolean

true means generate watermark, false means do not generate.

Generated from the schema Router serves at `GET /v2/models/kling/kling-v3-omni/openapi.json`, the same document it validates a call against before the request reaches the provider.

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
      "aspect_ratio": "16:9",
      "duration": "5",
      "mode": "pro",
      "prompt": "A paper boat drifting down a rain-soaked street at dusk."
    }
    

### 

​

Output
    
    
    {
      "code": 0,
      "data": {
        "created_at": 1798761600000,
        "task_id": "kling-task-1a2b3c4d5e6f",
        "task_result": {
          "videos": [
            {
              "duration": "5",
              "id": "kling-video-6f5e4d3c2b1a",
              "url": "https://example.invalid/kling/kling-v2-5-turbo/generated.mp4"
            }
          ]
        },
        "task_status": "succeed",
        "task_status_msg": "",
        "updated_at": 1798761840000
      },
      "message": "SUCCEED",
      "request_id": "9f2c1a04-7b6e-4d38-8a51-3c0e7d9b2f46"
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/kling/kling-v3-omni/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/kling/kling-v3-omni/code)

[Use Kling V2.6 with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/kling/kling-v2-6/code)[Use Kling V3 with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/kling/kling-v3/code)

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
