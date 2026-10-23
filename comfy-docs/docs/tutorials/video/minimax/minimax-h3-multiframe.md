---
url: https://docs.comfy.org/tutorials/video/minimax/minimax-h3-multiframe/
title: ComfyUI MiniMax H3 Multiframe Reference Workflow - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:44.341928+00:00
---

# ComfyUI MiniMax H3 Multiframe Reference Workflow - ComfyUI

> Source: https://docs.comfy.org/tutorials/video/minimax/minimax-h3-multiframe/

## On this page

  * Model downloads
  * Model storage
  * Prompting tips
  * Prompt writing guide



MiniMax H3

# ComfyUI MiniMax H3 Multiframe Reference Workflow

Copy pageCopy page

Build MiniMax H3 video continuations and multi-shot scenes in ComfyUI by pinning reference frames to set points on the timeline with Add Guide nodes.

Copy pageCopy page

Generate video continuations and multi-shot scenes by anchoring reference frames at specific points along the output timeline. The workflow combines the Reference to Video node with chained Add Guide nodes: each Add Guide pins a still image (plus optional audio) to a frame index, so the video passes through that exact composition at that moment. ![MiniMax H3 Multiframe Reference workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_minimax_h3_multiframe_reference-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “MiniMax H3: Multiframe Reference” in Template Library

## Frame Reference 1: h3_frame_ref_1.png

Identity reference and first frame of Shot 1, or use your own images.

## Frame Reference 2: h3_frame_ref_2.png

Keyframe anchored at 1.5s (Shot 2), or use your own images.

## Frame Reference 3: h3_frame_ref_3.png

Keyframe anchored at 3.0s (Shot 3), or use your own images.

## Frame Reference 4: h3_frame_ref_4.png

First frame anchored at 5.0s (Shot 4), or use your own images.

## 

​

Model downloads

## Diffusion Model: minimax_h3_ref2va_pruned_int8_convrot

Place in `ComfyUI/models/diffusion_models/`

## Text Encoder: qwen3vl_32b_minimax_h3_nvfp4_awq

Place in `ComfyUI/models/text_encoders/`

## VAE: minimax_h3_video_vae_int8_convrot

Place in `ComfyUI/models/vae/`

## VAE: minimax_h3_audio_vae_fp32

Place in `ComfyUI/models/vae/`

## LoRA: minimax_h3_ref2v_turbo_4step_v0.1_comfyui_bf16

Powers the optional Lightning LoRA turbo mode. Place in `ComfyUI/models/loras/`

## 

​

Model storage
    
    
    ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   └── minimax_h3_ref2va_pruned_int8_convrot.safetensors
    │   ├── 📂 text_encoders/
    │   │   └── qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors
    │   ├── 📂 vae/
    │   │   ├── minimax_h3_video_vae_int8_convrot.safetensors
    │   │   └── minimax_h3_audio_vae_fp32.safetensors
    │   └── 📂 loras/
    │       └── minimax_h3_ref2v_turbo_4step_v0.1_comfyui_bf16.safetensors
    

## 

​

Prompting tips

  1. **Reference by tag** : `<Picture 1>` is the image connected to the first `ref_images` slot, `<Picture 2>` the second, and so on. In this workflow, `<Picture 1>` is both the identity lock and the first frame of the video
  2. **Timeline anchors vs references** : Pictures connected only to Add Guide nodes pin compositions at specific frames but are not visible to the text encoder. Plug them into extra `ref_images` slots too if the prompt should see them as `<Picture N>`
  3. **Frame index** : Each Add Guide takes `frame_idx` in frames at 24fps; the template computes it from seconds with `round(seconds * 24)`. Negative values count from the end of the video. The index plus the guide length must stay inside the generated duration
  4. **Add more keyframes** : Copy one guide block (Load Image + Frame Index + Math Expression + Add Guide for MiniMax H3) and keep the `positive` outputs chained in series into the Basic Guider
  5. **Turbo mode (optional)** : Enable the **Lightning LoRA** checkbox to use the 4-step turbo LoRA for much faster generation, with slightly lower audio and motion quality



## 

​

Prompt writing guide

The template prompt follows the [full-reference mode prompt guide](https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/docs/VIDEO_PROMPT_WRITING_GUIDE_ref_en.md): it defines each subject, maps each `<Picture N>` to a shot’s first frame or keyframe, and cuts between shots at explicit timestamps. Use the same structure when writing your own multi-shot prompts. The guide is summarized in the [prompt guide](https://docs.comfy.org/tutorials/video/minimax/minimax-h3-prompt-guide).

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/video/minimax/minimax-h3-multiframe.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/video/minimax/minimax-h3-multiframe)

[ComfyUI MiniMax H3 Text-to-Video, Image-to-Video, and Reference-to-Video WorkflowsPrevious](https://docs.comfy.org/tutorials/video/minimax/minimax-h3-native)[ComfyUI MiniMax H3 Fun ControlNet Union: Pose, Depth, and Canny Control VideoNext](https://docs.comfy.org/tutorials/video/minimax/minimax-h3-fun-controlnet)

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
