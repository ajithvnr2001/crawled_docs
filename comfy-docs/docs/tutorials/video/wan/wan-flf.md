---
url: https://docs.comfy.org/tutorials/video/wan/wan-flf/
title: Wan2.1 FLF2V in ComfyUI: First and Last Frame Video Generation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:46.280194+00:00
---

# Wan2.1 FLF2V in ComfyUI: First and Last Frame Video Generation - ComfyUI

> Source: https://docs.comfy.org/tutorials/video/wan/wan-flf/

## On this page

  * Wan2.1 FLF2V 720P ComfyUI Native Workflow Example
    * 1\. Download Workflow Files and Related Input Files
    * 2\. Manual Model Installation
    * 3\. Complete Workflow Execution Step by Step



Wan2.1

# Wan2.1 FLF2V in ComfyUI: First and Last Frame Video Generation

Copy pageCopy page

Generate 720p video between a first and last frame with the Wan2.1 FLF2V native workflow in ComfyUI, including model files and setup steps.

Copy pageCopy page

Wan FLF2V (First-Last Frame Video Generation) is an open-source video generation model developed by the Alibaba Tongyi Wanxiang team. Its open-source license is [Apache 2.0](https://github.com/Wan-Video/Wan2.1?tab=Apache-2.0-1-ov-file). Users only need to provide two images as the starting and ending frames, and the model automatically generates intermediate transition frames, outputting a logically coherent and naturally flowing 720p high-definition video. **Core Technical Highlights**

  1. **Precise First-Last Frame Control** : The matching rate of first and last frames reaches 98%, defining video boundaries through starting and ending scenes, intelligently filling intermediate dynamic changes to achieve scene transitions and object morphing effects.
  2. **Stable and Smooth Video Generation** : Using CLIP semantic features and cross-attention mechanisms, the video jitter rate is reduced by 37% compared to similar models, ensuring natural and smooth transitions.
  3. **Multi-functional Creative Capabilities** : Supports dynamic embedding of Chinese and English subtitles, generation of anime/realistic/fantasy and other styles, adapting to different creative needs.
  4. **720p HD Output** : Directly generates 1280x720 resolution videos without post-processing, suitable for social media and commercial applications.
  5. **Open-source Ecosystem Support** : Model weights, code, and training framework are fully open-sourced, supporting deployment on mainstream AI platforms.

**Technical Principles and Architecture**

  1. **DiT Architecture** : Based on diffusion models and Diffusion Transformer architecture, combined with Full Attention mechanism to optimize spatiotemporal dependency modeling, ensuring video coherence.
  2. **3D Causal Variational Encoder** : Wan-VAE technology compresses HD frames to 1/128 size while retaining subtle dynamic details, significantly reducing memory requirements.
  3. **Three-stage Training Strategy** : Starting from 480P resolution pre-training, gradually upgrading to 720P, balancing generation quality and computational efficiency through phased optimization.

**Related Links**

  * **GitHub Repository** : [GitHub](https://github.com/Wan-Video/Wan2.1)
  * **Hugging Face Model Page** : [Hugging Face](https://huggingface.co/Wan-AI/Wan2.1-FLF2V-14B-720P)
  * **ModelScope Community** : [ModelScope](https://www.modelscope.cn/models/Wan-AI/Wan2.1-FLF2V-14B-720P)



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

Wan2.1 FLF2V 720P ComfyUI Native Workflow Example

### 

​

1\. Download Workflow Files and Related Input Files

Since this model is trained on high-resolution images, using smaller sizes may not yield good results. In the example, we use a size of 720 * 1280, which may cause users with lower VRAM hard to run smoothly and will take a long time to generate. If needed, please adjust the video generation size for testing. A small generation size may not produce good output with this model, please notice that.

Update your ComfyUI to the latest version, then download and drag the workflow file into ComfyUI, or find “Wan2.1 FLF2V 720P” in the Template Library under `Workflow` → `Browse Templates` → `Video`. ![Wan2.1 FLF2V 720P Workflow Preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/wan2.1_flf2v_720_f16-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Wan2.1 FLF2V” in Template Library

## Start Image: wan2.1_flf2v_720_f16_start_image.png

Starting frame for the video generation (LoadImage node 52). Download and use this image, or replace with your own.

## End Image: wan2.1_flf2v_720_f16_end_image.png

Ending frame for the video generation (LoadImage node 72). Download and use this image, or replace with your own.

### 

​

2\. Manual Model Installation

All models involved in this guide can be found [here](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files). **Diffusion Models** : Choose one version based on your hardware

## Diffusion Model: Wan2.1 FLF2V 14B FP16

wan2.1_flf2v_720p_14B_fp16.safetensors : Full precision, requires more VRAM. Place in `ComfyUI/models/diffusion_models/`

## Diffusion Model: Wan2.1 FLF2V 14B FP8

wan2.1_flf2v_720p_14B_fp8_e4m3fn.safetensors : Quantized version, lower VRAM usage. Place in `ComfyUI/models/diffusion_models/`

If you have previously tried Wan Video related workflows, you may already have the following files.

**Text Encoders** : Choose one version

## Text Encoder: UMT5 XXL FP16

umt5_xxl_fp16.safetensors : Full precision text encoder. Place in `ComfyUI/models/text_encoders/`

## Text Encoder: UMT5 XXL FP8

umt5_xxl_fp8_e4m3fn_scaled.safetensors : Quantized text encoder. Place in `ComfyUI/models/text_encoders/`

**VAE**

## VAE: Wan2.1 VAE

wan_2.1_vae.safetensors : Wan2.1 VAE for encoding/decoding. Place in `ComfyUI/models/vae/`

**CLIP Vision**

## CLIP Vision: CLIP Vision H

clip_vision_h.safetensors : CLIP Vision encoder. Place in `ComfyUI/models/clip_vision/`

File Storage Location
    
    
    ComfyUI/
    ├───📂 models/
    │   ├───📂 diffusion_models/
    │   │   └─── wan2.1_flf2v_720p_14B_fp16.safetensors           # or FP8 version
    │   ├───📂 text_encoders/
    │   │   └─── umt5_xxl_fp8_e4m3fn_scaled.safetensors           # or your chosen version
    │   ├───📂 vae/
    │   │   └─── wan_2.1_vae.safetensors
    │   └───📂 clip_vision/
    │       └─── clip_vision_h.safetensors   
    

### 

​

3\. Complete Workflow Execution Step by Step

![Wan2.1 FLF2V 720P Native Workflow Steps](https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2.1_flf2v_14B_720P_step_guide.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=f52356ef98601526215d4c21802f261f)

  1. Ensure the `Load Diffusion Model` node has loaded `wan2.1_flf2v_720p_14B_fp16.safetensors` or `wan2.1_flf2v_720p_14B_fp8_e4m3fn.safetensors`
  2. Ensure the `Load CLIP` node has loaded `umt5_xxl_fp8_e4m3fn_scaled.safetensors`
  3. Ensure the `Load VAE` node has loaded `wan_2.1_vae.safetensors`
  4. Ensure the `Load CLIP Vision` node has loaded `clip_vision_h.safetensors`
  5. Upload the starting frame to the `Start_image` node
  6. Upload the ending frame to the `End_image` node
  7. (Optional) Modify the positive and negative prompts, both Chinese and English are supported
  8. (**Important**) In `WanFirstLastFrameToVideo` we use 720 _1280 as default size.because it’s a 720P model, so using a small size will not yield good output. Please use size around 720_ 1280 for good generation.
  9. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to execute video generation



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/video/wan/wan-flf.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/video/wan/wan-flf)

[Wan2.1 Fun InP in ComfyUI: First and Last Frame VideoPrevious](https://docs.comfy.org/tutorials/video/wan/fun-inp)[ComfyUI Wan2.1 InfiniteTalk Workflow ExampleNext](https://docs.comfy.org/tutorials/video/wan/wan-infinitetalk)

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
