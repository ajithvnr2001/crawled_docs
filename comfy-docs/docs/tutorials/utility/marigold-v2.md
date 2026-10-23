---
url: https://docs.comfy.org/tutorials/utility/marigold-v2/
title: ComfyUI Marigold V2 Depth, Normal, and Albedo Estimation Guide - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:40.604139+00:00
---

# ComfyUI Marigold V2 Depth, Normal, and Albedo Estimation Guide - ComfyUI

> Source: https://docs.comfy.org/tutorials/utility/marigold-v2/

## On this page

  * Model Installation
  * Depth Estimation
    * 1\. Steps to Run
    * 2\. Model Downloads
  * Surface Normal Estimation
    * 1\. Steps to Run
    * 2\. Model Downloads
  * Albedo Estimation
    * 1\. Steps to Run
    * 2\. Model Downloads
  * Marigold V2 Post-Process Node



Depth & 3D

# ComfyUI Marigold V2 Depth, Normal, and Albedo Estimation Guide

Copy pageCopy page

Estimate depth, surface normals, and albedo from a single image in ComfyUI with Marigold V2: Qwen-Image Edit based diffusion transformers with dedicated LoRAs.

Copy pageCopy page

Marigold V2 is a family of monocular estimation models from Huawei Bayer Lab that repurpose a diffusion transformer (Qwen-Image Edit 2509) for geometry and intrinsic image estimation. From a single RGB image, the models predict a depth map, surface normals, or albedo, following up on the original Marigold (CVPR 2024) which repurposed Stable Diffusion for the same task. The V2 models ship as LoRAs on top of a shared base diffusion model, which keeps each download small and the workflow structure identical across the three tasks. Compared with classical depth networks, the diffusion-based approach produces sharp, boundary-aware predictions and generalizes to open-domain images without retraining. Typical uses include depth-guided control for image and video generation, 3D scene reconstruction pipelines, relighting, and material editing driven by the estimated albedo. Marigold V2 is supported natively in ComfyUI. Update to the latest version of [ComfyUI](https://github.com/comfyanonymous/ComfyUI) before starting.

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

Each workflow uses four files: the shared base diffusion model, plus a task-specific LoRA, VAE, and conditioning embedding. The three tasks use different LoRA, VAE, and conditioning files, so each workflow section below links the exact files it needs. The base diffusion model is shared across all three workflows:

## Diffusion Model

qwen_image_edit_2509_int8_convrot.safetensors → ComfyUI/models/diffusion_models/

If you plan to run all three tasks, download the per-task LoRAs, VAEs, and conditioning embeddings from the workflow sections and store them as shown in each section.

## 

​

Depth Estimation

Predict a depth map from a single image. The decoded prediction is normalized so that near surfaces appear bright. ![Marigold V2 depth estimation workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_marigold_v2_depth_estimation-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Depth Estimation: Marigold V2” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## ev_suv_gold_desert_pavilion.png

`LoadImage` node · `ev_suv_gold_desert_pavilion.png`

### 

​

1\. Steps to Run

  1. Load your input image in the `LoadImage` node
  2. Queue the workflow: the base model runs with the depth LoRA, and the Marigold V2 Post-Process node normalizes the decoded prediction
  3. Save or preview the resulting depth map



### 

​

2\. Model Downloads

## Depth LoRA

marigold_v2_depth_log_stage2.safetensors → ComfyUI/models/loras/

## Depth VAE

marigold_v2_depth_log_stage2_vae.safetensors → ComfyUI/models/vae/

## Depth conditioning embedding

marigold_v2_depth_conditioning.safetensors → ComfyUI/models/embeddings/
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 loras/
    │   │   └── marigold_v2_depth_log_stage2.safetensors
    │   ├── 📂 vae/
    │   │   └── marigold_v2_depth_log_stage2_vae.safetensors
    │   └── 📂 embeddings/
    │       └── marigold_v2_depth_conditioning.safetensors
    

## 

​

Surface Normal Estimation

Predict per-pixel surface normals from a single image. The output maps each pixel to the direction the surface faces, useful for relighting and geometry analysis. ![Marigold V2 surface normal estimation workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_marigold_v2_surface_normal_estimation-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Surface Normal Estimation: Marigold V2” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## greek_statue_orange_cloth.png

`LoadImage` node · `greek_statue_orange_cloth.png`

### 

​

1\. Steps to Run

  1. Load your input image in the `LoadImage` node
  2. Queue the workflow with the normals LoRA loaded
  3. Save or preview the resulting normal map



### 

​

2\. Model Downloads

## Normals LoRA

marigold_v2_normals.safetensors → ComfyUI/models/loras/

## Normals VAE

marigold_v2_normals_vae.safetensors → ComfyUI/models/vae/

## Normals conditioning embedding

marigold_v2_normals_conditioning.safetensors → ComfyUI/models/embeddings/
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 loras/
    │   │   └── marigold_v2_normals.safetensors
    │   ├── 📂 vae/
    │   │   └── marigold_v2_normals_vae.safetensors
    │   └── 📂 embeddings/
    │       └── marigold_v2_normals_conditioning.safetensors
    

## 

​

Albedo Estimation

Predict the albedo (intrinsic color) of a single image, separating material color from lighting and shading. The output is converted to sRGB by the Marigold V2 Post-Process node. ![Marigold V2 albedo estimation workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_marigold_v2_albedo_estimation-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Albedo Estimation: Marigold V2” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## flower_with_texture.png

`LoadImage` node · `flower_with_texture.png`

### 

​

1\. Steps to Run

  1. Load your input image in the `LoadImage` node
  2. Queue the workflow with the albedo LoRA loaded
  3. Save or preview the resulting albedo image



### 

​

2\. Model Downloads

## Albedo LoRA

marigold_v2_albedo.safetensors → ComfyUI/models/loras/

## Albedo VAE

marigold_v2_albedo_vae.safetensors → ComfyUI/models/vae/

## Albedo conditioning embedding

marigold_v2_albedo_conditioning.safetensors → ComfyUI/models/embeddings/
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 loras/
    │   │   └── marigold_v2_albedo.safetensors
    │   ├── 📂 vae/
    │   │   └── marigold_v2_albedo_vae.safetensors
    │   └── 📂 embeddings/
    │       └── marigold_v2_albedo_conditioning.safetensors
    

## 

​

Marigold V2 Post-Process Node

Every workflow ends in the **Marigold V2 Post-Process** node, which turns the raw decoded prediction into a viewable image. The **prediction** option must match the task:

  * **depth** : normalizes the prediction so near surfaces are bright
  * **normals** : maps raw values to unit surface normals
  * **albedo** : converts the prediction to sRGB



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/utility/marigold-v2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/utility/marigold-v2)

[ComfyUI Depth Anything 3 ExamplesPrevious](https://docs.comfy.org/tutorials/utility/depth-anything-3)[MoGe in ComfyUI: Depth, Point Maps, and 3D Mesh WorkflowsNext](https://docs.comfy.org/tutorials/utility/moge)

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
