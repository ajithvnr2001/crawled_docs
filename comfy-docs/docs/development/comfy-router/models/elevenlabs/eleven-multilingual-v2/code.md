---
url: https://docs.comfy.org/development/comfy-router/models/elevenlabs/eleven-multilingual-v2/code/
title: Use Eleven Multilingual V2 with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-19T14:35:02.080656+00:00
---

# Use Eleven Multilingual V2 with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/elevenlabs/eleven-multilingual-v2/code/

## On this page

  * Quick start
  * Schema
    * Input
    * Output
  * Examples
    * Input
    * Output
  * Before you ship



Elevenlabs

# Use Eleven Multilingual V2 with Comfy Router

Copy pageCopy page

Call elevenlabs/eleven_multilingual_v2 through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `elevenlabs/eleven_multilingual_v2`, served by Comfy Router from Elevenlabs. **Input:** Text · **Output:** Audio

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `elevenlabs/eleven_multilingual_v2` **Endpoint:** `POST https://api.comfy.org/v2/models/elevenlabs/eleven_multilingual_v2`

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
            "elevenlabs/eleven_multilingual_v2",
            {
                "text": "Hello from Comfy Router.",
                "voice_id": "21m00Tcm4TlvDq8ikWAM",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("elevenlabs/eleven_multilingual_v2", {
      text: "Hello from Comfy Router.",
      voice_id: "21m00Tcm4TlvDq8ikWAM",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/elevenlabs/eleven_multilingual_v2 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"text\": \"Hello from Comfy Router.\", \"voice_id\": \"21m00Tcm4TlvDq8ikWAM\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/elevenlabs/eleven_multilingual_v2/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "elevenlabs/eleven_multilingual_v2",
                {
                    "text": "Hello from Comfy Router.",
                    "voice_id": "21m00Tcm4TlvDq8ikWAM",
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
    const handle = await comfy.models.submit("elevenlabs/eleven_multilingual_v2", {
      text: "Hello from Comfy Router.",
      voice_id: "21m00Tcm4TlvDq8ikWAM",
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
    curl https://api.comfy.org/v2/models/elevenlabs/eleven_multilingual_v2/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"text\": \"Hello from Comfy Router.\", \"voice_id\": \"21m00Tcm4TlvDq8ikWAM\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/elevenlabs/eleven_multilingual_v2/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/elevenlabs/eleven_multilingual_v2/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Schema

### 

​

Input

​

apply_language_text_normalization

boolean

default:"false"

Controls language-specific text normalization. Can heavily increase latency. Currently only supported for Japanese.

​

apply_text_normalization

string

default:"\"auto\""

Controls text normalization. ‘auto’ lets the system decide, ‘on’ always applies normalization, ‘off’ skips normalization.Possible values: `auto`, `on`, `off`

​

language_code

string

Language code (ISO 639-1) to enforce for the model. If unsupported, an error is returned.

​

model_id

string

default:"\"eleven_multilingual_v2\""

Identifier of the model to use. Query /v1/models to list available models.

​

next_request_ids

string[]

Request IDs of next generations for continuity. Maximum 3.

​

next_text

string

Text that comes after this request, used to improve speech continuity.

​

previous_request_ids

string[]

Request IDs of previous generations for continuity. Maximum 3.

​

previous_text

string

Text that came before this request, used to improve speech continuity.

​

pronunciation_dictionary_locators

object[]

List of pronunciation dictionary locators (id, version_id). Maximum 3 per request.

​

pronunciation_dictionary_locators[].pronunciation_dictionary_id

string

required

The ID of the pronunciation dictionary

​

pronunciation_dictionary_locators[].version_id

string

required

The version ID of the pronunciation dictionary

​

seed

integer

Seed for deterministic generation. Must be between 0 and 4294967295.Range: `0` to `4294967295`

​

text

string

required

The text that will be converted into speech.

​

use_pvc_as_ivc

boolean

default:"false"

Deprecated. If true, uses IVC version of voice instead of PVC.

​

voice_settings

object

Voice settings configuration

​

voice_settings.similarity_boost

number

default:"0.75"

How closely the AI adheres to the original voice when replicating it.Range: `0` to `1`Format: `double`

​

voice_settings.speed

number

default:"1"

Speed adjustment. 1.0 is default, values below slow down, values above speed up.Range: `0.7` to `1.2`Format: `double`

​

voice_settings.stability

number

default:"0.5"

Stability of the voice. Lower values introduce broader emotional range.Range: `0` to `1`Format: `double`

​

voice_settings.style

number

default:"0"

Style exaggeration. Amplifies the style of the original speaker.Range: `0` to `1`Format: `double`

​

voice_settings.use_speaker_boost

boolean

default:"true"

Boosts similarity to the original speaker. Requires higher computational load.

​

voice_id

string

required

ID of the voice to use, letters and digits only. Router places it in the ElevenLabs request path.

Generated from the schema Router serves at `GET /v2/models/elevenlabs/eleven_multilingual_v2/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

*/*

string (binary)

Raw audio bytes. The Content-Type and encoding follow the requested output_format and are forwarded from ElevenLabs. The example is a placeholder for the binary body, not JSON or base64.

## 

​

Examples

### 

​

Input
    
    
    {
      "text": "Hello from Comfy Router.",
      "voice_id": "21m00Tcm4TlvDq8ikWAM"
    }
    

### 

​

Output

Binary body: raw bytes rather than a JSON document, returned as `*/*`, so there is no JSON example to show. The response `Content-Type` and encoding follow the request, as the Output schema above describes.

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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/elevenlabs/eleven-multilingual-v2/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/elevenlabs/eleven-multilingual-v2/code)

[Use Seedream 5.0 Pro 260628 with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/byteplus/seedream-5-0-pro-260628/code)[Use Eleven Sfx V2 with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/elevenlabs/eleven-sfx-v2/code)

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
