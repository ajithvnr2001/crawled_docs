---
url: https://docs.comfy.org/tutorials/image/boogu/boogu-image-0.1
title: Boogu-Image-0.1 ComfyUI Workflow Example - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:20.836407+00:00
---

# Boogu-Image-0.1 ComfyUI Workflow Example - ComfyUI

> Source: https://docs.comfy.org/tutorials/image/boogu/boogu-image-0.1

## On this page

  * Boogu-Image-0.1-Turbo text-to-image workflow
    * Boogu Turbo: Text to Image
    * Boogu-Image-0.1-Turbo model downloads
  * Boogu-Image-0.1-Edit image editing workflow
    * Boogu image 0.1 Edit
    * Boogu-Image-0.1-Edit model downloads



Boogu

# Boogu-Image-0.1 ComfyUI Workflow Example

Copy pageCopy page

Boogu-Image-0.1 is an Apache-2.0 10B parameter image generation and editing model family with text-to-image and instruction-driven editing variants.

Copy pageCopy page

**Boogu-Image-0.1** is an Apache-2.0 open-source unified image generation and editing model family. It uses a system that integrates understanding and generation to deliver competitive performance across photography, text rendering, stylization, and image editing tasks. **Model Variants** :

  * **Boogu-Image-0.1-Turbo** – A four-step distilled text-to-image variant focused on high-quality generation and photorealism, equipped with a LoRA rank-128 module. Requires only 3-4 sampling steps. Recommended as the default for most text-to-image use cases.
  * **Boogu-Image-0.1-Base** – The foundation model with strong diversity and controllability, ideal for fine-tuning and ultra-dense text rendering at 2K resolution.
  * **Boogu-Image-0.1-Edit** – A variant fine-tuned for image editing and transformation tasks with instruction-driven control.

**Model Highlights** :

  * **10B parameters** with efficient inference on consumer GPUs
  * **Apache-2.0 license** for open use and downstream development
  * **Bilingual text rendering** (Chinese and English) with reliable typography
  * **Versatile capabilities** : realistic photography, stylization, poster design, and precise text rendering

**Related Links** :

  * [Project Page](https://boogu.org/)
  * [GitHub](https://github.com/boogu-project/Boogu-Image)
  * [Hugging Face (ComfyUI)](https://huggingface.co/Comfy-Org/Boogu-Image)
  * [Hugging Face (Turbo)](https://huggingface.co/Boogu/Boogu-Image-0.1-Turbo-fp8)
  * [Hugging Face (Edit)](https://huggingface.co/Boogu/Boogu-Image-0.1-Edit-fp8)



## 

​

Boogu-Image-0.1-Turbo text-to-image workflow

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

Boogu Turbo: Text to Image

Generate high-quality images from text prompts using the Boogu Turbo model, a distilled 10B-parameter text-to-image pipeline that produces photorealistic outputs in just 4 steps. ![Boogu Turbo text-to-image workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_boogu_image_0_1_turbo_t2i-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Boogu Turbo” in Template Library

The Boogu-Image-0.1-Turbo workflow uses a subgraph that encapsulates the diffusion, text encoding, and VAE decode pipeline. You provide a text prompt and resolution settings, and the subgraph handles the rest.

### 

​

Boogu-Image-0.1-Turbo model downloads

## boogu_image_turbo_fp8_scaled.safetensors

Diffusion model for Boogu-Image-0.1-Turbo.

## qwen3vl_8b_fp8_scaled.safetensors

Text encoder for Boogu-Image-0.1-Turbo.

## ae.safetensors

VAE for Boogu-Image-0.1-Turbo.

## boogu_image_turbo_lora_rank_128_bf16.safetensors

LoRA module (rank-128) for Boogu-Image-0.1-Turbo.

**Model Storage Location**
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   └── boogu_image_turbo_fp8_scaled.safetensors
    │   ├── 📂 text_encoders/
    │   │   └── qwen3vl_8b_fp8_scaled.safetensors
    │   ├── 📂 vae/
    │   │   └── ae.safetensors
    │   └── 📂 loras/
    │       └── boogu_image_turbo_lora_rank_128_bf16.safetensors
    

## 

​

Boogu-Image-0.1-Edit image editing workflow

### 

​

Boogu image 0.1 Edit

Edit images using Boogu’s instruction-driven model, taking one input image and generating an edited output alongside a side-by-side comparison view. ![Boogu image 0.1 Edit workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_boogu_image_0_1_edit-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Boogu image 0.1 Edit” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## tech_cowboy.png

`LoadImage` node 32 · `tech_cowboy.png`

![tech_cowboy.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/tech_cowboy.png)

### 

​

Boogu-Image-0.1-Edit model downloads

## boogu_image_edit_fp8_scaled.safetensors

Diffusion model for Boogu-Image-0.1-Edit.

## qwen3vl_8b_fp8_scaled.safetensors

Text encoder for Boogu-Image-0.1-Edit.

## ae.safetensors

VAE for Boogu-Image-0.1-Edit.

**Model Storage Location**
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   └── boogu_image_edit_fp8_scaled.safetensors
    │   ├── 📂 text_encoders/
    │   │   └── qwen3vl_8b_fp8_scaled.safetensors
    │   └── 📂 vae/
    │       └── ae.safetensors
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/image/boogu/boogu-image-0.1.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/image/boogu/boogu-image-0.1)

[Z-Image-Turbo ComfyUI Workflow ExamplePrevious](https://docs.comfy.org/tutorials/image/z-image/z-image-turbo)[ComfyUI Native HiDream-I1 Text-to-Image Workflow ExampleNext](https://docs.comfy.org/tutorials/image/hidream/hidream-i1)

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
