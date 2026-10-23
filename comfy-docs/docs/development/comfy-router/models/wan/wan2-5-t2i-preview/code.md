---
url: https://docs.comfy.org/development/comfy-router/models/wan/wan2-5-t2i-preview/code/
title: Use Wan 2.5 T2I Preview with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:46.147425+00:00
---

# Use Wan 2.5 T2I Preview with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/wan/wan2-5-t2i-preview/code/

## On this page

  * Quick start
  * Schema
    * Input
    * Output
  * Examples
    * Input
    * Output
  * Before you ship



Wan

# Use Wan 2.5 T2I Preview with Comfy Router

Copy pageCopy page

Call wan/wan2.5-t2i-preview through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `wan/wan2.5-t2i-preview`, served by Comfy Router from Wan. **Input:** Text · **Output:** Image

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `wan/wan2.5-t2i-preview` **Endpoint:** `POST https://api.comfy.org/v2/models/wan/wan2.5-t2i-preview`

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
            "wan/wan2.5-t2i-preview",
            {
                "input": {
                    "prompt": "A single red maple leaf on a plain white background.",
                },
                "parameters": {
                    "n": 1,
                    "size": "1280*1280",
                },
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("wan/wan2.5-t2i-preview", {
      input: {
        prompt: "A single red maple leaf on a plain white background.",
      },
      parameters: {
        n: 1,
        size: "1280*1280",
      },
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/wan/wan2.5-t2i-preview \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input\": {\"prompt\":\"A single red maple leaf on a plain white background.\"}, \"parameters\": {\"n\":1,\"size\":\"1280*1280\"}}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/wan/wan2.5-t2i-preview/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "wan/wan2.5-t2i-preview",
                {
                    "input": {
                        "prompt": "A single red maple leaf on a plain white background.",
                    },
                    "parameters": {
                        "n": 1,
                        "size": "1280*1280",
                    },
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
    const handle = await comfy.models.submit("wan/wan2.5-t2i-preview", {
      input: {
        prompt: "A single red maple leaf on a plain white background.",
      },
      parameters: {
        n: 1,
        size: "1280*1280",
      },
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
    curl https://api.comfy.org/v2/models/wan/wan2.5-t2i-preview/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input\": {\"prompt\":\"A single red maple leaf on a plain white background.\"}, \"parameters\": {\"n\":1,\"size\":\"1280*1280\"}}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/wan/wan2.5-t2i-preview/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/wan/wan2.5-t2i-preview/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Schema

### 

​

Input

​

input

object

required

Enter basic information, such as prompt words, etc.

​

input.negative_prompt

string

Reverse prompt words to describe content that you do not want to see in the image

​

input.prompt

string

required

Positive prompt words to describe expected image elements and visual features. Support Chinese and English, length not exceeding 800 characters

​

model

string

The ID of the model to call for text-to-image generation. NOT constrained on this component: Comfy Router fills it from the `{model}` path segment of `POST /v2/models/wan/{model}`. A direct v1 call to `POST /proxy/wan/api/v1/services/aigc/text2image/image-synthesis` MUST supply it, and the enum of accepted spellings lives on that operation’s own component, `WanImageGenerationRequest`.

​

parameters

object

Image processing parameters

​

parameters.n

integer

default:"4"

Number of generated images. Range 1-4, default is 4Range: `1` to `4`

​

parameters.prompt_extend

boolean

default:"true"

Enable prompt intelligent rewriting. Default is true

​

parameters.seed

integer

Random number seed to control randomness. Range [0, 2147483647]Range: `0` to `2147483647`

​

parameters.size

string

default:"\"1280*1280\""

The output image resolution in the format width _height. Default is 1280_ 1280\. The API accepts a pixel area between 1638400 (1280 _1280) and 2073600 (1440_ 1440) with an aspect ratio between 1:4 and 4:1, so 768*2700 is valid

​

parameters.watermark

boolean

default:"false"

Whether to add watermark logo in lower right corner

Generated from the schema Router serves at `GET /v2/models/wan/wan2.5-t2i-preview/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

output

object

required

​

output.actual_prompt

string

Actual prompt after intelligent rewriting (for video tasks)

​

output.check_audio

string

Audio URL for I2V tasks with audio generation

​

output.code

string

The error code for the failed request (not returned if request is successful)

​

output.end_time

string

Task completion time

​

output.message

string

Detailed information about the failed request (not returned if request is successful)

​

output.orig_prompt

string

Original input prompt (for video tasks)

​

output.results

object[]

List of task results for image generation tasks

​

output.results[].actual_prompt

string

Actual prompt after intelligent rewriting (if enabled)

​

output.results[].code

string

Image error code (returned when some tasks fail)

​

output.results[].message

string

Image error information (returned when some tasks fail)

​

output.results[].orig_prompt

string

Original input prompt

​

output.results[].url

string

Generated image URL address

​

output.scheduled_time

string

Task execution time

​

output.submit_time

string

Task submission time

​

output.task_id

string

required

Task ID

​

output.task_metrics

object

Task result statistics for image generation tasks

​

output.task_metrics.FAILED

integer

Number of failed tasks

​

output.task_metrics.SUCCEEDED

integer

Number of successful tasks

​

output.task_metrics.TOTAL

integer

Total number of tasks

​

output.task_status

string

required

Task statusPossible values: `PENDING`, `RUNNING`, `SUCCEEDED`, `FAILED`, `CANCELED`, `UNKNOWN`

​

output.video_url

string

Video URL for completed video generation tasks. Link validity period 24 hours

​

request_id

string

required

Unique request identifier

​

usage

object

Output information statistics. Only successful results are counted

​

usage.SR

integer

Video resolution level (I2V and wan3.0-video tasks)

​

usage.duration

number

Duration of generated video in seconds (I2V and wan3.0-video tasks)

​

usage.fps

integer

Frame rate of the generated video (wan3.0-video tasks)

​

usage.image_count

integer

Number of generated images (T2I and I2I tasks)

​

usage.input_video_duration

number

Duration of the input video in seconds, 0.0 when no video input (wan3.0-video tasks)

​

usage.output_video_duration

number

Duration of the output video in seconds (wan3.0-video tasks)

​

usage.ratio

string

Aspect ratio of the generated video, e.g. 16:9 (wan3.0-video tasks)

​

usage.size

string

Image resolution (T2I and I2I tasks)

​

usage.video_count

integer

Number of generated videos (T2V tasks)

​

usage.video_duration

number

Duration of generated video in seconds (T2V tasks)

​

usage.video_ratio

string

Video resolution ratio (T2V tasks)

​

code

string

Error code for a failed request, reported at the ROOT of the envelope rather than under `output` (not returned if the request succeeded).

​

message

string

Detailed information about a failed request, reported at the ROOT of the envelope rather than under `output` (not returned if the request succeeded). Read this before falling back to `output.message`.

## 

​

Examples

### 

​

Input
    
    
    {
      "input": {
        "prompt": "A single red maple leaf on a plain white background."
      },
      "parameters": {
        "n": 1,
        "size": "1280*1280"
      }
    }
    

### 

​

Output
    
    
    {
      "output": {
        "end_time": "2027-01-01T00:00:12.000Z",
        "results": [
          {
            "actual_prompt": "a single red maple leaf resting on still water, shallow depth of field, soft morning light",
            "orig_prompt": "a single red maple leaf resting on still water",
            "url": "https://example.invalid/wan/generated-1.png"
          },
          {
            "code": "DataInspectionFailed",
            "message": "This candidate was rejected; the task as a whole succeeded.",
            "orig_prompt": "a single red maple leaf resting on still water"
          }
        ],
        "scheduled_time": "2027-01-01T00:00:01.000Z",
        "submit_time": "2027-01-01T00:00:00.000Z",
        "task_id": "0385dc79-5ff8-4d82-bcb6-7c1a9f2e4d60",
        "task_metrics": {
          "FAILED": 1,
          "SUCCEEDED": 1,
          "TOTAL": 2
        },
        "task_status": "SUCCEEDED"
      },
      "request_id": "7574ee8f-38a3-4b1e-9280-11c33ab46e51",
      "usage": {
        "image_count": 1,
        "size": "1280*1280"
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/wan/wan2-5-t2i-preview/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/wan/wan2-5-t2i-preview/code)

[Use Wan 2.5 I2V Preview with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/wan/wan2-5-i2v-preview/code)[Use Wan 2.5 T2V Preview with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/wan/wan2-5-t2v-preview/code)

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
