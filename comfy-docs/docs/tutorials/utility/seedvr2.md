---
url: https://docs.comfy.org/tutorials/utility/seedvr2/
title: SeedVR2: Image and video upscaling in ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-15T14:35:55.796893+00:00
---

# SeedVR2: Image and video upscaling in ComfyUI - ComfyUI

> Source: https://docs.comfy.org/tutorials/utility/seedvr2/

## On this page

Back to top

  * ComfyUI SeedVR2 Introduction
  * Model Installation
  * Example Workflows
    * SeedVR2 3B Int8: Upscale Image
    * 1.1 Steps to Run
    * SeedVR2 7B Int8: Upscale Image
    * 2.1 Steps to Run
    * SeedVR2 3B Int8: Upscale Video
    * 3.1 Steps to Run
    * Performance
  * Troubleshooting
    * The upscaled image is fully black
  * Community Resources



Upscale & Restore

# SeedVR2: Image and video upscaling in ComfyUI

Copy pageCopy page

Upscale images and videos with SeedVR2, the one-step diffusion restoration model from ByteDance Seed, in 3B and 7B sizes with FP16, FP8, and INT8 checkpoints.

Copy pageCopy page

# ComfyUI SeedVR2 Introduction

[SeedVR2](https://iceclear.github.io/projects/seedvr2/) (arXiv:2506.05301, from ByteDance Seed) is a one-step diffusion-based video restoration model. It performs adversarial training against real data to restore and upscale images and videos with high fidelity. SeedVR2 is natively supported in ComfyUI (PR [#14424](https://github.com/Comfy-Org/ComfyUI/pull/14424)). Key capabilities:

  * **Conservative upscaling** : preserves original structure and detail while enhancing clarity
  * **One-step inference** : single forward pass for both image and video upscaling
  * **Multiple model sizes** : 3B and 7B variants with FP16, FP8, INT8, NVFP4, and MXFP8 quantizations
  * **Both image and video** : supports single-image upscaling and video resolution enhancement

SeedVR2 comes in two sizes. The [3B model](https://huggingface.co/ByteDance-Seed/SeedVR2-3B) is a smaller variant with lower VRAM requirements, suitable for users with limited hardware. The [7B model](https://huggingface.co/ByteDance-Seed/SeedVR2-7B) is a larger variant that delivers higher quality results at the cost of increased VRAM and processing time. Both are available under the Apache 2.0 license.

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

## Model Installation

Download the SeedVR2 checkpoint(s) from the [Comfy-Org SeedVR2 repository](https://huggingface.co/Comfy-Org/SeedVR2) and save them to the corresponding ComfyUI folder:

  * [seedvr2_3b_fp16.safetensors](https://huggingface.co/Comfy-Org/SeedVR2/blob/main/diffusion_models/seedvr2_3b_fp16.safetensors): 3B FP16 base model, lower VRAM requirement
  * [seedvr2_3b_fp8_e4m3fn.safetensors](https://huggingface.co/Comfy-Org/SeedVR2/blob/main/diffusion_models/seedvr2_3b_fp8_e4m3fn.safetensors): 3B FP8 quantized, further reduced VRAM
  * [seedvr2_3b_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/SeedVR2/blob/main/diffusion_models/seedvr2_3b_int8_convrot.safetensors): 3B INT8 with convrot
  * [seedvr2_7b_fp16.safetensors](https://huggingface.co/Comfy-Org/SeedVR2/blob/main/diffusion_models/seedvr2_7b_fp16.safetensors): 7B FP16 base model, higher quality
  * [seedvr2_7b_fp8_e4m3fn.safetensors](https://huggingface.co/Comfy-Org/SeedVR2/blob/main/diffusion_models/seedvr2_7b_fp8_e4m3fn.safetensors): 7B FP8 quantized, balance of quality and VRAM
  * [seedvr2_7b_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/SeedVR2/blob/main/diffusion_models/seedvr2_7b_int8_convrot.safetensors): 7B INT8 with convrot
  * [seedvr2_7b_sharp_fp16.safetensors](https://huggingface.co/Comfy-Org/SeedVR2/blob/main/diffusion_models/seedvr2_7b_sharp_fp16.safetensors): 7B FP16 sharp variant for enhanced detail
  * [seedvr2_ema_vae_fp16.safetensors](https://huggingface.co/Comfy-Org/SeedVR2/blob/main/vae/seedvr2_ema_vae_fp16.safetensors): VAE checkpoint (shared across all model variants)

Place the files in the following directories:
    
    
    ComfyUI/
    ├── models/
    │   ├── diffusion_models/
    │   │   ├── seedvr2_3b_fp16.safetensors
    │   │   ├── seedvr2_3b_fp8_e4m3fn.safetensors
    │   │   ├── seedvr2_3b_int8_convrot.safetensors
    │   │   ├── seedvr2_7b_fp16.safetensors
    │   │   ├── seedvr2_7b_fp8_e4m3fn.safetensors
    │   │   ├── seedvr2_7b_int8_convrot.safetensors
    │   │   ├── seedvr2_7b_sharp_fp16.safetensors
    │   └── vae/
    │       └── seedvr2_ema_vae_fp16.safetensors
    

## Example Workflows

### SeedVR2 3B Int8: Upscale Image

Upscale images using SeedVR2 3B Int8, a one-step diffusion-based video restoration model that produces high-quality results with improved temporal consistency. ![SeedVR2 3B Int8 upscale image workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_seedvr2_3b_int8_upscale_image-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “SeedVR2 3B Int8: Upscale Image” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## watch_macro_shot.png

`LoadImage` node 1 · `watch_macro_shot.png`

**Example output**

![Input image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/watch_macro_shot.png)![SeedVR2 3B Int8 upscale example output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/utility_seedvr2_3b_int8_upscale_image.png)

### 1.1 Steps to Run

  1. Place your image in the `ComfyUI/input/` folder and select it in the `Load Image` node
  2. Select the `seedvr2_3b_int8_convrot.safetensors` checkpoint in the SeedVR2 model loader
  3. Click `Queue` or use `Ctrl(cmd) + Enter` to run



### SeedVR2 7B Int8: Upscale Image

Upscale images using SeedVR2 7B Int8, a one-step diffusion model that enhances resolution through adversarial training and adaptive window attention. ![SeedVR2 7B Int8 upscale image workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_seedvr2_7b_int8_upscale_image-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “SeedVR2 7B Int8: Upscale Image” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## indoor_portrait.png

`LoadImage` node 1 · `indoor_portrait.png`

**Example output**

![Input image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/indoor_portrait.png)![SeedVR2 7B Int8 upscale example output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/utility_seedvr2_7b_int8_upscale_image.png)

### 2.1 Steps to Run

  1. Place your image in the `ComfyUI/input/` folder and select it in the `Load Image` node
  2. Select the `seedvr2_7b_int8_convrot.safetensors` checkpoint in the SeedVR2 model loader
  3. Click `Queue` or use `Ctrl(cmd) + Enter` to run



### SeedVR2 3B Int8: Upscale Video

Upscale and restore video footage using SeedVR2 3B Int8, a one-step diffusion model that enhances resolution while maintaining temporal consistency across frames. ![SeedVR2 3B Int8 upscale video workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_seedvr2_3b_int8_upscale_video-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “SeedVR2 3B Int8: Upscale Video” in Template Library

**Input materials** Upload this file to the matching `LoadVideo` node:

## grainy_perfume_shot_crf32.mp4

`LoadVideo` node 73 · `grainy_perfume_shot_crf32.mp4`

**Example output**

### 3.1 Steps to Run

  1. Place your video in the `ComfyUI/input/` folder and select it in the `Load Video` node
  2. Select the `seedvr2_3b_int8_convrot.safetensors` checkpoint in the SeedVR2 model loader
  3. Click `Queue` or use `Ctrl(cmd) + Enter` to run



### Performance

Higher target resolutions require more processing time. The INT8 variant provides efficient inference with reduced VRAM usage compared to FP16.

* * *

## Troubleshooting

### The upscaled image is fully black

Attention backends can silently return black or corrupted output on quantized checkpoints. If the SeedVR2 INT8 workflows produce an all-black image, try these in order:

  1. **Run without FlashAttention:** if you enabled it through `--use-flash-attention` or a custom node pack, start ComfyUI with the default attention backend and re-run. Disabling FlashAttention has resolved all-black output on the 3B and 7B INT8 workflows on an RTX 3090.
  2. **Switch the checkpoint:** use the FP16 or FP8 file of the same size. If those render correctly, the INT8 quantization path is where it breaks.
  3. **Verify the files:** the diffusion model and `seedvr2_ema_vae_fp16.safetensors` must both be fully downloaded and placed as shown in Model Installation. A truncated download fails the same way.
  4. **Disable the live preview:** in some cases only the preview is black while the saved file is correct, so turning the live preview off removes the ambiguity.

If the result is still black, post on the tutorial discussion with your GPU, ComfyUI version, install method (Desktop, portable, or manual) and the console output, plus whether the 3B and 7B workflows fail identically.

* * *

## Community Resources

  * [SeedVR2 Project Page](https://iceclear.github.io/projects/seedvr2/): Official project website
  * [ByteDance SeedVR Codebase (GitHub)](https://github.com/ByteDance-Seed/SeedVR): Original research code and paper
  * [Comfy-Org/SeedVR2 (HuggingFace)](https://huggingface.co/Comfy-Org/SeedVR2): Official ComfyUI model weights
  * [ByteDance-Seed/SeedVR2-3B (HuggingFace)](https://huggingface.co/ByteDance-Seed/SeedVR2-3B): Original 3B model weights
  * [ByteDance-Seed/SeedVR2-7B (HuggingFace)](https://huggingface.co/ByteDance-Seed/SeedVR2-7B): Original 7B model weights
  * [Paper (arXiv)](https://arxiv.org/abs/2506.05301)



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/utility/seedvr2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/utility/seedvr2)

[Video upscale](https://docs.comfy.org/tutorials/utility/video-upscale)[RelayVSR](https://docs.comfy.org/tutorials/utility/relayvsr)
