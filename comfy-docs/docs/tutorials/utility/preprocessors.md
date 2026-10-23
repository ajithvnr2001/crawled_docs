---
url: https://docs.comfy.org/tutorials/utility/preprocessors/
title: ComfyUI preprocessor workflows - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:41.338209+00:00
---

# ComfyUI preprocessor workflows - ComfyUI

> Source: https://docs.comfy.org/tutorials/utility/preprocessors/

## On this page

  * What are preprocessors?
  * Depth estimation
    * Video to Depth Map
  * Lineart conversion
    * Video to Lineart / Canny
  * Pose detection
    * Video to Pose Map - OpenPose
  * Normals extraction
    * Video to Normal Map



Utility

# ComfyUI preprocessor workflows

Copy pageCopy page

Learn how to use depth estimation, lineart conversion, pose detection, and normals extraction preprocessors in ComfyUI

Copy pageCopy page

## 

​

What are preprocessors?

These workflows contain custom nodes. You need to install them using [ComfyUI Manager](https://docs.comfy.org/manager/overview) before running the workflows.

Preprocessors are foundational tools that extract structural information from images. They convert images into conditioning signals like depth maps, lineart, pose skeletons, and surface normals. These outputs drive better control and consistency in ControlNet, image-to-image, and video workflows. Using preprocessors as separate workflows enables:

  * Faster iteration without full graph reruns
  * Clear separation of preprocessing and generation
  * Easier debugging and tuning
  * More predictable image and video results



## 

​

Depth estimation

Depth estimation converts a flat image into a depth map representing relative distance within a scene. This structural signal is foundational for controlled generation, spatially aware edits, and relighting workflows. This workflow emphasizes:

  * Clean, stable depth extraction
  * Consistent normalization for downstream use
  * Easy integration with ControlNet and image-edit pipelines

Depth outputs can be reused across multiple passes, making it easier to iterate without re-running expensive upstream steps.

### 

​

Video to Depth Map

Convert a video to a temporally stable depth map. ![Video to Depth Map workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility-depthAnything-v2-relative-video-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Video to Depth Map” in Template Library

**Input materials** Upload this file to the matching `VHS_LoadVideo` node:

## roller_coaster.mp4

`VHS_LoadVideo` node 6 · `roller_coaster.mp4`

## 

​

Lineart conversion

Lineart preprocessors distill an image down to its essential edges and contours, removing texture and color while preserving structure. This workflow is designed to:

  * Produce clean, high-contrast lineart
  * Minimize broken or noisy edges
  * Provide reliable structural guidance for stylization and redraw workflows

Lineart pairs especially well with depth and pose, offering strong structural constraints without overconstraining style.

### 

​

Video to Lineart / Canny

Convert a video to lineart or Canny edges for control processors. ![Video to Lineart workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility-lineart-video-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Video to Lineart / Canny” in Template Library

**Input materials** Upload this file to the matching `VHS_LoadVideo` node:

## utility-lineart-video-input.mp4

`VHS_LoadVideo` node 2 · `utility-lineart-video-input.mp4`

## 

​

Pose detection

Pose detection extracts body keypoints and skeletal structure from images, enabling precise control over human posture and movement. This workflow focuses on:

  * Clear, readable pose outputs
  * Stable keypoint detection suitable for reuse across frames
  * Compatibility with pose-based ControlNet and animation pipelines

By isolating pose extraction into a dedicated workflow, pose data becomes easier to inspect, refine, and reuse.

### 

​

Video to Pose Map - OpenPose

Convert a video to a temporally stable pose control map. ![Video to Pose Map workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility-openpose-video-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Video to Pose Map - OpenPose” in Template Library

**Input materials** Upload this file to the matching `VHS_LoadVideo` node:

## pose_input.mp4

`VHS_LoadVideo` node 2 · `pose_input.mp4`

## 

​

Normals extraction

Normals estimation converts a flat image into a surface normal map: a per-pixel direction field that describes how each part of a surface is oriented (typically encoded as RGB). This signal is useful for relighting, material-aware stylization, and highly structured edits. This workflow emphasizes:

  * Clean, stable normal extraction with minimal speckling
  * Consistent orientation and normalization for reliable downstream use
  * ControlNet-ready outputs for relighting, refinement, and structure-preserving edits
  * Reuse across passes so you can iterate without re-running earlier steps

Normal outputs can be used to:

  * Drive relight/shading changes while preserving geometry
  * Add a stronger 3D-like structure to stylization and redraw pipelines
  * Improve consistency across frames when paired with pose/depth for animation work



### 

​

Video to Normal Map

Convert a video to a temporally stable normal map. ![Video to Normal Map workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility-normal_crafter-video-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Video to Normal Map” in Template Library

**Input materials** Upload this file to the matching `VHS_LoadVideo` node:

## normals_input.mp4

`VHS_LoadVideo` node 3 · `normals_input.mp4`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/utility/preprocessors.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/utility/preprocessors)

[ComfyUI ACE-Step 1.5 Music Generation GuidePrevious](https://docs.comfy.org/tutorials/audio/ace-step/ace-step-v1-5)[Image upscaling in ComfyUINext](https://docs.comfy.org/tutorials/utility/image-upscale)

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
