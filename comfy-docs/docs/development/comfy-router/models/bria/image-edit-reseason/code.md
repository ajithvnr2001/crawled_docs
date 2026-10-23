---
url: https://docs.comfy.org/development/comfy-router/models/bria/image-edit-reseason/code/
title: Use Image Edit Reseason with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-19T14:34:59.792774+00:00
---

# Use Image Edit Reseason with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/bria/image-edit-reseason/code/

## On this page

  * Quick start
  * Schema
    * Input
    * Output
  * Examples
    * Input
    * Output
  * Before you ship



Bria

# Use Image Edit Reseason with Comfy Router

Copy pageCopy page

Call bria/image-edit-reseason through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `bria/image-edit-reseason`, served by Comfy Router from Bria. **Input:** Image, Text · **Output:** Image

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `bria/image-edit-reseason` **Endpoint:** `POST https://api.comfy.org/v2/models/bria/image-edit-reseason`

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
            "bria/image-edit-reseason",
            {
                "image": "https://picsum.photos/id/237/960/540",
                "season": "winter",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("bria/image-edit-reseason", {
      image: "https://picsum.photos/id/237/960/540",
      season: "winter",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/bria/image-edit-reseason \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"image\": \"https://picsum.photos/id/237/960/540\", \"season\": \"winter\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/bria/image-edit-reseason/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "bria/image-edit-reseason",
                {
                    "image": "https://picsum.photos/id/237/960/540",
                    "season": "winter",
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
    const handle = await comfy.models.submit("bria/image-edit-reseason", {
      image: "https://picsum.photos/id/237/960/540",
      season: "winter",
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
    curl https://api.comfy.org/v2/models/bria/image-edit-reseason/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"image\": \"https://picsum.photos/id/237/960/540\", \"season\": \"winter\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/bria/image-edit-reseason/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/bria/image-edit-reseason/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Schema

### 

​

Input

​

image

string

required

The image to edit. Supported input types are Base64-encoded string or URL pointing to a publicly accessible image file. Accepted formats JPEG, JPG, PNG, WEBP.

​

season

string

required

The season to apply, one of “spring”, “summer”, “autumn”, or “winter”. Custom text is also accepted.

Generated from the schema Router serves at `GET /v2/models/bria/image-edit-reseason/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

error

object

Error object (only present when status is ERROR)

​

error.code

integer

Error code.

​

error.details

string

Additional error details.

​

error.message

string

Error message.

​

request_id

string

Unique identifier for the request.

​

result

object

Result object (only present when status is COMPLETED)

​

result.image_url

string

URL of the generated/edited image.

​

result.prompt

string

Original prompt.

​

result.refined_prompt

string

Refined version of the prompt, or null on a COMPLETED generation Bria did not refine. Nullable because the key is PRESENT carrying null rather than omitted; observed live on bria/image-edit-gen-fill.

​

result.seed

integer

Seed used for generation.

​

result.structured_instruction

string

The structured instruction, a JSON document serialized as a string, that `/v2/structured_instruction/generate` returns. That operation fills neither URL.

​

result.structured_prompt

string

The detailed JSON structured prompt.

​

result.video_url

string

URL of the generated video.

​

status

string

Current status of the request.Possible values: `IN_PROGRESS`, `COMPLETED`, `ERROR`, `UNKNOWN`

## 

​

Examples

### 

​

Input
    
    
    {
      "image": "https://picsum.photos/id/237/960/540",
      "season": "winter"
    }
    

### 

​

Output
    
    
    {
      "request_id": "0b3f9d7e-2c41-4a8b-9f10-6d5c8e2a4b71",
      "result": {
        "image_url": "https://example.invalid/bria/image-edit-reseason/generated.png",
        "seed": 42
      },
      "status": "COMPLETED"
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/bria/image-edit-reseason/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/bria/image-edit-reseason/code)

[Use Image Edit Replace Object By Text with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/bria/image-edit-replace-object-by-text/code)[Use Image Edit Restore with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/bria/image-edit-restore/code)

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
