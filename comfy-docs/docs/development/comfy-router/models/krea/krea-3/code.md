---
url: https://docs.comfy.org/development/comfy-router/models/krea/krea-3/code/
title: Use Krea 3 with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-19T14:35:01.749654+00:00
---

# Use Krea 3 with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/krea/krea-3/code/

## On this page

  * Quick start
  * Schema
    * Input
    * Output
  * Examples
    * Input
    * Output
  * Before you ship



Krea

# Use Krea 3 with Comfy Router

Copy pageCopy page

Call krea/krea-3 through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `krea/krea-3`, served by Comfy Router from Krea. **Input:** Text, Image · **Output:** Image

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `krea/krea-3` **Endpoint:** `POST https://api.comfy.org/v2/models/krea/krea-3`

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
            "krea/krea-3",
            {
                "image_urls": ["https://example.com/reference.png"],
                "prompt": "Place the product on a clean studio background",
                "resolution": "1k",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("krea/krea-3", {
      image_urls: ["https://example.com/reference.png"],
      prompt: "Place the product on a clean studio background",
      resolution: "1k",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/krea/krea-3 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"image_urls\": [\"https://example.com/reference.png\"], \"prompt\": \"Place the product on a clean studio background\", \"resolution\": \"1k\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/krea/krea-3/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "krea/krea-3",
                {
                    "image_urls": ["https://example.com/reference.png"],
                    "prompt": "Place the product on a clean studio background",
                    "resolution": "1k",
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
    const handle = await comfy.models.submit("krea/krea-3", {
      image_urls: ["https://example.com/reference.png"],
      prompt: "Place the product on a clean studio background",
      resolution: "1k",
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
    curl https://api.comfy.org/v2/models/krea/krea-3/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"image_urls\": [\"https://example.com/reference.png\"], \"prompt\": \"Place the product on a clean studio background\", \"resolution\": \"1k\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/krea/krea-3/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/krea/krea-3/requests/$REQUEST_ID \
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

1:1, 4:5, 3:4, 2:3, 9:16, 5:4, 4:3, 3:2, 16:9 or 21:9. Use with resolution; omit for automatic framing.

​

image_urls

string[]

Input image URLs, up to 8. Use image_url values from POST /proxy/krea/assets. Omit for text-to-image.

​

model

string

berry (default, quality) or jam (speed).

​

negative_prompt

string

​

prompt

string

required

Editing instruction. Describe what should change and what should stay the same.

​

regional_edit

boolean

Set true for a local edit that keeps the rest of the image. Needs model berry and at least one image in image_urls.

​

resolution

string

required

1k or 2k.

​

seed

integer

​

thinking_mode

string

fast (default), high or ultra. High and ultra plan complex edits in more detail and take longer. Ultra needs resolution 2k.

Generated from the schema Router serves at `GET /v2/models/krea/krea-3/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

completed_at

string (date-time)

required

Format: `date-time`

​

created_at

string (date-time)

required

Format: `date-time`

​

job_id

string (uuid)

required

Format: `uuid`

​

result

object

required

The finished generation. Not nullable here, unlike on `KreaJob`: a terminal job whose `result` carries no `urls` is answered as a Comfy Router error, so a `200` always carries it.

​

result.style_id

string

Set by loraTraining jobs rather than by a generation; a `200` for these models carries `urls`.

​

result.urls

string (uri)[]

required

The generated images, as downloadable links. At least one, because a `completed` job with an empty `urls` is `success_without_output` and never reaches this document.

​

status

string

required

Always `completed` on this document: it is the only status Router reports as a success, and Krea’s vocabulary is matched without a case fold.Possible values: `completed`

## 

​

Examples

### 

​

Input
    
    
    {
      "image_urls": [
        "https://example.com/reference.png"
      ],
      "prompt": "Place the product on a clean studio background",
      "resolution": "1k"
    }
    

### 

​

Output
    
    
    {
      "completed_at": "2027-01-01T00:00:37Z",
      "created_at": "2027-01-01T00:00:00Z",
      "job_id": "7f1c2e84-5b90-4a37-8d61-2c0f9ab4e153",
      "result": {
        "urls": [
          "https://example.invalid/krea/krea-2/generated.png"
        ]
      },
      "status": "completed"
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/krea/krea-3/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/krea/krea-3/code)

[Use Krea 2 with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/krea/krea-2/code)[Use LTX 2.5 Fast with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/ltx/ltx-2-5-fast/code)

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
