---
url: https://docs.comfy.org/catalog/models/kling/kling-4-0/
title: Kling 4.0 video generation model (kling/kling-4.0): where to run it and pricing - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-21T15:11:15.260235+00:00
---

# Kling 4.0 video generation model (kling/kling-4.0): where to run it and pricing - ComfyUI

> Source: https://docs.comfy.org/catalog/models/kling/kling-4-0/

## On this page

Back to top

  * Where you can run it
  * Call it with Comfy Router
  * Workflow templates
  * Nodes
  * Pricing



Catalog

# Kling 4.0 video generation model (kling/kling-4.0): where to run it and pricing

Copy pageCopy page

Kling 4.0 is a video generation model from Kling. Run it with Comfy Router and Comfy Cloud; templates, files, nodes, and pricing.

Copy pageCopy page

Model ID: kling/kling-4.0 Provider: kling Product: router, cloud, workflows, nodes Input: text, image, video Output: video License: closed Kling 4.0 is a video generation model from Kling. It takes text, image and video as input and produces video. It has no open weights. It runs on Kling’s servers, so you use it through Comfy Router and Partner Nodes in ComfyUI and Comfy Cloud.

## Where you can run it

Where| Page| Use it when  
---|---|---  
Comfy Router (API)| [Kling 4.0 with Comfy Router](https://docs.comfy.org/development/comfy-router/models/kling/kling-4-0/code)| You call `kling/kling-4.0` from your own code with `COMFY_API_KEY`  
Partner Nodes (ComfyUI and Comfy Cloud)| [Kling 4.0 in ComfyUI: Text, Image, Reference, and Edit Workflows](https://docs.comfy.org/tutorials/partner-nodes/kling/kling-4-0)| You build a workflow with the hosted model  
Comfy Cloud| [Open `api_kling4_i2v` on Comfy Cloud](https://cloud.comfy.org/?template=api_kling4_i2v)| You want to run a ready-made workflow without installing anything  
  
## Call it with Comfy Router

  * `POST https://api.comfy.org/v2/models/kling/kling-4.0`. Live request schema: `GET /v2/models/kling/kling-4.0/openapi.json`.



## Workflow templates

Template| Title| Added  
---|---|---  
`api_kling4_i2v`| Kling 4.0: Image to Video| 2026-10-27  
`api_kling4_t2v`| Kling 4.0: Text to Video| 2026-10-27  
`api_kling4_video_edit`| Kling 4.0: Video Edit| 2026-10-27  
`api_kling4_r2v`| Kling 4.0: Reference to Video| 2026-10-27  
  
## Nodes

  * [Kling4EditVideoNode](https://docs.comfy.org/built-in-nodes/Kling4EditVideoNode)
  * [Kling4ImageToVideoNode](https://docs.comfy.org/built-in-nodes/Kling4ImageToVideoNode)
  * [Kling4ReferenceToVideoNode](https://docs.comfy.org/built-in-nodes/Kling4ReferenceToVideoNode)
  * [Kling4TextToVideoNode](https://docs.comfy.org/built-in-nodes/Kling4TextToVideoNode)



## Pricing

Comfy Router charges the model maker’s list price, billed from your workspace credits (211 credits = $1 USD). Current per-model prices are on [router.comfy.org](https://router.comfy.org).

  * Price a call before you run it: `POST https://api.comfy.org/v2/models/kling/kling-4.0/estimate`.
  * Billing facts, such as whether a refused request is charged: the `billing` field from `GET https://api.comfy.org/v2/models/kling/kling-4.0`.

See [Comfy Router pricing](https://docs.comfy.org/development/comfy-router/pricing) and [Billing](https://docs.comfy.org/development/comfy-router/billing#model-billing-facts).

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/catalog/models/kling/kling-4-0.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/catalog/models/kling/kling-4-0)
