---
url: https://docs.comfy.org/tutorials/audio/stable-audio/stable-audio-1/
title: Stable Audio 1.0 ComfyUI workflow example - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:16.978946+00:00
---

# Stable Audio 1.0 ComfyUI workflow example - ComfyUI

> Source: https://docs.comfy.org/tutorials/audio/stable-audio/stable-audio-1/

## On this page

  * Workflow
    * Stable Audio 1.0: Text to Audio
  * Model download
    * Checkpoint
    * Text encoder



Stable Audio

# Stable Audio 1.0 ComfyUI workflow example

Copy pageCopy page

Guide to using Stability AI’s open-source Stable Audio 1.0 model in ComfyUI for text-to-audio generation.

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

**Stable Audio 1.0** is Stability AI’s first open-source audio generation model. It takes a text prompt and generates an audio clip. In ComfyUI, it works like a standard text-to-audio pipeline: CLIP encodes the prompt, a KSampler denoises the latent, and the VAE decodes it to audio. **Related links** :

  * [Hugging Face (stabilityai/stable-audio-open-1.0)](https://huggingface.co/stabilityai/stable-audio-open-1.0)



## 

​

Workflow

### 

​

Stable Audio 1.0: Text to Audio

Generate audio from text prompts using Stable Audio. ![Stable Audio 1.0 text to audio workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/audio_stable_audio_example-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Stable Audio 1.0: Text to Audio” in Template Library

The workflow uses **standard ComfyUI nodes** : no custom nodes required. It loads the Stable Audio 1.0 checkpoint, encodes your prompt via a CLIP text encoder (t5-base), denoises the latent audio with a KSampler, and decodes it to audio through the model’s VAE. **How to use** :

  1. **Load the checkpoint** : The `CheckpointLoaderSimple` node uses `stable-audio-open-1.0.safetensors`
  2. **Write a prompt** : Enter your description in the `CLIPTextEncode` node (e.g. “heaven church electronic dance music”)
  3. **Set duration** : Adjust the `EmptyLatentAudio` node’s length value (default 47.6 seconds)
  4. Click **Run** (`Ctrl/Cmd + Enter`) to generate. The audio will be saved to `ComfyUI/output/audio/`



## 

​

Model download

When loading the workflow, ComfyUI will prompt you with download links for any missing models. To set up manually, download the files below and place them in the correct folders.

### 

​

Checkpoint

## stable-audio-open-1.0.safetensors

2.3GB. Place in models/checkpoints/

Place the checkpoint in:
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   └── 📂 checkpoints/
    │       └── stable-audio-open-1.0.safetensors
    

### 

​

Text encoder

## t5-base.safetensors

Text encoder for prompt conditioning. Place in models/text_encoders/

Place the text encoder in:
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   └── 📂 text_encoders/
    │       └── t5-base.safetensors
    

After placing the files, press **R** in ComfyUI to refresh nodes and load the latest models.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/audio/stable-audio/stable-audio-1.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/audio/stable-audio/stable-audio-1)

[MiniMax Music 3 in ComfyUI: AI Music GenerationPrevious](https://docs.comfy.org/tutorials/audio/minimax/minimax-music-3)[Stable Audio 3 ComfyUI workflow exampleNext](https://docs.comfy.org/tutorials/audio/stable-audio/stable-audio-3)

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
