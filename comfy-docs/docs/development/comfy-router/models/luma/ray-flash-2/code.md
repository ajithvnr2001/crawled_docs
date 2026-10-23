---
url: https://docs.comfy.org/development/comfy-router/models/luma/ray-flash-2/code/
title: Use Ray Flash 2 with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:18.591450+00:00
---

# Use Ray Flash 2 with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/luma/ray-flash-2/code/

## On this page

  * Quick start
  * Schema
    * Input
    * Output
  * Examples
    * Input
    * Output
  * Before you ship



Luma

# Use Ray Flash 2 with Comfy Router

Copy pageCopy page

Call luma/ray-flash-2 through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `luma/ray-flash-2`, served by Comfy Router from Luma. **Input:** Text, Image · **Output:** Video

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `luma/ray-flash-2` **Endpoint:** `POST https://api.comfy.org/v2/models/luma/ray-flash-2`

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
            "luma/ray-flash-2",
            {
                "aspect_ratio": "16:9",
                "duration": "5s",
                "prompt": "a single red maple leaf resting on a plain white background",
                "resolution": "540p",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("luma/ray-flash-2", {
      aspect_ratio: "16:9",
      duration: "5s",
      prompt: "a single red maple leaf resting on a plain white background",
      resolution: "540p",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/luma/ray-flash-2 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"aspect_ratio\": \"16:9\", \"duration\": \"5s\", \"prompt\": \"a single red maple leaf resting on a plain white background\", \"resolution\": \"540p\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/luma/ray-flash-2/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "luma/ray-flash-2",
                {
                    "aspect_ratio": "16:9",
                    "duration": "5s",
                    "prompt": "a single red maple leaf resting on a plain white background",
                    "resolution": "540p",
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
    const handle = await comfy.models.submit("luma/ray-flash-2", {
      aspect_ratio: "16:9",
      duration: "5s",
      prompt: "a single red maple leaf resting on a plain white background",
      resolution: "540p",
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
    curl https://api.comfy.org/v2/models/luma/ray-flash-2/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"aspect_ratio\": \"16:9\", \"duration\": \"5s\", \"prompt\": \"a single red maple leaf resting on a plain white background\", \"resolution\": \"540p\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/luma/ray-flash-2/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/luma/ray-flash-2/requests/$REQUEST_ID \
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

required

The aspect ratio of the generationPossible values: `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `21:9`, `9:21`

​

callback_url

string (uri)

The callback URL of the generation, a POST request with Generation object will be sent to the callback URL when the generation is dreaming, completed, or failedFormat: `uri`

​

duration

`5s`, `9s` | string

required

​

generation_type

string

default:"\"video\""

Possible values: `video`

​

keyframes

object

The keyframes of the generation

​

keyframes.frame0

object

A keyframe can be either a Generation reference, an Image, or a Video

​

keyframes.frame1

object

A keyframe can be either a Generation reference, an Image, or a Video

​

loop

boolean

Whether to loop the video

​

model

string

The video model used for the generation. On the Comfy Router route `POST /v2/models/luma/{model}` this field is supplied from the path and MUST NOT be sent; on the v1 `POST /proxy/luma/generations` route it is required and constrained to the LumaVideoModel enum (`ray-2`, `ray-flash-2`).

​

prompt

string

required

The prompt of the generation

​

resolution

`540p`, `720p`, `1080p`, `4k` | string

required

Generated from the schema Router serves at `GET /v2/models/luma/ray-flash-2/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

assets

object

The assets of the generation

​

assets.image

string (uri)

The URL of the imageFormat: `uri`

​

assets.progress_video

string (uri)

The URL of the progress videoFormat: `uri`

​

assets.video

string (uri)

The URL of the videoFormat: `uri`

​

created_at

string (date-time)

The date and time when the generation was createdFormat: `date-time`

​

failure_reason

string

The reason for the state of the generation

​

generation_type

string

Possible values: `video`, `image`

​

id

string (uuid)

The ID of the generationFormat: `uuid`

​

model

string

The model used for the generation

​

request

object

The request of the generation

​

state

string

The state of the generationPossible values: `queued`, `dreaming`, `completed`, `failed`

## 

​

Examples

### 

​

Input
    
    
    {
      "aspect_ratio": "16:9",
      "duration": "5s",
      "prompt": "a single red maple leaf resting on a plain white background",
      "resolution": "540p"
    }
    

### 

​

Output
    
    
    {
      "assets": {
        "video": "https://example.invalid/luma/ray-flash-2/generated.mp4"
      },
      "created_at": "2027-01-01T00:00:00Z",
      "generation_type": "video",
      "id": "8c41d0b6-2e7a-4f35-b1d8-9a0e6f3c2b71",
      "model": "ray-flash-2",
      "state": "completed"
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/luma/ray-flash-2/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/luma/ray-flash-2/code)

[Use Ray 2 with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/luma/ray-2/code)[Use Uni 1 Max with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/luma_2/uni-1-max/code)

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
