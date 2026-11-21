---
url: https://docs.comfy.org/development/comfy-router/models/freepik/ai-image-style-transfer/code/
title: Use AI Image Style Transfer with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-21T15:11:28.477505+00:00
---

# Use AI Image Style Transfer with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/freepik/ai-image-style-transfer/code/

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



Freepik

# Use AI Image Style Transfer with Comfy Router

Copy pageCopy page

Call freepik/ai-image-style-transfer through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `freepik/ai-image-style-transfer`, served by Comfy Router from Freepik. **Input:** Text, Image · **Output:** Image

## Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `freepik/ai-image-style-transfer` **Endpoint:** `POST https://api.comfy.org/v2/models/freepik/ai-image-style-transfer`

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
            "freepik/ai-image-style-transfer",
            {
                "image": "https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80",
                "reference_image": "https://img.magnific.com/free-photo/beautiful-sunset_395237-33.jpg?w=740&q=80",
                "style_strength": 80,
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("freepik/ai-image-style-transfer", {
      image: "https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80",
      reference_image: "https://img.magnific.com/free-photo/beautiful-sunset_395237-33.jpg?w=740&q=80",
      style_strength: 80,
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/freepik/ai-image-style-transfer \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"image\": \"https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80\", \"reference_image\": \"https://img.magnific.com/free-photo/beautiful-sunset_395237-33.jpg?w=740&q=80\", \"style_strength\": 80}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/freepik/ai-image-style-transfer/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "freepik/ai-image-style-transfer",
                {
                    "image": "https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80",
                    "reference_image": "https://img.magnific.com/free-photo/beautiful-sunset_395237-33.jpg?w=740&q=80",
                    "style_strength": 80,
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
    const handle = await comfy.models.submit("freepik/ai-image-style-transfer", {
      image: "https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80",
      reference_image: "https://img.magnific.com/free-photo/beautiful-sunset_395237-33.jpg?w=740&q=80",
      style_strength: 80,
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
    curl https://api.comfy.org/v2/models/freepik/ai-image-style-transfer/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"image\": \"https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80\", \"reference_image\": \"https://img.magnific.com/free-photo/beautiful-sunset_395237-33.jpg?w=740&q=80\", \"style_strength\": 80}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/freepik/ai-image-style-transfer/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/freepik/ai-image-style-transfer/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## Schema

### Input

engine

string

default:"\"balanced\""

Engine preset for style transferPossible values: `balanced`, `definio`, `illusio`, `3d_cartoon`, `colorful_anime`, `caricature`, `real`, `super_real`, `softy`

fixed_generation

boolean

default:"false"

When enabled, using the same settings will consistently produce the same image.

flavor

string

default:"\"faithful\""

Flavor of the transferring stylePossible values: `faithful`, `gen_z`, `psychedelia`, `detaily`, `clear`, `donotstyle`, `donotstyle_sharp`

image

string

required

Base64 or URL of the image to do the style transfer

is_portrait

boolean

default:"false"

Indicates whether the image should be processed as a portrait.

portrait_beautifier

string

Facial beautification on portrait images. Only used if is_portrait is true.Possible values: `beautify_face`, `beautify_face_max`

portrait_style

string

default:"\"standard\""

Visual style applied to portrait images. Only used if is_portrait is true.Possible values: `standard`, `pop`, `super_pop`

prompt

string

Prompt for the AI model

reference_image

string

required

Base64 or URL of the reference image for style transfer

structure_strength

integer

default:"50"

Allows to maintain the structure of the original imageRange: `0` to `100`

style_strength

integer

default:"100"

Percentage of style strengthRange: `0` to `100`

webhook_url

string (uri)

Optional callback URL for async notifications.Format: `uri`

Generated from the schema Router serves at `GET /v2/models/freepik/ai-image-style-transfer/openapi.json`, the same document it validates a call against before the request reaches the provider.

### Output

data

object

required

data.generated

string (uri)[]

required

The finished generation’s image URLs. Present and non-empty on the document Router returns; this list IS the result. The links are Freepik’s own and expire.

data.status

string

required

Possible values: `COMPLETED`

data.task_id

string (uuid)

Format: `uuid`

## Examples

### Input
    
    
    {
      "image": "https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80",
      "reference_image": "https://img.magnific.com/free-photo/beautiful-sunset_395237-33.jpg?w=740&q=80",
      "style_strength": 80
    }
    

### Output
    
    
    {
      "data": {
        "generated": [
          "https://example.invalid/freepik/ai-image-style-transfer/styled.png"
        ],
        "status": "COMPLETED",
        "task_id": "046b6c7f-0b8a-43b9-b35d-6489e6daee91"
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/freepik/ai-image-style-transfer/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/freepik/ai-image-style-transfer/code)

[AI Image Relight](https://docs.comfy.org/development/comfy-router/models/freepik/ai-image-relight/code)[AI Image Upscaler Precision V2](https://docs.comfy.org/development/comfy-router/models/freepik/ai-image-upscaler-precision-v2/code)
