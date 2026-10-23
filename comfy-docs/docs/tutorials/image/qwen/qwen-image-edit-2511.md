---
url: https://docs.comfy.org/tutorials/image/qwen/qwen-image-edit-2511/
title: Qwen-Image-Edit-2511 ComfyUI Native Workflow Example - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:23.466932+00:00
---

# Qwen-Image-Edit-2511 ComfyUI Native Workflow Example - ComfyUI

> Source: https://docs.comfy.org/tutorials/image/qwen/qwen-image-edit-2511/

## On this page

  * Qwen-Image-Edit-2511 ComfyUI Native Workflow Example
    * Qwen Image Edit 2511 - Material Replacement
    * 1\. Workflow file
    * 2\. Model download



Qwen

# Qwen-Image-Edit-2511 ComfyUI Native Workflow Example

Copy pageCopy page

Edit images with Qwen-Image-Edit-2511 in ComfyUI, with improved character consistency, multi-person editing, LoRA support, and stronger geometric reasoning.

Copy pageCopy page

**Qwen-Image-Edit-2511** is an enhanced version of Qwen-Image-Edit-2509, featuring multiple improvements including notably better consistency. This model extends Qwen-Image’s unique text rendering capabilities to editing tasks, enabling precise text editing with dual semantic and appearance editing capabilities. **Key Enhancements in Qwen-Image-Edit-2511** :

  * **Mitigate Image Drift** : Improved stability during editing operations
  * **Improved Character Consistency** : Better preservation of identity and visual characteristics during imaginative edits
  * **Multi-Person Consistency** : High-fidelity fusion of multiple person images into coherent group shots
  * **Integrated LoRA Capabilities** : Popular community LoRAs built directly into the base model
  * **Enhanced Industrial Design Generation** : Better support for batch industrial product design and material replacement
  * **Strengthened Geometric Reasoning** : Direct generation of auxiliary construction lines for design or annotation

**Official Links** :

  * [GitHub Repository](https://github.com/QwenLM/Qwen-Image)
  * [Hugging Face](https://huggingface.co/Qwen/Qwen-Image-Edit-2511)
  * [ModelScope](https://modelscope.cn/models/Qwen/Qwen-Image-Edit-2511)
  * [Tech Report](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/Qwen_Image.pdf)
  * [Blog](https://qwen.ai/blog?id=qwen-image-edit-2511)



## 

​

Qwen-Image-Edit-2511 ComfyUI Native Workflow Example

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

Qwen Image Edit 2511 - Material Replacement

Replace materials in objects (for example, furniture) by combining reference images with Qwen-Image-Edit-2511. ![Qwen-Image-Edit-2511 workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_image_edit_2511-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Qwen-Image-Edit-2511” in Template Library

**Input materials** Upload these files to the matching `LoadImage` nodes:

## leather_sofa.png

`LoadImage` node 41 · `leather_sofa.png`

## texture_fur.png

`LoadImage` node 83 · `texture_fur.png`

![leather_sofa.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/leather_sofa.png)![texture_fur.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/texture_fur.png)

**Example output**

![Input image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/leather_sofa.png)![Qwen-Image-Edit-2511 example output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_qwen_image_edit_2511.png)

### 

​

1\. Workflow file

After updating ComfyUI, you can find the workflow file from the templates, or drag the workflow preview above into ComfyUI to load it.

### 

​

2\. Model download

**Text Encoders**

  * [qwen_2.5_vl_7b_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/blob/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors)

**LoRA (Optional - for 4-step Lightning acceleration)**

  * [Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16.safetensors](https://huggingface.co/lightx2v/Qwen-Image-Edit-2511-Lightning/blob/main/Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16.safetensors)

**Diffusion Models**

  * [qwen_image_edit_2511_bf16.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI/blob/main/split_files/diffusion_models/qwen_image_edit_2511_bf16.safetensors)

**VAE**

  * [qwen_image_vae.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/blob/main/split_files/vae/qwen_image_vae.safetensors)

**Model Storage Location**
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 text_encoders/
    │   │      └── qwen_2.5_vl_7b_fp8_scaled.safetensors
    │   ├── 📂 loras/
    │   │      └── Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16.safetensors
    │   ├── 📂 diffusion_models/
    │   │      └── qwen_image_edit_2511_bf16.safetensors
    │   └── 📂 vae/
    │          └── qwen_image_vae.safetensors
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/image/qwen/qwen-image-edit-2511.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/image/qwen/qwen-image-edit-2511)

[Qwen-Image-Edit ComfyUI Native Workflow ExamplePrevious](https://docs.comfy.org/tutorials/image/qwen/qwen-image-edit)[Qwen-Image-Layered ComfyUI Workflow ExampleNext](https://docs.comfy.org/tutorials/image/qwen/qwen-image-layered)

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
