---
url: https://docs.comfy.org/tutorials/video/wan/wan2-2-fun-camera/
title: Wan2.2 Fun Camera Control in ComfyUI: Camera Motion Video - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:47.601685+00:00
---

# Wan2.2 Fun Camera Control in ComfyUI: Camera Motion Video - ComfyUI

> Source: https://docs.comfy.org/tutorials/video/wan/wan2-2-fun-camera/

## On this page

  * Wan2.2 Fun Camera Control: Video Generation Workflow Example
    * 1\. Workflow and Asset Download
    * 2\. Model Links
    * 3\. Complete the Workflow Step-by-Step



Wan Video

# Wan2.2 Fun Camera Control in ComfyUI: Camera Motion Video

Copy pageCopy page

Generate video with preset camera moves in ComfyUI using Wan2.2-Fun-Camera-Control: pan and zoom in any direction, with a 4-step Lightning LoRA for faster runs.

Copy pageCopy page

**Wan2.2-Fun-Camera-Control** is a next-generation video generation and camera control model developed by Alibaba PAI. By introducing innovative Camera Control Codes and combining deep learning with multimodal conditional inputs, it generates high-quality videos that adhere to predefined camera motion conditions. The model is released under the **Apache 2.0 license** , allowing for commercial use. **Key Features** :

  * **Camera Motion Control** : Supports various camera motion modes, including **Pan Up** , **Pan Down** , **Pan Left** , **Pan Right** , **Zoom In** , **Zoom Out** , and combinations thereof.
  * **High-Quality Video Generation** : Based on the Wan2.2 architecture, it outputs cinematic-quality videos.

Here are the relevant model weights and code repository:

  * [🤗Wan2.2-Fun-A14B-Control-Camera](https://huggingface.co/alibaba-pai/Wan2.2-Fun-A14B-Control-Camera)
  * Code Repository: [VideoX-Fun](https://github.com/aigc-apps/VideoX-Fun)



## 

​

Wan2.2 Fun Camera Control: Video Generation Workflow Example

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

The workflow provided includes two versions:

  1. Using the [Wan2.2-Lightning](https://huggingface.co/lightx2v/Wan2.2-Lightning) 4-step LoRA via lightx2v: This may result in reduced video dynamics but offers faster generation.
  2. The fp8_scaled version without the acceleration LoRA.

Below are the timing results tested on an RTX4090D 24GB GPU for 640*640 resolution and 81-frame length:

Model Type| Resolution| VRAM Usage| First Generation Time| Second Generation Time  
---|---|---|---|---  
fp8_scaled| 640×640| 84%| ≈ 536 seconds| ≈ 513 seconds  
fp8_scaled + 4-step LoRA| 640×640| 89%| ≈ 108 seconds| ≈ 71 seconds  
  
While the 4-step LoRA improves initial user experience, it may reduce video dynamism. By default, the accelerated LoRA version is enabled. To switch workflows, select the nodes and press **Ctrl+B**.

### 

​

1\. Workflow and Asset Download

Download the video or JSON file below and drag it into ComfyUI to load the corresponding workflow. The workflow will prompt you to download the models. ![Wan2.2 Fun Camera Control workflow](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan2_2_14B_fun_camera-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Wan2.2 Fun Camera” in Template Library

Please download the image below, which we will use as input. **Input materials**

## video_wan2_2_14B_fun_camera_start_image.jpg

Starting frame for the video generation. Download and use this image, or replace with your own.

### 

​

2\. Model Links

The following models can be found in [Wan_2.2_ComfyUI_Repackaged](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged): **Diffusion Models**

## wan2.2_fun_camera_high_noise_14B_fp8_scaled.safetensors

High noise diffusion model for Wan2.2 Fun Camera

## wan2.2_fun_camera_low_noise_14B_fp8_scaled.safetensors

Low noise diffusion model for Wan2.2 Fun Camera

**Wan2.2-Lightning LoRA (Optional, for acceleration)**

## wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors

4-step acceleration LoRA for high noise model

## wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors

4-step acceleration LoRA for low noise model

**VAE**

## wan_2.1_vae.safetensors

Wan2.1 VAE for encoding/decoding

**Text Encoder**

## umt5_xxl_fp8_e4m3fn_scaled.safetensors

FP8 scaled text encoder

File save location
    
    
    ComfyUI/
    ├───📂 models/
    │   ├───📂 diffusion_models/
    │   │   ├─── wan2.2_fun_camera_low_noise_14B_fp8_scaled.safetensors
    │   │   └─── wan2.2_fun_camera_high_noise_14B_fp8_scaled.safetensors
    │   ├───📂 loras/
    │   │   ├─── wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors
    │   │   └─── wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors
    │   ├───📂 text_encoders/
    │   │   └─── umt5_xxl_fp8_e4m3fn_scaled.safetensors
    │   └───📂 vae/
    │       └── wan_2.1_vae.safetensors
    

### 

​

3\. Complete the Workflow Step-by-Step

![Wan2.2 Fun Camera Control Workflow Steps](https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan_2.2_14b_fun_camera.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=8fd9faf8734e1f53f4838d25bb7eb822)

This workflow uses LoRA. Ensure the Diffusion model and LoRA are consistent; high noise and low noise models and LoRA must be paired accordingly.

  1. **High noise** model and **LoRA** loading


  * Ensure the `Load Diffusion Model` node loads `wan2.2_fun_camera_high_noise_14B_fp8_scaled.safetensors`
  * Ensure the `LoraLoaderModelOnly` node loads `wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors`


  2. **Low noise** model and **LoRA** loading


  * Ensure the `Load Diffusion Model` node loads `wan2.2_fun_camera_low_noise_14B_fp8_scaled.safetensors`
  * Ensure the `LoraLoaderModelOnly` node loads `wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors`


  3. Ensure the `Load CLIP` node loads `umt5_xxl_fp8_e4m3fn_scaled.safetensors`
  4. Ensure the `Load VAE` node loads `wan_2.1_vae.safetensors`
  5. Upload the starting frame in the `Load Image` node
  6. Modify the Prompt (both Chinese and English are acceptable)
  7. Set camera control parameters in the `WanCameraEmbedding` node: 
     * **Camera Motion** : Select the camera motion type (Zoom In, Zoom Out, Pan Up, Pan Down, Pan Left, Pan Right, Static, etc.)
     * **Width/Height** : Set video resolution
     * **Length** : Set the number of video frames (default is 81 frames)
     * **Speed** : Set video speed (default is 1.0)
  8. Click the `Run` button or use the shortcut `Ctrl(cmd) + Enter` to execute video generation



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/video/wan/wan2-2-fun-camera.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/video/wan/wan2-2-fun-camera)

[Wan2.2 Fun Control in ComfyUI: Control-Video GenerationPrevious](https://docs.comfy.org/tutorials/video/wan/wan2-2-fun-control)[ComfyUI Wan2.1 Video ExamplesNext](https://docs.comfy.org/tutorials/video/wan/wan-video)

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
