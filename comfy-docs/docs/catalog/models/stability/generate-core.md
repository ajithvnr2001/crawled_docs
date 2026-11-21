---
url: https://docs.comfy.org/catalog/models/stability/generate-core/
title: Generate Core image generation model (stability/generate-core): where to run it and pricing - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-21T15:11:22.891871+00:00
---

# Generate Core image generation model (stability/generate-core): where to run it and pricing - ComfyUI

> Source: https://docs.comfy.org/catalog/models/stability/generate-core/

## On this page

Back to top

  * Where you can run it
  * Call it with Comfy Router
  * Pricing



Catalog

# Generate Core image generation model (stability/generate-core): where to run it and pricing

Copy pageCopy page

Generate Core is a image generation model from Stability AI. Run it with Comfy Router; templates, files, nodes, and pricing.

Copy pageCopy page

Model ID: stability/generate-core Provider: stability Product: router Input: text Output: image License: closed Generate Core is a image generation model from Stability AI. It takes text as input and produces image. It has no open weights. It runs on Stability AI’s servers, so you use it through Comfy Router.

## Where you can run it

Where| Page| Use it when  
---|---|---  
Comfy Router (API)| [Generate Core with Comfy Router](https://docs.comfy.org/development/comfy-router/models/stability/generate-core/code)| You call `stability/generate-core` from your own code with `COMFY_API_KEY`  
  
## Call it with Comfy Router

  * `POST https://api.comfy.org/v2/models/stability/generate-core`. Live request schema: `GET /v2/models/stability/generate-core/openapi.json`.



## Pricing

Comfy Router charges the model maker’s list price, billed from your workspace credits (211 credits = $1 USD). Current per-model prices are on [router.comfy.org](https://router.comfy.org).

  * Price a call before you run it: `POST https://api.comfy.org/v2/models/stability/generate-core/estimate`.
  * Billing facts, such as whether a refused request is charged: the `billing` field from `GET https://api.comfy.org/v2/models/stability/generate-core`.

See [Comfy Router pricing](https://docs.comfy.org/development/comfy-router/pricing) and [Billing](https://docs.comfy.org/development/comfy-router/billing#model-billing-facts).

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/catalog/models/stability/generate-core.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/catalog/models/stability/generate-core)
