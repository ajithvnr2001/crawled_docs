---
url: https://docs.comfy.org/development/comfy-router/models/fal/h3-max-turbo/code/
title: Use H3 Max Turbo with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:03.939694+00:00
---

# Use H3 Max Turbo with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/fal/h3-max-turbo/code/

## On this page

  * Quick start
  * Schema
    * Input
    * Output
  * Examples
    * Input
    * Output
  * Before you ship



fal

# Use H3 Max Turbo with Comfy Router

Copy pageCopy page

Call fal/h3-max-turbo through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `fal/h3-max-turbo`, served by Comfy Router from fal. **Input:** Text, Image · **Output:** Video + Audio

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `fal/h3-max-turbo` **Endpoint:** `POST https://api.comfy.org/v2/models/fal/h3-max-turbo`

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
            "fal/h3-max-turbo",
            {
                "duration": 5,
                "prompt": "a red fox running through a snowy forest",
                "prompt_expansion_mode": "balanced",
                "resolution": "480P",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("fal/h3-max-turbo", {
      duration: 5,
      prompt: "a red fox running through a snowy forest",
      prompt_expansion_mode: "balanced",
      resolution: "480P",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/fal/h3-max-turbo \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"duration\": 5, \"prompt\": \"a red fox running through a snowy forest\", \"prompt_expansion_mode\": \"balanced\", \"resolution\": \"480P\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/fal/h3-max-turbo/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "fal/h3-max-turbo",
                {
                    "duration": 5,
                    "prompt": "a red fox running through a snowy forest",
                    "prompt_expansion_mode": "balanced",
                    "resolution": "480P",
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
    const handle = await comfy.models.submit("fal/h3-max-turbo", {
      duration: 5,
      prompt: "a red fox running through a snowy forest",
      prompt_expansion_mode: "balanced",
      resolution: "480P",
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
    curl https://api.comfy.org/v2/models/fal/h3-max-turbo/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"duration\": 5, \"prompt\": \"a red fox running through a snowy forest\", \"prompt_expansion_mode\": \"balanced\", \"resolution\": \"480P\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/fal/h3-max-turbo/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/fal/h3-max-turbo/requests/$REQUEST_ID \
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

default:"\"16:9\""

Aspect ratio: 21:9, 16:9, 4:3, 1:1, 3:4, or 9:16.

​

duration

integer

default:"5"

Duration of the generated video in seconds.

​

enable_safety_checker

boolean

default:"true"

Enable the safety checker.

​

prompt

string

required

Text prompt for video generation.

​

prompt_expansion_mode

string

required

How much effort to spend rewriting the prompt before generation: balanced or quality.

​

resolution

string

default:"\"768P\""

Resolution of the generated video: 480P or 768P.

​

seed

integer

Random seed. A random seed is selected when omitted.

​

sync_mode

boolean

Return the generated video as base64 instead of a CDN URL.

Generated from the schema Router serves at `GET /v2/models/fal/h3-max-turbo/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

expanded_prompt

string

The prompt after expansion, as sent to the model.

​

timings

object

End-to-end timing breakdown (seconds).

​

video

object

required

The generated video file.

​

video.content_type

string

MIME type of the video file.

​

video.file_name

string

Name of the video file.

​

video.file_size

integer

Size of the video file in bytes.

​

video.url

string

URL of the generated video.

## 

​

Examples

### 

​

Input
    
    
    {
      "duration": 5,
      "prompt": "a red fox running through a snowy forest",
      "prompt_expansion_mode": "balanced",
      "resolution": "480P"
    }
    

### 

​

Output
    
    
    {
      "expanded_prompt": "a single red maple leaf falling onto still water, cinematic, 4k",
      "timings": {
        "inference": 42.5
      },
      "video": {
        "content_type": "video/mp4",
        "file_name": "output.mp4",
        "file_size": 4194304,
        "url": "https://example.invalid/fal/minimax/h3-max/output.mp4"
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/fal/h3-max-turbo/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/fal/h3-max-turbo/code)

[Use Crystal Upscaler with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/fal/crystal-upscaler/code)[Use H3 Max with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/fal/h3-max/code)

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
