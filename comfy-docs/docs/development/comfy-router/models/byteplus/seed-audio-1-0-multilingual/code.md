---
url: https://docs.comfy.org/development/comfy-router/models/byteplus/seed-audio-1-0-multilingual/code/
title: Use Seed Audio 1.0 Multilingual with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:59.840668+00:00
---

# Use Seed Audio 1.0 Multilingual with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/byteplus/seed-audio-1-0-multilingual/code/

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

# Use Seed Audio 1.0 Multilingual with Comfy Router

Copy pageCopy page

Call byteplus/seed-audio-1.0-multilingual through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `byteplus/seed-audio-1.0-multilingual`, served by Comfy Router from BytePlus. **Input:** Text · **Output:** Audio

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `byteplus/seed-audio-1.0-multilingual` **Endpoint:** `POST https://api.comfy.org/v2/models/byteplus/seed-audio-1.0-multilingual`

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
            "byteplus/seed-audio-1.0-multilingual",
            {
                "audio_config": {
                    "format": "wav",
                    "sample_rate": 24000,
                },
                "text_prompt": "Hello from Comfy Router.",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("byteplus/seed-audio-1.0-multilingual", {
      audio_config: {
        format: "wav",
        sample_rate: 24000,
      },
      text_prompt: "Hello from Comfy Router.",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/byteplus/seed-audio-1.0-multilingual \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"audio_config\": {\"format\":\"wav\",\"sample_rate\":24000}, \"text_prompt\": \"Hello from Comfy Router.\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/byteplus/seed-audio-1.0-multilingual/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "byteplus/seed-audio-1.0-multilingual",
                {
                    "audio_config": {
                        "format": "wav",
                        "sample_rate": 24000,
                    },
                    "text_prompt": "Hello from Comfy Router.",
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
    const handle = await comfy.models.submit("byteplus/seed-audio-1.0-multilingual", {
      audio_config: {
        format: "wav",
        sample_rate: 24000,
      },
      text_prompt: "Hello from Comfy Router.",
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
    curl https://api.comfy.org/v2/models/byteplus/seed-audio-1.0-multilingual/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"audio_config\": {\"format\":\"wav\",\"sample_rate\":24000}, \"text_prompt\": \"Hello from Comfy Router.\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/byteplus/seed-audio-1.0-multilingual/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/byteplus/seed-audio-1.0-multilingual/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Schema

### 

​

Input

​

audio_config

object

Output audio configuration.

​

audio_config.enable_subtitle

boolean

Whether to enable the subtitle service. When enabled, the response includes utterance- and word-level timestamps (default: false).

​

audio_config.format

string

Output audio format: wav (default), mp3, pcm or ogg_opus.Possible values: `wav`, `mp3`, `pcm`, `ogg_opus`

​

audio_config.loudness_rate

integer

-50 to 100; 100 means 2.0x volume, -50 means 0.5x volume (default: 0).Range: `-50` to `100`

​

audio_config.pitch_rate

integer

-12 to 12 (default: 0).Range: `-12` to `12`

​

audio_config.sample_rate

integer

Output sample rate: 8000, 16000, 24000 (default), 32000, 44100 or 48000.Possible values: `8000`, `16000`, `24000`, `32000`, `44100`, `48000`

​

audio_config.speech_rate

integer

-50 to 100; 100 means 2.0x speed, -50 means 0.5x speed (default: 0).Range: `-50` to `100`

​

model

string

Model identifier. Supported models: seed-audio-1.0 and seed-audio-1.0-multilingual. A direct v1 call to POST /proxy/byteplus/api/v3/tts/create MUST supply it — the proxy refuses any other value, and an omitted one, with a 400. It is NOT in this schema’s `required` list because Comfy Router fills it from the `{model}` path segment of /v2/models/byteplus/{model}, so a Router caller omits it.

​

references

object[]

Reference resources. Omit for text-only generation. Up to 3 audio references (each up to 30 seconds and 10 MB decoded; wav, mp3, pcm or ogg_opus) or exactly 1 image reference (up to 10 MB decoded; jpeg, png or webp). Image references cannot be mixed with audio references. Those ceilings are BytePlus’s and are stated in DECODED bytes: base64 inflates an asset by about 4/3, and a Comfy Router call is capped at 100 MiB for the whole JSON document, so an inline `audio_data`/`image_data` reference sent to /v2/models/byteplus/{model} may carry roughly 75 MB decoded before the transport limit refuses it. BytePlus’s own 10 MB per-reference ceiling is therefore what binds first for any single inlined reference, and three audio references at that ceiling now fit in one body; use `audio_url`/`image_url` to keep large assets out of the request entirely.

​

references[].audio_data

string

Base64-encoded reference audio.

​

references[].audio_url

string

URL of a remote reference audio file.

​

references[].image_data

string

Base64-encoded reference image.

​

references[].image_url

string

URL of a remote reference image.

​

references[].speaker

string

Voice ID. Can be a supported Doubao TTS voice or a voice-clone voice ID.

​

text_prompt

string

required

Prompt or text to synthesize (1 to 3,000 characters; an empty string is refused). When audio references are provided, reference them by order using @Audio1, @Audio2 and @Audio3.

​

watermark

object

Watermark configuration object. An empty object is accepted.

​

watermark.aigc_metadata

object

Implicit watermark. Adds metadata to the synthesized audio header.

​

watermark.aigc_metadata.content_producer

string

Name or code of the synthesis service provider.

​

watermark.aigc_metadata.content_propagator

string

Name or code of the content distribution service provider.

​

watermark.aigc_metadata.enable

boolean

Whether to enable the implicit watermark (default: false).

​

watermark.aigc_metadata.produce_id

string

Content production ID.

​

watermark.aigc_metadata.propagate_id

string

Content distribution ID.

​

watermark.aigc_watermark

boolean

Explicit watermark switch. Adds an audio rhythm marker at the end of the synthesized audio (default: false).

Generated from the schema Router serves at `GET /v2/models/byteplus/seed-audio-1.0-multilingual/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

audio

string

Generated audio data, Base64-encoded.

​

code

integer

Status code. Refer to the official error-code document for details.

​

duration

number

Duration after speed or post-processing, in seconds.Format: `double`

​

message

string

Status details.

​

original_duration

number

Original model output duration in seconds. Used for billing and capped at 120 seconds.Format: `double`

​

subtitle

object

Subtitle information for the audio. Present only when audio_config.enable_subtitle is set to true in the request.

​

subtitle.sentences

object[]

Utterance-level subtitle information.

​

subtitle.sentences[].end_time

integer

Segment end time, in milliseconds from the beginning of the audio.

​

subtitle.sentences[].start_time

integer

Segment start time, in milliseconds from the beginning of the audio.

​

subtitle.sentences[].text

string

The complete text of the segment.

​

subtitle.text

string

Subtitle text corresponding to the audio.

​

subtitle.words

object[]

Word-level subtitle information.

​

subtitle.words[].end_time

integer

Segment end time, in milliseconds from the beginning of the audio.

​

subtitle.words[].start_time

integer

Segment start time, in milliseconds from the beginning of the audio.

​

subtitle.words[].text

string

The complete text of the segment.

​

url

string

Temporary audio URL, valid for 2 hours.

## 

​

Examples

### 

​

Input
    
    
    {
      "audio_config": {
        "format": "wav",
        "sample_rate": 24000
      },
      "text_prompt": "Hello from Comfy Router."
    }
    

### 

​

Output
    
    
    {
      "audio": "PGJhc2U2ND4=",
      "duration": 1.2,
      "original_duration": 1.2,
      "url": "https://example.invalid/byteplus/seed-audio/generated.wav"
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/byteplus/seed-audio-1-0-multilingual/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/byteplus/seed-audio-1-0-multilingual/code)

[Use Seed 2.0 Pro 260328 with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/byteplus/seed-2-0-pro-260328/code)[Use Seed Audio 1.0 with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/byteplus/seed-audio-1-0/code)

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
