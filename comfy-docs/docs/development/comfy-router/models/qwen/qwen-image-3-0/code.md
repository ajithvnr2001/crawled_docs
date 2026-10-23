---
url: https://docs.comfy.org/development/comfy-router/models/qwen/qwen-image-3-0/code/
title: Use Qwen Image 3.0 with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:35.171874+00:00
---

# Use Qwen Image 3.0 with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/qwen/qwen-image-3-0/code/

## On this page

  * Quick start
  * Schema
    * Input
    * Output
  * Examples
    * Input
    * Output
  * Before you ship



Qwen

# Use Qwen Image 3.0 with Comfy Router

Copy pageCopy page

Call qwen/qwen-image-3.0 through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `qwen/qwen-image-3.0`, served by Comfy Router from Qwen. **Input:** Text, Image · **Output:** Image

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `qwen/qwen-image-3.0` **Endpoint:** `POST https://api.comfy.org/v2/models/qwen/qwen-image-3.0`

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
            "qwen/qwen-image-3.0",
            {
                "input": {
                    "messages": [
                        {
                            "content": [
                                {
                                    "text": "A single red maple leaf on a plain white background.",
                                },
                            ],
                            "role": "user",
                        },
                    ],
                },
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("qwen/qwen-image-3.0", {
      input: {
        messages: [
          {
            content: [
              {
                text: "A single red maple leaf on a plain white background.",
              },
            ],
            role: "user",
          },
        ],
      },
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/qwen/qwen-image-3.0 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input\": {\"messages\":[{\"content\":[{\"text\":\"A single red maple leaf on a plain white background.\"}],\"role\":\"user\"}]}}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/qwen/qwen-image-3.0/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "qwen/qwen-image-3.0",
                {
                    "input": {
                        "messages": [
                            {
                                "content": [
                                    {
                                        "text": "A single red maple leaf on a plain white background.",
                                    },
                                ],
                                "role": "user",
                            },
                        ],
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
    const handle = await comfy.models.submit("qwen/qwen-image-3.0", {
      input: {
        messages: [
          {
            content: [
              {
                text: "A single red maple leaf on a plain white background.",
              },
            ],
            role: "user",
          },
        ],
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
    curl https://api.comfy.org/v2/models/qwen/qwen-image-3.0/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input\": {\"messages\":[{\"content\":[{\"text\":\"A single red maple leaf on a plain white background.\"}],\"role\":\"user\"}]}}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/qwen/qwen-image-3.0/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/qwen/qwen-image-3.0/requests/$REQUEST_ID \
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

The input parameter object containing the request messages

​

input.messages

object[]

required

The request content array. Only single-round conversations are supported, so the array must contain exactly one object

​

input.messages[].content

object[]

required

The message content array. Text-to-image contains one text object; image editing contains 1-3 image objects and one text object

​

input.messages[].content[].image

string

The URL or Base64 encoded data of an input image. 1-3 images are supported for image editing

​

input.messages[].content[].text

string

The positive prompt that describes the image content, style, and composition to generate or edit

​

input.messages[].role

string

required

The role of the message sender. Must be set to userPossible values: `user`

​

model

string

The ID of the model to call for multimodal image generation and editing. Available values are qwen-image-3.0-pro and qwen-image-3.0. It is NOT in this schema’s `required` list because Comfy Router fills it from the `{model}` path segment of /v2/models/qwen/{model}, so a Router caller omits it; a direct v1 call to the /proxy/ route must supply it.

​

parameters

object

Additional parameters to control image generation

​

parameters.n

integer

default:"1"

The number of output images. Range 1-6, default is 1Range: `1` to `6`

​

parameters.negative_prompt

string

The negative prompt that describes content you do not want to appear in the image

​

parameters.prompt_extend

boolean

default:"true"

Whether to enable intelligent prompt rewriting. Default is true

​

parameters.prompt_extend_mode

string

default:"\"direct\""

The prompt rewriting method, direct (default, supported for T2I and I2I) or agent (T2I only)Possible values: `direct`, `agent`

​

parameters.seed

integer

Random number seed to control randomness. Range [0, 2147483647]Range: `0` to `2147483647`

​

parameters.size

string

The output image resolution in the format width _height, for example 1024_ 1024\. The API accepts a pixel area between 262144 (512 _512) and 6553600 (2560_ 2560) with an aspect ratio between 1:8 and 8:1. If not specified, the model automatically recommends a resolution based on the prompt

​

parameters.watermark

boolean

default:"false"

Whether to add a watermark. Default is false

Generated from the schema Router serves at `GET /v2/models/qwen/qwen-image-3.0/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

code

string

The error code for the failed request (not returned if request is successful)

​

message

string

Detailed information about the failed request (not returned if request is successful)

​

output

object

Contains the model generation results

​

output.choices

object[]

The list of result options

​

output.choices[].finish_reason

string

The reason why the task stopped. The value is stop when the task completes normally

​

output.choices[].message

object

The message returned by the model

​

output.choices[].message.content

object[]

The message content containing the generated image information

​

output.choices[].message.content[].image

string

The URL of the generated image in PNG format. The link is valid for 24 hours

​

output.choices[].message.content[].text

string

A textual element returned in place of an image. An element carrying only this field produced NO asset, so a caller keys completion off `image` rather than off the presence of a content element

​

output.choices[].message.role

string

The role of the message. Fixed as assistant

​

request_id

string

Unique request identifier

​

usage

object

The resource usage of this call. Only returned on success

​

usage.input_image_count

integer

The number of input images in the request. Returns 0 for text-to-image

​

usage.input_image_type

string

The input image billing tier, qima_input_1k or qima_input_2k, determined by the output resolution pixel area

​

usage.output_height

integer

The height of the final output image in pixels

​

usage.output_image_count

integer

The actual number of output images returned

​

usage.output_image_type

string

The output image billing tier, qima_output_1k or qima_output_2k, determined by the output resolution pixel area

​

usage.output_width

integer

The width of the final output image in pixels

## 

​

Examples

### 

​

Input
    
    
    {
      "input": {
        "messages": [
          {
            "content": [
              {
                "text": "A single red maple leaf on a plain white background."
              }
            ],
            "role": "user"
          }
        ]
      }
    }
    

### 

​

Output
    
    
    {
      "output": {
        "choices": [
          {
            "finish_reason": "stop",
            "message": {
              "content": [
                {
                  "image": "https://example.invalid/qwen/generated.png"
                }
              ],
              "role": "assistant"
            }
          }
        ]
      },
      "request_id": "9f2c1b3a-5d4e-4a67-8b90-1c2d3e4f5a6b",
      "usage": {
        "input_image_count": 0,
        "output_height": 512,
        "output_image_count": 1,
        "output_image_type": "qima_output_1k",
        "output_width": 512
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/qwen/qwen-image-3-0/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/qwen/qwen-image-3-0/code)

[Use Qwen Image 3.0 Pro with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/qwen/qwen-image-3-0-pro/code)[Use Recraft V2 with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/recraft/recraftv2/code)

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
