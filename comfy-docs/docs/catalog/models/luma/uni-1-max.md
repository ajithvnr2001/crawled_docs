---
url: https://docs.comfy.org/catalog/models/luma/uni-1-max/
title: Uni 1 Max image generation model (luma_2/uni-1-max): where to run it and pricing - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-21T15:11:17.154021+00:00
---

# Uni 1 Max image generation model (luma_2/uni-1-max): where to run it and pricing - ComfyUI

> Source: https://docs.comfy.org/catalog/models/luma/uni-1-max/

## On this page

Back to top

  * Where you can run it
  * Call it with Comfy Router
  * Workflow templates
  * Pricing



Catalog

# Uni 1 Max image generation model (luma_2/uni-1-max): where to run it and pricing

Copy pageCopy page

Uni 1 Max is a image generation model from Luma. Run it with Comfy Router and Comfy Cloud; templates, files, nodes, and pricing.

Copy pageCopy page

Model ID: luma_2/uni-1-max Provider: luma Product: router, cloud, workflows Input: text, image Output: image License: closed Uni 1 Max is a image generation model from Luma. It takes text and image as input and produces image. It has no open weights. It runs on Luma’s servers, so you use it through Comfy Router and Partner Nodes in ComfyUI and Comfy Cloud.

## Where you can run it

Where| Page| Use it when  
---|---|---  
Comfy Router (API)| [Uni 1 Max with Comfy Router](https://docs.comfy.org/development/comfy-router/models/luma_2/uni-1-max/code)| You call `luma_2/uni-1-max` from your own code with `COMFY_API_KEY`  
  
## Call it with Comfy Router

  * `POST https://api.comfy.org/v2/models/luma_2/uni-1-max`. Live request schema: `GET /v2/models/luma_2/uni-1-max/openapi.json`.



## Workflow templates

Template| Title| Added  
---|---|---  
`api_luma_uni_1_image_create`| Luma UNI-1: Image Creation| 2026-05-05  
`api_luma_uni_1_image_edit`| Luma UNI-1: Image Edit| 2026-05-05  
  
## Pricing

Comfy Router charges the model maker’s list price, billed from your workspace credits (211 credits = $1 USD). Current per-model prices are on [router.comfy.org](https://router.comfy.org).

  * Price a call before you run it: `POST https://api.comfy.org/v2/models/luma_2/uni-1-max/estimate`.
  * Billing facts, such as whether a refused request is charged: the `billing` field from `GET https://api.comfy.org/v2/models/luma_2/uni-1-max`.

See [Comfy Router pricing](https://docs.comfy.org/development/comfy-router/pricing) and [Billing](https://docs.comfy.org/development/comfy-router/billing#model-billing-facts).

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/catalog/models/luma/uni-1-max.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/catalog/models/luma/uni-1-max)
