---
url: https://docs.comfy.org/development/comfy-router/api/
title: Comfy Router API overview - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:43.778308+00:00
---

# Comfy Router API overview - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/api/

## On this page

  * Guides
  * Per-model examples
  * Next



Router API

# Comfy Router API overview

Copy pageCopy page

How the Comfy Router API works: one route per model ID, with guides for discovery, schemas, queued requests, errors, and billing.

Copy pageCopy page

Choose a model, inspect its schema, and call `POST /v2/models/{provider}/{model}`. The route and authentication stay the same across models. Each model accepts its own native request body and returns its own native result.

## 

​

Guides

## Discover models

List the catalog, page through it, and read one model’s entry.

## Schemas and results

Fetch a model’s input and output schema and read its result.

## Queued requests

Submit a run now, then poll, collect, or cancel it later.

## Errors and retries

Read error responses and retry without a second charge.

## Billing

What is charged, policy-refusal billing, and reconciling usage.

## 

​

Per-model examples

  * [Google Gemini](https://docs.comfy.org/development/comfy-router/models/google/gemini/code)
  * [Nano Banana 2](https://docs.comfy.org/development/comfy-router/models/google/nano-banana-2/code)
  * [Nano Banana 2 Lite](https://docs.comfy.org/development/comfy-router/models/google/nano-banana-2-lite/code)
  * [Nano Banana Pro](https://docs.comfy.org/development/comfy-router/models/google/nano-banana-pro/code)
  * [FLUX 1.1 Pro Ultra](https://docs.comfy.org/development/comfy-router/models/black-forest-labs/flux-1-1-pro-ultra-image/code)
  * [FLUX Kontext](https://docs.comfy.org/development/comfy-router/models/black-forest-labs/flux-1-kontext/code)
  * [FLUX Video Upscale](https://docs.comfy.org/development/comfy-router/models/black-forest-labs/flux-video-upscale/code)
  * [FLUX 3 Video](https://docs.comfy.org/development/comfy-router/models/black-forest-labs/flux-3-video/code)
  * [Ideogram 4](https://docs.comfy.org/development/comfy-router/models/ideogram/ideogram-v4/code)



## 

​

Next

  * [Quickstart](https://docs.comfy.org/development/comfy-router/quickstart): installation, invocation, and saving the image.
  * [Models](https://docs.comfy.org/development/comfy-router/models): browse the catalog and inspect model-specific request examples.
  * [Headers](https://docs.comfy.org/development/comfy-router/headers): authentication, idempotency, request IDs, and retry pacing.
  * [API reference](https://docs.comfy.org/development/comfy-router/reference): endpoint parameters, schemas, and response codes.



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/api.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/api)

[Comfy Router quickstartPrevious](https://docs.comfy.org/development/comfy-router/quickstart)[Discover Comfy Router modelsNext](https://docs.comfy.org/development/comfy-router/discover-models)

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
