---
url: https://docs.comfy.org/development/comfy-router/models/pika/pika-soundtrack/code/
title: Use Pika Soundtrack with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-13T15:12:13.879988+00:00
---

# Use Pika Soundtrack with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/pika/pika-soundtrack/code/

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



Pika

# Use Pika Soundtrack with Comfy Router

Copy pageCopy page

Call pika/pika-soundtrack through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `pika/pika-soundtrack`, served by Comfy Router from Pika. **Input:** Video, Text · **Output:** Video + Audio

## Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `pika/pika-soundtrack` **Endpoint:** `POST https://api.comfy.org/v2/models/pika/pika-soundtrack`

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
            "pika/pika-soundtrack",
            {
                "seed": -1,
                "video": "https://cdn.pika.art/v2/media/uploads/a7112d4d-62ed-4a11-8dee-74e89c2ec037/ae79aabfd458427495cf462f49e1cecc.mp4",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("pika/pika-soundtrack", {
      seed: -1,
      video: "https://cdn.pika.art/v2/media/uploads/a7112d4d-62ed-4a11-8dee-74e89c2ec037/ae79aabfd458427495cf462f49e1cecc.mp4",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/pika/pika-soundtrack \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"seed\": -1, \"video\": \"https://cdn.pika.art/v2/media/uploads/a7112d4d-62ed-4a11-8dee-74e89c2ec037/ae79aabfd458427495cf462f49e1cecc.mp4\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/pika/pika-soundtrack/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "pika/pika-soundtrack",
                {
                    "seed": -1,
                    "video": "https://cdn.pika.art/v2/media/uploads/a7112d4d-62ed-4a11-8dee-74e89c2ec037/ae79aabfd458427495cf462f49e1cecc.mp4",
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
    const handle = await comfy.models.submit("pika/pika-soundtrack", {
      seed: -1,
      video: "https://cdn.pika.art/v2/media/uploads/a7112d4d-62ed-4a11-8dee-74e89c2ec037/ae79aabfd458427495cf462f49e1cecc.mp4",
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
    curl https://api.comfy.org/v2/models/pika/pika-soundtrack/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"seed\": -1, \"video\": \"https://cdn.pika.art/v2/media/uploads/a7112d4d-62ed-4a11-8dee-74e89c2ec037/ae79aabfd458427495cf462f49e1cecc.mp4\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/pika/pika-soundtrack/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/pika/pika-soundtrack/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## Schema

### Input

instruction

string

What the audio should be and how it follows the action. Omit it for sound design from the video alone.

seed

integer

default:"-1"

Seed from -1 to 2147483647. -1 picks a random seed.Range: `-1` to `2147483647`

video

string

required

URL of the source video, H.264 or HEVC, at most 1200 seconds and 2 GB.

Generated from the schema Router serves at `GET /v2/models/pika/pika-soundtrack/openapi.json`, the same document it validates a call against before the request reaches the provider.

### Output

error

object

Set on a `failed` job.

error.code

string

Machine-readable failure code, such as invalid_input, content_moderation or provider_error.

error.message

string

Diagnostic text.

id

string

Job id used to poll for status.

model_id

string

The Pika catalog entry the job ran.

output

object

The finished job’s media, set when `status` is `completed`.

output.audio

object

One generated media file.

output.audio.content_type

string

MIME type of the file.

output.audio.url

string

Download URL of the generated file.

output.media_type

string

Which field carries the file: video or audio.

output.video

object

One generated media file.

output.video.content_type

string

MIME type of the file.

output.video.url

string

Download URL of the generated file.

status

string

Job status: queued, running, completed or failed.

usage

object

Units Pika reported for the job.

## Examples

### Input
    
    
    {
      "seed": -1,
      "video": "https://cdn.pika.art/v2/media/uploads/a7112d4d-62ed-4a11-8dee-74e89c2ec037/ae79aabfd458427495cf462f49e1cecc.mp4"
    }
    

### Output
    
    
    {
      "id": "media_8f3a2c91-5b7d-4e0a-9c26-31d4f2a8e6b0",
      "output": {
        "media_type": "video",
        "video": {
          "content_type": "video/mp4",
          "url": "https://example.invalid/pika/video.mp4"
        }
      },
      "status": "completed"
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/pika/pika-soundtrack/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/pika/pika-soundtrack/code)

[Pika Sfx](https://docs.comfy.org/development/comfy-router/models/pika/pika-sfx/code)[V3.5](https://docs.comfy.org/development/comfy-router/models/pixverse/v3-5/code)
