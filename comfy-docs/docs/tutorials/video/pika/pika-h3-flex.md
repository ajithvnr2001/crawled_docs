---
url: https://docs.comfy.org/tutorials/video/pika/pika-h3-flex/
title: Pika H3 Flex ComfyUI Workflows - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-30T13:55:13.457204+00:00
---

# Pika H3 Flex ComfyUI Workflows - ComfyUI

> Source: https://docs.comfy.org/tutorials/video/pika/pika-h3-flex/

## On this page

Back to top

  * Key features
  * Choosing a template Workflow
  * Text to Video (T2V)
    * Model downloads
  * Reference to Video (Ref2VA)
    * Model downloads
  * First and Last Frame (FL2VA)
    * Model downloads
  * Model storage
  * Prompting
  * FAQ



Pika

# Pika H3 Flex ComfyUI Workflows

Copy pageCopy page

Run Pika H3 Flex in ComfyUI: six-step text-to-video, reference-to-video, and first-and-last-frame Workflows with synchronized stereo audio.

Copy pageCopy page

![Pika H3 Flex](https://mintcdn.com/dripart/icfaG51neLouz0RW/images/pika/pika-h3-flex-logo-black.png?fit=max&auto=format&n=icfaG51neLouz0RW&q=85&s=728a44c1e60884f629fd3785193d68b2) ![Pika H3 Flex](https://mintcdn.com/dripart/icfaG51neLouz0RW/images/pika/pika-h3-flex-logo-white.png?fit=max&auto=format&n=icfaG51neLouz0RW&q=85&s=3816cb5dde6a980b9edf9607ffc19d10) [Pika H3 Flex](https://github.com/Pika-Labs/Pika-H3-Flex) is a post-trained version of [MiniMax H3](https://docs.comfy.org/tutorials/video/minimax/minimax-h3). Pika fine-tuned H3 on a curated multi-task corpus of video, audio, and reference examples, distilled the 50-step generator down to **six steps** , then refined it with reward feedback and preference optimization. It ships as two LoRA adapters that run on the MiniMax H3 base you already have in ComfyUI, so no new model architecture is involved.

The adapters are distributed under the [MiniMax H3 Community License Agreement](https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/LICENSE). Review its terms, including the territorial and commercial-use conditions, before using outputs commercially.

## 

​

Key features

  * **Six steps, same territory** : a 5-second 1344x768 clip finishes in about a minute on a single card, instead of the 20 to 50 steps a non-distilled H3 run needs
  * **Native stereo audio** : dialogue, SFX, and music are generated in the same pass as the picture
  * **Reference-driven control** : up to 12 references per generation (9 images, 3 videos, 3 audio clips), including motion-reference video and voice samples
  * **Multi-shot direction** : describe hard cuts, camera choreography, and dialogue inside one prompt
  * **Open weights** : the two adapters are public, and they load through the standard `LoraLoaderModelOnly` node



## 

​

Choosing a template Workflow

Three `video_pika_h3_flex_*` template Workflows are available in **Template Library** > **Video**. All three load the H3 base plus one adapter, and all three run Pika’s six-step sampling schedule.

## Text to Video

Prompt only, no image input. ComfyUI **0.43.2+**.

## Reference to Video

Two or more image references drive identity, props, and scene. ComfyUI **0.30.0+**.

## First and Last Frame

Two frames anchor the opening and the ending of the shot. ComfyUI **0.30.0+**.

The three templates ship Pika’s published six-step schedule: `lcm` with `ManualSigmas` and CFG 1.0 through `BasicGuider`. Keep the sigma list and the adapter strength at 1.0, and do not stack a turbo or Lightning LoRA on top, because the adapter is already distilled to six steps and a second acceleration LoRA breaks the output.

## 

​

Text to Video (T2V)

Generate a video with synchronized audio from a prompt alone.

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Pika H3 Flex: Text to Video” in Template Library

### 

​

Model downloads

## Diffusion Model: minimax_h3_fl2va_pruned_int8_convrot

Place in `ComfyUI/models/diffusion_models/`

## LoRA: pika_h3_flex_fl2va_v1_bf16

Place in `ComfyUI/models/loras/`

## Text Encoder: qwen3vl_32b_minimax_h3_nvfp4_awq

Place in `ComfyUI/models/text_encoders/`

## VAE: minimax_h3_video_vae_int8_convrot

Place in `ComfyUI/models/vae/`

## VAE: minimax_h3_audio_vae_fp32

Place in `ComfyUI/models/vae/`

## 

​

Reference to Video (Ref2VA)

Generate a video with synchronized audio from reference images. The references carry identity, costume, object shape, and environment, while the prompt carries the action and the shot.

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Pika H3 Flex: Reference to Video” in Template Library

## Input Image: ref_pilot_profile.png

Reference 1 in the template. Replace it with your own subject.

## Input Image: ref_subject_station.png

Reference 2 in the template. Replace it with a second subject or a scene.

### 

​

Model downloads

## Diffusion Model: minimax_h3_ref2va_pruned_int8_convrot

Place in `ComfyUI/models/diffusion_models/`

## LoRA: pika_h3_flex_ref2va_v1_bf16

Place in `ComfyUI/models/loras/`

## Text Encoder: qwen3vl_32b_minimax_h3_nvfp4_awq

Place in `ComfyUI/models/text_encoders/`

## VAE: minimax_h3_video_vae_int8_convrot

Place in `ComfyUI/models/vae/`

## VAE: minimax_h3_audio_vae_fp32

Place in `ComfyUI/models/vae/`

## 

​

First and Last Frame (FL2VA)

Animate between two still frames. The first image opens the shot, the second closes it, and the prompt describes the path between them.

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Pika H3 Flex: FL2VA” in Template Library

## Input Image: ref_popart_woman.png

First frame of the shot.

## Input Image: lastP_spin_jump_hole.png

Last frame of the shot.

### 

​

Model downloads

## Diffusion Model: minimax_h3_fl2va_pruned_int8_convrot

Place in `ComfyUI/models/diffusion_models/`

## LoRA: pika_h3_flex_fl2va_v1_bf16

Place in `ComfyUI/models/loras/`

## Text Encoder: qwen3vl_32b_minimax_h3_nvfp4_awq

Place in `ComfyUI/models/text_encoders/`

## VAE: minimax_h3_video_vae_int8_convrot

Place in `ComfyUI/models/vae/`

## VAE: minimax_h3_audio_vae_fp32

Place in `ComfyUI/models/vae/`

## 

​

Model storage

All three templates expect this layout. The H3 base files are shared with the existing MiniMax H3 templates; the only new files are the two adapters.
    
    
    ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   ├── minimax_h3_fl2va_pruned_int8_convrot.safetensors
    │   │   └── minimax_h3_ref2va_pruned_int8_convrot.safetensors
    │   ├── 📂 loras/
    │   │   ├── pika_h3_flex_fl2va_v1_bf16.safetensors
    │   │   └── pika_h3_flex_ref2va_v1_bf16.safetensors
    │   ├── 📂 text_encoders/
    │   │   └── qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors
    │   └── 📂 vae/
    │       ├── minimax_h3_video_vae_int8_convrot.safetensors
    │       └── minimax_h3_audio_vae_fp32.safetensors
    

## 

​

Prompting

Prompts follow the same structure as the rest of H3. For T2V and FL2VA, describe the style, then each shot with its camera move, then the two sound fields. For Ref2VA, use the full-reference form with `subject_definitions`, `summary`, `retention_analysis`, `detailed_description`, `overall_soundscape`, and `non_diegetic_music`, and label each reference as `<Subject 1>`, `<Picture 1>`, `<Video 1>`, or `<Audio 1>`. Read [Prompt guide](https://docs.comfy.org/tutorials/video/minimax/minimax-h3-prompt-guide) for the full syntax, including camera vocabulary and dialogue tags. Practical notes from testing the released adapters:

  * **Camera amplitude is advisory.** Describe the move as part of the shot sentence and always give it a stopping point. Explicit degrees and cut timestamps can land 0.2 to 0.3 seconds off, or in the opposite direction.
  * **Describe framing as content.** “Wide shot” alone tends to render as a medium shot; saying the subject is small inside a large empty room holds the wide framing better.
  * **Fine contact constraints are unreliable.** A hand that should stop a few centimetres away usually makes contact, so keep the beat working even if it does.
  * **Rendered text holds.** Short labels on props and products stay legible across camera moves.



## 

​

FAQ

Can I use these adapters with the existing MiniMax H3 templates?

Yes. The [MiniMax H3 templates](https://docs.comfy.org/tutorials/video/minimax/minimax-h3) use `res_multistep` with `BasicScheduler`, which is the 20-step path. Load the Pika adapter in the template’s LoRA node, switch the sampler to `lcm`, and replace the scheduler with `ManualSigmas`.

Why six steps?

Pika distilled the 50-step H3 generator with distribution matching distillation and then refined it with reward feedback. Six steps is the trained schedule, so raising the step count does not add detail, and lowering the sigma list below seven values breaks the schedule.

How many references can I wire?

The Ref2VA adapter accepts up to 9 images, 3 videos, and 3 standalone audio clips, 12 files in total. Video and audio references must each be 2 to 15 seconds, and the combined duration of each type stays within 15 seconds.

Where do the adapters come from?

Pika releases them at [Pika-Labs/Pika-H3-Flex](https://huggingface.co/Pika-Labs/Pika-H3-Flex), and Comfy republishes the ComfyUI-ready files in [Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3/tree/main/loras) under the same file names. The template nodes point at the Comfy repack.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/video/pika/pika-h3-flex.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/video/pika/pika-h3-flex)

[Prompt guide](https://docs.comfy.org/tutorials/video/minimax/minimax-h3-prompt-guide)[LTX-2.5 DFR](https://docs.comfy.org/tutorials/video/ltx/ltx-2-5-dfr)
