---
url: https://docs.comfy.org/development/comfy-router/models/black-forest-labs/flux-3-video/code/
title: Use FLUX 3 Video with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:24.928940+00:00
---

# Use FLUX 3 Video with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/black-forest-labs/flux-3-video/code/

## On this page

  * Quick start
  * Schema
    * Input
    * Output
  * Examples
    * Input
    * Output
  * Before you ship



Black Forest Labs

# Use FLUX 3 Video with Comfy Router

Copy pageCopy page

Python, TypeScript and cURL snippets for generating video with audio from FLUX 3 through Comfy Router, plus request fields and result shape

Copy pageCopy page

API Reference for FLUX 3 Video. FLUX 3 Video is Black Forest Labs’ video generation model, turning a text prompt into a short clip with synchronized audio. **Input:** Text, Image · **Output:** Video + Audio

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `bfl/flux-3-video` **Endpoint:** `POST https://api.comfy.org/v2/models/bfl/flux-3-video`

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
                "bfl/flux-3-video",
                {
                    "mode": "t2v",
                    "prompt": "a single red maple leaf falling onto still water, slow motion",
                    "duration": 5,
                    "aspect_ratio": "16:9",
                    "generate_audio": True,
                },
            )
    
        print("video:", result["result"]["sample"])
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    type Result = { result: { sample: string } };
    const result = await comfy.models.run<Result>("bfl/flux-3-video", {
      mode: "t2v",
      prompt: "a single red maple leaf falling onto still water, slow motion",
      duration: 5,
      aspect_ratio: "16:9",
      generate_audio: true,
    });
    if (result.kind !== "json") throw new Error("expected a JSON result");
    
    console.log("video:", result.data.result.sample);
    
    
    
    curl https://api.comfy.org/v2/models/bfl/flux-3-video \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"mode\": \"t2v\", \"prompt\": \"a single red maple leaf falling onto still water, slow motion\", \"duration\": 5, \"aspect_ratio\": \"16:9\", \"generate_audio\": true}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/bfl/flux-3-video/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "bfl/flux-3-video",
                {
                    "mode": "t2v",
                    "prompt": "a single red maple leaf falling onto still water, slow motion",
                    "duration": 5,
                    "aspect_ratio": "16:9",
                    "generate_audio": True,
                },
            )
            print("request_id:", handle.request_id)  # with the model ID, all another process needs
    
            # Poll until the request completes, waiting the Retry-After the server names.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # The provider's own payload, the same value models.run() returns.
            # A request that failed or was cancelled raises the typed Router error here.
            result = await handle.get()
    
        print("video:", result["result"]["sample"])
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // Each submit() call mints its own Idempotency-Key and reuses it for automatic retries.
    type Result = { result: { sample: string } };
    const handle = await comfy.models.submit<Result>("bfl/flux-3-video", {
      mode: "t2v",
      prompt: "a single red maple leaf falling onto still water, slow motion",
      duration: 5,
      aspect_ratio: "16:9",
      generate_audio: true,
    });
    console.log("requestId:", handle.requestId); // with the model ID, all another process needs
    
    // Poll until the request completes, waiting the Retry-After the server names.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // The same result models.run() returns. A request that failed or was cancelled rejects here.
    const result = await handle.get();
    if (result.kind !== "json") throw new Error("expected a JSON result");
    
    console.log("video:", result.data.result.sample);
    
    
    
    # 1. Submit. Router answers 201 with request_id, status_url, response_url and cancel_url.
    curl https://api.comfy.org/v2/models/bfl/flux-3-video/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"mode\": \"t2v\", \"prompt\": \"a single red maple leaf falling onto still water, slow motion\", \"duration\": 5, \"aspect_ratio\": \"16:9\", \"generate_audio\": true}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/bfl/flux-3-video/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/bfl/flux-3-video/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Schema

### 

​

Input

​

aspect_ratio

string

default:"\"auto\""

Output aspect ratio: auto, 21:9, 2:1, 16:9, 4:3, 1:1, 3:4, or 9:16. auto lets BFL choose from the prompt and any references.

​

draft

boolean

default:"false"

Draft mode: generate a fast preview whose result includes a draft_cache download URL. Send that bundle back with mode draft_enhance to render the full-quality version of the same generation.

​

draft_cache

string

draft_enhance only. Encrypted draft-cache bundle from a prior draft generation, as the base64-encoded downloaded bundle or its still-valid http(s) URL. The original inputs are embedded in the bundle.

​

duration

integer | string

default:"\"auto\""

Video duration in seconds (any whole second from 5 to 20), or auto to fit the content.Range: `5` to `20`

​

generate_audio

boolean

default:"true"

Generate synchronized audio alongside the video.

​

keyframes

string | number | string[] | string[] | number | string[][]

i2v only. Images that become frames of the video, each an http(s) URL or base64, one to ten total. Accepts a single image, a list of images (one starts the video, two start and end it, more spread evenly and need a set duration), or timestamped [seconds, image] pairs in time order, e.g. [[0, ”…”], [3.5, ”…”]]. A pair is a two-element array: number of seconds first, then the image.

​

mode

string

required

Generation mode: t2v (text-to-video), i2v (image-continuation), v2v (video-continuation), or draft_enhance (full-quality render of a prior draft). Spelled-out aliases such as text-to-video are accepted.

​

prompt

string

Free-form prompt describing the video. Required for every mode except draft_enhance.

​

resolution

string

Video resolution class: hd (720p), or fhd (1080p), qhd (2K) or uhd (4K) for a higher-resolution result finished by the video upsampler. Defaults to hd for t2v, i2v and v2v, and to fhd for draft_enhance. Exact dimensions vary with the aspect ratio.Possible values: `hd`, `fhd`, `qhd`, `uhd`

​

safety_tolerance

integer

default:"2"

Tolerance level for input and output harm moderation, 0 strictest. Sexual content is limited to level 3 and hate content to level 2 regardless of the requested tolerance; requests with conditioning media are limited to level 2.Range: `0` to `4`

​

start_video

string

v2v only. The video to continue, an http(s) URL or base64 MP4; the generated clip carries on from its final frames.

​

version

string

default:"\"latest\""

Endpoint version. latest serves the current release; dated pinnable release tags are added as they are published.

Generated from the schema Router serves at `GET /v2/models/bfl/flux-3-video/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

cost

number

Provider-reported cost in credits, populated once the task is Ready.Format: `float`

​

id

string

required

BFL task identifier.

​

progress

number

Optional generation progress reported by BFL.Range: `0` to `1`Format: `float`

​

result

object

required

The finished generation. Exactly one of the two URL leaves is populated: `sample` in the default mode, `draft_cache` in `draft: true` mode.

​

result.cost

number

Provider-reported task cost. This is BFL’s number, not the Comfy charge.Format: `double`

​

result.draft_cache

string (uri)

Signed URL returned INSTEAD of `sample` by the `draft: true` mode, re-hosted onto Comfy storage the same way `sample` is: normally a Comfy-hosted URL valid for up to 24 hours, and BFL’s own roughly two-hour delivery URL when the re-host could not be performed.Format: `uri`

​

result.sample

string (uri)

Signed URL for the generated MP4. Router re-hosts the asset onto Comfy storage and rewrites this field, so it is normally a Comfy-hosted URL valid for up to 24 hours - signed for 24 hours when minted and replayed from a 23-hour memo, so a later poll can hand back one with as little as an hour left; a leaf whose re-host could not be performed keeps BFL’s own roughly two-hour delivery URL instead. Absent in `draft: true` mode.Format: `uri`

​

status

string

required

Task status: Pending, Reasoning, Generating, Ready, Request Moderated, Content Moderated, Error, or Task not found. Compare case-insensitively; Router forwards BFL’s spelling unchanged.

## 

​

Examples

### 

​

Input
    
    
    {
      "mode": "t2v",
      "prompt": "a single red maple leaf falling onto still water, slow motion",
      "duration": 5,
      "aspect_ratio": "16:9",
      "generate_audio": true
    }
    

### 

​

Output
    
    
    {
      "id": "0a1b2c3d-...",
      "status": "Ready",
      "result": {
        "sample": "https://.../out.mp4"
      }
    }
    

`result.sample` is normally a Comfy-hosted signed URL, valid for up to 24 hours from creation. A replay can return an older URL, and an asset that could not be re-hosted keeps its shorter-lived provider URL. Download the MP4 promptly rather than storing the link. With `draft: true`, read `result.draft_cache` instead of expecting `result.sample`.

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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/black-forest-labs/flux-3-video/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/black-forest-labs/flux-3-video/code)

[Use FLUX 3 Image with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/black-forest-labs/flux-3-image/code)[Use FLUX Pro 1.0 Expand with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/black-forest-labs/flux-pro-1-0-expand/code)

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
