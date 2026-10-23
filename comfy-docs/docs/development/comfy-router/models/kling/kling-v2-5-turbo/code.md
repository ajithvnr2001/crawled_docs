---
url: https://docs.comfy.org/development/comfy-router/models/kling/kling-v2-5-turbo/code/
title: Use Kling V2.5 Turbo with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:13.854531+00:00
---

# Use Kling V2.5 Turbo with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/kling/kling-v2-5-turbo/code/

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

# Use Kling V2.5 Turbo with Comfy Router

Copy pageCopy page

Call kling/kling-v2-5-turbo through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `kling/kling-v2-5-turbo`, served by Comfy Router from Kling. **Input:** Text · **Output:** Video

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `kling/kling-v2-5-turbo` **Endpoint:** `POST https://api.comfy.org/v2/models/kling/kling-v2-5-turbo`

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
            "kling/kling-v2-5-turbo",
            {
                "aspect_ratio": "16:9",
                "duration": "5",
                "mode": "std",
                "prompt": "A red fox trotting through falling snow, cinematic lighting.",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("kling/kling-v2-5-turbo", {
      aspect_ratio: "16:9",
      duration: "5",
      mode: "std",
      prompt: "A red fox trotting through falling snow, cinematic lighting.",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/kling/kling-v2-5-turbo \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"aspect_ratio\": \"16:9\", \"duration\": \"5\", \"mode\": \"std\", \"prompt\": \"A red fox trotting through falling snow, cinematic lighting.\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/kling/kling-v2-5-turbo/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "kling/kling-v2-5-turbo",
                {
                    "aspect_ratio": "16:9",
                    "duration": "5",
                    "mode": "std",
                    "prompt": "A red fox trotting through falling snow, cinematic lighting.",
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
    const handle = await comfy.models.submit("kling/kling-v2-5-turbo", {
      aspect_ratio: "16:9",
      duration: "5",
      mode: "std",
      prompt: "A red fox trotting through falling snow, cinematic lighting.",
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
    curl https://api.comfy.org/v2/models/kling/kling-v2-5-turbo/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"aspect_ratio\": \"16:9\", \"duration\": \"5\", \"mode\": \"std\", \"prompt\": \"A red fox trotting through falling snow, cinematic lighting.\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/kling/kling-v2-5-turbo/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/kling/kling-v2-5-turbo/requests/$REQUEST_ID \
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

default:"\"16:9\""

Video aspect ratioPossible values: `16:9`, `9:16`, `1:1`

​

callback_url

string (uri)

The callback notification addressFormat: `uri`

​

camera_control

object

​

camera_control.config

object

​

camera_control.config.horizontal

number

Controls camera’s movement along horizontal axis (x-axis). Negative indicates left, positive indicates right.Range: `-10` to `10`

​

camera_control.config.pan

number

Controls camera’s rotation in vertical plane (x-axis). Negative indicates downward rotation, positive indicates upward rotation.Range: `-10` to `10`

​

camera_control.config.roll

number

Controls camera’s rolling amount (z-axis). Negative indicates counterclockwise, positive indicates clockwise.Range: `-10` to `10`

​

camera_control.config.tilt

number

Controls camera’s rotation in horizontal plane (y-axis). Negative indicates left rotation, positive indicates right rotation.Range: `-10` to `10`

​

camera_control.config.vertical

number

Controls camera’s movement along vertical axis (y-axis). Negative indicates downward, positive indicates upward.Range: `-10` to `10`

​

camera_control.config.zoom

number

Controls change in camera’s focal length. Negative indicates narrower field of view, positive indicates wider field of view.Range: `-10` to `10`

​

camera_control.type

string

Predefined camera movements type. simple: Customizable camera movement. down_back: Camera descends and moves backward. forward_up: Camera moves forward and tilts up. right_turn_forward: Rotate right and move forward. left_turn_forward: Rotate left and move forward.Possible values: `simple`, `down_back`, `forward_up`, `right_turn_forward`, `left_turn_forward`

​

cfg_scale

number

default:"0.5"

Flexibility in video generation. The higher the value, the lower the model’s degree of flexibility, and the stronger the relevance to the user’s prompt.Range: `0` to `1`Format: `float`

​

duration

string

default:"\"5\""

Video length in secondsPossible values: `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`

​

external_task_id

string

Customized Task ID

​

mode

string

default:"\"std\""

Video generation mode. std: Standard Mode, which is cost-effective. pro: Professional Mode, generates videos with longer duration but higher quality output.Possible values: `std`, `pro`

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

negative_prompt

string

Negative text prompt. It is recommended to supplement negative prompt information through negative sentences directly within positive prompts.

​

prompt

string

Positive text prompt. Use <<<voice_1>>> to specify a voice matching the voice_list parameter order. A task can reference up to 2 tones. When specifying a tone, the sound parameter value must be on.

​

shot_type

string

Storyboard method. Required when the multi_shot parameter is set to true.Possible values: `customize`, `intelligence`

​

sound

string

default:"\"off\""

Whether to generate sound simultaneously when generating videos. Only V2.6 and subsequent versions of the model support this parameter.Possible values: `on`, `off`

​

voice_list

object[]

List of voices referenced when generating videos. Supports up to 2 voices; reference them in `prompt` as <<<voice_1>>> and <<<voice_2>>> in list order. Requires `sound` set to “on”, which only V2.6 and subsequent versions of the model support; on an earlier model, or with `sound` left at its “off” default, voices are not applied.

​

voice_list[].voice_id

string

required

Voice ID returned through the voice customization API or a system preset voice ID.

​

watermark_info

object

Whether to generate watermarked results simultaneously. Custom watermark is not supported at this time.

​

watermark_info.enabled

boolean

true means generate watermark, false means do not generate.

Generated from the schema Router serves at `GET /v2/models/kling/kling-v2-5-turbo/openapi.json`, the same document it validates a call against before the request reaches the provider.

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
      "mode": "std",
      "prompt": "A red fox trotting through falling snow, cinematic lighting."
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/kling/kling-v2-5-turbo/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/kling/kling-v2-5-turbo/code)

[Use Kling Image O1 with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/kling/kling-image-o1/code)[Use Kling V2.6 with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/kling/kling-v2-6/code)

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
