---
url: https://docs.comfy.org/tutorials/video/ltx/ltx-2-5-dfr/
title: LTX-2.5 DFR in ComfyUI: Image to Video with Audio - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:43.769488+00:00
---

# LTX-2.5 DFR in ComfyUI: Image to Video with Audio - ComfyUI

> Source: https://docs.comfy.org/tutorials/video/ltx/ltx-2-5-dfr/

## On this page

  * The three stages
  * Model downloads
  * Model storage
  * Workflow controls
  * Prompting tips



LTX

# LTX-2.5 DFR in ComfyUI: Image to Video with Audio

Copy pageCopy page

Run the LTX-2.5 DFR workflow in ComfyUI: a three-stage Diffusion Fidelity Rendering pipeline that generates video with synchronized audio from one image.

Copy pageCopy page

Generate a video with synchronized audio from a single image through LTX-2.5’s Diffusion Fidelity Rendering path. DFR is the production-quality recipe: a distilled transformer paired with a detailing IC-LoRA, with keyframes generated inside the clip and reused as guides by the later passes. Turn on `Switch to T2V` to run the same pipeline from text alone. For the other LTX-2.5 workflows, see the [LTX-2.5 overview](https://docs.comfy.org/tutorials/video/ltx/ltx-2-5).

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “LTX-2.5 DFR” in Template Library

## Input Image: office_garden_169_outpaint.png

Download the default input image, or use your own image.

## 

​

The three stages

Stage| Runs at| Steps| What it does  
---|---|---|---  
1\. Generate| Half the output size| 8| Denoises the video, one detailing keyframe per second, and the audio together in one pass  
2\. Spatial x2| The output size| 3| Upsamples the stage-1 latent and re-samples it with the pixel-spatial detailing IC-LoRA, using the half-resolution latent as reference  
3\. Temporal x2| 241 frames at 48 fps| 4| Doubles the frame rate over the same duration, with the stage-2 keyframes pinned as guides  
  
Every stage samples with the `euler` sampler, `cfg` 1.0, and a fixed `ManualSigmas` schedule. The checkpoint is distilled, so the step counts and the schedules are part of the recipe: changing them changes the look of the result. The third stage is optional. Turn off `Run 3rd stage - Temporal Upscale` to skip it and get a clip at the stage-2 frame rate instead. Audio is carried from stage 1 through the whole pipeline, so the sound does not change when the temporal pass runs.

## 

​

Model downloads

The DFR workflow loads the full-precision text encoder and adds the detailing IC-LoRA plus the temporal upscaler, so its model set differs from the other LTX-2.5 workflows.

## Diffusion Model: ltx-2.5-22b-distilled-transformer-comfy-int8-convrot

Place in `ComfyUI/models/diffusion_models/`

## Text Encoder: gemma4-12b-with-proj-ltx-2.5-bf16

Place in `ComfyUI/models/text_encoders/`

## Text Encoder: gemma4_e2b_it_bf16

Optional: only needed when the prompt enhancer is enabled. Place in `ComfyUI/models/text_encoders/`

## LoRA: ltx-2.5-22b-ic-lora-pixel-spatial-upscaler-x2-1.0

Place in `ComfyUI/models/loras/`

## Upscaler: ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0

Place in `ComfyUI/models/latent_upscale_models/`

## Upscaler: ltx-2.5-latent-temporal-upscaler-x2-bf16-1.0

Place in `ComfyUI/models/latent_upscale_models/`

## VAE: ltx-2.5-video-vae-bf16

Place in `ComfyUI/models/vae/`

## VAE: ltx-2.5-audio-vae-bf16

Place in `ComfyUI/models/vae/`

## 

​

Model storage
    
    
    ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   └── ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors
    │   ├── 📂 text_encoders/
    │   │   ├── gemma4-12b-with-proj-ltx-2.5-bf16.safetensors
    │   │   └── gemma4_e2b_it_bf16.safetensors (optional)
    │   ├── 📂 loras/
    │   │   └── ltx-2.5-22b-ic-lora-pixel-spatial-upscaler-x2-1.0.safetensors
    │   ├── 📂 vae/
    │   │   ├── ltx-2.5-video-vae-bf16.safetensors
    │   │   └── ltx-2.5-audio-vae-bf16.safetensors
    │   └── 📂 latent_upscale_models/
    │       ├── ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0.safetensors
    │       └── ltx-2.5-latent-temporal-upscaler-x2-bf16-1.0.safetensors
    

## 

​

Workflow controls

  * `Start image (I2V)`: the first frame. It is ignored while `Switch to T2V` is on
  * `Output size (aspect / megapixels)`: the target aspect ratio and pixel budget, rounded to multiples of 32. Stage 1 runs at half of this size
  * `Switch to T2V`: run the pipeline from text only, without a start image
  * `Float (fps)` and `Float (Duration)`: 24 fps for 5 seconds by default, which is 121 frames
  * `Enable Prompt Enhancer`: rewrite and extend the prompt with the small Gemma 4 encoder before sampling
  * `Enable Tiled Decode`: decode the VAE in tiles to lower VRAM use, at a small cost in fine detail



## 

​

Prompting tips

  1. **Write for one continuous shot** : DFR builds the clip around generated keyframes, so describe a scene that unfolds in a single take rather than a sequence of cuts
  2. **Audio in the same pass** : put spoken lines in quotes and describe ambience and effects; the model generates the audio together with the video
  3. **Keep camera moves gentle** : fast moves across noisy textures and smooth gradients are where the pipeline is most likely to show boiling or banding



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/video/ltx/ltx-2-5-dfr.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/video/ltx/ltx-2-5-dfr)

[LTX-2.5: ComfyUI Workflow ExamplesPrevious](https://docs.comfy.org/tutorials/video/ltx/ltx-2-5)[Wan Animate 2: Motion TransferNext](https://docs.comfy.org/tutorials/video/wan/wan-animate-2)

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
