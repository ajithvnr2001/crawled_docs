---
url: https://docs.comfy.org/tutorials/video/kandinsky/kandinsky-5/
title: Kandinsky 5.0 in ComfyUI: Text-to-Video and Image-to-Video - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:42.780851+00:00
---

# Kandinsky 5.0 in ComfyUI: Text-to-Video and Image-to-Video - ComfyUI

> Source: https://docs.comfy.org/tutorials/video/kandinsky/kandinsky-5/

## On this page

  * Overview
  * Model variants
  * Text-to-Video workflow
    * Kandinsky 5.0 Video Lite Text to Video
    * 2\. Manually download models
  * Image-to-Video workflow
    * Kandinsky 5.0 Video Lite Image to Video
    * 2\. Manually download models
  * Resources



Kandinsky

# Kandinsky 5.0 in ComfyUI: Text-to-Video and Image-to-Video

Copy pageCopy page

Use Kandinsky 5.0 Video Lite in ComfyUI: text-to-video up to 10 seconds and image-to-video at 5 seconds, with 2B-parameter SFT, no-CFG, and distilled variants.

Copy pageCopy page

[Kandinsky 5.0](https://huggingface.co/kandinskylab/Kandinsky-5.0-I2V-Lite-5s) is a family of diffusion models for video and image generation developed by [Kandinsky Lab](https://huggingface.co/kandinskylab). The Kandinsky 5.0 T2V Lite is a lightweight 2B parameter model that ranks among the top open-source video generation models, capable of generating videos up to 10 seconds long.

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

Overview

Kandinsky 5.0 uses a latent diffusion pipeline with Flow Matching and features:

  * **Diffusion Transformer (DiT):** Main generative backbone with cross-attention to text embeddings
  * **Qwen2.5-VL and CLIP:** Provides high-quality text embeddings
  * **HunyuanVideo 3D VAE:** Encodes and decodes video into a latent space

The model family includes multiple variants optimized for different use cases:

  * **SFT model:** Highest generation quality
  * **CFG-distilled:** 2× faster inference
  * **Diffusion-distilled:** 6× faster with minimal quality loss (16 steps)
  * **Pretrain model:** Designed for fine-tuning

All models are available in 5-second and 10-second video generation versions.

## 

​

Model variants

Model| Video Duration| NFE| Latency (H100)  
---|---|---|---  
Kandinsky 5.0 T2V Lite SFT| 5s / 10s| 100| 139s / 224s  
Kandinsky 5.0 T2V Lite no-CFG| 5s / 10s| 50| 77s / 124s  
Kandinsky 5.0 T2V Lite distill| 5s / 10s| 16| 35s / 61s  
Kandinsky 5.0 I2V Lite| 5s| 100| 673s  
  
## 

​

Text-to-Video workflow

### 

​

Kandinsky 5.0 Video Lite Text to Video

A lightweight 2B model that generates videos from English and Russian prompts with high visual quality. ![Kandinsky 5.0 Video Lite Text to Video workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_kandinsky5_t2v-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Kandinsky 5.0 Video Lite Text to Video” in Template Library

### 

​

2\. Manually download models

**Text Encoders**

## Text Encoder: qwen_2.5_vl_7b_fp8_scaled.safetensors

Qwen2.5-VL 7B text encoder (FP8). Place in `ComfyUI/models/text_encoders/`

## Text Encoder: clip_l.safetensors

CLIP-L text encoder. Place in `ComfyUI/models/text_encoders/`

**Diffusion Model**

## Diffusion Model: kandinsky5lite_t2v_sft_5s.safetensors

Kandinsky 5.0 T2V Lite SFT diffusion model (5s). Place in `ComfyUI/models/diffusion_models/`

**VAE**

## VAE: hunyuan_video_vae_bf16.safetensors

HunyuanVideo 3D VAE. Place in `ComfyUI/models/vae/`
    
    
    ComfyUI/
    ├── 📂 models/
    │   ├── 📂 text_encoders/
    │   │      ├── qwen_2.5_vl_7b_fp8_scaled.safetensors
    │   │      └── clip_l.safetensors
    │   ├── 📂 diffusion_models/
    │   │      └── kandinsky5lite_t2v_sft_5s.safetensors
    │   └── 📂 vae/
    │          └── hunyuan_video_vae_bf16.safetensors
    

## 

​

Image-to-Video workflow

### 

​

Kandinsky 5.0 Video Lite Image to Video

A lightweight 2B model that generates videos from English and Russian prompts with high visual quality. ![Kandinsky 5.0 Video Lite Image to Video workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_kandinsky5_i2v-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Kandinsky 5.0 Video Lite Image to Video” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## crystal_flower.png

`LoadImage` node 11 · `crystal_flower.png`

![crystal_flower.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/crystal_flower.png)

### 

​

2\. Manually download models

**Text Encoders**

## Text Encoder: qwen_2.5_vl_7b_fp8_scaled.safetensors

Qwen2.5-VL 7B text encoder (FP8). Place in `ComfyUI/models/text_encoders/`

## Text Encoder: clip_l.safetensors

CLIP-L text encoder. Place in `ComfyUI/models/text_encoders/`

**Diffusion Model**

## Diffusion Model: kandinsky5lite_i2v_5s.safetensors

Kandinsky 5.0 I2V Lite diffusion model (5s). Place in `ComfyUI/models/diffusion_models/`

**VAE**

## VAE: hunyuan_video_vae_bf16.safetensors

HunyuanVideo 3D VAE. Place in `ComfyUI/models/vae/`
    
    
    ComfyUI/
    ├── 📂 models/
    │   ├── 📂 text_encoders/
    │   │      ├── qwen_2.5_vl_7b_fp8_scaled.safetensors
    │   │      └── clip_l.safetensors
    │   ├── 📂 diffusion_models/
    │   │      └── kandinsky5lite_i2v_5s.safetensors
    │   └── 📂 vae/
    │          └── hunyuan_video_vae_bf16.safetensors
    

## 

​

Resources

  * [HuggingFace Model Collection](https://huggingface.co/collections/kandinskylab/kandinsky-50-video-lite)
  * [GitHub Repository](https://github.com/ai-forever/Kandinsky-5)
  * [ComfyUI Integration](https://github.com/ai-forever/Kandinsky-5/blob/main/comfyui/README.md)
  * [Project Page](https://kandinskylab.github.io/kandinsky-5/)



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/video/kandinsky/kandinsky-5.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/video/kandinsky/kandinsky-5)

[Cosmos Predict2 Video2World in ComfyUI: Image to Video GenerationPrevious](https://docs.comfy.org/tutorials/video/cosmos/cosmos-predict2-video2world)[ComfyUI SCAIL-2 Character Replacement Workflow TutorialNext](https://docs.comfy.org/tutorials/video/zai/scail2)

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
