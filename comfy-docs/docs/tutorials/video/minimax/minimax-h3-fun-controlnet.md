---
url: https://docs.comfy.org/tutorials/video/minimax/minimax-h3-fun-controlnet/
title: ComfyUI MiniMax H3 Fun ControlNet Union: Pose, Depth, and Canny Control Video - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:44.090967+00:00
---

# ComfyUI MiniMax H3 Fun ControlNet Union: Pose, Depth, and Canny Control Video - ComfyUI

> Source: https://docs.comfy.org/tutorials/video/minimax/minimax-h3-fun-controlnet/

## On this page

  * Model downloads
  * Model storage
  * Prompting tips



MiniMax H3

# ComfyUI MiniMax H3 Fun ControlNet Union: Pose, Depth, and Canny Control Video

Copy pageCopy page

Guide MiniMax H3 video motion in ComfyUI with Canny, Depth, HED, MLSD, or Pose control videos, plus mask-based inpainting with the Fun ControlNet Union patch.

Copy pageCopy page

Control the motion of a MiniMax H3 video with a control video instead of text alone. The Fun ControlNet Union patch ([alibaba-pai/MiniMax-H3-Fun-Controlnet-Union](https://huggingface.co/alibaba-pai/MiniMax-H3-Fun-Controlnet-Union), packaged in [Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3)) is a single checkpoint that conditions H3 on Canny, Depth, HED, MLSD, or Pose control videos, and also runs video inpainting with a mask. It works with both the `fl2va` and `ref2va` transformer files. ![MiniMax H3 Fun ControlNet Union workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_minimax_h3_fun_controlnet_union-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “MiniMax H3 Fun ControlNet Union” in Template Library

**Input materials** Upload this file to the matching `Load Video` node:

## dancer_field_pose.mp4

Pose control video used by the example workflow, or use your own.

This template requires ComfyUI 0.35.0 or later. The example uses a pose control video: a built-in SDPose subgraph extracts the pose skeleton from the input video, so the output reproduces the dancer’s motion. You can also connect any preprocessed control video directly to the `Apply MiniMax H3 Fun ControlNet` node’s `control_video` input.

## 

​

Model downloads

## Diffusion Model: minimax_h3_ref2va_pruned_int8_convrot

Place in `ComfyUI/models/diffusion_models/`

## ControlNet Patch: minimax_h3_fun_controlnet_union_pruned_int8_convrot

Place in `ComfyUI/models/model_patches/`

## Text Encoder: qwen3vl_32b_minimax_h3_nvfp4_awq

Place in `ComfyUI/models/text_encoders/`

## VAE: minimax_h3_video_vae_int8_convrot

Place in `ComfyUI/models/vae/`

## VAE: minimax_h3_audio_vae_fp32

Place in `ComfyUI/models/vae/`

## LoRA: minimax_h3_ref2v_turbo_4step_v0.1_comfyui_bf16

Powers the optional Lightning LoRA turbo mode. Place in `ComfyUI/models/loras/`

## Checkpoint: sdpose_wholebody_fp16

Pose extractor used by the built-in SDPose subgraph. Place in `ComfyUI/models/checkpoints/`

## Detector: rt_detr_v4-x-hgnet_fp16

Person detector used by the built-in SDPose subgraph. Place in `ComfyUI/models/diffusion_models/`

## 

​

Model storage
    
    
    ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   ├── minimax_h3_ref2va_pruned_int8_convrot.safetensors
    │   │   └── rt_detr_v4-x-hgnet_fp16.safetensors
    │   ├── 📂 text_encoders/
    │   │   └── qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors
    │   ├── 📂 vae/
    │   │   ├── minimax_h3_video_vae_int8_convrot.safetensors
    │   │   └── minimax_h3_audio_vae_fp32.safetensors
    │   ├── 📂 loras/
    │   │   └── minimax_h3_ref2v_turbo_4step_v0.1_comfyui_bf16.safetensors
    │   ├── 📂 model_patches/
    │   │   └── minimax_h3_fun_controlnet_union_pruned_int8_convrot.safetensors
    │   └── 📂 checkpoints/
    │       └── sdpose_wholebody_fp16.safetensors
    

## 

​

Prompting tips

  1. **Video length** : The target video runs 5 to 15 seconds on the 17n+5 frame grid at 24fps (124 frames = 5 seconds). A control video longer than the target is trimmed to its first frames; a shorter one holds its last frame. To match the control video’s length exactly, link the example’s computed `batch_size` output to the length input of the `MiniMax H3 Reference to Video` node
  2. **Guidance and strength** : Keep `guidance_scale` at 1.0. Raise the patch `strength` above 1 only if the output drifts away from the control
  3. **Video inpainting** : Connect a mask to the `mask` input: regions marked `1` are regenerated under control of the optional `source_video` input, while the rest of the frame stays fixed
  4. **Turbo mode (optional)** : Enable the **Lightning LoRA** checkbox to use the 4-step turbo LoRA for much faster generation, with slightly lower audio and motion quality
  5. **Preparing control videos** : ComfyUI ships with built-in preprocessing nodes for each control type. See the [Detect Edges (Canny) node](https://docs.comfy.org/built-in-nodes/Canny) for edges and the [Depth Anything 3 tutorial](https://docs.comfy.org/tutorials/utility/depth-anything-3) for depth maps



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/video/minimax/minimax-h3-fun-controlnet.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/video/minimax/minimax-h3-fun-controlnet)

[ComfyUI MiniMax H3 Multiframe Reference WorkflowPrevious](https://docs.comfy.org/tutorials/video/minimax/minimax-h3-multiframe)[ComfyUI MiniMax H3 Prompt Guide: Official Guides, Tips, and Prompt EmbeddingsNext](https://docs.comfy.org/tutorials/video/minimax/minimax-h3-prompt-guide)

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
