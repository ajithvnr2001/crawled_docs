---
url: https://docs.comfy.org/tutorials/audio/stable-audio/stable-audio-3/
title: Stable Audio 3 ComfyUI workflow example - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:17.105621+00:00
---

# Stable Audio 3 ComfyUI workflow example - ComfyUI

> Source: https://docs.comfy.org/tutorials/audio/stable-audio/stable-audio-3/

## On this page

  * Available workflows
    * Stable Audio 3.0 Medium
    * Stable Audio 3.0 Medium Base
  * Model download
    * Checkpoints
    * Text encoders



Stable Audio

# Stable Audio 3 ComfyUI workflow example

Copy pageCopy page

Run Stability AI’s open-source Stable Audio 3 in ComfyUI for text-to-audio generation, with Qwen prompt expansion and category-aware reprompting.

Copy pageCopy page

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

**Stable Audio 3** ([GitHub](https://github.com/Stability-AI/stable-audio-3)) is Stability AI’s latest open-source audio generation model, trained on fully licensed music data and licensed for commercial use. It uses a dedicated subgraph node to produce high-quality stereo audio (including music, sound effects, and instruments) from text descriptions, with optional Qwen-powered category-aware reprompting. Stable Audio 3 comes in three variants:

  * **Small-SFX** : Sound effects and short ambiance, up to 2:00. Small enough to run on CPU.
  * **Small-Music** : Short music loops, on-device-friendly, up to 2:00.
  * **Medium** : Longer tracks with stronger structure and musicality, up to ~6:20. Requires a GPU.

**Related links** :

  * [GitHub: Stability-AI/stable-audio-3](https://github.com/Stability-AI/stable-audio-3)
  * [Hugging Face (Comfy-Org/stable-audio-3)](https://huggingface.co/Comfy-Org/stable-audio-3)
  * [Blog: Announcement](https://blog.comfy.org/p/stable-audio-3-day-0-support)



## 

​

Available workflows

### 

​

Stable Audio 3.0 Medium

Input a short text idea, optional duration, seed, and category. Generate stereo audio (music, SFX, or instruments) using Stable Audio 3 with optional AI-driven text expansion. ![Stable Audio 3 Medium workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/audio_stable_audio_3_medium-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Stable Audio 3.0 Medium” in Template Library

The **Stable Audio 3 Medium** workflow is a full-featured text-to-audio generation pipeline. You provide a short text idea, optional duration, seed, and category. The workflow expands your prompt using Qwen with a **category-aware reprompt template** , then generates stereo audio via the Stable Audio 3 checkpoint. **How to use** :

  1. **Text idea** : Enter a short description of the sound, music, or effect you want (e.g. “upbeat electronic dance track with heavy bass”)
  2. **Duration** : Set the desired clip length in seconds (default varies)
  3. **Seed** : Control reproducibility by adjusting the seed value
  4. **Category** : Choose a reprompt preset: **Music** , **Instrument** , **SFX** , or **One-shot**
  5. **Enable reprompt** : Toggle `use_reprompt` on to let Qwen expand your short idea into a detailed prompt before generation
  6. Click **Run** (`Ctrl/Cmd + Enter`) to generate. The audio will be saved to `ComfyUI/output/audio/`



### 

​

Stable Audio 3.0 Medium Base

Input a short text description of a sound, music, or effect. The workflow expands your prompt with Qwen and generates a stereo audio clip from Stable Audio 3. ![Stable Audio 3 Medium Base workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/audio_stable_audio_3_medium_base-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Stable Audio 3.0 Medium Base” in Template Library

A simplified version of Stable Audio 3 without Qwen reprompt expansion. It expects a complete text prompt and passes it directly to the model. Use this when you already have a detailed prompt and want faster generation. **How to use** :

  1. **Text prompt** : Enter a detailed description of the audio you want
  2. **Duration** : Set the clip length in seconds
  3. **Seed** : Control reproducibility
  4. Click **Run** (`Ctrl/Cmd + Enter`) to generate



## 

​

Model download

When loading the workflow, ComfyUI will prompt you with download links for any missing models. To set up manually, download the files below and place them in the correct folders.

### 

​

Checkpoints

## stable_audio_3_medium.safetensors

For the Medium workflow. Place in models/checkpoints/

## stable_audio_3_medium_base.safetensors

For the Medium Base workflow. Place in models/checkpoints/

Place checkpoints in:
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   └── 📂 checkpoints/
    │       ├── stable_audio_3_medium.safetensors
    │       └── stable_audio_3_medium_base.safetensors
    

### 

​

Text encoders

## t5gemma_b_b_ul2.safetensors

Required for all Stable Audio 3 workflows. Place in models/text_encoders/

## qwen3.5_2b_bf16.safetensors

Required for the Medium workflow (Qwen reprompt). Place in models/text_encoders/

Place text encoders in:
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   └── 📂 text_encoders/
    │       ├── t5gemma_b_b_ul2.safetensors
    │       └── qwen3.5_2b_bf16.safetensors
    

After placing the files, press **R** in ComfyUI to refresh nodes and load the latest models.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/audio/stable-audio/stable-audio-3.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/audio/stable-audio/stable-audio-3)

[Stable Audio 1.0 ComfyUI workflow examplePrevious](https://docs.comfy.org/tutorials/audio/stable-audio/stable-audio-1)[ComfyUI ACE-Step Native ExampleNext](https://docs.comfy.org/tutorials/audio/ace-step/ace-step-v1)

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
