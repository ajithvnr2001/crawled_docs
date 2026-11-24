---
url: https://docs.comfy.org/development/comfy-router/models/tencent/hunyuan-image-3-5/code/
title: Use Hunyuan Image 3.5 with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-24T18:44:23.447974+00:00
---

# Use Hunyuan Image 3.5 with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/tencent/hunyuan-image-3-5/code/

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



Tencent

# Use Hunyuan Image 3.5 with Comfy Router

Copy pageCopy page

Call tencent/hunyuan-image-3.5 through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `tencent/hunyuan-image-3.5`, served by Comfy Router from Tencent. **Input:** Text · **Output:** Image

## Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `tencent/hunyuan-image-3.5` **Endpoint:** `POST https://api.comfy.org/v2/models/tencent/hunyuan-image-3.5`

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
            "tencent/hunyuan-image-3.5",
            {
                "aspect_ratio": "16:9",
                "output_format": "png",
                "prompt": "a serene mountain lake at sunrise, ultra detailed, cinematic lighting",
                "resolution": "1080p",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("tencent/hunyuan-image-3.5", {
      aspect_ratio: "16:9",
      output_format: "png",
      prompt: "a serene mountain lake at sunrise, ultra detailed, cinematic lighting",
      resolution: "1080p",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/tencent/hunyuan-image-3.5 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"aspect_ratio\": \"16:9\", \"output_format\": \"png\", \"prompt\": \"a serene mountain lake at sunrise, ultra detailed, cinematic lighting\", \"resolution\": \"1080p\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/tencent/hunyuan-image-3.5/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "tencent/hunyuan-image-3.5",
                {
                    "aspect_ratio": "16:9",
                    "output_format": "png",
                    "prompt": "a serene mountain lake at sunrise, ultra detailed, cinematic lighting",
                    "resolution": "1080p",
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
    const handle = await comfy.models.submit("tencent/hunyuan-image-3.5", {
      aspect_ratio: "16:9",
      output_format: "png",
      prompt: "a serene mountain lake at sunrise, ultra detailed, cinematic lighting",
      resolution: "1080p",
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
    curl https://api.comfy.org/v2/models/tencent/hunyuan-image-3.5/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"aspect_ratio\": \"16:9\", \"output_format\": \"png\", \"prompt\": \"a serene mountain lake at sunrise, ultra detailed, cinematic lighting\", \"resolution\": \"1080p\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/tencent/hunyuan-image-3.5/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/tencent/hunyuan-image-3.5/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## Schema

### Input

aspect_ratio

string

Aspect ratio as a W:H ratio such as 16:9.

images

string (uri)[]

Reference images, by public https URL. REFUSED on this route: Hunyuan Image 3.5 is launched text-only, so a non-empty `images` is rejected with a 400. MPS fetches a reference image only by a crawler-accessible URL and cannot be handed stripped bytes, so caller images cannot have their EXIF location data removed first; image input is not supported yet. Send a prompt only.

n

integer

default:"1"

Number of images to generate. Only 1 is served (the metered quantity).Possible values: `1`

negative_prompt

string

Text describing what the image should avoid.

output_format

string

Image encoding of the generated output. One of png or jpeg.Possible values: `png`, `jpeg`

prompt

string

required

The text prompt describing the image to generate. Required: this route is text-only, so a prompt is the only accepted input. Trimmed before it is signed.

resolution

string

default:"\"1080p\""

Output resolution tier, which is also the metered tier. One of 720p, 1080p, 2k or 4k.Possible values: `720p`, `1080p`, `2k`, `4k`

Generated from the schema Router serves at `GET /v2/models/tencent/hunyuan-image-3.5/openapi.json`, the same document it validates a call against before the request reaches the provider.

### Output

Response

object

required

Response.ImageUrls

string (uri)[]

required

The generated images’ download URLs. Present and non-empty on the document Router returns; at least one entry is a fetchable URL. Tencent’s own links, documented as valid for about 12 hours.

Response.Message

string

Tencent’s status message, documented as an empty string when there is no error.

Response.RequestId

string

Tencent’s own request identifier, for troubleshooting with Tencent. It is neither the task id nor an asset.

Response.Status

string

required

Terminal success status. This document is returned only for `DONE`; other MPS statuses reach a Router caller as an error.Possible values: `DONE`

## Examples

### Input
    
    
    {
      "aspect_ratio": "16:9",
      "output_format": "png",
      "prompt": "a serene mountain lake at sunrise, ultra detailed, cinematic lighting",
      "resolution": "1080p"
    }
    

### Output
    
    
    {
      "Response": {
        "ImageUrls": [
          "https://example.invalid/tencent/hunyuan-image-3.5/generated.png"
        ],
        "Message": "",
        "RequestId": "9a1c0d4e-77b2-4e0c-8f2e-2f9a1c0d4e77",
        "Status": "DONE"
      }
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/tencent/hunyuan-image-3-5/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/tencent/hunyuan-image-3-5/code)

[Hunyuan 3D Uv](https://docs.comfy.org/development/comfy-router/models/tencent/hunyuan-3d-uv/code)[P1 20260311 Image To Model](https://docs.comfy.org/development/comfy-router/models/tripo/p1-20260311-image-to-model/code)
