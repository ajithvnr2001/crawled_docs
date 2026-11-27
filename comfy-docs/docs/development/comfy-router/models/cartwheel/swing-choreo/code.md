---
url: https://docs.comfy.org/development/comfy-router/models/cartwheel/swing-choreo/code/
title: Use Swing Choreo with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-27T17:19:26.342711+00:00
---

# Use Swing Choreo with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/cartwheel/swing-choreo/code/

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



Cartwheel

# Use Swing Choreo with Comfy Router

Copy pageCopy page

Call cartwheel/swing-choreo through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `cartwheel/swing-choreo`, served by Comfy Router from Cartwheel. **Input:** Text · **Output:** 3D

## Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `cartwheel/swing-choreo` **Endpoint:** `POST https://api.comfy.org/v2/models/cartwheel/swing-choreo`

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
            "cartwheel/swing-choreo",
            {
                "exportSettings": {
                    "characterID": "char-upload-MHR",
                    "exportType": "glb",
                    "forward": "-Z",
                    "frameRate": 30,
                    "frameStepSize": 1,
                    "up": "Y",
                },
                "prompts": ["two dancers spin and bow"],
                "swingChoreoProperties": {
                    "duration": 8,
                },
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("cartwheel/swing-choreo", {
      exportSettings: {
        characterID: "char-upload-MHR",
        exportType: "glb",
        forward: "-Z",
        frameRate: 30,
        frameStepSize: 1,
        up: "Y",
      },
      prompts: ["two dancers spin and bow"],
      swingChoreoProperties: {
        duration: 8,
      },
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/cartwheel/swing-choreo \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"exportSettings\": {\"characterID\":\"char-upload-MHR\",\"exportType\":\"glb\",\"forward\":\"-Z\",\"frameRate\":30,\"frameStepSize\":1,\"up\":\"Y\"}, \"prompts\": [\"two dancers spin and bow\"], \"swingChoreoProperties\": {\"duration\":8}}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/cartwheel/swing-choreo/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "cartwheel/swing-choreo",
                {
                    "exportSettings": {
                        "characterID": "char-upload-MHR",
                        "exportType": "glb",
                        "forward": "-Z",
                        "frameRate": 30,
                        "frameStepSize": 1,
                        "up": "Y",
                    },
                    "prompts": ["two dancers spin and bow"],
                    "swingChoreoProperties": {
                        "duration": 8,
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
    const handle = await comfy.models.submit("cartwheel/swing-choreo", {
      exportSettings: {
        characterID: "char-upload-MHR",
        exportType: "glb",
        forward: "-Z",
        frameRate: 30,
        frameStepSize: 1,
        up: "Y",
      },
      prompts: ["two dancers spin and bow"],
      swingChoreoProperties: {
        duration: 8,
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
    curl https://api.comfy.org/v2/models/cartwheel/swing-choreo/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"exportSettings\": {\"characterID\":\"char-upload-MHR\",\"exportType\":\"glb\",\"forward\":\"-Z\",\"frameRate\":30,\"frameStepSize\":1,\"up\":\"Y\"}, \"prompts\": [\"two dancers spin and bow\"], \"swingChoreoProperties\": {\"duration\":8}}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/cartwheel/swing-choreo/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/cartwheel/swing-choreo/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## Schema

### Input

exportSettings

object

required

Export format of the generated motion.

exportSettings.characterID

string

required

Character the motion is exported on, for example `char-upload-MHR`.

exportSettings.exportType

string

required

Export format, for example `glb` or `fbx-blender`.

exportSettings.forward

string

required

Forward axis, for example `-Z`.

exportSettings.frameRate

number

required

Export frame rate, for example 24, 30, 60 or 120.

exportSettings.frameStepSize

number

required

Frame step size, usually 1.

exportSettings.includeMesh

boolean

Includes the character mesh in the export.

exportSettings.keyframeCleaning

string

`none`, `reduce` or `simplify`.

exportSettings.moveInPlace

boolean

Keeps the character in place.

exportSettings.restPose

boolean

Prepends the rest pose as frame 0. Defaults to true.

exportSettings.up

string

required

Up axis, for example `Y`.

prompts

string[]

required

Exactly one prompt with at least one non-space character.

requestedModel

string

Omit it or send null when using Comfy Router; the model id selects `swing_choreo`.

swingChoreoProperties

object

required

Swing Choreo settings.

swingChoreoProperties.duration

integer

required

Scene length in whole seconds, 5 to 15.Range: `5` to `15`

Generated from the schema Router serves at `GET /v2/models/cartwheel/swing-choreo/openapi.json`, the same document it validates a call against before the request reaches the provider.

### Output

items

object[]

One generated motion with its actor exports.

items[].cameraFbxURL

string

Captured camera FBX, valid for 1 hour.

items[].durationSeconds

number

Planned Swing Choreo scene length in seconds, for example 7.416667. It can differ from the requested duration.

items[].errorMessage

string

items[].exportFilenames

string[]

items[].exportURLs

string[]

One export per actor, in actor order. Valid for 1 hour.

items[].jobID

string

items[].outputs

object[]

Swing Choreo actors in order.

items[].outputs[].actorIndex

integer

items[].outputs[].bvhURL

string

items[].outputs[].exportFilename

string

items[].outputs[].exportURL

string

items[].outputs[].mhrFbxURL

string

items[].sourceVideoMediaID

string

items[].status

string

`QUEUED`, `GENERATING`, `COMPLETED`, `FAILED` or `FLAGGED`.

items[].studioPreviewURL

string

MP4 preview, valid for 12 hours.

items[].title

string

nextToken

string

Present when more pages exist.

## Examples

### Input
    
    
    {
      "exportSettings": {
        "characterID": "char-upload-MHR",
        "exportType": "glb",
        "forward": "-Z",
        "frameRate": 30,
        "frameStepSize": 1,
        "up": "Y"
      },
      "prompts": [
        "two dancers spin and bow"
      ],
      "swingChoreoProperties": {
        "duration": 8
      }
    }
    

### Output
    
    
    {
      "items": [
        {
          "exportFilenames": [
            "actor0.glb"
          ],
          "exportURLs": [
            "https://example.invalid/cartwheel/actor0.glb"
          ],
          "jobID": "job-1",
          "status": "COMPLETED",
          "studioPreviewURL": "https://example.invalid/cartwheel/preview.mp4",
          "title": "a person waves with the right hand"
        }
      ]
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/cartwheel/swing-choreo/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/cartwheel/swing-choreo/code)

[Omnihuman 2.0](https://docs.comfy.org/development/comfy-router/models/byteplusomnihuman/omnihuman-2-0/code)[Swing Sketch](https://docs.comfy.org/development/comfy-router/models/cartwheel/swing-sketch/code)
