---
url: https://docs.comfy.org/catalog/models/runway/gen4-image/
title: Gen 4 Image image generation model (runway/gen4_image): where to run it and pricing - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-21T15:11:22.319058+00:00
---

# Gen 4 Image image generation model (runway/gen4_image): where to run it and pricing - ComfyUI

> Source: https://docs.comfy.org/catalog/models/runway/gen4-image/

## On this page

Back to top

  * Where you can run it
  * Call it with Comfy Router
  * Pricing



Catalog

# Gen 4 Image image generation model (runway/gen4_image): where to run it and pricing

Copy pageCopy page

Gen 4 Image is a image generation model from Runway. Run it with Comfy Router; templates, files, nodes, and pricing.

Copy pageCopy page

Model ID: runway/gen4_image Provider: runway Product: router Input: text, image Output: image License: closed Gen 4 Image is a image generation model from Runway. It takes text and image as input and produces image. It has no open weights. It runs on Runway’s servers, so you use it through Comfy Router.

## Where you can run it

Where| Page| Use it when  
---|---|---  
Comfy Router (API)| [Gen 4 Image with Comfy Router](https://docs.comfy.org/development/comfy-router/models/runway/gen4-image/code)| You call `runway/gen4_image` from your own code with `COMFY_API_KEY`  
  
## Call it with Comfy Router

  * `POST https://api.comfy.org/v2/models/runway/gen4_image`. Live request schema: `GET /v2/models/runway/gen4_image/openapi.json`.



## Pricing

Comfy Router charges the model maker’s list price, billed from your workspace credits (211 credits = $1 USD). Current per-model prices are on [router.comfy.org](https://router.comfy.org).

  * Price a call before you run it: `POST https://api.comfy.org/v2/models/runway/gen4_image/estimate`.
  * Billing facts, such as whether a refused request is charged: the `billing` field from `GET https://api.comfy.org/v2/models/runway/gen4_image`.

See [Comfy Router pricing](https://docs.comfy.org/development/comfy-router/pricing) and [Billing](https://docs.comfy.org/development/comfy-router/billing#model-billing-facts).

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/catalog/models/runway/gen4-image.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/catalog/models/runway/gen4-image)
