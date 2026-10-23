---
url: https://docs.comfy.org/tutorials/video/wan/fun-inp/
title: Wan2.1 Fun InP in ComfyUI: First and Last Frame Video - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:45.710982+00:00
---

# Wan2.1 Fun InP in ComfyUI: First and Last Frame Video - ComfyUI

> Source: https://docs.comfy.org/tutorials/video/wan/fun-inp/

## On this page

  * About Wan2.1-Fun-InP
  * Wan2.1 Fun InP Workflow
    * 1\. Download Workflow
    * 2\. Manual Model Installation
    * 3\. Complete the Workflow Step by Step
    * 4\. Workflow Notes
  * Other Wan2.1 Fun InP or video-related custom node packages



Wan2.1

# Wan2.1 Fun InP in ComfyUI: First and Last Frame Video

Copy pageCopy page

Run the Wan2.1 Fun InP workflow in ComfyUI to generate video between a start and end frame, with 1.3B and 14B model options and full setup steps.

Copy pageCopy page

**Wan2.1 Fun InP** is an open-source video generation model in Alibaba’s Wan2.1-Fun series. You provide a first and last frame image, and it generates the transition video between them with stable, coherent motion. This guide covers the official ComfyUI workflow for Wan2.1 Fun InP, available in lightweight 1.3B and high-performance 14B versions, with model downloads and step-by-step generation instructions.

## 

​

About Wan2.1-Fun-InP

**Wan-Fun InP** is an open-source video generation model released by Alibaba, part of the Wan2.1-Fun series, focusing on generating videos from images with first and last frame control. **Key features** :

  * **First and last frame control** : Supports inputting both first and last frame images to generate transitional video between them, enhancing video coherence and creative freedom. Compared to earlier community versions, Alibaba’s official model produces more stable and significantly higher quality results.
  * **Multi-resolution support** : Supports generating videos at 512x512, 768x768, 1024x1024 and other resolutions to accommodate different scenario requirements.

**Model versions** :

  * **1.3B** Lightweight: Suitable for local deployment and quick inference with **lower VRAM requirements**
  * **14B** High-performance: Model size reaches 32GB+, offering better results but requiring **higher VRAM**

Below are the relevant model weights and code repositories:

  * [Wan2.1-Fun-1.3B-Input](https://huggingface.co/alibaba-pai/Wan2.1-Fun-1.3B-Input)
  * [Wan2.1-Fun-14B-Input](https://huggingface.co/alibaba-pai/Wan2.1-Fun-14B-Input)
  * Code repository: [VideoX-Fun](https://github.com/aigc-apps/VideoX-Fun)



Currently, ComfyUI natively supports the Wan2.1 Fun InP model. Before starting this tutorial, please update your ComfyUI to ensure your version is after [this commit](https://github.com/Comfy-Org/ComfyUI/commit/0a1f8869c9998bbfcfeb2e97aa96a6d3e0a2b5df).

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

Wan2.1 Fun InP Workflow

### 

​

1\. Download Workflow

Download the image below and drag it into ComfyUI to load the workflow: ![Wan2.1 Fun InP Workflow](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/wan2.1_fun_inp-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Wan 2.1 Inpainting” in Template Library

## Start Image

Starting frame for the video generation. Download and use this image, or replace with your own.

## End Image

Ending frame for the video generation. Download and use this image, or replace with your own.

### 

​

2\. Manual Model Installation

If automatic model downloading is ineffective, please download the models manually and save them to the corresponding folders. All models involved in this guide can be found at [Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) and [Wan2.1-Fun](https://huggingface.co/collections/alibaba-pai/wan21-fun-67e4fb3b76ca01241eb7e334). **Diffusion Models** : Choose 1.3B or 14B. The 14B version has a larger file size (32GB) and higher VRAM requirements:

## Diffusion Model: Wan2.1 Fun InP 1.3B

`models/diffusion_models/wan2.1_fun_inp_1.3B_bf16.safetensors`

## Diffusion Model: Wan2.1 Fun InP 14B

`models/diffusion_models/Wan2.1-Fun-14B-InP.safetensors` (rename after download)

**Text Encoders** : Choose one of the following models (fp16 precision has a larger size and higher performance requirements):

## Text Encoder: umt5_xxl_fp16

`models/text_encoders/umt5_xxl_fp16.safetensors`

## Text Encoder: umt5_xxl_fp8

`models/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors`

**VAE**

## VAE: wan_2.1_vae

`models/vae/wan_2.1_vae.safetensors`

**CLIP Vision**

## CLIP Vision: clip_vision_h

`models/clip_vision/clip_vision_h.safetensors`

File storage location:
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   ├── wan2.1_fun_inp_1.3B_bf16.safetensors
    │   │   └── Wan2.1-Fun-14B-InP.safetensors
    │   ├── 📂 text_encoders/
    │   │   ├── umt5_xxl_fp16.safetensors
    │   │   └── umt5_xxl_fp8_e4m3fn_scaled.safetensors
    │   ├── 📂 vae/
    │   │   └── wan_2.1_vae.safetensors
    │   └── 📂 clip_vision/
    │       └── clip_vision_h.safetensors
    

### 

​

3\. Complete the Workflow Step by Step

![ComfyUI Wan2.1 Fun InP Video Generation Workflow Diagram](https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/fun_inp_flow_diagram.png?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=421176e8ecfb5b00bfc56979f396e249)

  1. Ensure the `Load Diffusion Model` node has loaded `wan2.1_fun_inp_1.3B_bf16.safetensors`
  2. Ensure the `Load CLIP` node has loaded `umt5_xxl_fp8_e4m3fn_scaled.safetensors`
  3. Ensure the `Load VAE` node has loaded `wan_2.1_vae.safetensors`
  4. Ensure the `Load CLIP Vision` node has loaded `clip_vision_h.safetensors`
  5. Upload the starting frame to the `Load Image` node (renamed to `Start_image`)
  6. Upload the ending frame to the second `Load Image` node
  7. (Optional) Modify the prompt (both English and Chinese are supported)
  8. (Optional) Adjust the video size in `WanFunInpaintToVideo`, avoiding overly large dimensions
  9. Click the `Run` button or use the shortcut `Ctrl(cmd) + Enter` to execute video generation



### 

​

4\. Workflow Notes

Please make sure to use the correct model, as `wan2.1_fun_inp_1.3B_bf16.safetensors` and `wan2.1_fun_control_1.3B_bf16.safetensors` are stored in the same folder and have very similar names. Ensure you are using the right model.

  * When using Wan Fun InP, you may need to frequently modify prompts to ensure the accuracy of the corresponding scene transitions.



## 

​

Other Wan2.1 Fun InP or video-related custom node packages

  * [ComfyUI-VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite)
  * [ComfyUI-WanVideoWrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper)
  * [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes)



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/video/wan/fun-inp.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/video/wan/fun-inp)

[ComfyUI Wan2.1 Fun Camera Official ExamplesPrevious](https://docs.comfy.org/tutorials/video/wan/fun-camera)[Wan2.1 FLF2V in ComfyUI: First and Last Frame Video GenerationNext](https://docs.comfy.org/tutorials/video/wan/wan-flf)

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
