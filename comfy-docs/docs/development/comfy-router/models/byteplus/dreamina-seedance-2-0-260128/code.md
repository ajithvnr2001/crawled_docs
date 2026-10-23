---
url: https://docs.comfy.org/development/comfy-router/models/byteplus/dreamina-seedance-2-0-260128/code/
title: Use Dreamina Seedance 2.0 260128 with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:56.743876+00:00
---

# Use Dreamina Seedance 2.0 260128 with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/byteplus/dreamina-seedance-2-0-260128/code/

## On this page

  * Quick start
  * Serving providers
  * Schema
    * Input
    * Output
  * Examples
    * Input
    * Output
  * Before you ship



BytePlus

# Use Dreamina Seedance 2.0 260128 with Comfy Router

Copy pageCopy page

Call byteplus/dreamina-seedance-2-0-260128 through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `byteplus/dreamina-seedance-2-0-260128`, served by Comfy Router from BytePlus. **Input:** Text, Image, Video, Audio · **Output:** Video + Audio

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `byteplus/dreamina-seedance-2-0-260128` **Endpoint:** `POST https://api.comfy.org/v2/models/byteplus/dreamina-seedance-2-0-260128`

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
            "byteplus/dreamina-seedance-2-0-260128",
            {
                "content": [
                    {
                        "text": "A red fox trotting through a snowy pine forest",
                        "type": "text",
                    },
                ],
                "duration": 5,
                "ratio": "16:9",
                "resolution": "720p",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("byteplus/dreamina-seedance-2-0-260128", {
      content: [
        {
          text: "A red fox trotting through a snowy pine forest",
          type: "text",
        },
      ],
      duration: 5,
      ratio: "16:9",
      resolution: "720p",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/byteplus/dreamina-seedance-2-0-260128 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"content\": [{\"text\":\"A red fox trotting through a snowy pine forest\",\"type\":\"text\"}], \"duration\": 5, \"ratio\": \"16:9\", \"resolution\": \"720p\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/byteplus/dreamina-seedance-2-0-260128/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "byteplus/dreamina-seedance-2-0-260128",
                {
                    "content": [
                        {
                            "text": "A red fox trotting through a snowy pine forest",
                            "type": "text",
                        },
                    ],
                    "duration": 5,
                    "ratio": "16:9",
                    "resolution": "720p",
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
    const handle = await comfy.models.submit("byteplus/dreamina-seedance-2-0-260128", {
      content: [
        {
          text: "A red fox trotting through a snowy pine forest",
          type: "text",
        },
      ],
      duration: 5,
      ratio: "16:9",
      resolution: "720p",
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
    curl https://api.comfy.org/v2/models/byteplus/dreamina-seedance-2-0-260128/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"content\": [{\"text\":\"A red fox trotting through a snowy pine forest\",\"type\":\"text\"}], \"duration\": 5, \"ratio\": \"16:9\", \"resolution\": \"720p\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/byteplus/dreamina-seedance-2-0-260128/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/byteplus/dreamina-seedance-2-0-260128/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Serving providers

This model is served by Comfy Router directly unless the request names another provider. The providers below serve it too, on the same endpoint and with the same model ID, selected with the `model_provider` query parameter.

  * **Comfy** (default): `POST https://api.comfy.org/v2/models/byteplus/dreamina-seedance-2-0-260128`
  * **fal** , as `fal/fal-seedance-2.0`: `POST https://api.comfy.org/v2/models/byteplus/dreamina-seedance-2-0-260128?model_provider=fal`
  * **Higgsfield** , as `higgsfield/higgsfield-seedance-2.0`: `POST https://api.comfy.org/v2/models/byteplus/dreamina-seedance-2-0-260128?model_provider=higgsfield`
  * **Pika** , as `pika/pika-seedance-2.0`: `POST https://api.comfy.org/v2/models/byteplus/dreamina-seedance-2-0-260128?model_provider=pika`
  * **Runware** , as `runware/runware-seedance-2.0`: `POST https://api.comfy.org/v2/models/byteplus/dreamina-seedance-2-0-260128?model_provider=runware`
  * **WaveSpeed** , as `wavespeed/wavespeed-seedance-2.0`: `POST https://api.comfy.org/v2/models/byteplus/dreamina-seedance-2-0-260128?model_provider=wavespeed`

`strict_mode` defaults to false, so Router translates the native request body documented on this page into the provider’s own schema and translates the response back. See [`model_provider`, `strict_mode` and `fallback_provider`](https://docs.comfy.org/development/comfy-router/reference#post-v2modelsprovidermodel) in the API reference, and [Serving providers](https://docs.comfy.org/development/comfy-router/providers) for every model routed this way.

## 

​

Schema

### 

​

Input

​

callback_url

string (uri)

Callback notification address for the result of this generation taskFormat: `uri`

​

content

object[]

required

The input content for the model to generate a video

​

content[].audio_url

object

Input audio object. Only Seedance 2.5, 2.0, 2.0 fast & 2.0 mini support audio input. Seedance 2.0, 2.0 fast & 2.0 mini cannot use audio alone - they must include at least 1 image or video; Seedance 2.5 supports audio-only input.

​

content[].audio_url.url

string

required

Audio URL, Base64 encoding, or Asset ID. Audio URL: Public URL of the audio (wav, mp3). Base64: Format data:audio/<format>;base64,<content> Asset ID: Format asset://<ASSET_ID>

​

content[].draft_task

object

Seedance 2.5 only. The Draft task to render as the final video. It must be the only content item. The final video reuses the Draft task’s prompt, input assets, duration, ratio, seed, generate_audio and omni_reference_task_type; do not send them again. resolution defaults to and only supports 1080p.

​

content[].draft_task.id

string

required

The task ID returned when the Draft video was created with `draft` set to true.

​

content[].image_url

object

​

content[].image_url.url

string

required

Image content for image-to-video generation (when type is “image_url”) Image URL: Make sure that the image URL is accessible. Base64-encoded content: Format must be data:image/<format>;base64,<content> Asset ID: Format asset://<ASSET_ID>

​

content[].role

string

The role/position of the content item. For images: first_frame, last_frame, or reference_image. For videos: reference_video (Seedance 2.5, 2.0, 2.0 fast & 2.0 mini only). For audio: reference_audio (Seedance 2.5, 2.0, 2.0 fast & 2.0 mini only).Possible values: `first_frame`, `last_frame`, `reference_image`, `reference_video`, `reference_audio`

​

content[].text

string

The input text information for the model. Includes text prompt and optional parameters.Text prompt (required): Description of the video to be generated using Chinese and English characters.Parameters (optional): Add —[parameters] after the text prompt to control video specifications:

  * —resolution (—rs): 480p, 720p, 1080p (default: 720p)
  * —ratio (—rt): 21:9, 16:9, 4:3, 1:1, 3:4, 9:16, 9:21, adaptive (default: 16:9 or adaptive)
  * —duration (—dur): 3-12 seconds (default: 5)
  * —framepersecond (—fps): 24 (default: 24)
  * —watermark (—wm): true/false (default: false)
  * —seed (—seed): -1 to 2^32-1 (default: -1)
  * —camerafixed (—cf): true/false (default: false)

Example: “A beautiful landscape —ratio 16:9 —resolution 720p —duration 5”Comfy-side guardrail, not a BytePlus constraint. BytePlus publishes no text-length limit and accepted 40,000 characters under test (2026-09-17). It counts characters, not bytes, so a multi-byte prompt may be several times this size on the wire. It bounds this one field, not the request: `content` is an array, and the per-request body limit is what bounds the whole document. Comfy Router (/v2/models/byteplus/{model}) is the surface that enforces it; on a direct v1 /proxy call BytePlus’s own validator answers instead. Set far above real traffic so it never adjudicates a genuine prompt — raise it if a caller needs more.

​

content[].type

string

required

The type of the input contentPossible values: `text`, `image_url`, `video_url`, `audio_url`, `draft_task`

​

content[].video_url

object

Input video object. Only Seedance 2.5, 2.0, 2.0 fast & 2.0 mini support video input.

​

content[].video_url.url

string

required

Video URL or Asset ID. Video URL: Public URL of the video (mp4, mov). Asset ID: Format asset://<ASSET_ID>

​

draft

boolean

default:"false"

Seedance 2.5 only. Generates a 480p Draft video; resolution must be 480p. Pass the returned task ID in a `draft_task` content item to render the final 1080p video. The Draft task ID stays valid for 7 days.

​

duration

`-1` | object

Video duration in seconds. Seedance 2.5: [4,30] or -1 (auto; video editing tasks support only -1). Seedance 2.0, 2.0 fast & 2.0 mini: [4,15] or -1 (auto). Seedance 1.5 pro: [4,12] or -1. Seedance 1.0: [2,12].Range: `2` to `30`

​

execution_expires_after

integer

Task timeout threshold in seconds. Default 172800 (48h). Range: [3600, 259200].Range: `3600` to `259200`

​

generate_audio

boolean

default:"true"

Supported by Seedance 2.5, 2.0, 2.0 fast, 2.0 mini, and 1.5 pro. Whether the generated video includes audio synchronized with the visuals. true: The model outputs a video with synchronized audio. false: The model outputs a silent video. On models that support it, the generated audio track is content-checked by the provider separately from the video; a refusal there is reported as `content_policy_violation` and, because the audio differs each run, can be intermittent for an input the provider otherwise accepts. Send `false` for a silent video if that happens; this helps only when the audio was the refused modality, which a synchronous Router response names as `refusal_subject: output_audio` (a queued request does not identify it yet). A Seedance 2.5 final render inherits `generate_audio` from its Draft task, so recreate the Draft with `false` instead.

​

model

string

The ID of the model to call. Supported models: seedance-1-5-pro-251215, seedance-1-0-pro-250528, seedance-1-0-pro-fast-251015, dreamina-seedance-2-0-260128, dreamina-seedance-2-0-fast-260128, dreamina-seedance-2-0-mini and dreamina-seedance-2-5-260628. A direct v1 call to POST /proxy/byteplus/api/v3/contents/generations/tasks MUST supply it — the proxy refuses any other value, and an omitted one, with a 400. It is NOT in this schema’s `required` list because Comfy Router fills it from the `{model}` path segment of /v2/models/byteplus/{model}, so a Router caller omits it.

​

output_format

string

default:"\"mp4\""

Seedance 2.5 only. Container format of the output video. mp4: General-purpose container (H.264/AAC, yuv420p) with broad compatibility and smaller file size. mov: Professional container (H.264 High 4:4:4 Predictive/PCM, yuv444p) with high color precision, suited for post-production; larger file size.Possible values: `mp4`, `mov`

​

ratio

string

Aspect ratio of the generated video. Seedance 2.0, 2.0 fast & 2.0 mini, 1.5 pro default: adaptive. Seedance 2.5 first-frame / first-last-frame generation: the output follows the first frame’s aspect ratio, so only `adaptive` (or omitting the field) is accepted; a concrete ratio is refused with a 400 before dispatch. Seedance 2.0 accepts a concrete ratio in those modes.Possible values: `16:9`, `4:3`, `1:1`, `3:4`, `9:16`, `21:9`, `9:21`, `adaptive`

​

resolution

string

Video resolution. Seedance 2.5, 2.0, 2.0 fast & 2.0 mini, 1.5 pro, 1.0 lite default: 720p. Seedance 1.0 pro & pro-fast default: 1080p. Note: Seedance 2.0, 2.0 fast & 2.0 mini do not support 1080p. Seedance 2.5 supports 480p, 720p, and 1080p.Possible values: `480p`, `720p`, `1080p`, `4k`

​

return_last_frame

boolean

default:"false"

Whether to return the last frame image of the generated video. true: Returns the last frame image of the generated video. After setting this parameter to true, you can obtain the last frame image by calling the Querying the information about a video generation task. The last frame image is in PNG format, with its pixel width and height consistent with those of the generated video, and it contains no watermarks. Using this parameter allows the generation of multiple consecutive videos: the last frame of the previously generated video is used as the first frame of the next video task, enabling quick generation of multiple consecutive videos. false: Does not return the last frame image of the generated video.

​

seed

integer

Seed integer for controlling randomness. Range: [-1, 2^32-1]. -1 uses a random seed.Range: `-1` to `4294967295`

​

service_tier

string

Service tier for processing. Seedance 2.5, 2.0 & 2.0 fast do not support flex (offline inference).Possible values: `default`, `flex`

​

watermark

boolean

default:"false"

Whether the generated video includes a watermark.

Generated from the schema Router serves at `GET /v2/models/byteplus/dreamina-seedance-2-0-260128/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

content

object

The output after the video generation task is completed, which contains the download URL of the output video and, when BytePlus returns one, the download URL of its last frame. Both `video_url` and `last_frame_url` are RE-HOSTED onto Comfy storage; every other field here is BytePlus’s own. Nullable - BytePlus clears the URLs 24 hours after the task, and a succeeded document polled after that can carry `content` absent or null.

​

content.last_frame_url

string

Download URL for the last frame of the generated video, returned when the request set `return_last_frame`. Do not infer the image format from this URL: BytePlus documents the last frame as PNG on the request side, Router re-hosts whatever bytes it is served and types them from the upstream Content-Type or a content sniff, and `image/jpeg` is only the last-resort fallback when both fail. Router re-hosts the last frame onto Comfy storage and rewrites this field, so it is normally a Comfy-signed URL valid for up to 24 hours - signed for 24 hours when minted and replayed from a 23-hour memo, so a later poll can hand back one with as little as an hour left. When the re-host could not be performed the field keeps BytePlus’s own URL instead, which BytePlus clears 24 hours after the task. Either way the link expires, so download the frame rather than storing the URL.

​

content.output_format

string

Container format of the generated video (mp4 or mov), when BytePlus nests it inside `content`. Seedance models more commonly return it as a TOP-LEVEL sibling of `content` \- see the top-level `output_format` field - and Router reads whichever of the two is present.

​

content.video_url

string

Download URL for the output video. Router re-hosts the video onto Comfy storage and rewrites this field, so it is normally a Comfy-signed URL valid for up to 24 hours - signed for 24 hours when minted and replayed from a 23-hour memo, so a later poll can hand back one with as little as an hour left. When the re-host could not be performed the field keeps BytePlus’s own URL instead, which BytePlus clears 24 hours after the task and caps at 100 downloads on some models. Either way the link expires, so download the video rather than storing the URL.

​

created_at

integer

The time when the task was created. The value is a UNIX timestamp in seconds.

​

duration

number

The duration of the generated video in seconds. Declared as a number rather than an integer because BytePlus is not consistent about it - video tasks have been observed returning whole seconds and sibling BytePlus surfaces report fractional durations - so a client must not assume an integral value. BytePlus’s own field, returned on succeeded video tasks and forwarded unchanged.

​

error

object

The error information. If the task succeeds, null is returned. If the task fails, the error information is returned.

​

error.code

string

Upstream ModelArk error code. SensitiveContentDetected, InputTextSensitiveContentDetected, InputImageSensitiveContentDetected, InputVideoSensitiveContentDetected, InputAudioSensitiveContentDetected, OutputTextSensitiveContentDetected, OutputImageSensitiveContentDetected, OutputVideoSensitiveContentDetected and OutputAudioSensitiveContentDetected identify content-policy refusals. A family may have a dot-separated reason, such as InputImageSensitiveContentDetected.PrivacyInformation, OutputVideoSensitiveContentDetected.PolicyViolation or OutputImageSensitiveContentDetected.DeepFake. This is an open string, not an enum: other codes describe validation and provider failures. Router recognizes policy families in HTTP 400 error envelopes and HTTP 200 failed-task responses without overriding transport failures.

​

error.message

string

The error message

​

id

string

The ID of the video generation task

​

model

string

The name and version of the model used by the task

​

output_format

string

Container format of the generated video (mp4 or mov), returned at the TOP LEVEL as a sibling of `content` \- this is where the Seedance video task query returns it. BytePlus’s own field, forwarded unchanged.

​

resolution

string

The resolution of the generated video, for example `1080p`. BytePlus’s own field, returned on succeeded video tasks and forwarded unchanged.

​

seed

integer

The generation seed actually used for the task. BytePlus’s own field, returned on succeeded video tasks and forwarded unchanged.Format: `int64`

​

status

string

The state of the taskPossible values: `queued`, `running`, `cancelled`, `succeeded`, `failed`, `expired`

​

updated_at

integer

The time when the task was last updated. The value is a UNIX timestamp in seconds.

​

usage

object

The token usage for the request

​

usage.completion_tokens

integer

The number of tokens generated by the model

​

usage.total_tokens

integer

For the video generation model, the number of input tokens is not calculated and defaults to 0. Therefore, total_tokens = completion_tokens.

## 

​

Examples

### 

​

Input
    
    
    {
      "content": [
        {
          "text": "A red fox trotting through a snowy pine forest",
          "type": "text"
        }
      ],
      "duration": 5,
      "ratio": "16:9",
      "resolution": "720p"
    }
    

### 

​

Output
    
    
    {
      "content": {
        "last_frame_url": "https://example.invalid/byteplus/seedance-1-0-pro-250528/last-frame",
        "video_url": "https://example.invalid/byteplus/seedance-1-0-pro-250528/generated.mp4"
      },
      "created_at": 1767225600,
      "duration": 5,
      "error": null,
      "id": "3f7a1b28-5c0d-4e91-8a6f-1b2c3d4e5f60",
      "model": "dreamina-seedance-2-0-260128",
      "output_format": "mp4",
      "resolution": "1080p",
      "seed": 1234567890123,
      "status": "succeeded",
      "updated_at": 1767225730
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/byteplus/dreamina-seedance-2-0-260128/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/byteplus/dreamina-seedance-2-0-260128/code)

[Use Video Edit Replace Background with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/bria/video-edit-replace-background/code)[Use Dreamina Seedance 2.0 Fast 260128 with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/byteplus/dreamina-seedance-2-0-fast-260128/code)

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
