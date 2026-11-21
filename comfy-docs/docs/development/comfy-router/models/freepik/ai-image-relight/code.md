---
url: https://docs.comfy.org/development/comfy-router/models/freepik/ai-image-relight/code/
title: Use AI Image Relight with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-21T15:11:27.999945+00:00
---

# Use AI Image Relight with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/freepik/ai-image-relight/code/

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

# Use AI Image Relight with Comfy Router

Copy pageCopy page

Call freepik/ai-image-relight through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `freepik/ai-image-relight`, served by Comfy Router from Freepik. **Input:** Text, Image · **Output:** Image

## Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `freepik/ai-image-relight` **Endpoint:** `POST https://api.comfy.org/v2/models/freepik/ai-image-relight`

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
            "freepik/ai-image-relight",
            {
                "image": "https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80",
                "prompt": "warm golden-hour sunlight from the left",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("freepik/ai-image-relight", {
      image: "https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80",
      prompt: "warm golden-hour sunlight from the left",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/freepik/ai-image-relight \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"image\": \"https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80\", \"prompt\": \"warm golden-hour sunlight from the left\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/freepik/ai-image-relight/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "freepik/ai-image-relight",
                {
                    "image": "https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80",
                    "prompt": "warm golden-hour sunlight from the left",
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
    const handle = await comfy.models.submit("freepik/ai-image-relight", {
      image: "https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80",
      prompt: "warm golden-hour sunlight from the left",
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
    curl https://api.comfy.org/v2/models/freepik/ai-image-relight/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"image\": \"https://img.magnific.com/free-photo/light-through-mountains_395237-33.jpg?semt=ais_hybrid&w=740&q=80\", \"prompt\": \"warm golden-hour sunlight from the left\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/freepik/ai-image-relight/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/freepik/ai-image-relight/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## Schema

### Input

advanced_settings

object

advanced_settings.blacks

integer

default:"50"

Adjust the level of black color in the image.Range: `0` to `100`

advanced_settings.brightness

integer

default:"50"

Adjust the level of brightness in the image.Range: `0` to `100`

advanced_settings.contrast

integer

default:"50"

Adjust the level of contrast in the image.Range: `0` to `100`

advanced_settings.engine

string

default:"\"automatic\""

Engine preset for relighting:

  * balanced: Well-rounded, general-purpose option
  * cool: Brighter with cooler tones
  * real: Aims to enhance photographic quality (Experimental)
  * illusio: Optimized for illustrations and drawings
  * fairy: Suited for fantasy-themed images
  * colorful_anime: Ideal for anime, cartoons, and vibrant colors
  * hard_transform: Significantly alters the original image
  * softy: Slightly softer effect, suitable for graphic designs Possible values: `automatic`, `balanced`, `cool`, `real`, `illusio`, `fairy`, `colorful_anime`, `hard_transform`, `softy`



advanced_settings.fixed_generation

boolean

default:"false"

When enabled, using the same settings will consistently produce the same image.

advanced_settings.saturation

integer

default:"50"

Adjust the level of saturation in the image.Range: `0` to `100`

advanced_settings.transfer_light_a

string

default:"\"automatic\""

Adjusts the intensity of light transfer.Possible values: `automatic`, `low`, `medium`, `normal`, `high`, `high_on_faces`

advanced_settings.transfer_light_b

string

default:"\"automatic\""

Also modifies light transfer intensity. Can be combined with transfer_light_a for varied effects.Possible values: `automatic`, `composition`, `straight`, `smooth_in`, `smooth_out`, `smooth_both`, `reverse_both`, `soft_in`, `soft_out`, `soft_mid`, `strong_mid`, `style_shift`, `strong_shift`

advanced_settings.whites

integer

default:"50"

Adjust the level of white color in the image.Range: `0` to `100`

change_background

boolean

default:"true"

When enabled, changes the background based on prompt and/or reference image. Useful for product placement and portraits.

image

string

required

Base64 or URL of the image to do the relight

interpolate_from_original

boolean

default:"false"

When enabled, makes the final image interpolate from the original using the light transfer strength slider.

light_transfer_strength

integer

default:"100"

Level of light transfer intensity. 0% keeps closest to original, 100% is maximum transfer.Range: `0` to `100`

preserve_details

boolean

default:"true"

Maintains texture and small details of the original image. Good for product photography, texts, etc.

prompt

string

You can guide the generation process and influence the light transfer with a descriptive prompt. IMPORTANT: You can emphasize specific aspects of the light in your prompt by using a number in parentheses, ranging from 1 to 1.4, like “(dark scene:1.3)”.

style

string

default:"\"standard\""

Style preset for the relight operation.Possible values: `standard`, `darker_but_realistic`, `clean`, `smooth`, `brighter`, `contrasted_n_hdr`, `just_composition`

transfer_light_from_lightmap

string

Base64 or URL of the lightmap for light transfer. Incompatible with ‘transfer_light_from_reference_image’

transfer_light_from_reference_image

string

Base64 or URL of the reference image for light transfer. Incompatible with ‘transfer_light_from_lightmap’

webhook_url

string (uri)

Optional callback URL that will receive asynchronous notifications whenever the task changes status.Format: `uri`

Generated from the schema Router serves at `GET /v2/models/freepik/ai-image-relight/openapi.json`, the same document it validates a call against before the request reaches the provider.

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
      "prompt": "warm golden-hour sunlight from the left"
    }
    

### Output
    
    
    {
      "data": {
        "generated": [
          "https://example.invalid/freepik/ai-image-relight/relit.png"
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/freepik/ai-image-relight/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/freepik/ai-image-relight/code)

[Patina](https://docs.comfy.org/development/comfy-router/models/fal/patina/code)[AI Image Style Transfer](https://docs.comfy.org/development/comfy-router/models/freepik/ai-image-style-transfer/code)
