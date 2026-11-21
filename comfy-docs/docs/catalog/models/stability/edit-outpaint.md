---
url: https://docs.comfy.org/catalog/models/stability/edit-outpaint/
title: Edit Outpaint image generation model (stability/edit-outpaint): where to run it and pricing - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-21T15:11:22.702430+00:00
---

# Edit Outpaint image generation model (stability/edit-outpaint): where to run it and pricing - ComfyUI

> Source: https://docs.comfy.org/catalog/models/stability/edit-outpaint/

## On this page

Back to top

  * Where you can run it
  * Call it with Comfy Router
  * Pricing



Catalog

# Edit Outpaint image generation model (stability/edit-outpaint): where to run it and pricing

Copy pageCopy page

Edit Outpaint is a image generation model from Stability AI. Run it with Comfy Router; templates, files, nodes, and pricing.

Copy pageCopy page

Model ID: stability/edit-outpaint Provider: stability Product: router Input: text, image Output: image License: closed Edit Outpaint is a image generation model from Stability AI. It takes text and image as input and produces image. It has no open weights. It runs on Stability AI’s servers, so you use it through Comfy Router.

## Where you can run it

Where| Page| Use it when  
---|---|---  
Comfy Router (API)| [Edit Outpaint with Comfy Router](https://docs.comfy.org/development/comfy-router/models/stability/edit-outpaint/code)| You call `stability/edit-outpaint` from your own code with `COMFY_API_KEY`  
  
## Call it with Comfy Router

  * `POST https://api.comfy.org/v2/models/stability/edit-outpaint`. Live request schema: `GET /v2/models/stability/edit-outpaint/openapi.json`.



## Pricing

Comfy Router charges the model maker’s list price, billed from your workspace credits (211 credits = $1 USD). Current per-model prices are on [router.comfy.org](https://router.comfy.org).

  * Price a call before you run it: `POST https://api.comfy.org/v2/models/stability/edit-outpaint/estimate`.
  * Billing facts, such as whether a refused request is charged: the `billing` field from `GET https://api.comfy.org/v2/models/stability/edit-outpaint`.

See [Comfy Router pricing](https://docs.comfy.org/development/comfy-router/pricing) and [Billing](https://docs.comfy.org/development/comfy-router/billing#model-billing-facts).

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/catalog/models/stability/edit-outpaint.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/catalog/models/stability/edit-outpaint)
