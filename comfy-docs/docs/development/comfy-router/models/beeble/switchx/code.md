---
url: https://docs.comfy.org/development/comfy-router/models/beeble/switchx/code/
title: Use SwitchX with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:48.791576+00:00
---

# Use SwitchX with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/beeble/switchx/code/

## On this page

  * Quick start
  * Schema
    * Input
    * Output
  * Examples
    * Input
    * Output
  * Before you ship



Beeble

# Use SwitchX with Comfy Router

Copy pageCopy page

Call beeble/switchx through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `beeble/switchx`, served by Comfy Router from Beeble. **Input:** Image, Video, Text · **Output:** Image + Video

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `beeble/switchx` **Endpoint:** `POST https://api.comfy.org/v2/models/beeble/switchx`

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
            "beeble/switchx",
            {
                "alpha_mode": "auto",
                "generation_type": "image",
                "max_resolution": 720,
                "prompt": "A cinematic product photo of a glass lamp on a marble table",
                "source_uri": "https://img.freepik.com/free-photo/portrait-woman_395237-33.jpg?w=740&q=80",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("beeble/switchx", {
      alpha_mode: "auto",
      generation_type: "image",
      max_resolution: 720,
      prompt: "A cinematic product photo of a glass lamp on a marble table",
      source_uri: "https://img.freepik.com/free-photo/portrait-woman_395237-33.jpg?w=740&q=80",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/beeble/switchx \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"alpha_mode\": \"auto\", \"generation_type\": \"image\", \"max_resolution\": 720, \"prompt\": \"A cinematic product photo of a glass lamp on a marble table\", \"source_uri\": \"https://img.freepik.com/free-photo/portrait-woman_395237-33.jpg?w=740&q=80\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/beeble/switchx/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "beeble/switchx",
                {
                    "alpha_mode": "auto",
                    "generation_type": "image",
                    "max_resolution": 720,
                    "prompt": "A cinematic product photo of a glass lamp on a marble table",
                    "source_uri": "https://img.freepik.com/free-photo/portrait-woman_395237-33.jpg?w=740&q=80",
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
    const handle = await comfy.models.submit("beeble/switchx", {
      alpha_mode: "auto",
      generation_type: "image",
      max_resolution: 720,
      prompt: "A cinematic product photo of a glass lamp on a marble table",
      source_uri: "https://img.freepik.com/free-photo/portrait-woman_395237-33.jpg?w=740&q=80",
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
    curl https://api.comfy.org/v2/models/beeble/switchx/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"alpha_mode\": \"auto\", \"generation_type\": \"image\", \"max_resolution\": 720, \"prompt\": \"A cinematic product photo of a glass lamp on a marble table\", \"source_uri\": \"https://img.freepik.com/free-photo/portrait-woman_395237-33.jpg?w=740&q=80\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/beeble/switchx/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/beeble/switchx/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Schema

### 

​

Input

​

alpha_mode

string

required

Alpha mode: auto, fill, custom, or selectPossible values: `auto`, `fill`, `custom`, `select`

​

alpha_uri

string

URI of a custom alpha matte. Required when alpha_mode is custom or select. Ignored for auto or fill.

​

callback_url

string

HTTPS URL for webhook notification on completion or failure.

​

generation_type

string

required

Output type: image or videoPossible values: `image`, `video`

​

idempotency_key

string

Idempotency key for safe retries. If a job with the same key already exists for your account, the API returns the existing job’s status instead of creating a duplicate.

​

max_resolution

integer

default:"1080"

Maximum output resolution: 720 or 1080 (default: 1080).

​

prompt

string

Text description of desired output (max 2,000 chars). At least one of prompt or reference_image_uri is required.

​

reference_image_uri

string

URI of the reference image for style transfer. Accepts the same URI types as source_uri.

​

source_uri

string

required

URI of the source image or video. Accepts beeble://uploads/{id}/{filename}, https URLs, or data:{mime};base64 URIs (max 50 MB).

Generated from the schema Router serves at `GET /v2/models/beeble/switchx/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

alpha_mode

string

auto, fill, custom, or select

​

completed_at

string

ISO 8601 timestamp when the job completed or failed.

​

created_at

string

ISO 8601 timestamp when the job was created.

​

error

string

Error message (present when status is failed).

​

generation_type

string

image or video

​

id

string

required

Job identifier (swx_…)

​

modified_at

string

ISO 8601 timestamp of the last status change.

​

output

object

Signed URLs for SwitchX job outputs.

​

output.alpha

string

Alpha matte URL.

​

output.render

string

Composited output URL.

​

output.source

string

Preprocessed source URL.

​

progress

integer

Progress percentage (0-100).

​

status

string

required

Current job status.Possible values: `in_queue`, `processing`, `completed`, `failed`

​

webhook

object

Webhook delivery status for a SwitchX job.

​

webhook.attempts

integer

Number of delivery attempts so far.

​

webhook.last_error

string

Error message from the last failed delivery attempt.

​

webhook.status

string

pending, delivered, or failed

## 

​

Examples

### 

​

Input
    
    
    {
      "alpha_mode": "auto",
      "generation_type": "image",
      "max_resolution": 720,
      "prompt": "A cinematic product photo of a glass lamp on a marble table",
      "source_uri": "https://img.freepik.com/free-photo/portrait-woman_395237-33.jpg?w=740&q=80"
    }
    

### 

​

Output
    
    
    {
      "alpha_mode": "auto",
      "completed_at": "2027-01-01T00:01:04Z",
      "created_at": "2027-01-01T00:00:00Z",
      "generation_type": "image",
      "id": "swx_1a2b3c4d5e6f7a8b",
      "modified_at": "2027-01-01T00:01:04Z",
      "output": {
        "alpha": "https://example.invalid/beeble/switchx/alpha.png",
        "render": "https://example.invalid/beeble/switchx/render.png",
        "source": "https://example.invalid/beeble/switchx/source.png"
      },
      "progress": 100,
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/beeble/switchx/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/beeble/switchx/code)

[Use Claude Sonnet 5 with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/anthropic/claude-sonnet-5/code)[Use Erase V1 with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/black-forest-labs/erase-v1/code)

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
