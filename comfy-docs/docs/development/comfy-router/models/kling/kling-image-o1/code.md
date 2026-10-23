---
url: https://docs.comfy.org/development/comfy-router/models/kling/kling-image-o1/code/
title: Use Kling Image O1 with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:12.623046+00:00
---

# Use Kling Image O1 with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/kling/kling-image-o1/code/

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

# Use Kling Image O1 with Comfy Router

Copy pageCopy page

Call kling/kling-image-o1 through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `kling/kling-image-o1`, served by Comfy Router from Kling. **Input:** Text, Image · **Output:** Image

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `kling/kling-image-o1` **Endpoint:** `POST https://api.comfy.org/v2/models/kling/kling-image-o1`

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
            "kling/kling-image-o1",
            {
                "aspect_ratio": "1:1",
                "n": 1,
                "prompt": "A watercolour koi pond at dawn, soft light.",
                "resolution": "1k",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("kling/kling-image-o1", {
      aspect_ratio: "1:1",
      n: 1,
      prompt: "A watercolour koi pond at dawn, soft light.",
      resolution: "1k",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/kling/kling-image-o1 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"aspect_ratio\": \"1:1\", \"n\": 1, \"prompt\": \"A watercolour koi pond at dawn, soft light.\", \"resolution\": \"1k\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/kling/kling-image-o1/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "kling/kling-image-o1",
                {
                    "aspect_ratio": "1:1",
                    "n": 1,
                    "prompt": "A watercolour koi pond at dawn, soft light.",
                    "resolution": "1k",
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
    const handle = await comfy.models.submit("kling/kling-image-o1", {
      aspect_ratio: "1:1",
      n: 1,
      prompt: "A watercolour koi pond at dawn, soft light.",
      resolution: "1k",
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
    curl https://api.comfy.org/v2/models/kling/kling-image-o1/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"aspect_ratio\": \"1:1\", \"n\": 1, \"prompt\": \"A watercolour koi pond at dawn, soft light.\", \"resolution\": \"1k\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/kling/kling-image-o1/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/kling/kling-image-o1/requests/$REQUEST_ID \
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

default:"\"auto\""

Aspect ratio of the generated images (width:height). auto is to intelligently generate images based on incoming content.Possible values: `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `3:2`, `2:3`, `21:9`, `auto`

​

callback_url

string (uri)

The callback notification address for the result of this task. If configured, the server will actively notify when the task status changes.Format: `uri`

​

element_list

object[]

Reference Element List based on element ID configuration. The sum of reference elements and reference images shall not exceed 10.

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

Reference Image List. Supports inputting image Base64 encoding or image URL (ensure accessibility). Supported formats include .jpg/.jpeg/.png. File size cannot exceed 10MB. Width and height dimensions shall not be less than 300px, aspect ratio between 1:2.5 ~ 2.5:1. The sum of reference elements and reference images shall not exceed 10.

​

image_list[].image

string

required

Image Base64 encoding or image URL (ensure accessibility)

​

model_name

string

Model name. Omit it or send null when using Comfy Router; the model is selected by the request path. A supplied name must match that path.

​

n

integer

default:"1"

Number of generated images. Value range [1,9].Range: `1` to `9`

​

prompt

string

required

Text prompt words, which can include positive and negative descriptions. Must not exceed 2,500 characters. The Omni model can achieve various capabilities through Prompt with elements and images. Specify an image in the format of <<<>>>, such as <<<image_1>>>.

​

resolution

string

default:"\"1k\""

Image generation resolution. 1k is 1K standard, 2k is 2K high-res, 4k is 4K high-res.Possible values: `1k`, `2k`, `4k`

​

result_type

string

default:"\"single\""

Control whether to generate a single image or a series of images.Possible values: `single`, `series`

​

series_amount

integer

default:"4"

Number of images in a series. Value range [2,9].Range: `2` to `9`

Generated from the schema Router serves at `GET /v2/models/kling/kling-image-o1/openapi.json`, the same document it validates a call against before the request reaches the provider.

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

Customer-defined task ID

​

data.task_result

object

​

data.task_result.images

object[]

​

data.task_result.images[].index

integer

Image Number (0-9)

​

data.task_result.images[].url

string (uri)

URL for generated imageFormat: `uri`

​

data.task_result.result_type

string

Whether the result is a single image or a series of imagesPossible values: `single`, `series`

​

data.task_result.series_images

object[]

Series images result list

​

data.task_result.series_images[].index

integer

Series-image sequence number

​

data.task_result.series_images[].url

string (uri)

URL for generated imageFormat: `uri`

​

data.task_status

string

Task StatusPossible values: `submitted`, `processing`, `succeed`, `failed`

​

data.task_status_msg

string

Task status information, displaying the failure reason when the task fails (such as triggering the content risk control of the platform, etc.)

​

data.updated_at

integer

Task update time, Unix timestamp in milliseconds

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
      "aspect_ratio": "1:1",
      "n": 1,
      "prompt": "A watercolour koi pond at dawn, soft light.",
      "resolution": "1k"
    }
    

### 

​

Output
    
    
    {
      "code": 0,
      "data": {
        "created_at": 1798761600000,
        "task_id": "kling-image-task-3c4d5e6f7a8b",
        "task_result": {
          "images": [
            {
              "index": 0,
              "url": "https://example.invalid/kling/kling-image-o1/generated.png"
            }
          ],
          "result_type": "single"
        },
        "task_status": "succeed",
        "task_status_msg": "",
        "updated_at": 1798761660000
      },
      "message": "SUCCEED",
      "request_id": "6a4b2c80-1e93-4d57-b8f2-05c7e9a3d146"
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/kling/kling-image-o1/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/kling/kling-image-o1/code)

[Use Kling 3.0 Turbo with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/kling/kling-3-0-turbo/code)[Use Kling V2.5 Turbo with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/kling/kling-v2-5-turbo/code)

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
