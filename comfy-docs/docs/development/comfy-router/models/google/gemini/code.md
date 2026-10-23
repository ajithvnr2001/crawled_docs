---
url: https://docs.comfy.org/development/comfy-router/models/google/gemini/code/
title: Use Google Gemini with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:08.711159+00:00
---

# Use Google Gemini with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/google/gemini/code/

## On this page

  * Quick start
  * Schema
    * Input
    * Output
  * Examples
    * Input
    * Output
  * Before you ship



Google

# Use Google Gemini with Comfy Router

Copy pageCopy page

Python, TypeScript and cURL snippets for calling Google Gemini text models over HTTP through Comfy Router, plus the request fields and the result shape

Copy pageCopy page

API Reference for Google Gemini. Google Gemini is Google’s family of multimodal text models, covering fast drafting through deep reasoning across the Flash and Pro tiers. **Input:** Text, Image, Audio, Video · **Output:** Text

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. Pick the model you want to call. The models share one request and response shape, documented once below.

  * Gemini 3.1 Pro

  * Gemini 3.5 Flash

  * Gemini 2.5 Pro

  * Gemini 2.5 Flash




**Model ID:** `vertexai/gemini-3.1-pro-preview`**Endpoint:** `POST https://api.comfy.org/v2/models/vertexai/gemini-3.1-pro-preview`

  * Wait for the result

  * Queue and collect later




Python

TypeScript

cURL
    
    
    import asyncio
    from comfy_sdk import AsyncComfy
    
    # Reads COMFY_API_KEY from the environment.
    # The SDK automatically creates an idempotency key and reuses it for automatic retries.
    async def main():
        async with AsyncComfy() as client:
            result = await client.models.run(
                "vertexai/gemini-3.1-pro-preview",
                {
                    "contents": [
                        {
                            "role": "user",
                            "parts": [
                                {
                                    "text": "Describe a single red maple leaf on a white background in one sentence.",
                                },
                            ],
                        },
                    ],
                    "generationConfig": {
                        "temperature": 0.7,
                        "maxOutputTokens": 256,
                    },
                },
            )
    
        print("text:", result["candidates"][0]["content"]["parts"][0]["text"])
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    type Result = { candidates: { content: { parts: { text: string }[] } }[] };
    const result = await comfy.models.run<Result>("vertexai/gemini-3.1-pro-preview", {
      contents: [
        {
          role: "user",
          parts: [
            {
              text: "Describe a single red maple leaf on a white background in one sentence.",
            },
          ],
        },
      ],
      generationConfig: {
        temperature: 0.7,
        maxOutputTokens: 256,
      },
    });
    if (result.kind !== "json") throw new Error("expected a JSON result");
    
    console.log("text:", result.data.candidates[0].content.parts[0].text);
    
    
    
    curl https://api.comfy.org/v2/models/vertexai/gemini-3.1-pro-preview \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"contents\": [{\"role\":\"user\",\"parts\":[{\"text\":\"Describe a single red maple leaf on a white background in one sentence.\"}]}], \"generationConfig\": {\"temperature\":0.7,\"maxOutputTokens\":256}}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/vertexai/gemini-3.1-pro-preview/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "vertexai/gemini-3.1-pro-preview",
                {
                    "contents": [
                        {
                            "role": "user",
                            "parts": [
                                {
                                    "text": "Describe a single red maple leaf on a white background in one sentence.",
                                },
                            ],
                        },
                    ],
                    "generationConfig": {
                        "temperature": 0.7,
                        "maxOutputTokens": 256,
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
    
        print("text:", result["candidates"][0]["content"]["parts"][0]["text"])
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // Each submit() call mints its own Idempotency-Key and reuses it for automatic retries.
    type Result = { candidates: { content: { parts: { text: string }[] } }[] };
    const handle = await comfy.models.submit<Result>("vertexai/gemini-3.1-pro-preview", {
      contents: [
        {
          role: "user",
          parts: [
            {
              text: "Describe a single red maple leaf on a white background in one sentence.",
            },
          ],
        },
      ],
      generationConfig: {
        temperature: 0.7,
        maxOutputTokens: 256,
      },
    });
    console.log("requestId:", handle.requestId); // with the model ID, all another process needs
    
    // Poll until the request completes, waiting the Retry-After the server names.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // The same result models.run() returns. A request that failed or was cancelled rejects here.
    const result = await handle.get();
    if (result.kind !== "json") throw new Error("expected a JSON result");
    
    console.log("text:", result.data.candidates[0].content.parts[0].text);
    
    
    
    # 1. Submit. Router answers 201 with request_id, status_url, response_url and cancel_url.
    curl https://api.comfy.org/v2/models/vertexai/gemini-3.1-pro-preview/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"contents\": [{\"role\":\"user\",\"parts\":[{\"text\":\"Describe a single red maple leaf on a white background in one sentence.\"}]}], \"generationConfig\": {\"temperature\":0.7,\"maxOutputTokens\":256}}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/vertexai/gemini-3.1-pro-preview/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/vertexai/gemini-3.1-pro-preview/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

**Model ID:** `vertexai/gemini-3.5-flash`**Endpoint:** `POST https://api.comfy.org/v2/models/vertexai/gemini-3.5-flash`

  * Wait for the result

  * Queue and collect later




Python

TypeScript

cURL
    
    
    import asyncio
    from comfy_sdk import AsyncComfy
    
    # Reads COMFY_API_KEY from the environment.
    # The SDK automatically creates an idempotency key and reuses it for automatic retries.
    async def main():
        async with AsyncComfy() as client:
            result = await client.models.run(
                "vertexai/gemini-3.5-flash",
                {
                    "contents": [
                        {
                            "role": "user",
                            "parts": [
                                {
                                    "text": "Describe a single red maple leaf on a white background in one sentence.",
                                },
                            ],
                        },
                    ],
                    "generationConfig": {
                        "temperature": 0.7,
                        "maxOutputTokens": 256,
                    },
                },
            )
    
        print("text:", result["candidates"][0]["content"]["parts"][0]["text"])
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    type Result = { candidates: { content: { parts: { text: string }[] } }[] };
    const result = await comfy.models.run<Result>("vertexai/gemini-3.5-flash", {
      contents: [
        {
          role: "user",
          parts: [
            {
              text: "Describe a single red maple leaf on a white background in one sentence.",
            },
          ],
        },
      ],
      generationConfig: {
        temperature: 0.7,
        maxOutputTokens: 256,
      },
    });
    if (result.kind !== "json") throw new Error("expected a JSON result");
    
    console.log("text:", result.data.candidates[0].content.parts[0].text);
    
    
    
    curl https://api.comfy.org/v2/models/vertexai/gemini-3.5-flash \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"contents\": [{\"role\":\"user\",\"parts\":[{\"text\":\"Describe a single red maple leaf on a white background in one sentence.\"}]}], \"generationConfig\": {\"temperature\":0.7,\"maxOutputTokens\":256}}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/vertexai/gemini-3.5-flash/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "vertexai/gemini-3.5-flash",
                {
                    "contents": [
                        {
                            "role": "user",
                            "parts": [
                                {
                                    "text": "Describe a single red maple leaf on a white background in one sentence.",
                                },
                            ],
                        },
                    ],
                    "generationConfig": {
                        "temperature": 0.7,
                        "maxOutputTokens": 256,
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
    
        print("text:", result["candidates"][0]["content"]["parts"][0]["text"])
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // Each submit() call mints its own Idempotency-Key and reuses it for automatic retries.
    type Result = { candidates: { content: { parts: { text: string }[] } }[] };
    const handle = await comfy.models.submit<Result>("vertexai/gemini-3.5-flash", {
      contents: [
        {
          role: "user",
          parts: [
            {
              text: "Describe a single red maple leaf on a white background in one sentence.",
            },
          ],
        },
      ],
      generationConfig: {
        temperature: 0.7,
        maxOutputTokens: 256,
      },
    });
    console.log("requestId:", handle.requestId); // with the model ID, all another process needs
    
    // Poll until the request completes, waiting the Retry-After the server names.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // The same result models.run() returns. A request that failed or was cancelled rejects here.
    const result = await handle.get();
    if (result.kind !== "json") throw new Error("expected a JSON result");
    
    console.log("text:", result.data.candidates[0].content.parts[0].text);
    
    
    
    # 1. Submit. Router answers 201 with request_id, status_url, response_url and cancel_url.
    curl https://api.comfy.org/v2/models/vertexai/gemini-3.5-flash/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"contents\": [{\"role\":\"user\",\"parts\":[{\"text\":\"Describe a single red maple leaf on a white background in one sentence.\"}]}], \"generationConfig\": {\"temperature\":0.7,\"maxOutputTokens\":256}}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/vertexai/gemini-3.5-flash/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/vertexai/gemini-3.5-flash/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

**Model ID:** `vertexai/gemini-2.5-pro`**Endpoint:** `POST https://api.comfy.org/v2/models/vertexai/gemini-2.5-pro`

  * Wait for the result

  * Queue and collect later




Python

TypeScript

cURL
    
    
    import asyncio
    from comfy_sdk import AsyncComfy
    
    # Reads COMFY_API_KEY from the environment.
    # The SDK automatically creates an idempotency key and reuses it for automatic retries.
    async def main():
        async with AsyncComfy() as client:
            result = await client.models.run(
                "vertexai/gemini-2.5-pro",
                {
                    "contents": [
                        {
                            "role": "user",
                            "parts": [
                                {
                                    "text": "Describe a single red maple leaf on a white background in one sentence.",
                                },
                            ],
                        },
                    ],
                    "generationConfig": {
                        "temperature": 0.7,
                        "maxOutputTokens": 256,
                    },
                },
            )
    
        print("text:", result["candidates"][0]["content"]["parts"][0]["text"])
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    type Result = { candidates: { content: { parts: { text: string }[] } }[] };
    const result = await comfy.models.run<Result>("vertexai/gemini-2.5-pro", {
      contents: [
        {
          role: "user",
          parts: [
            {
              text: "Describe a single red maple leaf on a white background in one sentence.",
            },
          ],
        },
      ],
      generationConfig: {
        temperature: 0.7,
        maxOutputTokens: 256,
      },
    });
    if (result.kind !== "json") throw new Error("expected a JSON result");
    
    console.log("text:", result.data.candidates[0].content.parts[0].text);
    
    
    
    curl https://api.comfy.org/v2/models/vertexai/gemini-2.5-pro \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"contents\": [{\"role\":\"user\",\"parts\":[{\"text\":\"Describe a single red maple leaf on a white background in one sentence.\"}]}], \"generationConfig\": {\"temperature\":0.7,\"maxOutputTokens\":256}}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/vertexai/gemini-2.5-pro/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "vertexai/gemini-2.5-pro",
                {
                    "contents": [
                        {
                            "role": "user",
                            "parts": [
                                {
                                    "text": "Describe a single red maple leaf on a white background in one sentence.",
                                },
                            ],
                        },
                    ],
                    "generationConfig": {
                        "temperature": 0.7,
                        "maxOutputTokens": 256,
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
    
        print("text:", result["candidates"][0]["content"]["parts"][0]["text"])
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // Each submit() call mints its own Idempotency-Key and reuses it for automatic retries.
    type Result = { candidates: { content: { parts: { text: string }[] } }[] };
    const handle = await comfy.models.submit<Result>("vertexai/gemini-2.5-pro", {
      contents: [
        {
          role: "user",
          parts: [
            {
              text: "Describe a single red maple leaf on a white background in one sentence.",
            },
          ],
        },
      ],
      generationConfig: {
        temperature: 0.7,
        maxOutputTokens: 256,
      },
    });
    console.log("requestId:", handle.requestId); // with the model ID, all another process needs
    
    // Poll until the request completes, waiting the Retry-After the server names.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // The same result models.run() returns. A request that failed or was cancelled rejects here.
    const result = await handle.get();
    if (result.kind !== "json") throw new Error("expected a JSON result");
    
    console.log("text:", result.data.candidates[0].content.parts[0].text);
    
    
    
    # 1. Submit. Router answers 201 with request_id, status_url, response_url and cancel_url.
    curl https://api.comfy.org/v2/models/vertexai/gemini-2.5-pro/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"contents\": [{\"role\":\"user\",\"parts\":[{\"text\":\"Describe a single red maple leaf on a white background in one sentence.\"}]}], \"generationConfig\": {\"temperature\":0.7,\"maxOutputTokens\":256}}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/vertexai/gemini-2.5-pro/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/vertexai/gemini-2.5-pro/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

**Model ID:** `vertexai/gemini-2.5-flash`**Endpoint:** `POST https://api.comfy.org/v2/models/vertexai/gemini-2.5-flash`

  * Wait for the result

  * Queue and collect later




Python

TypeScript

cURL
    
    
    import asyncio
    from comfy_sdk import AsyncComfy
    
    # Reads COMFY_API_KEY from the environment.
    # The SDK automatically creates an idempotency key and reuses it for automatic retries.
    async def main():
        async with AsyncComfy() as client:
            result = await client.models.run(
                "vertexai/gemini-2.5-flash",
                {
                    "contents": [
                        {
                            "role": "user",
                            "parts": [
                                {
                                    "text": "Describe a single red maple leaf on a white background in one sentence.",
                                },
                            ],
                        },
                    ],
                    "generationConfig": {
                        "temperature": 0.7,
                        "maxOutputTokens": 256,
                    },
                },
            )
    
        print("text:", result["candidates"][0]["content"]["parts"][0]["text"])
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    type Result = { candidates: { content: { parts: { text: string }[] } }[] };
    const result = await comfy.models.run<Result>("vertexai/gemini-2.5-flash", {
      contents: [
        {
          role: "user",
          parts: [
            {
              text: "Describe a single red maple leaf on a white background in one sentence.",
            },
          ],
        },
      ],
      generationConfig: {
        temperature: 0.7,
        maxOutputTokens: 256,
      },
    });
    if (result.kind !== "json") throw new Error("expected a JSON result");
    
    console.log("text:", result.data.candidates[0].content.parts[0].text);
    
    
    
    curl https://api.comfy.org/v2/models/vertexai/gemini-2.5-flash \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"contents\": [{\"role\":\"user\",\"parts\":[{\"text\":\"Describe a single red maple leaf on a white background in one sentence.\"}]}], \"generationConfig\": {\"temperature\":0.7,\"maxOutputTokens\":256}}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/vertexai/gemini-2.5-flash/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "vertexai/gemini-2.5-flash",
                {
                    "contents": [
                        {
                            "role": "user",
                            "parts": [
                                {
                                    "text": "Describe a single red maple leaf on a white background in one sentence.",
                                },
                            ],
                        },
                    ],
                    "generationConfig": {
                        "temperature": 0.7,
                        "maxOutputTokens": 256,
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
    
        print("text:", result["candidates"][0]["content"]["parts"][0]["text"])
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // Each submit() call mints its own Idempotency-Key and reuses it for automatic retries.
    type Result = { candidates: { content: { parts: { text: string }[] } }[] };
    const handle = await comfy.models.submit<Result>("vertexai/gemini-2.5-flash", {
      contents: [
        {
          role: "user",
          parts: [
            {
              text: "Describe a single red maple leaf on a white background in one sentence.",
            },
          ],
        },
      ],
      generationConfig: {
        temperature: 0.7,
        maxOutputTokens: 256,
      },
    });
    console.log("requestId:", handle.requestId); // with the model ID, all another process needs
    
    // Poll until the request completes, waiting the Retry-After the server names.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // The same result models.run() returns. A request that failed or was cancelled rejects here.
    const result = await handle.get();
    if (result.kind !== "json") throw new Error("expected a JSON result");
    
    console.log("text:", result.data.candidates[0].content.parts[0].text);
    
    
    
    # 1. Submit. Router answers 201 with request_id, status_url, response_url and cancel_url.
    curl https://api.comfy.org/v2/models/vertexai/gemini-2.5-flash/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"contents\": [{\"role\":\"user\",\"parts\":[{\"text\":\"Describe a single red maple leaf on a white background in one sentence.\"}]}], \"generationConfig\": {\"temperature\":0.7,\"maxOutputTokens\":256}}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/vertexai/gemini-2.5-flash/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/vertexai/gemini-2.5-flash/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Schema

### 

​

Input

​

contents

object[]

required

The content of the current conversation with the model. For single-turn queries, this is a single instance. For multi-turn queries, this is a repeated field that contains conversation history and the latest request.

​

contents[].parts

object[]

required

​

contents[].parts[].fileData

object

URI based data.

​

contents[].parts[].fileData.fileUri

string

URI

​

contents[].parts[].fileData.mimeType

string

The media type of the file specified in the data or fileUri fields. Acceptable values include the following. For gemini-2.0-flash-lite and gemini-2.0-flash, the maximum length of an audio file is 8.4 hours and the maximum length of a video file (without audio) is one hour. For more information, see Gemini audio and video requirements. Text files must be UTF-8 encoded. The contents of the text file count toward the token limit. There is no limit on image resolution.Possible values: `application/pdf`, `audio/mpeg`, `audio/mp3`, `audio/wav`, `image/png`, `image/jpeg`, `image/webp`, `text/plain`, `video/mov`, `video/mpeg`, `video/mp4`, `video/mpg`, `video/avi`, `video/wmv`, `video/mpegps`, `video/flv`, `image/heic`, `image/heif`, `audio/flac`, `video/webm`

​

contents[].parts[].inlineData

object

Inline data in raw bytes. For gemini-2.0-flash-lite and gemini-2.0-flash, you can specify up to 3000 images by using inlineData.

​

contents[].parts[].inlineData.data

string (byte)

The base64 encoding of the image, PDF, or video to include inline in the prompt. When including media inline, you must also specify the media type (mimeType) of the data. Size limit: 20MBFormat: `byte`

​

contents[].parts[].inlineData.mimeType

string

The media type of the file specified in the data or fileUri fields. Acceptable values include the following. For gemini-2.0-flash-lite and gemini-2.0-flash, the maximum length of an audio file is 8.4 hours and the maximum length of a video file (without audio) is one hour. For more information, see Gemini audio and video requirements. Text files must be UTF-8 encoded. The contents of the text file count toward the token limit. There is no limit on image resolution.Possible values: `application/pdf`, `audio/mpeg`, `audio/mp3`, `audio/wav`, `image/png`, `image/jpeg`, `image/webp`, `text/plain`, `video/mov`, `video/mpeg`, `video/mp4`, `video/mpg`, `video/avi`, `video/wmv`, `video/mpegps`, `video/flv`, `image/heic`, `image/heif`, `audio/flac`, `video/webm`

​

contents[].parts[].mediaProcessing

string

How the model reads this part’s video. Set “AGENTIC” to let the model decide which segments to inspect, instead of fixed-rate frame sampling. Omit for the default fixed-rate sampling. Supported on gemini-3.7-flash and newer Flash models.

​

contents[].parts[].text

string

A text prompt or code snippet.

​

contents[].parts[].thought

boolean

Indicates this part is a thinking/reasoning step from the model.

​

contents[].role

string

Possible values: `user`, `model`

​

generationConfig

object

Sampling, length and output settings for the generation. Every field is optional: the fields below that declare a `default` apply it when omitted, and the rest fall back to the model’s own behaviour.

​

generationConfig.imageConfig

object

Configuration for image generation

​

generationConfig.imageConfig.aspectRatio

string

Aspect ratio for generated images

​

generationConfig.imageConfig.imageOutputOptions

object

Optional. The image output format for generated images.

​

generationConfig.imageConfig.imageOutputOptions.compressionQuality

integer

Optional. The compression quality of the output image.

​

generationConfig.imageConfig.imageOutputOptions.mimeType

string

Optional. The image format that the output should be saved as, on the Vertex AI paths: requests served by Comfy’s own credentials, and BYOK requests authenticated with a GCP service account. Accepted values there are `image/png` and `image/jpeg`, matched case-insensitively and normalised to lower case before the request is forwarded; any other value is rejected with a 400 naming this field. Defaults to `image/png` when omitted. A BYOK request authenticated with a Google AI Studio API key is the exception: that upstream has no such property and rejects the whole call if it is present, so the field is dropped from the request rather than honoured or rejected, and the output format is whatever AI Studio chooses. On every path, read the media type back from the response part you are given (`inlineData.mimeType`, or `fileData.mimeType` when `uploadImagesToStorage` is set) rather than assuming the value you sent.

​

generationConfig.imageConfig.imageSize

string

Optional. Specifies the size of generated images. Supported values are 1K, 2K, 4K. If not specified, the model will use default value 1K.

​

generationConfig.maxOutputTokens

integer

Maximum number of tokens that can be generated in the response. A token is approximately 4 characters. 100 tokens correspond to roughly 60-80 words.Range: `16` to `65536`

​

generationConfig.responseModalities

`TEXT`, `IMAGE`[]

​

generationConfig.seed

integer

When seed is fixed to a specific value, the model makes a best effort to provide the same response for repeated requests. Deterministic output isn’t guaranteed. Also, changing the model or parameter settings, such as the temperature, can cause variations in the response even when you use the same seed value. By default, a random seed value is used. Available for the following models:, gemini-2.5-flash, gemini-2.5-pro, gemini-2.5-flash-preview-04-1, gemini-2.5-pro-preview-05-0, gemini-2.0-flash-lite-00, gemini-2.0-flash-001

​

generationConfig.stopSequences

string[]

​

generationConfig.temperature

number

default:"1"

The temperature is used for sampling during response generation, which occurs when topP and topK are applied. Temperature controls the degree of randomness in token selection. Lower temperatures are good for prompts that require a less open-ended or creative response, while higher temperatures can lead to more diverse or creative results. A temperature of 0 means that the highest probability tokens are always selected. In this case, responses for a given prompt are mostly deterministic, but a small amount of variation is still possible. If the model returns a response that’s too generic, too short, or the model gives a fallback response, try increasing the temperatureRange: `0` to `2`Format: `float`

​

generationConfig.thinkingConfig

object

Optional. Configuration for thinking features. Thinking is a process where the model breaks down a complex task into smaller steps to generate a higher-quality response.

​

generationConfig.thinkingConfig.includeThoughts

boolean

Optional. If true, the model will include its thoughts in the response.

​

generationConfig.thinkingConfig.thinkingBudget

integer

Optional. The token budget for the model’s thinking process. The model will make a best effort to stay within this budget.

​

generationConfig.thinkingConfig.thinkingLevel

string

Optional. The thinking level for the model.Possible values: `THINKING_LEVEL_UNSPECIFIED`, `LOW`, `MEDIUM`, `HIGH`, `MINIMAL`

​

generationConfig.topK

integer

default:"40"

Top-K changes how the model selects tokens for output. A top-K of 1 means the next selected token is the most probable among all tokens in the model’s vocabulary. A top-K of 3 means that the next token is selected from among the 3 most probable tokens by using temperature.Range: `1` to `…`

​

generationConfig.topP

number

default:"0.95"

If specified, nucleus sampling is used. Top-P changes how the model selects tokens for output. Tokens are selected from the most (see top-K) to least probable until the sum of their probabilities equals the top-P value. For example, if tokens A, B, and C have a probability of 0.3, 0.2, and 0.1 and the top-P value is 0.5, then the model will select either A or B as the next token by using temperature and excludes C as a candidate. Specify a lower value for less random responses and a higher value for more random responses.Range: `0` to `1`Format: `float`

​

safetySettings

object[]

Per request settings for blocking unsafe content. Enforced on GenerateContentResponse.candidates.

​

safetySettings[].category

string

required

Possible values: `HARM_CATEGORY_SEXUALLY_EXPLICIT`, `HARM_CATEGORY_HATE_SPEECH`, `HARM_CATEGORY_HARASSMENT`, `HARM_CATEGORY_DANGEROUS_CONTENT`

​

safetySettings[].threshold

string

required

Possible values: `OFF`, `BLOCK_NONE`, `BLOCK_LOW_AND_ABOVE`, `BLOCK_MEDIUM_AND_ABOVE`, `BLOCK_ONLY_HIGH`

​

systemInstruction

object

Instructions for the model to steer it toward better performance. For example, “Answer as concisely as possible” or “Don’t use technical terms in your response”. The text strings count toward the token limit. The role field of systemInstruction is ignored and doesn’t affect the performance of the model. Note: Only text should be used in parts and content in each part should be in a separate paragraph.

​

systemInstruction.parts

object[]

required

A list of ordered parts that make up a single message. Different parts may have different IANA MIME types. For limits on the inputs, such as the maximum number of tokens or the number of images, see the model specifications on the Google models page.

​

systemInstruction.parts[].text

string

A text prompt or code snippet.

​

systemInstruction.role

string

The identity of the entity that creates the message. The following values are supported: user: This indicates that the message is sent by a real person, typically a user-generated message. model: This indicates that the message is generated by the model. The model value is used to insert messages from the model into the conversation during multi-turn conversations. For non-multi-turn conversations, this field can be left blank or unset.Possible values: `user`, `model`

​

tools

object[]

A piece of code that enables the system to interact with external systems to perform an action, or set of actions, outside of knowledge and scope of the model. See Function calling.

​

tools[].functionDeclarations

object[]

​

tools[].functionDeclarations[].description

string

​

tools[].functionDeclarations[].name

string

required

​

tools[].functionDeclarations[].parameters

object

JSON schema for the function parameters

​

uploadImagesToStorage

boolean

If true, generated images will be uploaded to cloud storage and returned as signed URLs instead of inline base64 data. The URLs expire after 24 hours.

​

videoMetadata

object

For video input, the start and end offset of the video in Duration format. For example, to specify a 10 second clip starting at 1:00, set “startOffset”: { “seconds”: 60 } and “endOffset”: { “seconds”: 70 }. The metadata should only be specified while the video data is presented in inlineData or fileData.

​

videoMetadata.endOffset

object

Represents a duration offset for video timeline positions.

​

videoMetadata.endOffset.nanos

integer

Signed fractions of a second at nanosecond resolution. Negative second values with fractions must still have non-negative nanos values.Range: `0` to `999999999`

​

videoMetadata.endOffset.seconds

integer

Signed seconds of the span of time. Must be from -315,576,000,000 to +315,576,000,000 inclusive.Range: `-315576000000` to `315576000000`

​

videoMetadata.startOffset

object

Represents a duration offset for video timeline positions.

​

videoMetadata.startOffset.nanos

integer

Signed fractions of a second at nanosecond resolution. Negative second values with fractions must still have non-negative nanos values.Range: `0` to `999999999`

​

videoMetadata.startOffset.seconds

integer

Signed seconds of the span of time. Must be from -315,576,000,000 to +315,576,000,000 inclusive.Range: `-315576000000` to `315576000000`

Generated from the schema Router serves at `GET /v2/models/vertexai/gemini-3.1-pro-preview/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

candidates

object[]

​

candidates[].citationMetadata

object

​

candidates[].citationMetadata.citations

object[]

​

candidates[].citationMetadata.citations[].authors

string[]

​

candidates[].citationMetadata.citations[].endIndex

integer

​

candidates[].citationMetadata.citations[].license

string

​

candidates[].citationMetadata.citations[].publicationDate

string (date)

Format: `date`

​

candidates[].citationMetadata.citations[].startIndex

integer

​

candidates[].citationMetadata.citations[].title

string

​

candidates[].citationMetadata.citations[].uri

string

​

candidates[].content

object

The content of the current conversation with the model. For single-turn queries, this is a single instance. For multi-turn queries, this is a repeated field that contains conversation history and the latest request.

​

candidates[].content.parts

object[]

required

​

candidates[].content.parts[].fileData

object

URI based data.

​

candidates[].content.parts[].fileData.fileUri

string

URI

​

candidates[].content.parts[].fileData.mimeType

string

The media type of the file specified in the data or fileUri fields. Acceptable values include the following. For gemini-2.0-flash-lite and gemini-2.0-flash, the maximum length of an audio file is 8.4 hours and the maximum length of a video file (without audio) is one hour. For more information, see Gemini audio and video requirements. Text files must be UTF-8 encoded. The contents of the text file count toward the token limit. There is no limit on image resolution.Possible values: `application/pdf`, `audio/mpeg`, `audio/mp3`, `audio/wav`, `image/png`, `image/jpeg`, `image/webp`, `text/plain`, `video/mov`, `video/mpeg`, `video/mp4`, `video/mpg`, `video/avi`, `video/wmv`, `video/mpegps`, `video/flv`, `image/heic`, `image/heif`, `audio/flac`, `video/webm`

​

candidates[].content.parts[].inlineData

object

Inline data in raw bytes. For gemini-2.0-flash-lite and gemini-2.0-flash, you can specify up to 3000 images by using inlineData.

​

candidates[].content.parts[].inlineData.data

string (byte)

The base64 encoding of the image, PDF, or video to include inline in the prompt. When including media inline, you must also specify the media type (mimeType) of the data. Size limit: 20MBFormat: `byte`

​

candidates[].content.parts[].inlineData.mimeType

string

The media type of the file specified in the data or fileUri fields. Acceptable values include the following. For gemini-2.0-flash-lite and gemini-2.0-flash, the maximum length of an audio file is 8.4 hours and the maximum length of a video file (without audio) is one hour. For more information, see Gemini audio and video requirements. Text files must be UTF-8 encoded. The contents of the text file count toward the token limit. There is no limit on image resolution.Possible values: `application/pdf`, `audio/mpeg`, `audio/mp3`, `audio/wav`, `image/png`, `image/jpeg`, `image/webp`, `text/plain`, `video/mov`, `video/mpeg`, `video/mp4`, `video/mpg`, `video/avi`, `video/wmv`, `video/mpegps`, `video/flv`, `image/heic`, `image/heif`, `audio/flac`, `video/webm`

​

candidates[].content.parts[].mediaProcessing

string

How the model reads this part’s video. Set “AGENTIC” to let the model decide which segments to inspect, instead of fixed-rate frame sampling. Omit for the default fixed-rate sampling. Supported on gemini-3.7-flash and newer Flash models.

​

candidates[].content.parts[].text

string

A text prompt or code snippet.

​

candidates[].content.parts[].thought

boolean

Indicates this part is a thinking/reasoning step from the model.

​

candidates[].content.role

string

Possible values: `user`, `model`

​

candidates[].finishReason

string

​

candidates[].safetyRatings

object[]

​

candidates[].safetyRatings[].category

string

Possible values: `HARM_CATEGORY_SEXUALLY_EXPLICIT`, `HARM_CATEGORY_HATE_SPEECH`, `HARM_CATEGORY_HARASSMENT`, `HARM_CATEGORY_DANGEROUS_CONTENT`

​

candidates[].safetyRatings[].probability

string

The probability that the content violates the specified safety categoryPossible values: `NEGLIGIBLE`, `LOW`, `MEDIUM`, `HIGH`, `UNKNOWN`

​

createTime

string

Timestamp when the response was created.

​

modelVersion

string

The model version used to generate the response.

​

promptFeedback

object

​

promptFeedback.blockReason

string

​

promptFeedback.blockReasonMessage

string

​

promptFeedback.safetyRatings

object[]

​

promptFeedback.safetyRatings[].category

string

Possible values: `HARM_CATEGORY_SEXUALLY_EXPLICIT`, `HARM_CATEGORY_HATE_SPEECH`, `HARM_CATEGORY_HARASSMENT`, `HARM_CATEGORY_DANGEROUS_CONTENT`

​

promptFeedback.safetyRatings[].probability

string

The probability that the content violates the specified safety categoryPossible values: `NEGLIGIBLE`, `LOW`, `MEDIUM`, `HIGH`, `UNKNOWN`

​

responseId

string

Unique identifier for the response.

​

usageMetadata

object

​

usageMetadata.cachedContentTokenCount

integer

Output only. Number of tokens in the cached part in the input (the cached content).

​

usageMetadata.candidatesTokenCount

integer

Number of tokens in the response(s).

​

usageMetadata.candidatesTokensDetails

object[]

Breakdown of candidate tokens by modality.

​

usageMetadata.candidatesTokensDetails[].modality

string

Type of input or output content modality.Possible values: `MODALITY_UNSPECIFIED`, `TEXT`, `IMAGE`, `VIDEO`, `AUDIO`, `DOCUMENT`

​

usageMetadata.candidatesTokensDetails[].tokenCount

integer

Number of tokens for the given modality.

​

usageMetadata.promptTokenCount

integer

Number of tokens in the request. When cachedContent is set, this is still the total effective prompt size meaning this includes the number of tokens in the cached content.

​

usageMetadata.promptTokensDetails

object[]

Breakdown of prompt tokens by modality.

​

usageMetadata.promptTokensDetails[].modality

string

Type of input or output content modality.Possible values: `MODALITY_UNSPECIFIED`, `TEXT`, `IMAGE`, `VIDEO`, `AUDIO`, `DOCUMENT`

​

usageMetadata.promptTokensDetails[].tokenCount

integer

Number of tokens for the given modality.

​

usageMetadata.thoughtsTokenCount

integer

Number of tokens present in thoughts output.

​

usageMetadata.toolUsePromptTokenCount

integer

Number of tokens present in tool-use prompt(s).

​

usageMetadata.toolUsePromptTokensDetails

object[]

Breakdown of tool-use prompt tokens by modality.

​

usageMetadata.toolUsePromptTokensDetails[].modality

string

Type of input or output content modality.Possible values: `MODALITY_UNSPECIFIED`, `TEXT`, `IMAGE`, `VIDEO`, `AUDIO`, `DOCUMENT`

​

usageMetadata.toolUsePromptTokensDetails[].tokenCount

integer

Number of tokens for the given modality.

​

usageMetadata.totalTokenCount

integer

Total number of tokens (prompt + candidates).

​

usageMetadata.trafficType

string

Traffic type used for the request (e.g., PROVISIONED_THROUGHPUT).

## 

​

Examples

### 

​

Input
    
    
    {
      "contents": [
        {
          "role": "user",
          "parts": [
            {
              "text": "Describe a single red maple leaf on a white background in one sentence."
            }
          ]
        }
      ],
      "generationConfig": {
        "temperature": 0.7,
        "maxOutputTokens": 256
      }
    }
    

### 

​

Output
    
    
    {
      "candidates": [
        {
          "content": {
            "role": "model",
            "parts": [
              {
                "text": "A single red maple leaf rests on a plain white background, its edges sharp and its color deep."
              }
            ]
          },
          "finishReason": "STOP"
        }
      ],
      "usageMetadata": {
        "promptTokenCount": 18,
        "candidatesTokenCount": 24
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/google/gemini/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/google/gemini/code)

[Use Gemini Nano Banana 2.1 with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/google/gemini-nano-banana-2-1/code)[Use Nano Banana 2 Lite with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/google/nano-banana-2-lite/code)

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
