---
url: https://docs.comfy.org/development/comfy-router/models/openai/gpt-image-2/code/
title: Use GPT Image 2 with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:31.524282+00:00
---

# Use GPT Image 2 with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/openai/gpt-image-2/code/

## On this page

  * Quick start
  * Serving providers
  * Schema
    * Input
    * Output
  * Examples
    * Input
    * Output
  * Before you ship



OpenAI

# Use GPT Image 2 with Comfy Router

Copy pageCopy page

Call openai/gpt-image-2 through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `openai/gpt-image-2`, served by Comfy Router from OpenAI. **Input:** Text, Image · **Output:** Image

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `openai/gpt-image-2` **Endpoint:** `POST https://api.comfy.org/v2/models/openai/gpt-image-2`

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
            "openai/gpt-image-2",
            {
                "prompt": "a rocketship on a launchpad",
                "quality": "low",
                "size": "1024x1024",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("openai/gpt-image-2", {
      prompt: "a rocketship on a launchpad",
      quality: "low",
      size: "1024x1024",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/openai/gpt-image-2 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"a rocketship on a launchpad\", \"quality\": \"low\", \"size\": \"1024x1024\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/openai/gpt-image-2/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "openai/gpt-image-2",
                {
                    "prompt": "a rocketship on a launchpad",
                    "quality": "low",
                    "size": "1024x1024",
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
    const handle = await comfy.models.submit("openai/gpt-image-2", {
      prompt: "a rocketship on a launchpad",
      quality: "low",
      size: "1024x1024",
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
    curl https://api.comfy.org/v2/models/openai/gpt-image-2/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"a rocketship on a launchpad\", \"quality\": \"low\", \"size\": \"1024x1024\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/openai/gpt-image-2/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/openai/gpt-image-2/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Serving providers

This model is served by Comfy Router directly unless the request names another provider. The providers below serve it too, on the same endpoint and with the same model ID, selected with the `model_provider` query parameter.

  * **Comfy** (default): `POST https://api.comfy.org/v2/models/openai/gpt-image-2`
  * **fal** , as `fal/fal-gpt-image-2`: `POST https://api.comfy.org/v2/models/openai/gpt-image-2?model_provider=fal`
  * **Pika** , as `pika/pika-gpt-image-2`: `POST https://api.comfy.org/v2/models/openai/gpt-image-2?model_provider=pika`
  * **Runware** , as `runware/runware-gpt-image-2`: `POST https://api.comfy.org/v2/models/openai/gpt-image-2?model_provider=runware`
  * **WaveSpeed** , as `wavespeed/wavespeed-gpt-image-2`: `POST https://api.comfy.org/v2/models/openai/gpt-image-2?model_provider=wavespeed`

`strict_mode` defaults to false, so Router translates the native request body documented on this page into the provider’s own schema and translates the response back. See [`model_provider`, `strict_mode` and `fallback_provider`](https://docs.comfy.org/development/comfy-router/reference#post-v2modelsprovidermodel) in the API reference, and [Serving providers](https://docs.comfy.org/development/comfy-router/providers) for every model routed this way.

## 

​

Schema

### 

​

Input

​

background

string

Background transparency. `auto` lets the model choose.Possible values: `transparent`, `opaque`, `auto`

​

image

string | string[]

The source image(s) to edit. PRESENCE OF THIS FIELD SELECTS THE EDIT OPERATION — omit it entirely for text-to-image generation. The model’s published example is the GENERATION call, which omits this field. Adding `image` is the whole of the difference between the two modes — same endpoint, same model id — except that an edit prompt describes the CHANGE you want rather than the scene, so the edit body below reads differently from the generation example even though only this field is structurally new. It is copyable exactly as printed: `{"prompt": "give the rocketship rainbow coloring", "image": ["data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg=="], "size": "1024x1024"}` — the payload is a complete 1x1 PNG, not an abbreviation, and this body is pinned as an accepted case in Router’s own request-validation tests. Swap in your own image’s bytes. Accepts one image or an array of them; gpt-image-1 and later take up to 16, which Router enforces from this schema before dispatching.

​

mask

string

One image, as either an https URL Router fetches on the caller’s behalf or a `data:image/<format>;base64,<payload>` URI carrying the bytes inline. Accepted image types are png, webp and jpeg, and that set is ENFORCED at resolve time rather than left to the provider — an svg, gif, avif or tiff is refused here, naming the image you sent, instead of becoming a partner error two hops from the cause. Prefer the URL form. A base64 payload inflates roughly 4/3 and the whole request body is capped at 100 MiB, so the inline form caps out near a 75 MB source image; a URL sidesteps that entirely. The per-image and per-request media ceilings stated at the end of this description are tighter than the body cap, so for an image of any real size they are what you meet first. THE URL MUST RESOLVE WITHOUT YOUR CREDENTIALS. Router fetches it server-side and sends no caller credential with the request, so a presigned URL — one whose signature is in the query string — is the supported form. An authenticated endpoint such as `/api/assets/{id}/content` answers Router 401 rather than the image; request that URL yourself and pass the signed URL it redirects to. THE FETCH IS CONFINED TO A NAMED SET OF HOSTS rather than the open internet, and the same list is re-applied to every redirect hop as well as to the URL you send — so a URL on any other host, or one that redirects off the list, is refused before any provider is contacted. Today that list is Comfy’s own asset delivery only: a signed `storage.googleapis.com` URL under a Comfy asset bucket, which is the form `/api/assets/{id}/content` redirects you to. A partner CDN or a plain https host is NOT on the list. TWO WIDENINGS ARE BEING ROLLED OUT AND ARE BOTH OFF BY DEFAULT TODAY. They ship behind ONE switch and are enabled together, so treat everything below as forthcoming rather than as something to build against yet — ask before you rely on either. The FIRST is the bucket `POST /customers/storage` signs your upload into. Until the rollout reaches your environment an upload URL from that endpoint is refused here, even though the bucket is Comfy’s own and the host is the same one — so “upload to Comfy, then pass the URL” does NOT work yet, and the form that does is the signed URL `/api/assets/{id}/content` redirects to. The SECOND is ENABLED PER ACCOUNT rather than for everyone at once, because the bucket behind these hosts is yours rather than ours: even once the switch above is on, an account that has not had third-party inbound media enabled is refused, and told so in those words rather than told the host is unsupported. Ask your Comfy contact to enable it for your account. It additionally admits these third-party object-storage hosts, where the bucket is yours and Router makes no ownership claim on it: Cloudflare R2 (`<account>.r2.cloudflarestorage.com`, `pub-<hash>.r2.dev`), Amazon S3 (`s3.amazonaws.com` and `s3.<region>.amazonaws.com`, in either the path-style or the `<bucket>.`-prefixed form), Azure Blob Storage (`<account>.blob.core.windows.net`) and Alibaba Cloud OSS (`<bucket>.oss-<region>.aliyuncs.com`, including the `oss-accelerate` endpoint). Those are object-storage endpoints specifically: a general-purpose endpoint on the same provider domain, such as an Alibaba Function Compute trigger, is not on the list and is refused. WHAT IS MATCHED IS THE HOSTNAME FORM, NOT THE PROVIDER — so naming a provider above does NOT mean every URL that provider can issue is accepted, and three near-misses are worth stating outright because a caller can reasonably arrive with each of them. An R2 CUSTOM DOMAIN (`cdn.example.com`) is NOT accepted: Cloudflare documents `pub-<hash>.r2.dev` as a rate-limited debug hostname and points production traffic at a custom domain instead, but a custom domain carries nothing in its hostname identifying it as R2, so Router cannot tell it from any other host and refuses it — presign the `<account>.r2.cloudflarestorage.com` endpoint, or use the `pub-<hash>.r2.dev` form. S3’s IPv6 dualstack endpoint (`s3.dualstack.<region>.amazonaws.com`) is not accepted either; use the plain regional endpoint. Nor is Azure Blob’s alternate DNS zone (`<account>.z<N>.blob.storage.azure.net`); use `<account>.blob.core.windows.net`. The refusal you get back names these same forms, so you do not have to come here to read them. The `<account>` and `pub-<hash>` placeholders above show the form you will normally arrive with; they are not a depth restriction. Matching is on the object-storage domain suffix, so a deeper name under the same namespace (`a.b.pub-<hash>.r2.dev`) is accepted as well. What is NOT widened by that is the namespace itself — the suffix still has to be one of the ones listed. The example below shows the shape only: a real value also carries the signing query parameters, which are deliberately omitted here because a published example lives in the spec forever and a real signature is both a leaked credential and a link that stops working. Each image is capped at 25 MiB and one request’s images at 64 MiB in total.

​

model

string

The gpt-image model to run. Router splices the addressed model id in, so a caller addressing /v2/models/openai/gpt-image-2 does not send this.

​

moderation

string

Content moderation settingPossible values: `low`, `auto`

​

n

integer

The number of images to generate (1-10).Range: `1` to `10`

​

output_compression

integer

Compression level for JPEG or WebP (0-100)Range: `0` to `100`

​

output_format

string

Format of the output imagePossible values: `png`, `webp`, `jpeg`

​

partial_images

integer

Meaningful only alongside a live stream, which this surface cannot serve — `stream` is settled to `false` even when you send it. On a generation, any value other than `0` or `null` is refused with a 400, whether or not the request also sends `stream: true`; on a request carrying `image` the field is dropped rather than forwarded. Omit it.Range: `0` to `3`

​

prompt

string

required

A text description of the image to generate, or of the edit to make to `image`.

​

quality

string

The quality of the generated or edited image. `xhigh` and `max` are the two tiers gpt-image-2.5-flare and gpt-image-2.5-sunburst were added for; `standard` and `hd` are dall-e-era spellings no admitted model reads.Possible values: `auto`, `low`, `medium`, `high`, `xhigh`, `max`, `standard`, `hd`

​

size

string

Size of the image (e.g., 1024x1024, 1536x1024, auto)

​

stream

boolean

Declared so a caller who sends it is not refused, but INERT on this surface: Router SETTLES it to `false` before dispatch, because it captures the provider response rather than relaying a `text/event-stream` (a request carrying `image` drops the field instead, since the edit is re-encoded without it). No Comfy surface serves gpt-image partial-image streaming: the v1 `POST /proxy/openai/images/generations` ingress refuses `stream: true` with a 400 and never forwards the request upstream, so omit the field and read the completed response as one JSON body. Because the stream never opens, OpenAI’s restriction on combining `stream: true` with `n` greater than 1 does not apply here; `n` is forwarded as sent.

​

user

string

A unique identifier for end-user monitoring

Generated from the schema Router serves at `GET /v2/models/openai/gpt-image-2/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

data

object[]

​

data[].b64_json

string

Base64 encoded image data

​

data[].revised_prompt

string

Revised prompt

​

data[].url

string

URL of the image

​

usage

object

​

usage.input_tokens

integer

​

usage.input_tokens_details

object

​

usage.input_tokens_details.image_tokens

integer

​

usage.input_tokens_details.text_tokens

integer

​

usage.output_tokens

integer

​

usage.output_tokens_details

object

​

usage.output_tokens_details.image_tokens

integer

​

usage.output_tokens_details.text_tokens

integer

​

usage.total_tokens

integer

​

background

string

Whether the generated image’s background is `opaque` or `transparent`, as OpenAI resolved it for this generation. The request parameter defaults to `auto`, so this is where a caller who did not pin it learns which one was produced.

​

created

integer

Unix timestamp, in seconds, of when the generation completed. It is the one member OpenAI declares REQUIRED on an image-generation response, so it is present whenever OpenAI is the producer; a fal-, pika-, wavespeed- or runware-served response on any of the alt-backed ids omits it entirely, like the other four resolved-parameter members. Declared `int64` because a present-day epoch value is close enough to 2^31 that an unformatted `integer` generates a 32-bit field in many SDK generators.Format: `int64`

​

output_format

string

The encoding of the bytes in `data[].b64_json` — `png`, `webp` or `jpeg`. It is the format OpenAI actually encoded, which is the request’s `output_format` when one was sent and `png` when none was, so a decoder can key off it rather than re-deriving the format from the request.

​

quality

string

The quality tier the generation actually ran at — OpenAI reports one of `low`, `medium`, `high`, `xhigh` or `max`. It is the RESOLVED tier, not an echo of the request, whose own `quality` defaults to `auto`.

​

size

string

The pixel dimensions the generation actually ran at, as `<width>x<height>`. It is the RESOLVED size: the request’s `size` defaults to `auto` and explicitly admits `auto`, so this is the only place the dimensions actually used are reported.

## 

​

Examples

### 

​

Input
    
    
    {
      "prompt": "a rocketship on a launchpad",
      "quality": "low",
      "size": "1024x1024"
    }
    

### 

​

Output
    
    
    {
      "created": 1767225600,
      "data": [
        {
          "b64_json": "PGJhc2U2ND4="
        }
      ],
      "usage": {
        "input_tokens": 12,
        "input_tokens_details": {
          "image_tokens": 0,
          "text_tokens": 12
        },
        "output_tokens": 1056,
        "total_tokens": 1068
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/openai/gpt-image-2/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/openai/gpt-image-2/code)

[Use GPT Image 2.5 Sunburst with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/openai/gpt-image-2-5-sunburst/code)[Use o1-pro with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/openai/o1-pro/code)

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
