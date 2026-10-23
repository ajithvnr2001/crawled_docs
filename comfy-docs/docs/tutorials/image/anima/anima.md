---
url: https://docs.comfy.org/tutorials/image/anima/anima/
title: Anima Base v1 ComfyUI workflow example - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:20.645256+00:00
---

# Anima Base v1 ComfyUI workflow example - ComfyUI

> Source: https://docs.comfy.org/tutorials/image/anima/anima/

## On this page

  * Available workflows
    * Anima Base v1: Text to Image
    * Get started
    * Anima Preview: Anime Text-to-Image Generation
    * Get started
  * Anima model downloads
    * Preview model
  * Limitations



Anima

# Anima Base v1 ComfyUI workflow example

Copy pageCopy page

Anima is a 2B-parameter text-to-image model by CircleStone Labs / Comfy Org, optimized for anime and non-photorealistic illustration generation.

Copy pageCopy page

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

**Anima** is an open text-to-image model by [CircleStone Labs](https://huggingface.co/circlestone-labs/Anima) in partnership with Comfy Org. With **2 billion** parameters, it is designed to generate high-quality **anime and non-photorealistic** images, ideal for characters, scenes, and concept art. **Model highlights** :

  * **Anime and artistic illustration focus** : tuned for non-photorealistic art styles
  * **ComfyUI native support** : loaded with standard UNETLoader, CLIPLoader, and VAELoader nodes
  * **Qwen-3 0.6B text encoder** : provides strong language understanding and prompt adherence
  * **No input image needed** : pure text-to-image generation
  * **Compact footprint** : 2B diffusion model, runs comfortably on consumer GPUs

**Related links** :

  * [Hugging Face (Anima)](https://huggingface.co/circlestone-labs/Anima)



## 

​

Available workflows

Anima provides two workflows: the base version for standard use and a preview version for early access. Both workflows use a **Subgraph** node to manage the text-to-image generation pipeline. You can open the subgraph to inspect or customize the internal nodes.

## Learn about Subgraph

This workflow uses Subgraph nodes for modular processing. Check out the Subgraph documentation to learn how to customize and extend the workflow.

### 

​

Anima Base v1: Text to Image

Input a text prompt describing an anime or artistic illustration. Generate a non-photorealistic image focused on anime concepts, characters, or styles. ![Anima Base v1 text-to-image workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_anima_base_v1-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Anima Base v1” in Template Library

**Example output** ![Anima Base v1 example output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_anima_base_v1.png)

#### 

​

Get started

  1. Update ComfyUI to the latest version or use [Comfy Cloud](https://cloud.comfy.org/?template=image_anima_base_v1&utm_source=docs&utm_medium=referral&utm_campaign=anima)
  2. Go to **Template** and search for **Anima Base v1**
  3. Select the **Anima Base v1: Text to Image** workflow
  4. Download any missing models (see model downloads), enter your prompt, and click **Queue**



### 

​

Anima Preview: Anime Text-to-Image Generation

Input a text prompt to generate an anime-style image using the Anima model. Configure settings like steps and CFG scale to control the output. ![Anima Preview text-to-image workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_anima_preview-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Anima Preview” in Template Library

**Example output** ![Anima Preview example output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_anima_preview.png)

#### 

​

Get started

  1. Update ComfyUI to the latest version or use [Comfy Cloud](https://cloud.comfy.org/?template=image_anima_preview&utm_source=docs&utm_medium=referral&utm_campaign=anima)
  2. Go to **Template** and search for **Anima Preview**
  3. Select the **Anima Anime Text-to-Image Generation** workflow
  4. Download any missing models (see model downloads), enter your prompt, and click **Queue**



## 

​

Anima model downloads

You can find all model files at [circlestone-labs/Anima](https://huggingface.co/circlestone-labs/Anima) on Hugging Face.

## anima-base-v1.0.safetensors

Diffusion model (2B) for Anima Base v1.

## qwen_3_06b_base.safetensors

Text encoder (Qwen-3 0.6B) shared by both workflows.

## qwen_image_vae.safetensors

VAE shared by both workflows.

**Model storage location**
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   └── anima-base-v1.0.safetensors
    │   ├── 📂 text_encoders/
    │   │   └── qwen_3_06b_base.safetensors
    │   └── 📂 vae/
    │       └── qwen_image_vae.safetensors
    

### 

​

Preview model

If you are using the Preview workflow, download the preview diffusion model instead:

## anima-preview3-base.safetensors

Diffusion model (2B) for Anima Preview.

**Preview model storage location**
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   └── 📂 diffusion_models/
    │       └── anima-preview3-base.safetensors
    

## 

​

Limitations

  * **No realism** : the model is intentionally designed for anime and illustration styles; realistic renderings are out of scope
  * **Weak text rendering** : high-resolution text and complex typography may not render clearly
  * **Plain styling** : the base model produces simpler compositions; advanced artistic styles may require refinement or fine-tuning



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/image/anima/anima.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/image/anima/anima)

[ERNIE-Image ComfyUI workflow examplePrevious](https://docs.comfy.org/tutorials/image/ernie-image/ernie-image)[Lens ComfyUI workflow exampleNext](https://docs.comfy.org/tutorials/image/lens/lens)

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
