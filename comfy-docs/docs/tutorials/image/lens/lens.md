---
url: https://docs.comfy.org/tutorials/image/lens/lens/
title: Lens ComfyUI workflow example - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:22.274598+00:00
---

# Lens ComfyUI workflow example - ComfyUI

> Source: https://docs.comfy.org/tutorials/image/lens/lens/

## On this page

  * Lens text-to-image workflow
    * Lens: Text to Image
    * Get started
    * Lens Turbo: Text to Image
    * Get started
  * Lens model downloads
  * Available models



Lens

# Lens ComfyUI workflow example

Copy pageCopy page

Run Lens, Microsoft’s 3.8B open text-to-image model, in ComfyUI: a dual-stream MMDiT backbone, GPT-OSS-20B text features, and the FLUX.2 semantic VAE.

Copy pageCopy page

**Lens** is an open text-to-image model by **Microsoft** , licensed under MIT. With **3.8 billion** parameters, it uses a **dual-stream MMDiT** architecture with **GPT-OSS-20B** text encoder features and the **FLUX.2 semantic VAE** to deliver competitive image quality with substantially less training compute than larger T2I models. **Model highlights** :

  * **Dual-stream MMDiT architecture** : joint image-text processing for coherent generation
  * **GPT-OSS-20B multi-layer text features** : rich text understanding for accurate prompt following
  * **FLUX.2 semantic VAE** : high-fidelity latent representation
  * **Mixed-resolution training** : supports various aspect ratios without cropping
  * **Compact 3.8B footprint** : runs on consumer GPUs with 24 GB VRAM

**Related links** :

  * [Paper (arXiv)](https://arxiv.org/abs/2605.21573)
  * [GitHub](https://github.com/microsoft/Lens)
  * [Hugging Face (Microsoft)](https://huggingface.co/microsoft/Lens)
  * [Hugging Face (Comfy-Org)](https://huggingface.co/Comfy-Org/Lens)



## 

​

Lens text-to-image workflow

Both the standard and Turbo variants use a **Subgraph** node to manage the text-to-image generation pipeline. You can open the subgraph to inspect or customize the internal nodes.

## Learn about Subgraph

This workflow uses Subgraph nodes for modular processing. Check out the Subgraph documentation to learn how to customize and extend the workflow.

### 

​

Lens: Text to Image

Input a text prompt and select resolution and aspect ratio. Generate a high-quality image using the efficient Lens text-to-image model. ![Lens text-to-image workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_lens_t2i-1.webp)

## Download Workflow

Download JSON or search “Lens” in Template Library

**Example output** ![Lens text-to-image example output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_lens_t2i.png)

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

#### 

​

Get started

  1. Update ComfyUI to the latest version
  2. Go to **Template** and search for **Lens**
  3. Select the **Lens** workflow
  4. Download any missing models (see model downloads), enter your prompt, and click **Queue**



### 

​

Lens Turbo: Text to Image

Input a text prompt and select resolution, aspect ratio, and inference steps. Generate a high-quality image using the Lens text-to-image model. ![Lens Turbo text-to-image workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_lens_turbo_t2i-1.webp)

## Download Workflow

Download JSON or search “Lens Turbo” in Template Library

**Example output** ![Lens Turbo text-to-image example output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_lens_turbo_t2i.png)

#### 

​

Get started

  1. Update ComfyUI to the latest version
  2. Go to **Template** and search for **Lens Turbo**
  3. Select the **Lens Turbo** workflow
  4. Download any missing models (see model downloads), enter your prompt, and click **Queue**



## 

​

Lens model downloads

You can find all model files at [Comfy-Org/Lens](https://huggingface.co/Comfy-Org/Lens) on Hugging Face.

## lens_bf16.safetensors

Diffusion model for Lens (BF16).

## lens_turbo_bf16.safetensors

Diffusion model for Lens Turbo (BF16).

## gpt_oss_20b_nvfp4.safetensors

Text encoder (GPT-OSS-20B) shared by both Lens and Lens Turbo.

## flux2-vae.safetensors

VAE (FLUX.2) shared by both Lens and Lens Turbo.

**Model storage location**
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   ├── lens_bf16.safetensors (or lens_mxfp8.safetensors)
    │   │   └── lens_turbo_bf16.safetensors (or lens_turbo_mxfp8.safetensors)
    │   ├── 📂 text_encoders/
    │   │   └── gpt_oss_20b_nvfp4.safetensors
    │   └── 📂 vae/
    │       └── flux2-vae.safetensors
    

## 

​

Available models

Model| Description| Inference steps| Link  
---|---|---|---  
Lens| Standard 3.8B model: higher quality, more steps| ~50| [Hugging Face](https://huggingface.co/microsoft/Lens)  
Lens Turbo| Distilled variant: faster generation with fewer steps| ~8| [Hugging Face](https://huggingface.co/microsoft/Lens)  
  
Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/image/lens/lens.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/image/lens/lens)

[Anima Base v1 ComfyUI workflow examplePrevious](https://docs.comfy.org/tutorials/image/anima/anima)[PixelDiT ComfyUI Workflow ExampleNext](https://docs.comfy.org/tutorials/image/pixeldit/pixeldit)

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
