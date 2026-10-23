---
url: https://docs.comfy.org/development/comfy-router/models/meshy/meshy-5/code/
title: Use Meshy 5 with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:19.814563+00:00
---

# Use Meshy 5 with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/meshy/meshy-5/code/

## On this page

  * Quick start
  * Schema
    * Input
    * preview variant
    * refine variant
    * Output
  * Examples
    * Input
    * Output
  * Before you ship



Meshy

# Use Meshy 5 with Comfy Router

Copy pageCopy page

Call meshy/meshy-5 through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `meshy/meshy-5`, served by Comfy Router from Meshy. **Input:** Text · **Output:** 3D

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `meshy/meshy-5` **Endpoint:** `POST https://api.comfy.org/v2/models/meshy/meshy-5`

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
            "meshy/meshy-5",
            {
                "art_style": "realistic",
                "mode": "preview",
                "prompt": "a red cube",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("meshy/meshy-5", {
      art_style: "realistic",
      mode: "preview",
      prompt: "a red cube",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/meshy/meshy-5 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"art_style\": \"realistic\", \"mode\": \"preview\", \"prompt\": \"a red cube\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/meshy/meshy-5/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "meshy/meshy-5",
                {
                    "art_style": "realistic",
                    "mode": "preview",
                    "prompt": "a red cube",
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
    const handle = await comfy.models.submit("meshy/meshy-5", {
      art_style: "realistic",
      mode: "preview",
      prompt: "a red cube",
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
    curl https://api.comfy.org/v2/models/meshy/meshy-5/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"art_style\": \"realistic\", \"mode\": \"preview\", \"prompt\": \"a red cube\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/meshy/meshy-5/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/meshy/meshy-5/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Schema

### 

​

Input

#### 

​

`preview` variant

​

ai_model

string

The Meshy model to run. On the Comfy Router route this is supplied by the path (`/v2/models/meshy/{model}`) and may be omitted or sent as null; Router writes the path’s model here after validation. On the v1 /proxy route see MeshyTextTo3DPreviewRequest, which constrains it to MeshyAiModel.

​

art_style

string

default:"\"realistic\""

Describe your desired art style of the object.Possible values: `realistic`, `sculpture`

​

geometry_resolution

string

default:"\"standard\""

Geometry resolution of the generated mesh. 2k and 4k run the Ultra pass for finer surface detail. 2k and 4k require ai_model meshy-7.1 or latest.Possible values: `standard`, `2k`, `4k`

​

is_a_t_pose

boolean

default:"false"

Deprecated. Use pose_mode instead. Whether to generate the model in an A/T pose.

​

mode

string

required

This field should be set to “preview” when creating a preview task.Possible values: `preview`

​

moderation

boolean

default:"false"

When true, input content will be screened for potentially harmful content.

​

pose_mode

string

Specify the pose mode for the generated model.Possible values: `a-pose`, `t-pose`, “

​

prompt

string

required

Describe what kind of object the 3D model is. Maximum 800 characters.

​

should_remesh

boolean

default:"false"

Controls whether to enable the remesh phase. When false, returns highest-precision triangular mesh. Defaults to true for Meshy 5 and false for Meshy 6 and 7.

​

symmetry_mode

string

default:"\"auto\""

Controls symmetry behavior during model generation.Possible values: `off`, `auto`, `on`

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

​

ultra_mode

boolean

default:"false"

Deprecated. Use geometry_resolution instead; true is equivalent to geometry_resolution 2k. Only supported when ai_model is meshy-7, meshy-7.1 or latest. The exception is meshy-7: geometry_resolution 2k requires meshy-7.1 or latest, so on meshy-7 ultra_mode true is the way to request the Ultra pass.

#### 

​

`refine` variant

​

ai_model

string

The Meshy model to run. On the Comfy Router route this is supplied by the path (`/v2/models/meshy/{model}`) and may be omitted or sent as null; Router writes the path’s model here after validation. On the v1 /proxy route see MeshyTextTo3DRefineRequest, which constrains it to MeshyAiModel.

​

enable_pbr

boolean

default:"false"

Generate PBR Maps (metallic, roughness, normal) in addition to the base color. Note that enable_pbr should be set to false when using Sculpture style.

​

mode

string

required

This field should be set to “refine” when creating a refine task.Possible values: `refine`

​

moderation

boolean

default:"false"

When true, input content will be screened for potentially harmful content.

​

preview_task_id

string

required

The corresponding preview task id. The status of the given preview task must be SUCCEEDED.

​

texture_image_url

string

Provide a 2d image to guide the texturing process. Supports .jpg, .jpeg, .png formats or base64-encoded data URI.

​

texture_prompt

string

Provide an additional text prompt to guide the texturing process. Maximum 800 characters.

​

texture_resolution

string

default:"\"2k\""

Texture resolution of the generated textures. One of 2k, 4k or 8k. 4k and 8k require ai_model meshy-6, meshy-7, meshy-7.1 or latest.Possible values: `2k`, `4k`, `8k`

Generated from the schema Router serves at `GET /v2/models/meshy/meshy-5/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

art_style

string

The unmodified art_style that was used to create the preview task.

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

Downloadable URLs to the textured 3D model files generated by Meshy.

​

model_urls.fbx

string

Downloadable URL to the FBX file.

​

model_urls.glb

string

Downloadable URL to the GLB file.

​

model_urls.mtl

string

Downloadable URL to the MTL file.

​

model_urls.obj

string

Downloadable URL to the OBJ file.

​

model_urls.usdz

string

Downloadable URL to the USDZ file.

​

negative_prompt

string

Deprecated field maintained for backward compatibility.

​

preceding_tasks

integer

The count of preceding tasks. Only meaningful when status is PENDING.

​

progress

integer

Progress of the task. 0 if not started, 100 when succeeded.Range: `0` to `100`

​

prompt

string

The unmodified prompt that was used to create the task.

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

texture_image_url

string

Downloadable URL to the texture image that was used to guide the texturing process.

​

texture_prompt

string

Additional text prompt provided to guide the texturing process during the refine stage.

​

texture_richness

string

Deprecated field maintained for backward compatibility.

​

texture_urls

object[]

An array of texture URL objects that are generated from the task.

​

texture_urls[].base_color

string

Downloadable URL to the base color map image.

​

texture_urls[].metallic

string

Downloadable URL to the metallic map image.

​

texture_urls[].normal

string

Downloadable URL to the normal map image.

​

texture_urls[].roughness

string

Downloadable URL to the roughness map image.

​

thumbnail_url

string

Downloadable URL to the thumbnail image of the model file.

​

type

string

Type of the Text to 3D task.Possible values: `text-to-3d-preview`, `text-to-3d-refine`

​

video_url

string

Deprecated field returning the downloadable URL to the preview video.

## 

​

Examples

### 

​

Input
    
    
    {
      "art_style": "realistic",
      "mode": "preview",
      "prompt": "a red cube"
    }
    

### 

​

Output
    
    
    {
      "art_style": "realistic",
      "created_at": 1767225600000,
      "finished_at": 1767225719000,
      "id": "018f2c7a-4b1e-7c3d-9a05-6e2f8b41d0c9",
      "model_urls": {
        "fbx": "https://example.invalid/meshy/text-to-3d/model.fbx",
        "glb": "https://example.invalid/meshy/text-to-3d/model.glb",
        "mtl": "https://example.invalid/meshy/text-to-3d/model.mtl",
        "obj": "https://example.invalid/meshy/text-to-3d/model.obj",
        "usdz": "https://example.invalid/meshy/text-to-3d/model.usdz"
      },
      "progress": 100,
      "prompt": "a red cube",
      "started_at": 1767225601000,
      "status": "SUCCEEDED",
      "thumbnail_url": "https://example.invalid/meshy/text-to-3d/thumbnail.png",
      "type": "text-to-3d-preview"
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/meshy/meshy-5/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/meshy/meshy-5/code)

[Use Animations with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/meshy/animations/code)[Use Meshy 6 with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/meshy/meshy-6/code)

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
