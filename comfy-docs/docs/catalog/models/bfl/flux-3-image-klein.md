---
url: https://docs.comfy.org/catalog/models/bfl/flux-3-image-klein/
title: FLUX 3 Image image generation model (bfl/flux-3-image-klein): where to run it - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-21T15:11:09.142386+00:00
---

# FLUX 3 Image image generation model (bfl/flux-3-image-klein): where to run it - ComfyUI

> Source: https://docs.comfy.org/catalog/models/bfl/flux-3-image-klein/

## On this page

Back to top

  * Where you can run it
  * Model files for running it locally
  * Workflow templates
  * Nodes



Catalog

# FLUX 3 Image image generation model (bfl/flux-3-image-klein): where to run it

Copy pageCopy page

FLUX 3 Image is a image generation model from Black Forest Labs. Run it with ComfyUI locally and Comfy Cloud; templates, files, nodes, and pricing.

Copy pageCopy page

Model ID: bfl/flux-3-image-klein Provider: bfl Product: local, cloud, workflows, nodes Input: image, text Output: image License: open-weights FLUX 3 Image is a image generation model from Black Forest Labs. It takes image and text as input and produces image. It has open weights, so you can download the files and run it locally in ComfyUI.

## Where you can run it

Where| Page| Use it when  
---|---|---  
ComfyUI (local or Comfy Cloud)| [FLUX 3 Image Klein in ComfyUI: Text-to-Image and Edit](https://docs.comfy.org/tutorials/flux/flux-3-klein)| You follow a step-by-step workflow tutorial  
Partner Nodes (ComfyUI and Comfy Cloud)| [FLUX 3 Image in ComfyUI: Text to Image and Image Edit](https://docs.comfy.org/tutorials/partner-nodes/black-forest-labs/flux-3-image)| You build a workflow with the hosted model  
Comfy Cloud| [Open `api_bfl_flux3_image_edit` on Comfy Cloud](https://cloud.comfy.org/?template=api_bfl_flux3_image_edit)| You want to run a ready-made workflow without installing anything  
  
## Model files for running it locally

Put each file in the matching folder under `ComfyUI/models/`. These come from the workflow templates below (workflow_templates at `3c2199b9`).

File| Folder| Download  
---|---|---  
`flux3-image-klein-base-int8-convrot.safetensors`| `models/diffusion_models/`| [Download](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy/resolve/main/diffusion_models/flux3-image-klein-base-int8-convrot.safetensors)  
`flux3-image-klein-int8-convrot.safetensors`| `models/diffusion_models/`| [Download](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy/resolve/main/diffusion_models/flux3-image-klein-int8-convrot.safetensors)  
`qwen3vl_4b_int8_convrot.safetensors`| `models/text_encoders/`| [Download](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy/resolve/main/text_encoders/qwen3vl_4b_int8_convrot.safetensors)  
`qwen3.5_9b_flux3_prompt_upsampler_w4a8.safetensors`| `models/text_encoders/`| [Download](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy/resolve/main/text_encoders/qwen3.5_9b_flux3_prompt_upsampler_w4a8.safetensors)  
`flux2-vae.safetensors`| `models/vae/`| [Download](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy/resolve/main/vae/flux2-vae.safetensors)  
  
## Workflow templates

Template| Title| Added  
---|---|---  
`image_flux3_klein_image_edit`| FLUX 3 Image Klein: Image Edit| 2026-10-15  
`image_flux3_klein_distilled_image_edit`| FLUX 3 Image Klein Distilled: Image Edit| 2026-10-15  
`image_flux3_klein_t2i`| FLUX 3 Image Klein: Text to Image| 2026-10-15  
`image_flux3_klein_distilled_t2i`| FLUX 3 Image Klein Distilled: Text to Image| 2026-10-15  
`api_bfl_flux3_image_edit`| FLUX 3 Image: Image Edit| 2026-10-01  
`api_bfl_flux3_t2i`| FLUX 3 Image: Text to Image| 2026-10-01  
`api_bfl_flux3_image_bboxes`| FLUX 3 Image: Bounding Box Edit| 2026-10-01  
  
## Nodes

  * [EmptyFlux2LatentImage](https://docs.comfy.org/built-in-nodes/EmptyFlux2LatentImage)
  * [Flux3ImageNode](https://docs.comfy.org/built-in-nodes/Flux3ImageNode)
  * [Flux3LayoutPrompt](https://docs.comfy.org/built-in-nodes/Flux3LayoutPrompt)



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/catalog/models/bfl/flux-3-image-klein.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/catalog/models/bfl/flux-3-image-klein)
