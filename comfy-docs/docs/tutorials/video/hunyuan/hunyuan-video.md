---
url: https://docs.comfy.org/tutorials/video/hunyuan/hunyuan-video/
title: ComfyUI Hunyuan Video Examples - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:43.170942+00:00
---

# ComfyUI Hunyuan Video Examples - ComfyUI

> Source: https://docs.comfy.org/tutorials/video/hunyuan/hunyuan-video/

## On this page

  * Common Models for All Workflows
  * Hunyuan Text-to-Video Workflow
    * 1\. Workflow
    * 2\. Manual models installation
    * 3\. Steps to run the workflow
  * Hunyuan Image-to-Video Workflow
    * Shared Model for v1 and v2 Versions
    * V1 “concat” Image-to-Video Workflow
    * 1\. Workflow and Asset
    * 2\. Related models manual installation
    * 3\. Steps to run the workflow
    * v2 “replace” Image-to-Video Workflow
    * 1\. Workflow and Asset
    * 2\. Related models manual installation
    * 3\. Steps to run the workflow
  * Try It Yourself



Hunyuan

# ComfyUI Hunyuan Video Examples

Copy pageCopy page

This guide shows how to use Hunyuan Text-to-Video and Image-to-Video workflows in ComfyUI

Copy pageCopy page

Hunyuan Video series is developed and open-sourced by [Tencent](https://huggingface.co/tencent), featuring a hybrid architecture that supports both [Text-to-Video](https://github.com/Tencent/HunyuanVideo) and [Image-to-Video](https://github.com/Tencent/HunyuanVideo-I2V) generation with a parameter scale of 13B. Technical features:

  * **Core Architecture:** Uses a DiT (Diffusion Transformer) architecture similar to Sora, effectively fusing text, image, and motion information to improve consistency, quality, and alignment between generated video frames. A unified full-attention mechanism enables multi-view camera transitions while ensuring subject consistency.
  * **3D VAE:** The custom 3D VAE compresses videos into a compact latent space, making image-to-video generation more efficient.
  * **Superior Image-Video-Text Alignment:** Utilizing MLLM text encoders that excel in both image and video generation, better following text instructions, capturing details, and performing complex reasoning.

You can learn more through the official repositories: [Hunyuan Video](https://github.com/Tencent/HunyuanVideo) and [Hunyuan Video-I2V](https://github.com/Tencent/HunyuanVideo-I2V). This guide will walk you through setting up both **Text-to-Video** and **Image-to-Video** workflows in ComfyUI.

The workflow images in this tutorial contain metadata with model download information.Simply drag them into ComfyUI or use the menu `Workflows` -> `Open (ctrl+o)` to load the corresponding workflow, which will prompt you to download the required models.Alternatively, this guide provides direct model links if automatic downloads fail or you are not using the Desktop version. All models are available [here](https://huggingface.co/Comfy-Org/HunyuanVideo_repackaged/tree/main/split_files) for download.

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

Common Models for All Workflows

The following models are used in both Text-to-Video and Image-to-Video workflows. Download and save them to the specified directories:

## Text Encoder: clip_l.safetensors

Save to ComfyUI/models/text_encoders

## Text Encoder: llava_llama3_fp8_scaled.safetensors

Save to ComfyUI/models/text_encoders

## VAE: hunyuan_video_vae_bf16.safetensors

Save to ComfyUI/models/vae

Storage location:
    
    
    ComfyUI/
    ├── models/
    │   ├── text_encoders/
    │   │   ├── clip_l.safetensors
    │   │   └── llava_llama3_fp8_scaled.safetensors
    │   └── vae/
    │       └── hunyuan_video_vae_bf16.safetensors
    

## 

​

Hunyuan Text-to-Video Workflow

Hunyuan Text-to-Video was open-sourced in December 2024, supporting 5-second short video generation through natural language descriptions in both Chinese and English.

### 

​

1\. Workflow

Download the workflow image below and drag it into ComfyUI to load the workflow: ![ComfyUI Workflow - Hunyuan Text-to-Video](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/hunyuan_video_text_to_video-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Hunyuan Video” in Template Library

### 

​

2\. Manual models installation

## Diffusion Model: hunyuan_video_t2v_720p_bf16.safetensors

Save to ComfyUI/models/diffusion_models

Ensure you have all these model files in the correct locations:
    
    
    ComfyUI/
    ├── models/
    │   ├── text_encoders/
    │   │   ├── clip_l.safetensors                       // Shared model
    │   │   └── llava_llama3_fp8_scaled.safetensors      // Shared model
    │   ├── vae/
    │   │   └── hunyuan_video_vae_bf16.safetensors       // Shared model
    │   └── diffusion_models/
    │       └── hunyuan_video_t2v_720p_bf16.safetensors  // T2V model
    

### 

​

3\. Steps to run the workflow

![ComfyUI Hunyuan Video T2V Workflow](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/flow_diagram_t2v.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=8cf9db23e82c1c31702966878d7d6326)

  1. Ensure the `DualCLIPLoader` node has loaded these models: 
     * clip_name1: clip_l.safetensors
     * clip_name2: llava_llama3_fp8_scaled.safetensors
  2. Ensure the `Load Diffusion Model` node has loaded `hunyuan_video_t2v_720p_bf16.safetensors`
  3. Ensure the `Load VAE` node has loaded `hunyuan_video_vae_bf16.safetensors`
  4. Click the `Queue` button or use the shortcut `Ctrl(cmd) + Enter` to run the workflow



When the `length` parameter in the `EmptyHunyuanLatentVideo` node is set to 1, the model can generate a static image.

## 

​

Hunyuan Image-to-Video Workflow

Hunyuan Image-to-Video model was open-sourced on March 6, 2025, based on the HunyuanVideo framework. It transforms static images into smooth, high-quality videos and also provides LoRA training code to customize special video effects like hair growth, object transformation, and more. Currently, the Hunyuan Image-to-Video model has two versions:

  * v1 “concat”: Better motion fluidity but less adherence to the image guidance
  * v2 “replace”: Updated the day after v1, with better image guidance but seemingly less dynamic compared to v1



v1 “concat”

![HunyuanVideo v1](https://comfyanonymous.github.io/ComfyUI_examples/hunyuan_video/hunyuan_video_image_to_video.webp)

v2 “replace”

![HunyuanVideo v2](https://comfyanonymous.github.io/ComfyUI_examples/hunyuan_video/hunyuan_video_image_to_video_v2.webp)

### 

​

Shared Model for v1 and v2 Versions

## CLIP Vision: llava_llama3_vision.safetensors

Save to ComfyUI/models/clip_vision

### 

​

V1 “concat” Image-to-Video Workflow

#### 

​

1\. Workflow and Asset

Download the workflow image below and drag it into ComfyUI to load the workflow: ![ComfyUI Workflow - Hunyuan Image-to-Video v1](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/hunyuan-video/i2v/v1_robot.webp)

## Download Workflow

Download the workflow image and drag into ComfyUI

Download the image below and use it as the starting frame for the image-to-video generation:

## Starting Frame: robot-ballet.png

Save and use as input image for I2V generation

#### 

​

2\. Related models manual installation

## Diffusion Model: hunyuan_video_image_to_video_720p_bf16.safetensors

Save to ComfyUI/models/diffusion_models

Ensure you have all these model files in the correct locations:
    
    
    ComfyUI/
    ├── models/
    │   ├── clip_vision/
    │   │   └── llava_llama3_vision.safetensors                     // I2V shared model
    │   ├── text_encoders/
    │   │   ├── clip_l.safetensors                                  // Shared model
    │   │   └── llava_llama3_fp8_scaled.safetensors                 // Shared model
    │   ├── vae/
    │   │   └── hunyuan_video_vae_bf16.safetensors                  // Shared model
    │   └── diffusion_models/
    │       └── hunyuan_video_image_to_video_720p_bf16.safetensors  // I2V v1 "concat" version model
    

#### 

​

3\. Steps to run the workflow

![ComfyUI Hunyuan Video I2V v1 Workflow](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/flow_diagram_i2v_v1.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=66d1fd271cc2a45a4fbcd92850074912)

  1. Ensure that `DualCLIPLoader` has loaded these models: 
     * clip_name1: clip_l.safetensors
     * clip_name2: llava_llama3_fp8_scaled.safetensors
  2. Ensure that `Load CLIP Vision` has loaded `llava_llama3_vision.safetensors`
  3. Ensure that `Load Image Model` has loaded `hunyuan_video_image_to_video_720p_bf16.safetensors`
  4. Ensure that `Load VAE` has loaded `vae_name: hunyuan_video_vae_bf16.safetensors`
  5. Ensure that `Load Diffusion Model` has loaded `hunyuan_video_image_to_video_720p_bf16.safetensors`
  6. Click the `Queue` button or use the shortcut `Ctrl(cmd) + Enter` to run the workflow



### 

​

v2 “replace” Image-to-Video Workflow

The v2 workflow is essentially the same as the v1 workflow. You just need to download the **replace** model and use it in the `Load Diffusion Model` node.

#### 

​

1\. Workflow and Asset

Download the workflow image below and drag it into ComfyUI to load the workflow: ![ComfyUI Workflow - Hunyuan Image-to-Video v2](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/hunyuan-video/i2v/v2_fennec_gril.webp)

## Download Workflow

Download the workflow image and drag into ComfyUI

Download the image below and use it as the starting frame for the image-to-video generation:

## Starting Frame: flux_dev_example.png

Save and use as input image for I2V generation

#### 

​

2\. Related models manual installation

## Diffusion Model: hunyuan_video_v2_replace_image_to_video_720p_bf16.safetensors

Save to ComfyUI/models/diffusion_models

Ensure you have all these model files in the correct locations:
    
    
    ComfyUI/
    ├── models/
    │   ├── clip_vision/
    │   │   └── llava_llama3_vision.safetensors                                // I2V shared model
    │   ├── text_encoders/
    │   │   ├── clip_l.safetensors                                             // Shared model
    │   │   └── llava_llama3_fp8_scaled.safetensors                            // Shared model
    │   ├── vae/
    │   │   └── hunyuan_video_vae_bf16.safetensors                             // Shared model
    │   └── diffusion_models/
    │       └── hunyuan_video_v2_replace_image_to_video_720p_bf16.safetensors  // V2 "replace" version model
    

#### 

​

3\. Steps to run the workflow

![ComfyUI Hunyuan Video I2V v2 Workflow](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/flow_diagram_i2v_v2.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=f26ddd8edc837fbf9d2bb4f6459a82ee)

  1. Ensure the `DualCLIPLoader` node has loaded these models: 
     * clip_name1: clip_l.safetensors
     * clip_name2: llava_llama3_fp8_scaled.safetensors
  2. Ensure the `Load CLIP Vision` node has loaded `llava_llama3_vision.safetensors`
  3. Ensure the `Load Image Model` node has loaded `hunyuan_video_image_to_video_720p_bf16.safetensors`
  4. Ensure the `Load VAE` node has loaded `hunyuan_video_vae_bf16.safetensors`
  5. Ensure the `Load Diffusion Model` node has loaded `hunyuan_video_v2_replace_image_to_video_720p_bf16.safetensors`
  6. Click the `Queue` button or use the shortcut `Ctrl(cmd) + Enter` to run the workflow



## 

​

Try It Yourself

Here are some images and prompts we provide. Use them as-is or adjust to create your own video. ![example](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/humanoid_android_dressed_in_a_flowing.png?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=16d6b0ea15e14c74e8d2e5bfacfe4bf8)
    
    
    Futuristic robot dancing ballet, dynamic motion, fast motion, fast shot, moving scene
    

* * *

![example](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/samurai.png?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=f8a76a691a7a9ebda088941350538375)
    
    
    Samurai waving sword and hitting the camera. camera angle movement, zoom in, fast scene, super fast, dynamic
    

* * *

![example](https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hunyuanvideo/a_flying_car.png?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=aa2ce4f30c4d367170a8a696e62a7c7e)
    
    
    flying car fastly moving and flying through the city
    

* * *

![example](https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hunyuanvideo/cyber_car_race.png?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=875b086bd33ac131bda4fe6c718b9bc7)
    
    
    cyberpunk car race in night city, dynamic, super fast, fast shot
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/video/hunyuan/hunyuan-video.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/video/hunyuan/hunyuan-video)

[Bernini-R in ComfyUI: In-Context Image and Video EditingPrevious](https://docs.comfy.org/tutorials/video/bytedance/bernini-r)[HunyuanVideo 1.5Next](https://docs.comfy.org/tutorials/video/hunyuan/hunyuan-video-1-5)

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
