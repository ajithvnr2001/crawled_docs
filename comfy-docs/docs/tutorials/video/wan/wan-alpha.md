---
url: https://docs.comfy.org/tutorials/video/wan/wan-alpha/
title: Wan-Alpha Tutorial - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:46.136800+00:00
---

# Wan-Alpha Tutorial - ComfyUI

> Source: https://docs.comfy.org/tutorials/video/wan/wan-alpha/

## On this page

  * Video tutorial
  * Resources
  * Wan-Alpha Text-to-Video Workflow (14B)
    * 1\. Download the Workflow
    * 2\. Install Models
    * 3\. Complete the Workflow Step by Step



Wan2.1

# Wan-Alpha Tutorial

Copy pageCopy page

Learn how to generate videos with alpha channel transparency using Wan-Alpha in ComfyUI

Copy pageCopy page

Wan-Alpha is a specialized text-to-video model that generates high-quality videos with alpha channel transparency. Built on the Wan2.1-14B-T2V base model, it creates videos with transparent backgrounds and semi-transparent objects, perfect for compositing workflows. The model excels at generating transparent backgrounds, semi-transparent objects (bubbles, glass, water), glowing effects, and fine details with proper alpha channels (hair, smoke, particles).

# 

​

Video tutorial

## 

​

Resources

  * [Wan-Alpha GitHub](https://github.com/WeChatCV/Wan-Alpha)
  * [Hugging Face Model](https://huggingface.co/htdong/Wan-Alpha)
  * [ComfyUI Version](https://huggingface.co/htdong/Wan-Alpha_ComfyUI)
  * [Research Paper](https://arxiv.org/pdf/2509.24979)



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

Wan-Alpha Text-to-Video Workflow (14B)

### 

​

1\. Download the Workflow

Update your ComfyUI to the latest version, then download and drag the workflow file into ComfyUI, or find “Wan 2.1 Alpha T2V 14B” in the Template Library under `Workflow` → `Browse Templates` → `Video`. ![Wan-Alpha T2V workflow](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan2.1_alpha_t2v_14B-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Wan 2.1 Alpha T2V 14B” in Template Library

### 

​

2\. Install Models

All models mentioned can be found at [Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged). **Diffusion Models** : Choose one version:

## wan2.1_t2v_14B_fp8_scaled.safetensors

FP8 scaled diffusion model. Place in `ComfyUI/models/diffusion_models/`

## wan2.1_t2v_14B_bf16.safetensors

BF16 diffusion model. Place in `ComfyUI/models/diffusion_models/`

**Text Encoder**

## umt5_xxl_fp8_e4m3fn_scaled.safetensors

FP8 text encoder. Place in `ComfyUI/models/text_encoders/`

**VAE Models**

## wan_alpha_2.1_vae_rgb_channel.safetensors

RGB channel VAE. Place in `ComfyUI/models/vae/`

## wan_alpha_2.1_vae_alpha_channel.safetensors

Alpha channel VAE. Place in `ComfyUI/models/vae/`

**LoRA Models**

## wan_alpha_2.1_rgba_lora.safetensors

Alpha generation LoRA. Place in `ComfyUI/models/loras/`

## lightx2v_T2V_14B_cfg_step_distill_v2_lora_rank64_bf16.safetensors

Lightning LoRA for fast inference. Place in `ComfyUI/models/loras/`

File storage locations:
    
    
    ComfyUI/
    ├── models/
    │   ├── diffusion_models/
    │   │   ├── wan2.1_t2v_14B_fp8_scaled.safetensors
    │   │   └── wan2.1_t2v_14B_bf16.safetensors
    │   ├── text_encoders/
    │   │   └── umt5_xxl_fp8_e4m3fn_scaled.safetensors
    │   ├── vae/
    │   │   ├── wan_alpha_2.1_vae_rgb_channel.safetensors
    │   │   └── wan_alpha_2.1_vae_alpha_channel.safetensors
    │   └── loras/
    │       ├── wan_alpha_2.1_rgba_lora.safetensors
    │       └── lightx2v_T2V_14B_cfg_step_distill_v2_lora_rank64_bf16.safetensors
    

### 

​

3\. Complete the Workflow Step by Step

  1. Ensure the correct diffusion model is loaded in the `Load Diffusion Model` node
  2. Ensure the `Load CLIP` node has loaded `umt5_xxl_fp8_e4m3fn_scaled.safetensors`
  3. Ensure the `Load VAE` node for RGB has loaded `wan_alpha_2.1_vae_rgb_channel.safetensors`
  4. Ensure the second `Load VAE` node for Alpha has loaded `wan_alpha_2.1_vae_alpha_channel.safetensors`
  5. Ensure the `LoRA Loader` node has loaded `wan_alpha_2.1_rgba_lora.safetensors`
  6. (Optional) Load `lightx2v_T2V_14B_cfg_step_distill_v2_lora_rank64_bf16.safetensors` in the Lightning LoRA node for faster generation
  7. Set your positive prompt in the `CLIP Text Encode (Positive Prompt)` node
  8. (Optional) Modify video dimensions in the `EmptyHunyuanLatentVideo` node
  9. Click the `Run` button or use `Ctrl(Cmd) + Enter` to execute generation



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/video/wan/wan-alpha.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/video/wan/wan-alpha)

[ComfyUI Wan-Move Workflow ExamplePrevious](https://docs.comfy.org/tutorials/video/wan/wan-move)[Wan ATI Native WorkflowNext](https://docs.comfy.org/tutorials/video/wan/wan-ati)

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
