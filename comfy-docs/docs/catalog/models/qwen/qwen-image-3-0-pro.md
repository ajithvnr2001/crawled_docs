---
url: https://docs.comfy.org/catalog/models/qwen/qwen-image-3-0-pro/
title: Qwen Image 3.0 Pro image generation model (qwen/qwen-image-3.0-pro): where to run it and pricing - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-21T15:11:20.689306+00:00
---

# Qwen Image 3.0 Pro image generation model (qwen/qwen-image-3.0-pro): where to run it and pricing - ComfyUI

> Source: https://docs.comfy.org/catalog/models/qwen/qwen-image-3-0-pro/

## On this page

Back to top

  * Where you can run it
  * Call it with Comfy Router
  * Workflow templates
  * Nodes
  * Pricing



Catalog

# Qwen Image 3.0 Pro image generation model (qwen/qwen-image-3.0-pro): where to run it and pricing

Copy pageCopy page

Qwen Image 3.0 Pro is a image generation model from Qwen. Run it with Comfy Router and Comfy Cloud; templates, files, nodes, and pricing.

Copy pageCopy page

Model ID: qwen/qwen-image-3.0-pro Provider: qwen Product: router, cloud, workflows, nodes Input: text, image Output: image License: closed Qwen Image 3.0 Pro is a image generation model from Qwen. It takes text and image as input and produces image. It has no open weights. It runs on Qwen’s servers, so you use it through Comfy Router and Partner Nodes in ComfyUI and Comfy Cloud.

## Where you can run it

Where| Page| Use it when  
---|---|---  
Comfy Router (API)| [Qwen Image 3.0 Pro with Comfy Router](https://docs.comfy.org/development/comfy-router/models/qwen/qwen-image-3-0-pro/code)| You call `qwen/qwen-image-3.0-pro` from your own code with `COMFY_API_KEY`  
Partner Nodes (ComfyUI and Comfy Cloud)| [Qwen Image 3.0 Pro - Advanced AI Image Generation](https://docs.comfy.org/tutorials/partner-nodes/qwen/qwen-image-3-0-pro)| You build a workflow with the hosted model  
Comfy Cloud| [Open `api_qwen3_image_edit` on Comfy Cloud](https://cloud.comfy.org/?template=api_qwen3_image_edit)| You want to run a ready-made workflow without installing anything  
  
## Call it with Comfy Router

  * `POST https://api.comfy.org/v2/models/qwen/qwen-image-3.0-pro`. Live request schema: `GET /v2/models/qwen/qwen-image-3.0-pro/openapi.json`.



## Workflow templates

Template| Title| Added  
---|---|---  
`api_qwen3_image_edit`| Qwen Image 3.0 Pro: Image Edit| 2026-08-06  
`api_qwen3_t2i`| Qwen Image 3.0 Pro: Text to Image| 2026-08-06  
  
## Nodes

  * [QwenImageEditApi](https://docs.comfy.org/built-in-nodes/QwenImageEditApi)
  * [QwenImageTextToImageApi](https://docs.comfy.org/built-in-nodes/QwenImageTextToImageApi)



## Pricing

Comfy Router charges the model maker’s list price, billed from your workspace credits (211 credits = $1 USD). Current per-model prices are on [router.comfy.org](https://router.comfy.org).

  * Price a call before you run it: `POST https://api.comfy.org/v2/models/qwen/qwen-image-3.0-pro/estimate`.
  * Billing facts, such as whether a refused request is charged: the `billing` field from `GET https://api.comfy.org/v2/models/qwen/qwen-image-3.0-pro`.

See [Comfy Router pricing](https://docs.comfy.org/development/comfy-router/pricing) and [Billing](https://docs.comfy.org/development/comfy-router/billing#model-billing-facts).

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/catalog/models/qwen/qwen-image-3-0-pro.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/catalog/models/qwen/qwen-image-3-0-pro)
