---
url: https://docs.comfy.org/development/comfy-router/models/viggle/jst-2-scene-view/code/
title: Use Jst 2 Scene View with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-24T18:44:25.657467+00:00
---

# Use Jst 2 Scene View with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/viggle/jst-2-scene-view/code/

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

# Use Jst 2 Scene View with Comfy Router

Copy pageCopy page

Call viggle/jst-2-scene-view through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `viggle/jst-2-scene-view`, served by Comfy Router from Viggle. **Input:** 3D · **Output:** Image

## Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `viggle/jst-2-scene-view` **Endpoint:** `POST https://api.comfy.org/v2/models/viggle/jst-2-scene-view`

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
            "viggle/jst-2-scene-view",
            {
                "projection": "perspective",
                "referenceBatchIds": ["3f0a6c1e-8d2b-4b7a-9e5c-1a2b3c4d5e6f"],
                "sessionId": "replace-with-a-new-random-id",
                "targetPosition": {
                    "pitch": 0,
                    "position": [0.3, 0, 0],
                    "yaw": 30,
                },
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("viggle/jst-2-scene-view", {
      projection: "perspective",
      referenceBatchIds: ["3f0a6c1e-8d2b-4b7a-9e5c-1a2b3c4d5e6f"],
      sessionId: "replace-with-a-new-random-id",
      targetPosition: {
        pitch: 0,
        position: [0.3, 0, 0],
        yaw: 30,
      },
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/viggle/jst-2-scene-view \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"projection\": \"perspective\", \"referenceBatchIds\": [\"3f0a6c1e-8d2b-4b7a-9e5c-1a2b3c4d5e6f\"], \"sessionId\": \"replace-with-a-new-random-id\", \"targetPosition\": {\"pitch\":0,\"position\":[0.3,0,0],\"yaw\":30}}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/viggle/jst-2-scene-view/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "viggle/jst-2-scene-view",
                {
                    "projection": "perspective",
                    "referenceBatchIds": ["3f0a6c1e-8d2b-4b7a-9e5c-1a2b3c4d5e6f"],
                    "sessionId": "replace-with-a-new-random-id",
                    "targetPosition": {
                        "pitch": 0,
                        "position": [0.3, 0, 0],
                        "yaw": 30,
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
    const handle = await comfy.models.submit("viggle/jst-2-scene-view", {
      projection: "perspective",
      referenceBatchIds: ["3f0a6c1e-8d2b-4b7a-9e5c-1a2b3c4d5e6f"],
      sessionId: "replace-with-a-new-random-id",
      targetPosition: {
        pitch: 0,
        position: [0.3, 0, 0],
        yaw: 30,
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
    curl https://api.comfy.org/v2/models/viggle/jst-2-scene-view/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"projection\": \"perspective\", \"referenceBatchIds\": [\"3f0a6c1e-8d2b-4b7a-9e5c-1a2b3c4d5e6f\"], \"sessionId\": \"replace-with-a-new-random-id\", \"targetPosition\": {\"pitch\":0,\"position\":[0.3,0,0],\"yaw\":30}}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/viggle/jst-2-scene-view/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/viggle/jst-2-scene-view/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## Schema

### Input

fov

number

Field of view in degrees, 20 to 140.

projection

string

perspective (the default, 1 view) or pano (a 360° panorama, 6 views).

referenceBatchIds

string[]

required

1 to 35 batch ids of the session, from `result.outputBatch.batchId`.

seed

integer

Generation seed.Format: `int64`

sessionId

string

required

The session of the scene.

targetPosition

object

required

The camera as a position and two angles.

targetPosition.pitch

number

Degrees up or down, -90 to 90; positive looks up.

targetPosition.position

number[]

required

Camera position `[x, y, z]`.

targetPosition.yaw

number

Degrees about world +Y; positive turns left.

Generated from the schema Router serves at `GET /v2/models/viggle/jst-2-scene-view/openapi.json`, the same document it validates a call against before the request reaches the provider.

### Output

completedAt

integer

Format: `int64`

createdAt

integer

Format: `int64`

credits

number

Viggle credits the task is charged; 0 once a task that did not finish ready is refunded.

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

id

string

Scene task id (`scn_` prefix).

operation

string

Task kind: pano, generate or reconstruct.

queuePosition

integer

Tasks ahead of this one while it is queued.

result

object

The scene output, set only when the task is ready.

result.newViewCount

integer

result.operation

string

result.outputBatch

object

The image batch the task added to the session.

result.outputBatch.batchId

string

result.outputBatch.createdAt

number

result.outputBatch.kind

string

result.outputBatch.manifest

object

result.outputBatch.manifest.url

string

Download URL, valid for 3 hours.

result.outputBatch.views

object[]

result.outputBatch.views[].c2w

number[][]

4 × 4 camera-to-world matrix.

result.outputBatch.views[].index

integer

result.outputBatch.views[].intrinsic

number[]

Camera intrinsics.

result.outputBatch.views[].url

string

Download URL of the view image, valid for 3 hours.

result.panorama

object

result.panorama.url

string

Download URL, valid for 3 hours.

result.preview

object

result.preview.url

string

Download URL, valid for 3 hours.

result.referenceViewCount

integer

result.sessionId

string

result.spz

object

result.spz.url

string

Download URL, valid for 3 hours.

sessionId

string

status

string

Status: queued, processing, ready, failed or cancelled.

## Examples

### Input
    
    
    {
      "projection": "perspective",
      "referenceBatchIds": [
        "3f0a6c1e-8d2b-4b7a-9e5c-1a2b3c4d5e6f"
      ],
      "sessionId": "replace-with-a-new-random-id",
      "targetPosition": {
        "pitch": 0,
        "position": [
          0.3,
          0,
          0
        ],
        "yaw": 30
      }
    }
    

### Output
    
    
    {
      "credits": 6,
      "error": null,
      "id": "scn_0199f0c2-6a1e-7c3d-9b2a-4f5e6d7c8b9a.replace-with-a-new-random-id",
      "operation": "pano",
      "result": {
        "newViewCount": 6,
        "operation": "pano",
        "outputBatch": {
          "batchId": "3f0a6c1e-8d2b-4b7a-9e5c-1a2b3c4d5e6f",
          "kind": "initial",
          "views": [
            {
              "index": 0,
              "url": "https://example.invalid/viggle/view-0.png"
            }
          ]
        },
        "panorama": {
          "url": "https://example.invalid/viggle/panorama.png"
        },
        "referenceViewCount": 0,
        "sessionId": "replace-with-a-new-random-id",
        "spz": {
          "url": "https://example.invalid/viggle/scene.spz"
        }
      },
      "sessionId": "replace-with-a-new-random-id",
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/viggle/jst-2-scene-view/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/viggle/jst-2-scene-view/code)

[Veo 3.1 Lite Generate 001](https://docs.comfy.org/development/comfy-router/models/veo/veo-3-1-lite-generate-001/code)[Jst 2 Scene](https://docs.comfy.org/development/comfy-router/models/viggle/jst-2-scene/code)
