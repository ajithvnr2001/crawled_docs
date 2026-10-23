---
url: https://docs.comfy.org/development/comfy-router/models/runway/aleph2/code/
title: Use Aleph 2 with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:39.338694+00:00
---

# Use Aleph 2 with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/runway/aleph2/code/

## On this page

  * Quick start
  * Schema
    * Input
    * Output
  * Examples
    * Input
    * Output
  * Before you ship



Runway

# Use Aleph 2 with Comfy Router

Copy pageCopy page

Call runway/aleph2 through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `runway/aleph2`, served by Comfy Router from Runway. **Input:** Video, Text, Image · **Output:** Video

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `runway/aleph2` **Endpoint:** `POST https://api.comfy.org/v2/models/runway/aleph2`

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
            "runway/aleph2",
            {
                "promptText": "recolor the scene in cool blue tones",
                "videoUri": "https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("runway/aleph2", {
      promptText: "recolor the scene in cool blue tones",
      videoUri: "https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/runway/aleph2 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"promptText\": \"recolor the scene in cool blue tones\", \"videoUri\": \"https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/runway/aleph2/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "runway/aleph2",
                {
                    "promptText": "recolor the scene in cool blue tones",
                    "videoUri": "https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4",
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
    const handle = await comfy.models.submit("runway/aleph2", {
      promptText: "recolor the scene in cool blue tones",
      videoUri: "https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4",
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
    curl https://api.comfy.org/v2/models/runway/aleph2/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"promptText\": \"recolor the scene in cool blue tones\", \"videoUri\": \"https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/runway/aleph2/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/runway/aleph2/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Schema

### 

​

Input

​

contentModeration

object

Settings that affect the behavior of the content moderation system.

​

contentModeration.publicFigureThreshold

string

When set to `low`, the content moderation system will be less strict about preventing generations that include recognizable public figures.Possible values: `auto`, `low`

​

keyframes

object[]

Timed guidance images placed at specific points in the input video. Up to 5 keyframes.

​

model

string

Model to use for generation. On the Comfy Router route `POST /v2/models/runway/{model}` this field is supplied from the path and MUST NOT be sent; on the v1 `POST /proxy/runway/video_to_video` route it is required and constrained to the RunwayVideoToVideoModelEnum (`aleph2`).

​

promptImage

object[]

A list of up to 5 image keyframes for guiding the edit at specific points in the video.

​

promptImage[].position

`first`, `last` | object

required

The position in the output video where the image should apply.

​

promptImage[].uri

string

required

A HTTPS URL, Runway or data URI containing an encoded image.

​

promptText

string

required

A non-empty string up to 1000 characters describing what should appear in the output.

​

seed

integer

Random seed for generation.Range: `0` to `4294967295`Format: `int64`

​

videoUri

string

required

The input video to edit (HTTPS URL, Runway upload URI, or data URI). Must be 30 seconds or shorter.

Generated from the schema Router serves at `GET /v2/models/runway/aleph2/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

createdAt

string (date-time)

required

Task creation timestampFormat: `date-time`

​

id

string

required

Task ID

​

output

string[]

The finished generation’s asset URLs — for `runway/gen4_turbo` and `runway/aleph2` each element is a VIDEO URL. Present once the task terminates successfully; this list IS the result.

​

progress

number

Float value between 0 and 1 representing the progress of the task. Only available if status is RUNNING.Range: `0` to `1`Format: `float`

​

status

string

required

Possible statuses for a Runway task.Possible values: `SUCCEEDED`, `RUNNING`, `FAILED`, `PENDING`, `CANCELLED`, `THROTTLED`

## 

​

Examples

### 

​

Input
    
    
    {
      "promptText": "recolor the scene in cool blue tones",
      "videoUri": "https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4"
    }
    

### 

​

Output
    
    
    {
      "createdAt": "2027-01-01T00:00:00Z",
      "id": "5f7c1b28-9a03-4e61-8d2f-1b2c3d4e5f60",
      "output": [
        "https://example.invalid/runway/gen4_turbo/generated.mp4"
      ],
      "status": "SUCCEEDED"
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/runway/aleph2/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/runway/aleph2/code)

[Use Recraft V4 with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/recraft/recraftv4/code)[Use Gen 4 Image with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/runway/gen4-image/code)

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
