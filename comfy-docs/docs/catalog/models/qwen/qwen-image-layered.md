---
url: https://docs.comfy.org/catalog/models/qwen/qwen-image-layered/
title: Qwen-Image-Layered generation model (qwen/qwen-image-layered): where to run it - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-21T15:11:21.108350+00:00
---

# Qwen-Image-Layered generation model (qwen/qwen-image-layered): where to run it - ComfyUI

> Source: https://docs.comfy.org/catalog/models/qwen/qwen-image-layered/

## On this page

Back to top

  * Where you can run it
  * Model files for running it locally
  * Workflow templates
  * Nodes



Catalog

# Qwen-Image-Layered generation model (qwen/qwen-image-layered): where to run it

Copy pageCopy page

Qwen-Image-Layered is a generation model from Qwen. Run it with ComfyUI locally and Comfy Cloud; templates, files, nodes, and pricing.

Copy pageCopy page

Model ID: qwen/qwen-image-layered Provider: qwen Product: local, cloud, workflows, nodes Input: image License: open-weights Qwen-Image-Layered is a generation model from Qwen. It takes image as input and produces media. It has open weights, so you can download the files and run it locally in ComfyUI.

## Where you can run it

Where| Page| Use it when  
---|---|---  
ComfyUI (local or Comfy Cloud)| [Qwen-Image-Layered in ComfyUI: Image Layer Decomposition](https://docs.comfy.org/tutorials/image/qwen/qwen-image-layered)| You follow a step-by-step workflow tutorial  
Comfy Cloud| [Open `image_qwen_image_layered` on Comfy Cloud](https://cloud.comfy.org/?template=image_qwen_image_layered)| You want to run a ready-made workflow without installing anything  
  
## Model files for running it locally

Put each file in the matching folder under `ComfyUI/models/`. These come from the workflow templates below (workflow_templates at `3c2199b9`).

File| Folder| Download  
---|---|---  
`qwen_image_layered_bf16.safetensors`| `models/diffusion_models/`| [Download](https://huggingface.co/Comfy-Org/Qwen-Image-Layered_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_layered_bf16.safetensors)  
`qwen_image_layered_control_bf16.safetensors`| `models/diffusion_models/`| [Download](https://huggingface.co/DiffSynth-Studio/Qwen-Image-Layered-Control/resolve/main/qwen_image_layered_control_bf16.safetensors)  
`qwen_image_layered_vae.safetensors`| `models/vae/`| [Download](https://huggingface.co/Comfy-Org/Qwen-Image-Layered_ComfyUI/resolve/main/split_files/vae/qwen_image_layered_vae.safetensors)  
`qwen_2.5_vl_7b_fp8_scaled.safetensors`| `models/text_encoders/`| [Download](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors)  
  
## Workflow templates

Template| Title| Added  
---|---|---  
`image_qwen_image_layered_control`| Layer Decomposition: Qwen-Image-Layered Control| 2026-01-15  
`image_qwen_image_layered`| Layer Decomposition: Qwen-Image-Layered| 2025-12-22  
  
## Nodes

  * [EmptyQwenImageLayeredLatentImage](https://docs.comfy.org/built-in-nodes/EmptyQwenImageLayeredLatentImage)



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/catalog/models/qwen/qwen-image-layered.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/catalog/models/qwen/qwen-image-layered)
