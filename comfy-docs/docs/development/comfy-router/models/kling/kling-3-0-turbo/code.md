---
url: https://docs.comfy.org/development/comfy-router/models/kling/kling-3-0-turbo/code/
title: Use Kling 3.0 Turbo with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:13.545554+00:00
---

# Use Kling 3.0 Turbo with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/kling/kling-3-0-turbo/code/

## On this page

  * Quick start
  * Serving providers
  * Schema
    * Input
    * Output
  * Examples
    * Input
    * Output
  * Before you ship



Kling

# Use Kling 3.0 Turbo with Comfy Router

Copy pageCopy page

Call kling/kling-3.0-turbo through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `kling/kling-3.0-turbo`, served by Comfy Router from Kling. **Input:** Text · **Output:** Video

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `kling/kling-3.0-turbo` **Endpoint:** `POST https://api.comfy.org/v2/models/kling/kling-3.0-turbo`

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
            "kling/kling-3.0-turbo",
            {
                "prompt": "A neon-lit alley in the rain, slow dolly forward.",
                "settings": {
                    "aspect_ratio": "16:9",
                    "duration": 5,
                    "resolution": "1080p",
                },
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("kling/kling-3.0-turbo", {
      prompt: "A neon-lit alley in the rain, slow dolly forward.",
      settings: {
        aspect_ratio: "16:9",
        duration: 5,
        resolution: "1080p",
      },
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/kling/kling-3.0-turbo \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"A neon-lit alley in the rain, slow dolly forward.\", \"settings\": {\"aspect_ratio\":\"16:9\",\"duration\":5,\"resolution\":\"1080p\"}}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/kling/kling-3.0-turbo/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "kling/kling-3.0-turbo",
                {
                    "prompt": "A neon-lit alley in the rain, slow dolly forward.",
                    "settings": {
                        "aspect_ratio": "16:9",
                        "duration": 5,
                        "resolution": "1080p",
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
    const handle = await comfy.models.submit("kling/kling-3.0-turbo", {
      prompt: "A neon-lit alley in the rain, slow dolly forward.",
      settings: {
        aspect_ratio: "16:9",
        duration: 5,
        resolution: "1080p",
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
    curl https://api.comfy.org/v2/models/kling/kling-3.0-turbo/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"A neon-lit alley in the rain, slow dolly forward.\", \"settings\": {\"aspect_ratio\":\"16:9\",\"duration\":5,\"resolution\":\"1080p\"}}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/kling/kling-3.0-turbo/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/kling/kling-3.0-turbo/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Serving providers

This model is served by Comfy Router directly unless the request names another provider. The providers below serve it too, on the same endpoint and with the same model ID, selected with the `model_provider` query parameter.

  * **Comfy** (default): `POST https://api.comfy.org/v2/models/kling/kling-3.0-turbo`
  * **Higgsfield** , as `higgsfield/higgsfield-kling-3-turbo`: `POST https://api.comfy.org/v2/models/kling/kling-3.0-turbo?model_provider=higgsfield`

`strict_mode` defaults to false, so Router translates the native request body documented on this page into the provider’s own schema and translates the response back. See [`model_provider`, `strict_mode` and `fallback_provider`](https://docs.comfy.org/development/comfy-router/reference#post-v2modelsprovidermodel) in the API reference, and [Serving providers](https://docs.comfy.org/development/comfy-router/providers) for every model routed this way.

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

duration

string

default:"\"5\""

Video length in secondsPossible values: `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`

​

options

object

General configuration such as callback address and watermark options.

​

options.callback_url

string

Callback notification URL for task results. The server notifies when the task status changes.

​

options.external_task_id

string

Customized Task ID. Does not overwrite the system-generated task ID but can be used for queries. Must be unique within a single user account.

​

options.watermark_info

object

Whether to generate watermarked results simultaneously. Custom watermarks are not supported.

​

options.watermark_info.enabled

boolean

true means generate watermarked result, false means do not generate. Default false.

​

prompt

string

required

Prompt that may include both positive and negative descriptions. Recommended length under 2500 characters. Multi-shot videos use the format “shot n, m, words; shot n, m, words;”.

​

settings

object

Output configuration such as resolution, aspect ratio and duration.

​

settings.aspect_ratio

string

Aspect ratio (width:height) of the generated frames. One of “16:9”, “9:16” or “1:1”. Default “16:9”.Possible values: `16:9`, `9:16`, `1:1`

​

settings.duration

integer

Video length in seconds. Supported values 3 through 15. Default 5.Range: `3` to `15`

​

settings.resolution

string

Clarity of the generated video. One of “720p” or “1080p”. Default “720p”.Possible values: `720p`, `1080p`

Generated from the schema Router serves at `GET /v2/models/kling/kling-3.0-turbo/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

code

integer

Error code. 0 indicates success.

​

data

object[]

Tasks matching the query.

​

data[].billing

object[]

Billing details for the task.

​

data[].billing[].amount

string

Consumption amount, accurate to two decimal places.

​

data[].billing[].charge_type

string

Consumption account type. “cash” for balance, “unit” for a resource package.

​

data[].billing[].package_type

string

Consumable resource bundle type (only present when charge_type is “unit”). One of “video”, “image” or “audio”.

​

data[].create_time

integer

Task creation time. Unix timestamp in milliseconds.Format: `int64`

​

data[].external_id

string

The custom task ID for this task, if any.

​

data[].id

string

The task ID.

​

data[].message

string

Task status information, displaying the failure reason when the task fails.

​

data[].outputs

object[]

Generated outputs for the task.

​

data[].outputs[].duration

string

Duration of the generated video in seconds.

​

data[].outputs[].group_id

string

Grouping marker, present only for grouped images.

​

data[].outputs[].id

string

Output ID generated by the system.

​

data[].outputs[].mp3_duration

string

Duration of the generated MP3 audio in seconds.

​

data[].outputs[].mp3_url

string

MP3 URL of the generated audio (hotlink-protected).

​

data[].outputs[].name

string

Name of the generated material.

​

data[].outputs[].owned_by

string

Source of the material. “kling” denotes the official library; numbers are creator IDs.

​

data[].outputs[].status

string

Status of the material. One of “succeeded” or “deleted”.

​

data[].outputs[].type

string

Output content type. One of “video”, “image”, “audio”, “voice” or “element”.

​

data[].outputs[].url

string

URL of the generated result (hotlink-protected). Cleared after 30 days.

​

data[].outputs[].watermark_url

string

URL of the watermarked result (hotlink-protected).

​

data[].outputs[].wav_duration

string

Duration of the generated WAV audio in seconds.

​

data[].outputs[].wav_url

string

WAV URL of the generated audio (hotlink-protected).

​

data[].status

string

Task status. One of “submitted”, “processing”, “succeeded” or “failed”.

​

data[].update_time

integer

Task update time. Unix timestamp in milliseconds.Format: `int64`

​

message

string

Error message.

​

request_id

string

Request ID generated by the system.

## 

​

Examples

### 

​

Input
    
    
    {
      "prompt": "A neon-lit alley in the rain, slow dolly forward.",
      "settings": {
        "aspect_ratio": "16:9",
        "duration": 5,
        "resolution": "1080p"
      }
    }
    

### 

​

Output
    
    
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
              "url": "https://example.invalid/kling/kling-3.0-turbo/generated.mp4"
            }
          ],
          "status": "succeeded",
          "update_time": 1798761820000
        }
      ],
      "message": "SUCCEED",
      "request_id": "3d7e5c91-0b42-4f68-9a13-8e2c6d4b0a75"
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/kling/kling-3-0-turbo/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/kling/kling-3-0-turbo/code)

[Use P Image Ideogram with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/ideogram/p-image-ideogram/code)[Use Kling Image O1 with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/kling/kling-image-o1/code)

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
