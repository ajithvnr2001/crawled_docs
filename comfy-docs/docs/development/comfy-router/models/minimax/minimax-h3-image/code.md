---
url: https://docs.comfy.org/development/comfy-router/models/minimax/minimax-h3-image/code/
title: Use MiniMax H3 Image with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-12T15:52:11.207060+00:00
---

# Use MiniMax H3 Image with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/minimax/minimax-h3-image/code/

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



MiniMax

# Use MiniMax H3 Image with Comfy Router

Copy pageCopy page

Call minimax/minimax-h3-image through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `minimax/minimax-h3-image`, served by Comfy Router from MiniMax. **Input:** Text, Image · **Output:** Image

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `minimax/minimax-h3-image` **Endpoint:** `POST https://api.comfy.org/v2/models/minimax/minimax-h3-image`

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
            "minimax/minimax-h3-image",
            {
                "area": "1K",
                "prompt": "A single red maple leaf resting on a plain white background.",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("minimax/minimax-h3-image", {
      area: "1K",
      prompt: "A single red maple leaf resting on a plain white background.",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/minimax/minimax-h3-image \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"area\": \"1K\", \"prompt\": \"A single red maple leaf resting on a plain white background.\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/minimax/minimax-h3-image/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "minimax/minimax-h3-image",
                {
                    "area": "1K",
                    "prompt": "A single red maple leaf resting on a plain white background.",
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
    const handle = await comfy.models.submit("minimax/minimax-h3-image", {
      area: "1K",
      prompt: "A single red maple leaf resting on a plain white background.",
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
    curl https://api.comfy.org/v2/models/minimax/minimax-h3-image/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"area\": \"1K\", \"prompt\": \"A single red maple leaf resting on a plain white background.\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/minimax/minimax-h3-image/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/minimax/minimax-h3-image/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Schema

### 

​

Input

​

area

string

Output area level when `size` is omitted or `auto`. One of `1K`, `2K`, `4K` (default).

​

aspect_ratio

string

Output aspect ratio when `size` is omitted or `auto`. `auto` (default) or `X:Y` between 1:3 and 3:1, such as `16:9`.

​

disable_prompt_enhanced

boolean

default:"false"

Turns MiniMax’s prompt enhancement off. Requires a fixed `size` or an `X:Y` `aspect_ratio`.

​

images

object[]

Optional reference images. When present the request runs as an image edit, exactly as on the edits route.

​

images[].image_url

string

required

A public http(s) URL or a `data:image/<format>;base64,` URI. JPEG, PNG, WEBP, HEIC or HEIF, each side 128 to 8192 px, long side at most 4 times the short side.

​

model

string

Model name. `MiniMax-H3-Image` or `MiniMax-H3-Image-Highspeed`. Router callers may omit this field or send null; Router fills in the model selected by the request path.

​

n

integer

default:"1"

Number of images. Input tokens are charged once per image.Range: `1` to `10`

​

output_compression

integer

Compression quality for `jpeg` and `webp`, default 95.Range: `0` to `100`

​

output_format

string

Output image format. One of `png`, `jpeg`, `jpg` (default), `webp`.

​

prompt

string

required

Text description of the image. With `images`, the description of the edit; the reference images are image 1, image 2 and so on, in array order.

​

size

string

Output size, `auto` (default) or `WIDTHxHEIGHT` such as `2720x1536`. A fixed size must have an area of 655,360 to 20,000,000 pixels and an aspect ratio between 1:3 and 3:1, and cannot be combined with `aspect_ratio` or `area`.

Generated from the schema Router serves at `GET /v2/models/minimax/minimax-h3-image/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

created

integer

Format: `int64`

​

data

object[]

​

data[].error

object

Present only when this image failed or was withheld.

​

data[].error.code

string

​

data[].error.message

string

​

data[].revised_prompt

string

The prompt MiniMax used for this image.

​

data[].size

string

Actual image size as `WIDTHxHEIGHT`.

​

data[].url

string

URL of the generated image. It expires, so download the image.

​

output_format

string

​

request_id

string

​

usage

object

Token usage of the successful images. Billing is based on it.

​

usage.generated_images

integer

​

usage.input_tokens

integer

​

usage.input_tokens_details

object

​

usage.input_tokens_details.image_tokens

integer

​

usage.input_tokens_details.text_tokens

integer

​

usage.output_tokens

integer

​

usage.output_tokens_details

object

​

usage.output_tokens_details.image_tokens

integer

​

usage.total_tokens

integer

## 

​

Examples

### 

​

Input
    
    
    {
      "area": "1K",
      "prompt": "A single red maple leaf resting on a plain white background."
    }
    

### 

​

Output
    
    
    {
      "created": 1794300000,
      "data": [
        {
          "size": "1024x1024",
          "url": "https://example.invalid/minimax/minimax-h3-image/generated.jpg"
        }
      ],
      "output_format": "jpeg",
      "request_id": "06a1b2c3d4e5f60718293a4b5c6d7e8f",
      "usage": {
        "generated_images": 1,
        "input_tokens": 10,
        "input_tokens_details": {
          "image_tokens": 0,
          "text_tokens": 10
        },
        "output_tokens": 1024,
        "output_tokens_details": {
          "image_tokens": 1024
        },
        "total_tokens": 1034
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/minimax/minimax-h3-image/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/minimax/minimax-h3-image/code)

[MiniMax H3 Image Highspeed](https://docs.comfy.org/development/comfy-router/models/minimax/minimax-h3-image-highspeed/code)[MiniMax H3](https://docs.comfy.org/development/comfy-router/models/minimax/minimax-h3/code)
