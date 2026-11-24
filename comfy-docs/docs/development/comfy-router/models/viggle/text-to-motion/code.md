---
url: https://docs.comfy.org/development/comfy-router/models/viggle/text-to-motion/code/
title: Use Text To Motion with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-24T18:44:25.058608+00:00
---

# Use Text To Motion with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/viggle/text-to-motion/code/

## On this page

Back to top

  * Quick start
  * Schema
    * Input
    * Output
  * Examples
    * Input
    * Output
  * Before you ship



Viggle

# Use Text To Motion with Comfy Router

Copy pageCopy page

Call viggle/text-to-motion through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `viggle/text-to-motion`, served by Comfy Router from Viggle. **Input:** Text · **Output:** 3D

## Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `viggle/text-to-motion` **Endpoint:** `POST https://api.comfy.org/v2/models/viggle/text-to-motion`

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
            "viggle/text-to-motion",
            {
                "duration_seconds": 5,
                "text": "a person waves with the right hand",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("viggle/text-to-motion", {
      duration_seconds: 5,
      text: "a person waves with the right hand",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/viggle/text-to-motion \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"duration_seconds\": 5, \"text\": \"a person waves with the right hand\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/viggle/text-to-motion/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "viggle/text-to-motion",
                {
                    "duration_seconds": 5,
                    "text": "a person waves with the right hand",
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
    const handle = await comfy.models.submit("viggle/text-to-motion", {
      duration_seconds: 5,
      text: "a person waves with the right hand",
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
    curl https://api.comfy.org/v2/models/viggle/text-to-motion/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"duration_seconds\": 5, \"text\": \"a person waves with the right hand\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/viggle/text-to-motion/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/viggle/text-to-motion/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## Schema

### Input

duration_seconds

number

Animation length in seconds, 3 to 60. Defaults to 5.

guidance_scale

number

How strongly the animation follows the text, 0 to 30. Defaults to 5.

name

string

Optional display label.

smooth

boolean

Smooths the generated animation. Defaults to true.

text

string

required

The movement to generate, 1 to 400 characters.

Generated from the schema Router serves at `GET /v2/models/viggle/text-to-motion/openapi.json`, the same document it validates a call against before the request reaches the provider.

### Output

credits_used

number

Viggle credits the job is charged, set once it is ready.Format: `double`

duration_seconds

number

Format: `double`

error

object

Viggle’s error object, set when the job failed.

error.code

string

error.message

string

error.request_id

string

error.retryable

boolean

fbx

object

Download URLs of one file format, one per rig.

fbx.metahuman_body_url

string

fbx.metahuman_url

string

fbx.mixamo_url

string

glb

object

Download URLs of one file format, one per rig.

glb.metahuman_body_url

string

glb.metahuman_url

string

glb.mixamo_url

string

id

string

status

string

Status: queued, processing, ready or failed.

## Examples

### Input
    
    
    {
      "duration_seconds": 5,
      "text": "a person waves with the right hand"
    }
    

### Output
    
    
    {
      "credits_used": 30,
      "duration_seconds": 5.04,
      "error": null,
      "fbx": {
        "metahuman_body_url": "https://example.invalid/viggle/metahuman_body.fbx",
        "metahuman_url": "https://example.invalid/viggle/metahuman.fbx",
        "mixamo_url": "https://example.invalid/viggle/mixamo.fbx"
      },
      "glb": {
        "metahuman_body_url": "https://example.invalid/viggle/metahuman_body.glb",
        "metahuman_url": "https://example.invalid/viggle/metahuman.glb",
        "mixamo_url": "https://example.invalid/viggle/mixamo.glb"
      },
      "id": "mot_extract_6d46ca9311eead39",
      "status": "ready"
    }
    

## Before you ship

The SDKs create an `Idempotency-Key` and reuse it for automatic retries. For manual retries, reuse the original key. Router can hold the connection for up to 10 minutes. When a request fails, Router sends an `X-Comfy-Error-Type` response header explaining why. A `422` means Router rejected the input before calling the provider, and a `413` means the request body was larger than Router accepts. Download generated assets promptly because [result URLs can expire](https://docs.comfy.org/development/comfy-router/reference#result-assets). Any size limit named in a field description above is the provider’s own bound on that field, quoted from the provider’s specification. Router applies a separate cap to the whole request body, which base64-encoded media counts against: see [request body size](https://docs.comfy.org/development/comfy-router/limitations#request-bodies-are-capped). This page documents one partner model called through Comfy Router. The same `comfy-sdk` / `@comfyorg/sdk` package also ships a second client, for running a whole ComfyUI workflow graph on Comfy Cloud: `Comfy(api_key=...)` / `new Comfy({ apiKey })`, with `client.workflows`, `client.assets` and `client.jobs`. See [Comfy SDKs](https://docs.comfy.org/development/api-development/sdks).

## Headers

Authentication, idempotency, request IDs, error buckets, retry pacing, spend limits.

## Using the Router API

Model discovery, validation errors, retries, and billing.

## Limitations

What Router does not do today, and what to use instead.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/viggle/text-to-motion/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/viggle/text-to-motion/code)

[Motion Capture](https://docs.comfy.org/development/comfy-router/models/viggle/motion-capture/code)[Video Remix](https://docs.comfy.org/development/comfy-router/models/viggle/video-remix/code)
