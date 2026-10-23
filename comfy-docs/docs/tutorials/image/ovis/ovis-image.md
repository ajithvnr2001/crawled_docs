---
url: https://docs.comfy.org/tutorials/image/ovis/ovis-image/
title: Ovis-Image ComfyUI Workflow Example - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:22.935944+00:00
---

# Ovis-Image ComfyUI Workflow Example - ComfyUI

> Source: https://docs.comfy.org/tutorials/image/ovis/ovis-image/

## On this page

  * Ovis-Image text-to-image workflow
    * Ovis-Image Text to Image
  * Model links



Ovis

# Ovis-Image ComfyUI Workflow Example

Copy pageCopy page

Ovis-Image is a 7B text-to-image model for high-quality text rendering in ComfyUI, delivering crisp bilingual text on posters, banners, and UI mockups.

Copy pageCopy page

**Ovis-Image** is a 7B text-to-image model built upon [Ovis-U1](https://github.com/AIDC-AI/Ovis-U1), specifically optimized for high-quality text rendering. It delivers text rendering quality comparable to much larger 20B-class systems while remaining compact enough to run on widely accessible hardware. **Model Highlights** :

  * **Strong Text Rendering at 7B Scale** : Delivers text rendering quality comparable to much larger 20B-class systems like Qwen-Image and competitive with leading closed-source models like GPT4o in text-centric scenarios
  * **High Fidelity on Text-Heavy Prompts** : Excels on prompts that demand tight alignment between linguistic content and rendered typography (e.g., posters, banners, logos, UI mockups, infographics)
  * **Accurate Bilingual Text Rendering** : Produces legible, correctly spelled, and semantically consistent text in both Chinese and English across diverse fonts, sizes, and aspect ratios
  * **Efficiency and Deployability** : Fits on a single high-end GPU with moderate memory, supports low-latency interactive use

**Related Links** :

  * [GitHub](https://github.com/AIDC-AI/Ovis-Image)
  * [Hugging Face](https://huggingface.co/AIDC-AI/Ovis-Image-7B)



## 

​

Ovis-Image text-to-image workflow

### 

​

Ovis-Image Text to Image

Ovis-Image is a 7B text-to-image model specifically optimized for high-quality text rendering in generated images. Designed to operate efficiently under stringent computational constraints. ![Ovis-Image text-to-image workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_ovis_text_to_image-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Ovis image” in Template Library

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

Model links

**text_encoders**

  * [ovis_2.5.safetensors](https://huggingface.co/Comfy-Org/Ovis-Image/blob/main/split_files/text_encoders/ovis_2.5.safetensors)

**diffusion_models**

  * [ovis_image_bf16.safetensors](https://huggingface.co/Comfy-Org/Ovis-Image/blob/main/split_files/diffusion_models/ovis_image_bf16.safetensors)

**vae**

  * [ae.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/blob/main/split_files/vae/ae.safetensors)

**Model Storage Location**
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 text_encoders/
    │   │      └── ovis_2.5.safetensors
    │   ├── 📂 diffusion_models/
    │   │      └── ovis_image_bf16.safetensors
    │   └── 📂 vae/
    │          └── ae.safetensors
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/image/ovis/ovis-image.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/image/ovis/ovis-image)

[ComfyUI Native HiDream-O1-Image Workflow ExamplePrevious](https://docs.comfy.org/tutorials/image/hidream/hidream-o1)[ComfyUI NewBie-image-Exp0.1 Workflow ExampleNext](https://docs.comfy.org/tutorials/image/newbie-image/newbie-image-exp-0-1)

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
