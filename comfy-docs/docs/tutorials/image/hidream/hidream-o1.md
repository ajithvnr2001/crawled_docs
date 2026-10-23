---
url: https://docs.comfy.org/tutorials/image/hidream/hidream-o1/
title: ComfyUI Native HiDream-O1-Image Workflow Example - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:21.715306+00:00
---

# ComfyUI Native HiDream-O1-Image Workflow Example - ComfyUI

> Source: https://docs.comfy.org/tutorials/image/hidream/hidream-o1/

## On this page

  * Model Versions
  * HiDream-O1-Image Full Workflow
    * HiDream O1 Full: Image generation
    * 1\. Download Workflow
    * 2\. Download Models
    * 3\. Using the Workflow
  * HiDream-O1-Image Dev Workflow
    * HiDream O1 Dev
    * 1\. Download Workflow
    * 2\. Download Models
    * 3\. Using the Workflow
  * Additional Notes



HiDream

# ComfyUI Native HiDream-O1-Image Workflow Example

Copy pageCopy page

This guide walks you through the ComfyUI native HiDream-O1-Image text-to-image and image editing workflows

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

![HiDream-O1-Image Demo](https://raw.githubusercontent.com/HiDream-ai/HiDream-O1-Image/main/assets/general.webp) HiDream-O1-Image is a unified image generative foundation model open-sourced by HiDream-ai on May 8, 2026. Built on a Pixel-level Unified Transformer (UiT), it operates without external VAEs or disjoint text encoders, supporting **text-to-image** , **instruction-based image editing** , **subject-driven personalization** , and **storyboard generation** at up to 2,048 × 2,048 resolution. HiDream-O1-Image is released under the [MIT License](https://github.com/HiDream-ai/HiDream-O1-Image?tab=MIT-1-ov-file) and natively supported in ComfyUI (PR [#13817](https://github.com/Comfy-Org/ComfyUI/pull/13817)). [HiDream-O1-Image - GitHub](https://github.com/HiDream-ai/HiDream-O1-Image)

### 

​

Model Versions

Model| Inference Steps| Repository  
---|---|---  
HiDream-O1-Image (Full)| 50| [🤗 HiDream-O1-Image](https://huggingface.co/HiDream-ai/HiDream-O1-Image)  
HiDream-O1-Image-Dev| 28| [🤗 HiDream-O1-Image-Dev](https://huggingface.co/HiDream-ai/HiDream-O1-Image-Dev)  
  
## 

​

HiDream-O1-Image Full Workflow

### 

​

HiDream O1 Full: Image generation

Input a text prompt and optionally upload reference images. Generate a high-resolution image up to 2048x2048 with text-to-image, editing, or subject-driven personalization. ![HiDream O1 Full workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_hidream_o1-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “HiDream O1 Full” in Template Library

**Example output** ![HiDream O1 Full example output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_hidream_o1.png)

### 

​

1\. Download Workflow

### 

​

2\. Download Models

**Checkpoint** : re-packaged and quantized. All use bf16 for worst outliers, unused deepstack layers removed:

  * [hidream_o1_image_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/HiDream-O1-Image/blob/main/checkpoints/hidream_o1_image_fp8_scaled.safetensors): FP8, uses fp8/mxfp8 matmuls on safe MLP layers for speedup on supported hardware
  * [hidream_o1_image_mxfp8.safetensors](https://huggingface.co/Comfy-Org/HiDream-O1-Image/blob/main/checkpoints/hidream_o1_image_mxfp8.safetensors): MXFP8 quantized variant
  * [hidream_o1_image_bf16.safetensors](https://huggingface.co/Comfy-Org/HiDream-O1-Image/blob/main/checkpoints/hidream_o1_image_bf16.safetensors): Full bf16 precision (largest)

**Text Encoder** (prompt enhancement): shared across all versions:

  * [gemma4_e4b_it_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/gemma-4/blob/main/text_encoders/gemma4_e4b_it_fp8_scaled.safetensors)

**LoRA (optional)** : the Dev distillation can also be applied to the Full model as a LoRA, allowing you to adjust the distillation strength (by [Kijai](https://huggingface.co/Kijai/hidream-O1-image_comfy)):

  * [hidream_o1_dev_lora_rank_64_bf16.safetensors](https://huggingface.co/Kijai/hidream-O1-image_comfy/blob/main/loras/hidream_o1_dev_lora_rank_64_bf16.safetensors): Full rank
  * [hidream_o1_dev_lora_rank_64_bf16_pruned_v1.safetensors](https://huggingface.co/Kijai/hidream-O1-image_comfy/blob/main/loras/hidream_o1_dev_lora_rank_64_bf16_pruned_v1.safetensors): Pruned variant
  * [hidream_o1_image_dev_2604_lora_avg_rankg_224_bf16.safetensors](https://huggingface.co/Kijai/hidream-O1-image_comfy/blob/main/loras/hidream_o1_image_dev_2604_lora_avg_rankg_224_bf16.safetensors): Alternative checkpoint-based distillation


    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 checkpoints/
    │   │   ├── hidream_o1_image_fp8_scaled.safetensors
    │   │   ├── hidream_o1_image_mxfp8.safetensors
    │   │   └── hidream_o1_image_bf16.safetensors
    │   ├── 📂 loras/
    │   │   └── hidream_o1_dev_lora_rank_64_bf16.safetensors
    │   └── 📂 text_encoders/
    │       └── gemma4_e4b_it_fp8_scaled.safetensors
    

### 

​

3\. Using the Workflow

  * Make sure `CheckpointLoaderSimple` loads your chosen checkpoint
  * Enter your prompt in the `CLIPTextEncode` node
  * **Text-to-Image mode:** set the **“Switch to Image Edit”** toggle to **off** (default). The sampler will use your text prompt directly.
  * **Image Edit mode:** set **“Switch to Image Edit”** to **on** , then upload a reference image in the `Load Image` node and connect it to `HiDreamO1ReferenceImages`.



> **Note:** The O1 sampler outputs latent samples that need to be decoded through a `VAEDecode` node using the VAE loaded by `CheckpointLoaderSimple`.

## 

​

HiDream-O1-Image Dev Workflow

### 

​

HiDream O1 Dev

Input a text prompt and optional reference images. Generate a high-resolution image (up to 2048x2048) with support for text-to-image, image editing, and subject-driven personalization. ![HiDream O1 Dev workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_hidream_o1_dev-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “HiDream O1 Dev” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## noir_portrait.png

`LoadImage` node 213 · `noir_portrait.png`

![noir_portrait.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/noir_portrait.png)

**Example output**

![Input image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/noir_portrait.png)![HiDream O1 Dev example output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_hidream_o1_dev.png)

### 

​

1\. Download Workflow

### 

​

2\. Download Models

**Checkpoint (Dev)** : re-packaged and quantized. All use bf16 for worst outliers, unused deepstack layers removed:

  * [hidream_o1_image_dev_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/HiDream-O1-Image/blob/main/checkpoints/hidream_o1_image_dev_fp8_scaled.safetensors): FP8, uses fp8/mxfp8 matmuls on safe MLP layers for speedup on supported hardware
  * [hidream_o1_image_dev_mxfp8.safetensors](https://huggingface.co/Comfy-Org/HiDream-O1-Image/blob/main/checkpoints/hidream_o1_image_dev_mxfp8.safetensors): MXFP8 quantized variant
  * [hidream_o1_image_dev_bf16.safetensors](https://huggingface.co/Comfy-Org/HiDream-O1-Image/blob/main/checkpoints/hidream_o1_image_dev_bf16.safetensors): Full bf16 precision (largest)

**Text Encoder** (prompt enhancement): shared across all versions:

  * [gemma4_e4b_it_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/gemma-4/blob/main/text_encoders/gemma4_e4b_it_fp8_scaled.safetensors)


    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 checkpoints/
    │   │   ├── hidream_o1_image_dev_fp8_scaled.safetensors
    │   │   ├── hidream_o1_image_dev_mxfp8.safetensors
    │   │   └── hidream_o1_image_dev_bf16.safetensors
    │   └── 📂 text_encoders/
    │       └── gemma4_e4b_it_fp8_scaled.safetensors
    

### 

​

3\. Using the Workflow

  * Make sure `CheckpointLoaderSimple` loads `hidream_o1_image_dev_fp8_scaled.safetensors`
  * The Dev version uses 28 steps with CFG=1.0, no negative prompt needed
  * **Text-to-Image mode:** set the **“Switch to Image Edit”** toggle to **off** (default)
  * **Image Edit mode:** set **“Switch to Image Edit”** to **on** , upload a reference image in `Load Image`, and connect it to `HiDreamO1ReferenceImages`



## 

​

Additional Notes

  * **Long Text Rendering:** HiDream-O1-Image excels at rendering text within images. Specify text content, font style, color, and positioning in your prompt for best results. ![Long-Text Rendering & Layout Control](https://raw.githubusercontent.com/HiDream-ai/HiDream-O1-Image/main/assets/text-layout.webp)
  * **Image Scaling:** If your input reference image is too large, enable the `ImageScaleToTotalPixels` node (Ctrl+B) to scale it to 4MP.
  * **Patch Seam Smoothing (Experimental):** The `HiDreamO1PatchSeamSmoothing` node reduces visible seam artifacts during sampling. Enabled by default in the Full workflow.



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/image/hidream/hidream-o1.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/image/hidream/hidream-o1)

[HiDream-E1 and E1.1 in ComfyUI: Instruct Image EditingPrevious](https://docs.comfy.org/tutorials/image/hidream/hidream-e1)[Ovis-Image ComfyUI Workflow ExampleNext](https://docs.comfy.org/tutorials/image/ovis/ovis-image)

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
