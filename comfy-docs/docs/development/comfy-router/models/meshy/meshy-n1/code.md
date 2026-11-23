---
url: https://docs.comfy.org/development/comfy-router/models/meshy/meshy-n1/code/
title: Use Meshy N1 with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-23T19:03:20.265671+00:00
---

# Use Meshy N1 with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/meshy/meshy-n1/code/

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



Meshy

# Use Meshy N1 with Comfy Router

Copy pageCopy page

Call meshy/meshy-n1 through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `meshy/meshy-n1`, served by Comfy Router from Meshy. **Input:** Image, 3D · **Output:** 3D

## Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `meshy/meshy-n1` **Endpoint:** `POST https://api.comfy.org/v2/models/meshy/meshy-n1`

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
            "meshy/meshy-n1",
            {
                "image_style_url": "https://example.invalid/meshy/n1/front.png",
                "model_url": "https://cdn.meshy.ai/model/example_model_2.glb",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("meshy/meshy-n1", {
      image_style_url: "https://example.invalid/meshy/n1/front.png",
      model_url: "https://cdn.meshy.ai/model/example_model_2.glb",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/meshy/meshy-n1 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"image_style_url\": \"https://example.invalid/meshy/n1/front.png\", \"model_url\": \"https://cdn.meshy.ai/model/example_model_2.glb\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/meshy/meshy-n1/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "meshy/meshy-n1",
                {
                    "image_style_url": "https://example.invalid/meshy/n1/front.png",
                    "model_url": "https://cdn.meshy.ai/model/example_model_2.glb",
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
    const handle = await comfy.models.submit("meshy/meshy-n1", {
      image_style_url: "https://example.invalid/meshy/n1/front.png",
      model_url: "https://cdn.meshy.ai/model/example_model_2.glb",
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
    curl https://api.comfy.org/v2/models/meshy/meshy-n1/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"image_style_url\": \"https://example.invalid/meshy/n1/front.png\", \"model_url\": \"https://cdn.meshy.ai/model/example_model_2.glb\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/meshy/meshy-n1/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/meshy/meshy-n1/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## Schema

### Input

ai_model

string

The Meshy model to run. On the Comfy Router route this is supplied by the path (`/v2/models/meshy/{model}`) and may be omitted or sent as null; Router writes the path’s model here after validation.

enable_original_uv

boolean

Use the original UV of the model instead of generating new UVs.

enable_pbr

boolean

default:"false"

meshy-n1 does not generate PBR maps, so only false is accepted.Possible values: `false`

image_style_url

string

One reference image, used as the front view. Supports jpg, jpeg, png and webp, or a base64 data URI. Do not send with multiview_image_urls.

input_task_id

string

The ID of a completed Meshy task whose mesh to texture. Required if model_url is not provided.

model_url

string

A publicly accessible URL or data URI to a 3D model. Supported formats glb, gltf, obj, fbx, stl. Required if input_task_id is not provided. At most 7,999,999 triangle faces.

multiview_image_urls

string[]

One to four reference images of the same object. The first image is the front view. Do not send with image_style_url.

target_formats

string[]

The model formats to generate. One or more of glb, obj, fbx, stl, usdz and 3mf.

texture_resolution

string

default:"\"2k\""

Texture resolution of the base color map. meshy-n1 supports 2k only.Possible values: `2k`

Generated from the schema Router serves at `GET /v2/models/meshy/meshy-n1/openapi.json`, the same document it validates a call against before the request reaches the provider.

### Output

created_at

integer

Timestamp of when the task was created, in milliseconds.

expires_at

integer

Timestamp of when the task result expires, in milliseconds.

finished_at

integer

Timestamp of when the task was finished, in milliseconds. 0 if not finished.

id

string

required

Unique identifier for the task.

image_style_url

string

The image input that was used to create the texturing task.

model_urls

object

Downloadable URLs to the textured 3D model files.

model_urls.fbx

string

Downloadable URL to the FBX file.

model_urls.glb

string

Downloadable URL to the GLB file.

model_urls.mtl

string

Downloadable URL to the MTL material file for the OBJ file.

model_urls.obj

string

Downloadable URL to the OBJ file.

model_urls.stl

string

Downloadable URL to the STL file.

model_urls.usdz

string

Downloadable URL to the USDZ file.

multiview_image_urls

string[]

The reference images that were used to create the texturing task.

preceding_tasks

integer

The count of preceding tasks. Only meaningful when status is PENDING.

progress

integer

Progress of the task. 0 if not started, 100 when succeeded.Range: `0` to `100`

started_at

integer

Timestamp of when the task was started, in milliseconds. 0 if not started.

status

string

required

Possible values: `SUCCEEDED`

task_error

object

Error object that contains the error message if the task failed.

task_error.message

string

Detailed error message.

text_style_prompt

string

The text prompt that was used to create the texturing task.

texture_urls

object[]

An array of texture URL objects that are generated from the task.

texture_urls[].base_color

string

Downloadable URL to the base color map image.

texture_urls[].metallic

string

Downloadable URL to the metallic map image.

texture_urls[].normal

string

Downloadable URL to the normal map image.

texture_urls[].roughness

string

Downloadable URL to the roughness map image.

thumbnail_url

string

Downloadable URL to the thumbnail image of the model file.

type

string

Type of the Retexture task.Possible values: `retexture`

## Examples

### Input
    
    
    {
      "image_style_url": "https://example.invalid/meshy/n1/front.png",
      "model_url": "https://cdn.meshy.ai/model/example_model_2.glb"
    }
    

### Output
    
    
    {
      "created_at": 1767225600000,
      "finished_at": 1767225621000,
      "id": "018f2c7a-4b1e-7c3d-9a05-6e2f8b41d0c9",
      "model_urls": {
        "fbx": "https://example.invalid/meshy/retexture/model.fbx",
        "glb": "https://example.invalid/meshy/retexture/model.glb"
      },
      "progress": 100,
      "started_at": 1767225601000,
      "status": "SUCCEEDED",
      "texture_urls": [
        {
          "base_color": "https://example.invalid/meshy/retexture/texture_0.png"
        }
      ],
      "thumbnail_url": "https://example.invalid/meshy/retexture/preview.png",
      "type": "retexture"
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/meshy/meshy-n1/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/meshy/meshy-n1/code)

[Meshy 7](https://docs.comfy.org/development/comfy-router/models/meshy/meshy-7/code)[Relief](https://docs.comfy.org/development/comfy-router/models/meshy/relief/code)
