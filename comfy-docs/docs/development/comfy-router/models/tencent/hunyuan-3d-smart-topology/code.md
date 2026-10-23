---
url: https://docs.comfy.org/development/comfy-router/models/tencent/hunyuan-3d-smart-topology/code/
title: Use Hunyuan 3D Smart Topology with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-19T14:35:02.328855+00:00
---

# Use Hunyuan 3D Smart Topology with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/tencent/hunyuan-3d-smart-topology/code/

## On this page

  * Quick start
  * Schema
    * Input
    * Output
  * Examples
    * Input
    * Output
  * Before you ship



Tencent

# Use Hunyuan 3D Smart Topology with Comfy Router

Copy pageCopy page

Call tencent/hunyuan-3d-smart-topology through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `tencent/hunyuan-3d-smart-topology`, served by Comfy Router from Tencent. **Input:** 3D · **Output:** 3D

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `tencent/hunyuan-3d-smart-topology` **Endpoint:** `POST https://api.comfy.org/v2/models/tencent/hunyuan-3d-smart-topology`

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
            "tencent/hunyuan-3d-smart-topology",
            {
                "File3D": {
                    "Type": "GLB",
                    "Url": "https://vcg-test-1258344699.cos.ap-guangzhou.myqcloud.com/test/3d/test.glb",
                },
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("tencent/hunyuan-3d-smart-topology", {
      File3D: {
        Type: "GLB",
        Url: "https://vcg-test-1258344699.cos.ap-guangzhou.myqcloud.com/test/3d/test.glb",
      },
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/tencent/hunyuan-3d-smart-topology \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"File3D\": {\"Type\":\"GLB\",\"Url\":\"https://vcg-test-1258344699.cos.ap-guangzhou.myqcloud.com/test/3d/test.glb\"}}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/tencent/hunyuan-3d-smart-topology/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "tencent/hunyuan-3d-smart-topology",
                {
                    "File3D": {
                        "Type": "GLB",
                        "Url": "https://vcg-test-1258344699.cos.ap-guangzhou.myqcloud.com/test/3d/test.glb",
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
    const handle = await comfy.models.submit("tencent/hunyuan-3d-smart-topology", {
      File3D: {
        Type: "GLB",
        Url: "https://vcg-test-1258344699.cos.ap-guangzhou.myqcloud.com/test/3d/test.glb",
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
    curl https://api.comfy.org/v2/models/tencent/hunyuan-3d-smart-topology/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"File3D\": {\"Type\":\"GLB\",\"Url\":\"https://vcg-test-1258344699.cos.ap-guangzhou.myqcloud.com/test/3d/test.glb\"}}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/tencent/hunyuan-3d-smart-topology/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/tencent/hunyuan-3d-smart-topology/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Schema

### 

​

Input

​

FaceLevel

string

Polygon reduction level.Possible values: `high`, `medium`, `low`

​

File3D

object

required

3D file input for smart topology

​

File3D.Type

string

required

3D file format typePossible values: `OBJ`, `GLB`

​

File3D.Url

string (uri)

required

URL of the 3D file to retopologiseFormat: `uri`

​

PolygonType

string

Polygon type for the output mesh. Defaults to triangle.Possible values: `triangle`, `quadrilateral`

Generated from the schema Router serves at `GET /v2/models/tencent/hunyuan-3d-smart-topology/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

Response

object

required

​

Response.ErrorCode

string

Tencent’s error code, documented as an empty string when there is no error. Router does not read it once `Status` is present.

​

Response.ErrorMessage

string

Tencent’s error message, documented as an empty string when there is no error. Router does not read it once `Status` is present.

​

Response.RequestId

string

Tencent’s own request identifier, for troubleshooting with Tencent. It is neither the job id nor an asset.

​

Response.ResultFile3Ds

object[]

required

The finished job’s generated 3D files. Present and non-empty on the document Router returns; at least one entry carries a fetchable `Url`. The links are Tencent’s own and are documented as valid for 24 hours.

​

Response.ResultFile3Ds[].PreviewImageUrl

string (uri)

Preview image URLFormat: `uri`

​

Response.ResultFile3Ds[].Type

string

File format. A finished job can return several entries in no fixed order, and not every entry is a mesh: the UV and smart-topology operations have been observed returning OBJ, GLB and FBX meshes beside an IMAGE (a PNG texture). Select an entry by `Type` rather than by position. Deliberately not an enum: the values above are only the ones observed, this component is shared with operations whose output has never been observed (part, texture-edit), and the output schema is descriptive, so an unlisted value Tencent returns must not turn a healthy result into a schema violation.

​

Response.ResultFile3Ds[].Url

string (uri)

File URL (valid for 24 hours)Format: `uri`

​

Response.Status

string

required

Possible values: `DONE`

## 

​

Examples

### 

​

Input
    
    
    {
      "File3D": {
        "Type": "GLB",
        "Url": "https://vcg-test-1258344699.cos.ap-guangzhou.myqcloud.com/test/3d/test.glb"
      }
    }
    

### 

​

Output
    
    
    {
      "Response": {
        "ErrorCode": "",
        "ErrorMessage": "",
        "RequestId": "9a1c0d4e-77b2-4e0c-8f2e-2f9a1c0d4e77",
        "ResultFile3Ds": [
          {
            "PreviewImageUrl": "https://example.invalid/tencent/hunyuan-3d-smart-topology/preview.png",
            "Type": "GLB",
            "Url": "https://example.invalid/tencent/hunyuan-3d-smart-topology/retopologised.glb"
          }
        ],
        "Status": "DONE"
      }
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/tencent/hunyuan-3d-smart-topology/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/tencent/hunyuan-3d-smart-topology/code)

[Use Hunyuan 3D Part with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/tencent/hunyuan-3d-part/code)[Use Hunyuan 3D Texture Edit with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/tencent/hunyuan-3d-texture-edit/code)

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
