---
url: https://docs.comfy.org/catalog/models/bria/fibo/
title: Fibo image generation model (bria/fibo): where to run it and pricing - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-21T15:11:09.777455+00:00
---

# Fibo image generation model (bria/fibo): where to run it and pricing - ComfyUI

> Source: https://docs.comfy.org/catalog/models/bria/fibo/

## On this page

Back to top

  * Where you can run it
  * Call it with Comfy Router
  * Model files for running it locally
  * Workflow templates
  * Nodes
  * Pricing



Catalog

# Fibo image generation model (bria/fibo): where to run it and pricing

Copy pageCopy page

Fibo is a image generation model from Bria. Run it with Comfy Router, ComfyUI locally and Comfy Cloud; templates, files, nodes, and pricing.

Copy pageCopy page

Model ID: bria/fibo Provider: bria Product: router, local, cloud, workflows, nodes Input: image, text Output: image License: open-weights Fibo is a image generation model from Bria. It takes image and text as input and produces image. It has open weights, so you can download the files and run it locally in ComfyUI, or call the hosted version through Comfy Router.

## Where you can run it

Where| Page| Use it when  
---|---|---  
Comfy Router (API)| [Fibo with Comfy Router](https://docs.comfy.org/development/comfy-router/models/bria/fibo/code)| You call `bria/fibo` from your own code with `COMFY_API_KEY`  
ComfyUI (local or Comfy Cloud)| [Bria FIBO 2.0 Open Weights in ComfyUI: Image Edit](https://docs.comfy.org/tutorials/image/bria/fibo-2-0)| You follow a step-by-step workflow tutorial  
Comfy Cloud| [Open `image_fibo2_edit_turbo_pe` on Comfy Cloud](https://cloud.comfy.org/?template=image_fibo2_edit_turbo_pe)| You want to run a ready-made workflow without installing anything  
  
## Call it with Comfy Router

  * `POST https://api.comfy.org/v2/models/bria/fibo`. Live request schema: `GET /v2/models/bria/fibo/openapi.json`.



## Model files for running it locally

Put each file in the matching folder under `ComfyUI/models/`. These come from the workflow templates below (workflow_templates at `3c2199b9`).

File| Folder| Download  
---|---|---  
`fibo2_edit_turbo_int8_convrot.safetensors`| `models/diffusion_models/`| [Download](https://huggingface.co/Comfy-Org/Fibo-2.0/resolve/main/diffusion_models/fibo2_edit_turbo_int8_convrot.safetensors)  
`fibo2_dev_int8_convrot.safetensors`| `models/diffusion_models/`| [Download](https://huggingface.co/Comfy-Org/Fibo-2.0/resolve/main/diffusion_models/fibo2_dev_int8_convrot.safetensors)  
`qwen3vl_4b_bf16.safetensors`| `models/text_encoders/`| [Download](https://huggingface.co/Comfy-Org/Fibo-2.0/resolve/main/text_encoders/qwen3vl_4b_bf16.safetensors)  
`qwen3vl_8b_int8_convrot.safetensors`| `models/text_encoders/`| [Download](https://huggingface.co/Comfy-Org/Qwen3-VL/resolve/main/text_encoders/qwen3vl_8b_int8_convrot.safetensors)  
`flux2-vae.safetensors`| `models/vae/`| [Download](https://huggingface.co/Comfy-Org/Fibo-2.0/resolve/main/vae/flux2-vae.safetensors)  
  
## Workflow templates

Template| Title| Added  
---|---|---  
`image_fibo2_edit_turbo_pe`| Fibo 2.0 Turbo: Image Edit| 2026-10-26  
`image_fibo2_edit_dev_pe`| Fibo 2.0 Dev: Image Edit| 2026-10-26  
  
## Nodes

  * [TextEncodeFibo2](https://docs.comfy.org/built-in-nodes/TextEncodeFibo2)



## Pricing

Comfy Router charges the model maker’s list price, billed from your workspace credits (211 credits = $1 USD). Current per-model prices are on [router.comfy.org](https://router.comfy.org).

  * Price a call before you run it: `POST https://api.comfy.org/v2/models/bria/fibo/estimate`.
  * Billing facts, such as whether a refused request is charged: the `billing` field from `GET https://api.comfy.org/v2/models/bria/fibo`.

See [Comfy Router pricing](https://docs.comfy.org/development/comfy-router/pricing) and [Billing](https://docs.comfy.org/development/comfy-router/billing#model-billing-facts).

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/catalog/models/bria/fibo.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/catalog/models/bria/fibo)
