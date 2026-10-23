---
url: https://docs.comfy.org/development/comfy-router/models/bria/video-edit-remove-background/code/
title: Use Video Edit Remove Background with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-19T14:35:00.006399+00:00
---

# Use Video Edit Remove Background with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/bria/video-edit-remove-background/code/

## On this page

  * Quick start
  * Schema
    * Input
    * Output
  * Examples
    * Input
    * Output
  * Before you ship



Bria

# Use Video Edit Remove Background with Comfy Router

Copy pageCopy page

Call bria/video-edit-remove-background through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `bria/video-edit-remove-background`, served by Comfy Router from Bria. **Input:** Video · **Output:** Video

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `bria/video-edit-remove-background` **Endpoint:** `POST https://api.comfy.org/v2/models/bria/video-edit-remove-background`

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
            "bria/video-edit-remove-background",
            {
                "background_color": "Transparent",
                "output_container_and_codec": "webm_vp9",
                "video": "https://example.com/input.mp4",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("bria/video-edit-remove-background", {
      background_color: "Transparent",
      output_container_and_codec: "webm_vp9",
      video: "https://example.com/input.mp4",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/bria/video-edit-remove-background \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"background_color\": \"Transparent\", \"output_container_and_codec\": \"webm_vp9\", \"video\": \"https://example.com/input.mp4\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/bria/video-edit-remove-background/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "bria/video-edit-remove-background",
                {
                    "background_color": "Transparent",
                    "output_container_and_codec": "webm_vp9",
                    "video": "https://example.com/input.mp4",
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
    const handle = await comfy.models.submit("bria/video-edit-remove-background", {
      background_color: "Transparent",
      output_container_and_codec: "webm_vp9",
      video: "https://example.com/input.mp4",
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
    curl https://api.comfy.org/v2/models/bria/video-edit-remove-background/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"background_color\": \"Transparent\", \"output_container_and_codec\": \"webm_vp9\", \"video\": \"https://example.com/input.mp4\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/bria/video-edit-remove-background/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/bria/video-edit-remove-background/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Schema

### 

​

Input

​

background_color

string

Background color for the output video. If Transparent, the output codec must support alpha.Possible values: `Transparent`, `Black`, `White`, `Gray`, `Red`, `Green`, `Blue`, `Yellow`, `Cyan`, `Magenta`, `Orange`

​

output_container_and_codec

string

Output container and codec preset.Possible values: `mp4_h264`, `mp4_h265`, `webm_vp9`, `mov_h265`, `mov_proresks`, `mkv_h264`, `mkv_h265`, `mkv_vp9`, `gif`

​

preserve_audio

boolean

Whether to preserve audio from the input video.

​

video

string

required

Publicly accessible URL of the input video. Input resolution supported up to 16000x16000 (16K). Max duration 60 seconds.

Generated from the schema Router serves at `GET /v2/models/bria/video-edit-remove-background/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

error

object

Error object (only present when status is ERROR)

​

error.code

integer

Error code.

​

error.details

string

Additional error details.

​

error.message

string

Error message.

​

request_id

string

Unique identifier for the request.

​

result

object

Result object (only present when status is COMPLETED)

​

result.image_url

string

URL of the generated/edited image.

​

result.prompt

string

Original prompt.

​

result.refined_prompt

string

Refined version of the prompt, or null on a COMPLETED generation Bria did not refine. Nullable because the key is PRESENT carrying null rather than omitted; observed live on bria/image-edit-gen-fill.

​

result.seed

integer

Seed used for generation.

​

result.structured_instruction

string

The structured instruction, a JSON document serialized as a string, that `/v2/structured_instruction/generate` returns. That operation fills neither URL.

​

result.structured_prompt

string

The detailed JSON structured prompt.

​

result.video_url

string

URL of the generated video.

​

status

string

Current status of the request.Possible values: `IN_PROGRESS`, `COMPLETED`, `ERROR`, `UNKNOWN`

## 

​

Examples

### 

​

Input
    
    
    {
      "background_color": "Transparent",
      "output_container_and_codec": "webm_vp9",
      "video": "https://example.com/input.mp4"
    }
    

### 

​

Output
    
    
    {
      "request_id": "0b3f9d7e-2c41-4a8b-9f10-6d5c8e2a4b71",
      "result": {
        "video_url": "https://example.invalid/bria/video-edit-remove-background/generated.mp4"
      },
      "status": "COMPLETED"
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/bria/video-edit-remove-background/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/bria/video-edit-remove-background/code)

[Use Video Edit Green Screen with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/bria/video-edit-green-screen/code)[Use Video Edit Replace Background with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/bria/video-edit-replace-background/code)

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
