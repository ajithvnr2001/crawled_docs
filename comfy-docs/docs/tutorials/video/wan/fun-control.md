---
url: https://docs.comfy.org/tutorials/video/wan/fun-control/
title: ComfyUI Wan2.1 Fun Control Video Examples - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:45.346689+00:00
---

# ComfyUI Wan2.1 Fun Control Video Examples - ComfyUI

> Source: https://docs.comfy.org/tutorials/video/wan/fun-control/

## On this page

  * About Wan2.1-Fun-Control
  * Model Installation
  * ComfyUI Native Workflow
    * 1\. Workflow File Download
    * 2\. Complete the Workflow Step by Step
    * 3\. Usage Notes
  * Workflow Using Custom Nodes
    * 1\. Workflow File Download
    * 2\. Complete the Workflow Step by Step
    * 3\. Workflow Notes
  * Usage Tips



Wan2.1

# ComfyUI Wan2.1 Fun Control Video Examples

Copy pageCopy page

This guide demonstrates how to use Wan2.1 Fun Control in ComfyUI to generate videos with control videos

Copy pageCopy page

Wan2.1-Fun-Control is an open-source video generation model from Alibaba’s VideoX-Fun project that follows preset control conditions instead of relying on prompt text alone. You can guide the output with Canny edge maps, depth maps, OpenPose skeletons, MLSD geometric edges, or point trajectories. The model ships in two sizes: the 1.3B version (about 19 GB) for lightweight local deployment with lower VRAM requirements, and the 14B version (about 47 GB of total model storage, with the diffusion weights at about 32.8 GB) for higher-quality results. Both support multi-resolution video prediction at 512, 768, and 1024 pixels, generate up to 81 frames (about 5 seconds) at 16 frames per second, and accept multilingual prompts. ComfyUI supports Wan2.1-Fun-Control natively.

## 

​

About Wan2.1-Fun-Control

**Wan2.1-Fun-Control** is an open-source video generation and control project developed by Alibaba team. It introduces innovative Control Codes mechanisms combined with deep learning and multimodal conditional inputs to generate high-quality videos that conform to preset control conditions. The project focuses on precisely guiding generated video content through multimodal control conditions. Currently, the Fun Control model supports various control conditions, including **Canny (line art), Depth, OpenPose (human posture), MLSD (geometric edges), and trajectory control.** The model also supports multi-resolution video prediction with options for 512, 768, and 1024 resolutions at 16 frames per second, generating videos up to 81 frames (approximately 5 seconds) in length. Model versions:

  * **1.3B** Lightweight: Suitable for local deployment and quick inference with **lower VRAM requirements**
  * **14B** High-performance: Model size reaches 32GB+, offering better results but **requiring higher VRAM**

**Model Weights Download** :

## Wan2.1-Fun-1.3B-Control

Lightweight version, lower VRAM requirements

## Wan2.1-Fun-14B-Control

High-performance version, 32GB+ file size, higher VRAM requirements

**Code Repository** : [VideoX-Fun](https://github.com/aigc-apps/VideoX-Fun) ComfyUI now **natively supports** the Wan2.1 Fun Control model. Before starting this tutorial, please update your ComfyUI to ensure you’re using a version after [this commit](https://github.com/Comfy-Org/ComfyUI/commit/3661c833bcc41b788a7c9f0e7bc48524f8ee5f82). In this guide, we will provide two workflows:

  1. A workflow using only native Comfy Core nodes
  2. A workflow using custom nodes



Due to current limitations in native nodes for video support, the native-only workflow ensures users can complete the process without installing custom nodes. However, we have found that providing a good user experience for video generation is challenging without custom nodes, so we are providing both workflow versions in this guide.

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

Model Installation

You only need to install these models once. The workflow images also contain model download information, so you can choose your preferred download method. The following models can be found at [Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged) and [Wan2.1-Fun](https://huggingface.co/collections/alibaba-pai/wan21-fun-67e4fb3b76ca01241eb7e334) Click the corresponding links to download. If you have used Wan-related workflows before, you only need to download the **Diffusion models**. **Diffusion models** — choose 1.3B or 14B. The 14B version has a larger file size (32GB) and higher VRAM requirements:

## wan2.1_fun_control_1.3B_bf16.safetensors

Wan2.1 Fun Control 1.3B diffusion model — lightweight, lower VRAM requirements

## Wan2.1-Fun-14B-Control

Wan2.1 Fun Control 14B diffusion model. Rename to `Wan2.1-Fun-14B-Control.safetensors` after downloading. 32GB+ file size, higher VRAM requirements

**Text encoders** — choose one of the following models (fp16 precision has a larger size and higher performance requirements):

## umt5_xxl_fp16.safetensors

UMT5 XXL text encoder — fp16 precision, larger size, higher performance

## umt5_xxl_fp8_e4m3fn_scaled.safetensors

UMT5 XXL text encoder — fp8 precision, smaller size, lower performance requirements

**VAE**

## wan_2.1_vae.safetensors

Wan2.1 VAE model

**CLIP Vision**

## clip_vision_h.safetensors

CLIP Vision model for processing reference images

File storage location:
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   ├── wan2.1_fun_control_1.3B_bf16.safetensors
    │   │   └── Wan2.1-Fun-14B-Control.safetensors
    │   ├── 📂 text_encoders/
    │   │   └── umt5_xxl_fp8_e4m3fn_scaled.safetensors
    │   ├── 📂 vae/
    │   │   └── wan_2.1_vae.safetensors
    │   └── 📂 clip_vision/
    │       └── clip_vision_h.safetensors
    

## 

​

ComfyUI Native Workflow

In this workflow, we use videos converted to **WebP format** since the `Load Image` node does not currently support mp4 format. We also use **Canny Edge** to preprocess the original video. Because many users encounter installation failures and environment issues when installing custom nodes, this version of the workflow uses only native nodes to ensure a smoother experience. Thanks to our powerful ComfyUI authors who provide feature-rich nodes. If you want to directly check the related version, see Workflow Using Custom Nodes.

### 

​

1\. Workflow File Download

![Wan2.1 Fun Control Native Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/wan2.1_fun_control/wan2.1_fun_control_native.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download the workflow image and drag it into ComfyUI to load the workflow

**Input materials**

## Start Image: wan2.1_fun_control_start_frame.png

Input start frame for the native workflow. Download and use this image, or replace with your own.

## Control Video: 01-portrait_video.webp

Input control video in WebP format for the native workflow. The native workflow requires WebP format since Load Image does not support mp4.

### 

​

2\. Complete the Workflow Step by Step

![Wan2.1 Fun Control Workflow Steps](https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/fun_control_native_flow_diagram.png?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=97774a50d0e95007c34d94a6eb2d9580)

  1. Ensure the `Load Diffusion Model` node has loaded `wan2.1_fun_control_1.3B_bf16.safetensors`
  2. Ensure the `Load CLIP` node has loaded `umt5_xxl_fp8_e4m3fn_scaled.safetensors`
  3. Ensure the `Load VAE` node has loaded `wan_2.1_vae.safetensors`
  4. Ensure the `Load CLIP Vision` node has loaded `clip_vision_h.safetensors`
  5. Upload the starting frame to the `Load Image` node (renamed to `Start_image`)
  6. Upload the control video to the second `Load Image` node. Note: This node currently does not support mp4, only WebP videos
  7. (Optional) Modify the prompt (both English and Chinese are supported)
  8. (Optional) Adjust the video size in `WanFunControlToVideo`, avoiding overly large dimensions
  9. Click the `Run` button or use the shortcut `Ctrl(cmd) + Enter` to execute video generation



### 

​

3\. Usage Notes

  * Since we need to input the same number of frames as the control video into the `WanFunControlToVideo` node, if the specified frame count exceeds the actual control video frames, the excess frames may display scenes not conforming to control conditions. We will address this issue in the Workflow Using Custom Nodes
  * Avoid setting overly large dimensions, as this can make the sampling process very time-consuming. Try generating smaller images first, then upscale
  * Use your imagination to build upon this workflow by adding text-to-image or other types of workflows to achieve direct text-to-video generation or style transfer
  * Use tools like [ComfyUI-comfyui_controlnet_aux](https://github.com/Fannovel16/comfyui_controlnet_aux) for richer control options



## 

​

Workflow Using Custom Nodes

We will need to install the following two custom nodes:

  * [ComfyUI-VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite)
  * [ComfyUI-comfyui_controlnet_aux](https://github.com/Fannovel16/comfyui_controlnet_aux)

You can use [ComfyUI Manager](https://github.com/Comfy-Org/ComfyUI-Manager) to install missing nodes or follow the installation instructions for each custom node package.

### 

​

1\. Workflow File Download

![Wan2.1 Fun Control Workflow](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/wan2.1_fun_control-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Wan 2.1 ControlNet” in Template Library

**Input materials**

## Start Image: wan2.1_fun_control_start_frame.png

Input start frame for the custom nodes workflow. Download and use this image, or replace with your own.

## Control Video: wan2.1_fun_control_control_video.mp4

Input control video in MP4 format for the custom nodes workflow. The custom Load Video node supports mp4 format.

### 

​

2\. Complete the Workflow Step by Step

![Wan2.1 Fun Control Workflow Using Custom Nodes Steps](https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/fun_control_using_custom_nodes_flow_diagram.png?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=b22315f2f052e9196bd49b3d95a983f5)

> The model part is essentially the same. If you have already experienced the native-only workflow, you can directly upload the corresponding images and run it.

  1. Ensure the `Load Diffusion Model` node has loaded `wan2.1_fun_control_1.3B_bf16.safetensors`
  2. Ensure the `Load CLIP` node has loaded `umt5_xxl_fp8_e4m3fn_scaled.safetensors`
  3. Ensure the `Load VAE` node has loaded `wan_2.1_vae.safetensors`
  4. Ensure the `Load CLIP Vision` node has loaded `clip_vision_h.safetensors`
  5. Upload the starting frame to the `Load Image` node
  6. Upload an mp4 format video to the `Load Video(Upload)` custom node. Note that the workflow has adjusted the default `frame_load_cap`
  7. For the current image, the `DWPose Estimator` only uses the `detect_face` option
  8. (Optional) Modify the prompt (both English and Chinese are supported)
  9. (Optional) Adjust the video size in `WanFunControlToVideo`, avoiding overly large dimensions
  10. Click the `Run` button or use the shortcut `Ctrl(cmd) + Enter` to execute video generation



### 

​

3\. Workflow Notes

Thanks to the ComfyUI community authors for their custom node packages:

  * This example uses `Load Video(Upload)` to support mp4 videos
  * The `video_info` obtained from `Load Video(Upload)` allows us to maintain the same `fps` for the output video
  * You can replace `DWPose Estimator` with other preprocessors from the `ComfyUI-comfyui_controlnet_aux` node package
  * Prompts support multiple languages



## 

​

Usage Tips

![Apply Multi Control Videos](https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/apply_multi_control_videos.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=7bb51781350a318a61068b1b369b816f)

  * A useful tip is that you can combine multiple image preprocessing techniques and then use the `Image Blend` node to achieve the goal of applying multiple control methods simultaneously.
  * You can use the `Video Combine` node from `ComfyUI-VideoHelperSuite` to save videos in mp4 format
  * We use `SaveAnimatedWEBP` because we currently do not support embedding workflow into **mp4** and some other custom nodes may not support embedding workflow too. To preserve the workflow in the video, we choose the `SaveAnimatedWEBP` node.
  * In the `WanFunControlToVideo` node, `control_video` is not mandatory, so sometimes you can skip using a control video, first generate a very small video size like 320x320, and then use them as control video input to achieve consistent results.
  * [ComfyUI-WanVideoWrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper)
  * [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes)



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/video/wan/fun-control.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/video/wan/fun-control)

[Wan ATI Native WorkflowPrevious](https://docs.comfy.org/tutorials/video/wan/wan-ati)[ComfyUI Wan2.1 Fun Camera Official ExamplesNext](https://docs.comfy.org/tutorials/video/wan/fun-camera)

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
