---
url: https://docs.comfy.org/development/comfy-router/models/minimax/minimax-h3/code/
title: Use MiniMax H3 with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:22.912490+00:00
---

# Use MiniMax H3 with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/minimax/minimax-h3/code/

## On this page

  * Quick start
  * Schema
    * Input
    * Output
  * Examples
    * Input
    * Output
  * Before you ship



MiniMax

# Use MiniMax H3 with Comfy Router

Copy pageCopy page

Call minimax/minimax-h3 through Comfy Router: endpoint, request shape, and the MP4 with native stereo audio that Router returns

Copy pageCopy page

API Reference for MiniMax H3. MiniMax H3 (Hailuo 03) is an omni-modal video model. It generates the picture and its audio track together in one pass, so a finished clip already carries dialogue, sound effects and music. **Input:** Text, Image · **Output:** Video + Audio

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `minimax/minimax-h3` **Endpoint:** `POST https://api.comfy.org/v2/models/minimax/minimax-h3`

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
                "minimax/minimax-h3",
                {
                    "content": [
                        {
                            "text": "A single red maple leaf resting on a plain white background.",
                            "type": "text",
                        },
                    ],
                    "duration": 5,
                    "ratio": "16:9",
                    "resolution": "768P",
                },
            )
    
        print("video:", result["task"]["content"]["url"])
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    type Result = { task: { content: { url: string } } };
    const result = await comfy.models.run<Result>("minimax/minimax-h3", {
      content: [
        {
          text: "A single red maple leaf resting on a plain white background.",
          type: "text",
        },
      ],
      duration: 5,
      ratio: "16:9",
      resolution: "768P",
    });
    if (result.kind !== "json") throw new Error("expected a JSON result");
    
    console.log("video:", result.data.task.content.url);
    
    
    
    curl https://api.comfy.org/v2/models/minimax/minimax-h3 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"content\": [{\"text\":\"A single red maple leaf resting on a plain white background.\",\"type\":\"text\"}], \"duration\": 5, \"ratio\": \"16:9\", \"resolution\": \"768P\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/minimax/minimax-h3/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "minimax/minimax-h3",
                {
                    "content": [
                        {
                            "text": "A single red maple leaf resting on a plain white background.",
                            "type": "text",
                        },
                    ],
                    "duration": 5,
                    "ratio": "16:9",
                    "resolution": "768P",
                },
            )
            print("request_id:", handle.request_id)  # with the model ID, all another process needs
    
            # Poll until the request completes, waiting the Retry-After the server names.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # The provider's own payload, the same value models.run() returns.
            # A request that failed or was cancelled raises the typed Router error here.
            result = await handle.get()
    
        print("video:", result["task"]["content"]["url"])
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // Each submit() call mints its own Idempotency-Key and reuses it for automatic retries.
    type Result = { task: { content: { url: string } } };
    const handle = await comfy.models.submit<Result>("minimax/minimax-h3", {
      content: [
        {
          text: "A single red maple leaf resting on a plain white background.",
          type: "text",
        },
      ],
      duration: 5,
      ratio: "16:9",
      resolution: "768P",
    });
    console.log("requestId:", handle.requestId); // with the model ID, all another process needs
    
    // Poll until the request completes, waiting the Retry-After the server names.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // The same result models.run() returns. A request that failed or was cancelled rejects here.
    const result = await handle.get();
    if (result.kind !== "json") throw new Error("expected a JSON result");
    
    console.log("video:", result.data.task.content.url);
    
    
    
    # 1. Submit. Router answers 201 with request_id, status_url, response_url and cancel_url.
    curl https://api.comfy.org/v2/models/minimax/minimax-h3/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"content\": [{\"text\":\"A single red maple leaf resting on a plain white background.\",\"type\":\"text\"}], \"duration\": 5, \"ratio\": \"16:9\", \"resolution\": \"768P\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/minimax/minimax-h3/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/minimax/minimax-h3/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Schema

### 

​

Input

​

aigc_watermark

boolean

Whether to add an AIGC watermark to the output. Defaults to false.

​

callback_url

string

Optional. URL to receive task state changes after challenge verification.

​

content

object[]

required

Content items driving the generation. Must contain one non-empty text item; optionally add first_frame/last_frame images or reference_* media.

​

content[].audio_url

object

Audio source. Required for audio_url items.

​

content[].audio_url.url

string

A publicly reachable URL, an mm_file://{file_id} reference, or a data URI.

​

content[].image_url

object

Image source. Required for image_url items.

​

content[].image_url.url

string

A publicly reachable URL, an mm_file://{file_id} reference, or a data URI.

​

content[].role

string

Role of a media item. Options: first_frame, last_frame, reference_image, reference_video, reference_audio, base_video. Keyframe roles and reference_* roles are mutually exclusive within a request; base_video marks the source video of a video regeneration request.

​

content[].text

string

The prompt text. Exactly one non-empty text item is required per request.

​

content[].type

string

required

Content item type. Options: text, image_url, video_url, audio_url.

​

content[].video_url

object

Video source. Required for video_url items.

​

content[].video_url.url

string

A publicly reachable URL, an mm_file://{file_id} reference, or a data URI.

​

duration

integer

required

Video length in seconds. Comfy Router accepts 4 to 15 and refuses anything outside it before the provider is called. MiniMax’s own documentation for this model states 5 to 15; the ComfyUI MiniMax H3 nodes offer 4 to 15 and a 4-second generation has been observed to succeed, so 4 is accepted here.Range: `4` to `15`

​

model

string

ID of model. Options: MiniMax-H3. Router callers may omit this field or send null; Router injects the model selected by the request path before provider dispatch.

​

ratio

string

Aspect ratio. Options: adaptive (default), 21:9, 16:9, 4:3, 1:1, 3:4, 9:16. Required and must not be adaptive for text-to-video; ignored (treated as adaptive) for first-frame or last-frame generation.

​

resolution

string

required

Video resolution. Options: 2K, 768P. The value is matched case-insensitively and canonicalised before dispatch, so `2k` and `768p` are accepted and sent as `2K` and `768P`.Possible values: `2K`, `2k`, `768P`, `768p`

​

seed

integer

Random seed in [-1, 2^32 - 1]; omitted or -1 is random.Format: `int64`

Generated from the schema Router serves at `GET /v2/models/minimax/minimax-h3/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

task

object

A Minimax V2 video generation task.

​

task.content

object

Generated output; present when status is succeeded.

​

task.content.prompt

string

The enhanced video prompt produced by a succeeded h3_context_ir task.

​

task.content.url

string

Time-limited URL of the generated MP4. Query again for a refreshed URL.

​

task.duration

number

The duration of the generated video in seconds.

​

task.error

object

Error details when status is failed; carries code and message.

​

task.id

string

The task ID.

​

task.model

string

The model used for the task.

​

task.ratio

string

The actual aspect ratio of the generated video.

​

task.resolution

string

The resolution of the generated video.

​

task.status

string

Task status. Options: queued, running, succeeded, failed, cancelled, expired.

​

task.task_type

string

The type of the task.

​

task.usage

object

Usage recorded for the task.

​

task.usage.completion_tokens

integer

​

task.usage.input_image_count

integer

​

task.usage.input_seconds

number

​

task.usage.output_seconds

number

​

task.usage.prompt_tokens

integer

​

task.usage.total_seconds

number

​

task.usage.total_tokens

integer

## 

​

Examples

### 

​

Input
    
    
    {
      "content": [
        {
          "text": "A single red maple leaf resting on a plain white background.",
          "type": "text"
        }
      ],
      "duration": 5,
      "ratio": "16:9",
      "resolution": "768P"
    }
    

### 

​

Output
    
    
    {
      "task": {
        "content": {
          "url": "https://example.invalid/minimax/minimax-h3/generated.mp4"
        },
        "duration": 6,
        "id": "3f7a1b28-5c0d-4e91-8a6f-1b2c3d4e5f60",
        "model": "MiniMax-H3",
        "ratio": "16:9",
        "resolution": "768P",
        "status": "succeeded",
        "usage": {
          "output_seconds": 6,
          "total_seconds": 6
        }
      }
    }
    

**The MP4 carries a generated audio track.** H3 is omni-modal: voice, sound effects and music are synthesised jointly with the picture in a single forward pass, not layered on afterwards, and the result is one MP4 with native stereo audio. Nothing in the request body above switches that off: the documented fields are the prompt content, `duration`, `ratio`, `resolution`, `seed`, `aigc_watermark` and `callback_url`, and none of them selects a silent render. A pipeline that means to lay its own voiceover over the clip therefore has to mute or strip the returned track first, or it will mux over a clip that is already talking. The prompt is what steers the audio: describe the dialogue, the sound effects and the music in the same prompt block as the shot. See the [MiniMax H3 prompt guide](https://docs.comfy.org/tutorials/video/minimax/minimax-h3-prompt-guide) for how to structure one, and the [MiniMax H3 overview](https://docs.comfy.org/tutorials/video/minimax/minimax-h3) for what the model does in ComfyUI. The video URL expires. Router re-hosts the MP4 and answers a Comfy-signed URL valid for 12 hours, falling back to MiniMax’s own shorter-lived link when the re-host fails. The `task.content.url` description in the response schema above tells you to query again for a refreshed URL: that is MiniMax’s own wording for their API, carried through unchanged, and Router does not expose MiniMax’s task-query route. Re-reading a queued request’s result route returns the stored result document while the request is [retained, for 24 hours after it completes](https://docs.comfy.org/development/comfy-router/queue#idempotency-and-billing), but nothing documents that read as minting a newly signed URL. Download the MP4 promptly rather than storing the link.

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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/minimax/minimax-h3/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/minimax/minimax-h3/code)

[Use Rigging with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/meshy/rigging/code)[Use Image To Video with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/moonvalley/image-to-video/code)

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
