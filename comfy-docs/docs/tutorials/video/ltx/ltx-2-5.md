---
url: https://docs.comfy.org/tutorials/video/ltx/ltx-2-5/
title: LTX-2.5: ComfyUI Workflow Examples - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:43.985716+00:00
---

# LTX-2.5: ComfyUI Workflow Examples - ComfyUI

> Source: https://docs.comfy.org/tutorials/video/ltx/ltx-2-5/

## On this page

  * Key features
  * Getting started
  * ComfyUI Native Workflows
    * LTX-2.5 Text to Video (T2V)
    * Model downloads
    * Model storage
    * Prompting tips
    * LTX-2.5 Image to Video (I2V)
    * Model downloads
    * Model storage
    * Prompting tips
    * LTX-2.5 FLF2V
    * Model downloads
    * Model storage
    * Prompting tips
  * LTX-2.5 DFR: Image to Video
  * Resources



LTX

# LTX-2.5: ComfyUI Workflow Examples

Copy pageCopy page

Use LTX-2.5 in ComfyUI with native text-to-video, image-to-video, and first-last-frame workflows, including synchronized audio and native multishot scenes.

Copy pageCopy page

[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5) is Lightricks’ open-weights video and world model, natively supported in ComfyUI. It builds on LTX-2.3 with a Diffusion Fidelity Rendering pipeline that allocates rendering compute by scene complexity. The model keeps the synchronized audio and video generation of LTX-2.3 and adds native multishot: one generation produces multiple connected shots that hold character, environment, lighting, and voice across cuts. LTX-2.5 ships with a custom Gemma 4 12B text encoder that retains multiple subjects, actions, lighting, and camera direction across complex prompts, plus an optional prompt enhancer that expands short prompts into detailed instructions. Auto duration predicts the clip length from the described action before diffusion begins. The distilled model provides faster generation, and output supports native 4K HDR at up to 50 FPS with a RAW workflow for professional finishing pipelines. ComfyUI ships with four native workflows for LTX-2.5:

  * **Text-to-Video** (T2V): Generate videos from text prompts
  * **Image-to-Video** (I2V): Generate videos from an input image
  * **FLF2V** : Interpolate between a first and last frame image
  * **DFR** : Generate a video with audio through the Diffusion Fidelity Rendering pipeline, from an image or from text



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

  * **Diffusion Fidelity Rendering** : keyframes-first generation that builds every scene on a grid of high-fidelity keyframes
  * **Diffusion Video Decoder** : sharper faces, legible text, and fewer smears in fast motion
  * **Native multishot** : one generation yields multiple connected shots holding character, environment, lighting, voice, and style across cuts
  * **Gemma 4 12B text encoder** : retains multiple subjects, actions, lighting, detail, and camera direction across complex prompts
  * **Prompt enhancer** _(optional)_ : a lightweight model that expands short prompts into detailed instructions
  * **Auto duration** : predicts the right clip length from the described action before diffusion begins
  * **Native 4K HDR** : high-resolution HDR output built for professional finishing, with synchronized audio-video at up to 50 FPS



## 

​

Getting started

LTX-2.5 is natively supported in ComfyUI. To get started:

  1. Update ComfyUI to the latest version
  2. Go to **Template Library** > **Video** > choose any LTX-2.5 workflow
  3. Request access to the model repository on Hugging Face (see below), then follow the pop-up to download models and run the workflow



The LTX-2.5 model files are hosted in the gated [Lightricks/LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5) and [Lightricks/LTX-2.5-22b-IC-LoRA-Pixel-Spatial-Upscaler](https://huggingface.co/Lightricks/LTX-2.5-22b-IC-LoRA-Pixel-Spatial-Upscaler) repositories on Hugging Face. Open the repository pages, accept the model license, and wait for your access request to be approved before downloading the models. Model downloads will fail without access.

## 

​

ComfyUI Native Workflows

### 

​

LTX-2.5 Text to Video (T2V)

Generate videos from text prompts with optional spatial upscaling for enhanced resolution.

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “LTX-2.5 T2V” in Template Library

#### 

​

Model downloads

## Diffusion Model: ltx-2.5-22b-distilled-transformer-comfy-int8-convrot

Place in `ComfyUI/models/diffusion_models/`

## Text Encoder: gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot

Place in `ComfyUI/models/text_encoders/`

## Text Encoder: gemma4_e2b_it_int8_convrot

Optional: only needed when the prompt enhancer is enabled. Place in `ComfyUI/models/text_encoders/`

## VAE: ltx-2.5-video-vae-bf16

Place in `ComfyUI/models/vae/`

## VAE: ltx-2.5-audio-vae-bf16

Place in `ComfyUI/models/vae/`

## Upscaler: ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0

Place in `ComfyUI/models/latent_upscale_models/`

#### 

​

Model storage
    
    
    ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   └── ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors
    │   ├── 📂 text_encoders/
    │   │   ├── gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors
    │   │   └── gemma4_e2b_it_int8_convrot.safetensors (optional)
    │   ├── 📂 vae/
    │   │   ├── ltx-2.5-video-vae-bf16.safetensors
    │   │   └── ltx-2.5-audio-vae-bf16.safetensors
    │   └── 📂 latent_upscale_models/
    │       └── ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0.safetensors
    

#### 

​

Prompting tips

  1. **Describe the whole scene** : Include the shot type, scene, action, characters, and camera movement in one flowing paragraph
  2. **Audio** : Describe sounds and dialogue needed for the scene; the model generates synchronized audio together with the video
  3. **Use the prompt enhancer (optional)** : The workflow keeps it off by default. Enable `prompt_enhance` on the LTX-2.5 node to expand short prompts into detailed cinematic instructions. It needs the separate enhancer model (~5 GB) and adds about 1-2 minutes of generation time



* * *

### 

​

LTX-2.5 Image to Video (I2V)

Generate videos from an input image, with the model animating the scene from the provided first frame.

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “LTX-2.5 I2V” in Template Library

## Input Image: neon_cyborg_portrait.png

Download the default input image, or use your own image.

#### 

​

Model downloads

The I2V workflow uses the same model set as Text-to-Video.

## Diffusion Model: ltx-2.5-22b-distilled-transformer-comfy-int8-convrot

Place in `ComfyUI/models/diffusion_models/`

## Text Encoder: gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot

Place in `ComfyUI/models/text_encoders/`

## Text Encoder: gemma4_e2b_it_int8_convrot

Optional: only needed when the prompt enhancer is enabled. Place in `ComfyUI/models/text_encoders/`

## VAE: ltx-2.5-video-vae-bf16

Place in `ComfyUI/models/vae/`

## VAE: ltx-2.5-audio-vae-bf16

Place in `ComfyUI/models/vae/`

## Upscaler: ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0

Place in `ComfyUI/models/latent_upscale_models/`

#### 

​

Model storage
    
    
    ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   └── ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors
    │   ├── 📂 text_encoders/
    │   │   ├── gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors
    │   │   └── gemma4_e2b_it_int8_convrot.safetensors (optional)
    │   ├── 📂 vae/
    │   │   ├── ltx-2.5-video-vae-bf16.safetensors
    │   │   └── ltx-2.5-audio-vae-bf16.safetensors
    │   └── 📂 latent_upscale_models/
    │       └── ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0.safetensors
    

#### 

​

Prompting tips

  1. **Describe what happens next** : Write the motion, camera movement, and sounds that follow from the input image; do not re-describe what is already visible
  2. **Anchor the first frame** : Use phrasing like “Use the provided start image as the first frame” when writing a continuation
  3. **Audio** : Describe dialogue and sounds for the scene; the model generates synchronized audio



* * *

### 

​

LTX-2.5 FLF2V

Generate a video between a first and last frame image, blending both frames into a single animated sequence.

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “LTX-2.5 FLF2V” in Template Library

## First Frame: robot_hand_back.png

First frame of the video.

## Last Frame: robot_hand_energy.png

Last frame of the video.

#### 

​

Model downloads

The FLF2V workflow uses the same model set as Text-to-Video, without the spatial upscaler.

## Diffusion Model: ltx-2.5-22b-distilled-transformer-comfy-int8-convrot

Place in `ComfyUI/models/diffusion_models/`

## Text Encoder: gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot

Place in `ComfyUI/models/text_encoders/`

## Text Encoder: gemma4_e2b_it_int8_convrot

Optional: only needed when the prompt enhancer is enabled. Place in `ComfyUI/models/text_encoders/`

## VAE: ltx-2.5-video-vae-bf16

Place in `ComfyUI/models/vae/`

## VAE: ltx-2.5-audio-vae-bf16

Place in `ComfyUI/models/vae/`

#### 

​

Model storage
    
    
    ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   └── ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors
    │   ├── 📂 text_encoders/
    │   │   ├── gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors
    │   │   └── gemma4_e2b_it_int8_convrot.safetensors (optional)
    │   └── 📂 vae/
    │       ├── ltx-2.5-video-vae-bf16.safetensors
    │       └── ltx-2.5-audio-vae-bf16.safetensors
    

#### 

​

Prompting tips

  1. **Describe the transition** : Write what happens between the two frames, including camera movement and audio
  2. **Keep frames aligned** : Use images with the same aspect ratio for a smooth interpolation
  3. **Audio** : Describe dialogue and sounds for the scene; the model generates synchronized audio



* * *

## 

​

LTX-2.5 DFR: Image to Video

DFR is the production-quality recipe: a distilled transformer paired with a detailing IC-LoRA, with keyframes generated inside the clip and reused as guides by the later passes. It runs from an image, or from text with `Switch to T2V`. It has its own page: [LTX-2.5 DFR: Image to Video](https://docs.comfy.org/tutorials/video/ltx/ltx-2-5-dfr).

## 

​

Resources

  * [Hugging Face Model](https://huggingface.co/Lightricks/LTX-2.5)
  * [LTX Model Page](https://ltx.io/model/ltx-2-5)
  * [GitHub Repository](https://github.com/Lightricks/LTX-Video)
  * [ComfyUI-LTXVideo](https://github.com/Lightricks/ComfyUI-LTXVideo/)



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/video/ltx/ltx-2-5.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/video/ltx/ltx-2-5)

[LTX-2.3: ComfyUI Workflow ExamplesPrevious](https://docs.comfy.org/tutorials/video/ltx/ltx-2-3)[LTX-2.5 DFR in ComfyUI: Image to Video with AudioNext](https://docs.comfy.org/tutorials/video/ltx/ltx-2-5-dfr)

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
