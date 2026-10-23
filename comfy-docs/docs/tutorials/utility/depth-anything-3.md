---
url: https://docs.comfy.org/tutorials/utility/depth-anything-3/
title: ComfyUI Depth Anything 3 Examples - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:40.080365+00:00
---

# ComfyUI Depth Anything 3 Examples - ComfyUI

> Source: https://docs.comfy.org/tutorials/utility/depth-anything-3/

## On this page

  * ComfyUI Depth Anything 3 Introduction
  * Model Installation
  * Example Workflows
    * Depth Anything 3: Image Depth Estimation
    * Steps to Run
    * Depth Anything 3: Video Depth Estimation
    * Steps to Run
  * Model Variants
  * Community Resources



Depth & 3D

# ComfyUI Depth Anything 3 Examples

Copy pageCopy page

Run Depth Anything 3 in ComfyUI for monocular and multi-view depth estimation, camera pose recovery, and 3D reconstruction from images and video.

Copy pageCopy page

# 

​

ComfyUI Depth Anything 3 Introduction

[Depth Anything 3 (DA3)](https://github.com/ByteDance-Seed/Depth-Anything-3), from ByteDance Seed, is a vision transformer that recovers spatially consistent geometry from arbitrary visual inputs, with or without known camera poses. A single plain DINO encoder and unified depth-ray representation let one model family cover monocular depth, multi-view depth, camera pose estimation, and 3D reconstruction. Key capabilities:

  * **Unified monocular & multi-view depth**: estimate depth from a single image or multiple views
  * **Camera pose estimation** : recover camera positions from unordered image sets
  * **3D reconstruction** from multi-view inputs
  * **Video depth estimation** : per-frame depth sequences for video inputs
  * **Multiple model variants** : Small, Base, Mono/Metric Large



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

ComfyUI now natively supports Depth Anything 3 nodes. Make sure you have updated to the latest version of [ComfyUI](https://github.com/Comfy-Org/ComfyUI) before starting.

## 

​

Model Installation

Download the Depth Anything 3 checkpoint(s) and save them to the corresponding ComfyUI folder:

  * **Small** ([depth_anything_3_small.safetensors](https://huggingface.co/Comfy-Org/Depth-Anything-3/blob/main/geometry_estimation/depth_anything_3_small.safetensors)): Lightweight, fast inference
  * **Base** ([depth_anything_3_base.safetensors](https://huggingface.co/Comfy-Org/Depth-Anything-3/blob/main/geometry_estimation/depth_anything_3_base.safetensors)): Balanced performance
  * **Mono-Large** ([depth_anything_3_mono_large.safetensors](https://huggingface.co/Comfy-Org/Depth-Anything-3/blob/main/geometry_estimation/depth_anything_3_mono_large.safetensors)): Best for monocular depth, includes sky detection
  * **Metric-Large** ([depth_anything_3_metric_large.safetensors](https://huggingface.co/Comfy-Org/Depth-Anything-3/blob/main/geometry_estimation/depth_anything_3_metric_large.safetensors)): Metric scale depth in metres, includes sky detection


    
    
    ComfyUI/
    ├── models/
    │   ├── geometry_estimation/
    │   │   ├── depth_anything_3_small.safetensors
    │   │   ├── depth_anything_3_base.safetensors
    │   │   ├── depth_anything_3_mono_large.safetensors
    │   │   └── depth_anything_3_metric_large.safetensors
    

## 

​

Example Workflows

### 

​

Depth Anything 3: Image Depth Estimation

Upload one image and generate a depth map using Depth Anything 3. View a side-by-side comparison of the original image and depth output. ![Depth Anything 3 image depth estimation workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_depth_anything3_image_depth_estimation-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Depth Anything 3: Image Depth Estimation” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## retro_futuristic_home.png

`LoadImage` node 85 · `retro_futuristic_home.png`

![Input image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/retro_futuristic_home.png)

### 

​

Steps to Run

  1. **LoadImage** : load your input image
  2. **LoadDA3Model** : select a Depth Anything 3 variant
  3. **Run** : click Queue or use `Cmd+Enter`
  4. The workflow outputs a depth map and side-by-side comparison



## Learn about Subgraph

This workflow uses Subgraph nodes for modular processing. Check out the Subgraph documentation to learn how to customize and extend the workflow.

### 

​

Depth Anything 3: Video Depth Estimation

Upload a video to generate a per-frame depth sequence. Inside the subgraph, **GetVideoComponents** splits the input video into frames, **LoadDA3Model** loads the model, and **SetVideoComponents** reassembles the depth frames back into a video output. ![Depth Anything 3 video depth estimation workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_depth_anything3_video_depth_estimation-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Depth Anything 3: Video Depth Estimation” in Template Library

**Input materials** Upload this file to the matching `LoadVideo` node:

## empty_room_assembly.mp4

`LoadVideo` node 87 · `empty_room_assembly.mp4`

### 

​

Steps to Run

  1. **LoadVideo** : load your input video
  2. **Select Model** : choose between **Small** , **Base** , **Mono-Large** , or **Metric-Large**
  3. **Run** : click Queue or use `Cmd+Enter`
  4. The workflow outputs a video with per-frame depth maps



## Learn about Subgraph

This workflow uses Subgraph nodes for modular processing. Check out the Subgraph documentation to learn how to customize and extend the workflow.

## 

​

Model Variants

Variant| head_type| has_sky| has_confidence| camera_decoder| Best for  
---|---|---|---|---|---  
**Small**|  dualdpt| ❌| ✅| ✅| Fast inference, mobile/edge  
**Base**|  dualdpt| ❌| ✅| ✅| Balanced performance  
**Mono-Large**|  dpt| ✅| ❌| ❌| Monocular depth with sky detection  
**Metric-Large**|  dpt| ✅| ❌| ❌| Physical metric depth in metres  
  
  * **Small** and **Base** use the `dualdpt` head type with confidence estimation and camera decoder support for multi-view applications.
  * **Mono-Large** and **Metric-Large** use the `dpt` head type with sky detection. Metric-Large outputs raw depth in metres.



## 

​

Community Resources

  * [Depth Anything 3 GitHub (ByteDance-Seed)](https://github.com/ByteDance-Seed/Depth-Anything-3): Research paper and code
  * [Comfy-Org/Depth-Anything-3](https://huggingface.co/Comfy-Org/Depth-Anything-3): Official ComfyUI model weights



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/utility/depth-anything-3.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/utility/depth-anything-3)

[SAM 3D Body: Extract 3D Human Mesh From Video in ComfyUIPrevious](https://docs.comfy.org/tutorials/utility/sam3d-body)[ComfyUI Marigold V2 Depth, Normal, and Albedo Estimation GuideNext](https://docs.comfy.org/tutorials/utility/marigold-v2)

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
