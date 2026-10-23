---
url: https://docs.comfy.org/tutorials/video/wan/wan2-2-fun-inp/
title: Wan2.2 Fun InP in ComfyUI: Start and End Frame Video - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:47.934342+00:00
---

# Wan2.2 Fun InP in ComfyUI: Start and End Frame Video - ComfyUI

> Source: https://docs.comfy.org/tutorials/video/wan/wan2-2-fun-inp/

## On this page

  * ComfyOrg Wan2.2 Fun InP & Control Youtube Live Stream Replay
  * Wan2.2 Fun Inp Start-End Frame Video Generation Workflow Example
    * 1\. Download Workflow File
    * 2\. Models
    * 3\. Workflow Guide



Wan Video

# Wan2.2 Fun InP in ComfyUI: Start and End Frame Video

Copy pageCopy page

Run the Wan2.2 Fun InP 14B workflow in ComfyUI to generate video between a start and end frame, with high and low noise models and Lightning LoRAs.

Copy pageCopy page

**Wan2.2-Fun-Inp** is a start-end frame controlled video generation model launched by Alibaba PAI team. It supports inputting **start and end frame images** to generate intermediate transition videos, providing creators with greater creative control. The model is released under the **Apache 2.0 license** and supports commercial use. **Key Features** :

  * **Start-End Frame Control** : Supports inputting start and end frame images to generate intermediate transition videos, enhancing video coherence and creative freedom
  * **High-Quality Video Generation** : Based on the Wan2.2 architecture, outputs film-level quality videos
  * **Multi-Resolution Support** : Supports generating videos at 512x512, 768x768, 1024x1024 and other resolutions to suit different scenarios

**Model Version** :

  * **14B High-Performance Version** : Model size exceeds 32GB, with better results but requires high VRAM

Below are the relevant model weights and code repositories:

  * [🤗Wan2.2-Fun-Inp-14B](https://huggingface.co/alibaba-pai/Wan2.2-Fun-A14B-InP)
  * Code repository: [VideoX-Fun](https://github.com/aigc-apps/VideoX-Fun)



## 

​

ComfyOrg Wan2.2 Fun InP & Control Youtube Live Stream Replay

## 

​

Wan2.2 Fun Inp Start-End Frame Video Generation Workflow Example

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

  1. A version using [Wan2.2-Lightning](https://huggingface.co/lightx2v/Wan2.2-Lightning) 4-step LoRA from lightx2v for accelerated video generation
  2. A fp8_scaled version without acceleration LoRA

Below are the test results using an RTX4090D 24GB VRAM GPU at 640x640 resolution with 81 frames

Model Type| VRAM Usage| First Generation Time| Second Generation Time  
---|---|---|---  
fp8_scaled| 83%| ≈ 524s| ≈ 520s  
fp8_scaled + 4-step LoRA| 89%| ≈ 138s| ≈ 79s  
  
Since the acceleration with LoRA is significant but the video dynamic is lost, the provided workflows enable the accelerated LoRA version by default. If you want to enable the other workflow, select it and use **Ctrl+B** to activate.

### 

​

1\. Download Workflow File

Please update your ComfyUI to the latest version, and find “**Wan2.2 Fun Inp** ” under the menu `Workflow` -> `Browse Templates` -> `Video` to load the workflow. Or, after updating ComfyUI to the latest version, download the workflow below and drag it into ComfyUI to load. ![Wan2.2 Fun Inp workflow](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan2_2_14B_fun_inpaint-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Wan2.2 Fun Inp” in Template Library

Use the following materials as the start and end frames **Input materials**

## video_wan2_2_14B_fun_inpaint_start_image.png

Start frame for video generation. Download and use this image, or replace with your own.

## video_wan2_2_14B_fun_inpaint_end_image.png

End frame for video generation. Download and use this image, or replace with your own.

### 

​

2\. Models

All models involved in this guide can be found [here](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/tree/main/split_files). **Diffusion Models**

## High Noise 14B FP8 Scaled

wan2.2_fun_inpaint_high_noise_14B_fp8_scaled.safetensors: High noise diffusion model for start-end frame inpainting

## Low Noise 14B FP8 Scaled

wan2.2_fun_inpaint_low_noise_14B_fp8_scaled.safetensors: Low noise diffusion model for start-end frame inpainting

**Lightning LoRA (Optional, for acceleration)**

## Lightning 4-Step High Noise LoRA

wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors: 4-step acceleration LoRA for high noise model

## Lightning 4-Step Low Noise LoRA

wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors: 4-step acceleration LoRA for low noise model

**VAE**

## Wan2.1 VAE

wan_2.1_vae.safetensors: Wan2.1 VAE for encoding and decoding

**Text Encoder**

## UMT5 XXL FP8 Scaled

umt5_xxl_fp8_e4m3fn_scaled.safetensors: Scaled FP8 text encoder
    
    
    ComfyUI/
    ├───📂 models/
    │   ├───📂 diffusion_models/
    │   │   ├─── wan2.2_fun_inpaint_high_noise_14B_fp8_scaled.safetensors
    │   │   └─── wan2.2_fun_inpaint_low_noise_14B_fp8_scaled.safetensors
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

![Workflow Step Image](https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_fun_inp.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=3d87de35d3eaa2f9599c35e9963c6c18)

This workflow uses LoRA. Please make sure the corresponding Diffusion model and LoRA are matched.

  1. **High noise** model and **LoRA** loading 
     * Ensure the `Load Diffusion Model` node loads the `wan2.2_fun_inpaint_high_noise_14B_fp8_scaled.safetensors` model
     * Ensure the `LoraLoaderModelOnly` node loads the `wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors`
  2. **Low noise** model and **LoRA** loading 
     * Ensure the `Load Diffusion Model` node loads the `wan2.2_fun_inpaint_low_noise_14B_fp8_scaled.safetensors` model
     * Ensure the `LoraLoaderModelOnly` node loads the `wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors`
  3. Ensure the `Load CLIP` node loads the `umt5_xxl_fp8_e4m3fn_scaled.safetensors` model
  4. Ensure the `Load VAE` node loads the `wan_2.1_vae.safetensors` model
  5. Upload the start and end frame images as materials
  6. Enter your prompt in the Prompt group
  7. Adjust the size and video length in the `WanFunInpaintToVideo` node 
     * Adjust the `width` and `height` parameters. The default is `640`. We set a smaller size, but you can modify it as needed.
     * Adjust the `length`, which is the total number of frames. The current workflow fps is 16. For example, if you want to generate a 5-second video, you should set it to 5*16 = 80.
  8. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to execute video generation



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/video/wan/wan2-2-fun-inp.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/video/wan/wan2-2-fun-inp)

[Wan2.2-S2V in ComfyUI: Audio-Driven Video GenerationPrevious](https://docs.comfy.org/tutorials/video/wan/wan2-2-s2v)[Wan2.2 Fun Control in ComfyUI: Control-Video GenerationNext](https://docs.comfy.org/tutorials/video/wan/wan2-2-fun-control)

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
