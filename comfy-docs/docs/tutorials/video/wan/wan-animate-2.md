---
url: https://docs.comfy.org/tutorials/video/wan/wan-animate-2/
title: Wan Animate 2: Motion Transfer - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:45.891642+00:00
---

# Wan Animate 2: Motion Transfer - ComfyUI

> Source: https://docs.comfy.org/tutorials/video/wan/wan-animate-2/

## On this page

  * Model Highlights
  * Wan Animate 2 workflow
    * Model downloads
    * Workflow instructions
    * Extending to longer videos



Wan Video

# Wan Animate 2: Motion Transfer

Copy pageCopy page

Animate a still character with Wan Animate 2 in ComfyUI: transfer motion from a driving video directly, with no pose extraction or skeleton preprocessing.

Copy pageCopy page

Wan Animate 2 is an end-to-end character animation framework from the Wan team that directly consumes driving videos in a redesigned Diffusion Transformer. It achieves high-fidelity motion generation and strong identity preservation by eliminating intermediate motion extractors: no pose extraction or skeleton preprocessing is needed. The model also adds text-driven viewpoint control, decoupling the output camera perspective from the driving video. This lets you animate a still character using a driving video while controlling the camera independently, and even generate a fresh background from your text prompt.

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

Model Highlights

  * **Direct motion transfer** : Animates a still character from a driving video without pose extraction or skeleton preprocessing
  * **Identity preservation** : Keeps the reference character’s identity, appearance, and details intact
  * **Text-driven camera control** : Decouples output camera perspective from the driving video
  * **Fresh backgrounds** : Generates a new background from your text prompt instead of copying the driving video’s background
  * **High-fidelity motion** : Replicates complex motions and expressions from the driving video



## 

​

Wan Animate 2 workflow

Animate a still character using a driving video, transferring motion directly from video frames. The output preserves the reference character’s identity while generating a fresh background and camera movement from your text prompt.

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Wan Animate 2” in Template Library

**Input materials** Upload these files to the matching nodes:

## Reference image

`LoadImage` node: pink_hair_mech_arms_ref.png (the character to animate)

## Driving video

`LoadVideo` node: street_dance_drive.mp4 (the motion source)

### 

​

Model downloads

This workflow uses the `wan_animate_2_int8_convrot.safetensors` diffusion model. The repository also ships BF16 and distilled variants; if you want to use those instead, change the model selection in the `UNETLoader` node. All files are available in the [Comfy-Org/Wan-Animate-2](https://huggingface.co/Comfy-Org/Wan-Animate-2) repository:

## Diffusion Model (INT8, required)

wan_animate_2_int8_convrot.safetensors: INT8 convrot quantized diffusion model used by this workflow

## Diffusion Model (BF16, optional)

wan_animate_2_bf16.safetensors: Full-precision base model. Requires changing the UNETLoader model selection.

## Diffusion Model (Distill INT8, optional)

wan_animate_2_distill_int8_convrot.safetensors: Distilled INT8 variant. Requires changing the UNETLoader model selection.

## Diffusion Model (Distill BF16, optional)

wan_animate_2_distill_bf16.safetensors: Distilled BF16 variant. Requires changing the UNETLoader model selection.

## LoRA

lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors: LightX2V acceleration LoRA

## Text Encoder

umt5_xxl_fp8_e4m3fn_scaled.safetensors: UMT5-XXL FP8 text encoder

## CLIP Vision

clip_vision_h.safetensors: CLIP Vision encoder

## VAE

Wan2_1_VAE_bf16.safetensors: Wan2.1 VAE for encoding and decoding

Place the files in the following directories:
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   ├── wan_animate_2_bf16.safetensors
    │   │   ├── wan_animate_2_distill_bf16.safetensors
    │   │   ├── wan_animate_2_distill_int8_convrot.safetensors
    │   │   └── wan_animate_2_int8_convrot.safetensors
    │   ├── 📂 loras/
    │   │   └── lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors
    │   ├── 📂 text_encoders/
    │   │   └── umt5_xxl_fp8_e4m3fn_scaled.safetensors
    │   ├── 📂 clip_vision/
    │   │   └── clip_vision_h.safetensors
    │   └── 📂 vae/
    │       └── Wan2_1_VAE_bf16.safetensors
    

### 

​

Workflow instructions

  1. Make sure all the models are loaded correctly
  2. Upload the reference image: the character in this image is the target character to animate
  3. Upload the driving video: its motion is transferred to the reference character
  4. Update the prompt to describe the scene, background, and camera movement you want
  5. Click `Run` or use the shortcut `Ctrl(cmd) + Enter` to generate the video



### 

​

Extending to longer videos

Longer videos are handled inside the workflow: the `Motion Transfer (Wan Animate 2)` subgraph loops (`StartLoop` / `EndLoop`) and keeps generating until it has covered the whole driving video, so one subgraph is all you need. Nothing has to be duplicated or rewired. One loop iteration generates 81 frames, about 3.4 seconds at 24 fps. That is the `Int (fragment_length)` value inside the subgraph. You can raise it, but it has to stay a legal Wan length: 81, 85, 89, and so on, which is `4n + 1`. The loop math reads the driving video’s frame count, works out how many continuations are needed, and the tail is trimmed so the output has exactly as many frames as the driving video. Each continuation repeats the previous segment’s last frame and that duplicate is removed, so every extra segment adds `fragment_length - 1` new frames. Looping uses the core loop nodes, so the workflow needs ComfyUI 0.36.0 or newer. The `Video Stitch` subgraph is the comparison preview: it places the generated video next to the driving video. It is not part of the extension path.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/video/wan/wan-animate-2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/video/wan/wan-animate-2)

[LTX-2.5 DFR in ComfyUI: Image to Video with AudioPrevious](https://docs.comfy.org/tutorials/video/ltx/ltx-2-5-dfr)[Wan2.2 Video Generation ComfyUI Official Native Workflow ExampleNext](https://docs.comfy.org/tutorials/video/wan/wan2_2)

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
