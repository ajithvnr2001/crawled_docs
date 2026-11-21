---
url: https://docs.comfy.org/catalog/models/bfl/flux-2-max/
title: FLUX 2 Max image generation model (bfl/flux-2-max): where to run it and pricing - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-21T15:11:09.083476+00:00
---

# FLUX 2 Max image generation model (bfl/flux-2-max): where to run it and pricing - ComfyUI

> Source: https://docs.comfy.org/catalog/models/bfl/flux-2-max/

## On this page

Back to top

  * Where you can run it
  * Call it with Comfy Router
  * Workflow templates
  * Pricing



Catalog

# FLUX 2 Max image generation model (bfl/flux-2-max): where to run it and pricing

Copy pageCopy page

FLUX 2 Max is a image generation model from Black Forest Labs. Run it with Comfy Router and Comfy Cloud; templates, files, nodes, and pricing.

Copy pageCopy page

Model ID: bfl/flux-2-max Provider: bfl Product: router, cloud, workflows Input: text, image Output: image License: closed FLUX 2 Max is a image generation model from Black Forest Labs. It takes text and image as input and produces image. It has no open weights. It runs on Black Forest Labs’s servers, so you use it through Comfy Router and Partner Nodes in ComfyUI and Comfy Cloud.

## Where you can run it

Where| Page| Use it when  
---|---|---  
Comfy Router (API)| [FLUX 2 Max with Comfy Router](https://docs.comfy.org/development/comfy-router/models/black-forest-labs/flux-2-max/code)| You call `bfl/flux-2-max` from your own code with `COMFY_API_KEY`  
  
## Call it with Comfy Router

  * `POST https://api.comfy.org/v2/models/bfl/flux-2-max`. Live request schema: `GET /v2/models/bfl/flux-2-max/openapi.json`.



## Workflow templates

Template| Title| Added  
---|---|---  
`api_bfl_flux2_max_sofa_swap`| FLUX.2 [max]: Object Swap| 2025-12-22  
`api_flux2`| FLUX.2 Pro| 2025-11-26  
  
## Pricing

Comfy Router charges the model maker’s list price, billed from your workspace credits (211 credits = $1 USD). Current per-model prices are on [router.comfy.org](https://router.comfy.org).

  * Price a call before you run it: `POST https://api.comfy.org/v2/models/bfl/flux-2-max/estimate`.
  * Billing facts, such as whether a refused request is charged: the `billing` field from `GET https://api.comfy.org/v2/models/bfl/flux-2-max`.

See [Comfy Router pricing](https://docs.comfy.org/development/comfy-router/pricing) and [Billing](https://docs.comfy.org/development/comfy-router/billing#model-billing-facts).

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/catalog/models/bfl/flux-2-max.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/catalog/models/bfl/flux-2-max)
