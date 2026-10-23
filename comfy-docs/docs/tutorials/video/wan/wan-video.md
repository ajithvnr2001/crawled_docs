---
url: https://docs.comfy.org/tutorials/video/wan/wan-video/
title: Wan2.1 in ComfyUI: Text-to-Video and Image-to-Video Workflows - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-19T14:35:05.384184+00:00
---

# Wan2.1 in ComfyUI: Text-to-Video and Image-to-Video Workflows - ComfyUI

> Source: https://docs.comfy.org/tutorials/video/wan/wan-video/

## On this page

  * Wan2.1 ComfyUI Native Workflow Examples
  * Model Installation
  * Wan2.1 Text-to-Video Workflow (1.3B)
    * Wan 2.1 Text to Video
    * Model Downloads
    * Steps to Run
  * Wan2.1 Image-to-Video Workflow (14B)
    * 480P Version
    * Wan 2.1 Image to Video
    * Model Downloads
    * Steps to Run
    * 720P Version
    * Model Downloads
    * Steps to Run



Wan2.1

# Wan2.1 in ComfyUI: Text-to-Video and Image-to-Video Workflows

Copy pageCopy page

Run the 1.3B text-to-video model and the 14B image-to-video model, with model file installation and the native ComfyUI workflows for both.

Copy pageCopy page

Wan2.1 Video series is a video generation model open-sourced by Alibaba in February 2025 under the [Apache 2.0 license](https://github.com/Wan-Video/Wan2.1?tab=Apache-2.0-1-ov-file). It offers two versions:

  * 14B (14 billion parameters)
  * 1.3B (1.3 billion parameters) Covering multiple tasks including text-to-video (T2V) and image-to-video (I2V). The model not only outperforms existing open-source models in performance but more importantly, its lightweight version requires only 8GB of VRAM to run, significantly lowering the barrier to entry.



  * [Wan2.1 Code Repository](https://github.com/Wan-Video/Wan2.1)
  * [Wan2.1 Model Repository](https://huggingface.co/Wan-AI)



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

Wan2.1 ComfyUI Native Workflow Examples

Please update ComfyUI to the latest version before starting the examples to make sure you have native Wan Video support.

## 

​

Model Installation

All models mentioned in this guide can be found [here](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files). Below are the common models you’ll need for the examples in this guide, which you can download in advance: Choose one version from **Text encoders** to download:

## umt5_xxl_fp16.safetensors

FP16 precision text encoder. Place in `ComfyUI/models/text_encoders/`

## umt5_xxl_fp8_e4m3fn_scaled.safetensors

FP8 scaled text encoder. Place in `ComfyUI/models/text_encoders/`

**VAE**

## wan_2.1_vae.safetensors

Wan2.1 VAE model. Place in `ComfyUI/models/vae/`

**CLIP Vision**

## clip_vision_h.safetensors

CLIP Vision model for image conditioning. Place in `ComfyUI/models/clip_vision/`

File storage locations:
    
    
    ComfyUI/
    ├── models/
    │   ├── diffusion_models/
    │   │   └── ... (download per workflow below)
    │   ├── text_encoders/
    │   │   └── umt5_xxl_fp8_e4m3fn_scaled.safetensors
    │   ├── vae/
    │   │   └── wan_2.1_vae.safetensors
    │   └── clip_vision/
    │       └── clip_vision_h.safetensors
    

For diffusion models, we’ll use the fp16 precision models in this guide because we’ve found that they perform better than the bf16 versions. If you need other precision versions, please visit [here](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files/diffusion_models) to download them.

## 

​

Wan2.1 Text-to-Video Workflow (1.3B)

### 

​

Wan 2.1 Text to Video

Generate videos from text prompts using Wan 2.1. ![Wan 2.1 Text to Video workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/text_to_video_wan-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Wan 2.1 Text to Video” in Template Library

### 

​

Model Downloads

## wan2.1_t2v_1.3B_fp16.safetensors

Diffusion model for Wan2.1 Text-to-Video. Place in `ComfyUI/models/diffusion_models/`

> If you need other t2v precision versions, please visit [here](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files/diffusion_models) to download them.

### 

​

Steps to Run

![ComfyUI Wan2.1 Workflow Steps](https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2.1_t2v_1.3b_flow_diagram.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=db6d32906ab2db132e6b92fdb0823419)

  1. Make sure the `Load Diffusion Model` node has loaded the `wan2.1_t2v_1.3B_fp16.safetensors` model
  2. Make sure the `Load CLIP` node has loaded the `umt5_xxl_fp8_e4m3fn_scaled.safetensors` model
  3. Make sure the `Load VAE` node has loaded the `wan_2.1_vae.safetensors` model
  4. (Optional) You can modify the video dimensions in the `EmptyHunyuanLatentVideo` node if needed
  5. (Optional) If you need to modify the prompts (positive and negative), make changes in the `CLIP Text Encoder` node at number `5`
  6. Click the `Run` button or use the shortcut `Ctrl(cmd) + Enter` to execute the video generation



## 

​

Wan2.1 Image-to-Video Workflow (14B)

**Since Wan Video separates the 480P and 720P models** , we’ll need to provide examples for both resolutions in this guide. In addition to using different models, they also have slight parameter differences.

### 

​

480P Version

### 

​

Wan 2.1 Image to Video

Generate videos from images using Wan 2.1. ![Wan 2.1 Image to Video workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_to_video_wan-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Wan 2.1 Image to Video” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## image_to_video_wan_start_image.png

`LoadImage` node 52 · `image_to_video_wan_start_image.png`

![image_to_video_wan_start_image.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/image_to_video_wan_start_image.png)

#### 

​

Model Downloads

## wan2.1_i2v_480p_14B_fp16.safetensors

Diffusion model for Wan2.1 I2V 480P. Place in `ComfyUI/models/diffusion_models/`

#### 

​

Steps to Run

![ComfyUI Wan2.1 Workflow Steps](https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2.1_i2v_14b_480p_flow_diagram.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=91de28e61a2633cf39b3a52afc2a6459)

  1. Make sure the `Load Diffusion Model` node has loaded the `wan2.1_i2v_480p_14B_fp16.safetensors` model
  2. Make sure the `Load CLIP` node has loaded the `umt5_xxl_fp8_e4m3fn_scaled.safetensors` model
  3. Make sure the `Load VAE` node has loaded the `wan_2.1_vae.safetensors` model
  4. Make sure the `Load CLIP Vision` node has loaded the `clip_vision_h.safetensors` model
  5. Upload the provided input image in the `Load Image` node
  6. (Optional) Enter the video description content you want to generate in the `CLIP Text Encoder` node
  7. (Optional) You can modify the video dimensions in the `WanImageToVideo` node if needed
  8. Click the `Run` button or use the shortcut `Ctrl(cmd) + Enter` to execute the video generation



### 

​

720P Version

![Wan2.1 Image-to-Video Workflow 14B 720P](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/wan2.1/wan2.1_i2v_14b_720P.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download the workflow image and drag it into ComfyUI to load the workflow

## Input Image

Download the default input image, or use your own image.

#### 

​

Model Downloads

## wan2.1_i2v_720p_14B_fp16.safetensors

Diffusion model for Wan2.1 I2V 720P. Place in `ComfyUI/models/diffusion_models/`

#### 

​

Steps to Run

![ComfyUI Wan2.1 Workflow Steps](https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2.1_i2v_14b_720p_flow_diagram.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=c99af487f3164515ac1ffaf94f0add71)

  1. Make sure the `Load Diffusion Model` node has loaded the `wan2.1_i2v_720p_14B_fp16.safetensors` model
  2. Make sure the `Load CLIP` node has loaded the `umt5_xxl_fp8_e4m3fn_scaled.safetensors` model
  3. Make sure the `Load VAE` node has loaded the `wan_2.1_vae.safetensors` model
  4. Make sure the `Load CLIP Vision` node has loaded the `clip_vision_h.safetensors` model
  5. Upload the provided input image in the `Load Image` node
  6. (Optional) Enter the video description content you want to generate in the `CLIP Text Encoder` node
  7. (Optional) You can modify the video dimensions in the `WanImageToVideo` node if needed
  8. Click the `Run` button or use the shortcut `Ctrl(cmd) + Enter` to execute the video generation



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/video/wan/wan-video.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/video/wan/wan-video)

[Wan2.2 Fun Camera Control in ComfyUI: Camera Motion VideoPrevious](https://docs.comfy.org/tutorials/video/wan/wan2-2-fun-camera)[ComfyUI Wan2.1 InfiniteTalk Workflow ExampleNext](https://docs.comfy.org/tutorials/video/wan/wan-infinitetalk)

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
