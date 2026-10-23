---
url: https://docs.comfy.org/tutorials/flux/flux1-krea-dev/
title: FLUX.1 Krea Dev ComfyUI Workflow Tutorial - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:20.512199+00:00
---

# FLUX.1 Krea Dev ComfyUI Workflow Tutorial - ComfyUI

> Source: https://docs.comfy.org/tutorials/flux/flux1-krea-dev/

## On this page

  * FLUX.1 Krea Dev ComfyUI Workflow
    * FLUX.1 Krea Dev
    * 1\. Workflow Files
    * 2\. Manual Model Installation
    * 3\. Step-by-step Verification to Ensure Workflow Runs Properly



FLUX

# FLUX.1 Krea Dev ComfyUI Workflow Tutorial

Copy pageCopy page

Generate images with the open-source FLUX.1 Krea Dev model in ComfyUI, built by Black Forest Labs and Krea for natural details and distinctive aesthetics.

Copy pageCopy page

![FLUX.1 Krea Dev Poster](https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_1_krea_dev_poster.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=79640b1911971da78cf2bedb7b3b75ca) [FLUX.1 Krea Dev](https://huggingface.co/black-forest-labs/FLUX.1-Krea-dev) is an advanced text-to-image generation model developed in collaboration between Black Forest Labs (BFL) and Krea. This is currently the best open-source FLUX model, specifically designed for text-to-image generation. **Model Features**

  * **Unique Aesthetic Style** : Focuses on generating images with unique aesthetics, avoiding common “AI look” appearance
  * **Natural Details** : Does not produce blown-out highlights, maintaining natural detail representatio
  * **Exceptional Realism** : Provides outstanding realism and image quality
  * **Fully Compatible Architecture** : Fully compatible architecture design with FLUX.1 [dev]

**Model License** This model is released under the [flux-1-dev-non-commercial-license](https://huggingface.co/black-forest-labs/FLUX.1-Krea-dev/blob/main/LICENSE.md)

## 

​

FLUX.1 Krea Dev ComfyUI Workflow

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

FLUX.1 Krea Dev

A fine-tuned FLUX model pushing photorealism to the max. ![FLUX.1 Krea Dev workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/flux1_krea_dev-1.webp)

## Run on Comfy Cloud

Run this workflow on Comfy Cloud

## Download Workflow

Download JSON or search “FLUX.1 Krea Dev” in Template Library

**Example output** ![FLUX.1 Krea Dev example output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/flux1_krea_dev.png)

#### 

​

1\. Workflow Files

#### 

​

2\. Manual Model Installation

Please download the following model files: **Diffusion model**

  * [flux1-krea-dev_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/FLUX.1-Krea-dev_ComfyUI/blob/main/split_files/diffusion_models/flux1-krea-dev_fp8_scaled.safetensors)

If you want to pursue higher quality and have enough VRAM, you can try the original model weights

  * [flux1-krea-dev.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-Krea-dev/blob/main/flux1-krea-dev.safetensors)



The `flux1-dev.safetensors` file requires agreeing to the [black-forest-labs/FLUX.1-Krea-dev](https://huggingface.co/black-forest-labs/FLUX.1-Krea-dev/) agreement before downloading via browser.

If you have used FLUX related workflows before, the following models are the same and don’t need to be downloaded again **Text encoders**

  * [clip_l.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/blob/main/clip_l.safetensors?download=true)
  * [t5xxl_fp16.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/blob/main/t5xxl_fp16.safetensors?download=true) Recommended when your VRAM is greater than 32GB.
  * [t5xxl_fp8_e4m3fn.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/blob/main/t5xxl_fp8_e4m3fn.safetensors) For Low VRAM

**VAE**

  * [ae.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-schnell/blob/main/ae.safetensors?download=true)

File save location:
    
    
    ComfyUI/
    ├── models/
    │   ├── diffusion_models/
    │   │   └── flux1-krea-dev_fp8_scaled.safetensors or flux1-krea-dev.safetensors
    │   ├── text_encoders/
    │   │   ├── clip_l.safetensors
    │   │   └── t5xxl_fp16.safetensors or t5xxl_fp8_e4m3fn.safetensors
    │   ├── vae/
    │   │   └── ae.safetensors
    
    

#### 

​

3\. Step-by-step Verification to Ensure Workflow Runs Properly

For low VRAM users, this model may not run smoothly on your device, you can wait for the community to provide FP8 or GGUF version.

Please refer to the image below to ensure all model files have been loaded correctly ![ComfyUI FLUX Krea Dev Workflow](https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_1_krea_dev_guide.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=8475817d518de939bb6c5aabf8c1770e)

  1. Ensure that `flux1-krea-dev_fp8_scaled.safetensors` or `flux1-krea-dev.safetensors` is loaded in the `Load Diffusion Model` node 
     * `flux1-krea-dev_fp8_scaled.safetensors` is recommended for low VRAM users
     * `flux1-krea-dev.safetensors` is the original weights, if you have enough VRAM like 24GB you can use it for better quality
  2. Ensure the following models are loaded in the `DualCLIPLoader` node: 
     * clip_name1: t5xxl_fp16.safetensors or t5xxl_fp8_e4m3fn.safetensors
     * clip_name2: clip_l.safetensors
  3. Ensure that `ae.safetensors` is loaded in the `Load VAE` node
  4. Click the `Queue` button, or use the shortcut `Ctrl(cmd) + Enter` to run the workflow



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/flux/flux1-krea-dev.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/flux/flux1-krea-dev)

[FLUX 3 Image Klein in ComfyUI: Text-to-Image and EditPrevious](https://docs.comfy.org/tutorials/flux/flux-3-klein)[ComfyUI FLUX Kontext Dev Native Workflow ExampleNext](https://docs.comfy.org/tutorials/flux/flux-1-kontext-dev)

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
