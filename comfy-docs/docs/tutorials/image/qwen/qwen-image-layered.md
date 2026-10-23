---
url: https://docs.comfy.org/tutorials/image/qwen/qwen-image-layered/
title: Qwen-Image-Layered ComfyUI Workflow Example - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:23.836907+00:00
---

# Qwen-Image-Layered ComfyUI Workflow Example - ComfyUI

> Source: https://docs.comfy.org/tutorials/image/qwen/qwen-image-layered/

## On this page

  * Qwen-Image-Layered workflow
    * Qwen-Image-Layered Decomposition
  * Model links
  * FP8 version
  * Layers and output
    * How the layers become separate images
  * Workflow settings
    * Sampler settings
    * Input size
    * Prompt (optional)



Qwen

# Qwen-Image-Layered ComfyUI Workflow Example

Copy pageCopy page

Qwen-Image-Layered is a model capable of decomposing an image into multiple RGBA layers, enabling inherent editability through layer decomposition.

Copy pageCopy page

**Qwen-Image-Layered** is a model developed by Alibaba’s Qwen team that can decompose an image into multiple RGBA layers. This layered representation unlocks inherent editability: each layer can be independently manipulated without affecting other content. **Key Features** :

  * **Inherent Editability** : Each layer can be independently manipulated without affecting other content
  * **High-Fidelity Elementary Operations** : Supports resizing, repositioning, and recoloring with physical isolation of semantic components
  * **Variable-Layer Decomposition** : Not limited to a fixed number of layers - decompose into 3, 4, 8, or more layers as needed
  * **Recursive Decomposition** : Any layer can be further decomposed, enabling infinite decomposition depth

**Related Links** :

  * [Hugging Face](https://huggingface.co/Qwen/Qwen-Image-Layered)
  * [Research Paper](https://arxiv.org/abs/2512.15603)
  * [Blog](https://qwen.ai/blog?id=qwen-image-layered)



## 

​

Qwen-Image-Layered workflow

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

Qwen-Image-Layered Decomposition

Decompose an image into editable RGBA layers for recolor, replace, resize, and reposition workflows. ![Qwen-Image-Layered workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_image_layered-1.webp)

## Download Workflow

Download the JSON workflow file

## Run on Comfy Cloud

Run ComfyUI online with zero setup

**Input materials** Upload this file to `LoadImage` node **74** :

## coastal_smiling_woman.png

`LoadImage` node 74 · `coastal_smiling_woman.png`

![coastal_smiling_woman.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/coastal_smiling_woman.png)

## 

​

Model links

**text_encoders**

  * [qwen_2.5_vl_7b_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/blob/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors)

**diffusion_models**

  * [qwen_image_layered_bf16.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-Layered_ComfyUI/blob/main/split_files/diffusion_models/qwen_image_layered_bf16.safetensors)

**vae**

  * [qwen_image_layered_vae.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-Layered_ComfyUI/blob/main/split_files/vae/qwen_image_layered_vae.safetensors)

**Model Storage Location**
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 text_encoders/
    │   │      └── qwen_2.5_vl_7b_fp8_scaled.safetensors
    │   ├── 📂 diffusion_models/
    │   │      └── qwen_image_layered_bf16.safetensors
    │   └── 📂 vae/
    │          └── qwen_image_layered_vae.safetensors
    

## 

​

FP8 version

By default we are using bf16, which requires high VRAM. For lower VRAM usage, you can use the fp8 version:

  * [qwen_image_layered_fp8mixed.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-Layered_ComfyUI/blob/main/split_files/diffusion_models/qwen_image_layered_fp8mixed.safetensors)

Then update the **Load Diffusion model** node inside the [Subgraph](https://docs.comfy.org/interface/features/subgraph) to use it.

## 

​

Layers and output

The number of layers is set by the `layers` widget on the **Empty Qwen Image Layered Latent** node inside the [Subgraph](https://docs.comfy.org/interface/features/subgraph). This model regenerates the full image as well as the layers, so a generation always decodes to `layers + 1` images:

`layers`| Images decoded| Contents  
---|---|---  
`0`| 1| The full image only  
`2` (template default)| 3| The full image, then 2 layers  
`5`| 6| The full image, then 5 layers  
  
**The first image is the full image, not a layer.** The image to layers workflow drops it automatically with a `LatentCut` node (`dim` `t`, `index` `1`) before the batch split, so the template outputs `layers` images. If you build a custom graph without that node, discard the first image when you only want the layers. `layers` accepts `0`, which gives you that image on its own. **Compositing all of the layers back together recreates the full image.** Use it as a check: if stacking the layers does not reproduce the first image, the decomposition did not do what you wanted.

### 

​

How the layers become separate images

The **Empty Qwen Image Layered Latent** node allocates a 5D latent shaped `[batch_size, 16, layers + 1, height // 8, width // 8]`. The layers sit on the third axis, the same temporal axis that video models use for frames. The **LatentCutToBatch** node with `dim` set to `t` moves that axis into the batch dimension, so after **VAE Decode** each layer is a separate image in the batch. The template inserts a `LatentCut` node (`dim` `t`, `index` `1`) before `LatentCutToBatch` to drop the full-image entry, so the decoded batch contains only the layers. A layer’s position in the stack is therefore its index in the batch, counting from the full image at index 0. There is no z-index field and no per-layer metadata carrying that order, so reordering or filtering the batch reorders the layers. The Qwen-Image-Layered VAE decodes to 4 channels, so the decoded layers carry an alpha channel.

## 

​

Workflow settings

### 

​

Sampler settings

This model is slow. The original sampling settings are steps: 50 and CFG: 4.0, which will at least double the generation time.

### 

​

Input size

For input size, 640px is recommended. Use 1024px for high-resolution output.

### 

​

Prompt (optional)

The text prompt is intended to describe the overall content of the input image, including elements that may be partially occluded (e.g., you may specify the text hidden behind a foreground object). It is not designed to control the semantic content of individual layers explicitly.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/image/qwen/qwen-image-layered.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/image/qwen/qwen-image-layered)

[Qwen-Image-Edit-2511 ComfyUI Native Workflow ExamplePrevious](https://docs.comfy.org/tutorials/image/qwen/qwen-image-edit-2511)[Qwen-Image-2.1 ComfyUI Native Workflow ExampleNext](https://docs.comfy.org/tutorials/image/qwen/qwen-image-2-1)

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
