---
url: https://docs.comfy.org/tutorials/video/cosmos/cosmos-predict2-video2world/
title: Cosmos Predict2 Video2World in ComfyUI: Image to Video Generation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:43.503529+00:00
---

# Cosmos Predict2 Video2World in ComfyUI: Image to Video Generation - ComfyUI

> Source: https://docs.comfy.org/tutorials/video/cosmos/cosmos-predict2-video2world/

## On this page

  * Cosmos Predict2 Video2World Workflow
    * 1\. Workflow File
    * 2\. Manual Model Installation
    * 3\. Complete Workflow Step by Step



Cosmos

# Cosmos Predict2 Video2World in ComfyUI: Image to Video Generation

Copy pageCopy page

Generate physics-aware video from a still image in ComfyUI with the NVIDIA Cosmos-Predict2 Video2World workflow, including manual install steps.

Copy pageCopy page

Cosmos-Predict2 is NVIDIA’s next-generation physical world foundation model, specifically designed for high-quality visual generation and prediction tasks in physical AI scenarios. The model features exceptional physical accuracy, environmental interactivity, and detail reproduction capabilities, enabling realistic simulation of complex physical phenomena and dynamic scenes. Cosmos-Predict2 supports various generation methods including Text-to-Image (Text2Image) and Video-to-World (Video2World), and is widely used in industrial simulation, autonomous driving, urban planning, scientific research, and other fields. It serves as a crucial foundational tool for promoting deep integration of intelligent vision and the physical world.

## GitHub

Cosmos-Predict2 source code and documentation

## Hugging Face

Cosmos-Predict2 model collection

This guide will walk you through completing **Video2World** generation in ComfyUI. For the text-to-image section, please refer to the following part:

## Cosmos Predict2 Text to Image

Using Cosmos-Predict2 for text-to-image generation

## Run on Comfy Cloud

Run Cosmos-Predict2 workflows on Comfy Cloud with powerful GPUs

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

Cosmos Predict2 Video2World Workflow

When testing the 2B version, it takes around 16GB VRAM.

### 

​

1\. Workflow File

Please download the video below and drag it into ComfyUI to load the workflow. The workflow already has embedded model download links.

## Run on Comfy Cloud

Run this workflow on Comfy Cloud with pre-installed models

## Download Workflow File

Download the JSON format workflow file

Please download the following image as input: ![Input Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/cosmos/predict2/input.png)

### 

​

2\. Manual Model Installation

If the model download was not successful, you can try to download them manually by yourself in this section. **Diffusion model**

## Diffusion Model

cosmos_predict2_2B_video2world_480p_16fps.safetensors

For other weights, please visit [Cosmos_Predict2_repackaged](https://huggingface.co/Comfy-Org/Cosmos_Predict2_repackaged) to download. **Text encoder**

## Text Encoder

oldt5_xxl_fp8_e4m3fn_scaled.safetensors

**VAE**

## VAE

wan_2.1_vae.safetensors

File Storage Location
    
    
    📂 ComfyUI/
    ├──📂 models/
    │   ├── 📂 diffusion_models/
    │   │   └─── cosmos_predict2_2B_video2world_480p_16fps.safetensors
    │   ├── 📂 text_encoders/
    │   │   └─── oldt5_xxl_fp8_e4m3fn_scaled.safetensors
    │   └── 📂 vae/
    │       └──  wan_2.1_vae.safetensors
    

### 

​

3\. Complete Workflow Step by Step

![Workflow Step Guide](https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/cosmos/cosmos_predict2_2B_video2world_480p_16fps_step_guide.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=ea0b6deafa617381a38a57ccb3c92014) Please follow the steps in the image to run the workflow:

  1. Ensure the `Load Diffusion Model` node has loaded `cosmos_predict2_2B_video2world_480p_16fps.safetensors`
  2. Ensure the `Load CLIP` node has loaded `oldt5_xxl_fp8_e4m3fn_scaled.safetensors`
  3. Ensure the `Load VAE` node has loaded `wan_2.1_vae.safetensors`
  4. Upload the provided input image in the `Load Image` node
  5. (Optional) If you need first and last frame control, use the shortcut `Ctrl(cmd) + B` to enable last frame input
  6. (Optional) You can modify the prompts in the `ClipTextEncode` node
  7. (Optional) Modify the size and frame count in the `CosmosPredict2ImageToVideoLatent` node
  8. Click the `Run` button or use the shortcut `Ctrl(cmd) + Enter` to run the workflow
  9. Once generation is complete, the video will automatically save to the `ComfyUI/output/` directory, you can also preview it in the `save video` node



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/video/cosmos/cosmos-predict2-video2world.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/video/cosmos/cosmos-predict2-video2world)

[HunyuanVideo 1.5Previous](https://docs.comfy.org/tutorials/video/hunyuan/hunyuan-video-1-5)[Kandinsky 5.0 in ComfyUI: Text-to-Video and Image-to-VideoNext](https://docs.comfy.org/tutorials/video/kandinsky/kandinsky-5)

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
