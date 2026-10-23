---
url: https://docs.comfy.org/development/comfy-router/models/veo/veo-3-1-generate-001/code/
title: Use Veo 3.1 Generate 001 with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:41.765755+00:00
---

# Use Veo 3.1 Generate 001 with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/veo/veo-3-1-generate-001/code/

## On this page

  * Quick start
  * Schema
    * Input
    * Output
  * Examples
    * Input
    * Output
  * Before you ship



Veo

# Use Veo 3.1 Generate 001 with Comfy Router

Copy pageCopy page

Call veo/veo-3.1-generate-001 through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `veo/veo-3.1-generate-001`, served by Comfy Router from Veo. **Input:** Text, Image, Video · **Output:** Video + Audio

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `veo/veo-3.1-generate-001` **Endpoint:** `POST https://api.comfy.org/v2/models/veo/veo-3.1-generate-001`

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
            "veo/veo-3.1-generate-001",
            {
                "instances": [
                    {
                        "prompt": "a single red maple leaf falling onto still water, slow motion",
                    },
                ],
                "parameters": {
                    "durationSeconds": 4,
                    "generateAudio": False,
                    "sampleCount": 1,
                },
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("veo/veo-3.1-generate-001", {
      instances: [
        {
          prompt: "a single red maple leaf falling onto still water, slow motion",
        },
      ],
      parameters: {
        durationSeconds: 4,
        generateAudio: false,
        sampleCount: 1,
      },
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/veo/veo-3.1-generate-001 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"instances\": [{\"prompt\":\"a single red maple leaf falling onto still water, slow motion\"}], \"parameters\": {\"durationSeconds\":4,\"generateAudio\":false,\"sampleCount\":1}}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/veo/veo-3.1-generate-001/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "veo/veo-3.1-generate-001",
                {
                    "instances": [
                        {
                            "prompt": "a single red maple leaf falling onto still water, slow motion",
                        },
                    ],
                    "parameters": {
                        "durationSeconds": 4,
                        "generateAudio": False,
                        "sampleCount": 1,
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
    const handle = await comfy.models.submit("veo/veo-3.1-generate-001", {
      instances: [
        {
          prompt: "a single red maple leaf falling onto still water, slow motion",
        },
      ],
      parameters: {
        durationSeconds: 4,
        generateAudio: false,
        sampleCount: 1,
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
    curl https://api.comfy.org/v2/models/veo/veo-3.1-generate-001/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"instances\": [{\"prompt\":\"a single red maple leaf falling onto still water, slow motion\"}], \"parameters\": {\"durationSeconds\":4,\"generateAudio\":false,\"sampleCount\":1}}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/veo/veo-3.1-generate-001/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/veo/veo-3.1-generate-001/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Schema

### 

​

Input

​

instances

object[]

​

instances[].cameraControl

string

Camera motion type. Requires image to be provided.Possible values: `fixed`, `pan_left`, `pan_right`, `tilt_up`, `tilt_down`, `truck_left`, `truck_right`, `pedestal_up`, `pedestal_down`, `push_in`, `pull_out`

​

instances[].image

object

Optional first frame image to guide video generation

​

instances[].image.bytesBase64Encoded

string (byte)

Base64-encoded image dataFormat: `byte`

​

instances[].image.gcsUri

string

Cloud Storage URI of the image. On a non-BYOK request a `gs://` URI (or its `https://storage.googleapis.com` form) naming a Comfy-owned bucket is refused with 400 unless the object is under your own `POST /customers/storage` prefix or is a video a previous Veo generate wrote for you.

​

instances[].image.mimeType

string

MIME type of the image (image/jpeg or image/png)Possible values: `image/jpeg`, `image/png`

​

instances[].lastFrame

object

Optional last frame image. Used with image to generate video between first and last frames. Supported by Veo 3.0+ models.

​

instances[].lastFrame.bytesBase64Encoded

string (byte)

Base64-encoded image dataFormat: `byte`

​

instances[].lastFrame.gcsUri

string

Cloud Storage URI of the image. On a non-BYOK request a `gs://` URI (or its `https://storage.googleapis.com` form) naming a Comfy-owned bucket is refused with 400 unless the object is under your own `POST /customers/storage` prefix or is a video a previous Veo generate wrote for you.

​

instances[].lastFrame.mimeType

string

MIME type of the image (image/jpeg or image/png)Possible values: `image/jpeg`, `image/png`

​

instances[].mask

object

Optional mask for video editing. Applies to input video.

​

instances[].mask.bytesBase64Encoded

string (byte)

Base64-encoded mask bytesFormat: `byte`

​

instances[].mask.gcsUri

string

Cloud Storage URI to mask file. On a non-BYOK request a `gs://` URI (or its `https://storage.googleapis.com` form) naming a Comfy-owned bucket is refused with 400 unless the object is under your own `POST /customers/storage` prefix or is a video a previous Veo generate wrote for you.

​

instances[].mask.maskMode

string

How the mask is appliedPossible values: `insert`, `remove`, `remove_static`, `outpaint`

​

instances[].mask.mimeType

string

MIME type of the mask (image/png, image/jpeg, image/webp, or video formats)

​

instances[].prompt

string

required

Text description of the video to generate

​

instances[].referenceImages

object[]

Optional reference images to guide video generation. Supports up to 3 asset images or 1 style image. Supported by Veo 3.1 models (preview).

​

instances[].referenceImages[].image

object

required

​

instances[].referenceImages[].image.bytesBase64Encoded

string (byte)

Base64-encoded image dataFormat: `byte`

​

instances[].referenceImages[].image.gcsUri

string

Cloud Storage URI of the image. On a non-BYOK request a `gs://` URI (or its `https://storage.googleapis.com` form) naming a Comfy-owned bucket is refused with 400 unless the object is under your own `POST /customers/storage` prefix or is a video a previous Veo generate wrote for you.

​

instances[].referenceImages[].image.mimeType

string

MIME type of the image (image/jpeg or image/png)Possible values: `image/jpeg`, `image/png`

​

instances[].referenceImages[].referenceId

string

Optional identifier for the reference image

​

instances[].referenceImages[].referenceType

string

required

Type of reference imagePossible values: `asset`, `style`

​

instances[].video

object

Optional input video for video extension or editing. Incompatible with image and referenceImages.

​

instances[].video.bytesBase64Encoded

string (byte)

Base64-encoded video bytesFormat: `byte`

​

instances[].video.gcsUri

string

Cloud Storage URI of the input video. On a non-BYOK request a `gs://` URI (or its `https://storage.googleapis.com` form) naming a Comfy-owned bucket is refused with 400 unless the object is under your own `POST /customers/storage` prefix or is a video a previous Veo generate wrote for you.

​

instances[].video.mimeType

string

MIME type of the videoPossible values: `video/mov`, `video/mpeg`, `video/mp4`, `video/mpg`, `video/avi`, `video/wmv`, `video/mpegps`, `video/x-flv`

​

parameters

object

​

parameters.aspectRatio

string

Aspect ratio of the generated video. Default: 16:9Possible values: `16:9`, `9:16`

​

parameters.compressionQuality

string

Video compression quality. Default: optimizedPossible values: `optimized`, `lossless`

​

parameters.durationSeconds

number

Target duration of the generated video in seconds. Veo 2: 5-8. Veo 3/3.1: 4, 6, or 8. Default: 8

​

parameters.enhancePrompt

boolean

Automatically improve prompt for higher quality. Defaults to true.

​

parameters.fps

integer

Frame rate of generated videos in frames per second

​

parameters.generateAudio

boolean

Whether to generate audio along with the video. Defaults to true. Supported by Veo 3.0+ models.

​

parameters.negativePrompt

string

Text describing what to avoid in the generated video

​

parameters.personGeneration

string

Controls people in generated videos. Default: allow_adultPossible values: `dont_allow`, `allow_adult`, `allowAll`

​

parameters.pubsubTopic

string

Cloud Pub/Sub topic for progress updates (projects/{project}/topics/{topic}). Not accepted on Comfy-credentialed (non-BYOK) requests: the generate route answers 400 if it is present, because the operation runs in Comfy’s project and Vertex would publish as Comfy’s service agent. Accepted only on bring-your-own-key requests, where Vertex evaluates the topic grant in your own project.

​

parameters.resizeMode

string

Resize approach for input image. Default: padPossible values: `pad`, `crop`

​

parameters.resolution

string

Output video resolution. Supported by Veo 3.0+ models. Default: 720pPossible values: `720p`, `1080p`, `4k`

​

parameters.sampleCount

integer

Number of videos to generate. If not specified, 1 video is generated.Range: `1` to `4`

​

parameters.seed

integer

Random seed for deterministic output. Different seeds used per video if sampleCount > 1.Format: `uint32`

​

parameters.storageUri

string

Optional Cloud Storage destination for the generated videos, as a `gs://` URI. IT MUST NAME A BUCKET OF YOUR OWN. Outside bring-your-own-key, this route runs under Comfy’s own Google Cloud credentials rather than yours, so a destination inside a Comfy-owned bucket would be a write performed by Comfy’s service account, into a shared layout, billed to Comfy’s project. A request naming one is refused with a 400 and nothing is generated — with one exception on a synchronous Comfy Router call (`POST /v2/models/{provider}/{model}`) where platform storage is enabled: a value naming Router’s own Veo or Gemini asset bucket is replaced with a destination Router mints under your own platform prefix for that call (see the Router Veo route), and only that exact Router-minted destination is let through. A queued Router submit (`POST /v2/models/{provider}/{model}/requests`) makes no such replacement, so it refuses that value with a 400 like any other Comfy-owned bucket. Any other destination is forwarded to Vertex unchanged and is yours to grant access to. A bring-your-own-key call runs in your own project and is forwarded as sent.

​

parameters.task

string

Operation type for the video generation requestPossible values: `textToVideo`, `imageToVideo`, `referenceToVideo`, `edit`, `extend`, `upscale`

Generated from the schema Router serves at `GET /v2/models/veo/veo-3.1-generate-001/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

done

boolean

Whether the operation has completed

​

error

object

Error details, present if the operation failed

​

error.code

integer

gRPC error code

​

error.message

string

Error message

​

name

string

Operation resource name

​

response

object

The prediction response, present when done is true

​

response.@type

string

​

response.raiMediaFilteredCount

integer

Number of videos filtered by responsible AI policies

​

response.raiMediaFilteredReasons

string[]

Reasons why videos were filtered by responsible AI policies

​

response.videos

object[]

​

response.videos[].bytesBase64Encoded

string

Base64-encoded video content

​

response.videos[].gcsUri

string

Cloud Storage URI of the generated video

​

response.videos[].mimeType

string

Video MIME type (video/mp4)

## 

​

Examples

### 

​

Input
    
    
    {
      "instances": [
        {
          "prompt": "a single red maple leaf falling onto still water, slow motion"
        }
      ],
      "parameters": {
        "durationSeconds": 4,
        "generateAudio": false,
        "sampleCount": 1
      }
    }
    

### 

​

Output
    
    
    {
      "done": true,
      "name": "projects/example-project/locations/us-central1/publishers/google/models/veo-3.1-fast-generate-001/operations/1a2b3c4d",
      "response": {
        "@type": "type.googleapis.com/cloud.ai.large_models.vision.GenerateVideoResponse",
        "raiMediaFilteredCount": 0,
        "videos": [
          {
            "gcsUri": "https://storage.googleapis.com/EXAMPLE_BUCKET/veo/USER_ID/REQUEST_ID/sample_0.mp4",
            "mimeType": "video/mp4"
          }
        ]
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/veo/veo-3-1-generate-001/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/veo/veo-3-1-generate-001/code)

[Use Veo 3.1 Fast Generate 001 with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/veo/veo-3-1-fast-generate-001/code)[Use Veo 3.1 Lite Generate 001 with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/veo/veo-3-1-lite-generate-001/code)

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
