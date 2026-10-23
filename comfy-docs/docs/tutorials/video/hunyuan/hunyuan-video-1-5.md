---
url: https://docs.comfy.org/tutorials/video/hunyuan/hunyuan-video-1-5/
title: HunyuanVideo 1.5 in ComfyUI: T2V and I2V on Consumer GPUs - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-19T14:35:07.213749+00:00
---

# HunyuanVideo 1.5 in ComfyUI: T2V and I2V on Consumer GPUs - ComfyUI

> Source: https://docs.comfy.org/tutorials/video/hunyuan/hunyuan-video-1-5/

## On this page

  * Model highlights
  * Common models for all workflows
    * Storage
  * Hunyuan Video 1.5 Text-to-Video Workflow
    * Model downloads
    * Model storage
    * Steps to run the workflow
  * Hunyuan Video 1.5 Image-to-Video Workflow
    * Model downloads
    * Model storage
    * Steps to run the workflow
  * Super-resolution upscaler



Hunyuan

# HunyuanVideo 1.5 in ComfyUI: T2V and I2V on Consumer GPUs

Copy pageCopy page

Run HunyuanVideo 1.5 in ComfyUI on a 24GB GPU: 8.3B text-to-video and image-to-video at 720p, plus a super-resolution upscaler for 1080p.

Copy pageCopy page

[HunyuanVideo 1.5](https://github.com/Tencent/HunyuanVideo) is a lightweight 8.3B parameter model developed by Tencent’s Hunyuan team. It delivers flagship-quality video generation on consumer GPUs (24GB VRAM), dramatically lowering the barrier to entry without compromising on quality.

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

Model highlights

  * **Compact powerhouse** : Delivers SOTA performance comparable to larger models while running on consumer hardware.
  * **Versatile generation** : Supports high-quality Text-to-Video and Image-to-Video (5-10s) with exceptional consistency.
  * **Precise control** : Strong instruction following for camera movements, physics, and emotional expressions.
  * **Cinematic quality** : Native 720p output (upscalable to 1080p) with professional aesthetics.
  * **Rich features** : Supports diverse styles (realistic, anime, 3D) and in-video text rendering (Chinese/English).



## 

​

Common models for all workflows

The following models are used in both Text-to-Video and Image-to-Video workflows. Download and save them to the specified directories:

## Download Qwen2.5 VL 7B

qwen_2.5_vl_7b_fp8_scaled.safetensors — save to `ComfyUI/models/text_encoders/`

## Download ByT5 Small

byt5_small_glyphxl_fp16.safetensors — save to `ComfyUI/models/text_encoders/`

## Download HunyuanVideo 1.5 VAE

hunyuanvideo15_vae_fp16.safetensors — save to `ComfyUI/models/vae/`

#### 

​

Storage
    
    
    ComfyUI/
    ├── 📂 models/
    │   ├── 📂 text_encoders/
    │   │   ├── qwen_2.5_vl_7b_fp8_scaled.safetensors
    │   │   └── byt5_small_glyphxl_fp16.safetensors
    │   └── 📂 vae/
    │       └── hunyuanvideo15_vae_fp16.safetensors
    

## 

​

Hunyuan Video 1.5 Text-to-Video Workflow

HunyuanVideo 1.5 Text-to-Video generates 5-10 second videos from natural language descriptions with enhanced quality and reduced VRAM requirements. ![ComfyUI Workflow - Hunyuan Video 1.5 T2V](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_hunyuan_video_1.5_720p_t2v-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Hunyuan Video 1.5 T2V” in Template Library

### 

​

Model downloads

## Download T2V Diffusion Model

hunyuanvideo1.5_720p_t2v_fp16.safetensors — save to `ComfyUI/models/diffusion_models/`

#### 

​

Model storage
    
    
    ComfyUI/
    ├── 📂 models/
    │   ├── 📂 text_encoders/
    │   │   ├── qwen_2.5_vl_7b_fp8_scaled.safetensors       // Shared model
    │   │   └── byt5_small_glyphxl_fp16.safetensors           // Shared model
    │   ├── 📂 vae/
    │   │   └── hunyuanvideo15_vae_fp16.safetensors           // Shared model
    │   └── 📂 diffusion_models/
    │       └── hunyuanvideo1.5_720p_t2v_fp16.safetensors     // T2V model
    

### 

​

Steps to run the workflow

  1. Ensure the `DualCLIPLoader` node has loaded these models: 
     * clip_name1: `qwen_2.5_vl_7b_fp8_scaled.safetensors`
     * clip_name2: `byt5_small_glyphxl_fp16.safetensors`
  2. Ensure the `Load Diffusion Model` node has loaded `hunyuanvideo1.5_720p_t2v_fp16.safetensors`
  3. Ensure the `Load VAE` node has loaded `hunyuanvideo15_vae_fp16.safetensors`
  4. Click the `Queue` button or use the shortcut `Ctrl(Cmd) + Enter` to run the workflow



The workflow includes a super-resolution upscaler node. When enabled, it uses `hunyuanvideo1.5_1080p_sr_distilled_fp16.safetensors` to upscale the output to 1080p.

## 

​

Hunyuan Video 1.5 Image-to-Video Workflow

HunyuanVideo 1.5 Image-to-Video transforms static images into smooth, high-quality videos with improved consistency and motion dynamics. ![ComfyUI Workflow - Hunyuan Video 1.5 I2V](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_hunyuan_video_1.5_720p_i2v-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Hunyuan Video 1.5 I2V” in Template Library

**Input materials**

## Input Image

Download the default input image, or use your own image as the starting frame.

### 

​

Model downloads

## Download CLIP Vision

sigclip_vision_patch14_384.safetensors — save to `ComfyUI/models/clip_vision/`

## Download I2V Diffusion Model

hunyuanvideo1.5_720p_i2v_fp16.safetensors — save to `ComfyUI/models/diffusion_models/`

#### 

​

Model storage
    
    
    ComfyUI/
    ├── 📂 models/
    │   ├── 📂 clip_vision/
    │   │   └── sigclip_vision_patch14_384.safetensors          // I2V vision encoder
    │   ├── 📂 text_encoders/
    │   │   ├── qwen_2.5_vl_7b_fp8_scaled.safetensors           // Shared model
    │   │   └── byt5_small_glyphxl_fp16.safetensors             // Shared model
    │   ├── 📂 vae/
    │   │   └── hunyuanvideo15_vae_fp16.safetensors             // Shared model
    │   └── 📂 diffusion_models/
    │       └── hunyuanvideo1.5_720p_i2v_fp16.safetensors       // I2V model
    

### 

​

Steps to run the workflow

  1. Ensure the `DualCLIPLoader` node has loaded these models: 
     * clip_name1: `qwen_2.5_vl_7b_fp8_scaled.safetensors`
     * clip_name2: `byt5_small_glyphxl_fp16.safetensors`
  2. Ensure the `CLIPVisionLoader` node has loaded `sigclip_vision_patch14_384.safetensors`
  3. Ensure the `Load Diffusion Model` node has loaded `hunyuanvideo1.5_720p_i2v_fp16.safetensors`
  4. Ensure the `Load VAE` node has loaded `hunyuanvideo15_vae_fp16.safetensors`
  5. Click the `Queue` button or use the shortcut `Ctrl(Cmd) + Enter` to run the workflow



## 

​

Super-resolution upscaler

Both workflows include a super-resolution node that can upscale the output video from 720p to 1080p. This optional upscaler uses a distilled model for efficient high-resolution output.

## Download 1080p Upscaler

hunyuanvideo1.5_1080p_sr_distilled_fp16.safetensors — save to `ComfyUI/models/diffusion_models/`

All shared and workflow-specific models combined:
    
    
    ComfyUI/
    ├── 📂 models/
    │   ├── 📂 clip_vision/
    │   │   └── sigclip_vision_patch14_384.safetensors
    │   ├── 📂 text_encoders/
    │   │   ├── qwen_2.5_vl_7b_fp8_scaled.safetensors
    │   │   └── byt5_small_glyphxl_fp16.safetensors
    │   ├── 📂 vae/
    │   │   └── hunyuanvideo15_vae_fp16.safetensors
    │   └── 📂 diffusion_models/
    │       ├── hunyuanvideo1.5_720p_t2v_fp16.safetensors        // T2V model
    │       ├── hunyuanvideo1.5_720p_i2v_fp16.safetensors        // I2V model
    │       └── hunyuanvideo1.5_1080p_sr_distilled_fp16.safetensors  // Upscaler
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/video/hunyuan/hunyuan-video-1-5.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/video/hunyuan/hunyuan-video-1-5)

[ComfyUI Hunyuan Video ExamplesPrevious](https://docs.comfy.org/tutorials/video/hunyuan/hunyuan-video)[Cosmos Predict2 Video2World in ComfyUI: Image to Video GenerationNext](https://docs.comfy.org/tutorials/video/cosmos/cosmos-predict2-video2world)

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
