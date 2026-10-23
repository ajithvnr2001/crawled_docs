---
url: https://docs.comfy.org/tutorials/video/wan/wan-ati/
title: Wan ATI Native Workflow - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:46.005605+00:00
---

# Wan ATI Native Workflow - ComfyUI

> Source: https://docs.comfy.org/tutorials/video/wan/wan-ati/

## On this page

  * Key Features
  * WAN ATI Trajectory Control Workflow Example
    * 1\. Workflow Download
    * 2\. Manual Model Installation
    * 3\. Complete the Workflow Execution Step by Step



Wan2.1

# Wan ATI Native Workflow

Copy pageCopy page

Wan ATI trajectory control in ComfyUI: draw trajectories to direct object, region, and camera motion in generated video, built on Wan2.1.

Copy pageCopy page

**ATI (Any Trajectory Instruction)** is a controllable video generation framework proposed by the ByteDance team. ATI is implemented based on Wan2.1 and supports unified control of objects, local regions, and camera motion in videos through arbitrary trajectory instructions.

## Project Repository

ATI source code and documentation on GitHub

## Online Trajectory Editing Tool

Visual tool to draw and edit motion trajectories on images

## 

​

Key Features

  * **Unified Motion Control** : Supports trajectory control for multiple motion types including objects, local regions, and camera movements.
  * **Interactive Trajectory Editor** : Visual tool that allows users to freely draw and edit motion trajectories on images.
  * **Wan2.1 Compatible** : Based on the official Wan2.1 implementation, compatible with environments and model structures.
  * **Rich Visualization Tools** : Supports visualization of input trajectories, output videos, and trajectory overlays.



## 

​

WAN ATI Trajectory Control Workflow Example

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

### 

​

1\. Workflow Download

Update your ComfyUI to the latest version, then download and drag the workflow file into ComfyUI, or find “Wan2.1 ATI” in the Template Library under `Workflow` → `Browse Templates` → `Video`. ![Wan2.1 ATI Workflow Preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan_ati-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Wan2.1 ATI” in Template Library

We will use the following image as input:

## Input Image: video_wan_ati_input_image.jpg

Download the default input image, or use your own image as the starting frame.

### 

​

2\. Manual Model Installation

All models involved in this guide can be found [here](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files). **Diffusion Model** : Choose one version:

## Diffusion Model: Wan2_1-I2V-ATI-14B_fp8_e4m3fn.safetensors

Wan2.1 I2V ATI 14B diffusion model (fp8 precision). Place in `ComfyUI/models/diffusion_models/`

**Text Encoders** : Choose one version:

## Text Encoder: umt5_xxl_fp16.safetensors

Full precision text encoder (higher quality, larger size). Place in `ComfyUI/models/text_encoders/`

## Text Encoder: umt5_xxl_fp8_e4m3fn_scaled.safetensors

FP8 text encoder (lower VRAM usage). Place in `ComfyUI/models/text_encoders/`

**VAE**

## VAE: wan_2.1_vae.safetensors

Wan2.1 VAE model. Place in `ComfyUI/models/vae/`

**CLIP Vision**

## CLIP Vision: clip_vision_h.safetensors

CLIP Vision model for processing reference images. Place in `ComfyUI/models/clip_vision/`

**File Storage Location**
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   └── Wan2_1-I2V-ATI-14B_fp8_e4m3fn.safetensors
    │   ├── 📂 text_encoders/
    │   │   └── umt5_xxl_fp8_e4m3fn_scaled.safetensors  # or your chosen version
    │   ├── 📂 clip_vision/
    │   │   └── clip_vision_h.safetensors
    │   └── 📂 vae/
    │       └── wan_2.1_vae.safetensors
    

### 

​

3\. Complete the Workflow Execution Step by Step

![Workflow step diagram](https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan_ati_guide.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=300a2b5bd7002d944e1224e22ed4cd92) Please follow the numbered steps in the image to ensure smooth execution of the corresponding workflow.

  1. Ensure the `Load Diffusion Model` node has loaded the `Wan2_1-I2V-ATI-14B_fp8_e4m3fn.safetensors` model
  2. Ensure the `Load CLIP` node has loaded the `umt5_xxl_fp8_e4m3fn_scaled.safetensors` model
  3. Ensure the `Load VAE` node has loaded the `wan_2.1_vae.safetensors` model
  4. Ensure the `Load CLIP Vision` node has loaded the `clip_vision_h.safetensors` model
  5. Upload the provided input image in the `Load Image` node
  6. Trajectory editing: Currently there is no corresponding trajectory editor in ComfyUI yet. You can use the following link to complete trajectory editing. 
     * [Online Trajectory Editing Tool](https://comfyui-wiki.github.io/Trajectory-Annotation-Tool/)
  7. If you need to modify the prompts (positive and negative), please make changes in the `CLIP Text Encoder` node numbered `5`
  8. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to execute video generation



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/video/wan/wan-ati.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/video/wan/wan-ati)

[Wan-Alpha TutorialPrevious](https://docs.comfy.org/tutorials/video/wan/wan-alpha)[ComfyUI Wan2.1 Fun Control Video ExamplesNext](https://docs.comfy.org/tutorials/video/wan/fun-control)

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
