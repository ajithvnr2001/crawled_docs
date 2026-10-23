---
url: https://docs.comfy.org/tutorials/llm/gemma4/gemma4/
title: Gemma 4 ComfyUI workflow example - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:25.203478+00:00
---

# Gemma 4 ComfyUI workflow example - ComfyUI

> Source: https://docs.comfy.org/tutorials/llm/gemma4/gemma4/

## On this page

  * Available workflow
    * Gemma4: Text Generation
  * Model Download



LLM

# Gemma 4 ComfyUI workflow example

Copy pageCopy page

Run Google’s lightweight open Gemma 4 LLM in ComfyUI for text generation, image understanding, video analysis, and audio transcription with up to 256K context.

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

**Gemma 4** is the latest generation of lightweight open LLMs from Google DeepMind, built for text generation, image understanding, video analysis, audio transcription, and structured tool use. It is natively supported in ComfyUI as the default **Text Generation** model. **Model highlights** :

  * **Multimodal by design** : accepts text, image, video, and audio inputs simultaneously
  * **Three sizes available** : 
    * **E2B (2B)** : Fast and lightweight, ideal for consumer GPUs
    * **E4B (4B)** : Balanced performance, recommended default
    * **12B** : Best quality, requires higher VRAM
  * **Thinking mode** : Built-in step-by-step reasoning before generating answers
  * **Long context** : Up to 128K tokens (E2B/E4B) and 256K tokens (12B)
  * **Multilingual** : 35+ languages out of the box, pre-trained on 140+
  * **Function calling** : Native support for structured tool use and agentic workflows
  * **ComfyUI native** : loaded and run through the built-in `TextGenerate` and `CLIPLoader` nodes

**Related links** :

  * [Hugging Face (Comfy-Org/gemma-4)](https://huggingface.co/Comfy-Org/gemma-4)
  * [Google AI for Developers](https://ai.google.dev/gemma)
  * [ComfyUI Source Code (nodes_textgen.py)](https://github.com/Comfy-Org/ComfyUI/blob/master/comfy_extras/nodes_textgen.py)



## 

​

Available workflow

### 

​

Gemma4: Text Generation

Input your text prompt and optionally an image, audio, or video. Generate text output with configurable reasoning, coding, and multilingual support. ![Gemma 4 text generation workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/llm_gemma4_text_gen-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Gemma4: Text Generation” in Template Library

**Input materials** Upload these optional files to the matching nodes:

## the_lily_veil.png

`LoadImage` node 2 · `the_lily_veil.png`

## long_demo.mp3

`LoadAudio` node 5 · `long_demo.mp3`

## video_wan_vace_inpainting_input_video.mp4

`LoadVideo` node 6 · not used in this workflow’s generation · `video_wan_vace_inpainting_input_video.mp4`

This workflow demonstrates the core **text generation** capabilities of Gemma 4. It accepts an optional image, audio file, or video as additional context alongside your text prompt, and generates natural language output, with support for reasoning, coding, and multilingual prompts. **Inputs** :

  * **Text prompt** : your question or instruction
  * **Image** (optional): for visual understanding tasks (OCR, object detection, chart reading, etc.)
  * **Audio** (optional): for speech recognition or transcription
  * **Video** (optional): the template loads the video and splits it with **Get Video Components** , but those frames are not connected to the text generator, so the video does not affect the output

**Key controls** :

  * **Max length** : maximum number of tokens to generate (default 256)
  * **Sampling mode** : toggle sampling on/off and adjust temperature, top-k, top-p, repetition penalty, and seed
  * **Thinking mode** : enable step-by-step reasoning before the final answer
  * **Use default template** : apply the built-in system prompt for the model

**Output** :

  * **Generated text** : the model’s response as a plain text string



## Learn about Subgraph

This workflow uses Subgraph nodes for modular processing. Check out the Subgraph documentation to learn how to customize and extend the workflow.

## 

​

Model Download

Gemma 4 models are loaded as text encoders in ComfyUI. Download the relevant model file and place it in the correct directory:

## Gemma 4 2B (E2B IT FP8)

Fast, lightweight. Recommended for consumer GPUs.

## Gemma 4 4B (E4B IT FP8)

Balanced performance. The default model in the workflow.

## View All Variants

Browse all Gemma 4 model weights.

Place the downloaded `.safetensors` file in:
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   └── 📂 text_encoders/
    │       └── gemma4_e4b_it_fp8_scaled.safetensors
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/llm/gemma4/gemma4.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/llm/gemma4/gemma4)

[ComfyUI Hunyuan3D-2 ExamplesPrevious](https://docs.comfy.org/tutorials/3d/hunyuan3D-2)[Qwen 3.0 ComfyUI workflow exampleNext](https://docs.comfy.org/tutorials/llm/qwen/qwen3)

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
