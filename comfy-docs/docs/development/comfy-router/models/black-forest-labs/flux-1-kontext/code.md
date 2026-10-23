---
url: https://docs.comfy.org/development/comfy-router/models/black-forest-labs/flux-1-kontext/code/
title: Use FLUX.1 Kontext with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:50.322758+00:00
---

# Use FLUX.1 Kontext with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/black-forest-labs/flux-1-kontext/code/

## On this page

  * Quick start
  * Before you ship



Black Forest Labs

# Use FLUX.1 Kontext with Comfy Router

Copy pageCopy page

Python, TypeScript and cURL snippets for calling FLUX.1 Kontext Pro and Kontext Max through Comfy Router, plus request fields and result shape

Copy pageCopy page

API Reference for FLUX.1 Kontext. FLUX.1 Kontext is Black Forest Labs’ instruction-driven image editing model: send an image and a text instruction, get the edited image back with the rest of the scene preserved. **Input:** Image, Text · **Output:** Image

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. Pick the model you want to call. Everything below, from the snippets to the schema and examples, follows your choice.

  * Kontext Pro

  * Kontext Max




**Model ID:** `bfl/flux-kontext-pro`**Endpoint:** `POST https://api.comfy.org/v2/models/bfl/flux-kontext-pro`

  * Wait for the result

  * Queue and collect later




Python

TypeScript

cURL
    
    
    import asyncio
    import base64
    from comfy_sdk import AsyncComfy
    
    with open("input.jpg", "rb") as f:
        input_image = base64.b64encode(f.read()).decode()
    
    # Reads COMFY_API_KEY from the environment.
    # The SDK automatically creates an idempotency key and reuses it for automatic retries.
    async def main():
        async with AsyncComfy() as client:
            result = await client.models.run(
                "bfl/flux-kontext-pro",
                {
                    "prompt": "replace the background with a sunlit beach, keep the subject unchanged",
                    "input_image": input_image,
                    "aspect_ratio": "1:1",
                },
            )
    
        print("image:", result["result"]["sample"])
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    import { readFile } from "node:fs/promises";
    
    const inputImage = (await readFile("input.jpg")).toString("base64");
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    type Result = { result: { sample: string } };
    const result = await comfy.models.run<Result>("bfl/flux-kontext-pro", {
      prompt: "replace the background with a sunlit beach, keep the subject unchanged",
      input_image: inputImage,
      aspect_ratio: "1:1",
    });
    if (result.kind !== "json") throw new Error("expected a JSON result");
    
    console.log("image:", result.data.result.sample);
    
    
    
    INPUT_IMAGE=$(base64 < input.jpg | tr -d '\n')
    
    curl https://api.comfy.org/v2/models/bfl/flux-kontext-pro \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"replace the background with a sunlit beach, keep the subject unchanged\", \"input_image\": \"$INPUT_IMAGE\", \"aspect_ratio\": \"1:1\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/bfl/flux-kontext-pro/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

Python

TypeScript

cURL
    
    
    import asyncio
    import base64
    from comfy_sdk import AsyncComfy
    
    with open("input.jpg", "rb") as f:
        input_image = base64.b64encode(f.read()).decode()
    
    # Reads COMFY_API_KEY from the environment.
    # Each submit() call mints its own Idempotency-Key and reuses it for automatic retries.
    async def main():
        async with AsyncComfy() as client:
            handle = await client.models.submit(
                "bfl/flux-kontext-pro",
                {
                    "prompt": "replace the background with a sunlit beach, keep the subject unchanged",
                    "input_image": input_image,
                    "aspect_ratio": "1:1",
                },
            )
            print("request_id:", handle.request_id)  # with the model ID, all another process needs
    
            # Poll until the request completes, waiting the Retry-After the server names.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # The provider's own payload, the same value models.run() returns.
            # A request that failed or was cancelled raises the typed Router error here.
            result = await handle.get()
    
        print("image:", result["result"]["sample"])
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    import { readFile } from "node:fs/promises";
    
    const inputImage = (await readFile("input.jpg")).toString("base64");
    
    // Reads COMFY_API_KEY from the environment.
    // Each submit() call mints its own Idempotency-Key and reuses it for automatic retries.
    type Result = { result: { sample: string } };
    const handle = await comfy.models.submit<Result>("bfl/flux-kontext-pro", {
      prompt: "replace the background with a sunlit beach, keep the subject unchanged",
      input_image: inputImage,
      aspect_ratio: "1:1",
    });
    console.log("requestId:", handle.requestId); // with the model ID, all another process needs
    
    // Poll until the request completes, waiting the Retry-After the server names.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // The same result models.run() returns. A request that failed or was cancelled rejects here.
    const result = await handle.get();
    if (result.kind !== "json") throw new Error("expected a JSON result");
    
    console.log("image:", result.data.result.sample);
    
    
    
    INPUT_IMAGE=$(base64 < input.jpg | tr -d '\n')
    
    # 1. Submit. Router answers 201 with request_id, status_url, response_url and cancel_url.
    curl https://api.comfy.org/v2/models/bfl/flux-kontext-pro/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"replace the background with a sunlit beach, keep the subject unchanged\", \"input_image\": \"$INPUT_IMAGE\", \"aspect_ratio\": \"1:1\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/bfl/flux-kontext-pro/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/bfl/flux-kontext-pro/requests/$REQUEST_ID \
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

Aspect ratio of the output between 21:9 and 9:21, e.g. 16:9. Defaults to the input image’s aspect ratio when one is given, otherwise 1:1.

​

input_image

string

Image to edit, as a base64-encoded image or an http(s) URL. Optional; without it the model generates from the prompt alone.

​

input_image_2

string

Additional reference image, base64-encoded or an http(s) URL (experimental multi-reference).

​

input_image_3

string

Additional reference image, base64-encoded or an http(s) URL (experimental multi-reference).

​

input_image_4

string

Additional reference image, base64-encoded or an http(s) URL (experimental multi-reference).

​

output_format

string

default:"\"png\""

Output image format.Possible values: `jpeg`, `png`, `webp`

​

prompt

string

required

Text prompt describing the edit to apply to input_image, or the image to generate when no input_image is given.

​

prompt_upsampling

boolean

default:"false"

Whether to upsample the prompt. If active, the prompt is automatically modified for more creative generation.

​

safety_tolerance

integer

default:"2"

Tolerance level for input and output moderation, between 0 (most strict) and 6 (least strict).Range: `0` to `6`

​

seed

integer

Optional seed for reproducibility. A random seed is used when omitted.

​

webhook_secret

string

Optional secret for webhook signature verification.

​

webhook_url

string (uri)

URL to receive webhook notifications.Format: `uri`

Generated from the schema Router serves at `GET /v2/models/bfl/flux-kontext-pro/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

cost

number

Provider-reported cost in credits, populated once the task is Ready.Format: `float`

​

id

string

required

BFL task identifier.

​

progress

number

Optional generation progress reported by BFL.Range: `0` to `1`Format: `float`

​

result

object

required

The finished generation. Not nullable here: this component’s `required` entry is a promise that a `200` carries the result, and a nullable `result` would reduce it to a key-presence check.

​

result.cost

number

Provider-reported cost of the generation. This is BFL’s number, not the Comfy charge.Format: `double`

​

result.duration

number

Provider-reported generation duration in seconds.Format: `double`

​

result.end_time

number

Provider-reported completion time of the generation, in seconds since the Unix epoch. `double` for the same reason as `start_time`.Format: `double`

​

result.prompt

string

The prompt the generation actually ran, after any prompt upsampling.

​

result.sample

string (uri)

Signed URL for the generated asset. Router re-hosts the asset onto Comfy storage and rewrites this field, so it is normally a Comfy-hosted URL valid for up to 24 hours - signed for 24 hours when minted, and replayed from a 23-hour memo, so a later poll can hand back one with as little as an hour left; a leaf whose re-host could not be performed keeps BFL’s own short-lived delivery URL instead - roughly two hours for video, roughly ten minutes for images. Either way the link expires, so download the asset rather than storing the URL.Format: `uri`

​

result.seed

integer

The seed the generation used, whether supplied or chosen by the provider. Declared `int64` because BFL returns seeds above 2^31 (e.g. 2784347701), which an unformatted `integer` generates as a 32-bit field in many SDK generators.Format: `int64`

​

result.start_time

number

Provider-reported start time of the generation, in seconds since the Unix epoch. `double`, not `float`: float32 spacing near a present-day epoch value is ~128 seconds, which collapses a whole generation’s span to a single decoded value.Format: `double`

​

status

string

required

Task status: Pending, Reasoning, Generating, Ready, Request Moderated, Content Moderated, Error, or Task not found.

## 

​

Examples

### 

​

Input
    
    
    {
      "prompt": "replace the background with a sunlit beach, keep the subject unchanged",
      "input_image": "<base64 of input.jpg>",
      "aspect_ratio": "1:1"
    }
    

### 

​

Output
    
    
    {
      "id": "0a1b2c3d-...",
      "status": "Ready",
      "result": {
        "sample": "https://.../out.png",
        "prompt": "replace the background with a sunlit beach, keep the subject unchanged",
        "seed": 1234567890
      }
    }
    

The URL is temporary. Download the image promptly if you need to keep it.

**Model ID:** `bfl/flux-kontext-max`**Endpoint:** `POST https://api.comfy.org/v2/models/bfl/flux-kontext-max`

  * Wait for the result

  * Queue and collect later




Python

TypeScript

cURL
    
    
    import asyncio
    import base64
    from comfy_sdk import AsyncComfy
    
    with open("input.jpg", "rb") as f:
        input_image = base64.b64encode(f.read()).decode()
    
    # Reads COMFY_API_KEY from the environment.
    # The SDK automatically creates an idempotency key and reuses it for automatic retries.
    async def main():
        async with AsyncComfy() as client:
            result = await client.models.run(
                "bfl/flux-kontext-max",
                {
                    "prompt": "replace the background with a sunlit beach, keep the subject unchanged",
                    "input_image": input_image,
                    "aspect_ratio": "1:1",
                },
            )
    
        print("image:", result["result"]["sample"])
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    import { readFile } from "node:fs/promises";
    
    const inputImage = (await readFile("input.jpg")).toString("base64");
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    type Result = { result: { sample: string } };
    const result = await comfy.models.run<Result>("bfl/flux-kontext-max", {
      prompt: "replace the background with a sunlit beach, keep the subject unchanged",
      input_image: inputImage,
      aspect_ratio: "1:1",
    });
    if (result.kind !== "json") throw new Error("expected a JSON result");
    
    console.log("image:", result.data.result.sample);
    
    
    
    INPUT_IMAGE=$(base64 < input.jpg | tr -d '\n')
    
    curl https://api.comfy.org/v2/models/bfl/flux-kontext-max \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"replace the background with a sunlit beach, keep the subject unchanged\", \"input_image\": \"$INPUT_IMAGE\", \"aspect_ratio\": \"1:1\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/bfl/flux-kontext-max/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

Python

TypeScript

cURL
    
    
    import asyncio
    import base64
    from comfy_sdk import AsyncComfy
    
    with open("input.jpg", "rb") as f:
        input_image = base64.b64encode(f.read()).decode()
    
    # Reads COMFY_API_KEY from the environment.
    # Each submit() call mints its own Idempotency-Key and reuses it for automatic retries.
    async def main():
        async with AsyncComfy() as client:
            handle = await client.models.submit(
                "bfl/flux-kontext-max",
                {
                    "prompt": "replace the background with a sunlit beach, keep the subject unchanged",
                    "input_image": input_image,
                    "aspect_ratio": "1:1",
                },
            )
            print("request_id:", handle.request_id)  # with the model ID, all another process needs
    
            # Poll until the request completes, waiting the Retry-After the server names.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # The provider's own payload, the same value models.run() returns.
            # A request that failed or was cancelled raises the typed Router error here.
            result = await handle.get()
    
        print("image:", result["result"]["sample"])
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    import { readFile } from "node:fs/promises";
    
    const inputImage = (await readFile("input.jpg")).toString("base64");
    
    // Reads COMFY_API_KEY from the environment.
    // Each submit() call mints its own Idempotency-Key and reuses it for automatic retries.
    type Result = { result: { sample: string } };
    const handle = await comfy.models.submit<Result>("bfl/flux-kontext-max", {
      prompt: "replace the background with a sunlit beach, keep the subject unchanged",
      input_image: inputImage,
      aspect_ratio: "1:1",
    });
    console.log("requestId:", handle.requestId); // with the model ID, all another process needs
    
    // Poll until the request completes, waiting the Retry-After the server names.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // The same result models.run() returns. A request that failed or was cancelled rejects here.
    const result = await handle.get();
    if (result.kind !== "json") throw new Error("expected a JSON result");
    
    console.log("image:", result.data.result.sample);
    
    
    
    INPUT_IMAGE=$(base64 < input.jpg | tr -d '\n')
    
    # 1. Submit. Router answers 201 with request_id, status_url, response_url and cancel_url.
    curl https://api.comfy.org/v2/models/bfl/flux-kontext-max/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"replace the background with a sunlit beach, keep the subject unchanged\", \"input_image\": \"$INPUT_IMAGE\", \"aspect_ratio\": \"1:1\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/bfl/flux-kontext-max/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/bfl/flux-kontext-max/requests/$REQUEST_ID \
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

Aspect ratio of the output between 21:9 and 9:21, e.g. 16:9. Defaults to the input image’s aspect ratio when one is given, otherwise 1:1.

​

input_image

string

Image to edit, as a base64-encoded image or an http(s) URL. Optional; without it the model generates from the prompt alone.

​

input_image_2

string

Additional reference image, base64-encoded or an http(s) URL (experimental multi-reference).

​

input_image_3

string

Additional reference image, base64-encoded or an http(s) URL (experimental multi-reference).

​

input_image_4

string

Additional reference image, base64-encoded or an http(s) URL (experimental multi-reference).

​

output_format

string

default:"\"png\""

Output image format.Possible values: `jpeg`, `png`, `webp`

​

prompt

string

required

Text prompt describing the edit to apply to input_image, or the image to generate when no input_image is given.

​

prompt_upsampling

boolean

default:"false"

Whether to upsample the prompt. If active, the prompt is automatically modified for more creative generation.

​

safety_tolerance

integer

default:"2"

Tolerance level for input and output moderation, between 0 (most strict) and 6 (least strict).Range: `0` to `6`

​

seed

integer

Optional seed for reproducibility. A random seed is used when omitted.

​

webhook_secret

string

Optional secret for webhook signature verification.

​

webhook_url

string (uri)

URL to receive webhook notifications.Format: `uri`

Generated from the schema Router serves at `GET /v2/models/bfl/flux-kontext-max/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

cost

number

Provider-reported cost in credits, populated once the task is Ready.Format: `float`

​

id

string

required

BFL task identifier.

​

progress

number

Optional generation progress reported by BFL.Range: `0` to `1`Format: `float`

​

result

object

required

The finished generation. Not nullable here: this component’s `required` entry is a promise that a `200` carries the result, and a nullable `result` would reduce it to a key-presence check.

​

result.cost

number

Provider-reported cost of the generation. This is BFL’s number, not the Comfy charge.Format: `double`

​

result.duration

number

Provider-reported generation duration in seconds.Format: `double`

​

result.end_time

number

Provider-reported completion time of the generation, in seconds since the Unix epoch. `double` for the same reason as `start_time`.Format: `double`

​

result.prompt

string

The prompt the generation actually ran, after any prompt upsampling.

​

result.sample

string (uri)

Signed URL for the generated asset. Router re-hosts the asset onto Comfy storage and rewrites this field, so it is normally a Comfy-hosted URL valid for up to 24 hours - signed for 24 hours when minted, and replayed from a 23-hour memo, so a later poll can hand back one with as little as an hour left; a leaf whose re-host could not be performed keeps BFL’s own short-lived delivery URL instead - roughly two hours for video, roughly ten minutes for images. Either way the link expires, so download the asset rather than storing the URL.Format: `uri`

​

result.seed

integer

The seed the generation used, whether supplied or chosen by the provider. Declared `int64` because BFL returns seeds above 2^31 (e.g. 2784347701), which an unformatted `integer` generates as a 32-bit field in many SDK generators.Format: `int64`

​

result.start_time

number

Provider-reported start time of the generation, in seconds since the Unix epoch. `double`, not `float`: float32 spacing near a present-day epoch value is ~128 seconds, which collapses a whole generation’s span to a single decoded value.Format: `double`

​

status

string

required

Task status: Pending, Reasoning, Generating, Ready, Request Moderated, Content Moderated, Error, or Task not found.

## 

​

Examples

### 

​

Input
    
    
    {
      "prompt": "replace the background with a sunlit beach, keep the subject unchanged",
      "input_image": "<base64 of input.jpg>",
      "aspect_ratio": "1:1"
    }
    

### 

​

Output
    
    
    {
      "id": "0a1b2c3d-...",
      "status": "Ready",
      "result": {
        "sample": "https://.../out.png",
        "prompt": "replace the background with a sunlit beach, keep the subject unchanged",
        "seed": 1234567890
      }
    }
    

The URL is temporary. Download the image promptly if you need to keep it.

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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/black-forest-labs/flux-1-kontext/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/black-forest-labs/flux-1-kontext/code)

[Use Flux 1.1 Pro Ultra Image with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/black-forest-labs/flux-1-1-pro-ultra-image/code)[Use FLUX 2 Max with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/black-forest-labs/flux-2-max/code)

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
