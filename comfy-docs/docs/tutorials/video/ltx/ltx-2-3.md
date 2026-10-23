---
url: https://docs.comfy.org/tutorials/video/ltx/ltx-2-3/
title: LTX-2.3: ComfyUI Workflow Examples - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:43.408534+00:00
---

# LTX-2.3: ComfyUI Workflow Examples - ComfyUI

> Source: https://docs.comfy.org/tutorials/video/ltx/ltx-2-3/

## On this page

  * Key features
  * Getting started
  * ComfyUI Native Workflows
    * LTX-2.3 Text to Video (T2V)
    * LTX-2.3 Text to Video
    * Model downloads
    * Model storage
    * Prompting tips
    * LTX-2.3 Image to Video (I2V)
    * LTX-2.3 Image to Video
    * Model downloads
    * Model storage
    * LTX-2.3 FLF2V
    * LTX-2.3 First-Last Frame to Video
    * Model downloads
    * Model storage
    * LTX-2.3 Image Audio to Video (IA2V)
    * LTX-2.3 Image and Audio to Video
    * Model downloads
    * Model storage
    * LTX-2.3 IC-LoRA Union Control
    * Model downloads
    * Model storage
    * Video editing with IC-LoRA
    * Remove Subtitles from Video
    * Remove Object from Video
    * Restore Archival Footage
    * Video Outpainting
    * Googly Eyes
    * LTX-2.3 ID-LoRA
    * LTX-2.3 ID LoRA
    * Model downloads
    * Model storage
  * Prompting tips
  * Resources



LTX

# LTX-2.3: ComfyUI Workflow Examples

Copy pageCopy page

Use LTX-2.3 in ComfyUI with native workflows for text-to-video, image-to-video, FLF2V, audio-driven video, IC-LoRA control, and ID-LoRA personalization.

Copy pageCopy page

[LTX-2.3](https://huggingface.co/Lightricks/LTX-2.3) is the latest evolution of Lightricks’ open-source audio-video generation model, now natively supported in ComfyUI. Building on LTX-2, this release delivers major quality improvements across fine details, portrait video, audio quality, image-to-video consistency, prompt understanding, and text rendering. ComfyUI ships with six native workflows for LTX-2.3, each designed for a specific generation mode:

  * **Text-to-Video** (T2V): Generate videos from text prompts
  * **Image-to-Video** (I2V): Generate videos from an input image
  * **FLF2V** : Interpolate between a start and end image
  * **Image-Audio-to-Video** (IA2V): Generate lip-synced videos from an image and audio
  * **IC-LoRA Union Control** : Control video generation with depth, pose, or edge guidance
  * **ID-LoRA** : Generate personalized videos with synchronized audio from a reference image and audio clip



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

Key features

  * **Finer details** : New latent space and updated VAE for sharper textures, cleaner edges, and more precise visuals
  * **9:16 Portrait support** : Greatly improved quality for vertical portrait videos
  * **Better audio** : Cleaner sound with reduced noise and enhanced dialogue
  * **Improved image-to-video** : More consistent motion and fewer glitches
  * **Smarter prompt understanding** : Improved text encoder for more accurate interpretation
  * **Native ComfyUI support** : All workflows are built-in, no custom nodes required



## 

​

Getting started

LTX-2.3 is natively supported in ComfyUI. To get started:

  1. Update ComfyUI to the latest version
  2. Go to **Template Library** > **Video** > choose any LTX-2.3 workflow
  3. Follow the pop-up to download models and run the workflow



## 

​

ComfyUI Native Workflows

### 

​

LTX-2.3 Text to Video (T2V)

Generate videos from text prompts with improved prompt understanding and text rendering.

### 

​

LTX-2.3 Text to Video

Generate videos from text prompts with improved prompt understanding and text rendering. ![LTX-2.3 Text to Video \( workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_3_t2v-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “LTX-2.3 T2V” in Template Library

#### 

​

Model downloads

## Checkpoint: ltx-2.3-22b-dev-fp8

Place in `ComfyUI/models/checkpoints/`

## LoRA: distilled 1.1

Place in `ComfyUI/models/loras/`

## LoRA: gemma abliterated

Place in `ComfyUI/models/loras/`

## Text Encoder: gemma 12B

Place in `ComfyUI/models/text_encoders/`

## Upscaler: spatial x2

Place in `ComfyUI/models/latent_upscale_models/`

#### 

​

Model storage
    
    
    ComfyUI/
    ├── 📂 models/
    │   ├── 📂 checkpoints/
    │   │   └── ltx-2.3-22b-dev-fp8.safetensors
    │   ├── 📂 loras/
    │   │   ├── ltx_2.3_22b_distilled_1.1_lora_dynamic_fro09_avg_rank_111_bf16.safetensors
    │   │   └── gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors
    │   ├── 📂 text_encoders/
    │   │   └── gemma_3_12B_it_fp4_mixed.safetensors
    │   └── 📂 latent_upscale_models/
    │       └── ltx-2.3-spatial-upscaler-x2-1.1.safetensors
    

#### 

​

Prompting tips

  1. **Core Actions** : Describe events and actions as they occur over time
  2. **Visual Details** : Describe all visual details you want to appear in the video
  3. **Audio** : Describe sounds and dialogue needed for the scene



* * *

### 

​

LTX-2.3 Image to Video (I2V)

Generate videos from an input image with more consistent motion and smoother animations.

### 

​

LTX-2.3 Image to Video

Generate videos from an input image with improved motion consistency. ![LTX-2.3 Image to Video \( workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_3_i2v-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “LTX-2.3 I2V” in Template Library

## Input Image: egyptian_queen.png

Download the default input image, or use your own image.

#### 

​

Model downloads

The I2V workflow uses the same model set as Text-to-Video.

## Checkpoint: ltx-2.3-22b-dev-fp8

Place in `ComfyUI/models/checkpoints/`

## LoRA: distilled 1.1

Place in `ComfyUI/models/loras/`

## LoRA: gemma abliterated

Place in `ComfyUI/models/loras/`

## Text Encoder: gemma 12B

Place in `ComfyUI/models/text_encoders/`

## Upscaler: spatial x2

Place in `ComfyUI/models/latent_upscale_models/`

#### 

​

Model storage
    
    
    ComfyUI/
    ├── 📂 models/
    │   ├── 📂 checkpoints/
    │   │   └── ltx-2.3-22b-dev-fp8.safetensors
    │   ├── 📂 loras/
    │   │   ├── ltx_2.3_22b_distilled_1.1_lora_dynamic_fro09_avg_rank_111_bf16.safetensors
    │   │   └── gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors
    │   ├── 📂 text_encoders/
    │   │   └── gemma_3_12B_it_fp4_mixed.safetensors
    │   └── 📂 latent_upscale_models/
    │       └── ltx-2.3-spatial-upscaler-x2-1.1.safetensors
    

* * *

### 

​

LTX-2.3 FLF2V

Interpolate between a start image and an end image to generate a smooth video transition.

### 

​

LTX-2.3 First-Last Frame to Video

Interpolate between a start and end image. ![LTX-2.3 First-Last Frame to Video \( workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_3_flf2v-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “LTX-2.3 FLF2V” in Template Library

## Start Image: high_view_classic_car.png

First frame of the video.

## End Image: low_view_classic_car.png

Last frame of the video.

#### 

​

Model downloads

The FLF2V workflow uses the distilled checkpoint instead of the dev checkpoint.

## Checkpoint: ltx-2.3-22b-distilled-fp8

Place in `ComfyUI/models/checkpoints/`

## Text Encoder: gemma 12B

Place in `ComfyUI/models/text_encoders/`

#### 

​

Model storage
    
    
    ComfyUI/
    ├── 📂 models/
    │   ├── 📂 checkpoints/
    │   │   └── ltx-2.3-22b-distilled-fp8.safetensors
    │   └── 📂 text_encoders/
    │       └── gemma_3_12B_it_fp4_mixed.safetensors
    

* * *

### 

​

LTX-2.3 Image Audio to Video (IA2V)

Upload an image and an audio file to generate a high-quality video with synchronized lip movements.

### 

​

LTX-2.3 Image and Audio to Video

Generate lip-synced videos from an image and audio. ![LTX-2.3 Image and Audio to Video \( workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_3_ia2v-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “LTX-2.3 IA2V” in Template Library

## Input Image: cactus_man.png

Reference image for the speaking character.

## Reference Audio: ltx_23_audio.mp3

Audio track for lip synchronization.

#### 

​

Model downloads

The IA2V workflow uses the same model set as Text-to-Video.

## Checkpoint: ltx-2.3-22b-dev-fp8

Place in `ComfyUI/models/checkpoints/`

## LoRA: distilled 1.1

Place in `ComfyUI/models/loras/`

## LoRA: gemma abliterated

Place in `ComfyUI/models/loras/`

## Text Encoder: gemma 12B

Place in `ComfyUI/models/text_encoders/`

## Upscaler: spatial x2

Place in `ComfyUI/models/latent_upscale_models/`

#### 

​

Model storage
    
    
    ComfyUI/
    ├── 📂 models/
    │   ├── 📂 checkpoints/
    │   │   └── ltx-2.3-22b-dev-fp8.safetensors
    │   ├── 📂 loras/
    │   │   ├── ltx_2.3_22b_distilled_1.1_lora_dynamic_fro09_avg_rank_111_bf16.safetensors
    │   │   └── gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors
    │   ├── 📂 text_encoders/
    │   │   └── gemma_3_12B_it_fp4_mixed.safetensors
    │   └── 📂 latent_upscale_models/
    │       └── ltx-2.3-spatial-upscaler-x2-1.1.safetensors
    

* * *

### 

​

LTX-2.3 IC-LoRA Union Control

Generate LTX-2.3 videos with IC-LoRA using aligned control inputs like depth, pose, or edges. IC-LoRA is an in-context LoRA trained on top of LTX-2.3 that applies structural guidance from a reference video. It accepts control signals from various preprocessors including depth maps, Canny edges, and pose skeletons. This workflow uses a subgraph for modular processing. ![LTX-2.3 IC-LoRA preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_3_ic_lora-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “LTX-2.3 IC-LoRA” in Template Library

## Learn about Subgraph

This workflow uses a Subgraph node for modular processing. Check out the Subgraph documentation to learn how to customize and extend the workflow.

**Input materials**

## Control Video: stone_ruins.mp4

Driving video for control signal extraction.

## Reference Image: the_forgotten_gate.png

Reference image for style and content.

#### 

​

Model downloads

## Checkpoint: ltx-2.3-22b-distilled-fp8

Place in `ComfyUI/models/checkpoints/`

## LoRA: IC-LoRA Union Control

Place in `ComfyUI/models/loras/`

## LoRA: gemma abliterated

Place in `ComfyUI/models/loras/`

## Text Encoder: gemma 12B

Place in `ComfyUI/models/text_encoders/`

## Geometry: MoGe Normal

Place in `ComfyUI/models/geometry_estimation/`

#### 

​

Model storage
    
    
    ComfyUI/
    ├── 📂 models/
    │   ├── 📂 checkpoints/
    │   │   └── ltx-2.3-22b-distilled-fp8.safetensors
    │   ├── 📂 loras/
    │   │   ├── ltx-2.3-22b-ic-lora-union-control-ref0.5.safetensors
    │   │   └── gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors
    │   ├── 📂 text_encoders/
    │   │   └── gemma_3_12B_it_fp4_mixed.safetensors
    │   └── 📂 geometry_estimation/
    │       └── moge_2_vitl_normal_fp16.safetensors
    

* * *

### 

​

Video editing with IC-LoRA

IC-LoRA weights are not limited to generation control. The Template Library includes ready-made LTX-2.3 IC-LoRA workflows for editing existing footage, and each one runs in Comfy Cloud or locally in ComfyUI. Community IC-LoRA checkpoints trained on top of LTX-2.3 (for example, the [LTX2.3-ICEdit-Insight](https://huggingface.co/joyfox/LTX2.3-ICEdit-Insight) family) are also compatible with the native LTX-2.3 model.

#### 

​

Remove Subtitles from Video

Remove subtitles, captions, watermarks, or other text overlays from a video: ![LTX-2.3 Remove Subtitles workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_ltx2_3_lora_remove_subtitles_from_video-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Remove Subtitles” in Template Library

#### 

​

Remove Object from Video

Remove a specific object from the foreground of a video by describing it in the prompt: ![LTX-2.3 Remove Object workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_ltx2_3_obscura_remova_lora_remove_object_from_video-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Remove Object” in Template Library

#### 

​

Restore Archival Footage

Restore old or degraded archival footage: ![LTX-2.3 Restore Archival Footage workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_ltx2_3_lora_restore_archival_footage-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Restore Archival” in Template Library

#### 

​

Video Outpainting

Expand a video in any direction using the LTX-2.3 Video Outpainting IC-LoRA: ![LTX-2.3 Video Outpainting workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_ltx2_3_lora_video_outpainting-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Video Outpainting” in Template Library

#### 

​

Googly Eyes

Apply the Googlyeyes LTX-2.3 LoRA to an input video to give everyone in the frame googly eyes: ![LTX-2.3 Googly Eyes workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_ltx2_3_lora_googly_eyes-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Googly Eyes” in Template Library

For community IC-LoRAs, place the editing LoRA in `ComfyUI/models/loras/` and load it with a LoRA loader alongside the LTX-2.3 checkpoint, then run the workflow with your video as input and a prompt like:
    
    
    Remove subtitles, captions, and related text occlusions from the video, restoring a clean and natural underlying image.
    

* * *

### 

​

LTX-2.3 ID-LoRA

Generate personalized videos with synchronized audio from a text prompt, reference image, and short audio clip. Uses ID-LoRA to adapt a person’s appearance and voice in a single generative model.

### 

​

LTX-2.3 ID LoRA

Generate personalized videos with synchronized audio from a reference image and audio clip. ![LTX-2.3 ID LoRA \( workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_3_id_lora-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “LTX-2.3 ID-LoRA” in Template Library

## Reference Image: vintage_thinker.png

Reference image for the character appearance.

## Reference Audio: ltx23_reference_audio.mp3

Audio clip for voice cloning and lip sync.

#### 

​

Model downloads

## Checkpoint: ltx-2.3-22b-dev-fp8

Place in `ComfyUI/models/checkpoints/`

## LoRA: distilled 1.1

Place in `ComfyUI/models/loras/`

## LoRA: ID-LoRA TalkVid

Place in `ComfyUI/models/loras/`

## Text Encoder: gemma 12B

Place in `ComfyUI/models/text_encoders/`

## Upscaler: spatial x2

Place in `ComfyUI/models/latent_upscale_models/`

#### 

​

Model storage
    
    
    ComfyUI/
    ├── 📂 models/
    │   ├── 📂 checkpoints/
    │   │   └── ltx-2.3-22b-dev-fp8.safetensors
    │   ├── 📂 loras/
    │   │   ├── ltx_2.3_22b_distilled_1.1_lora_dynamic_fro09_avg_rank_111_bf16.safetensors
    │   │   └── ltx-2.3-id-lora-talkvid-3k.safetensors
    │   ├── 📂 text_encoders/
    │   │   └── gemma_3_12B_it_fp4_mixed.safetensors
    │   └── 📂 latent_upscale_models/
    │       └── ltx-2.3-spatial-upscaler-x2-1.1.safetensors
    

## 

​

Prompting tips

When writing prompts for LTX-2.3, focus on detailed, chronological descriptions of actions and scenes:

  1. **Core Actions** : Describe events and actions as they occur over time
  2. **Visual Details** : Describe all visual details you want to appear in the video
  3. **Audio** : Describe sounds and dialogue needed for the scene



## 

​

Resources

  * [Hugging Face Model](https://huggingface.co/Lightricks/LTX-2.3)
  * [GitHub Repository](https://github.com/Lightricks/LTX-2)
  * [ComfyUI-LTXVideo](https://github.com/Lightricks/ComfyUI-LTXVideo/)
  * [IC-LoRA Model](https://huggingface.co/Lightricks/LTX-2.3-22b-IC-LoRA-Union-Control)



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/video/ltx/ltx-2-3.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/video/ltx/ltx-2-3)

[LTX-2.0 ComfyUI Workflow ExamplesPrevious](https://docs.comfy.org/tutorials/video/ltx/ltx-2)[LTX-2.5: ComfyUI Workflow ExamplesNext](https://docs.comfy.org/tutorials/video/ltx/ltx-2-5)

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
