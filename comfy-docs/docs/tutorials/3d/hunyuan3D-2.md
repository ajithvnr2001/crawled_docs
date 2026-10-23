---
url: https://docs.comfy.org/tutorials/3d/hunyuan3D-2/
title: ComfyUI Hunyuan3D-2 Examples - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-18T12:01:23.895638+00:00
---

# ComfyUI Hunyuan3D-2 Examples - ComfyUI

> Source: https://docs.comfy.org/tutorials/3d/hunyuan3D-2/

## On this page

  * Hunyuan3D 2.0 Introduction
  * ComfyUI Hunyuan3D-2mv Workflow Example
    * HY 3D 2.0 MV
    * 1\. Workflow
    * 2\. Manual Model Installation
    * 3\. Steps to Run the Workflow
  * Hunyuan3D-2mv-turbo Workflow
    * HY 3D 2.0 MV Turbo
    * 1\. Workflow
    * 2\. Manual Model Installation
    * 3\. Steps to Run the Workflow
  * Hunyuan3D-2 Single View Workflow
    * HY 3D 2.0
    * 1\. Workflow
    * 2\. Manual Model Installation
    * 3\. Steps to Run the Workflow
  * Hunyuan3D 2.1 Single View Workflow
    * HY 3D 2.1
    * 1\. Manual Model Installation
    * 2\. Steps to Run the Workflow
  * Community Resources
  * Hunyuan3D 2.0 Open-Source Model Series



3D

# ComfyUI Hunyuan3D-2 Examples

Copy pageCopy page

Hunyuan3D 2.0 and 2.1 in ComfyUI: generate 3D meshes from one image or several views with Tencent’s open-source 3D models.

Copy pageCopy page

# 

​

Hunyuan3D 2.0 Introduction

![Hunyuan 3D 2](https://raw.githubusercontent.com/Tencent/Hunyuan3D-2/main/assets/images/e2e-1.gif) ![Hunyuan 3D 2](https://raw.githubusercontent.com/Tencent/Hunyuan3D-2/main/assets/images/e2e-2.gif) [Hunyuan3D 2.0](https://github.com/Tencent/Hunyuan3D-2) is an open-source 3D asset generation model released by Tencent, capable of generating high-fidelity 3D models with high-resolution texture maps through text or images. Hunyuan3D 2.0 adopts a two-stage generation approach, first generating a geometry model without textures, then synthesizing high-resolution texture maps. This effectively separates the complexity of shape and texture generation. Below are the two core components of Hunyuan3D 2.0:

  1. **Geometry Generation Model (Hunyuan3D-DiT)** : Based on a flow diffusion Transformer architecture, it generates untextured geometric models that precisely match input conditions.
  2. **Texture Generation Model (Hunyuan3D-Paint)** : Combines geometric conditions and multi-view diffusion techniques to add high-resolution textures to models, supporting PBR materials.

**Key Advantages**

  * **High-Precision Generation** : Sharp geometric structures, rich texture colors, support for PBR material generation, achieving near-realistic lighting effects.
  * **Diverse Usage Methods** : Provides code calls, Blender plugins, Gradio applications, and online experience through the official website, suitable for different user needs.
  * **Lightweight and Compatibility** : The Hunyuan3D-2mini model requires only 5GB VRAM, the standard version needs 6GB VRAM for shape generation, and the complete process (shape + texture) requires only 12GB VRAM.

Recently (March 18, 2025), Hunyuan3D 2.0 also introduced a multi-view shape generation model (Hunyuan3D-2mv), which supports generating more detailed geometric structures from inputs at different angles. This example includes four workflows:

  * Using Hunyuan3D-2mv with multiple view inputs to generate 3D models
  * Using Hunyuan3D-2mv-turbo with multiple view inputs to generate 3D models
  * Using Hunyuan3D-2 with a single view input to generate 3D models
  * Using Hunyuan3D 2.1 with a single view input to generate 3D models



ComfyUI now natively supports Hunyuan3D-2mv, but does not yet support texture and material generation. Please make sure you have updated to the latest version of [ComfyUI](https://github.com/Comfy-Org/ComfyUI) before starting.The workflow example PNG images in this tutorial contain workflow JSON in their metadata:

  * You can drag them directly into ComfyUI
  * Or use the menu `Workflows` -> `Open (ctrl+o)`

This will load the corresponding workflow and prompt you to download the required models. The generated `.glb` format models will be output to the `ComfyUI/output/mesh` folder.

## 

​

ComfyUI Hunyuan3D-2mv Workflow Example

In the Hunyuan3D-2mv workflow, we’ll use multi-view images to generate a 3D model. Note that multiple view images are not mandatory in this workflow - you can use only the `front` view image to generate a 3D model.

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

HY 3D 2.0 MV

Generate 3D models from multiple views using Hunyuan3D 2.0 MV. ![HY 3D 2.0 MV workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/3d_hunyuan3d_multiview_to_model-1.webp)

## Run on Comfy Cloud

Run this workflow instantly on Comfy Cloud

## Download Workflow

Download JSON or search “HY 3D 2.0 MV” in Template Library

**Input materials** Upload these files to the matching `LoadImage` nodes:

## 3d_hunyuan3d_multiview_to_model_front_image.png

`LoadImage` node 56 · front view

## 3d_hunyuan3d_multiview_to_model_left_image.png

`LoadImage` node 78 · left view

## 3d_hunyuan3d_multiview_to_model_back_image.png

`LoadImage` node 80 · back view

## 3d_hunyuan3d_multiview_to_model_right_image.png

`LoadImage` node 87 · right view

### 

​

1\. Workflow

Please download the images below and drag into ComfyUI to load the workflow. ![Hunyuan3D-2mv workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/3d/hunyuan3d-2/hunyuan3d_2mv_elf/hunyuan-3d-multiview-elf.webp) Download the images below we will use them as input images. ![input image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/3d/hunyuan3d-2/hunyuan3d_2mv_elf/front.png) ![input image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/3d/hunyuan3d-2/hunyuan3d_2mv_elf/left.png) ![input image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/3d/hunyuan3d-2/hunyuan3d_2mv_elf/back.png)

In this example, the input images have already been preprocessed to remove excess background. In actual use, you can use custom nodes like [ComfyUI_essentials](https://github.com/cubiq/ComfyUI_essentials) to automatically remove excess background.

### 

​

2\. Manual Model Installation

Download the model below and save it to the corresponding ComfyUI folder

  * hunyuan3d-dit-v2-mv: [model.fp16.safetensors](https://huggingface.co/tencent/Hunyuan3D-2mv/blob/main/hunyuan3d-dit-v2-mv/model.fp16.safetensors?download=true) \- after downloading, you can rename it to `hunyuan3d-dit-v2-mv.safetensors`


    
    
    ComfyUI/
    ├── models/
    │   ├── checkpoints/
    │   │   └── hunyuan3d-dit-v2-mv.safetensors  // renamed file
    

### 

​

3\. Steps to Run the Workflow

![ComfyUI hunyuan3d_2mv](https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/3d/hunyuan3d-2mv/hunyuan3d_2mv.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=17e6ac738f0e0133536bceb6e3ea1b56)

  1. Ensure that the Image Only Checkpoint Loader(img2vid model) has loaded our downloaded and renamed `hunyuan3d-dit-v2-mv.safetensors` model
  2. Load the corresponding view images in each of the `Load Image` nodes
  3. Click the `Queue` button, or use the shortcut `Ctrl(cmd) + Enter` to run the workflow

If you need to add more views, make sure to load other view images in the `Hunyuan3Dv2ConditioningMultiView` node, and ensure that you load the corresponding view images in the `Load Image` nodes.

## 

​

Hunyuan3D-2mv-turbo Workflow

In the Hunyuan3D-2mv-turbo workflow, we’ll use the Hunyuan3D-2mv-turbo model to generate 3D models. This model is a step distillation version of Hunyuan3D-2mv, allowing for faster 3D model generation. In this version of the workflow, we set `cfg` to 1.0 and add a `flux guidance` node to control the `distilled cfg` generation.

### 

​

HY 3D 2.0 MV Turbo

Generate 3D models from multiple views using Hunyuan3D 2.0 MV Turbo. ![HY 3D 2.0 MV Turbo workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/3d_hunyuan3d_multiview_to_model_turbo-1.webp)

## Run on Comfy Cloud

Run this workflow instantly on Comfy Cloud

## Download Workflow

Download JSON or search “HY 3D 2.0 MV Turbo” in Template Library

**Input materials** Upload these files to the matching `LoadImage` nodes:

## 3d_hunyuan3d_multiview_to_model_turbo_front_view.png

`LoadImage` node 56 · front view

## 3d_hunyuan3d_multiview_to_model_turbo_back_view.png

`LoadImage` node 82 · back view

## 3d_hunyuan3d_multiview_to_model_turbo_left_view.png

`LoadImage` node 85 · left view

## 3d_hunyuan3d_multiview_to_model_turbo_right_view.png

`LoadImage` node 87 · right view

### 

​

1\. Workflow

Please download the images below and drag into ComfyUI to load the workflow. ![Hunyuan3D-2mv-turbo workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/3d/hunyuan3d-2/hunyuan3d_2mv_turbo/hunyuan-3d-turbo.webp) Download the images below we will use them as input images. ![input image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/3d/hunyuan3d-2/hunyuan3d_2mv_turbo/front.png) ![input image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/3d/hunyuan3d-2/hunyuan3d_2mv_turbo/right.png)

### 

​

2\. Manual Model Installation

Download the model below and save it to the corresponding ComfyUI folder

  * hunyuan3d-dit-v2-mv-turbo: [model.fp16.safetensors](https://huggingface.co/tencent/Hunyuan3D-2mv/blob/main/hunyuan3d-dit-v2-mv-turbo/model.fp16.safetensors?download=true) \- after downloading, you can rename it to `hunyuan3d-dit-v2-mv-turbo.safetensors`


    
    
    ComfyUI/
    ├── models/
    │   ├── checkpoints/
    │   │   └── hunyuan3d-dit-v2-mv-turbo.safetensors  // renamed file
    

### 

​

3\. Steps to Run the Workflow

![ComfyUI hunyuan3d_2mv_turbo](https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/3d/hunyuan3d-2mv/hunyuan3d_2mv_turbo.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=33bb861fd695fd4b10a53345f004d2cc)

  1. Ensure that the `Image Only Checkpoint Loader(img2vid model)` node has loaded our renamed `hunyuan3d-dit-v2-mv-turbo.safetensors` model
  2. Load the corresponding view images in each of the `Load Image` nodes
  3. Click the `Queue` button, or use the shortcut `Ctrl(cmd) + Enter` to run the workflow



## 

​

Hunyuan3D-2 Single View Workflow

In the Hunyuan3D-2 workflow, we’ll use the Hunyuan3D-2 model to generate 3D models. This model is not a multi-view model. In this workflow, we use the `Hunyuan3Dv2Conditioning` node instead of the `Hunyuan3Dv2ConditioningMultiView` node.

### 

​

HY 3D 2.0

Generate 3D models from single images using Hunyuan3D 2.0. ![HY 3D 2.0 workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/3d_hunyuan3d_image_to_model-1.webp)

## Run on Comfy Cloud

Run this workflow instantly on Comfy Cloud

## Download Workflow

Download JSON or search “HY 3D 2.0” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## 3d_hunyuan3d_image_to_model_input_image.png

`LoadImage` node 56 · `3d_hunyuan3d_image_to_model_input_image.png`

### 

​

1\. Workflow

Please download the image below and drag it into ComfyUI to load the workflow. ![Hunyuan3D-2 workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/3d/hunyuan3d-2/hunyuan3d-non-multiview-train.webp) Download the image below we will use it as input image. ![ComfyUI Hunyuan 3D 2 workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/3d/hunyuan3d-2/hunyuan_3d_v2_non_multiview_train.png)

### 

​

2\. Manual Model Installation

Download the model below and save it to the corresponding ComfyUI folder

  * hunyuan3d-dit-v2-0: [model.fp16.safetensors](https://huggingface.co/tencent/Hunyuan3D-2/blob/main/hunyuan3d-dit-v2-0/model.fp16.safetensors?download=true) \- after downloading, you can rename it to `hunyuan3d-dit-v2.safetensors`


    
    
    ComfyUI/
    ├── models/
    │   ├── checkpoints/
    │   │   └── hunyuan3d-dit-v2.safetensors  // renamed file
    

### 

​

3\. Steps to Run the Workflow

![ComfyUI hunyuan3d_2](https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/3d/hunyuan3d-2mv/hunyuan3d_2_non_multiview.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=33c158fcfb133560674aa56bfdb5087d)

  1. Ensure that the `Image Only Checkpoint Loader(img2vid model)` node has loaded our renamed `hunyuan3d-dit-v2.safetensors` model
  2. Load the image in the `Load Image` node
  3. Click the `Queue` button, or use the shortcut `Ctrl(cmd) + Enter` to run the workflow



## 

​

Hunyuan3D 2.1 Single View Workflow

Hunyuan3D 2.1 is Tencent’s follow-up shape model, released in June 2025. It refines the geometry quality of Hunyuan3D 2.0, and the ComfyUI checkpoint repackages the shape pipeline into a single file, so this workflow needs one model download instead of separate DiT and VAE files. Like the other workflows on this page, it outputs an untextured mesh.

### 

​

HY 3D 2.1

Generate a 3D mesh from a single image using Hunyuan3D 2.1. ![HY 3D 2.1 workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/3d_hunyuan3d-v2.1-1.webp)

## Run on Comfy Cloud

Run this workflow instantly on Comfy Cloud

## Download Workflow

Download JSON or search “HY 3D 2.1” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## 3d_hunyuan3d-v2.1_input_image.png

`LoadImage` node 2 · `3d_hunyuan3d-v2.1_input_image.png`

### 

​

1\. Manual Model Installation

Download the checkpoint below and save it to the `checkpoints` folder:

## hunyuan_3d_v2.1.safetensors

Place in `ComfyUI/models/checkpoints/`
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   └── 📂 checkpoints/
    │       └── hunyuan_3d_v2.1.safetensors
    

The file is about 7.4 GB.

### 

​

2\. Steps to Run the Workflow

  1. Ensure that the `Image Only Checkpoint Loader(img2vid model)` node has loaded `hunyuan_3d_v2.1.safetensors`
  2. Load your reference image in the `Load Image` node
  3. Click the `Queue` button, or use the shortcut `Ctrl(cmd) + Enter` to run the workflow

The generated `.glb` mesh is saved to `ComfyUI/output/mesh/`.

## 

​

Community Resources

Below are ComfyUI community resources related to Hunyuan3D-2

  * [ComfyUI-Hunyuan3DWrapper](https://github.com/kijai/ComfyUI-Hunyuan3DWrapper)
  * [Kijai/Hunyuan3D-2_safetensors](https://huggingface.co/Kijai/Hunyuan3D-2_safetensors/tree/main)
  * [ComfyUI-3D-Pack](https://github.com/MrForExample/ComfyUI-3D-Pack)



## 

​

Hunyuan3D 2.0 Open-Source Model Series

Currently, Hunyuan3D 2.0 has open-sourced multiple models covering the complete 3D generation process. You can visit [Hunyuan3D-2](https://github.com/Tencent/Hunyuan3D-2) for more information. **Hunyuan3D-2mini Series**

Model| Description| Date| Parameters| Huggingface  
---|---|---|---|---  
Hunyuan3D-DiT-v2-mini| Mini Image to Shape Model| 2025-03-18| 0.6B| [Visit](https://huggingface.co/tencent/Hunyuan3D-2mini/tree/main/hunyuan3d-dit-v2-mini)  
  
**Hunyuan3D-2mv Series**

Model| Description| Date| Parameters| Huggingface  
---|---|---|---|---  
Hunyuan3D-DiT-v2-mv-Fast| Guidance Distillation Version, can halve DIT inference time| 2025-03-18| 1.1B| [Visit](https://huggingface.co/tencent/Hunyuan3D-2mv/tree/main/hunyuan3d-dit-v2-mv-fast)  
Hunyuan3D-DiT-v2-mv| Multi-view Image to Shape Model, suitable for 3D creation requiring multiple angles to understand the scene| 2025-03-18| 1.1B| [Visit](https://huggingface.co/tencent/Hunyuan3D-2mv/tree/main/hunyuan3d-dit-v2-mv)  
  
**Hunyuan3D-2 Series**

Model| Description| Date| Parameters| Huggingface  
---|---|---|---|---  
Hunyuan3D-DiT-v2-0-Fast| Guidance Distillation Model| 2025-02-03| 1.1B| [Visit](https://huggingface.co/tencent/Hunyuan3D-2/tree/main/hunyuan3d-dit-v2-0-fast)  
Hunyuan3D-DiT-v2-0| Image to Shape Model| 2025-01-21| 1.1B| [Visit](https://huggingface.co/tencent/Hunyuan3D-2/tree/main/hunyuan3d-dit-v2-0)  
Hunyuan3D-Paint-v2-0| Texture Generation Model| 2025-01-21| 1.3B| [Visit](https://huggingface.co/tencent/Hunyuan3D-2/tree/main/hunyuan3d-paint-v2-0)  
Hunyuan3D-Delight-v2-0| Image Delight Model| 2025-01-21| 1.3B| [Visit](https://huggingface.co/tencent/Hunyuan3D-2/tree/main/hunyuan3d-delight-v2-0)  
  
Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/3d/hunyuan3D-2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/3d/hunyuan3D-2)

[TripoSplat Image to Gaussian Splat ComfyUI Workflow ExamplePrevious](https://docs.comfy.org/tutorials/3d/triposplat)[Gemma 4 ComfyUI workflow exampleNext](https://docs.comfy.org/tutorials/llm/gemma4/gemma4)

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
