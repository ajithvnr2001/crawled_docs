---
url: https://docs.comfy.org/development/comfy-router/models/gemini-interactions/gemini-omni-flash-preview/code/
title: Use Gemini Omni Flash Preview with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:05.872474+00:00
---

# Use Gemini Omni Flash Preview with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/gemini-interactions/gemini-omni-flash-preview/code/

## On this page

  * Quick start
  * Schema
    * Input
    * Output
  * Examples
    * Input
    * Output
  * Before you ship



Gemini Interactions

# Use Gemini Omni Flash Preview with Comfy Router

Copy pageCopy page

Call gemini-interactions/gemini-omni-flash-preview through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `gemini-interactions/gemini-omni-flash-preview`, served by Comfy Router from Gemini Interactions. **Input:** Text, Image, Audio, Video · **Output:** Text + Image + Audio

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `gemini-interactions/gemini-omni-flash-preview` **Endpoint:** `POST https://api.comfy.org/v2/models/gemini-interactions/gemini-omni-flash-preview`

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
            "gemini-interactions/gemini-omni-flash-preview",
            {
                "input": "Reply with the single word: ok",
                "stream": False,
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("gemini-interactions/gemini-omni-flash-preview", {
      input: "Reply with the single word: ok",
      stream: false,
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/gemini-interactions/gemini-omni-flash-preview \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input\": \"Reply with the single word: ok\", \"stream\": false}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/gemini-interactions/gemini-omni-flash-preview/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "gemini-interactions/gemini-omni-flash-preview",
                {
                    "input": "Reply with the single word: ok",
                    "stream": False,
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
    const handle = await comfy.models.submit("gemini-interactions/gemini-omni-flash-preview", {
      input: "Reply with the single word: ok",
      stream: false,
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
    curl https://api.comfy.org/v2/models/gemini-interactions/gemini-omni-flash-preview/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input\": \"Reply with the single word: ok\", \"stream\": false}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/gemini-interactions/gemini-omni-flash-preview/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/gemini-interactions/gemini-omni-flash-preview/requests/$REQUEST_ID \
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

Either a prompt string or an array of typed content parts (text, image, audio, video, document).

​

model

string

Gemini model identifier: `gemini-omni-1.1-flash` (generally available), or the deprecated `gemini-omni-flash-preview`. On the Comfy Router route `POST /v2/models/gemini-interactions/{model}` it is supplied from the path and may be omitted. Those two spellings — the set Comfy Router addresses as `gemini-interactions/<model>` — are the ones this operation serves (supportedGeminiInteractionModels); they are written out here rather than constrained to an enum, because the proxy validates the model itself and answers its own 400 for a spelling it does not serve.

​

previous_interaction_id

string

ID of a prior stored interaction, enabling stateful multi-turn video editing.

Generated from the schema Router serves at `GET /v2/models/gemini-interactions/gemini-omni-flash-preview/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

id

string

​

model

string

​

object

string

​

status

string

required

Always `completed` on a Router response. The provider’s other statuses (`in_progress`, `requires_action`, `failed`, `cancelled`, `incomplete`, `budget_exceeded`) do not reach a caller through Router as a 200; they are returned as a Comfy Router error carrying the provider’s body.Possible values: `completed`

​

steps

object[]

required

The interaction timeline, in order. Narrowed here from the untyped `steps` on `GeminiInteraction` so the output leaf is addressable; the provider keeps adding step types, so an item is `additionalProperties: true` and only the fields a Router caller reads are declared.

​

steps[].content

object[]

The typed content blocks of this step.

​

steps[].content[].data

string

Base64-encoded inline media, on a media block delivered inline. Google caps inline media at 4 MB and requires `delivery: uri` above it.

​

steps[].content[].mime_type

string

Media type of `data` or `uri`, on a media block.

​

steps[].content[].text

string

The generated text. Present on a `text` block, and this is the leaf the nightly Router SDK case asserts — on a `model_output` step specifically (`steps[type=model_output].content[].text`).

​

steps[].content[].type

string

Block kind — `text`, `image`, `audio`, `video` or `document`.

​

steps[].content[].uri

string

Reference to media delivered out of band, fetched by the caller from the URI it names.

​

steps[].type

string

Step kind. `model_output` is the generated answer; `user_input` is the caller’s own turn echoed back by the retrieval route; `thought` is internal reasoning. The tool steps (`function_call`, `function_result`, `code_execution_call`, `google_search_call`, …) are open-ended and Google adds to them.

​

usage

object

Token usage for a Gemini interaction.

​

usage.input_tokens_by_modality

object[]

Token count for one modality.

​

usage.input_tokens_by_modality[].modality

string

One of `text`, `image`, `audio`, `video`, `document`.

​

usage.input_tokens_by_modality[].tokens

integer

​

usage.output_tokens_by_modality

object[]

Token count for one modality.

​

usage.output_tokens_by_modality[].modality

string

One of `text`, `image`, `audio`, `video`, `document`.

​

usage.output_tokens_by_modality[].tokens

integer

​

usage.total_cached_tokens

integer

​

usage.total_input_tokens

integer

​

usage.total_output_tokens

integer

​

usage.total_thought_tokens

integer

​

usage.total_tokens

integer

## 

​

Examples

### 

​

Input
    
    
    {
      "input": "Reply with the single word: ok",
      "stream": false
    }
    

### 

​

Output
    
    
    {
      "id": "interactions/3f6c1a90-2b47-4d18-9a55-7c0e8b21d4f3",
      "object": "interaction",
      "status": "completed",
      "steps": [
        {
          "content": [
            {
              "text": "ok",
              "type": "text"
            }
          ],
          "type": "model_output"
        }
      ],
      "usage": {
        "input_tokens_by_modality": [
          {
            "modality": "text",
            "tokens": 9
          }
        ],
        "output_tokens_by_modality": [
          {
            "modality": "text",
            "tokens": 2
          }
        ],
        "total_cached_tokens": 0,
        "total_input_tokens": 9,
        "total_output_tokens": 2,
        "total_thought_tokens": 0,
        "total_tokens": 11
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/gemini-interactions/gemini-omni-flash-preview/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/gemini-interactions/gemini-omni-flash-preview/code)

[Use Gemini Omni 1.1 Flash with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/gemini-interactions/gemini-omni-1-1-flash/code)[Use Gemini 2.5 Flash Image with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/google/gemini-2-5-flash-image/code)

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
