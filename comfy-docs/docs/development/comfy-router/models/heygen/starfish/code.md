---
url: https://docs.comfy.org/development/comfy-router/models/heygen/starfish/code/
title: Use Starfish with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:10.028957+00:00
---

# Use Starfish with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/heygen/starfish/code/

## On this page

  * Quick start
  * Schema
    * Input
    * Output
  * Examples
    * Input
    * Output
  * Before you ship



HeyGen

# Use Starfish with Comfy Router

Copy pageCopy page

Call heygen/starfish through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `heygen/starfish`, served by Comfy Router from HeyGen. **Input:** Text · **Output:** Audio

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `heygen/starfish` **Endpoint:** `POST https://api.comfy.org/v2/models/heygen/starfish`

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
            "heygen/starfish",
            {
                "text": "Hello from Comfy. This voice is generated with the HeyGen Starfish engine.",
                "voice_id": "d2f4f24783d04e22ab49ee8fdc3715e0",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("heygen/starfish", {
      text: "Hello from Comfy. This voice is generated with the HeyGen Starfish engine.",
      voice_id: "d2f4f24783d04e22ab49ee8fdc3715e0",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/heygen/starfish \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"text\": \"Hello from Comfy. This voice is generated with the HeyGen Starfish engine.\", \"voice_id\": \"d2f4f24783d04e22ab49ee8fdc3715e0\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/heygen/starfish/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "heygen/starfish",
                {
                    "text": "Hello from Comfy. This voice is generated with the HeyGen Starfish engine.",
                    "voice_id": "d2f4f24783d04e22ab49ee8fdc3715e0",
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
    const handle = await comfy.models.submit("heygen/starfish", {
      text: "Hello from Comfy. This voice is generated with the HeyGen Starfish engine.",
      voice_id: "d2f4f24783d04e22ab49ee8fdc3715e0",
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
    curl https://api.comfy.org/v2/models/heygen/starfish/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"text\": \"Hello from Comfy. This voice is generated with the HeyGen Starfish engine.\", \"voice_id\": \"d2f4f24783d04e22ab49ee8fdc3715e0\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/heygen/starfish/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/heygen/starfish/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Schema

### 

​

Input

​

input_type

string

Type of the input: ‘text’ for plain text, ‘ssml’ for SSML markup. Defaults to ‘text’

​

language

string

Base language code (e.g. ‘en’). Auto-detected from text when omitted

​

locale

string

BCP-47 locale tag (e.g. ‘en-US’). When set, language is inferred from locale

​

speed

number

Speed multiplier (0.5-2.0)Range: `0.5` to `2`Format: `double`

​

text

string

required

Text to synthesize (1-5000 characters)

​

voice_id

string

required

Voice ID to use. The voice must support the starfish engine

Generated from the schema Router serves at `GET /v2/models/heygen/starfish/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

data

object

required

Payload of a successful HeyGen text-to-speech response

​

data.audio_url

string

required

URL of the generated audio file

​

data.duration

number

Duration of the audio in secondsFormat: `double`

​

data.request_id

string

Unique identifier for this generation request

​

data.word_timestamps

object[]

Word-level timing data

​

data.word_timestamps[].end

number

End time in secondsFormat: `double`

​

data.word_timestamps[].start

number

Start time in secondsFormat: `double`

​

data.word_timestamps[].word

string

The word

## 

​

Examples

### 

​

Input
    
    
    {
      "text": "Hello from Comfy. This voice is generated with the HeyGen Starfish engine.",
      "voice_id": "d2f4f24783d04e22ab49ee8fdc3715e0"
    }
    

### 

​

Output
    
    
    {
      "data": {
        "audio_url": "https://example.invalid/heygen/starfish/speech.mp3",
        "duration": 12.5,
        "request_id": "018f2c7a-4b1e-7c3d-9a05-6e2f8b41d0c9"
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/heygen/starfish/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/heygen/starfish/code)

[Use Nano Banana Pro with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/google/nano-banana-pro/code)[Use Higgsfield Genjutsu Motion Transfer V1.0 with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/higgsfield/higgsfield-genjutsu-motion-transfer-v1-0/code)

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
