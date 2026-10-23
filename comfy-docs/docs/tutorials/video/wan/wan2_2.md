---
url: https://docs.comfy.org/tutorials/video/wan/wan2_2/
title: Wan2.2 Video Generation ComfyUI Official Native Workflow Example - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:48.200565+00:00
---

# Wan2.2 Video Generation ComfyUI Official Native Workflow Example - ComfyUI

> Source: https://docs.comfy.org/tutorials/video/wan/wan2_2/

## On this page

  * Model Highlights
  * Wan2.2 Open Source Model Versions
  * ComfyOrg Wan2.2 Live Streams
  * Wan2.2 TI2V 5B Hybrid Version Workflow Example
    * Wan 2.2 5B Video Generation
    * 2\. Manually Download Models
    * 3\. Follow the Steps
  * Wan2.2 14B T2V Text-to-Video Workflow Example
    * Wan 2.2 14B Text to Video
    * 2\. Manually Download Models
    * 3\. Follow the Steps
  * Wan2.2 14B I2V Image-to-Video Workflow Example
    * Wan 2.2 14B Image to Video
    * 2\. Manually Download Models
    * 3\. Follow the Steps
  * Wan2.2 14B FLF2V Workflow Example
    * Wan 2.2 14B First-Last Frame to Video
    * 2\. Follow the Steps
  * Community Resources
    * GGUF Versions
    * WanVideoWrapper



Wan Video

# Wan2.2 Video Generation ComfyUI Official Native Workflow Example

Copy pageCopy page

Run Wan2.2 video workflows in ComfyUI: the 5B hybrid TI2V model plus 14B text-to-video, image-to-video, and first-last-frame examples, with downloads.

Copy pageCopy page

Wan 2.2 is a new generation multimodal generative model launched by WAN AI. This model adopts an innovative MoE (Mixture of Experts) architecture, consisting of high-noise and low-noise expert models. It can divide expert models according to denoising timesteps, thus generating higher quality video content. Wan 2.2 has three core features: cinematic-level aesthetic control, deeply integrating professional film industry aesthetic standards, supporting multi-dimensional visual control such as lighting, color, and composition; large-scale complex motion, easily restoring various complex motions and enhancing the smoothness and controllability of motion; precise semantic compliance, excelling in complex scenes and multi-object generation, better restoring users’ creative intentions. The model supports multiple generation modes such as text-to-video and image-to-video, suitable for content creation, artistic creation, education and training, and other application scenarios. [Wan2.2 Prompt Guide](https://alidocs.dingtalk.com/i/nodes/EpGBa2Lm8aZxe5myC99MelA2WgN7R35y)

## 

​

Model Highlights

  * **Cinematic-level Aesthetic Control** : Professional camera language, supports multi-dimensional visual control such as lighting, color, and composition
  * **Large-scale Complex Motion** : Smoothly restores various complex motions, enhances motion controllability and naturalness
  * **Precise Semantic Compliance** : Complex scene understanding, multi-object generation, better restoring creative intentions
  * **Efficient Compression Technology** : 5B version with high compression ratio VAE, memory optimization, supports mixed training



## 

​

Wan2.2 Open Source Model Versions

The Wan2.2 series models are based on the Apache 2.0 open source license and support commercial use. The Apache 2.0 license allows you to freely use, modify, and distribute these models, including for commercial purposes, as long as you retain the original copyright notice and license text.

Model Type| Model Name| Parameters| Main Function| Model Repository  
---|---|---|---|---  
Hybrid Model| Wan2.2-TI2V-5B| 5B| Hybrid version supporting both text-to-video and image-to-video, a single model meets two core task requirements| 🤗 [Wan2.2-TI2V-5B](https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B)  
Image-to-Video| Wan2.2-I2V-A14B| 14B| Converts static images into dynamic videos, maintaining content consistency and smooth dynamic process| 🤗 [Wan2.2-I2V-A14B](https://huggingface.co/Wan-AI/Wan2.2-I2V-A14B)  
Text-to-Video| Wan2.2-T2V-A14B| 14B| Generates high-quality videos from text descriptions, with cinematic-level aesthetic control and precise semantic compliance| 🤗 [Wan2.2-T2V-A14B](https://huggingface.co/Wan-AI/Wan2.2-T2V-A14B)  
  
## 

​

ComfyOrg Wan2.2 Live Streams

For ComfyUI Wan2.2 usage, we have conducted live streams, which you can view to learn how to use them.

This tutorial will use the [🤗 Comfy-Org/Wan_2.2_ComfyUI_Repackaged](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged) version.

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

![Wan2.2 template](https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/template.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=ccf5d56775dac715ac40f767978d4371)

## 

​

Wan2.2 TI2V 5B Hybrid Version Workflow Example

The Wan2.2 5B version should fit well on 8GB vram with the ComfyUI native offloading.

### 

​

Wan 2.2 5B Video Generation

Fast text-to-video and image-to-video generation with 5B parameters. Optimized for rapid prototyping and creative exploration. ![Wan 2.2 5B Video Generation workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan2_2_5B_ti2v-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Wan2.2 5B” in Template Library

### 

​

2\. Manually Download Models

All models mentioned can be found at [Comfy-Org/Wan_2.2_ComfyUI_Repackaged](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged). **Diffusion Model**

## wan2.2_ti2v_5B_fp16.safetensors

5B hybrid diffusion model. Place in `ComfyUI/models/diffusion_models/`

**VAE**

## wan2.2_vae.safetensors

Wan2.2 VAE. Place in `ComfyUI/models/vae/`

**Text Encoder**

## umt5_xxl_fp8_e4m3fn_scaled.safetensors

FP8 text encoder. Place in `ComfyUI/models/text_encoders/`
    
    
    ComfyUI/
    ├───📂 models/
    │   ├───📂 diffusion_models/
    │   │   └───wan2.2_ti2v_5B_fp16.safetensors
    │   ├───📂 text_encoders/
    │   │   └─── umt5_xxl_fp8_e4m3fn_scaled.safetensors 
    │   └───📂 vae/
    │       └── wan2.2_vae.safetensors
    

### 

​

3\. Follow the Steps

![Step Diagram](https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_5b_t2v.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=964289dd7f3c51119c95f98372dbd209)

  1. Ensure the `Load Diffusion Model` node loads the `wan2.2_ti2v_5B_fp16.safetensors` model.
  2. Ensure the `Load CLIP` node loads the `umt5_xxl_fp8_e4m3fn_scaled.safetensors` model.
  3. Ensure the `Load VAE` node loads the `wan2.2_vae.safetensors` model.
  4. (Optional) If you need to perform image-to-video generation, you can use the shortcut Ctrl+B to enable the `Load image` node to upload an image.
  5. (Optional) In the `Wan22ImageToVideoLatent` node, you can adjust the size settings and the total number of video frames (`length`).
  6. (Optional) If you need to modify the prompts (positive and negative), please do so in the `CLIP Text Encoder` node at step 5.
  7. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to execute video generation.



## 

​

Wan2.2 14B T2V Text-to-Video Workflow Example

### 

​

Wan 2.2 14B Text to Video

Generate high-quality videos from text prompts with cinematic aesthetic control and dynamic motion generation using Wan 2.2. ![Wan 2.2 14B Text to Video workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan2_2_14B_t2v-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Wan2.2 14B T2V” in Template Library

### 

​

2\. Manually Download Models

All models mentioned can be found at [Comfy-Org/Wan_2.2_ComfyUI_Repackaged](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged). **Diffusion Models**

## wan2.2_t2v_high_noise_14B_fp8_scaled.safetensors

High noise diffusion model. Place in `ComfyUI/models/diffusion_models/`

## wan2.2_t2v_low_noise_14B_fp8_scaled.safetensors

Low noise diffusion model. Place in `ComfyUI/models/diffusion_models/`

**VAE**

## wan_2.1_vae.safetensors

Wan2.1 VAE (compatible with Wan2.2). Place in `ComfyUI/models/vae/`

**Text Encoder**

## umt5_xxl_fp8_e4m3fn_scaled.safetensors

FP8 text encoder. Place in `ComfyUI/models/text_encoders/`
    
    
    ComfyUI/
    ├───📂 models/
    │   ├───📂 diffusion_models/
    │   │   ├─── wan2.2_t2v_low_noise_14B_fp8_scaled.safetensors
    │   │   └─── wan2.2_t2v_high_noise_14B_fp8_scaled.safetensors
    │   ├───📂 text_encoders/
    │   │   └─── umt5_xxl_fp8_e4m3fn_scaled.safetensors 
    │   └───📂 vae/
    │       └── wan_2.1_vae.safetensors
    

### 

​

3\. Follow the Steps

![Step Diagram](https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_t2v.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=0ce44ad0e8f5e8dff6c9324404ee5e46)

  1. Ensure the first `Load Diffusion Model` node loads the `wan2.2_t2v_high_noise_14B_fp8_scaled.safetensors` model.
  2. Ensure the second `Load Diffusion Model` node loads the `wan2.2_t2v_low_noise_14B_fp8_scaled.safetensors` model.
  3. Ensure the `Load CLIP` node loads the `umt5_xxl_fp8_e4m3fn_scaled.safetensors` model.
  4. Ensure the `Load VAE` node loads the `wan_2.1_vae.safetensors` model.
  5. (Optional) In the `EmptyHunyuanLatentVideo` node, you can adjust the size settings and the total number of video frames (`length`).
  6. (Optional) If you need to modify the prompts (positive and negative), please do so in the `CLIP Text Encoder` node at step 5.
  7. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to execute video generation.



## 

​

Wan2.2 14B I2V Image-to-Video Workflow Example

### 

​

Wan 2.2 14B Image to Video

Transform static images into dynamic videos with precise motion control and style preservation using Wan 2.2. ![Wan 2.2 14B Image to Video workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan2_2_14B_i2v-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Wan2.2 14B I2V” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## video_wan2_2_14B_i2v_input_image.jpg

`LoadImage` node 97 · `video_wan2_2_14B_i2v_input_image.jpg`

**Example output**

![Input image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/video_wan2_2_14B_i2v_input_image.jpg)

### 

​

2\. Manually Download Models

All models mentioned can be found at [Comfy-Org/Wan_2.2_ComfyUI_Repackaged](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged). **Diffusion Models**

## wan2.2_i2v_high_noise_14B_fp16.safetensors

High noise I2V diffusion model. Place in `ComfyUI/models/diffusion_models/`

## wan2.2_i2v_low_noise_14B_fp16.safetensors

Low noise I2V diffusion model. Place in `ComfyUI/models/diffusion_models/`

**VAE**

## wan_2.1_vae.safetensors

Wan2.1 VAE (compatible with Wan2.2). Place in `ComfyUI/models/vae/`

**Text Encoder**

## umt5_xxl_fp8_e4m3fn_scaled.safetensors

FP8 text encoder. Place in `ComfyUI/models/text_encoders/`
    
    
    ComfyUI/
    ├───📂 models/
    │   ├───📂 diffusion_models/
    │   │   ├─── wan2.2_i2v_low_noise_14B_fp16.safetensors
    │   │   └─── wan2.2_i2v_high_noise_14B_fp16.safetensors
    │   ├───📂 text_encoders/
    │   │   └─── umt5_xxl_fp8_e4m3fn_scaled.safetensors 
    │   └───📂 vae/
    │       └── wan_2.1_vae.safetensors
    

### 

​

3\. Follow the Steps

![Step Diagram](https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_i2v.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=a9c4c6cfa365f7a0e4d7274b6c799316)

  1. Make sure the first `Load Diffusion Model` node loads the `wan2.2_t2v_high_noise_14B_fp8_scaled.safetensors` model.
  2. Make sure the second `Load Diffusion Model` node loads the `wan2.2_t2v_low_noise_14B_fp8_scaled.safetensors` model.
  3. Make sure the `Load CLIP` node loads the `umt5_xxl_fp8_e4m3fn_scaled.safetensors` model.
  4. Make sure the `Load VAE` node loads the `wan_2.1_vae.safetensors` model.
  5. In the `Load Image` node, upload the image to be used as the initial frame.
  6. If you need to modify the prompts (positive and negative), do so in the `CLIP Text Encoder` node at step 6.
  7. (Optional) In `EmptyHunyuanLatentVideo`, you can adjust the size settings and the total number of video frames (`length`).
  8. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to execute video generation.



## 

​

Wan2.2 14B FLF2V Workflow Example

The first and last frame workflow uses the same model locations as the I2V section.

### 

​

Wan 2.2 14B First-Last Frame to Video

Generate smooth video transitions by defining start and end frames. ![Wan 2.2 14B First-Last Frame to Video workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan2_2_14B_flf2v-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Wan2.2 14B FLF2V” in Template Library

**Input materials** Upload these files to the matching `LoadImage` nodes:

## video_wan2_2_14B_flf2v_start_image.png

`LoadImage` node 62 · `video_wan2_2_14B_flf2v_start_image.png`

## video_wan2_2_14B_flf2v_end_image.png

`LoadImage` node 68 · `video_wan2_2_14B_flf2v_end_image.png`

![video_wan2_2_14B_flf2v_start_image.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/video_wan2_2_14B_flf2v_start_image.png)![video_wan2_2_14B_flf2v_end_image.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/video_wan2_2_14B_flf2v_end_image.png)

### 

​

2\. Follow the Steps

![Step Diagram](https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_flf2v.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=6def22f3de024219e66dd4ea7cae7c03)

  1. Upload the image to be used as the starting frame in the first `Load Image` node.
  2. Upload the image to be used as the ending frame in the second `Load Image` node.
  3. Adjust the size settings in the `WanFirstLastFrameToVideo` node. 
     * By default, a relatively small size is set to prevent low VRAM users from consuming too many resources.
     * If you have enough VRAM, you can try a resolution around 720P.
  4. Write appropriate prompts according to your first and last frames.
  5. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to execute video generation.



## 

​

Community Resources

### 

​

GGUF Versions

  * [bullerwins/Wan2.2-I2V-A14B-GGUF/](https://huggingface.co/bullerwins/Wan2.2-I2V-A14B-GGUF/)
  * [bullerwins/Wan2.2-T2V-A14B-GGUF](https://huggingface.co/bullerwins/Wan2.2-T2V-A14B-GGUF)
  * [QuantStack/Wan2.2 GGUFs](https://huggingface.co/collections/QuantStack/wan22-ggufs-6887ec891bdea453a35b95f3)

**Custom Node** [City96/ComfyUI-GGUF](https://github.com/city96/ComfyUI-GGUF)

### 

​

WanVideoWrapper

[Kijai/ComfyUI-WanVideoWrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper) **Wan2.2 models** [Kijai/WanVideo_comfy_fp8_scaled](https://hf-mirror.com/Kijai/WanVideo_comfy_fp8_scaled) **Wan2.1 models** [Kijai/WanVideo_comfy/Lightx2v](https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Lightx2v) **Lightx2v 4steps LoRA**

  * [Wan2.2-T2V-A14B-4steps-lora-rank64-V1](https://huggingface.co/lightx2v/Wan2.2-Lightning/tree/main/Wan2.2-T2V-A14B-4steps-lora-rank64-V1)



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/video/wan/wan2_2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/video/wan/wan2_2)

[Wan Animate 2: Motion TransferPrevious](https://docs.comfy.org/tutorials/video/wan/wan-animate-2)[Wan2.2 Animate ComfyUI native workflowNext](https://docs.comfy.org/tutorials/video/wan/wan2-2-animate)

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
