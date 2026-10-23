---
url: https://docs.comfy.org/tutorials/flux/flux-2-dev/
title: FLUX.2 Dev in ComfyUI: Text-to-Image and Product Mockups - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:20.119467+00:00
---

# FLUX.2 Dev in ComfyUI: Text-to-Image and Product Mockups - ComfyUI

> Source: https://docs.comfy.org/tutorials/flux/flux-2-dev/

## On this page

  * About FLUX.2
  * FLUX.2 Dev
  * FLUX.2 Dev Text to Image
  * Product Mockup
  * Model links



FLUX

# FLUX.2 Dev in ComfyUI: Text-to-Image and Product Mockups

Copy pageCopy page

Run FLUX.2 Dev in ComfyUI for photorealistic images up to 4MP with multi-reference consistency, legible text rendering, and product mockup workflows.

Copy pageCopy page

## 

​

About FLUX.2

[FLUX.2](https://bfl.ai/blog/flux-2) is a next-generation image model from [Black Forest Labs](https://blackforestlabs.ai/), delivering up to 4MP photorealistic output with far better lighting, skin, fabric, and hand detail. It adds reliable multi-reference consistency (up to 10 images), improved editing precision, better visual understanding, and professional-class text rendering. **Key Features:**

  * **Multi-Reference Consistency:** Reliably maintains identity, product geometry, textures, materials, wardrobe, and composition intent across multiple outputs
  * **High-Resolution Photorealism:** Generates images up to 4MP with real-world lighting behavior, spatial reasoning, and physics-aware detail
  * **Professional-Grade Control:** Exact pose control, hex-code accurate brand colors, any aspect ratio, and structured prompting for programmatic workflows
  * **Usable Text Rendering:** Produces clean, legible text across UI screens, infographics, and multi-language content

**Available Models:**

  * **FLUX.2 Dev:** Open-source model (used in this tutorial)
  * **FLUX.2 Pro:** API version from Black Forest Labs



We are using quantized weights in this workflow. The original FLUX.2 repository is available [here](https://huggingface.co/black-forest-labs/FLUX.2-dev/).

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

FLUX.2 Dev

Generate photorealistic images with multi-reference consistency and professional text rendering. ![FLUX.2 Dev workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux2-1.webp)

## Run on Comfy Cloud

Open this workflow directly in Comfy Cloud

## Download Workflow

Download the JSON workflow file for local use

**Input materials** Upload this file to `LoadImage` node **46** :

## Input Image for FLUX.2 Dev

`LoadImage` node 46 · `image_flux2_input_image.png`

![Input Image for FLUX.2 Dev](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/image_flux2_input_image.png)![FLUX.2 Dev example output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_flux2.png)

## 

​

FLUX.2 Dev Text to Image

Text-to-image with enhanced lighting, materials, and realistic details. No input images are required. ![FLUX.2 Dev text-to-image workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux2_text_to_image-1.webp)

## Run on Comfy Cloud

Open this workflow directly in Comfy Cloud

## Download Workflow

Download the JSON workflow file for local use

**Example output** ![FLUX.2 Dev text-to-image example](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_flux2_text_to_image.png)

## 

​

Product Mockup

Create product mockups by applying design patterns to packaging, mugs, and other products using multi-reference consistency. ![FLUX.2 Dev product mockup workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux2_fp8-1.webp)

## Run on Comfy Cloud

Open this workflow directly in Comfy Cloud

## Download Workflow

Download the JSON workflow file for local use

**Input materials** Upload these files to the matching `LoadImage` nodes:

## Input Ref Image for FLUX.2 Dev

`LoadImage` node 42 · `image_flux2_input_ref_image.png`

## Input Illustration for FLUX.2 Dev

`LoadImage` node 46 · `image_flux2_input_Illustration.png`

![Input Ref Image for FLUX.2 Dev](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/image_flux2_input_ref_image.png)![Input Illustration for FLUX.2 Dev](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/image_flux2_input_Illustration.png)

**Example output** ![FLUX.2 Dev product mockup output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_flux2_fp8.png)

## 

​

Model links

**text_encoders**

  * [mistral_3_small_flux2_bf16.safetensors](https://huggingface.co/Comfy-Org/flux2-dev/blob/main/split_files/text_encoders/mistral_3_small_flux2_bf16.safetensors)

**diffusion_models**

  * [flux2_dev_fp8mixed.safetensors](https://huggingface.co/Comfy-Org/flux2-dev/blob/main/split_files/diffusion_models/flux2_dev_fp8mixed.safetensors)

**vae**

  * [flux2-vae.safetensors](https://huggingface.co/Comfy-Org/flux2-dev/blob/main/split_files/vae/flux2-vae.safetensors)

**Model Storage Location**
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 text_encoders/
    │   │      └── mistral_3_small_flux2_bf16.safetensors
    │   ├── 📂 diffusion_models/
    │   │      └── flux2_dev_fp8mixed.safetensors
    │   └── 📂 vae/
    │          └── flux2-vae.safetensors
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/flux/flux-2-dev.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/flux/flux-2-dev)

[Mixing ControlNets in ComfyUI: Region-Based Image ControlPrevious](https://docs.comfy.org/tutorials/controlnet/mixing-controlnets)[ComfyUI FLUX.2 Klein 4B GuideNext](https://docs.comfy.org/tutorials/flux/flux-2-klein)

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
