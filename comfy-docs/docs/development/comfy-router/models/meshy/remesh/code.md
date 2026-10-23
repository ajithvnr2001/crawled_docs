---
url: https://docs.comfy.org/development/comfy-router/models/meshy/remesh/code/
title: Use Remesh with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:21.202238+00:00
---

# Use Remesh with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/meshy/remesh/code/

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

# Use Remesh with Comfy Router

Copy pageCopy page

Call meshy/remesh through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `meshy/remesh`, served by Comfy Router from Meshy. **Input:** 3D · **Output:** 3D

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `meshy/remesh` **Endpoint:** `POST https://api.comfy.org/v2/models/meshy/remesh`

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
            "meshy/remesh",
            {
                "input_task_id": "0193abcd-0000-0000-0000-000000000000",
                "origin_at": "bottom",
                "resize_height": 1,
                "target_formats": ["glb", "fbx"],
                "target_polycount": 50000,
                "topology": "quad",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("meshy/remesh", {
      input_task_id: "0193abcd-0000-0000-0000-000000000000",
      origin_at: "bottom",
      resize_height: 1,
      target_formats: ["glb", "fbx"],
      target_polycount: 50000,
      topology: "quad",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/meshy/remesh \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input_task_id\": \"0193abcd-0000-0000-0000-000000000000\", \"origin_at\": \"bottom\", \"resize_height\": 1, \"target_formats\": [\"glb\",\"fbx\"], \"target_polycount\": 50000, \"topology\": \"quad\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/meshy/remesh/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "meshy/remesh",
                {
                    "input_task_id": "0193abcd-0000-0000-0000-000000000000",
                    "origin_at": "bottom",
                    "resize_height": 1,
                    "target_formats": ["glb", "fbx"],
                    "target_polycount": 50000,
                    "topology": "quad",
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
    const handle = await comfy.models.submit("meshy/remesh", {
      input_task_id: "0193abcd-0000-0000-0000-000000000000",
      origin_at: "bottom",
      resize_height: 1,
      target_formats: ["glb", "fbx"],
      target_polycount: 50000,
      topology: "quad",
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
    curl https://api.comfy.org/v2/models/meshy/remesh/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input_task_id\": \"0193abcd-0000-0000-0000-000000000000\", \"origin_at\": \"bottom\", \"resize_height\": 1, \"target_formats\": [\"glb\",\"fbx\"], \"target_polycount\": 50000, \"topology\": \"quad\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/meshy/remesh/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/meshy/remesh/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Schema

### 

​

Input

​

convert_format_only

boolean

default:"false"

If true, only changes the format of the input model file, ignoring other inputs like topology, resize_height, and target_polycount.

​

input_task_id

string

The ID of the completed Image to 3D or Text to 3D task you wish to remesh. Required if model_url is not provided.

​

model_url

string

A publicly accessible URL or data URI to a 3D model. Supported formats glb, gltf, obj, fbx, stl. Required if input_task_id is not provided.

​

origin_at

string

Position of the origin.Possible values: `bottom`, `center`, “

​

resize_height

number

default:"0"

Resize the model to a certain height measured in meters. 0 means no resizing.

​

target_formats

`glb`, `fbx`, `obj`, `usdz`, `blend`, `stl`[]

default:"[\"glb\"]"

A list of target formats for the remeshed model.

​

target_polycount

integer

default:"30000"

Specify the target number of polygons in the generated model. Valid range is 100 to 300,000.Range: `100` to `300000`

​

topology

string

default:"\"triangle\""

Specify the topology of the generated model.Possible values: `quad`, `triangle`

Generated from the schema Router serves at `GET /v2/models/meshy/remesh/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

created_at

integer

Timestamp of when the task was created, in milliseconds.Format: `int64`

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

model_urls

object

Downloadable URLs to the remeshed 3D model files.

​

model_urls.blend

string

Downloadable URL to the Blender file.

​

model_urls.fbx

string

Downloadable URL to the FBX file.

​

model_urls.glb

string

Downloadable URL to the GLB file.

​

model_urls.obj

string

Downloadable URL to the OBJ file.

​

model_urls.stl

string

Downloadable URL to the STL file.

​

model_urls.usdz

string

Downloadable URL to the USDZ file.

​

preceding_tasks

integer

The count of preceding tasks. Only meaningful when status is PENDING.

​

progress

integer

Progress of the task. 0 if not started, 100 when succeeded.Range: `0` to `100`

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

Type of the Remesh task.Possible values: `remesh`

## 

​

Examples

### 

​

Input
    
    
    {
      "input_task_id": "0193abcd-0000-0000-0000-000000000000",
      "origin_at": "bottom",
      "resize_height": 1,
      "target_formats": [
        "glb",
        "fbx"
      ],
      "target_polycount": 50000,
      "topology": "quad"
    }
    

### 

​

Output
    
    
    {
      "created_at": 1767225600000,
      "finished_at": 1767225663000,
      "id": "018f2c7a-4b1e-7c3d-9a05-6e2f8b41d0c9",
      "model_urls": {
        "fbx": "https://example.invalid/meshy/remesh/model.fbx",
        "glb": "https://example.invalid/meshy/remesh/model.glb",
        "obj": "https://example.invalid/meshy/remesh/model.obj"
      },
      "progress": 100,
      "started_at": 1767225601000,
      "status": "SUCCEEDED",
      "type": "remesh"
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/meshy/remesh/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/meshy/remesh/code)

[Use Meshy 7 with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/meshy/meshy-7/code)[Use Rigging with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/meshy/rigging/code)

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
