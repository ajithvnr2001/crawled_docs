---
url: https://docs.comfy.org/development/comfy-router/models/typesafe/jev-1-13-0/code/
title: Use Jev 1.13.0 with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-22T15:07:51.131174+00:00
---

# Use Jev 1.13.0 with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/typesafe/jev-1-13-0/code/

## On this page

Back to top

  * Quick start
  * Schema
    * Input
    * Output
  * Examples
    * Input
    * Output
  * Before you ship



Typesafe

# Use Jev 1.13.0 with Comfy Router

Copy pageCopy page

Call typesafe/jev-1.13.0 through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `typesafe/jev-1.13.0`, served by Comfy Router from Typesafe. **Input:** Text, Image · **Output:** Text

## Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `typesafe/jev-1.13.0` **Endpoint:** `POST https://api.comfy.org/v2/models/typesafe/jev-1.13.0`

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
            "typesafe/jev-1.13.0",
            {
                "questions": {
                    "department": {
                        "criteria": {
                            "billing": "Payments, invoicing, refunds",
                            "technical": "Bugs, outages, integrations",
                        },
                        "instructions": "Which team should handle this?",
                        "type": "choice",
                    },
                    "is_urgent": {
                        "instructions": "Does this convey urgency?",
                        "type": "noul",
                    },
                },
                "state": "Help! My payouts have been failing for 3 days.",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("typesafe/jev-1.13.0", {
      questions: {
        department: {
          criteria: {
            billing: "Payments, invoicing, refunds",
            technical: "Bugs, outages, integrations",
          },
          instructions: "Which team should handle this?",
          type: "choice",
        },
        is_urgent: {
          instructions: "Does this convey urgency?",
          type: "noul",
        },
      },
      state: "Help! My payouts have been failing for 3 days.",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/typesafe/jev-1.13.0 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"questions\": {\"department\":{\"criteria\":{\"billing\":\"Payments, invoicing, refunds\",\"technical\":\"Bugs, outages, integrations\"},\"instructions\":\"Which team should handle this?\",\"type\":\"choice\"},\"is_urgent\":{\"instructions\":\"Does this convey urgency?\",\"type\":\"noul\"}}, \"state\": \"Help! My payouts have been failing for 3 days.\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/typesafe/jev-1.13.0/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "typesafe/jev-1.13.0",
                {
                    "questions": {
                        "department": {
                            "criteria": {
                                "billing": "Payments, invoicing, refunds",
                                "technical": "Bugs, outages, integrations",
                            },
                            "instructions": "Which team should handle this?",
                            "type": "choice",
                        },
                        "is_urgent": {
                            "instructions": "Does this convey urgency?",
                            "type": "noul",
                        },
                    },
                    "state": "Help! My payouts have been failing for 3 days.",
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
    const handle = await comfy.models.submit("typesafe/jev-1.13.0", {
      questions: {
        department: {
          criteria: {
            billing: "Payments, invoicing, refunds",
            technical: "Bugs, outages, integrations",
          },
          instructions: "Which team should handle this?",
          type: "choice",
        },
        is_urgent: {
          instructions: "Does this convey urgency?",
          type: "noul",
        },
      },
      state: "Help! My payouts have been failing for 3 days.",
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
    curl https://api.comfy.org/v2/models/typesafe/jev-1.13.0/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"questions\": {\"department\":{\"criteria\":{\"billing\":\"Payments, invoicing, refunds\",\"technical\":\"Bugs, outages, integrations\"},\"instructions\":\"Which team should handle this?\",\"type\":\"choice\"},\"is_urgent\":{\"instructions\":\"Does this convey urgency?\",\"type\":\"noul\"}}, \"state\": \"Help! My payouts have been failing for 3 days.\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/typesafe/jev-1.13.0/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/typesafe/jev-1.13.0/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## Schema

### Input

assets

object

The images in the request, keyed by a reference string. Every reference must appear somewhere in `state`, `instructions` or `criteria`. Each image is a still PNG or JPEG of 280 to 1568 pixels per side and at most 16 MiB after decoding; TypeSafe refuses a call over 32 MiB in total.

model

string

The pinned Jev version. Optional: Router fills it from the model id in the path. The `jev-latest` and `jev-preview` aliases are not accepted.

questions

object

required

The questions to answer, keyed by an id you choose. The answer to each is returned under the same id.

state

object

required

The content to evaluate: a string, or structured data (an object or array) up to 64 levels deep. An asset reference anywhere in it is replaced by that image.

Generated from the schema Router serves at `GET /v2/models/typesafe/jev-1.13.0/openapi.json`, the same document it validates a call against before the request reaches the provider.

### Output

answers

object

required

One answer per question, keyed by the question ids you sent.

model

string

required

The Jev version that answered, such as `jev-1.14.0`.

usage

object

Token usage for the request.

usage.input_tokens

integer

Input tokens, including every image in the request.

usage.output_tokens

integer

Output tokens.

## Examples

### Input
    
    
    {
      "questions": {
        "department": {
          "criteria": {
            "billing": "Payments, invoicing, refunds",
            "technical": "Bugs, outages, integrations"
          },
          "instructions": "Which team should handle this?",
          "type": "choice"
        },
        "is_urgent": {
          "instructions": "Does this convey urgency?",
          "type": "noul"
        }
      },
      "state": "Help! My payouts have been failing for 3 days."
    }
    

### Output
    
    
    {
      "answers": {
        "is_urgent": {
          "noul": 0.95,
          "type": "noul"
        },
        "mug": {
          "box": {
            "bottom": 0.82,
            "left": 0.44,
            "right": 0.84,
            "top": 0.25
          },
          "confidence": 0.92,
          "type": "box"
        }
      },
      "model": "jev-1.14.0",
      "usage": {
        "input_tokens": 290,
        "output_tokens": 21
      }
    }
    

## Before you ship

The SDKs create an `Idempotency-Key` and reuse it for automatic retries. For manual retries, reuse the original key. Router can hold the connection for up to 10 minutes. When a request fails, Router sends an `X-Comfy-Error-Type` response header explaining why. A `422` means Router rejected the input before calling the provider, and a `413` means the request body was larger than Router accepts. Download generated assets promptly because [result URLs can expire](https://docs.comfy.org/development/comfy-router/reference#result-assets). Any size limit named in a field description above is the provider’s own bound on that field, quoted from the provider’s specification. Router applies a separate cap to the whole request body, which base64-encoded media counts against: see [request body size](https://docs.comfy.org/development/comfy-router/limitations#request-bodies-are-capped). This page documents one partner model called through Comfy Router. The same `comfy-sdk` / `@comfyorg/sdk` package also ships a second client, for running a whole ComfyUI workflow graph on Comfy Cloud: `Comfy(api_key=...)` / `new Comfy({ apiKey })`, with `client.workflows`, `client.assets` and `client.jobs`. See [Comfy SDKs](https://docs.comfy.org/development/api-development/sdks).

## Headers

Authentication, idempotency, request IDs, error buckets, retry pacing, spend limits.

## Using the Router API

Model discovery, validation errors, retries, and billing.

## Limitations

What Router does not do today, and what to use instead.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/typesafe/jev-1-13-0/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/typesafe/jev-1-13-0/code)

[Hunyuan 3D Uv](https://docs.comfy.org/development/comfy-router/models/tencent/hunyuan-3d-uv/code)[Jev 1.14.0](https://docs.comfy.org/development/comfy-router/models/typesafe/jev-1-14-0/code)
