---
url: https://docs.comfy.org/tutorials/image/qwen/qwen-image-edit/
title: Qwen-Image-Edit ComfyUI Native Workflow Example - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:23.697937+00:00
---

# Qwen-Image-Edit ComfyUI Native Workflow Example - ComfyUI

> Source: https://docs.comfy.org/tutorials/image/qwen/qwen-image-edit/

## On this page

  * ComfyOrg Qwen-Image-Edit Live Stream
  * Qwen-Image-Edit ComfyUI Native Workflow Example
    * Qwen Image Edit
    * 1\. Workflow File
    * 2\. Model Download
    * 3\. Follow the Steps to Complete the Workflow



Qwen

# Qwen-Image-Edit ComfyUI Native Workflow Example

Copy pageCopy page

Qwen-Image-Edit is the image editing version of Qwen-Image, further trained based on the 20B model, supporting precise text editing and dual semantic/appearance editing capabilities.

Copy pageCopy page

**Qwen-Image-Edit** is the image editing version of Qwen-Image. It is further trained based on the 20B Qwen-Image model, successfully extending Qwen-Image’s unique text rendering capabilities to editing tasks, enabling precise text editing. In addition, Qwen-Image-Edit feeds the input image into both Qwen2.5-VL (for visual semantic control) and the VAE Encoder (for visual appearance control), thus achieving dual semantic and appearance editing capabilities. **Model Features** Features include:

  * Precise Text Editing: Qwen-Image-Edit supports bilingual (Chinese and English) text editing, allowing direct addition, deletion, and modification of text in images while preserving the original text size, font, and style.
  * Dual Semantic/Appearance Editing: Qwen-Image-Edit supports not only low-level visual appearance editing (such as style transfer, addition, deletion, modification, etc.) but also high-level visual semantic editing (such as IP creation, object rotation, etc.).
  * Strong Cross-Benchmark Performance: Evaluations on multiple public benchmarks show that Qwen-Image-Edit achieves SOTA in editing tasks, making it a powerful foundational model for image generation.

**Official Links** :

  * [GitHub Repository](https://github.com/QwenLM/Qwen-Image)
  * [Hugging Face](https://huggingface.co/Qwen/Qwen-Image-Edit)
  * [ModelScope](https://modelscope.cn/models/qwen/Qwen-Image-Edit)



## 

​

ComfyOrg Qwen-Image-Edit Live Stream

## 

​

Qwen-Image-Edit ComfyUI Native Workflow Example

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

Qwen Image Edit

Edit images with precise bilingual text editing and dual semantic/appearance editing capabilities using Qwen-Image-Edit’s 20B MMDiT model. ![Qwen-Image-Edit workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_image_edit-1.webp)

## Run on Comfy Cloud

Run this workflow on Cloud GPUs with zero setup

## Download Workflow

Download JSON or search “Qwen Image Edit” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## image_qwen_image_edit_input_image.png

`LoadImage` node 78 · `image_qwen_image_edit_input_image.png`

![image_qwen_image_edit_input_image.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/image_qwen_image_edit_input_image.png)

**Example output**

![Input image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/image_qwen_image_edit_input_image.png)![Qwen-Image-Edit example output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_qwen_image_edit.jpg)

### 

​

1\. Workflow File

### 

​

2\. Model Download

All models can be found at [Comfy-Org/Qwen-Image_ComfyUI](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/tree/main) or [Comfy-Org/Qwen-Image-Edit_ComfyUI](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI) **Diffusion model**

  * [qwen_image_edit_fp8_e4m3fn.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI/blob/main/split_files/diffusion_models/qwen_image_edit_fp8_e4m3fn.safetensors)

**LoRA**

  * [Qwen-Image-Lightning-4steps-V1.0.safetensors](https://huggingface.co/lightx2v/Qwen-Image-Lightning/blob/main/Qwen-Image-Lightning-4steps-V1.0.safetensors)

**Text encoder**

  * [qwen_2.5_vl_7b_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/blob/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors)

**VAE**

  * [qwen_image_vae.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/blob/main/split_files/vae/qwen_image_vae.safetensors)

Model Storage Location
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   └── qwen_image_edit_fp8_e4m3fn.safetensors
    │   ├── 📂 loras/
    │   │   └── Qwen-Image-Lightning-4steps-V1.0.safetensors
    │   ├── 📂 vae/
    │   │   └── qwen_image_vae.safetensors
    │   └── 📂 text_encoders/
    │       └── qwen_2.5_vl_7b_fp8_scaled.safetensors
    

### 

​

3\. Follow the Steps to Complete the Workflow

![Steps Diagram](https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/qwen_image_edit.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=98a706bfa8f1578a4dfd7f2a0a415926)

  1. Model Loading 
     * Ensure the `Load Diffusion Model` node loads `qwen_image_edit_fp8_e4m3fn.safetensors`
     * Ensure the `Load CLIP` node loads `qwen_2.5_vl_7b_fp8_scaled.safetensors`
     * Ensure the `Load VAE` node loads `qwen_image_vae.safetensors`
  2. Image Loading 
     * Ensure the `Load Image` node uploads the image to be edited
  3. Prompt Setting 
     * Set the prompt in the `CLIP Text Encoder` node
  4. The Scale Image to Total Pixels node will scale your input image to a total of one million pixels, 
     * Mainly to avoid quality loss in output images caused by oversized input images such as 2048x2048
     * If you are familiar with your input image size, you can bypass this node using `Ctrl+B`
  5. If you want to use the 4-step Lighting LoRA to speed up image generation, you can select the `LoraLoaderModelOnly` node and press `Ctrl+B` to enable it
  6. For the `steps` and `cfg` settings of the Ksampler node, we’ve added a note below the node where you can test the optimal parameter settings
  7. Click the `Queue` button, or use the shortcut `Ctrl(cmd) + Enter` to run the workflow



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/image/qwen/qwen-image-edit.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/image/qwen/qwen-image-edit)

[Qwen-Image-2512 ComfyUI Native Workflow ExamplePrevious](https://docs.comfy.org/tutorials/image/qwen/qwen-image-2512)[Qwen-Image-Edit-2511 ComfyUI Native Workflow ExampleNext](https://docs.comfy.org/tutorials/image/qwen/qwen-image-edit-2511)

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
