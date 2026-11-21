---
url: https://docs.comfy.org/catalog/models/stability/control-style/
title: Control Style image generation model (stability/control-style): where to run it and pricing - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-21T15:11:22.509441+00:00
---

# Control Style image generation model (stability/control-style): where to run it and pricing - ComfyUI

> Source: https://docs.comfy.org/catalog/models/stability/control-style/

## On this page

Back to top

  * Where you can run it
  * Call it with Comfy Router
  * Pricing



Catalog

# Control Style image generation model (stability/control-style): where to run it and pricing

Copy pageCopy page

Control Style is a image generation model from Stability AI. Run it with Comfy Router; templates, files, nodes, and pricing.

Copy pageCopy page

Model ID: stability/control-style Provider: stability Product: router Input: text, image Output: image License: closed Control Style is a image generation model from Stability AI. It takes text and image as input and produces image. It has no open weights. It runs on Stability AI’s servers, so you use it through Comfy Router.

## Where you can run it

Where| Page| Use it when  
---|---|---  
Comfy Router (API)| [Control Style with Comfy Router](https://docs.comfy.org/development/comfy-router/models/stability/control-style/code)| You call `stability/control-style` from your own code with `COMFY_API_KEY`  
  
## Call it with Comfy Router

  * `POST https://api.comfy.org/v2/models/stability/control-style`. Live request schema: `GET /v2/models/stability/control-style/openapi.json`.



## Pricing

Comfy Router charges the model maker’s list price, billed from your workspace credits (211 credits = $1 USD). Current per-model prices are on [router.comfy.org](https://router.comfy.org).

  * Price a call before you run it: `POST https://api.comfy.org/v2/models/stability/control-style/estimate`.
  * Billing facts, such as whether a refused request is charged: the `billing` field from `GET https://api.comfy.org/v2/models/stability/control-style`.

See [Comfy Router pricing](https://docs.comfy.org/development/comfy-router/pricing) and [Billing](https://docs.comfy.org/development/comfy-router/billing#model-billing-facts).

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/catalog/models/stability/control-style.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/catalog/models/stability/control-style)
