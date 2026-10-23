---
url: https://docs.comfy.org/development/comfy-router/models/ideogram/ideogram-4-5/code/
title: Use Ideogram 4.5 with Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:11.925380+00:00
---

# Use Ideogram 4.5 with Comfy Router - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/models/ideogram/ideogram-4-5/code/

## On this page

  * Quick start
  * Schema
    * Input
    * Output
  * Examples
    * Input
    * Output
  * Before you ship



Ideogram

# Use Ideogram 4.5 with Comfy Router

Copy pageCopy page

Call ideogram/ideogram-4-5 through Comfy Router: endpoint, request shape and the response Router returns.

Copy pageCopy page

API Reference for `ideogram/ideogram-4-5`, served by Comfy Router from Ideogram. **Input:** Text, Image · **Output:** Image

## 

​

Quick start

Create a key in [your Comfy workspace](https://platform.comfy.org/profile/api-keys?onboarding=router) and export it as `COMFY_API_KEY`. The Python and TypeScript snippets use the Comfy SDKs (`pip install comfy-sdk` and `npm install @comfyorg/sdk`); the cURL snippet is the same call over raw HTTP. **Model ID:** `ideogram/ideogram-4-5` **Endpoint:** `POST https://api.comfy.org/v2/models/ideogram/ideogram-4-5`

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
            "ideogram/ideogram-4-5",
            {
                "prompt": "A poster for a jazz festival, bold typography, warm colours",
                "quality": "low",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("ideogram/ideogram-4-5", {
      prompt: "A poster for a jazz festival, bold typography, warm colours",
      quality: "low",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/ideogram/ideogram-4-5 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"A poster for a jazz festival, bold typography, warm colours\", \"quality\": \"low\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/ideogram/ideogram-4-5/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Queued delivery](https://docs.comfy.org/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "ideogram/ideogram-4-5",
                {
                    "prompt": "A poster for a jazz festival, bold typography, warm colours",
                    "quality": "low",
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
    const handle = await comfy.models.submit("ideogram/ideogram-4-5", {
      prompt: "A poster for a jazz festival, bold typography, warm colours",
      quality: "low",
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
    curl https://api.comfy.org/v2/models/ideogram/ideogram-4-5/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"A poster for a jazz festival, bold typography, warm colours\", \"quality\": \"low\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/ideogram/ideogram-4-5/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/ideogram/ideogram-4-5/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Schema

### 

​

Input

​

enable_copyright_detection

boolean

Opt into post-generation copyright detection.

​

image

string

One image, as either an https URL Router fetches on the caller’s behalf or a `data:image/<format>;base64,<payload>` URI carrying the bytes inline. Accepted image types are png, webp and jpeg, and that set is ENFORCED at resolve time rather than left to the provider — an svg, gif, avif or tiff is refused here, naming the image you sent, instead of becoming a partner error two hops from the cause. Prefer the URL form. A base64 payload inflates roughly 4/3 and the whole request body is capped at 100 MiB, so the inline form caps out near a 75 MB source image; a URL sidesteps that entirely. The per-image and per-request media ceilings stated at the end of this description are tighter than the body cap, so for an image of any real size they are what you meet first. THE URL MUST RESOLVE WITHOUT YOUR CREDENTIALS. Router fetches it server-side and sends no caller credential with the request, so a presigned URL — one whose signature is in the query string — is the supported form. An authenticated endpoint such as `/api/assets/{id}/content` answers Router 401 rather than the image; request that URL yourself and pass the signed URL it redirects to. THE FETCH IS CONFINED TO A NAMED SET OF HOSTS rather than the open internet, and the same list is re-applied to every redirect hop as well as to the URL you send — so a URL on any other host, or one that redirects off the list, is refused before any provider is contacted. Today that list is Comfy’s own asset delivery only: a signed `storage.googleapis.com` URL under a Comfy asset bucket, which is the form `/api/assets/{id}/content` redirects you to. A partner CDN or a plain https host is NOT on the list. TWO WIDENINGS ARE BEING ROLLED OUT AND ARE BOTH OFF BY DEFAULT TODAY. They ship behind ONE switch and are enabled together, so treat everything below as forthcoming rather than as something to build against yet — ask before you rely on either. The FIRST is the bucket `POST /customers/storage` signs your upload into. Until the rollout reaches your environment an upload URL from that endpoint is refused here, even though the bucket is Comfy’s own and the host is the same one — so “upload to Comfy, then pass the URL” does NOT work yet, and the form that does is the signed URL `/api/assets/{id}/content` redirects to. The SECOND is ENABLED PER ACCOUNT rather than for everyone at once, because the bucket behind these hosts is yours rather than ours: even once the switch above is on, an account that has not had third-party inbound media enabled is refused, and told so in those words rather than told the host is unsupported. Ask your Comfy contact to enable it for your account. It additionally admits these third-party object-storage hosts, where the bucket is yours and Router makes no ownership claim on it: Cloudflare R2 (`<account>.r2.cloudflarestorage.com`, `pub-<hash>.r2.dev`), Amazon S3 (`s3.amazonaws.com` and `s3.<region>.amazonaws.com`, in either the path-style or the `<bucket>.`-prefixed form), Azure Blob Storage (`<account>.blob.core.windows.net`) and Alibaba Cloud OSS (`<bucket>.oss-<region>.aliyuncs.com`, including the `oss-accelerate` endpoint). Those are object-storage endpoints specifically: a general-purpose endpoint on the same provider domain, such as an Alibaba Function Compute trigger, is not on the list and is refused. WHAT IS MATCHED IS THE HOSTNAME FORM, NOT THE PROVIDER — so naming a provider above does NOT mean every URL that provider can issue is accepted, and three near-misses are worth stating outright because a caller can reasonably arrive with each of them. An R2 CUSTOM DOMAIN (`cdn.example.com`) is NOT accepted: Cloudflare documents `pub-<hash>.r2.dev` as a rate-limited debug hostname and points production traffic at a custom domain instead, but a custom domain carries nothing in its hostname identifying it as R2, so Router cannot tell it from any other host and refuses it — presign the `<account>.r2.cloudflarestorage.com` endpoint, or use the `pub-<hash>.r2.dev` form. S3’s IPv6 dualstack endpoint (`s3.dualstack.<region>.amazonaws.com`) is not accepted either; use the plain regional endpoint. Nor is Azure Blob’s alternate DNS zone (`<account>.z<N>.blob.storage.azure.net`); use `<account>.blob.core.windows.net`. The refusal you get back names these same forms, so you do not have to come here to read them. The `<account>` and `pub-<hash>` placeholders above show the form you will normally arrive with; they are not a depth restriction. Matching is on the object-storage domain suffix, so a deeper name under the same namespace (`a.b.pub-<hash>.r2.dev`) is accepted as well. What is NOT widened by that is the namespace itself — the suffix still has to be one of the ones listed. The example below shows the shape only: a real value also carries the signing query parameters, which are deliberately omitted here because a published example lives in the spec forever and a real signature is both a leaked credential and a link that stops working. Each image is capped at 25 MiB and one request’s images at 64 MiB in total.

​

images

string[]

Optional source images for the generate operation. The first is the primary source and the rest are references. Up to five, or four with a mask.

​

magic_prompt

string

Generate only. Prompt rewriting for text-to-image. Supported values are auto, on, and off. Defaults to auto.

​

mask

string

One image, as either an https URL Router fetches on the caller’s behalf or a `data:image/<format>;base64,<payload>` URI carrying the bytes inline. Accepted image types are png, webp and jpeg, and that set is ENFORCED at resolve time rather than left to the provider — an svg, gif, avif or tiff is refused here, naming the image you sent, instead of becoming a partner error two hops from the cause. Prefer the URL form. A base64 payload inflates roughly 4/3 and the whole request body is capped at 100 MiB, so the inline form caps out near a 75 MB source image; a URL sidesteps that entirely. The per-image and per-request media ceilings stated at the end of this description are tighter than the body cap, so for an image of any real size they are what you meet first. THE URL MUST RESOLVE WITHOUT YOUR CREDENTIALS. Router fetches it server-side and sends no caller credential with the request, so a presigned URL — one whose signature is in the query string — is the supported form. An authenticated endpoint such as `/api/assets/{id}/content` answers Router 401 rather than the image; request that URL yourself and pass the signed URL it redirects to. THE FETCH IS CONFINED TO A NAMED SET OF HOSTS rather than the open internet, and the same list is re-applied to every redirect hop as well as to the URL you send — so a URL on any other host, or one that redirects off the list, is refused before any provider is contacted. Today that list is Comfy’s own asset delivery only: a signed `storage.googleapis.com` URL under a Comfy asset bucket, which is the form `/api/assets/{id}/content` redirects you to. A partner CDN or a plain https host is NOT on the list. TWO WIDENINGS ARE BEING ROLLED OUT AND ARE BOTH OFF BY DEFAULT TODAY. They ship behind ONE switch and are enabled together, so treat everything below as forthcoming rather than as something to build against yet — ask before you rely on either. The FIRST is the bucket `POST /customers/storage` signs your upload into. Until the rollout reaches your environment an upload URL from that endpoint is refused here, even though the bucket is Comfy’s own and the host is the same one — so “upload to Comfy, then pass the URL” does NOT work yet, and the form that does is the signed URL `/api/assets/{id}/content` redirects to. The SECOND is ENABLED PER ACCOUNT rather than for everyone at once, because the bucket behind these hosts is yours rather than ours: even once the switch above is on, an account that has not had third-party inbound media enabled is refused, and told so in those words rather than told the host is unsupported. Ask your Comfy contact to enable it for your account. It additionally admits these third-party object-storage hosts, where the bucket is yours and Router makes no ownership claim on it: Cloudflare R2 (`<account>.r2.cloudflarestorage.com`, `pub-<hash>.r2.dev`), Amazon S3 (`s3.amazonaws.com` and `s3.<region>.amazonaws.com`, in either the path-style or the `<bucket>.`-prefixed form), Azure Blob Storage (`<account>.blob.core.windows.net`) and Alibaba Cloud OSS (`<bucket>.oss-<region>.aliyuncs.com`, including the `oss-accelerate` endpoint). Those are object-storage endpoints specifically: a general-purpose endpoint on the same provider domain, such as an Alibaba Function Compute trigger, is not on the list and is refused. WHAT IS MATCHED IS THE HOSTNAME FORM, NOT THE PROVIDER — so naming a provider above does NOT mean every URL that provider can issue is accepted, and three near-misses are worth stating outright because a caller can reasonably arrive with each of them. An R2 CUSTOM DOMAIN (`cdn.example.com`) is NOT accepted: Cloudflare documents `pub-<hash>.r2.dev` as a rate-limited debug hostname and points production traffic at a custom domain instead, but a custom domain carries nothing in its hostname identifying it as R2, so Router cannot tell it from any other host and refuses it — presign the `<account>.r2.cloudflarestorage.com` endpoint, or use the `pub-<hash>.r2.dev` form. S3’s IPv6 dualstack endpoint (`s3.dualstack.<region>.amazonaws.com`) is not accepted either; use the plain regional endpoint. Nor is Azure Blob’s alternate DNS zone (`<account>.z<N>.blob.storage.azure.net`); use `<account>.blob.core.windows.net`. The refusal you get back names these same forms, so you do not have to come here to read them. The `<account>` and `pub-<hash>` placeholders above show the form you will normally arrive with; they are not a depth restriction. Matching is on the object-storage domain suffix, so a deeper name under the same namespace (`a.b.pub-<hash>.r2.dev`) is accepted as well. What is NOT widened by that is the namespace itself — the suffix still has to be one of the ones listed. The example below shows the shape only: a real value also carries the signing query parameters, which are deliberately omitted here because a published example lives in the spec forever and a real signature is both a leaked credential and a link that stops working. Each image is capped at 25 MiB and one request’s images at 64 MiB in total.

​

num_images

integer

default:"1"

Number of images to return. Each is billed.Range: `1` to `8`

​

prompt

string

required

The instruction or description for the image, 1 to 10,000 characters.

​

quality

string

Quality tier, which is also the billed rate. With source images: very_low, low, medium, or high (default medium). Without source images: low, medium, or high (default high); very_low on a text-to-image request is refused.Possible values: `very_low`, `low`, `medium`, `high`

​

reference_images

string[]

Optional reference images for Precise Edit; requires `image`. Up to four, or three with a mask.

​

seed

integer

Seed for reproducible results.Range: `0` to `2147483647`

​

size

string

Generate only. Output size. auto (default), source (requires images), or WIDTHxHEIGHT. Omit it when you send a mask; a request that sets both is refused.

Generated from the schema Router serves at `GET /v2/models/ideogram/ideogram-4-5/openapi.json`, the same document it validates a call against before the request reaches the provider.

### 

​

Output

​

data

object[]

The generated images.

​

data[].is_image_safe

boolean

Indicates whether the image is considered safe. Only use images where this is true.

​

data[].prompt

string

The prompt used to generate this image.

​

data[].resolution

string

The resolution of the generated image.

​

data[].seed

integer

The seed used for this image.

​

data[].url

string

URL to the generated image.

​

generation_id

string

The identifier of the generation.

​

seed

integer

The seed used for the generation.

## 

​

Examples

### 

​

Input
    
    
    {
      "prompt": "A poster for a jazz festival, bold typography, warm colours",
      "quality": "low"
    }
    

### 

​

Output
    
    
    {
      "data": [
        {
          "is_image_safe": true,
          "prompt": "A poster for a jazz festival, bold typography, warm colours",
          "resolution": "2048x2048",
          "seed": 918273645,
          "url": "https://example.invalid/ideogram/ideogram-4-5/generated.png"
        }
      ],
      "generation_id": "gen_0123456789",
      "seed": 918273645
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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/models/ideogram/ideogram-4-5/code.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/models/ideogram/ideogram-4-5/code)

[Use Higgsfield Kling 3 Pro with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/higgsfield/higgsfield-kling-3-pro/code)[Use Ideogram V3 with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/ideogram/ideogram-v3/code)

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
