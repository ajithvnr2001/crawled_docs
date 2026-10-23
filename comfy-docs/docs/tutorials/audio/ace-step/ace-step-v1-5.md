---
url: https://docs.comfy.org/tutorials/audio/ace-step/ace-step-v1-5/
title: ACE-Step 1.5 in ComfyUI: Local AI Music Generation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-19T14:35:06.421273+00:00
---

# ACE-Step 1.5 in ComfyUI: Local AI Music Generation - ComfyUI

> Source: https://docs.comfy.org/tutorials/audio/ace-step/ace-step-v1-5/

## On this page

  * Option 1: All-in-One Checkpoint (Recommended)
    * ACE-Step 1.5 Music Generation AIO
    * AIO Model Download
  * Option 2: Split Model Files
    * ACE-Step 1.5 Music Generation Workflow
    * Split Model Downloads
  * ACE-Step 1.5 Key Features in ComfyUI
    * Chain-of-Thought Planning
    * Hybrid LM + DiT Architecture
  * Coming Soon to ComfyUI
  * ACE-Step 1.5 ComfyUI Related Resources



ACE-Step

# ACE-Step 1.5 in ComfyUI: Local AI Music Generation

Copy pageCopy page

Generate complete songs locally in ComfyUI with ACE-Step 1.5, an open-source music model that turns a text description and optional lyrics into audio.

Copy pageCopy page

ACE-Step 1.5 is an open-source music generation model from ACE Studio and StepFun that turns a text description and optional lyrics into a complete song. ComfyUI runs it natively, so you can generate full tracks locally, from 10-second loops to multi-minute compositions. At the core of the model is a language model planner paired with a Diffusion Transformer (DiT) audio decoder. The planner expands a simple query into a song blueprint, synthesizing structure, metadata, lyrics, and captions through Chain-of-Thought reasoning, and the DiT renders the audio. Alignment relies on the model’s own internal mechanisms instead of an external reward model or human preference data. Generation is fast enough for interactive sessions: under 2 seconds for a full song on an A100 and under 10 seconds on an RTX 3090. The under 4 GB VRAM configuration runs the DiT alone with the LM planner disabled. Training a LoRA on a few songs is enough to capture your own style.

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

**Model highlights** :

  * **Commercial-grade quality** : Quality beyond most commercial music models, with a musical coherence score of 4.72
  * **Fast generation** : A full song in under 2 seconds on an A100, or under 10 seconds on an RTX 3090
  * **Long-form output** : Durations from 10 seconds up to 10 minutes
  * **50+ languages** : Strong support for English, Chinese, Japanese, Korean, Spanish, German, French, Portuguese, Italian, and Russian
  * **LoRA fine-tuning** : Lightweight personalization through LoRA training in ComfyUI



## 

​

Option 1: All-in-One Checkpoint (Recommended)

The AIO version packages all models into a single checkpoint file, making it easier to download and manage.

### 

​

ACE-Step 1.5 Music Generation AIO

Input style tags and lyrics to generate a full song. The workflow uses the ACE-Step 1.5 model to produce commercial-grade music in under 10 seconds on consumer hardware.

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “ACE-Step 1.5 Music Generation AIO” in Template Library

### 

​

AIO Model Download

## ace_step_1.5_turbo_aio.safetensors

All-in-one checkpoint file (recommended for most users).

**AIO Model Storage Location**
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   └── 📂 checkpoints/
    │       └── ace_step_1.5_turbo_aio.safetensors
    

## 

​

Option 2: Split Model Files

The split version allows you to download individual model components separately.

### 

​

ACE-Step 1.5 Music Generation Workflow

Input a text prompt describing the music style and optional lyrics. Generate a full, high-quality audio song in under 10 seconds on consumer hardware.

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “ACE-Step 1.5 Music Generation Workflow” in Template Library

### 

​

Split Model Downloads

## acestep_v1.5_turbo.safetensors

Diffusion model.

## qwen_0.6b_ace15.safetensors

Text encoder (0.6B).

## qwen_1.7b_ace15.safetensors

Text encoder (1.7B).

## ace_1.5_vae.safetensors

VAE model.

**Split Models Storage Location**
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   └── acestep_v1.5_turbo.safetensors
    │   ├── 📂 text_encoders/
    │   │   ├── qwen_0.6b_ace15.safetensors
    │   │   └── qwen_1.7b_ace15.safetensors
    │   └── 📂 vae/
    │       └── ace_1.5_vae.safetensors
    

## 

​

ACE-Step 1.5 Key Features in ComfyUI

### 

​

Chain-of-Thought Planning

The ACE-Step 1.5 model synthesizes metadata, lyrics, and captions via Chain-of-Thought reasoning to guide the diffusion process, resulting in more coherent long-form compositions.

### 

​

Hybrid LM + DiT Architecture

ACE-Step 1.5 combines a Language Model that plans the song structure with a Diffusion Transformer (DiT) that handles audio synthesis, all running natively in ComfyUI.

## 

​

Coming Soon to ComfyUI

These features are available in ACE-Step 1.5 but not yet supported in ComfyUI:

  * **Cover** : Give the model any song as input along with a new prompt and lyrics, and it will reimagine the track in a completely different style
  * **Repaint** : Select a segment, regenerate just that section, and the model stitches it back in while keeping everything else untouched



## 

​

ACE-Step 1.5 ComfyUI Related Resources

  * [Project Page](https://ace-step.github.io/)
  * [Hugging Face](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files)
  * [GitHub](https://github.com/ace-step/ACE-Step)
  * [Blog Post](https://blog.comfy.org/p/ace-step-15-is-now-available-in-comfyui)



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/audio/ace-step/ace-step-v1-5.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/audio/ace-step/ace-step-v1-5)

[ComfyUI ACE-Step Native ExamplePrevious](https://docs.comfy.org/tutorials/audio/ace-step/ace-step-v1)[ComfyUI preprocessor workflowsNext](https://docs.comfy.org/tutorials/utility/preprocessors)

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
