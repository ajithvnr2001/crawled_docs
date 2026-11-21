---
url: https://docs.comfy.org/catalog/models/bfl/flux-3-video/
title: FLUX 3 Video video generation and audio generation model (bfl/flux-3-video): where to run it and pricing - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-21T15:11:09.574461+00:00
---

# FLUX 3 Video video generation and audio generation model (bfl/flux-3-video): where to run it and pricing - ComfyUI

> Source: https://docs.comfy.org/catalog/models/bfl/flux-3-video/

## On this page

Back to top

  * Where you can run it
  * Call it with Comfy Router
  * Workflow templates
  * Nodes
  * Pricing



Catalog

# FLUX 3 Video video generation and audio generation model (bfl/flux-3-video): where to run it and pricing

Copy pageCopy page

FLUX 3 Video is a video generation and audio generation model from Black Forest Labs. Run it with Comfy Router and Comfy Cloud; templates, files, nodes…

Copy pageCopy page

Model ID: bfl/flux-3-video Provider: bfl Product: router, cloud, workflows, nodes Input: text, image Output: video, audio License: closed FLUX 3 Video is a video generation and audio generation model from Black Forest Labs. It takes text and image as input and produces video and audio. It has no open weights. It runs on Black Forest Labs’s servers, so you use it through Comfy Router and Partner Nodes in ComfyUI and Comfy Cloud.

## Where you can run it

Where| Page| Use it when  
---|---|---  
Comfy Router (API)| [FLUX 3 Video with Comfy Router](https://docs.comfy.org/development/comfy-router/models/black-forest-labs/flux-3-video/code)| You call `bfl/flux-3-video` from your own code with `COMFY_API_KEY`  
Partner Nodes (ComfyUI and Comfy Cloud)| [FLUX 3 Max in ComfyUI: Keyframed Video with Native Audio](https://docs.comfy.org/tutorials/partner-nodes/black-forest-labs/flux-3-max)| You build a workflow with the hosted model  
Partner Nodes (ComfyUI and Comfy Cloud)| [FLUX 3 Video - AI video generation with native audio](https://docs.comfy.org/tutorials/partner-nodes/black-forest-labs/flux-3-video)| You build a workflow with the hosted model  
Comfy Cloud| [Open `api_bfl_flux3_i2v` on Comfy Cloud](https://cloud.comfy.org/?template=api_bfl_flux3_i2v)| You want to run a ready-made workflow without installing anything  
  
## Call it with Comfy Router

  * `POST https://api.comfy.org/v2/models/bfl/flux-3-video`. Live request schema: `GET /v2/models/bfl/flux-3-video/openapi.json`.



## Workflow templates

Template| Title| Added  
---|---|---  
`api_flux3_max_t2v`| FLUX 3 Max: Text to Video| 2026-10-20  
`api_flux3_max_i2v`| FLUX 3 Max: Image to Video| 2026-10-19  
`api_bfl_flux3_i2v`| FLUX 3 Video: Image to Video| 2026-08-04  
`api_bfl_flux3_t2v`| FLUX 3 Video: Text to Video| 2026-08-04  
  
## Nodes

  * [Flux3ImageToVideoNode](https://docs.comfy.org/built-in-nodes/Flux3ImageToVideoNode)
  * [Flux3MaxImageToVideoNode](https://docs.comfy.org/built-in-nodes/Flux3MaxImageToVideoNode)
  * [Flux3MaxTextToVideoNode](https://docs.comfy.org/built-in-nodes/Flux3MaxTextToVideoNode)
  * [Flux3TextToVideoNode](https://docs.comfy.org/built-in-nodes/Flux3TextToVideoNode)



## Pricing

Comfy Router charges the model maker’s list price, billed from your workspace credits (211 credits = $1 USD). Current per-model prices are on [router.comfy.org](https://router.comfy.org).

  * Price a call before you run it: `POST https://api.comfy.org/v2/models/bfl/flux-3-video/estimate`.
  * Billing facts, such as whether a refused request is charged: the `billing` field from `GET https://api.comfy.org/v2/models/bfl/flux-3-video`.

See [Comfy Router pricing](https://docs.comfy.org/development/comfy-router/pricing) and [Billing](https://docs.comfy.org/development/comfy-router/billing#model-billing-facts).

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/catalog/models/bfl/flux-3-video.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/catalog/models/bfl/flux-3-video)
