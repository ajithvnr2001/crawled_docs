---
url: https://docs.comfy.org/development/comfy-router/models/elevenlabs/eleven-v4/code/
title: Use Eleven V4 with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:03.673393+00:00
---

# Use Eleven V4 with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/elevenlabs/eleven-v4/code/

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

# Use Eleven V4 with Comfy Router

Copy pageCopy page

Call elevenlabs/eleven_v4 through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `elevenlabs/eleven_v4`, served by Comfy Router from Elevenlabs. **Input:** Text · **Output:** Audio

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `elevenlabs/eleven_v4` **Endpoint:** `POST https://api.comfy.org/v2/models/elevenlabs/eleven_v4`

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
            "elevenlabs/eleven_v4",
            {
                "inputs": [
                    {
                        "text": "Hello from Comfy Router.",
                        "voice_id": "21m00Tcm4TlvDq8ikWAM",
                    },
                ],
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("elevenlabs/eleven_v4", {
      inputs: [
        {
          text: "Hello from Comfy Router.",
          voice_id: "21m00Tcm4TlvDq8ikWAM",
        },
      ],
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/elevenlabs/eleven_v4 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"inputs\": [{\"text\":\"Hello from Comfy Router.\",\"voice_id\":\"21m00Tcm4TlvDq8ikWAM\"}]}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/elevenlabs/eleven_v4/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "elevenlabs/eleven_v4",
                {
                    "inputs": [
                        {
                            "text": "Hello from Comfy Router.",
                            "voice_id": "21m00Tcm4TlvDq8ikWAM",
                        },
                    ],
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
    const handle = await comfy.models.submit("elevenlabs/eleven_v4", {
      inputs: [
        {
          text: "Hello from Comfy Router.",
          voice_id: "21m00Tcm4TlvDq8ikWAM",
        },
      ],
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
    curl https://api.comfy.org/v2/models/elevenlabs/eleven_v4/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"inputs\": [{\"text\":\"Hello from Comfy Router.\",\"voice_id\":\"21m00Tcm4TlvDq8ikWAM\"}]}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/elevenlabs/eleven_v4/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/elevenlabs/eleven_v4/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Schema

### 

​

Input

​

apply_text_normalization

string

default:"\"auto\""

Controls text normalization with three modes: ‘auto’ - system automatically decides whether to apply text normalization ‘on’ - text normalization will always be applied ‘off’ - text normalization will be skippedPossible values: `auto`, `on`, `off`

​

inputs

object[]

required

A list of dialogue inputs, each containing text and a voice ID which will be converted into speech. The maximum number of unique voice IDs is 10.

​

inputs[].text

string

required

The text to be converted into speech.

​

inputs[].voice_id

string

required

The ID of the voice to be used for the generation.

​

language_code

string

Language code (ISO 639-1) used to enforce a language for the model and text normalization. If the model does not support provided language code, an error will be returned.

​

model_id

string

Identifier of the model that will be used. This route admits ‘eleven_v3’, ‘eleven_v4’ and ‘eleven_v4_turbo’ and nothing else; any other value is rejected with 400 before the request reaches ElevenLabs. The upstream ElevenLabs advice to query GET /v1/models for the available set does NOT describe this route, which serves only these models. It is NOT in this schema’s `required` list because Comfy Router fills it from the `{model}` path segment of /v2/models/elevenlabs/{model}, so a Router caller omits it.

​

pronunciation_dictionary_locators

object[]

A list of pronunciation dictionary locators (id, version_id) to be applied to the text. They will be applied in order. You may have up to 3 locators per request.

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

If specified, our system will make a best effort to sample deterministically. Repeated requests with the same seed and parameters should return the same result. Must be integer between 0 and 4294967295.Range: `0` to `4294967295`

​

settings

object

Settings controlling the dialogue generation

​

settings.stability

number

default:"0.5"

Determines how stable the voice is and the randomness between each generation. Lower values introduce broader emotional range for the voice. Higher values can result in a monotonous voice with limited emotion.Format: `double`

Generated from the schema Router serves at `GET /v2/models/elevenlabs/eleven_v4/openapi.json`, the same document it validates a call against before the request reaches the provider.

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
      "inputs": [
        {
          "text": "Hello from Comfy Router.",
          "voice_id": "21m00Tcm4TlvDq8ikWAM"
        }
      ]
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/elevenlabs/eleven-v4/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/elevenlabs/eleven-v4/code)

[Use Eleven V4 Turbo with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/elevenlabs/eleven-v4-turbo/code)[Use Crystal Upscaler with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/fal/crystal-upscaler/code)

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
