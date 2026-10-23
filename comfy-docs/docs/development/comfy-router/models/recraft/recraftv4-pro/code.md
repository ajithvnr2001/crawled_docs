---
url: https://docs.comfy.org/development/comfy-router/models/recraft/recraftv4-pro/code/
title: Use Recraft V4 Pro with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:37.651297+00:00
---

# Use Recraft V4 Pro with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/recraft/recraftv4-pro/code/

## On this page

  * Quick start
  * Schema
    * Input
    * Output
  * Examples
    * Input
    * Output
  * Before you ship



Recraft

# Use Recraft V4 Pro with Comfy Router

Copy pageCopy page

Call recraft/recraftv4_pro through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `recraft/recraftv4_pro`, served by Comfy Router from Recraft. **Input:** Text · **Output:** Image

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `recraft/recraftv4_pro` **Endpoint:** `POST https://api.comfy.org/v2/models/recraft/recraftv4_pro`

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
            "recraft/recraftv4_pro",
            {
                "n": 1,
                "prompt": "A single red maple leaf on a plain white background.",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("recraft/recraftv4_pro", {
      n: 1,
      prompt: "A single red maple leaf on a plain white background.",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/recraft/recraftv4_pro \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"n\": 1, \"prompt\": \"A single red maple leaf on a plain white background.\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/recraft/recraftv4_pro/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "recraft/recraftv4_pro",
                {
                    "n": 1,
                    "prompt": "A single red maple leaf on a plain white background.",
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
    const handle = await comfy.models.submit("recraft/recraftv4_pro", {
      n: 1,
      prompt: "A single red maple leaf on a plain white background.",
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
    curl https://api.comfy.org/v2/models/recraft/recraftv4_pro/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"n\": 1, \"prompt\": \"A single red maple leaf on a plain white background.\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/recraft/recraftv4_pro/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/recraft/recraftv4_pro/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Schema

### 

​

Input

​

controls

object

The controls for the generated image

​

controls.artistic_level

integer

Defines artistic tone of your image. At a simple level, the person looks straight at the camera in a static and clean style. Dynamic and eccentric levels introduce movement and creativity.Range: `0` to `5`

​

controls.background_color

object

RGB color values

​

controls.background_color.rgb

integer[]

required

​

controls.colors

object[]

An array of preferable colors

​

controls.colors[].rgb

integer[]

required

​

controls.no_text

boolean

Do not embed text layouts

​

model

string

The model to use for generation (e.g., “recraftv3”). This field is NOT constrained to an enum: the proxy forwards whatever the caller sends. The spellings Comfy ships — the set Comfy Router addresses as `recraft/<model>` — are recraftv2, recraftv3, recraftv4, recraftv4_pro, recraftv4_1, recraftv4_1_utility, recraftv4_1_pro, recraftv4_1_utility_pro, recraftv4_styles, recraftv4_styles_pro, recraftv4_1_vector, recraftv4_1_utility_vector, recraftv4_1_pro_vector, recraftv4_1_utility_pro_vector, recraftv4_styles_vector and recraftv4_styles_pro_vector. They are written out here rather than named by reference because the RecraftGenerationModel component that declares them is `$ref`-ed by nothing and is therefore pruned from the spec served at GET /openapi, so a pointer to it would dangle in the served document. The four `recraftv4_styles*` spellings additionally require `style_id` — see that field.

​

n

integer

The number of images to generate. Recraft accepts 1-6.Range: `1` to `6`

​

prompt

string

required

The text prompt describing the image to generate

​

response_format

string

Possible values: `url`, `b64_json`

​

size

string

The size of the generated image (e.g., “1024x1024”)

​

style

string

The style to apply to the generated image (e.g., “digital_illustration”)

​

style_id

string

The style ID to apply to the generated image (e.g., “123e4567-e89b-12d3-a456-426614174000”). If style_id is provided, style should not be provided. REQUIRED by the four `recraftv4_styles*` models: Recraft rejects those without a style_id or style reference. Mint one with `POST /proxy/recraft/styles`, which this same proxy serves under the same credentials. Nothing on this route enforces the pairing — the body is forwarded to Recraft unchanged, so a `recraftv4_styles*` call without it reaches the partner and comes back 4xx.

Generated from the schema Router serves at `GET /v2/models/recraft/recraftv4_pro/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

created

integer

required

Unix timestamp when the generation was created

​

credits

integer

required

Number of credits used for the generation

​

data

object[]

required

Array of generated image information

​

data[].b64_json

string

Base64-encoded image data (present instead of `url` when the request set `response_format: b64_json`)

​

data[].image_id

string

Unique identifier for the generated image

​

data[].url

string

URL to access the generated image (present when `response_format` is `url`, the default)

​

style_id

string

The resolved style id, returned by Recraft when style references are used (notably required-input models recraftv4_styles*); reusable as `style_id` in later requests.

## 

​

Examples

### 

​

Input
    
    
    {
      "n": 1,
      "prompt": "A single red maple leaf on a plain white background."
    }
    

### 

​

Output
    
    
    {
      "created": 1767225600,
      "credits": 1,
      "data": [
        {
          "image_id": "3f7a1b28-5c0d-4e91-8a6f-1b2c3d4e5f60",
          "url": "https://example.invalid/recraft/recraftv3/generated.png"
        }
      ]
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/recraft/recraftv4-pro/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/recraft/recraftv4-pro/code)

[Use Recraft V4.1 with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/recraft/recraftv4-1/code)[Use Recraft V4 Styles Pro Vector with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/recraft/recraftv4-styles-pro-vector/code)

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
