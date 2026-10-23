---
url: https://docs.comfy.org/tutorials/utility/video-segment-sam3/
title: SAM 3.1: Segment Anything in ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:41.685361+00:00
---

# SAM 3.1: Segment Anything in ComfyUI - ComfyUI

> Source: https://docs.comfy.org/tutorials/utility/video-segment-sam3/

## On this page

  * Key strengths
  * SAM 3.1 Segment Workflows
    * 1\. Download Workflow
    * SAM3: Video Segmentation
    * SAM3: Image Segmentation
    * 2\. Download Models
    * 3\. Using the Workflows
  * Additional Notes



Segmentation & Background

# SAM 3.1: Segment Anything in ComfyUI

Copy pageCopy page

Learn how to use Meta’s SAM 3.1 model in ComfyUI to segment objects in images and videos using text prompts

Copy pageCopy page

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

[SAM 3](https://ai.meta.com/sam3) (Segment Anything Model 3) is Meta’s unified foundation model for promptable segmentation in images and videos. It can detect, segment, and track objects using text or visual prompts such as points, boxes, and masks. Compared to its predecessor [SAM 2](https://github.com/facebookresearch/sam2), SAM 3 introduces the ability to exhaustively segment all instances of an open-vocabulary concept specified by a short text phrase. [SAM 3.1 Multiplex](https://github.com/facebookresearch/sam3) is the latest checkpoint release that introduces a shared-memory approach for joint multi-object tracking: significantly faster without sacrificing accuracy. SAM 3.1 is natively supported in ComfyUI (PR [#13408](https://github.com/Comfy-Org/ComfyUI/pull/13408)), and the model weights are available under the [SAM License](https://github.com/facebookresearch/sam3/blob/main/LICENSE). [SAM 3 GitHub](https://github.com/facebookresearch/sam3) | [Paper (arXiv)](https://arxiv.org/abs/2604.02296) | [🤗 Model Hub](https://huggingface.co/Comfy-Org/sam3.1) SAM 3.1 segments and tracks objects across video frames based on text prompts. The example above shows the segmentation output with masks applied to the target objects throughout the video.

### 

​

Key strengths

  * **Text-driven segmentation** : describe what to segment in natural language, no need for manual point/box annotations
  * **Image and video support** : works on both single images and video sequences with tracking across frames
  * **Multi-object support** : segment and track multiple objects simultaneously using comma-separated prompts
  * **Open-vocabulary** : handles a vastly larger set of open-vocabulary concepts than prior works



> **Limitations:** The model has a max token limit of 32 for text prompts. For best results, keep prompts short and specific to the target object.

## 

​

SAM 3.1 Segment Workflows

### 

​

1\. Download Workflow

Update your ComfyUI to the latest version, then go to `Workflow` -> `Browse Templates` and find the SAM 3.1 workflows under the Utility category.

### 

​

SAM3: Video Segmentation

Use the SAM3 model to segment the main subject or content from a video, isolating specific objects or regions. ![SAM3 video segmentation workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_video_segment_sam3-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “SAM3: Video Segmentation” in Template Library

**Input materials** Upload this file to the matching `LoadVideo` node:

## drinking_unicorn.mp4

`LoadVideo` node 115 · `drinking_unicorn.mp4`

**Example output**

### 

​

SAM3: Image Segmentation

Use the SAM3 model to segment the main subject or content from a photo or image, isolating specific objects or regions. ![SAM3 image segmentation workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_image_segment_sam3-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “SAM3: Image Segmentation” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## neon_guitarist.png

`LoadImage` node 79 · `neon_guitarist.png`

![Input image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/neon_guitarist.png)

### 

​

2\. Download Models

The SAM 3.1 model is hosted on the [Comfy-Org SAM 3.1 model repository](https://huggingface.co/Comfy-Org/sam3.1).

  * [sam3.1_multiplex_fp16.safetensors](https://huggingface.co/Comfy-Org/sam3.1/blob/main/checkpoints/sam3.1_multiplex_fp16.safetensors)

Place it in the following directory structure:
    
    
    📂 ComfyUI/
    └── 📂 models/
        └── 📂 checkpoints/
            └── sam3.1_multiplex_fp16.safetensors
    

### 

​

3\. Using the Workflows

**Image Segmentation:**

  * **Image** : Load an image via the `Load Image` node (place it in the ComfyUI `input/` folder)
  * **Object Prompt** : A short text description of the object(s) to segment, e.g. `person`, `car`, `cat`
  * The output is a mask applied to the image, with an RGBA preview showing the segmentation result

**Video Segmentation:**

  * **Video** : Load a video via the `Load Video` node
  * **Object Prompt** : Same as image, a short text prompt describing what to track and segment across frames
  * The output provides masks and bounding boxes for each frame

**Prompt format:**

Prompt| Role  
---|---  
SAM3 object prompt| Short description of **what** to segment. Max 32 tokens.  
  
To prompt multiple subjects separately, separate with commas and use `:N` to specify the max amount of objects detected per prompt: `eye:2, window panels:4`

## Learn about Subgraph

This workflow uses Subgraph nodes for modular processing. Check out the Subgraph documentation to learn how to customize and extend the workflow.

## 

​

Additional Notes

  * **Keep prompts short and specific** : the model has a 32-token limit per prompt
  * **Multi-object detection** : use commas to separate different object types, and `:N` to cap detections per type
  * **Segmentation masks** : the output mask can be used as input to other workflows (e.g., inpainting, background removal)
  * **Update required** : make sure ComfyUI is updated to the latest version to access SAM 3.1 support



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/utility/video-segment-sam3.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/utility/video-segment-sam3)

[SeedVR2: Image and video upscaling in ComfyUIPrevious](https://docs.comfy.org/tutorials/utility/seedvr2)[BiRefNet: Remove Image Background in ComfyUINext](https://docs.comfy.org/tutorials/utility/remove-background-birefnet)

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
