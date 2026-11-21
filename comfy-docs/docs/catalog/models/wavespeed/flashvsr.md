---
url: https://docs.comfy.org/catalog/models/wavespeed/flashvsr/
title: Flashvsr video generation model (wavespeed/flashvsr): where to run it and pricing - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-21T15:11:26.814513+00:00
---

# Flashvsr video generation model (wavespeed/flashvsr): where to run it and pricing - ComfyUI

> Source: https://docs.comfy.org/catalog/models/wavespeed/flashvsr/

## On this page

Back to top

  * Where you can run it
  * Call it with Comfy Router
  * Workflow templates
  * Nodes
  * Pricing



Catalog

# Flashvsr video generation model (wavespeed/flashvsr): where to run it and pricing

Copy pageCopy page

Flashvsr is a video generation model from WaveSpeed. Run it with Comfy Router and Comfy Cloud; templates, files, nodes, and pricing.

Copy pageCopy page

Model ID: wavespeed/flashvsr Provider: wavespeed Product: router, cloud, workflows, nodes Input: video Output: video License: closed Flashvsr is a video generation model from WaveSpeed. It takes video as input and produces video. It has no open weights. It runs on WaveSpeed’s servers, so you use it through Comfy Router and Partner Nodes in ComfyUI and Comfy Cloud.

## Where you can run it

Where| Page| Use it when  
---|---|---  
Comfy Router (API)| [Flashvsr with Comfy Router](https://docs.comfy.org/development/comfy-router/models/wavespeed/flashvsr/code)| You call `wavespeed/flashvsr` from your own code with `COMFY_API_KEY`  
Partner Nodes (ComfyUI and Comfy Cloud)| [WaveSpeed FlashVSR](https://docs.comfy.org/tutorials/partner-nodes/wavespeed/wavespeed-flashvsr)| You build a workflow with the hosted model  
Comfy Cloud| [Open `api_wavespeed_flshvsr_video_upscale` on Comfy Cloud](https://cloud.comfy.org/?template=api_wavespeed_flshvsr_video_upscale)| You want to run a ready-made workflow without installing anything  
  
## Call it with Comfy Router

  * `POST https://api.comfy.org/v2/models/wavespeed/flashvsr`. Live request schema: `GET /v2/models/wavespeed/flashvsr/openapi.json`.



## Workflow templates

Template| Title| Added  
---|---|---  
`api_wavespeed_flshvsr_video_upscale`| Video Upscale: WaveSpeed FlashVSR| 2026-01-23  
  
## Nodes

  * [WavespeedFlashVSRNode](https://docs.comfy.org/built-in-nodes/WavespeedFlashVSRNode)



## Pricing

Comfy Router charges the model maker’s list price, billed from your workspace credits (211 credits = $1 USD). Current per-model prices are on [router.comfy.org](https://router.comfy.org).

  * Price a call before you run it: `POST https://api.comfy.org/v2/models/wavespeed/flashvsr/estimate`.
  * Billing facts, such as whether a refused request is charged: the `billing` field from `GET https://api.comfy.org/v2/models/wavespeed/flashvsr`.

See [Comfy Router pricing](https://docs.comfy.org/development/comfy-router/pricing) and [Billing](https://docs.comfy.org/development/comfy-router/billing#model-billing-facts).

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/catalog/models/wavespeed/flashvsr.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/catalog/models/wavespeed/flashvsr)
