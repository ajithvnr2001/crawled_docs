---
url: https://docs.comfy.org/tutorials/video/ltxv/
title: LTX-Video 0.9.5 in ComfyUI: T2V, I2V, Multi-Frame Control - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:44.448542+00:00
---

# LTX-Video 0.9.5 in ComfyUI: T2V, I2V, Multi-Frame Control - ComfyUI

> Source: https://docs.comfy.org/tutorials/video/ltxv/

## On this page

  * Multi Frame Control
  * Image to Video
    * LTXV Image to Video
  * Text to Video
    * LTXV Text to Video
  * Requirements



LTX

# LTX-Video 0.9.5 in ComfyUI: T2V, I2V, Multi-Frame Control

Copy pageCopy page

Run LTX-Video 0.9.5 in ComfyUI for text-to-video, image-to-video, and multi-frame control from start and end images, with model download and setup steps.

Copy pageCopy page

[LTX-Video](https://huggingface.co/Lightricks/LTX-Video) is a very efficient video model by lightricks. The important thing with this model is to give it long descriptive prompts.

  * Local users

  * Cloud users




Make sure your ComfyUI is updated.

  * [Download ComfyUI](https://www.comfy.org/download)
  * [Update Guide](https://docs.comfy.org/installation/update_comfyui)

Workflows in this guide can be found in the [Workflow Templates](https://docs.comfy.org/interface/features/template). If you can’t find them in the template, your ComfyUI may be outdated.If nodes are missing when loading a workflow, possible reasons:

  1. You are not using the latest ComfyUI version (Nightly version)
  2. Some nodes failed to import at startup



  * [Cloud](https://cloud.comfy.org) will update after ComfyUI stable release.

So, if you find any core node missing in this document, it might be because the new core nodes have not yet been released in the latest stable version. Please wait for the next stable release.

## 

​

Multi Frame Control

Allows you to control the video with a series of images. You can download the input images: [starting frame](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/ltxv/multi-frame/house1.png) and [ending frame](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/ltxv/multi-frame/house2.png). ![LTX-Video Multi Frame Control](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/ltxv/multi-frame/workflow.webp)

Drag the video directly into ComfyUI to run the workflow.

## 

​

Image to Video

### 

​

LTXV Image to Video

Generate videos from still images. ![LTXV Image to Video workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/ltxv_image_to_video-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “LTXV Image to Video” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## ltxv_image_to_video_input_image.jpg

`LoadImage` node 78 · `ltxv_image_to_video_input_image.jpg`

![ltxv_image_to_video_input_image.jpg](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/ltxv_image_to_video_input_image.jpg)

Drag the video directly into ComfyUI to run the workflow.

## 

​

Text to Video

### 

​

LTXV Text to Video

Generate videos from text prompts. ![LTXV Text to Video workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/ltxv_text_to_video-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “LTXV Text to Video” in Template Library

Drag the video directly into ComfyUI to run the workflow.

## 

​

Requirements

Download the following models and place them in the locations specified below:

## ltx-video-2b-v0.9.5.safetensors

Download and place in ComfyUI/models/checkpoints/

## t5xxl_fp16.safetensors

Download and place in ComfyUI/models/text_encoders/
    
    
    ├── checkpoints/
    │   └── ltx-video-2b-v0.9.5.safetensors
    └── text_encoders/
        └── t5xxl_fp16.safetensors
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/video/ltxv.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/video/ltxv)

[FastVideo FastH3: ComfyUI Workflow ExamplesPrevious](https://docs.comfy.org/tutorials/video/minimax/minimax-h3-fastvideo)[LTX-2.0 ComfyUI Workflow ExamplesNext](https://docs.comfy.org/tutorials/video/ltx/ltx-2)

⌘I

[ComfyUI home page![light logo](https://mintcdn.com/dripart/WCFdTagRdhtvk9-o/logo/light.svg?fit=max&auto=format&n=WCFdTagRdhtvk9-o&q=85&s=ec112de87239058f5a931a7e4b594965)![dark logo](https://mintcdn.com/dripart/QzWbjSCBG7w61rR3/logo/dark.svg?fit=max&auto=format&n=QzWbjSCBG7w61rR3&q=85&s=62b4d879fb3aadbd7a468d1539032d6f)](https://docs.comfy.org/)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

Resources

[installation](https://docs.comfy.org/installation/system_requirements)[Tutorials](https://docs.comfy.org/tutorials/basic/text-to-image)[Development](https://docs.comfy.org/development/overview)

Products

[Features](https://www.comfy.org/?utm_source=docs)[Gallery](https://www.comfy.org/gallery?utm_source=docs)[Download](https://www.comfy.org/download?utm_source=docs)

Company

[About](https://www.comfy.org/about?utm_source=docs)[Careers](https://www.comfy.org/careers?utm_source=docs)[Terms of Service](https://www.comfy.org/terms-of-service?utm_source=docs)[Privacy Policy](https://www.comfy.org/privacy-policy?utm_source=docs)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=dripart)
