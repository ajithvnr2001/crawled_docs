---
url: https://docs.comfy.org/development/comfy-router/models/meshy/relief/code/
title: Use Relief with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-23T19:03:20.137238+00:00
---

# Use Relief with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/meshy/relief/code/

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

# Use Relief with Comfy Router

Copy pageCopy page

Call meshy/relief through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `meshy/relief`, served by Comfy Router from Meshy. **Input:** Image · **Output:** Image + 3D

## Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `meshy/relief` **Endpoint:** `POST https://api.comfy.org/v2/models/meshy/relief`

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
            "meshy/relief",
            {
                "image_url": "https://example.invalid/meshy/relief/logo.png",
                "variant": "low",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("meshy/relief", {
      image_url: "https://example.invalid/meshy/relief/logo.png",
      variant: "low",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/meshy/relief \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"image_url\": \"https://example.invalid/meshy/relief/logo.png\", \"variant\": \"low\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/meshy/relief/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "meshy/relief",
                {
                    "image_url": "https://example.invalid/meshy/relief/logo.png",
                    "variant": "low",
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
    const handle = await comfy.models.submit("meshy/relief", {
      image_url: "https://example.invalid/meshy/relief/logo.png",
      variant: "low",
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
    curl https://api.comfy.org/v2/models/meshy/relief/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"image_url\": \"https://example.invalid/meshy/relief/logo.png\", \"variant\": \"low\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/meshy/relief/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/meshy/relief/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## Schema

### Input

base_thickness_mm

number

Base plate thickness in millimeters, 0.1 to 10. With remove_base true, omit it or send 0.Range: `0` to `10`

bend_angle

number

default:"60"

Bend angle in degrees. Below 1 the relief stays flat.Range: `0` to `360`

bend_axis

string

`xz` (default, bends the left and right edges) or `yz` (bends the top and bottom edges). Applies only when bend_mode is convex or concave.

bend_mode

string

`off` (default), `convex` or `concave`.

carving_depth_mm

number

Carving depth in millimeters. The default is 6 for variant high and 3 for variant low.Range: `0` to `60`

carving_mode

string

`emboss` (default) or `engrave`.

color_mapping

boolean

default:"false"

Color the model from the image. GLB, OBJ, FBX and USDZ carry the color; STL and 3MF stay white. The cost does not change.

image_url

string

required

A public URL or data URI of a jpg, jpeg, png or webp image. At most 20 MB and at least 32 x 32 pixels. Transparent areas are filled with black.

mesh_resolution

integer

default:"1024"

Points along the longer side. Larger values give much larger files (about 150 MB GLB and 300 MB STL at 2048).Range: `512` to `2048`

removal_threshold

number

default:"0.01"

Background removal threshold. Applies only when remove_base is true.Range: `0.01` to `1`

remove_base

boolean

default:"false"

Cut away the background so the relief has no base plate.

should_generate_model

boolean

default:"true"

Set to false for a depth map only, with no model and no preview. The cost does not change.

size_mm

number

default:"60"

Length of the longer side in millimeters.Range: `20` to `250`

target_formats

string[]

The model formats to generate. One or more of glb, obj, fbx, stl, usdz and 3mf. The default is glb and stl.

variant

string

`low` (default) gives slight depth and finer detail, for laser or CNC work. `high` gives deeper, sculptural relief, for 3D printing. It also sets the default carving_depth_mm.

Generated from the schema Router serves at `GET /v2/models/meshy/relief/openapi.json`, the same document it validates a call against before the request reaches the provider.

### Output

consumed_credits

integer

Meshy credits the task used. 0 for a failed task.

created_at

integer

Timestamp of when the task was created, in milliseconds.Format: `int64`

depth_map_url

string

Downloadable URL to the 2k 16-bit grayscale depth map PNG. The values are relative, not millimeters.

expires_at

integer

Timestamp of when the task result expires, in milliseconds. 0 if not finished.Format: `int64`

finished_at

integer

Timestamp of when the task was finished, in milliseconds. 0 if not finished.Format: `int64`

id

string

required

Unique identifier for the task.

model_urls

object

Downloadable URLs to the relief model files, one per requested format. Empty for a depth-map-only task.

model_urls.3mf

string

Downloadable URL to the 3MF file.

model_urls.fbx

string

Downloadable URL to the FBX file.

model_urls.glb

string

Downloadable URL to the GLB file, in meters.

model_urls.mtl

string

Downloadable URL to the MTL material file for the OBJ file.

model_urls.obj

string

Downloadable URL to the OBJ file.

model_urls.stl

string

Downloadable URL to the binary STL file, in millimeters.

model_urls.usdz

string

Downloadable URL to the USDZ file.

preceding_tasks

integer

The count of preceding tasks. Only meaningful when status is PENDING.

progress

integer

Progress of the task. 0 if not started, 100 when succeeded.Range: `0` to `100`

started_at

integer

Timestamp of when the task was started, in milliseconds. 0 if not started.Format: `int64`

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

texture_urls

object[]

Texture URLs. Present only with color_mapping true.

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

Downloadable URL to the preview image. Empty for a depth-map-only task.

type

string

Type of the task. Always relief.

## Examples

### Input
    
    
    {
      "image_url": "https://example.invalid/meshy/relief/logo.png",
      "variant": "low"
    }
    

### Output
    
    
    {
      "consumed_credits": 20,
      "created_at": 1767225600000,
      "depth_map_url": "https://example.invalid/meshy/relief/depth.png",
      "finished_at": 1767225663000,
      "id": "018f2c7a-4b1e-7c3d-9a05-6e2f8b41d0c9",
      "model_urls": {
        "glb": "https://example.invalid/meshy/relief/model.glb",
        "stl": "https://example.invalid/meshy/relief/model.stl"
      },
      "progress": 100,
      "started_at": 1767225601000,
      "status": "SUCCEEDED",
      "thumbnail_url": "https://example.invalid/meshy/relief/preview.png",
      "type": "relief"
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/meshy/relief/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/meshy/relief/code)

[Meshy N1](https://docs.comfy.org/development/comfy-router/models/meshy/meshy-n1/code)[Remesh](https://docs.comfy.org/development/comfy-router/models/meshy/remesh/code)
