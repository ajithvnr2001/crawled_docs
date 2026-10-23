---
url: https://docs.comfy.org/development/comfy-router/models/ltx/ltx-2-5-pro/code/
title: Use LTX 2.5 Pro with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:17.824756+00:00
---

# Use LTX 2.5 Pro with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/ltx/ltx-2-5-pro/code/

## On this page

  * Quick start
  * Schema
    * Input
    * Output
  * Examples
    * Input
    * Output
  * Before you ship



LTX

# Use LTX 2.5 Pro with Comfy Router

Copy pageCopy page

Call ltx/ltx-2-5-pro through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `ltx/ltx-2-5-pro`, served by Comfy Router from LTX. **Input:** Text · **Output:** Video + Audio

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `ltx/ltx-2-5-pro` **Endpoint:** `POST https://api.comfy.org/v2/models/ltx/ltx-2-5-pro`

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
            "ltx/ltx-2-5-pro",
            {
                "duration": 2,
                "fps": 24,
                "generate_audio": False,
                "prompt": "A single red maple leaf resting on a plain white background.",
                "resolution": "1280x720",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("ltx/ltx-2-5-pro", {
      duration: 2,
      fps: 24,
      generate_audio: false,
      prompt: "A single red maple leaf resting on a plain white background.",
      resolution: "1280x720",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/ltx/ltx-2-5-pro \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"duration\": 2, \"fps\": 24, \"generate_audio\": false, \"prompt\": \"A single red maple leaf resting on a plain white background.\", \"resolution\": \"1280x720\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/ltx/ltx-2-5-pro/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "ltx/ltx-2-5-pro",
                {
                    "duration": 2,
                    "fps": 24,
                    "generate_audio": False,
                    "prompt": "A single red maple leaf resting on a plain white background.",
                    "resolution": "1280x720",
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
    const handle = await comfy.models.submit("ltx/ltx-2-5-pro", {
      duration: 2,
      fps: 24,
      generate_audio: false,
      prompt: "A single red maple leaf resting on a plain white background.",
      resolution: "1280x720",
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
    curl https://api.comfy.org/v2/models/ltx/ltx-2-5-pro/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"duration\": 2, \"fps\": 24, \"generate_audio\": false, \"prompt\": \"A single red maple leaf resting on a plain white background.\", \"resolution\": \"1280x720\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/ltx/ltx-2-5-pro/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/ltx/ltx-2-5-pro/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Schema

### 

​

Input

​

duration

integer

required

Video duration in seconds (maximum depends on resolution and frame rate)Possible values: `2`, `3`, `4`, `5`, `6`, `8`, `10`, `12`, `14`, `16`, `18`, `20`

​

fps

integer

default:"25"

Frame rate in frames per secondPossible values: `24`, `25`, `48`, `50`

​

generate_audio

boolean

default:"true"

Generate audio for the video

​

model

string

Model to use for generation. On the Comfy Router route `POST /v2/models/ltx/{model}` this field is supplied from the path and may be omitted. The spellings LTX serves on this operation — the set Comfy Router addresses as `ltx/<model>` — are ltx-2-5-fast and ltx-2-5-pro; they are written out here rather than constrained to an enum for the reason the comment above gives. Which resolutions each one admits is the `x-comfy-model-resolutions` matrix on the `resolution` property below.

​

prompt

string

required

Text prompt describing the desired video content

​

resolution

string

required

Output video resolution. The enum is the union over all models; the supported set is per model. Supported pairs: ltx-2-5-fast: 1280x720, 720x1280, 1920x1080, 1080x1920, 2560x1440, 1440x2560, 3840x2160, 2160x3840; ltx-2-5-pro: 1280x720, 720x1280, 1920x1080, 1080x1920. Other (model, resolution) pairs are not supported; the v2 routes reject them with 400. The same matrix is published machine-readably in this property’s x-comfy-model-resolutions extension.Possible values: `1280x720`, `720x1280`, `1920x1080`, `1080x1920`, `2560x1440`, `1440x2560`, `3840x2160`, `2160x3840`

Generated from the schema Router serves at `GET /v2/models/ltx/ltx-2-5-pro/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

completed_at

string

Job completion timestamp (ISO 8601)

​

created_at

string

Job creation timestamp (ISO 8601)

​

error

object

Present when status is failed

​

error.message

string

​

error.type

string

​

id

string

Unique job identifier

​

result

object

Present when status is completed; output URLs expire 24 hours after completion

​

result.video_url

string

URL of the generated video

​

status

string

Job status (pending, processing, completed, failed)

## 

​

Examples

### 

​

Input
    
    
    {
      "duration": 2,
      "fps": 24,
      "generate_audio": false,
      "prompt": "A single red maple leaf resting on a plain white background.",
      "resolution": "1280x720"
    }
    

### 

​

Output
    
    
    {
      "completed_at": "2026-01-01T00:02:10Z",
      "created_at": "2026-01-01T00:00:00Z",
      "id": "3f7a1b28-5c0d-4e91-8a6f-1b2c3d4e5f60",
      "result": {
        "video_url": "https://example.invalid/ltx/generated.mp4"
      },
      "status": "completed"
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/ltx/ltx-2-5-pro/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/ltx/ltx-2-5-pro/code)

[Use LTX 2.5 Fast with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/ltx/ltx-2-5-fast/code)[Use Photon 1 with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/luma/photon-1/code)

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
