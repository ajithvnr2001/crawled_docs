---
url: https://docs.comfy.org/tutorials/utility/moge/
title: MoGe in ComfyUI: Depth, Point Maps, and 3D Mesh Workflows - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:41.076184+00:00
---

# MoGe in ComfyUI: Depth, Point Maps, and 3D Mesh Workflows - ComfyUI

> Source: https://docs.comfy.org/tutorials/utility/moge/

## On this page

  * ComfyUI MoGe Introduction
  * Model Installation
  * Example Workflows
    * MoGe: Depth Estimation
    * 1.1 Steps to Run
    * MoGe: Perspective Geometry Estimation
    * 2.1 Steps to Run
    * Moge: Panorama to Mesh
    * 3.1 Steps to Run
    * MoGe 3: Geometry Estimation
    * 4.1 Steps to Run
  * Community Resources



Depth & 3D

# MoGe in ComfyUI: Depth, Point Maps, and 3D Mesh Workflows

Copy pageCopy page

Use MoGe in ComfyUI for monocular geometry estimation: metric depth and point maps, normal maps, and mesh generation from a single image.

Copy pageCopy page

# 

​

ComfyUI MoGe Introduction

[MoGe](https://github.com/microsoft/MoGe) (CVPR 2025, from Microsoft Research) is a powerful model for recovering 3D geometry from monocular open-domain images. It estimates metric point maps, metric depth maps, normal maps, and camera FOV: all in a single forward pass. Key capabilities:

  * **Accurate 3D geometry estimation** : point maps, depth maps, and normal maps from a single image: one model, one forward pass
  * **Metric scale** (MoGe-2, MoGe-3): point maps and depth maps in real-world scale
  * **Flexible resolution support** : works with various resolutions and aspect ratios (2:1 to 1:2)
  * **Fast inference** : ~60ms per image on A100 / RTX 3090 (FP16, ViT-L)
  * **Mesh generation** from both perspective and panoramic images

ComfyUI ships checkpoints for three MoGe versions:

File| Version| Metric Scale| Normal Maps| Params  
---|---|---|---|---  
`moge_1_vitl_fp16`| **MoGe-1**|  -| -| 314M  
`moge_2_vitl_normal_fp16`| **MoGe-2**|  ✅| ✅| 331M  
`moge_3_vitl_fp16`| **MoGe-3**|  ✅| ✅| 370M  
`moge_3_vitg_fp16`| **MoGe-3**|  ✅| ✅| 1.25B  
  
> MoGe-2 adds metric scale and high-quality normal map estimation with sharper visual detail and lower inference latency. **MoGe-2 with normal (`moge_2_vitl_normal_fp16`) is the recommended checkpoint.** MoGe-3 keeps the MoGe-2 architecture and adds a self-guided sparse volumetric refinement stage for significantly improved fine-grained point map geometry. It ships as a ViT-L checkpoint (`moge_3_vitl_fp16`) and a larger ViT-g checkpoint (`moge_3_vitg_fp16`).

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

ComfyUI now natively supports MoGe nodes. Make sure you have updated to the latest version of [ComfyUI](https://github.com/Comfy-Org/ComfyUI) before starting.Generated `.glb` format models will be output to the `ComfyUI/output/mesh` folder.

## 

​

Model Installation

Download the MoGe checkpoint(s) and save them to the corresponding ComfyUI folder:

  * **MoGe-2 (recommended)** : [moge_2_vitl_normal_fp16.safetensors](https://huggingface.co/Comfy-Org/MoGe/blob/main/geometry_estimation/moge_2_vitl_normal_fp16.safetensors)
  * **MoGe-1 (baseline)** : [moge_1_vitl_fp16.safetensors](https://huggingface.co/Comfy-Org/MoGe/blob/main/geometry_estimation/moge_1_vitl_fp16.safetensors)
  * **MoGe-3 (highest detail)** : [moge_3_vitg_fp16.safetensors](https://huggingface.co/Comfy-Org/MoGe/blob/main/geometry_estimation/moge_3_vitg_fp16.safetensors) (1.25B) or [moge_3_vitl_fp16.safetensors](https://huggingface.co/Comfy-Org/MoGe/blob/main/geometry_estimation/moge_3_vitl_fp16.safetensors) (370M)


    
    
    ComfyUI/
    ├── models/
    │   ├── geometry_estimation/
    │   │   ├── moge_2_vitl_normal_fp16.safetensors
    │   │   ├── moge_1_vitl_fp16.safetensors
    │   │   ├── moge_3_vitg_fp16.safetensors
    │   │   └── moge_3_vitl_fp16.safetensors
    

MoGe-3 checkpoints only: the `Run MoGe Inference` and `Run MoGe Panorama Inference` nodes expose an advanced `refine_steps` control (0 to 8, default 3) that runs sparse volumetric refinement passes over the predicted depth. `0` disables refinement, and more passes sharpen fine detail and edges at a roughly linear cost. MoGe-1 and MoGe-2 checkpoints ignore this setting.

## 

​

Example Workflows

### 

​

MoGe: Depth Estimation

Upload a single RGB image and generate a colored depth preview and raw depth map. ![MoGe depth estimation workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_moge_depth_estimation-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “MoGe: Depth Estimation” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## alien_world.png

`LoadImage` node 9 · `alien_world.png`

### 

​

1.1 Steps to Run

  1. Ensure the `LoadMoGeModel` node has loaded a MoGe checkpoint
  2. Load an image in the `Load Image` node
  3. Click `Queue` or use `Ctrl(cmd) + Enter` to run
  4. The workflow outputs colored depth preview, raw depth preview, and a mask



### 

​

MoGe: Perspective Geometry Estimation

Upload an image to estimate its perspective geometry. Generate a 3D depth map and surface normals from the input, then convert to a textured GLB mesh. ![MoGe perspective to mesh workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/3d_moge_perspective_to_mesh-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “MoGe: Perspective Geometry Estimation” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## modern_living_room.png

`LoadImage` node 9 · `modern_living_room.png`

![Input image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/modern_living_room.png)

This is **monocular geometry estimation** : occluded areas and object backsides will be missing or fragmented. Useful for quick scene prototyping, reference geometry, or visualizing depth and normals as a mesh, but not a replacement for multi-view 3D reconstruction.

### 

​

2.1 Steps to Run

  1. Ensure the `LoadMoGeModel` node has loaded a MoGe checkpoint
  2. Load a perspective photo in the `Load Image` node
  3. (Optional) View the OpenGL and DirectX normal previews
  4. Click `Queue` or use `Ctrl(cmd) + Enter` to run



### 

​

Moge: Panorama to Mesh

Upload an equirectangular 360° panorama image and generate a textured GLB mesh with vertex colors. ![MoGe panorama to mesh workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/3d_moge_panorama_to_mesh-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Moge: Panorama to Mesh” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## lego_street_panorama.png

`LoadImage` node 28 · `lego_street_panorama.png`

![Input panorama](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/lego_street_panorama.png)

The workflow uses `MoGePanoramaInference` to split the panorama into 12 perspective views, run monocular geometry estimation on each view independently, then merge them into a single mesh.

### 

​

3.1 Steps to Run

  1. Ensure the `LoadMoGeModel` node has loaded one of the MoGe checkpoints
  2. Load an equirectangular panorama image in the `Load Image` node
  3. Click `Queue` or use `Ctrl(cmd) + Enter` to run



### 

​

MoGe 3: Geometry Estimation

Estimate fine-detail geometry from a single image with MoGe 3. The MoGe-3 checkpoints lift the coarse point map onto a sparse voxel shell and refine depth with lightweight sparse 3D convolutions, which keeps thin structures and depth discontinuities that image-space decoders blur. ![MoGe 3 geometry estimation workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_moge3_geometry_estimation-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Geometry Estimation: MoGe 3” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## cosmic_suitcase.png

`LoadImage` node 3 · `cosmic_suitcase.png`

### 

​

4.1 Steps to Run

  1. Ensure the `Geometry Estimation (MoGe 3)` subgraph has a MoGe 3 checkpoint selected: the template ships with `moge_3_vitg_fp16.safetensors`, and `moge_3_vitl_fp16.safetensors` is available in the same dropdown
  2. Load an image in the `Load Image` node
  3. (Optional) Change `output` on the subgraph node to render a different map: `mask` is the default, and `depth`, `depth_colored`, `normal_opengl`, and `normal_directx` are the other options
  4. Click `Queue` or use `Ctrl(cmd) + Enter` to run



* * *

## 

​

Community Resources

  * [MoGe GitHub (microsoft/MoGe)](https://github.com/microsoft/MoGe): Research paper and code
  * [Comfy-Org/MoGe](https://huggingface.co/Comfy-Org/MoGe): Official ComfyUI model weights



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/utility/moge.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/utility/moge)

[ComfyUI Marigold V2 Depth, Normal, and Albedo Estimation GuidePrevious](https://docs.comfy.org/tutorials/utility/marigold-v2)[ComfyUI frame interpolation workflowNext](https://docs.comfy.org/tutorials/utility/frame-interpolation)

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
