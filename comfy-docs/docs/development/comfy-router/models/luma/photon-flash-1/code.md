---
url: https://docs.comfy.org/development/comfy-router/models/luma/photon-flash-1/code/
title: Use Photon Flash 1 with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:18.126782+00:00
---

# Use Photon Flash 1 with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/luma/photon-flash-1/code/

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

# Use Photon Flash 1 with Comfy Router

Copy pageCopy page

Call luma/photon-flash-1 through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `luma/photon-flash-1`, served by Comfy Router from Luma. **Input:** Text · **Output:** Image

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `luma/photon-flash-1` **Endpoint:** `POST https://api.comfy.org/v2/models/luma/photon-flash-1`

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
            "luma/photon-flash-1",
            {
                "aspect_ratio": "1:1",
                "prompt": "a red circle on a plain white background",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("luma/photon-flash-1", {
      aspect_ratio: "1:1",
      prompt: "a red circle on a plain white background",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/luma/photon-flash-1 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"aspect_ratio\": \"1:1\", \"prompt\": \"a red circle on a plain white background\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/luma/photon-flash-1/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "luma/photon-flash-1",
                {
                    "aspect_ratio": "1:1",
                    "prompt": "a red circle on a plain white background",
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
    const handle = await comfy.models.submit("luma/photon-flash-1", {
      aspect_ratio: "1:1",
      prompt: "a red circle on a plain white background",
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
    curl https://api.comfy.org/v2/models/luma/photon-flash-1/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"aspect_ratio\": \"1:1\", \"prompt\": \"a red circle on a plain white background\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/luma/photon-flash-1/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/luma/photon-flash-1/requests/$REQUEST_ID \
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

The aspect ratio of the generationPossible values: `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `21:9`, `9:21`

​

callback_url

string (uri)

The callback URL for the generationFormat: `uri`

​

character_ref

object

​

character_ref.identity0

object

The image identity object

​

character_ref.identity0.images

string (uri)[]

The URLs of the image identity

​

generation_type

string

default:"\"image\""

Possible values: `image`

​

image_ref

object[]

The image reference object

​

image_ref[].url

string (uri)

The URL of the image referenceFormat: `uri`

​

image_ref[].weight

number

The weight of the image reference

​

model

string

The image model used for the generation. On the Comfy Router route `POST /v2/models/luma/{model}` this field is supplied from the path and MUST NOT be sent; on the v1 `POST /proxy/luma/generations/image` route it is constrained to the LumaImageModel enum (`photon-1`, `photon-flash-1`), which the Rewrite enforces by refusing an omitted or unknown model.

​

modify_image_ref

object

The modify image reference object

​

modify_image_ref.url

string (uri)

The URL of the image referenceFormat: `uri`

​

modify_image_ref.weight

number

The weight of the modify image reference

​

prompt

string

The prompt of the generation

​

style_ref

object[]

The image reference object

​

style_ref[].url

string (uri)

The URL of the image referenceFormat: `uri`

​

style_ref[].weight

number

The weight of the image reference

Generated from the schema Router serves at `GET /v2/models/luma/photon-flash-1/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

assets

object

The assets of an image generation. `image` is the result; `video` and `progress_video` belong to the Dream Machine VIDEO operation, which shares this status route, and Luma sends them here as explicit nulls.

​

assets.image

string (uri)

The URL of the generated image — the leaf a `luma/photon-*` generation fills. Null until the generation reaches `completed`.Format: `uri`

​

assets.progress_video

string (uri)

Always null on an image generation; it is the in-flight preview Luma publishes while a VIDEO generation runs.Format: `uri`

​

assets.video

string (uri)

Always null on an image generation; the `luma/ray-*` video models fill it instead.Format: `uri`

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

The type of the generation — always `image` on this operationPossible values: `image`

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

The image generation request, echoed back inside the terminal document. Luma serialises every field of its request model, writing an explicit `null` into each one the caller did not set, so read a field’s presence from its VALUE rather than from the key.

​

request.aspect_ratio

string

default:"\"16:9\""

The aspect ratio of the generationPossible values: `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `21:9`, `9:21`

​

request.callback_url

string (uri)

The callback URL for the generationFormat: `uri`

​

request.character_ref

object

​

request.character_ref.identity0

object

An image identity as it comes BACK inside the terminal document. Same shape as `LumaImageIdentity`, with its members nullable for the reason `LumaImageRefEcho` gives.

​

request.character_ref.identity0.images

string (uri)[]

The URLs of the image identity

​

request.generation_type

string

Always `image` when set, echoing the operation. Null when the caller did not send one, for the reason this whole echo object exists.

​

request.image_ref

object[]

An image reference as it comes BACK inside the terminal document. Same shape as `LumaImageRef`, with each member nullable because Luma echoes an unset one as an explicit `null` rather than omitting it.

​

request.image_ref[].url

string (uri)

The URL of the image referenceFormat: `uri`

​

request.image_ref[].weight

number

The weight of the image reference

​

request.model

string

default:"\"photon-1\""

The image model used for the generationPossible values: `photon-1`, `photon-flash-1`

​

request.modify_image_ref

object

A modify-image reference as it comes BACK inside the terminal document. Same shape as `LumaModifyImageRef`, with its members nullable for the reason `LumaImageRefEcho` gives.

​

request.modify_image_ref.url

string (uri)

The URL of the image referenceFormat: `uri`

​

request.modify_image_ref.weight

number

The weight of the modify image reference

​

request.prompt

string

The prompt of the generation

​

request.style_ref

object[]

An image reference as it comes BACK inside the terminal document. Same shape as `LumaImageRef`, with each member nullable because Luma echoes an unset one as an explicit `null` rather than omitting it.

​

request.style_ref[].url

string (uri)

The URL of the image referenceFormat: `uri`

​

request.style_ref[].weight

number

The weight of the image reference

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
      "aspect_ratio": "1:1",
      "prompt": "a red circle on a plain white background"
    }
    

### 

​

Output
    
    
    {
      "assets": {
        "image": "https://example.invalid/luma/photon-flash-1/generated.png",
        "progress_video": null,
        "video": null
      },
      "created_at": "2027-01-01T00:00:00Z",
      "failure_reason": null,
      "generation_type": "image",
      "id": "a1c73f26-08d5-4e69-b7a2-3c4d5e6f7a80",
      "model": "photon-flash-1",
      "request": {
        "aspect_ratio": "1:1",
        "callback_url": null,
        "character_ref": null,
        "generation_type": "image",
        "image_ref": null,
        "model": "photon-flash-1",
        "modify_image_ref": null,
        "prompt": "a red circle on a plain white background",
        "style_ref": null
      },
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/luma/photon-flash-1/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/luma/photon-flash-1/code)

[Use Photon 1 with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/luma/photon-1/code)[Use Ray 2 with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/luma/ray-2/code)

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
