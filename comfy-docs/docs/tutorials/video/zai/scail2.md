---
url: https://docs.comfy.org/tutorials/video/zai/scail2/
title: ComfyUI SCAIL-2 Character Replacement Workflow Tutorial - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:48.351082+00:00
---

# ComfyUI SCAIL-2 Character Replacement Workflow Tutorial - ComfyUI

> Source: https://docs.comfy.org/tutorials/video/zai/scail2/

## On this page

  * SCAIL-2 Character Replacement Workflow
    * SCAIL-2 Character Replacement
  * How the Workflow Works
    * Long Videos
  * Two Modes
  * Inputs and Parameters
    * Shared Parameters (Base & Extend)
    * SAM3 Tracking (two inputs)
  * Model Installation
    * Required Models
    * File Storage Locations



ZAI

# ComfyUI SCAIL-2 Character Replacement Workflow Tutorial

Copy pageCopy page

Drive a reference character image with a driving video for character animation or in-video character replacement using SCAIL-2.

Copy pageCopy page

**SCAIL-2** is an end-to-end character animation model built on Wan2.1. It drives a reference character image with a driving video, enabling both character animation (making a character perform the motion) and in-video character replacement (swapping a tracked person in a video with the reference character). **Key Features** :

  * **End-to-End Character Animation** : Drive a still character image with motion from a driving video
  * **Two Modes** : Animation Mode (character performs the motion) and Replacement Mode (swap tracked person with reference character)
  * **Long Video Support** : Chunk-based extended generation with frame overlap between segments
  * **Built-in ComfyUI Nodes** : Uses native `WanSCAILToVideo`, `SCAIL2ColoredMask`, and `SAM3` tracking. No custom nodes required beyond standard model downloads.

**Related Links** :

  * [Hugging Face: SCAIL-2](https://huggingface.co/zai-org/SCAIL-2)
  * [SCAIL-2 Diffusion Model](https://huggingface.co/Comfy-Org/SCAIL-2)



## 

​

SCAIL-2 Character Replacement Workflow

### 

​

SCAIL-2 Character Replacement

Replace a character in a video while preserving motion and scene context. ![SCAIL-2 Character Replacement workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan21_scail2_character_replacement-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “SCAIL-2 Character Replacement” in Template Library

**Input materials**

## Reference Image

Download the default reference character image, or use your own.

## Driving Video

Download the default driving video, or use your own.

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

How the Workflow Works

This workflow uses two subgraph nodes: a **Base** subgraph (first segment) and an **Extend** subgraph (subsequent segments). This supports character animation for both short and long videos.

  1. **Load** a driving video (`pose_video`) and a reference character image
  2. **Base subgraph** processes the first segment (81 frames by default)
  3. **Extend subgraph** processes additional segments 2+, chaining `previous_frames` from the prior segment
  4. Preview the result and save



## Learn about Subgraph

This workflow uses Subgraph nodes for modular processing. Check out the Subgraph documentation to learn how to customize and extend the workflow.

### 

​

Long Videos

For longer videos, calculate the number of segments: `ceil(total_frames / 76)`. Each segment except the first uses the Extend subgraph. Duplicate the Extend node for more segments, chain the `previous_frames` output, and increment `segment_index`.

> **Note:** `WanSCAILToVideo` cannot queue all segments automatically. Run each segment manually.

## 

​

Two Modes

Mode| `replace_mode`| Driving Mask BG| Summary  
---|---|---|---  
**Replacement**| `true` (default)| White| Swap the tracked person in the driving video with the reference character  
**Animation**| `false`| Black| Reference character performs the driving motion  
  
Set the `replace_mode` parameter on both subgraph nodes.

## 

​

Inputs and Parameters

### 

​

Shared Parameters (Base & Extend)

Parameter| Description  
---|---  
`pose_video`| The driving video containing motion to transfer  
`reference_image`| The character image to animate or insert  
`prompt`| Output video description  
`replace_mode`| `true` = Replacement, `false` = Animation  
`segment_index`| `1` for first chunk, `2+` for continuation. Pose offset = `76 × (index − 1)`  
`width` / `height`| Output resolution, e.g. `896×512`. Must be divisible by 16  
`frame_count`| Frames per segment (default: 81)  
`previous_frame_count`| Overlap frames between segments (default: 5)  
`pose_strength` / `pose_start` / `pose_end`| Pose conditioning strength and timing  
  
### 

​

SAM3 Tracking (two inputs)

The `sam3_video_object` and `sam3_image_object` inputs control the SAM3 mask tracking, **not** the SCAIL-2 output prompt. These determine which objects are tracked for the colored masks:

Input| Target| Output  
---|---|---  
`sam3_video_object`| Driving video| `pose_video_mask`  
`sam3_image_object`| Reference image| `reference_image_mask`  
  
  * Use open-vocabulary text (default: `human`)
  * Use the same term when the subject is the same across video and reference
  * Use different terms if the video and reference need different focus (e.g., crowded scenes)



## 

​

Model Installation

Update ComfyUI to the latest version first for the built-in WanSCAILToVideo and SCAIL2ColoredMask nodes.

### 

​

Required Models

**diffusion_models**

  * [wan2.1_14B_SCAIL_2_fp16.safetensors](https://huggingface.co/Comfy-Org/SCAIL-2/blob/main/diffusion_models/wan2.1_14B_SCAIL_2_fp16.safetensors)

**text_encoders** (choose one)

  * [umt5_xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/blob/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors)

**clip_vision**

  * [clip_vision_h.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/blob/main/split_files/clip_vision/clip_vision_h.safetensors)

**vae**

  * [Wan2_1_VAE_bf16.safetensors](https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1_VAE_bf16.safetensors)

**loras**

  * [lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors](https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Lightx2v/lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors)
  * [wan2.1_SCAIL_2_DPO_lora_bf16.safetensors](https://huggingface.co/Comfy-Org/SCAIL-2/blob/main/loras/wan2.1_SCAIL_2_DPO_lora_bf16.safetensors)

**checkpoints**

  * [sam3.1_multiplex_fp16.safetensors](https://huggingface.co/Comfy-Org/sam3.1/blob/main/checkpoints/sam3.1_multiplex_fp16.safetensors)



### 

​

File Storage Locations
    
    
    ComfyUI/
    ├── models/
    │   ├── diffusion_models/
    │   │   └── wan2.1_14B_SCAIL_2_fp16.safetensors
    │   ├── text_encoders/
    │   │   └── umt5_xxl_fp8_e4m3fn_scaled.safetensors
    │   ├── clip_vision/
    │   │   └── clip_vision_h.safetensors
    │   ├── vae/
    │   │   └── Wan2_1_VAE_bf16.safetensors
    │   ├── loras/
    │   │   ├── lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors
    │   │   └── wan2.1_SCAIL_2_DPO_lora_bf16.safetensors
    │   └── checkpoints/
    │       └── sam3.1_multiplex_fp16.safetensors
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/video/zai/scail2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/video/zai/scail2)

[Kandinsky 5.0 in ComfyUI: Text-to-Video and Image-to-VideoPrevious](https://docs.comfy.org/tutorials/video/kandinsky/kandinsky-5)[ComfyUI YuE2 Music Generation GuideNext](https://docs.comfy.org/tutorials/audio/yue2/yue2)

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
