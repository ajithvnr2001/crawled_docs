---
url: https://docs.comfy.org/tutorials/partner-nodes/hunyuan3d/hunyuan3d-3-0/
title: Hunyuan 3D 3.0 in ComfyUI: Text, Image, and Multi-View to 3D - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:31.407873+00:00
---

# Hunyuan 3D 3.0 in ComfyUI: Text, Image, and Multi-View to 3D - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/hunyuan3d/hunyuan3d-3-0/

## On this page

  * What Hunyuan 3D 3.0 is good at
  * Getting started
    * 1\. Access workflow templates
    * 2\. Run the workflow
    * HunYuan3D: Text to Model
    * HY 3D: Image to Model
  * Advanced features
    * HY 3D: 3D Parts Decomposition
    * HY 3D: UV Unwrapping
    * HY 3D: Smart Topology



Hunyuan 3D

# Hunyuan 3D 3.0 in ComfyUI: Text, Image, and Multi-View to 3D

Copy pageCopy page

Generate 3D models in ComfyUI with the Hunyuan 3D 3.0 partner node from text, images, or multiple views, plus parts decomposition and UV unwrapping.

Copy pageCopy page

Hunyuan 3D 3.0 is Tencent’s state-of-the-art 3D generation model that enables minutes-level 3D content creation. It can generate production-ready 3D assets from text prompts, images, or sketches with far lower barriers to entry than traditional 3D modeling pipelines. ComfyUI has now natively integrated the corresponding Hunyuan 3D API, allowing you to conveniently use the related nodes in ComfyUI for model generation. Currently, ComfyUI’s Partner nodes support the following Hunyuan 3D model generation capabilities:

  * Text-to-3D generation
  * Image-to-3D generation
  * Multi-view-to-3D generation



## 

​

What Hunyuan 3D 3.0 is good at

  * **Game development ideation** : Fast generation of characters, props, and environments with optimized topology for rigging and real-time rendering
  * **Product & e-commerce**: Turn product photos into interactive 3D models for online display
  * **Industrial design** : Sketch-to-3D prototyping and 3D-print-ready part decomposition
  * **VFX & animation**: High-resolution assets with professional UVs and PBR materials



To use the Partner Nodes, you need to ensure that you are logged in properly and using a permitted network environment. Please refer to the [Partner Nodes Overview](https://docs.comfy.org/tutorials/partner-nodes/overview) section of the documentation to understand the specific requirements for using the Partner Nodes.

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

Getting started

### 

​

1\. Access workflow templates

  1. Open the Template Library in the sidebar
  2. Navigate to **3D** → **Hunyuan 3D**
  3. Select a workflow template for Hunyuan 3D



### 

​

2\. Run the workflow

  1. Input your text prompt, images, or sketches depending on the workflow type
  2. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to execute model generation
  3. After the workflow completes, preview and export your 3D model



### 

​

HunYuan3D: Text to Model

Input a text prompt or upload a reference image to generate a detailed 3D model asset. **Example prompt** : “Mechanical dolphin with gears, steampunk” ![HunYuan3D: Text to Model workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_hunyuan3d_text_to_model-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “HunYuan3D: Text to Model” in Template Library

### 

​

HY 3D: Image to Model

Upload an image to generate a 3D model with geometry and PBR textures. Upload 2–4 multi-view images from different angles for improved geometry and material fidelity. ![HY 3D: Image to Model workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_hunyuan3d_image_to_model-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “HY 3D: Image to Model” in Template Library

**Input materials** Upload these files to the matching `LoadImage` nodes:

## pink_robot_front.png

`LoadImage` node 1 · `pink_robot_front.png`

## pink_robot_back.png

`LoadImage` node 10 · `pink_robot_back.png`

![pink_robot_front.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/pink_robot_front.png)![pink_robot_back.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/pink_robot_back.png)

## 

​

Advanced features

Following the [initial HY 3D 3.0 integration](https://blog.comfy.org/p/hunyuan-3d-30-in-comfyui-state-of), Hunyuan 3D’s advanced processing features are now available via Partner Nodes. These workflows help close the gap between generation and production by bringing key post-processing steps into ComfyUI.

### 

​

HY 3D: 3D Parts Decomposition

Upload a 3D model to automatically segment it into its constituent parts, generating a fully decomposed 3D asset for reuse and editing. ![HY 3D: 3D Parts Decomposition workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_hunyuan3d_part-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “HY 3D: 3D Parts Decomposition” in Template Library

### 

​

HY 3D: UV Unwrapping

Upload a 3D model to perform UV unwrapping. Generate a processed model with optimized UV layout for texturing. ![HY 3D: UV Unwrapping workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_hunyuan3d_model2uv-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “HY 3D: UV Unwrapping” in Template Library

### 

​

HY 3D: Smart Topology

Upload a high-poly 3D model file. Generate a lower-polygon, topologically optimized 3D model with a specified reduction level. ![HY 3D: Smart Topology workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_hunyuan3d_smart_topology-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “HY 3D: Smart Topology” in Template Library

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/hunyuan3d/hunyuan3d-3-0.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/hunyuan3d/hunyuan3d-3-0)

[3D Models in ComfyUIPrevious](https://docs.comfy.org/tutorials/partner-nodes/3d/overview)[Meshy 7 in ComfyUI: Text to 3D and Image to 3D WorkflowsNext](https://docs.comfy.org/tutorials/partner-nodes/meshy/meshy-7)

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
