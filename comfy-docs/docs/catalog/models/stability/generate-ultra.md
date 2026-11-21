---
url: https://docs.comfy.org/catalog/models/stability/generate-ultra/
title: Generate Ultra image generation model (stability/generate-ultra): where to run it and pricing - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-21T15:11:23.142716+00:00
---

# Generate Ultra image generation model (stability/generate-ultra): where to run it and pricing - ComfyUI

> Source: https://docs.comfy.org/catalog/models/stability/generate-ultra/

## On this page

Back to top

  * Where you can run it
  * Call it with Comfy Router
  * Pricing



Catalog

# Generate Ultra image generation model (stability/generate-ultra): where to run it and pricing

Copy pageCopy page

Generate Ultra is a image generation model from Stability AI. Run it with Comfy Router; templates, files, nodes, and pricing.

Copy pageCopy page

Model ID: stability/generate-ultra Provider: stability Product: router Input: text, image Output: image License: closed Generate Ultra is a image generation model from Stability AI. It takes text and image as input and produces image. It has no open weights. It runs on Stability AI’s servers, so you use it through Comfy Router.

## Where you can run it

Where| Page| Use it when  
---|---|---  
Comfy Router (API)| [Generate Ultra with Comfy Router](https://docs.comfy.org/development/comfy-router/models/stability/generate-ultra/code)| You call `stability/generate-ultra` from your own code with `COMFY_API_KEY`  
  
## Call it with Comfy Router

  * `POST https://api.comfy.org/v2/models/stability/generate-ultra`. Live request schema: `GET /v2/models/stability/generate-ultra/openapi.json`.



## Pricing

Comfy Router charges the model maker’s list price, billed from your workspace credits (211 credits = $1 USD). Current per-model prices are on [router.comfy.org](https://router.comfy.org).

  * Price a call before you run it: `POST https://api.comfy.org/v2/models/stability/generate-ultra/estimate`.
  * Billing facts, such as whether a refused request is charged: the `billing` field from `GET https://api.comfy.org/v2/models/stability/generate-ultra`.

See [Comfy Router pricing](https://docs.comfy.org/development/comfy-router/pricing) and [Billing](https://docs.comfy.org/development/comfy-router/billing#model-billing-facts).

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/catalog/models/stability/generate-ultra.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/catalog/models/stability/generate-ultra)
