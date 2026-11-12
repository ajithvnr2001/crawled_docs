---
url: https://docs.comfy.org/development/comfy-router/models/pixverse/v6-max/code/
title: Use V6 Max with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-12T15:52:10.959482+00:00
---

# Use V6 Max with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/pixverse/v6-max/code/

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



Pixverse

# Use V6 Max with Comfy Router

Copy pageCopy page

Call pixverse/v6-max through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `pixverse/v6-max`, served by Comfy Router from Pixverse. **Input:** Text · **Output:** Video

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `pixverse/v6-max` **Endpoint:** `POST https://api.comfy.org/v2/models/pixverse/v6-max`

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
            "pixverse/v6-max",
            {
                "aspect_ratio": "16:9",
                "duration": 5,
                "prompt": "a single red maple leaf falling onto still water",
                "quality": "360p",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("pixverse/v6-max", {
      aspect_ratio: "16:9",
      duration: 5,
      prompt: "a single red maple leaf falling onto still water",
      quality: "360p",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/pixverse/v6-max \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"aspect_ratio\": \"16:9\", \"duration\": 5, \"prompt\": \"a single red maple leaf falling onto still water\", \"quality\": \"360p\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/pixverse/v6-max/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "pixverse/v6-max",
                {
                    "aspect_ratio": "16:9",
                    "duration": 5,
                    "prompt": "a single red maple leaf falling onto still water",
                    "quality": "360p",
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
    const handle = await comfy.models.submit("pixverse/v6-max", {
      aspect_ratio: "16:9",
      duration: 5,
      prompt: "a single red maple leaf falling onto still water",
      quality: "360p",
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
    curl https://api.comfy.org/v2/models/pixverse/v6-max/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"aspect_ratio\": \"16:9\", \"duration\": 5, \"prompt\": \"a single red maple leaf falling onto still water\", \"quality\": \"360p\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/pixverse/v6-max/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/pixverse/v6-max/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Schema

### 

​

Input

​

aspect_ratio

string

required

Possible values: `16:9`, `4:3`, `1:1`, `3:4`, `9:16`, `2:3`, `3:2`, `21:9`

​

duration

integer

required

Range: `1` to `15`

​

generate_audio_switch

boolean

default:"false"

​

model

string

PixVerse text-to-video model identifier. On the Comfy Router route `POST /v2/models/pixverse/{model}` this field is supplied from the path and may be omitted.

​

motion_mode

string

Possible values: `normal`, `fast`

​

negative_prompt

string

​

prompt

string

required

​

quality

string

required

Possible values: `360p`, `540p`, `720p`, `1080p`

​

seed

integer

​

style

string

Possible values: `anime`, `3d_animation`, `clay`, `comic`, `cyberpunk`

​

template_id

integer

​

water_mark

boolean

Generated from the schema Router serves at `GET /v2/models/pixverse/v6-max/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

ErrCode

integer

​

ErrMsg

string

​

Resp

object

required

​

Resp.create_time

string

​

Resp.credits

integer

​

Resp.id

integer

​

Resp.modify_time

string

​

Resp.negative_prompt

string

​

Resp.outputHeight

integer

​

Resp.outputWidth

integer

​

Resp.prompt

string

​

Resp.resolution_ratio

integer

​

Resp.seed

integer

​

Resp.size

integer

​

Resp.status

integer

required

Possible values: `1`, `5`, `6`, `7`, `8`

​

Resp.style

string

​

Resp.url

string

required

## 

​

Examples

### 

​

Input
    
    
    {
      "aspect_ratio": "16:9",
      "duration": 5,
      "prompt": "a single red maple leaf falling onto still water",
      "quality": "360p"
    }
    

### 

​

Output
    
    
    {
      "ErrCode": 0,
      "ErrMsg": "",
      "Resp": {
        "credits": 1,
        "id": 4242,
        "status": 1,
        "url": "https://example.invalid/pixverse/v6/out.mp4"
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/pixverse/v6-max/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/pixverse/v6-max/code)

[V3.5](https://docs.comfy.org/development/comfy-router/models/pixverse/v3-5/code)[V6](https://docs.comfy.org/development/comfy-router/models/pixverse/v6/code)
