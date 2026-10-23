---
url: https://docs.comfy.org/development/comfy-router/models/byteplus/seedream-5-0-260128/code/
title: Use Seedream 5.0 260128 with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:01.921337+00:00
---

# Use Seedream 5.0 260128 with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/byteplus/seedream-5-0-260128/code/

## On this page

  * Quick start
  * Schema
    * Input
    * Output
  * Examples
    * Input
    * Output
  * Before you ship



BytePlus

# Use Seedream 5.0 260128 with Comfy Router

Copy pageCopy page

Call byteplus/seedream-5-0-260128 through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `byteplus/seedream-5-0-260128`, served by Comfy Router from BytePlus. **Input:** Text, Image · **Output:** Image

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `byteplus/seedream-5-0-260128` **Endpoint:** `POST https://api.comfy.org/v2/models/byteplus/seedream-5-0-260128`

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
            "byteplus/seedream-5-0-260128",
            {
                "prompt": "A red fox trotting through a snowy pine forest, cinematic lighting",
                "response_format": "url",
                "watermark": False,
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("byteplus/seedream-5-0-260128", {
      prompt: "A red fox trotting through a snowy pine forest, cinematic lighting",
      response_format: "url",
      watermark: false,
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/byteplus/seedream-5-0-260128 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"A red fox trotting through a snowy pine forest, cinematic lighting\", \"response_format\": \"url\", \"watermark\": false}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/byteplus/seedream-5-0-260128/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "byteplus/seedream-5-0-260128",
                {
                    "prompt": "A red fox trotting through a snowy pine forest, cinematic lighting",
                    "response_format": "url",
                    "watermark": False,
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
    const handle = await comfy.models.submit("byteplus/seedream-5-0-260128", {
      prompt: "A red fox trotting through a snowy pine forest, cinematic lighting",
      response_format: "url",
      watermark: false,
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
    curl https://api.comfy.org/v2/models/byteplus/seedream-5-0-260128/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"A red fox trotting through a snowy pine forest, cinematic lighting\", \"response_format\": \"url\", \"watermark\": false}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/byteplus/seedream-5-0-260128/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/byteplus/seedream-5-0-260128/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Schema

### 

​

Input

​

guidance_scale

number

Controls how closely the output image aligns with the input prompt. Range [1, 10]. Higher values result in stronger prompt adherence. Not supported by seedream-5.0-pro, 5.0-lite, 4.5 and 4.0.Range: `1` to `10`Format: `float`

​

image

string | string[]

Seedream-5.0-pro, 5.0-lite, 4.5 and 4.0 support this parameter.Enter the Base64 encoding or an accessible URL of the image to edit. Seedream-5.0-pro, 5.0-lite, 4.5 and 4.0 support inputting a single image or multiple images (see the multi-image blending example).• Image URL: Make sure that the image URL is accessible. • Base64 encoding: The format must be data:image/<image format>;base64,<Base64 encoding>. Note: <image format> must be in lowercase, e.g., data:image/png;base64,<base64_image>.Comfy Router limits the entire JSON request to 100 MiB, including base64 expansion and all reference images. Use URLs for inputs that would exceed this transport limit.An input image must meet the following requirements: • Image format: jpeg, png (seedream-5.0-pro, 5.0-lite, 4.5 and 4.0 also support webp, bmp, tiff and gif; seedream-5.0-pro also supports heic and heif) • Aspect ratio (width/height): In the range [1/16, 16] for seedream-5.0-pro, 5.0-lite, 4.5 and 4.0 • Width and height (px): > 14 • Size: No more than 10 MB (30 MB for seedream-5.0-pro) • Total pixels: No more than 6000x6000 (36,000,000 px) for seedream-5.0-pro • Maximum of 14 reference images (10 for seedream-5.0-pro and 5.0-flash)In the layer-separation scenario (layer_decomposition enabled), image is required and only a single input image is supported (passing multiple images returns an error). Input images must be png, jpeg, webp, bmp, tiff or gif (heic and heif are not supported), up to 30 MB, with total pixels in the range [512x512, 6000x6000] and aspect ratio in [1/16, 16].

​

layer_decomposition

boolean

default:"false"

Controls whether layer separation is enabled. Only seedream-5.0-pro and 5.0-flash support this parameter. true: Layer-separation mode. The model decomposes the single input image into one base image plus multiple layers (up to 16), and returns the position and content information of each produced layer, including the stacking order (z_index), bounding box (bounding_box), name (name) and description (description). false: Standard image-generation mode; no layer separation is performed. Notes on layer-separation mode: only a single input image is supported (passing multiple images returns an error); if any single layer fails to generate, the whole request fails — partial success is not supported; at most 17 images are returned (1 base image + 16 layers). sequential_image_generation, sequential_image_generation_options, tools and stream return an error if passed.

​

model

string

Model identifier. Supported models: seedream-4-0-250828, seedream-4-5-251128, seedream-5-0-260128, seedream-5-0-pro-260628 and seedream-5-0-flash-260915. A direct v1 call to POST /proxy/byteplus/api/v3/images/generations MUST supply it — the proxy refuses any other value, and an omitted one, with a 400. It is NOT in this schema’s `required` list because Comfy Router fills it from the `{model}` path segment of /v2/models/byteplus/{model}, so a Router caller omits it.

​

optimize_prompt_options

object

Configuration for prompt optimization feature. Only seedream-5.0-pro/5.0-lite/4.5 (only support standard mode) and seedream-4.0 support this parameter.

​

optimize_prompt_options.mode

string

default:"\"standard\""

Set the mode for the prompt optimization feature. standard = Higher quality, longer generation time. fast = Faster but at a more average quality.Possible values: `standard`, `fast`

​

output_format

string

default:"\"jpeg\""

Specifies the format of the output image. Only seedream-5.0-pro, 5.0-flash and 5.0-lite support this parameter. In the layer-separation scenario, output_format only controls the format of the base image; every layer is always output as png.Possible values: `png`, `jpeg`

​

prompt

string

Text description for image generation or transformation. Optional in the layer-separation scenario (seedream-5.0-pro or 5.0-flash with layer_decomposition enabled): if a prompt is provided, the model recognizes and separates the elements you specify according to the prompt intent; if no prompt is provided, the model automatically detects all major elements in the image and separates them into independent layers.

​

response_format

string

default:"\"url\""

Specifies the format of the generated image returned in the responsePossible values: `url`, `b64_json`

​

seed

integer

default:"-1"

Random seed to control the stochasticity of image generation. Range: [-1, 2147483647]. If not specified, a seed will be automatically generated. To reproduce the same output, use the same seed value.Range: `-1` to `2147483647`

​

sequential_image_generation

string

Controls whether to disable the batch generation feature. This parameter is only supported on seedream-5.0-lite, 4.5 and 4.0 (not supported by seedream-5.0-pro or 5.0-flash). Valid values: auto: In automatic mode, the model automatically determines whether to return multiple images and how many images it will contain based on the user’s prompt. disabled: Disables batch generation feature. The model will only generate one image.Possible values: `auto`, `disabled`

​

sequential_image_generation_options

object

Only seedream-5.0-lite, 4.5 and 4.0 support this parameter (not supported by seedream-5.0-pro or 5.0-flash). Configuration for the batch image generation feature. This parameter is only effective when sequential_image_generation is set to auto.

​

sequential_image_generation_options.max_images

integer

default:"15"

Specifies the maximum number of images to generate in this request. Number of input reference images + Number of generated images ≤ 15.Range: `1` to `15`

​

size

string

“seedream-4-0-250828”: Set the specification for the generated image. Two methods are available but cannot be used together. Method 1 | Specify the resolution. Optional values: 1K, 2K, 4K Method 2 | Specify width and height in pixels. Default: 2048x2048, total pixels: [1024x1024, 4096x4096], aspect ratio: [1/16, 16] “seedream-4-5-251128”: Two methods available. Method 1 | Specify the resolution. Optional values: 2K, 4K Method 2 | Specify width and height in pixels. Default: 2048x2048, total pixels: [2560x1440, 4096x4096], aspect ratio: [1/16, 16] “seedream-5-0-260128”: Two methods available. Method 1 | Specify the resolution. Optional values: 2K, 3K Method 2 | Specify width and height in pixels. Default: 2048x2048, total pixels: [2560x1440, ~3072x3072], aspect ratio: [1/16, 16] “seedream-5-0-pro-260628”: Two methods available (cannot be used together). Method 1 | Specify the resolution and describe the aspect ratio, shape or purpose of the image in the prompt; the model decides the final size. Optional values: 1K, 2K Method 2 | Specify width and height in pixels. Default: 1024x1024, total pixels: [1024x1024 (1048576), 2048x2048 (4194304)], aspect ratio: [1/16, 16] “seedream-5-0-flash-260915”: Two methods available (cannot be used together). Method 1 | Specify the resolution and describe the aspect ratio, shape or purpose of the image in the prompt; the model decides the final size. Optional values: 1K, 1.5K, 2K. Default: 2K Method 2 | Specify width and height in pixels. Total pixels: [1280x720 (921600), 2048x2048x1.1025 (4624220)], aspect ratio: [1/16, 16] “seedream-5-0-pro-260628” and “seedream-5-0-flash-260915” with layer_decomposition enabled: Only the resolution-level method is supported. Optional values: 1K, 1.5K, 2K, auto. Default: auto. The base image is output at the specified resolution with the aspect ratio of the original input image; each layer is output close to the specified resolution, keeping the aspect ratio it had in the original image. auto: Output is based on the size and aspect ratio of the input image. Inputs within [1280x720, ~2048x2048] are output at the original input size; inputs smaller than 1K are output at 1K; inputs larger than 2K are output at 2K.

​

stream

boolean

default:"false"

Comfy Router settles an explicitly supplied stream flag to false because it captures a complete JSON result. On the v1 proxy, this field controls whether to enable streaming output mode. Only seedream-5.0-lite, 4.5 and 4.0 support this parameter (not supported by seedream-5.0-pro or 5.0-flash). false = All output images are returned at once. true = Each output image is returned immediately after generated.

​

watermark

boolean

default:"true"

Specifies whether to add a watermark to the generated image. false = No watermark, true = Adds watermark with ‘AI generated’ label

Generated from the schema Router serves at `GET /v2/models/byteplus/seedream-5-0-260128/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

created

integer

Unix timestamp (in seconds) indicating the time when the request was created

​

data

object[]

Contains information about the generated image(s). In the layer-separation scenario, the first element of the array is the base image (z_index=0), and the following elements are the layers, ordered by increasing z_index.

​

data[].b64_json

string

Base64-encoded image data (if response_format is “b64_json”)

​

data[].bounding_box

object

The bounding-box information of the region that the current layer occupies within the base image. Only layers return this field; the base image covers the whole canvas and does not return bounding_box. Returned only when layer_decomposition is true.

​

data[].bounding_box.absolute

integer[]

The absolute pixel coordinates of the layer’s bounding box, in the output base image’s coordinate system with the top-left corner at (0, 0). Coordinate format: [left, top, right, bottom].

​

data[].bounding_box.normalized

integer[]

The per-mille quantized (normalized) coordinates of the layer’s bounding box, proportionally mapped to a discrete integer range of [0, 1000] based on the base image size, truncated at a maximum of 1000. Coordinate format: [left, top, right, bottom].

​

data[].description

string

A detailed description of the current separated element, providing richer layer characteristics (such as color, state, material) than name. Only layers return this field; the base image does not. Returned only when layer_decomposition is true.

​

data[].name

string

The name/label of the current separated element, automatically generated by the model from the characteristics of the separated subject. Only layers return this field; the base image does not. Returned only when layer_decomposition is true.

​

data[].output_format

string

The file format of the output image. Only seedream-5.0-pro supports this field.

​

data[].size

string

The width and height of the image in pixels, in the format <width>x<height>. Only seedream-5.0-pro, 5.0-lite, 4.5 and 4.0 support this parameter.

​

data[].url

string (uri)

URL for image download (if response_format is “url”)Format: `uri`

​

data[].z_index

integer

The stacking order of the layer, increasing from bottom to top: 0 is the bottom-most layer (the base image); larger values sit higher. Use it to recompose the layers into the complete image at the correct stacking order. Returned only when layer_decomposition is true.

​

error

object

Error information (if any)

​

error.code

string

Upstream ModelArk error code. SensitiveContentDetected, InputTextSensitiveContentDetected, InputImageSensitiveContentDetected, InputVideoSensitiveContentDetected, InputAudioSensitiveContentDetected, OutputTextSensitiveContentDetected, OutputImageSensitiveContentDetected, OutputVideoSensitiveContentDetected and OutputAudioSensitiveContentDetected identify content-policy refusals. A family may have a dot-separated reason, such as InputImageSensitiveContentDetected.PrivacyInformation, OutputVideoSensitiveContentDetected.PolicyViolation or OutputImageSensitiveContentDetected.DeepFake. This is an open string, not an enum: other codes describe validation and provider failures. Router recognizes policy families in HTTP 400 error envelopes and HTTP 200 failed-task responses without overriding transport failures.

​

error.message

string

Error message

​

model

string

The model ID used for the request

​

usage

object

​

usage.generated_images

integer

Number of images generated by the model

​

usage.input_images

integer

The number of images input to the model. Only seedream-5.0-pro supports this field.

​

usage.output_tokens

integer

The number of tokens used for the picture generated by the model.

​

usage.total_tokens

integer

The total number of tokens consumed by this request.

## 

​

Examples

### 

​

Input
    
    
    {
      "prompt": "A red fox trotting through a snowy pine forest, cinematic lighting",
      "response_format": "url",
      "watermark": false
    }
    

### 

​

Output
    
    
    {
      "created": 1767225600,
      "data": [
        {
          "size": "1024x1024",
          "url": "https://example.invalid/byteplus/seedream-4-0-250828/generated.png"
        }
      ],
      "model": "seedream-5-0-260128",
      "usage": {
        "generated_images": 1
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/byteplus/seedream-5-0-260128/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/byteplus/seedream-5-0-260128/code)

[Use Seedream 4.5 251128 with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/byteplus/seedream-4-5-251128/code)[Use Seedream 5.0 Flash 260915 with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/byteplus/seedream-5-0-flash-260915/code)

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
