---
url: https://docs.comfy.org/catalog/models/ltxv/ltx-video/
title: LTX-0.9.5 video generation model (ltxv/ltx-video): where to run it - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-21T15:11:17.034616+00:00
---

# LTX-0.9.5 video generation model (ltxv/ltx-video): where to run it - ComfyUI

> Source: https://docs.comfy.org/catalog/models/ltxv/ltx-video/

## On this page

Back to top

  * Where you can run it
  * Model files for running it locally
  * Workflow templates
  * Nodes



Catalog

# LTX-0.9.5 video generation model (ltxv/ltx-video): where to run it

Copy pageCopy page

LTX-0.9.5 is a video generation model from Lightricks (LTXV). Run it with ComfyUI locally and Comfy Cloud; templates, files, nodes, and pricing.

Copy pageCopy page

Model ID: ltxv/ltx-video Provider: ltxv Product: local, cloud, workflows, nodes Input: image, text Output: video License: open-weights LTX-0.9.5 is a video generation model from Lightricks (LTXV). It takes image and text as input and produces video. It has open weights, so you can download the files and run it locally in ComfyUI.

## Where you can run it

Where| Page| Use it when  
---|---|---  
ComfyUI (local or Comfy Cloud)| [LTX-Video 0.9.5 in ComfyUI: T2V, I2V, Multi-Frame Control](https://docs.comfy.org/tutorials/video/ltxv)| You follow a step-by-step workflow tutorial  
Comfy Cloud| [Open `ltxv_image_to_video` on Comfy Cloud](https://cloud.comfy.org/?template=ltxv_image_to_video)| You want to run a ready-made workflow without installing anything  
  
## Model files for running it locally

Put each file in the matching folder under `ComfyUI/models/`. These come from the workflow templates below (workflow_templates at `3c2199b9`).

File| Folder| Download  
---|---|---  
`ltx-video-2b-v0.9.5.safetensors`| `models/checkpoints/`| [Download](https://huggingface.co/Lightricks/LTX-Video/resolve/main/ltx-video-2b-v0.9.5.safetensors)  
`ltx-video-2b-v0.9.safetensors`| `models/checkpoints/`| [Download](https://huggingface.co/Lightricks/LTX-Video/resolve/main/ltx-video-2b-v0.9.safetensors?download=true)  
`t5xxl_fp16.safetensors`| `models/text_encoders/`| [Download](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp16.safetensors)  
  
## Workflow templates

Template| Title| Added  
---|---|---  
`ltxv_image_to_video`| LTXV Image to Video| 2025-03-01  
`ltxv_text_to_video`| LTXV Text to Video| 2025-03-01  
  
## Nodes

  * [EmptyLTXVLatentVideo](https://docs.comfy.org/built-in-nodes/EmptyLTXVLatentVideo)
  * [LTXVConditioning](https://docs.comfy.org/built-in-nodes/LTXVConditioning)
  * [LTXVImgToVideo](https://docs.comfy.org/built-in-nodes/LTXVImgToVideo)
  * [LTXVScheduler](https://docs.comfy.org/built-in-nodes/LTXVScheduler)



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/catalog/models/ltxv/ltx-video.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/catalog/models/ltxv/ltx-video)
