---
url: https://docs.comfy.org/tutorials/image/z-image/z-image/
title: Z-Image ComfyUI Workflow Example - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:24.243655+00:00
---

# Z-Image ComfyUI Workflow Example - ComfyUI

> Source: https://docs.comfy.org/tutorials/image/z-image/z-image/

## On this page

  * Z-Image text-to-image workflow
    * Z-Image: Text to Image
  * Z-Image model downloads



Z-Image

# Z-Image ComfyUI Workflow Example

Copy pageCopy page

Z-Image is a 6B efficient image generation foundation model from Alibaba Tongyi Lab. Its single-stream DiT design targets fine-tuning and custom development.

Copy pageCopy page

**Z-Image (造相)** is a powerful and highly efficient image generation model with **6B** parameters, developed by Alibaba’s Tongyi Lab. It uses a **Scalable Single-Stream DiT** (S3-DiT) architecture where text, visual semantic tokens, and image VAE tokens are concatenated at the sequence level to serve as a unified input stream, maximizing parameter efficiency. Z-Image (Base) is the non-distilled foundation model designed for community-driven fine-tuning and custom development. **Model Highlights** :

  * **Photorealistic Quality** : Delivers strong photorealistic image generation while maintaining excellent aesthetic quality
  * **Accurate Bilingual Text Rendering** : Excels at accurately rendering complex Chinese and English text
  * **Prompt Enhancing & Reasoning**: Prompt Enhancer empowers the model with reasoning capabilities
  * **Fine-tuning Ready** : Ideal base model for custom training and adaptation

**Related Links** :

  * [GitHub](https://github.com/Tongyi-MAI/Z-Image)
  * [Hugging Face](https://huggingface.co/Tongyi-MAI/Z-Image)
  * [ModelScope](https://modelscope.cn/models/Tongyi-MAI/Z-Image)



## 

​

Z-Image text-to-image workflow

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

Z-Image: Text to Image

Foundation for creative freedom. Diverse aesthetics with exceptional photorealistic quality; ideal for fine-tuning; responsive to negative prompts; high generation diversity. ![Z-Image text-to-image workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_z_image-1.webp)

## Run on Comfy Cloud

Run this workflow directly on Comfy Cloud

## Download Workflow

Download the Z-Image text-to-image workflow JSON file

**Example output** ![Z-Image example output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_z_image.png)

## 

​

Z-Image model downloads

## qwen_3_4b.safetensors

Text encoder for Z-Image.

## z_image_bf16.safetensors

Diffusion model for Z-Image.

## ae.safetensors

VAE for Z-Image.

**Model Storage Location**
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 text_encoders/
    │   │      └── qwen_3_4b.safetensors
    │   ├── 📂 diffusion_models/
    │   │      └── z_image_bf16.safetensors
    │   └── 📂 vae/
    │          └── ae.safetensors
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/image/z-image/z-image.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/image/z-image/z-image)

[Qwen-Image-2.1 ComfyUI Native Workflow ExamplePrevious](https://docs.comfy.org/tutorials/image/qwen/qwen-image-2-1)[Z-Image-Turbo ComfyUI Workflow ExampleNext](https://docs.comfy.org/tutorials/image/z-image/z-image-turbo)

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
