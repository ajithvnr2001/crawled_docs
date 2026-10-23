---
url: https://docs.comfy.org/development/comfy-router/models/synclabs/sync-3/code/
title: Use Sync 3 with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:40.003363+00:00
---

# Use Sync 3 with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/synclabs/sync-3/code/

## On this page

  * Quick start
  * Schema
    * Input
    * Output
  * Examples
    * Input
    * Output
  * Before you ship



Synclabs

# Use Sync 3 with Comfy Router

Copy pageCopy page

Call synclabs/sync-3 through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `synclabs/sync-3`, served by Comfy Router from Synclabs. **Input:** Video, Image, Audio, Text · **Output:** Video

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `synclabs/sync-3` **Endpoint:** `POST https://api.comfy.org/v2/models/synclabs/sync-3`

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
            "synclabs/sync-3",
            {
                "input": [
                    {
                        "type": "video",
                        "url": "https://example.invalid/synclabs/sync-3/speaker.mp4",
                    },
                    {
                        "type": "audio",
                        "url": "https://example.invalid/synclabs/sync-3/voiceover.wav",
                    },
                ],
                "options": {
                    "sync_mode": "bounce",
                },
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("synclabs/sync-3", {
      input: [
        {
          type: "video",
          url: "https://example.invalid/synclabs/sync-3/speaker.mp4",
        },
        {
          type: "audio",
          url: "https://example.invalid/synclabs/sync-3/voiceover.wav",
        },
      ],
      options: {
        sync_mode: "bounce",
      },
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/synclabs/sync-3 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input\": [{\"type\":\"video\",\"url\":\"https://example.invalid/synclabs/sync-3/speaker.mp4\"},{\"type\":\"audio\",\"url\":\"https://example.invalid/synclabs/sync-3/voiceover.wav\"}], \"options\": {\"sync_mode\":\"bounce\"}}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/synclabs/sync-3/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "synclabs/sync-3",
                {
                    "input": [
                        {
                            "type": "video",
                            "url": "https://example.invalid/synclabs/sync-3/speaker.mp4",
                        },
                        {
                            "type": "audio",
                            "url": "https://example.invalid/synclabs/sync-3/voiceover.wav",
                        },
                    ],
                    "options": {
                        "sync_mode": "bounce",
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
    const handle = await comfy.models.submit("synclabs/sync-3", {
      input: [
        {
          type: "video",
          url: "https://example.invalid/synclabs/sync-3/speaker.mp4",
        },
        {
          type: "audio",
          url: "https://example.invalid/synclabs/sync-3/voiceover.wav",
        },
      ],
      options: {
        sync_mode: "bounce",
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
    curl https://api.comfy.org/v2/models/synclabs/sync-3/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input\": [{\"type\":\"video\",\"url\":\"https://example.invalid/synclabs/sync-3/speaker.mp4\"},{\"type\":\"audio\",\"url\":\"https://example.invalid/synclabs/sync-3/voiceover.wav\"}], \"options\": {\"sync_mode\":\"bounce\"}}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/synclabs/sync-3/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/synclabs/sync-3/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Schema

### 

​

Input

​

dubParams

object

Dubbing parameters attached to a Sync Labs generate request

​

dubParams.numSpeakers

integer

Number of speakers in the source video; 0 enables auto-detection

​

dubParams.providerName

string

required

Provider to use for dubbing (e.g. elevenlabs)

​

dubParams.sourceLang

string

Source language code; defaults to auto

​

dubParams.targetLang

string

required

Target language code for dubbing

​

input

object[]

required

Input items; exactly one visual input (video or image) and one audio or text input

​

input[].assetId

string

ID of an asset from the Sync Labs media library

​

input[].provider

object

Text-to-speech provider configuration for a Sync Labs text input

​

input[].provider.name

string

required

TTS provider name (e.g. elevenlabs)

​

input[].provider.script

string

required

Script to be used for generation

​

input[].provider.similarityBoost

number

How closely the AI should adhere to the original voiceFormat: `double`

​

input[].provider.stability

number

Voice stability; lower values introduce broader emotional rangeFormat: `double`

​

input[].provider.voiceId

string

required

Sync voice id (cloned voice from the Studio) or ElevenLabs voice ID

​

input[].refId

string

Reference identifier used to link this input to segment definitions

​

input[].segments_frames

integer[][]

Deprecated - use the top-level segments array instead

​

input[].segments_secs

number[][]

Deprecated - use the top-level segments array instead

​

input[].type

string

required

Input type (video, image, audio, or text)

​

input[].url

string

URL of the media to be used for generation

​

model

string

Name of the model to use for generation; only sync-3 is supported. On the Comfy Router route `POST /v2/models/synclabs/{model}` this field is supplied from the path and may be omitted.

​

options

object

Additional options available for a Sync Labs generation

​

options.active_speaker_detection

object

Active speaker detection configuration

​

options.active_speaker_detection.auto_detect

boolean

Whether to automatically detect and apply generation to the active speaker

​

options.active_speaker_detection.bounding_boxes

integer[][]

Per-frame array of bounding boxes [x1, y1, x2, y2] for the detected face

​

options.active_speaker_detection.bounding_boxes_url

string

URL to a JSON file containing bounding boxes

​

options.active_speaker_detection.coordinates

integer[]

Pixel coordinates [x, y] in the source video frame identified by frame_number

​

options.active_speaker_detection.frame_number

integer

Frame index that corresponds to the provided coordinates for manual speaker selection

​

options.active_speaker_detection.v3

boolean

Whether to use ASD v3

​

options.model_mode

string

Edit region for the model (lips, face, head); only works with react-1

​

options.occlusion_detection_enabled

boolean

Whether to detect occlusion during generation

​

options.prompt

string

Emotion prompt; only works with react-1

​

options.sync_mode

string

How to handle duration mismatches between video and audio (bounce, loop, cut_off, silence, remap)

​

options.temperature

number

How expressive lipsync can be, 0 to 1Format: `double`

​

outputFileName

string

Base filename for the generated output without extension

​

projectId

string

Optionally attach this generation to a Sync Labs project

​

segments

object[]

Segment definitions applying different audio inputs to different video segments

​

segments[].audioInput

object

required

Audio input configuration for a specific segment

​

segments[].audioInput.endTime

number

Optional end time in seconds to crop the referenced audioFormat: `double`

​

segments[].audioInput.refId

string

required

Reference ID of the audio/text-to-speech input to use for this segment

​

segments[].audioInput.startTime

number

Optional start time in seconds to crop the referenced audioFormat: `double`

​

segments[].endTime

number

required

Segment end time in secondsFormat: `double`

​

segments[].optionsOverride

object

Override generation options for a specific segment

​

segments[].optionsOverride.active_speaker_detection

object

Active speaker detection configuration

​

segments[].optionsOverride.active_speaker_detection.auto_detect

boolean

Whether to automatically detect and apply generation to the active speaker

​

segments[].optionsOverride.active_speaker_detection.bounding_boxes

integer[][]

Per-frame array of bounding boxes [x1, y1, x2, y2] for the detected face

​

segments[].optionsOverride.active_speaker_detection.bounding_boxes_url

string

URL to a JSON file containing bounding boxes

​

segments[].optionsOverride.active_speaker_detection.coordinates

integer[]

Pixel coordinates [x, y] in the source video frame identified by frame_number

​

segments[].optionsOverride.active_speaker_detection.frame_number

integer

Frame index that corresponds to the provided coordinates for manual speaker selection

​

segments[].optionsOverride.active_speaker_detection.v3

boolean

Whether to use ASD v3

​

segments[].optionsOverride.occlusion_detection_enabled

boolean

Override occlusion detection for this segment

​

segments[].optionsOverride.sync_mode

string

Override the sync mode for this segment

​

segments[].optionsOverride.temperature

number

Override temperature (0-1) for this segmentFormat: `double`

​

segments[].startTime

number

required

Segment start time in secondsFormat: `double`

​

webhookUrl

string

Webhook URL for generation status updates

Generated from the schema Router serves at `GET /v2/models/synclabs/sync-3/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

createdAt

string

The date and time the generation was created

​

error

string

The error message if the generation failed

​

errorCode

string

Stable, machine-readable error code if the generation failed

​

id

string

Unique identifier for the generation

​

input

object[]

The input items used for generation

​

input[].assetId

string

ID of an asset from the Sync Labs media library

​

input[].provider

object

Text-to-speech provider configuration for a Sync Labs text input

​

input[].provider.name

string

required

TTS provider name (e.g. elevenlabs)

​

input[].provider.script

string

required

Script to be used for generation

​

input[].provider.similarityBoost

number

How closely the AI should adhere to the original voiceFormat: `double`

​

input[].provider.stability

number

Voice stability; lower values introduce broader emotional rangeFormat: `double`

​

input[].provider.voiceId

string

required

Sync voice id (cloned voice from the Studio) or ElevenLabs voice ID

​

input[].refId

string

Reference identifier used to link this input to segment definitions

​

input[].segments_frames

integer[][]

Deprecated - use the top-level segments array instead

​

input[].segments_secs

number[][]

Deprecated - use the top-level segments array instead

​

input[].type

string

required

Input type (video, image, audio, or text)

​

input[].url

string

URL of the media to be used for generation

​

model

string

The name of the model used for generation

​

options

object

Additional options available for a Sync Labs generation

​

options.active_speaker_detection

object

Active speaker detection configuration

​

options.active_speaker_detection.auto_detect

boolean

Whether to automatically detect and apply generation to the active speaker

​

options.active_speaker_detection.bounding_boxes

integer[][]

Per-frame array of bounding boxes [x1, y1, x2, y2] for the detected face

​

options.active_speaker_detection.bounding_boxes_url

string

URL to a JSON file containing bounding boxes

​

options.active_speaker_detection.coordinates

integer[]

Pixel coordinates [x, y] in the source video frame identified by frame_number

​

options.active_speaker_detection.frame_number

integer

Frame index that corresponds to the provided coordinates for manual speaker selection

​

options.active_speaker_detection.v3

boolean

Whether to use ASD v3

​

options.model_mode

string

Edit region for the model (lips, face, head); only works with react-1

​

options.occlusion_detection_enabled

boolean

Whether to detect occlusion during generation

​

options.prompt

string

Emotion prompt; only works with react-1

​

options.sync_mode

string

How to handle duration mismatches between video and audio (bounce, loop, cut_off, silence, remap)

​

options.temperature

number

How expressive lipsync can be, 0 to 1Format: `double`

​

outputDuration

number

The duration of the output media in secondsFormat: `double`

​

outputFileName

string

The sanitized filename applied to the output media

​

outputUrl

string

The URL of the output media

​

projectId

string

The id of the project this generation is attached to

​

segmentOutputUrl

string

The URL of the segment output media

​

segments

object[]

The segments of the generation

​

segments[].audioInput

object

required

Audio input configuration for a specific segment

​

segments[].audioInput.endTime

number

Optional end time in seconds to crop the referenced audioFormat: `double`

​

segments[].audioInput.refId

string

required

Reference ID of the audio/text-to-speech input to use for this segment

​

segments[].audioInput.startTime

number

Optional start time in seconds to crop the referenced audioFormat: `double`

​

segments[].endTime

number

required

Segment end time in secondsFormat: `double`

​

segments[].optionsOverride

object

Override generation options for a specific segment

​

segments[].optionsOverride.active_speaker_detection

object

Active speaker detection configuration

​

segments[].optionsOverride.active_speaker_detection.auto_detect

boolean

Whether to automatically detect and apply generation to the active speaker

​

segments[].optionsOverride.active_speaker_detection.bounding_boxes

integer[][]

Per-frame array of bounding boxes [x1, y1, x2, y2] for the detected face

​

segments[].optionsOverride.active_speaker_detection.bounding_boxes_url

string

URL to a JSON file containing bounding boxes

​

segments[].optionsOverride.active_speaker_detection.coordinates

integer[]

Pixel coordinates [x, y] in the source video frame identified by frame_number

​

segments[].optionsOverride.active_speaker_detection.frame_number

integer

Frame index that corresponds to the provided coordinates for manual speaker selection

​

segments[].optionsOverride.active_speaker_detection.v3

boolean

Whether to use ASD v3

​

segments[].optionsOverride.occlusion_detection_enabled

boolean

Override occlusion detection for this segment

​

segments[].optionsOverride.sync_mode

string

Override the sync mode for this segment

​

segments[].optionsOverride.temperature

number

Override temperature (0-1) for this segmentFormat: `double`

​

segments[].startTime

number

required

Segment start time in secondsFormat: `double`

​

status

string

The status of the generation (PENDING, PROCESSING, COMPLETED, FAILED, REJECTED)

​

synthesizedAudioUrl

string

The URL of the audio synthesized from a text (TTS) input

​

webhookUrl

string

The URL to the webhook endpoint

## 

​

Examples

### 

​

Input
    
    
    {
      "input": [
        {
          "type": "video",
          "url": "https://example.invalid/synclabs/sync-3/speaker.mp4"
        },
        {
          "type": "audio",
          "url": "https://example.invalid/synclabs/sync-3/voiceover.wav"
        }
      ],
      "options": {
        "sync_mode": "bounce"
      }
    }
    

### 

​

Output
    
    
    {
      "createdAt": "2026-01-01T00:00:00.000Z",
      "id": "9a3d0c1e-0000-4000-8000-000000000000",
      "model": "sync-3",
      "outputDuration": 4.25,
      "outputFileName": "lipsync",
      "outputUrl": "https://example.invalid/synclabs/sync-3/output.mp4",
      "status": "COMPLETED"
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/synclabs/sync-3/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/synclabs/sync-3/code)

[Use Gen 4 Turbo with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/runway/gen4-turbo/code)[Use Hunyuan 3D Part with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/tencent/hunyuan-3d-part/code)

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
