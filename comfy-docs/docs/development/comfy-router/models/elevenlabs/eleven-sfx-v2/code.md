---
url: https://docs.comfy.org/development/comfy-router/models/elevenlabs/eleven-sfx-v2/code/
title: Use Eleven Sfx V2 with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:03.013843+00:00
---

# Use Eleven Sfx V2 with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/elevenlabs/eleven-sfx-v2/code/

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

# Use Eleven Sfx V2 with Comfy Router

Copy pageCopy page

Call elevenlabs/eleven_sfx_v2 through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `elevenlabs/eleven_sfx_v2`, served by Comfy Router from Elevenlabs. **Input:** Text · **Output:** Audio

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `elevenlabs/eleven_sfx_v2` **Endpoint:** `POST https://api.comfy.org/v2/models/elevenlabs/eleven_sfx_v2`

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
            "elevenlabs/eleven_sfx_v2",
            {
                "duration_seconds": 5,
                "text": "A distant rumble of thunder rolling across a valley.",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("elevenlabs/eleven_sfx_v2", {
      duration_seconds: 5,
      text: "A distant rumble of thunder rolling across a valley.",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/elevenlabs/eleven_sfx_v2 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"duration_seconds\": 5, \"text\": \"A distant rumble of thunder rolling across a valley.\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/elevenlabs/eleven_sfx_v2/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "elevenlabs/eleven_sfx_v2",
                {
                    "duration_seconds": 5,
                    "text": "A distant rumble of thunder rolling across a valley.",
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
    const handle = await comfy.models.submit("elevenlabs/eleven_sfx_v2", {
      duration_seconds: 5,
      text: "A distant rumble of thunder rolling across a valley.",
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
    curl https://api.comfy.org/v2/models/elevenlabs/eleven_sfx_v2/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"duration_seconds\": 5, \"text\": \"A distant rumble of thunder rolling across a valley.\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/elevenlabs/eleven_sfx_v2/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/elevenlabs/eleven_sfx_v2/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Schema

### 

​

Input

​

duration_seconds

number

required

The duration of the sound which will be generated in seconds. Must be at least 0.5 and at most 30. REQUIRED on this route: unlike the upstream ElevenLabs API, which guesses an optimal duration when the field is null, this route rejects a request that omits it with 400 “Duration is required”. The field stays nullable only so an explicit null is a well-formed document; it is still refused. This value is the quantity the request is metered on.Range: `0.5` to `30`Format: `double`

​

loop

boolean

default:"false"

Whether to create a sound effect that loops smoothly. ElevenLabs documents this as available only for the ‘eleven_text_to_sound_v2’ model, which is the model this route forwards ‘eleven_sfx_v2’ as (see model_id), so it applies here.

​

model_id

string

The model ID to use for the sound generation. This route admits ‘eleven_sfx_v2’ and nothing else; any other value is rejected with 400 before the request reaches ElevenLabs. ‘eleven_sfx_v2’ is Comfy’s id for the model ElevenLabs calls ‘eleven_text_to_sound_v2’; the proxy rewrites the forwarded body to that vendor spelling, which ElevenLabs’ own enum requires (it refuses ‘eleven_sfx_v2’ with 422), so a caller never sends the vendor id. It is NOT in this schema’s `required` list because Comfy Router fills it from the `{model}` path segment of /v2/models/elevenlabs/{model}, so a Router caller omits it.

​

prompt_influence

number

A higher prompt influence makes your generation follow the prompt more closely while also making generations less variable. Must be a value between 0 and 1. Defaults to 0.3.Range: `0` to `1`Format: `double`

​

text

string

required

The text that will get converted into a sound effect.

Generated from the schema Router serves at `GET /v2/models/elevenlabs/eleven_sfx_v2/openapi.json`, the same document it validates a call against before the request reaches the provider.

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
      "duration_seconds": 5,
      "text": "A distant rumble of thunder rolling across a valley."
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/elevenlabs/eleven-sfx-v2/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/elevenlabs/eleven-sfx-v2/code)

[Use Eleven Multilingual V2 with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/elevenlabs/eleven-multilingual-v2/code)[Use Eleven V3 with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/elevenlabs/eleven-v3/code)

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
