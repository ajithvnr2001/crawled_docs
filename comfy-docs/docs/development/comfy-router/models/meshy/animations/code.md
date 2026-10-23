---
url: https://docs.comfy.org/development/comfy-router/models/meshy/animations/code/
title: Use Animations with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:19.541288+00:00
---

# Use Animations with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/meshy/animations/code/

## On this page

  * Quick start
  * Schema
    * Input
    * Output
  * Examples
    * Input
    * Output
  * Before you ship



Meshy

# Use Animations with Comfy Router

Copy pageCopy page

Call meshy/animations through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `meshy/animations`, served by Comfy Router from Meshy. **Input:** 3D · **Output:** 3D

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `meshy/animations` **Endpoint:** `POST https://api.comfy.org/v2/models/meshy/animations`

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
            "meshy/animations",
            {
                "action_id": 92,
                "post_process": {
                    "fps": 60,
                    "operation_type": "change_fps",
                },
                "rig_task_id": "0193abcd-0000-0000-0000-000000000000",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("meshy/animations", {
      action_id: 92,
      post_process: {
        fps: 60,
        operation_type: "change_fps",
      },
      rig_task_id: "0193abcd-0000-0000-0000-000000000000",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/meshy/animations \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"action_id\": 92, \"post_process\": {\"fps\":60,\"operation_type\":\"change_fps\"}, \"rig_task_id\": \"0193abcd-0000-0000-0000-000000000000\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/meshy/animations/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "meshy/animations",
                {
                    "action_id": 92,
                    "post_process": {
                        "fps": 60,
                        "operation_type": "change_fps",
                    },
                    "rig_task_id": "0193abcd-0000-0000-0000-000000000000",
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
    const handle = await comfy.models.submit("meshy/animations", {
      action_id: 92,
      post_process: {
        fps: 60,
        operation_type: "change_fps",
      },
      rig_task_id: "0193abcd-0000-0000-0000-000000000000",
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
    curl https://api.comfy.org/v2/models/meshy/animations/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"action_id\": 92, \"post_process\": {\"fps\":60,\"operation_type\":\"change_fps\"}, \"rig_task_id\": \"0193abcd-0000-0000-0000-000000000000\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/meshy/animations/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/meshy/animations/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Schema

### 

​

Input

​

action_id

integer

required

The identifier of the animation action to apply.

​

post_process

object

Parameters for post-processing animation files.

​

post_process.fps

integer

default:"30"

The target frame rate. Default is 30. Applicable only when operation_type is change_fps.Possible values: `24`, `25`, `30`, `60`

​

post_process.operation_type

string

required

The type of operation to perform.Possible values: `change_fps`, `fbx2usdz`, `extract_armature`

​

rig_task_id

string

required

The id of a successfully completed rigging task (from POST /openapi/v1/rigging). The character from this task will be animated.

Generated from the schema Router serves at `GET /v2/models/meshy/animations/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

created_at

integer

Timestamp of when the task was created, in milliseconds.Format: `int64`

​

expires_at

integer

Timestamp of when the task result expires, in milliseconds.Format: `int64`

​

finished_at

integer

Timestamp of when the task was finished, in milliseconds. 0 if not finished.Format: `int64`

​

id

string

required

Unique identifier for the task.

​

preceding_tasks

integer

The count of preceding tasks. Only meaningful when status is PENDING.

​

progress

integer

Progress of the task (0-100).Range: `0` to `100`

​

result

object

Contains the output animation URLs if the task SUCCEEDED.

​

result.animation_fbx_url

string

Downloadable URL for the animation in FBX format.

​

result.animation_glb_url

string

Downloadable URL for the animation in GLB format.

​

result.processed_animation_fps_fbx_url

string

Downloadable URL for the animation with changed FPS in FBX format.

​

result.processed_armature_fbx_url

string

Downloadable URL for the processed armature in FBX format.

​

result.processed_usdz_url

string

Downloadable URL for the processed animation in USDZ format.

​

started_at

integer

Timestamp of when the task was started, in milliseconds. 0 if not started.Format: `int64`

​

status

string

required

Possible values: `SUCCEEDED`

​

task_error

object

Error object that contains the error message if the task failed.

​

task_error.message

string

Detailed error message.

​

type

string

Type of the Animation task.Possible values: `animate`

## 

​

Examples

### 

​

Input
    
    
    {
      "action_id": 92,
      "post_process": {
        "fps": 60,
        "operation_type": "change_fps"
      },
      "rig_task_id": "0193abcd-0000-0000-0000-000000000000"
    }
    

### 

​

Output
    
    
    {
      "created_at": 1767225600000,
      "expires_at": 1767830400000,
      "finished_at": 1767225648000,
      "id": "018f2c7a-4b1e-7c3d-9a05-6e2f8b41d0c9",
      "progress": 100,
      "result": {
        "animation_fbx_url": "https://example.invalid/meshy/animations/animation.fbx",
        "animation_glb_url": "https://example.invalid/meshy/animations/animation.glb"
      },
      "started_at": 1767225601000,
      "status": "SUCCEEDED",
      "type": "animate"
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/meshy/animations/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/meshy/animations/code)

[Use Uni 1 with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/luma_2/uni-1/code)[Use Meshy 5 with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/meshy/meshy-5/code)

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
