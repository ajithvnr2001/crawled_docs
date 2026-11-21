---
url: https://docs.comfy.org/catalog/models/wan/wan2-6-r2v/
title: Wan 2.6 R2V video generation and audio generation model (wan/wan2.6-r2v): where to run it and pricing - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-21T15:11:26.291185+00:00
---

# Wan 2.6 R2V video generation and audio generation model (wan/wan2.6-r2v): where to run it and pricing - ComfyUI

> Source: https://docs.comfy.org/catalog/models/wan/wan2-6-r2v/

## On this page

Back to top

  * Where you can run it
  * Call it with Comfy Router
  * Workflow templates
  * Pricing



Catalog

# Wan 2.6 R2V video generation and audio generation model (wan/wan2.6-r2v): where to run it and pricing

Copy pageCopy page

Wan 2.6 R2V is a video generation and audio generation model from Wan. Run it with Comfy Router and Comfy Cloud; templates, files, nodes, and pricing.

Copy pageCopy page

Model ID: wan/wan2.6-r2v Provider: wan Product: router, cloud, workflows Input: image, video, text Output: video, audio License: closed Wan 2.6 R2V is a video generation and audio generation model from Wan. It takes image, video and text as input and produces video and audio. It has no open weights. It runs on Wan’s servers, so you use it through Comfy Router and Partner Nodes in ComfyUI and Comfy Cloud.

## Where you can run it

Where| Page| Use it when  
---|---|---  
Comfy Router (API)| [Wan 2.6 R2V with Comfy Router](https://docs.comfy.org/development/comfy-router/models/wan/wan2-6-r2v/code)| You call `wan/wan2.6-r2v` from your own code with `COMFY_API_KEY`  
  
## Call it with Comfy Router

  * `POST https://api.comfy.org/v2/models/wan/wan2.6-r2v`. Live request schema: `GET /v2/models/wan/wan2.6-r2v/openapi.json`.



## Workflow templates

Template| Title| Added  
---|---|---  
`api_wan_r2v`| WAN2.6: Reference to Video| 2026-01-03  
`api_wan2_6_i2v`| Wan2.6: Image to Video| 2025-12-20  
`api_wan2_6_t2v`| Wan2.6: Text to Video| 2025-12-20  
  
## Pricing

Comfy Router charges the model maker’s list price, billed from your workspace credits (211 credits = $1 USD). Current per-model prices are on [router.comfy.org](https://router.comfy.org).

  * Price a call before you run it: `POST https://api.comfy.org/v2/models/wan/wan2.6-r2v/estimate`.
  * Billing facts, such as whether a refused request is charged: the `billing` field from `GET https://api.comfy.org/v2/models/wan/wan2.6-r2v`.

See [Comfy Router pricing](https://docs.comfy.org/development/comfy-router/pricing) and [Billing](https://docs.comfy.org/development/comfy-router/billing#model-billing-facts).

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/catalog/models/wan/wan2-6-r2v.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/catalog/models/wan/wan2-6-r2v)
