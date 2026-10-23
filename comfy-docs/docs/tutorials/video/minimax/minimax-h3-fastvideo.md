---
url: https://docs.comfy.org/tutorials/video/minimax/minimax-h3-fastvideo/
title: FastVideo FastH3: ComfyUI Workflow Examples - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:44.234278+00:00
---

# FastVideo FastH3: ComfyUI Workflow Examples - ComfyUI

> Source: https://docs.comfy.org/tutorials/video/minimax/minimax-h3-fastvideo/

## On this page

  * Requirements
  * FastH3 Text to Video
    * Prompting tips
  * FastH3 Image to Video
    * First/last-frame mode
    * Prompting tips
  * Model downloads
    * Model storage
  * Workflow structure notes



MiniMax H3

# FastVideo FastH3: ComfyUI Workflow Examples

Copy pageCopy page

FastVideo FastH3 generates MiniMax H3 video with synchronized audio in 8 sampling steps in ComfyUI, for text-to-video and first/last-frame workflows.

Copy pageCopy page

[FastVideo FastH3](https://huggingface.co/FastVideo/FastVideo-FastH3-8-Step-V2) is a DMD2-distilled MiniMax H3 checkpoint from the FastVideo team that generates video with synchronized native audio in **8 sampling steps** instead of the base model’s full schedule. It reuses the H3 text encoder, video VAE, and audio VAE, so output matches the base model’s setup while sampling finishes in a fraction of the steps. The FastH3 preview work was developed in collaboration with Nuva Lab and the NVIDIA FastGen team; read the [FastH3 announcement](https://haoailab.com/blogs/fasth3-preview/) for distillation details. ComfyUI ships with the 8-step V2 checkpoint, repacked by Comfy-Org in the [FastVideo-FastH3-Comfy](https://huggingface.co/FastVideo/FastVideo-FastH3-Comfy) repository. FastH3 trades some motion and audio fidelity for speed. Use it for drafts, iteration, and fast turnaround; use the base MiniMax H3 workflows when maximum quality matters.

The distilled checkpoint supports text-to-video and first/last-frame image-to-video only. Ref2VA (multi-reference conditioning) was not distilled; use the base [MiniMax H3 workflows](https://docs.comfy.org/tutorials/video/minimax/minimax-h3-native) for reference-based generation.

## 

​

Requirements

  * ComfyUI 0.36.0 or later
  * The MiniMax H3 text encoder and VAEs (shared with the base model, listed below)



## 

​

FastH3 Text to Video

Generate synchronized video and audio from a text prompt in 8 steps.

## Download Workflow

Download JSON or search “FastVideo FastH3: Text to Video” in Template Library

### 

​

Prompting tips

  1. **Describe the whole scene** : State the overall scene first (location, character, what is happening), then break it into timed shots
  2. **Shots, camera, and audio** : Describe the shots, camera moves, and the accompanying audio (dialogue, SFX, music) in one prompt block
  3. **Resolution** : H3’s native canvas is a 768px short edge, capped at 768x1344, and resolutions are rounded to a multiple of 32
  4. **Duration** : The duration input snaps to the model’s 17-frame-per-block (17k+5) grid at 24fps
  5. **Steps are fixed at 8** : The distilled checkpoint is trained for exactly 8 steps; changing the step count in the scheduler degrades quality

For prompt writing resources, see the [prompt guide](https://docs.comfy.org/tutorials/video/minimax/minimax-h3-prompt-guide).

## 

​

FastH3 Image to Video

Animate a still image with synchronized audio, with optional first/last-frame control.

## Download Workflow

Download JSON or search “FastVideo FastH3: Image to Video” in Template Library

**Input material** Upload this file to the matching `LoadImage` node, or use your own image:

## red_line_barrier.png

Example first frame for the Image to Video workflow

### 

​

First/last-frame mode

Connect images to `first_frame` and/or `last_frame` on the `MiniMaxH3ImageToVideo` node to generate the motion between two keyframes. Leave both disconnected for text-to-video.

### 

​

Prompting tips

  1. **Describe the motion and audio** : With an image providing the look, the prompt should focus on motion, camera, and the accompanying audio
  2. **Duration** : The duration input snaps to the model’s 17-frame-per-block (17k+5) grid at 24fps
  3. **Steps are fixed at 8** : Keep the scheduler at 8 steps; the checkpoint is distilled for that schedule



## 

​

Model downloads

The diffusion model comes from the FastVideo repository; the text encoder and VAEs are shared with the base MiniMax H3 model.

## Diffusion Model: fastvideo_fasth3_8step_v2_pruned_int8_convrot

Place in `ComfyUI/models/diffusion_models/`

## Text Encoder: qwen3vl_32b_minimax_h3_nvfp4_awq

Place in `ComfyUI/models/text_encoders/`

## VAE: minimax_h3_video_vae_int8_convrot

Place in `ComfyUI/models/vae/`

## VAE: minimax_h3_audio_vae_fp32

Place in `ComfyUI/models/vae/`

### 

​

Model storage
    
    
    ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   └── fastvideo_fasth3_8step_v2_pruned_int8_convrot.safetensors
    │   ├── 📂 text_encoders/
    │   │   └── qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors
    │   └── 📂 vae/
    │       ├── minimax_h3_video_vae_int8_convrot.safetensors
    │       └── minimax_h3_audio_vae_fp32.safetensors
    

## 

​

Workflow structure notes

Both FastH3 workflows share these nodes with the base H3 setup, with distillation-specific settings:

  * **BlockSparseAttention** : Runs Video Sparse Attention (VSA) with `keep_percent` 10 starting at 20% of the schedule, reducing attention cost while preserving quality
  * **MiniMaxH3SigmaShift** : Applies the H3 sigma shift (10 for video, 3 for audio) that matches the distilled schedule
  * **ComfyMathExpression** : Converts the duration input into a valid frame `length` on the 17k+5 grid at 24fps
  * **Sampler** : `res_multistep` sampler with the `simple` scheduler at 8 steps



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/video/minimax/minimax-h3-fastvideo.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/video/minimax/minimax-h3-fastvideo)

[ComfyUI MiniMax H3 Prompt Guide: Official Guides, Tips, and Prompt EmbeddingsPrevious](https://docs.comfy.org/tutorials/video/minimax/minimax-h3-prompt-guide)[LTX-Video 0.9.5 in ComfyUI: T2V, I2V, Multi-Frame ControlNext](https://docs.comfy.org/tutorials/video/ltxv)

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
