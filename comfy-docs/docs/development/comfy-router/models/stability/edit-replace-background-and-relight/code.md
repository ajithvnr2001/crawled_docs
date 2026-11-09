---
url: https://docs.comfy.org/development/comfy-router/models/stability/edit-replace-background-and-relight/code/
title: Use Edit Replace Background And Relight with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-09T17:17:29.566890+00:00
---

# Use Edit Replace Background And Relight with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/stability/edit-replace-background-and-relight/code/

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



Stability

# Use Edit Replace Background And Relight with Comfy Router

Copy pageCopy page

Call stability/edit-replace-background-and-relight through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `stability/edit-replace-background-and-relight`, served by Comfy Router from Stability. **Input:** Text, Image · **Output:** Image

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `stability/edit-replace-background-and-relight` **Endpoint:** `POST https://api.comfy.org/v2/models/stability/edit-replace-background-and-relight`

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
            "stability/edit-replace-background-and-relight",
            {
                "background_prompt": "a sunlit beach at golden hour",
                "light_source_direction": "above",
                "light_source_strength": 0.5,
                "seed": 12345,
                "subject_image": "https://storage.googleapis.com/example-bucket/subject.png",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("stability/edit-replace-background-and-relight", {
      background_prompt: "a sunlit beach at golden hour",
      light_source_direction: "above",
      light_source_strength: 0.5,
      seed: 12345,
      subject_image: "https://storage.googleapis.com/example-bucket/subject.png",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/stability/edit-replace-background-and-relight \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"background_prompt\": \"a sunlit beach at golden hour\", \"light_source_direction\": \"above\", \"light_source_strength\": 0.5, \"seed\": 12345, \"subject_image\": \"https://storage.googleapis.com/example-bucket/subject.png\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/stability/edit-replace-background-and-relight/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "stability/edit-replace-background-and-relight",
                {
                    "background_prompt": "a sunlit beach at golden hour",
                    "light_source_direction": "above",
                    "light_source_strength": 0.5,
                    "seed": 12345,
                    "subject_image": "https://storage.googleapis.com/example-bucket/subject.png",
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
    const handle = await comfy.models.submit("stability/edit-replace-background-and-relight", {
      background_prompt: "a sunlit beach at golden hour",
      light_source_direction: "above",
      light_source_strength: 0.5,
      seed: 12345,
      subject_image: "https://storage.googleapis.com/example-bucket/subject.png",
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
    curl https://api.comfy.org/v2/models/stability/edit-replace-background-and-relight/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"background_prompt\": \"a sunlit beach at golden hour\", \"light_source_direction\": \"above\", \"light_source_strength\": 0.5, \"seed\": 12345, \"subject_image\": \"https://storage.googleapis.com/example-bucket/subject.png\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/stability/edit-replace-background-and-relight/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/stability/edit-replace-background-and-relight/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Schema

### 

​

Input

​

background_prompt

string

The new background. Required when `background_reference` is omitted.

​

background_reference

string (uri)

A Comfy-signed asset URL of an image the new background follows.Format: `uri`

​

foreground_prompt

string

What the subject is.

​

keep_original_background

string

`true` keeps elements of the original background. Default `false`. A string, as in Stability’s form fields.Possible values: `true`, `false`

​

light_reference

string (uri)

A Comfy-signed asset URL of an image the lighting follows.Format: `uri`

​

light_source_direction

string

Where the light comes from. `left` is not offered.Possible values: `right`, `below`, `above`

​

light_source_strength

number

How strong the light is. Needs `light_reference` or `light_source_direction`.Range: `0` to `1`

​

negative_prompt

string

What to keep out of the image.

​

original_background_depth

number

How closely the new background matches the subject’s depth. Default 0.5.Range: `0` to `1`

​

output_format

string

Only `png` is returned.Possible values: `png`

​

preserve_original_subject

number

How exactly to keep the original subject. Default 0.6.Range: `0` to `1`

​

seed

integer

0 or omitted picks a random seed.Range: `0` to `4294967294`

​

subject_image

string (uri)

required

A Comfy-signed asset URL of the image whose subject is kept.Format: `uri`

Generated from the schema Router serves at `GET /v2/models/stability/edit-replace-background-and-relight/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

finish_reason

string

required

Always SUCCESS on a 200.

​

image

string (uri)

required

Comfy-signed URL of the (first) PNG image, valid for up to 24 hours.Format: `uri`

​

images

string (uri)[]

SDXL only, when more than one image was returned. Every Comfy-signed image URL, in output order, each valid for up to 24 hours.

​

seed

integer

required

The seed the image was generated with.

## 

​

Examples

### 

​

Input
    
    
    {
      "background_prompt": "a sunlit beach at golden hour",
      "light_source_direction": "above",
      "light_source_strength": 0.5,
      "seed": 12345,
      "subject_image": "https://storage.googleapis.com/example-bucket/subject.png"
    }
    

### 

​

Output
    
    
    {
      "finish_reason": "SUCCESS",
      "image": "https://example.invalid/stability/image.png",
      "seed": 12345
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/stability/edit-replace-background-and-relight/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/stability/edit-replace-background-and-relight/code)

[Edit Remove Background](https://docs.comfy.org/development/comfy-router/models/stability/edit-remove-background/code)[Edit Search And Recolor](https://docs.comfy.org/development/comfy-router/models/stability/edit-search-and-recolor/code)
