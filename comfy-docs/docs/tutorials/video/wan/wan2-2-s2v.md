---
url: https://docs.comfy.org/tutorials/video/wan/wan2-2-s2v/
title: Wan2.2-S2V in ComfyUI: Audio-Driven Video Generation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:48.450177+00:00
---

# Wan2.2-S2V in ComfyUI: Audio-Driven Video Generation - ComfyUI

> Source: https://docs.comfy.org/tutorials/video/wan/wan2-2-s2v/

## On this page

  * Wan2.2 S2V ComfyUI Native Workflow
    * Wan2.2-S2V Audio-Driven Video Generation
    * 2\. Model Links
    * 3\. Workflow Instructions
    * 3.1 About Lightning LoRA
    * 3.2 About fp8_scaled and bf16 Models
    * 3.3 Step-by-Step Operation Instructions



Wan Video

# Wan2.2-S2V in ComfyUI: Audio-Driven Video Generation

Copy pageCopy page

Animate a portrait from audio with the Wan2.2-S2V workflow in ComfyUI: 14B fp8 or bf16 diffusion models plus video extension for minute-level output.

Copy pageCopy page

We’re excited to announce that Wan2.2-S2V, the advanced audio-driven video generation model, is now natively supported in ComfyUI! This powerful AI model can transform static images and audio inputs into dynamic video content, supporting dialogue, singing, performance, and various creative content needs. **Model Highlights**

  * **Audio-Driven Video Generation** : Transforms static images and audio into synchronized videos
  * **Cinematic-Grade Quality** : Generates film-quality videos with natural expressions and movements
  * **Minute-Level Generation** : Supports long-form video creation
  * **Multi-Format Support** : Works with full-body and half-body characters
  * **Enhanced Motion Control** : Generates actions and environments from text instructions

Wan2.2 S2V Code: [GitHub](https://github.com/aigc-apps/VideoX-Fun) Wan2.2 S2V Model: [Hugging Face](https://huggingface.co/Wan-AI/Wan2.2-S2V-14B)

## 

​

Wan2.2 S2V ComfyUI Native Workflow

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

### 

​

Wan2.2-S2V Audio-Driven Video Generation

Transform static images and audio into dynamic videos with perfect synchronization and minute-level generation. ![Wan2.2-S2V Audio-Driven Video Generation workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan2_2_14B_s2v-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Wan2.2 S2V” in Template Library

**Input materials** Upload these files to the matching nodes:

## video_wan2_2_14B_s2v_reference_image.jpg

`LoadImage` node 52 · `video_wan2_2_14B_s2v_reference_image.jpg`

## video_wan2_2_14B_s2v_input_audio.MP3

`LoadAudio` node 58 · `video_wan2_2_14B_s2v_input_audio.MP3`

![video_wan2_2_14B_s2v_reference_image.jpg](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/video_wan2_2_14B_s2v_reference_image.jpg)

### 

​

2\. Model Links

You can find the models in [our repo](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged) **diffusion_models**

## wan2.2_s2v_14B_fp8_scaled.safetensors

FP8 scaled diffusion model. Place in `ComfyUI/models/diffusion_models/`

## wan2.2_s2v_14B_bf16.safetensors

BF16 diffusion model. Place in `ComfyUI/models/diffusion_models/`

**audio_encoders**

## wav2vec2_large_english_fp16.safetensors

Audio encoder model. Place in `ComfyUI/models/audio_encoders/`

**vae**

## wan_2.1_vae.safetensors

Wan2.1 VAE model. Place in `ComfyUI/models/vae/`

**text_encoders**

## umt5_xxl_fp8_e4m3fn_scaled.safetensors

FP8 scaled text encoder. Place in `ComfyUI/models/text_encoders/`
    
    
    ComfyUI/
    ├───📂 models/
    │   ├───📂 diffusion_models/
    │   │   ├─── wan2.2_s2v_14B_fp8_scaled.safetensors
    │   │   └─── wan2.2_s2v_14B_bf16.safetensors
    │   ├───📂 text_encoders/
    │   │   └─── umt5_xxl_fp8_e4m3fn_scaled.safetensors 
    │   ├───📂 audio_encoders/ # Create one if you can't find this folder
    │   │   └─── wav2vec2_large_english_fp16.safetensors 
    │   └───📂 vae/
    │       └── wan_2.1_vae.safetensors
    

### 

​

3\. Workflow Instructions

![Workflow Instructions](https://mintcdn.com/dripart/ht3vzHrjy1qaRsl9/images/tutorial/video/wan/wan_2.2_14b_s2v.jpg?fit=max&auto=format&n=ht3vzHrjy1qaRsl9&q=85&s=295f87179e12d937cbfbcc3e21d474c0)

#### 

​

3.1 About Lightning LoRA

#### 

​

3.2 About fp8_scaled and bf16 Models

You can find both models [here](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/tree/main/split_files/diffusion_models):

## wan2.2_s2v_14B_fp8_scaled.safetensors

FP8 scaled diffusion model

## wan2.2_s2v_14B_bf16.safetensors

BF16 diffusion model

This template uses `wan2.2_s2v_14B_fp8_scaled.safetensors`, which requires less VRAM. But you can try `wan2.2_s2v_14B_bf16.safetensors` to reduce quality degradation.

#### 

​

3.3 Step-by-Step Operation Instructions

**Step 1: Load Models**

  1. **Load Diffusion Model** : Load `wan2.2_s2v_14B_fp8_scaled.safetensors` or `wan2.2_s2v_14B_bf16.safetensors`
     * The provided workflow uses `wan2.2_s2v_14B_fp8_scaled.safetensors`, which requires less VRAM
     * But you can try `wan2.2_s2v_14B_bf16.safetensors` to reduce quality degradation
  2. **Load CLIP** : Load `umt5_xxl_fp8_e4m3fn_scaled.safetensors`
  3. **Load VAE** : Load `wan_2.1_vae.safetensors`
  4. **AudioEncoderLoader** : Load `wav2vec2_large_english_fp16.safetensors`
  5. **LoraLoaderModelOnly** : Load `wan2.2_t2v_lightx2v_4steps_lora_v1.1_high_noise.safetensors` (Lightning LoRA)
     * We tested all wan2.2 lightning LoRAs. Since this is not a LoRA specifically trained for Wan2.2 S2V, many key values don’t match, but we added it because it significantly reduces generation time. We will continue to optimize this template
     * Using it will cause significant dynamic and quality loss
     * If you find the output quality too poor, you can try the original 20-step workflow
  6. **LoadAudio** : Upload our provided audio file or your own audio
  7. **Load Image** : Upload reference image
  8. **Batch sizes** : Set according to the number of Video S2V Extend subgraph nodes you add
     * Each Video S2V Extend subgraph adds 77 frames to the final output
     * For example: If you added 2 Video S2V Extend subgraphs, the batch size should be 3, which means the total number of sampling iterations
     * **Chunk Length** : Keep the default value of 77
  9. **Sampler Settings** : Choose different settings based on whether you use Lightning LoRA
     * With 4-step Lightning LoRA: steps: 4, cfg: 1.0
     * Without 4-step Lightning LoRA: steps: 20, cfg: 6.0
  10. **Size Settings** : Set the output video dimensions
  11. **Video S2V Extend** : Video extension subgraph nodes. Since our default frames per sampling is 77, and this is a 16fps model, each extension will generate 77 / 16 = 4.8125 seconds of video
     * You need some calculation to match the number of video extension subgraph nodes with the input audio length. For example: If input audio is 14s, the total frames needed are 14x16=224, each video extension is 77 frames, so you need 224/77 = 2.9, rounded up to 3 video extension subgraph nodes
  12. Use Ctrl-Enter or click the Run button to execute the workflow



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/video/wan/wan2-2-s2v.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/video/wan/wan2-2-s2v)

[Wan Dancer: Music to Dance Video GenerationPrevious](https://docs.comfy.org/tutorials/video/wan/wan-dancer)[Wan2.2 Fun InP in ComfyUI: Start and End Frame VideoNext](https://docs.comfy.org/tutorials/video/wan/wan2-2-fun-inp)

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
