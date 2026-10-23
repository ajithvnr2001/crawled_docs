---
url: https://docs.comfy.org/tutorials/video/wan/wan-move/
title: ComfyUI Wan-Move Workflow Example - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:46.980550+00:00
---

# ComfyUI Wan-Move Workflow Example - ComfyUI

> Source: https://docs.comfy.org/tutorials/video/wan/wan-move/

## On this page

  * Wan-Move image-to-video workflow
  * Model links



Wan2.1

# ComfyUI Wan-Move Workflow Example

Copy pageCopy page

Generate motion-controllable video with Wan-Move in ComfyUI: guide object motion with point trajectories for precise image-to-video generation.

Copy pageCopy page

**Wan-Move** is a motion-controllable video generation framework developed by Alibaba’s Tongyi Lab. It enables users to control object motion in generated videos by specifying point trajectories on the input image, making image-to-video generation more precise and controllable. **Key Features** :

  * **High-Quality 5s 480p Motion Control** : Generates 5-second, 480p videos with fine-grained motion controllability
  * **Latent Trajectory Guidance** : Represents motion conditions by propagating first frame features along trajectories
  * **Fine-grained Point-level Control** : Object motions are represented with dense point trajectories, enabling precise region-level control
  * **No Architecture Changes** : Seamlessly integrates into Wan-I2V-14B without extra motion modules

**Related Links** :

  * [GitHub](https://github.com/ali-vilab/Wan-Move)
  * [Hugging Face](https://huggingface.co/Ruihang/Wan-Move-14B-480P)
  * [Paper](https://arxiv.org/abs/2512.08765)



## 

​

Wan-Move image-to-video workflow

Preview the workflow output: ![Wan-Move preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wanmove_480p-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Wan-Move Motion-Control” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## snowboard_rush.png

`LoadImage` node · `snowboard_rush.png`

![snowboard_rush.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/snowboard_rush.png)

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

## Checkpoint: Wan21-WanMove

Place in `ComfyUI/models/diffusion_models/`

## LoRA: LightX2V Distilled

Place in `ComfyUI/models/loras/`

## Text Encoder: umt5

Place in `ComfyUI/models/text_encoders/`

## CLIP Vision: clip_vision_h

Place in `ComfyUI/models/clip_vision/`

## VAE: wan_2.1_vae

Place in `ComfyUI/models/vae/`

**Model Storage Location**
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 text_encoders/
    │   │      └── umt5_xxl_fp8_e4m3fn_scaled.safetensors
    │   ├── 📂 clip_vision/
    │   │      └── clip_vision_h.safetensors
    │   ├── 📂 loras/
    │   │      └── lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors
    │   ├── 📂 diffusion_models/
    │   │      └── Wan21-WanMove_fp8_scaled_e4m3fn_KJ.safetensors
    │   └── 📂 vae/
    │          └── wan_2.1_vae.safetensors
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/video/wan/wan-move.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/video/wan/wan-move)

[ComfyUI Wan2.1 VACE Video ExamplesPrevious](https://docs.comfy.org/tutorials/video/wan/vace)[Wan-Alpha TutorialNext](https://docs.comfy.org/tutorials/video/wan/wan-alpha)

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
