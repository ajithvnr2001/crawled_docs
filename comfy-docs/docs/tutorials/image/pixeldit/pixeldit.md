---
url: https://docs.comfy.org/tutorials/image/pixeldit/pixeldit/
title: PixelDiT ComfyUI Workflow Example - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:23.046864+00:00
---

# PixelDiT ComfyUI Workflow Example - ComfyUI

> Source: https://docs.comfy.org/tutorials/image/pixeldit/pixeldit/

## On this page

  * PixelDiT text-to-image workflow
    * Workflow controls
  * Model downloads
    * Model storage location



PixelDiT

# PixelDiT ComfyUI Workflow Example

Copy pageCopy page

PixelDiT is NVIDIA’s pixel-space diffusion transformer for 1024px text-to-image generation. It operates directly in pixel space: no VAE encode/decode required.

Copy pageCopy page

**PixelDiT** is NVIDIA’s pixel-space diffusion transformer for 1024px text-to-image generation. Unlike traditional diffusion models that operate in latent space, PixelDiT generates images directly in pixel space using a dual-level DiT architecture: a patch-level DiT combined with a pixel-level DiT: with MM-DiT fusion for joint attention between text and image tokens. **Model Highlights** :

  * **VAE-free** : generates directly in pixel space; no traditional VAE encode/decode
  * **Dual-level DiT** : patch-level DiT + pixel-level DiT for high-quality generation
  * **Multi aspect ratio** : 1024px base resolution with support for several aspect ratios
  * **~1.3B parameters** : efficient enough for consumer GPUs
  * **License** : NSCLv1 (non-commercial research/evaluation only)

**Related Links** :

  * [Official model on Hugging Face](https://huggingface.co/nvidia/PixelDiT-1300M-1024px)
  * [Comfy-Org/PixelDiT](https://huggingface.co/Comfy-Org/PixelDiT)



## 

​

PixelDiT text-to-image workflow

![PixelDiT text-to-image workflow](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_pixeldit_t2i-1.webp)

## Download Workflow

Download JSON or search “PixelDiT” in Template Library

## Run on Comfy Cloud

Open in cloud

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

The workflow consists of three main nodes:

  1. **ResolutionSelector** : choose your desired output resolution
  2. **Text to Image (PixelDiT) subgraph** : the core generation node with exposed controls for prompt, seed, model selection and resolution
  3. **SaveImage** : saves the generated image



## Learn about Subgraph

This workflow uses Subgraph nodes for modular processing. Check out the Subgraph documentation to learn how to customize and extend the workflow.

### 

​

Workflow controls

The exposed controls on the **Text to Image (PixelDiT)** subgraph node include:

Control| Description  
---|---  
**Positive Prompt**|  The text prompt describing the image you want to generate  
**Negative Prompt**|  Text describing what to avoid in the generated image  
**Seed**|  Random seed for reproducibility  
**UNet Model**|  PixelDiT model checkpoint selection  
**CLIP Model**|  Text encoder model selection  
  
## 

​

Model downloads

PixelDiT uses two model files: a text encoder and the diffusion model.

## Text Encoder

gemma_2_2b_it_elm_bf16.safetensors: Gemma-2-2B-IT text encoder

## Diffusion Model

pixeldit_1300m_1024px_bf16.safetensors: PixelDiT 1300M 1024px diffusion model

### 

​

Model storage location
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 text_encoders/
    │   │      └── gemma_2_2b_it_elm_bf16.safetensors
    │   └── 📂 diffusion_models/
    │          └── pixeldit_1300m_1024px_bf16.safetensors
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/image/pixeldit/pixeldit.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/image/pixeldit/pixeldit)

[Lens ComfyUI workflow examplePrevious](https://docs.comfy.org/tutorials/image/lens/lens)[Krea-2 ComfyUI Workflow ExampleNext](https://docs.comfy.org/tutorials/image/krea/krea-2)

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
