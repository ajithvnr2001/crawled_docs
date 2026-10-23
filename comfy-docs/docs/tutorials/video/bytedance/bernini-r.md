---
url: https://docs.comfy.org/tutorials/video/bytedance/bernini-r/
title: Bernini-R in ComfyUI: In-Context Image and Video Editing - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:42.249214+00:00
---

# Bernini-R in ComfyUI: In-Context Image and Video Editing - ComfyUI

> Source: https://docs.comfy.org/tutorials/video/bytedance/bernini-r/

## On this page

  * ComfyUI Bernini-R Introduction
  * Model Installation
  * Example Workflows
  * 1\. Image Editing
    * Steps to Run
  * 2\. Video Editing
    * Steps to Run
  * Community Resources



ByteDance

# Bernini-R in ComfyUI: In-Context Image and Video Editing

Copy pageCopy page

Edit images and videos in ComfyUI with ByteDance Bernini-R, a renderer-only Wan 2.2 model that conditions on reference images or video without LoRA training.

Copy pageCopy page

# 

​

ComfyUI Bernini-R Introduction

[Bernini-R](https://github.com/bytedance/Bernini) is ByteDance’s **renderer-only** Wan 2.2 model for in-context image and video conditioning. It uses a set of conditioning streams (source video, reference images, reference video) to guide generation. No LoRA training or fine-tuning required. Key capabilities:

  * **Multiple task types in one model** : image/video generation, editing, relighting, restyling, subject insertion
  * **In-context conditioning** : reference images/videos act as visual prompts, injected as tokens
  * **Lightweight** : renderer-only model. No diffusion-based text-to-video backbone.
  * **Flexible input support** : single or multi-image references, video-to-video, reference-guided editing

Bernini-R supports these task types:

Task| Inputs| Description  
---|---|---  
**t2v**|  Text prompt| Text-to-video generation  
**v2v**|  Source video| Video-to-video restyling  
**rv2v**|  Source video + ref images(s)| Reference-guided video editing (relighting, subject insertion)  
**r2v**|  Reference image(s) only| Reference-to-video generation  
**img**|  Source image + text prompt| Image editing (relighting, restyling, subject insertion)  
**ads2v**|  Source video + ref video| Insert image/video content into source video  
  
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

ComfyUI now natively supports Bernini-R nodes. Make sure you have updated to the latest version of [ComfyUI](https://github.com/Comfy-Org/ComfyUI) before starting.

## 

​

Model Installation

Download the required model weights and save them to the corresponding ComfyUI folders: **text_encoders:**

  * [umt5_xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/blob/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors?download=true)

**vae:**

  * [Wan2_1_VAE_bf16.safetensors](https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1_VAE_bf16.safetensors?download=true)

**loras:**

  * [lightx2v_T2V_14B_cfg_step_distill_v2_lora_rank64_bf16.safetensors](https://huggingface.co/Kijai/WanVideo_comfy/blob/main/lightx2v_T2V_14B_cfg_step_distill_v2_lora_rank64_bf16.safetensors?download=true)

**diffusion_models:**

  * [wan2.2_bernini_r_fp16.safetensors](https://huggingface.co/Comfy-Org/Bernini-R/blob/main/wan2.2_bernini_r_fp16.safetensors)


    
    
    ComfyUI/
    ├── models/
    │   ├── text_encoders/
    │   │   └── umt5_xxl_fp8_e4m3fn_scaled.safetensors
    │   ├── vae/
    │   │   └── Wan2_1_VAE_bf16.safetensors
    │   ├── loras/
    │   │   └── lightx2v_T2V_14B_cfg_step_distill_v2_lora_rank64_bf16.safetensors
    │   ├── diffusion_models/
    │   │   └── wan2.2_bernini_r_fp16.safetensors
    

## 

​

Example Workflows

* * *

## 

​

1\. Image Editing

**What it does:** Generate an edited image with matched lighting and view a side-by-side before/after comparison. Ideal for portrait and product relighting, consistent lighting across photo sets, and e-commerce catalog photography. ![Bernini-R Image Editing workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_bernini_r_image_editing-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Bernini-R” in Template Library

**Input materials**

## Input Image

Download the default input image, or use your own.

## Reference Image

Download the default reference image, or use your own.

### 

​

Steps to Run

  1. **Select Task Type** : choose your task (Image Editing, Subject to Image, etc.)
  2. **Connect Inputs** : load source image and optional reference images
  3. **Write Prompt** : describe the desired edit
  4. **Run** : click Queue or use `Cmd+Enter`

**Reference Image input:** Use for **Subject to Image** when you need one or more reference images (subject, outfit, scene, props). In the prompt, use `image0`, `image1`, … to reference each image. Not needed for **Image Editing** : that task uses `source_image` instead.

## Learn about Subgraph

This workflow uses Subgraph nodes for modular processing. Check out the Subgraph documentation to learn how to customize and extend the workflow.

* * *

## 

​

2\. Video Editing

**What it does:** Generate an edited video with consistent relighting using Bernini-R. Connect a source video, optional reference image(s) or reference video, pick the task type, write a prompt, and run. ![Bernini-R Video Editing workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_bernini_r_video_editing-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Bernini-R” in Template Library

**Input materials**

## Input Video

Download the default input video, or use your own.

## Reference Image

Download the default reference image, or use your own.

### 

​

Steps to Run

  1. **Load Source Video** : connect your input video
  2. **(Optional) Load References** : reference image(s) or reference video
  3. **Select Task Type** : v2v, rv2v, r2v, or ads2v
  4. **Write Prompt** : describe the desired edit
  5. **Run** : click Queue or use `Cmd+Enter`

**Reference Image input:** Use when a task needs one or more reference images (rv2v, r2v, multi-piece outfits). Each batched image becomes its own in-context token. Mention `image0`, `image1`, … in the prompt if references play different roles.

## Learn about Subgraph

This workflow uses Subgraph nodes for modular processing. Check out the Subgraph documentation to learn how to customize and extend the workflow.

* * *

## 

​

Community Resources

  * [Bernini GitHub (bytedance/Bernini)](https://github.com/bytedance/Bernini): Research paper and task documentation
  * [Comfy-Org/Bernini-R](https://huggingface.co/Comfy-Org/Bernini-R): Official ComfyUI model weights
  * [Bernini: Latent Semantic Planning for Video Diffusion](https://arxiv.org/abs/2605.22344): Research paper



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/video/bytedance/bernini-r.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/video/bytedance/bernini-r)

[ComfyUI Wan2.1 InfiniteTalk Workflow ExamplePrevious](https://docs.comfy.org/tutorials/video/wan/wan-infinitetalk)[ComfyUI Hunyuan Video ExamplesNext](https://docs.comfy.org/tutorials/video/hunyuan/hunyuan-video)

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
