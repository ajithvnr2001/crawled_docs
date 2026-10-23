---
url: https://docs.comfy.org/tutorials/video/wan/wan2-2-fun-control/
title: Wan2.2 Fun Control in ComfyUI: Control-Video Generation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:47.755708+00:00
---

# Wan2.2 Fun Control in ComfyUI: Control-Video Generation - ComfyUI

> Source: https://docs.comfy.org/tutorials/video/wan/wan2-2-fun-control/

## On this page

  * ComfyOrg Wan2.2 Fun InP & Control Youtube Live Stream Replay
  * Wan2.2 Fun Control Video Generation Workflow Example
    * 1\. Download Workflow and Materials
    * 2\. Models
    * 3\. Workflow Guide
    * Additional Notes



Wan Video

# Wan2.2 Fun Control in ComfyUI: Control-Video Generation

Copy pageCopy page

Run the Wan2.2 Fun Control 14B workflow in ComfyUI to generate video guided by a control video, with high and low noise models and 4-step LoRAs.

Copy pageCopy page

**Wan2.2-Fun-Control** is a next-generation video generation and control model launched by Alibaba PAI team. Through innovative Control Codes mechanism combined with deep learning and multi-modal conditional inputs, it can generate high-quality videos that comply with preset control conditions. The model is released under the **Apache 2.0 license** and supports commercial use. **Key Features** :

  * **Multi-modal Control** : Supports multiple control conditions including **Canny (line art)** , **Depth** , **OpenPose (human pose)** , **MLSD (geometric edges)** , and **trajectory control**
  * **High-Quality Video Generation** : Based on the Wan2.2 architecture, outputs film-level quality videos
  * **Multi-language Support** : Supports multi-language prompts including Chinese and English

Below are the relevant model weights and code repositories:

  * [🤗Wan2.2-Fun-A14B-Control](https://huggingface.co/alibaba-pai/Wan2.2-Fun-A14B-Control)
  * Code repository: [VideoX-Fun](https://github.com/aigc-apps/VideoX-Fun)



## 

​

ComfyOrg Wan2.2 Fun InP & Control Youtube Live Stream Replay

## 

​

Wan2.2 Fun Control Video Generation Workflow Example

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

This workflow provides two versions:

  1. A version using [Wan2.2-Lightning](https://huggingface.co/lightx2v/Wan2.2-Lightning) 4-step LoRA from lightx2v: may cause some loss in video dynamics but offers faster speed
  2. A fp8_scaled version without acceleration LoRA

Below are the test results using an RTX4090D 24GB VRAM GPU at 640×640 resolution with 81 frames

Model Type| VRAM Usage| First Generation Time| Second Generation Time  
---|---|---|---  
fp8_scaled| 83%| ≈ 524s| ≈ 520s  
fp8_scaled + 4-step LoRA| 89%| ≈ 138s| ≈ 79s  
  
Since using the 4-step LoRA provides a better experience for first-time workflow users, but may cause some loss in video dynamics, we have enabled the accelerated LoRA version by default. If you want to enable the other workflow, select it and use **Ctrl+B** to activate.

### 

​

1\. Download Workflow and Materials

Update your ComfyUI to the latest version, then download and drag the workflow file into ComfyUI, or find “Wan2.2 Fun Control” in the Template Library under `Workflow` → `Browse Templates` → `Video`. ![Wan2.2 Fun Control workflow](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan2_2_14B_fun_control-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Wan2.2 Fun Control” in Template Library

Please download the following images and videos as input materials. **Input materials**

## video_wan2_2_14B_fun_control_start_image.jpg

Start frame for video generation. Download and use this image, or replace with your own.

## video_wan2_2_14B_fun_control_start_image_control_video.mp4

Preprocessed pose control video. Download and use this video, or replace with your own.

> We use a preprocessed video here.

### 

​

2\. Models

All models involved in this guide can be found [here](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/tree/main/split_files). **Diffusion Models**

## Wan2.2 Fun Control High Noise 14B FP8

wan2.2_fun_control_high_noise_14B_fp8_scaled.safetensors: High noise diffusion model

## Wan2.2 Fun Control Low Noise 14B FP8

wan2.2_fun_control_low_noise_14B_fp8_scaled.safetensors: Low noise diffusion model

**Wan2.2-Lightning LoRA (Optional, for acceleration)**

## High Noise 4-Step LoRA

wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors: High noise 4-step acceleration LoRA

## Low Noise 4-Step LoRA

wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors: Low noise 4-step acceleration LoRA

**VAE**

## Wan2.1 VAE

wan_2.1_vae.safetensors: Wan2.1 VAE for encoding/decoding

**Text Encoder**

## UMT5 XXL FP8 Scaled

umt5_xxl_fp8_e4m3fn_scaled.safetensors: Scaled FP8 text encoder
    
    
    ComfyUI/
    ├───📂 models/
    │   ├───📂 diffusion_models/
    │   │   ├─── wan2.2_fun_control_low_noise_14B_fp8_scaled.safetensors
    │   │   └─── wan2.2_fun_control_high_noise_14B_fp8_scaled.safetensors
    │   ├───📂 loras/
    │   │   ├─── wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors
    │   │   └─── wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors
    │   ├───📂 text_encoders/
    │   │   └─── umt5_xxl_fp8_e4m3fn_scaled.safetensors 
    │   └───📂 vae/
    │       └── wan_2.1_vae.safetensors
    

### 

​

3\. Workflow Guide

![Wan2.2 Fun Control Workflow Steps](https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_fun_control.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=1c5d26bea52f7f790ac6059e7a195c8d)

This workflow uses LoRA. Please ensure the corresponding Diffusion model and LoRA are matched: high noise and low noise models and LoRAs need to be used correspondingly.

  1. **High noise** model and **LoRA** loading 
     * Ensure the `Load Diffusion Model` node loads the `wan2.2_fun_control_high_noise_14B_fp8_scaled.safetensors` model
     * Ensure the `LoraLoaderModelOnly` node loads the `wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors`
  2. **Low noise** model and **LoRA** loading 
     * Ensure the `Load Diffusion Model` node loads the `wan2.2_fun_control_low_noise_14B_fp8_scaled.safetensors` model
     * Ensure the `LoraLoaderModelOnly` node loads the `wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors`
  3. Ensure the `Load CLIP` node loads the `umt5_xxl_fp8_e4m3fn_scaled.safetensors` model
  4. Ensure the `Load VAE` node loads the `wan_2.1_vae.safetensors` model
  5. Upload the start frame in the `Load Image` node
  6. In the second `Load video` node, load the pose control video. The provided video has been preprocessed and can be used directly
  7. Since we provide a preprocessed pose video, the corresponding video image preprocessing node needs to be disabled. You can select it and use `Ctrl + B` to disable it
  8. Modify the Prompt: you can use both Chinese and English
  9. In `Wan22FunControlToVideo`, modify the video dimensions. The default is set to 640×640 resolution to avoid excessive processing time for users with low VRAM
  10. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to execute video generation



### 

​

Additional Notes

Since ComfyUI’s built-in nodes only include Canny preprocessor, you can use tools like [ComfyUI-comfyui_controlnet_aux](https://github.com/Fannovel16/comfyui_controlnet_aux) to implement other types of image preprocessing

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/video/wan/wan2-2-fun-control.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/video/wan/wan2-2-fun-control)

[Wan2.2 Fun InP in ComfyUI: Start and End Frame VideoPrevious](https://docs.comfy.org/tutorials/video/wan/wan2-2-fun-inp)[Wan2.2 Fun Camera Control in ComfyUI: Camera Motion VideoNext](https://docs.comfy.org/tutorials/video/wan/wan2-2-fun-camera)

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
