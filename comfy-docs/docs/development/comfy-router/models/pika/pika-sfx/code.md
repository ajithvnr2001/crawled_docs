---
url: https://docs.comfy.org/development/comfy-router/models/pika/pika-sfx/code/
title: Use Pika Sfx with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-13T15:12:14.058651+00:00
---

# Use Pika Sfx with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/pika/pika-sfx/code/

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

# Use Pika Sfx with Comfy Router

Copy pageCopy page

Call pika/pika-sfx through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `pika/pika-sfx`, served by Comfy Router from Pika. **Input:** Text · **Output:** Audio

## Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `pika/pika-sfx` **Endpoint:** `POST https://api.comfy.org/v2/models/pika/pika-sfx`

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
            "pika/pika-sfx",
            {
                "duration": 2,
                "prompt": "a wooden door creaking open",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("pika/pika-sfx", {
      duration: 2,
      prompt: "a wooden door creaking open",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/pika/pika-sfx \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"duration\": 2, \"prompt\": \"a wooden door creaking open\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/pika/pika-sfx/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "pika/pika-sfx",
                {
                    "duration": 2,
                    "prompt": "a wooden door creaking open",
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
    const handle = await comfy.models.submit("pika/pika-sfx", {
      duration: 2,
      prompt: "a wooden door creaking open",
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
    curl https://api.comfy.org/v2/models/pika/pika-sfx/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"duration\": 2, \"prompt\": \"a wooden door creaking open\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/pika/pika-sfx/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/pika/pika-sfx/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## Schema

### Input

duration

number

default:"10"

Length of the sound effect in seconds, 1 to 20.Range: `1` to `20`

prompt

string

required

Description of the sound effect.

seed

integer

default:"-1"

Seed for reproducible output, -1 to 2147483647. -1 picks a random seed.Range: `-1` to `2147483647`

Generated from the schema Router serves at `GET /v2/models/pika/pika-sfx/openapi.json`, the same document it validates a call against before the request reaches the provider.

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
      "duration": 2,
      "prompt": "a wooden door creaking open"
    }
    

### Output
    
    
    {
      "id": "media_2d8e4b71-9c05-4f3a-b6d2-81e7a5c09f44",
      "output": {
        "audio": {
          "content_type": "audio/mpeg",
          "url": "https://example.invalid/pika/audio.mp3"
        },
        "media_type": "audio"
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/pika/pika-sfx/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/pika/pika-sfx/code)

[Pika Music](https://docs.comfy.org/development/comfy-router/models/pika/pika-music/code)[Pika Soundtrack](https://docs.comfy.org/development/comfy-router/models/pika/pika-soundtrack/code)
