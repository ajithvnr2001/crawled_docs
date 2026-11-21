---
url: https://docs.comfy.org/catalog/models/bfl/flux-1-krea-dev/
title: FLUX.1 Krea image generation model (bfl/flux-1-krea-dev): where to run it - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-21T15:11:08.896734+00:00
---

# FLUX.1 Krea image generation model (bfl/flux-1-krea-dev): where to run it - ComfyUI

> Source: https://docs.comfy.org/catalog/models/bfl/flux-1-krea-dev/

## On this page

Back to top

  * Where you can run it
  * Model files for running it locally
  * Workflow templates



Catalog

# FLUX.1 Krea image generation model (bfl/flux-1-krea-dev): where to run it

Copy pageCopy page

FLUX.1 Krea is a image generation model from Black Forest Labs. Run it with ComfyUI locally and Comfy Cloud; templates, files, nodes, and pricing.

Copy pageCopy page

Model ID: bfl/flux-1-krea-dev Provider: bfl Product: local, cloud, workflows Input: text Output: image License: open-weights FLUX.1 Krea is a image generation model from Black Forest Labs. It takes text as input and produces image. It has open weights, so you can download the files and run it locally in ComfyUI.

## Where you can run it

Where| Page| Use it when  
---|---|---  
ComfyUI (local or Comfy Cloud)| [FLUX.1 Krea Dev ComfyUI Workflow Tutorial](https://docs.comfy.org/tutorials/flux/flux1-krea-dev)| You follow a step-by-step workflow tutorial  
Comfy Cloud| [Open `flux1_krea_dev` on Comfy Cloud](https://cloud.comfy.org/?template=flux1_krea_dev)| You want to run a ready-made workflow without installing anything  
  
## Model files for running it locally

Put each file in the matching folder under `ComfyUI/models/`. These come from the workflow templates below (workflow_templates at `3c2199b9`).

File| Folder| Download  
---|---|---  
`flux1-krea-dev_fp8_scaled.safetensors`| `models/diffusion_models/`| [Download](https://huggingface.co/Comfy-Org/FLUX.1-Krea-dev_ComfyUI/resolve/main/split_files/diffusion_models/flux1-krea-dev_fp8_scaled.safetensors)  
`clip_l.safetensors`| `models/text_encoders/`| [Download](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors)  
`t5xxl_fp16.safetensors`| `models/text_encoders/`| [Download](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp16.safetensors)  
`ae.safetensors`| `models/vae/`| [Download](https://huggingface.co/Comfy-Org/Lumina_Image_2.0_Repackaged/resolve/main/split_files/vae/ae.safetensors)  
  
## Workflow templates

Template| Title| Added  
---|---|---  
`flux1_krea_dev`| Flux.1 Krea Dev| 2025-07-31  
  
Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/catalog/models/bfl/flux-1-krea-dev.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/catalog/models/bfl/flux-1-krea-dev)
