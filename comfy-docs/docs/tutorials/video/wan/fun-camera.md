---
url: https://docs.comfy.org/tutorials/video/wan/fun-camera/
title: ComfyUI Wan2.1 Fun Camera Official Examples - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:45.203722+00:00
---

# ComfyUI Wan2.1 Fun Camera Official Examples - ComfyUI

> Source: https://docs.comfy.org/tutorials/video/wan/fun-camera/

## On this page

  * About Wan2.1 Fun Camera
  * Model Installation
    * Diffusion Models
    * Text Encoders
    * VAE
    * CLIP Vision
  * ComfyUI Wan2.1 Fun Camera 1.3B Workflow
    * Wan 2.1 Fun Camera 1.3B
    * 3\. Complete the Workflow Step by Step
  * ComfyUI Wan2.1 Fun Camera 14B Workflow
    * Wan 2.1 Fun Camera 14B
  * Performance Reference



Wan2.1

# ComfyUI Wan2.1 Fun Camera Official Examples

Copy pageCopy page

This guide demonstrates how to use Wan2.1 Fun Camera in ComfyUI for video generation

Copy pageCopy page

Wan2.1 Fun Camera is a camera-motion video generation model from Alibaba’s VideoX-Fun project, supported natively in ComfyUI. It generates videos whose camera movement follows your control conditions, so you can direct how the camera moves in the output instead of describing every shot in the prompt. The model is part of the Wan2.1-Fun family and ships in two sizes: the 1.3B version (about 19 GB) for lightweight local runs and the 14B version (about 47 GB) for higher-fidelity output. Both support multi-resolution video prediction at 512, 768, and 1024 pixels, are trained at 16 frames per second for up to 81 frames (about 5 seconds), and accept multilingual prompts. The weights are released under the Apache-2.0 license.

## 

​

About Wan2.1 Fun Camera

**Wan2.1 Fun Camera** is a video generation project launched by the Alibaba team, focusing on controlling video generation effects through camera motion. **Model Weights Download** :

  * [14B Version](https://huggingface.co/alibaba-pai/Wan2.1-Fun-V1.1-14B-Control-Camera)
  * [1.3B Version](https://huggingface.co/alibaba-pai/Wan2.1-Fun-V1.1-1.3B-Control-Camera)

**Code Repository** : [VideoX-Fun](https://github.com/aigc-apps/VideoX-Fun) **ComfyUI now natively supports the Wan2.1 Fun Camera model**.

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

Model Installation

These models only need to be installed once. Additionally, model download information is included in the corresponding workflow images, so you can choose your preferred way to download the models. All of the following models can be found at [Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged)

### 

​

Diffusion Models

Choose either 1.3B or 14B:

## wan2.1_fun_camera_v1.1_1.3B_bf16.safetensors

Wan2.1 Fun Camera 1.3B diffusion model

## wan2.1_fun_camera_v1.1_14B_bf16.safetensors

Wan2.1 Fun Camera 14B diffusion model

If you’ve used Wan2.1 related models before, you should already have the following models. If not, please download them:

### 

​

Text Encoders

Choose one of the following:

## umt5_xxl_fp16.safetensors

Full precision text encoder

## umt5_xxl_fp8_e4m3fn_scaled.safetensors

FP8 quantized text encoder (recommended for lower VRAM)

### 

​

VAE

## wan_2.1_vae.safetensors

Wan2.1 VAE model

### 

​

CLIP Vision

## clip_vision_h.safetensors

CLIP vision encoder

File Storage Location:
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │ ├── 📂 diffusion_models/
    │ │   ├── wan2.1_fun_camera_v1.1_1.3B_bf16.safetensors # 1.3B version
    │ │   └── wan2.1_fun_camera_v1.1_14B_bf16.safetensors # 14B version
    │ ├── 📂 text_encoders/
    │ │   └── umt5_xxl_fp8_e4m3fn_scaled.safetensors
    │ ├── 📂 vae/
    │ │   └── wan_2.1_vae.safetensors
    │ └── 📂 clip_vision/
    │     └── clip_vision_h.safetensors
    

## 

​

ComfyUI Wan2.1 Fun Camera 1.3B Workflow

### 

​

Wan 2.1 Fun Camera 1.3B

Generate dynamic videos with cinematic camera movements using Wan 2.1 Fun Camera 1.3B model. ![Wan 2.1 Fun Camera 1.3B workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan2.1_fun_camera_v1.1_1.3B-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Wan 2.1 Fun Camera 1.3B” in Template Library

Download the video below and drag it into ComfyUI to load the corresponding workflow:

If you want to use the 14B version, simply replace the model file with the 14B version, but please be aware of the VRAM requirements.

**Input materials** Upload this file to the matching `LoadImage` node:

## video_wan2.1_fun_camera_v1.1_1.3B_start_image.jpg

`LoadImage` node 52 · `video_wan2.1_fun_camera_v1.1_1.3B_start_image.jpg`

![video_wan2.1_fun_camera_v1.1_1.3B_start_image.jpg](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/video_wan2.1_fun_camera_v1.1_1.3B_start_image.jpg)

### 

​

3\. Complete the Workflow Step by Step

![Wan2.1 Fun Camera Workflow Steps](https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2-1-fun-camera-1-3b-step-guide.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=f6fb10f8a36cb9036a66e1e99986c641)

  1. Ensure the correct version of model file is loaded: 
     * 1.3B version: `wan2.1_fun_camera_v1.1_1.3B_bf16.safetensors`
     * 14B version: `wan2.1_fun_camera_v1.1_14B_bf16.safetensors`
  2. Ensure the `Load CLIP` node has loaded `umt5_xxl_fp8_e4m3fn_scaled.safetensors`
  3. Ensure the `Load VAE` node has loaded `wan_2.1_vae.safetensors`
  4. Ensure the `Load CLIP Vision` node has loaded `clip_vision_h.safetensors`
  5. Upload the starting frame to the `Load Image` node
  6. Modify the Prompt if you’re using your own input image
  7. Set camera motion in the `WanCameraEmbedding` node
  8. Click the `Run` button or use the shortcut `Ctrl(cmd) + Enter` to execute generation



## 

​

ComfyUI Wan2.1 Fun Camera 14B Workflow

### 

​

Wan 2.1 Fun Camera 14B

Generate high-quality videos with advanced camera control using the full 14B model. ![Wan 2.1 Fun Camera 14B workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan2.1_fun_camera_v1.1_14B-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Wan 2.1 Fun Camera 14B” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## video_wan2.1_fun_camera_v1.1_14B_start_image.jpg

`LoadImage` node 52 · `video_wan2.1_fun_camera_v1.1_14B_start_image.jpg`

![video_wan2.1_fun_camera_v1.1_14B_start_image.jpg](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/video_wan2.1_fun_camera_v1.1_14B_start_image.jpg)

## 

​

Performance Reference

**1.3B Version** :

  * 512x512 resolution on RTX 4090 takes about 72 seconds to generate 81 frames

**14B Version** :

  * RTX4090 24GB VRAM may experience insufficient memory when generating 512x512 resolution, and memory issues have also occurred on A100 when using larger sizes



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/video/wan/fun-camera.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/video/wan/fun-camera)

[ComfyUI Wan2.1 Fun Control Video ExamplesPrevious](https://docs.comfy.org/tutorials/video/wan/fun-control)[Wan2.1 Fun InP in ComfyUI: First and Last Frame VideoNext](https://docs.comfy.org/tutorials/video/wan/fun-inp)

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
