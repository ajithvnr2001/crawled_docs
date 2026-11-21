---
url: https://docs.comfy.org/catalog/models/baidu/ernie-image/
title: ERNIE-Image image generation model (baidu/ernie-image): where to run it - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-21T15:11:08.552473+00:00
---

# ERNIE-Image image generation model (baidu/ernie-image): where to run it - ComfyUI

> Source: https://docs.comfy.org/catalog/models/baidu/ernie-image/

## On this page

Back to top

  * Where you can run it
  * Model files for running it locally
  * Workflow templates



Catalog

# ERNIE-Image image generation model (baidu/ernie-image): where to run it

Copy pageCopy page

ERNIE-Image is a image generation model from Baidu. Run it with ComfyUI locally and Comfy Cloud; templates, files, nodes, and pricing.

Copy pageCopy page

Model ID: baidu/ernie-image Provider: baidu Product: local, cloud, workflows Input: text Output: image License: open-weights ERNIE-Image is a image generation model from Baidu. It takes text as input and produces image. It has open weights, so you can download the files and run it locally in ComfyUI.

## Where you can run it

Where| Page| Use it when  
---|---|---  
ComfyUI (local or Comfy Cloud)| [ERNIE-Image ComfyUI workflow example](https://docs.comfy.org/tutorials/image/ernie-image/ernie-image)| You follow a step-by-step workflow tutorial  
Comfy Cloud| [Open `image_ernie_image` on Comfy Cloud](https://cloud.comfy.org/?template=image_ernie_image)| You want to run a ready-made workflow without installing anything  
  
## Model files for running it locally

Put each file in the matching folder under `ComfyUI/models/`. These come from the workflow templates below (workflow_templates at `3c2199b9`).

File| Folder| Download  
---|---|---  
`ernie-image-turbo.safetensors`| `models/diffusion_models/`| [Download](https://huggingface.co/Comfy-Org/ERNIE-Image/resolve/main/diffusion_models/ernie-image-turbo.safetensors)  
`ernie-image.safetensors`| `models/diffusion_models/`| [Download](https://huggingface.co/Comfy-Org/ERNIE-Image/resolve/main/diffusion_models/ernie-image.safetensors)  
`ernie-image-prompt-enhancer.safetensors`| `models/text_encoders/`| [Download](https://huggingface.co/Comfy-Org/ERNIE-Image/resolve/main/text_encoders/ernie-image-prompt-enhancer.safetensors)  
`ministral-3-3b.safetensors`| `models/text_encoders/`| [Download](https://huggingface.co/Comfy-Org/ERNIE-Image/resolve/main/text_encoders/ministral-3-3b.safetensors)  
`flux2-vae.safetensors`| `models/vae/`| [Download](https://huggingface.co/Comfy-Org/ERNIE-Image/resolve/main/vae/flux2-vae.safetensors)  
  
## Workflow templates

Template| Title| Added  
---|---|---  
`image_ernie_image_turbo`| Ernie Image Turbo: Text To Image| 2026-04-14  
`image_ernie_image`| Ernie Image: Text to Image| 2026-04-14  
  
Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/catalog/models/baidu/ernie-image.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/catalog/models/baidu/ernie-image)
