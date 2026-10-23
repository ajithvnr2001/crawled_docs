---
url: https://docs.comfy.org/tutorials/utility/sam3d-body/
title: SAM 3D Body: Extract 3D Human Mesh From Video in ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:41.794253+00:00
---

# SAM 3D Body: Extract 3D Human Mesh From Video in ComfyUI - ComfyUI

> Source: https://docs.comfy.org/tutorials/utility/sam3d-body/

## On this page

  * SAM 3D Body: 3D Human Mesh Extraction From Video
  * How it works
  * Steps to run
  * Model downloads
    * Model storage location



Pose & Detection

# SAM 3D Body: Extract 3D Human Mesh From Video in ComfyUI

Copy pageCopy page

Extract a full-body 3D human mesh from a video using SAM 3D Body, with pose and shape estimation, face expressions, and a rendered mesh overlay video.

Copy pageCopy page

**SAM 3D Body** is an open-source model that recovers a full-body 3D human mesh from a single video. It combines video tracking, person detection, and mesh prediction to reconstruct the human body with pose, shape, and face expressions, then renders the recovered rig back onto the video. The workflow is useful for motion capture prototyping, biomechanics analysis, and character animation previsualization.

### 

​

SAM 3D Body: 3D Human Mesh Extraction From Video

Load a video of a person. Extract a full-body 3D human mesh with pose, shape, and face expressions, rendered as an overlay video. ![SAM 3D Body workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_sam3d_body-1.webp)

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

## Run on Comfy Cloud

Run this workflow instantly on Comfy Cloud

## Download Workflow

Download JSON or search “SAM 3D Body: 3D Human Mesh Extraction From Video” in Template Library

**Input materials** Upload this file to the `LoadVideo` node:

## woman_holding_water_glass.mp4

`LoadVideo` node 85 · `woman_holding_water_glass.mp4`

## 

​

How it works

  1. **Video tracking** : SAM3 tracks the person across the video frames. Tracking is practically required when multiple people appear in the clip, and improves detection accuracy in general
  2. **Person detection** : RT-DETR detects the person bounding boxes, guided by the text prompt (`person`)
  3. **Mesh prediction** : SAM 3D Body predicts the full-body 3D mesh from the tracked frames, with optional MoGe camera FOV for more accurate alignment with the source video
  4. **Face expressions** : a MediaPipe-based step adds face expressions, which the base model does not detect
  5. **Smoothing** : the mesh sequence is smoothed over time
  6. **Rendering** : a pose file (GLB) is built and the mesh is rendered back onto the video, then saved as an output video



## 

​

Steps to run

  1. **Load a video** : use the `LoadVideo` node to load a video of a person
  2. **Queue the workflow** : press Ctrl (Cmd on macOS) + Enter
  3. **Wait for the pipeline** : tracking, detection, mesh prediction, and rendering run in sequence
  4. **View the result** : inspect the mesh in the `Preview3D` node. The overlay video is saved to `ComfyUI/output/video/SAM3D_body/`



## 

​

Model downloads

Download the SAM 3D Body model and required files. Place them in the corresponding `models/` subdirectories.

## SAM3 multiplex checkpoint

sam3.1_multiplex_fp16.safetensors: SAM3 multiplex checkpoint for video tracking

## SAM 3D Body detection

sam_3d_body_dinov3_bf16.safetensors: SAM 3D Body detection model (DINOv3 backbone)

## MoGe geometry

moge_2_vitl_normal_fp16.safetensors: optional camera FOV estimation for alignment

## RT-DETR person detector

rt_detr_v4-x-hgnet_fp32.safetensors: RT-DETR person detection model

### 

​

Model storage location
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 checkpoints/
    │   │      └── sam3.1_multiplex_fp16.safetensors
    │   ├── 📂 detection/
    │   │      └── sam_3d_body_dinov3_bf16.safetensors
    │   ├── 📂 geometry_estimation/
    │   │      └── moge_2_vitl_normal_fp16.safetensors
    │   └── 📂 diffusion_models/
    │          └── rt_detr_v4-x-hgnet_fp32.safetensors
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/utility/sam3d-body.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/utility/sam3d-body)

[MediaPipe: Face Detection in ComfyUIPrevious](https://docs.comfy.org/tutorials/utility/face-detection/mediapipe)[ComfyUI Depth Anything 3 ExamplesNext](https://docs.comfy.org/tutorials/utility/depth-anything-3)

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
