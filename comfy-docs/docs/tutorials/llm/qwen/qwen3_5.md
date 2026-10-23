---
url: https://docs.comfy.org/tutorials/llm/qwen/qwen3_5/
title: Qwen3.5 ComfyUI workflow example - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:24.607300+00:00
---

# Qwen3.5 ComfyUI workflow example - ComfyUI

> Source: https://docs.comfy.org/tutorials/llm/qwen/qwen3_5/

## On this page

  * Use Cases
  * Available workflow
    * Qwen3.5: Text Generation
  * Model Download



LLM

# Qwen3.5 ComfyUI workflow example

Copy pageCopy page

Run Qwen3.5, Alibaba Cloud’s 4B multimodal LLM, in ComfyUI for image captioning, reverse prompt engineering, and visual question answering.

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

**Qwen3.5** is an open-source multimodal LLM from Alibaba Cloud, building on the Qwen 3.0 series with added image understanding capabilities. It supports both text generation and image-based tasks such as image captioning and reverse prompt engineering. **Model highlights** :

  * **Multimodal** : accepts text and image inputs for visual understanding tasks
  * **Image captioning** : can describe images and generate detailed captions
  * **Reverse prompt engineering** : extract prompts and generation parameters from reference images
  * **ComfyUI native** : works with the built-in `TextGenerate` node, no custom nodes needed
  * **Lightweight** : 4B parameter model, suitable for consumer GPUs



## 

​

Use Cases

Qwen3.5 excels in scenarios where combining visual understanding with text generation adds value to a ComfyUI workflow:

  * **Image reverse prompt engineering** : feed a reference image to Qwen3.5 and ask it to generate a detailed text prompt that could reproduce the image. This is especially useful when you encounter a great image but don’t know how it was prompted.
  * **Prompt optimization** : load an existing prompt and an image concept, then ask Qwen3.5 to generate, refine, or expand prompts with richer detail for better generation results.
  * **Image captioning** : automatically generate captions, descriptions, or metadata tags for generated images, useful for cataloging or training data preparation.
  * **Visual question answering** : ask questions about image content (“What objects are in this scene?”, “What color is the background?”) and get structured text answers.
  * **Text reading** : with a suitable prompt, the model may attempt to read visible text or labels in images, though reliability depends on the quality and clarity of the rendered text.



## 

​

Available workflow

### 

​

Qwen3.5: Text Generation

Use the Qwen3.5 model to analyze an input image and generate descriptive text prompts. This workflow performs image captioning and reverse prompt engineering. ![Qwen3.5 text generation workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/llm_qwen3_5_text_gen-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Qwen3.5: Text Generation” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## man_with_red_hat.png

`LoadImage` node 2 · `man_with_red_hat.png`

![Input image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/man_with_red_hat.png)

This workflow demonstrates the **text generation and image understanding** capabilities of Qwen3.5. It accepts a text prompt and an optional image, and generates descriptive text or structured analysis based on the input. **Inputs** :

  * **Text prompt** : your question, instruction, or task description
  * **Image** (optional): for visual understanding tasks (image captioning, reverse prompt engineering, prompt optimization, etc.)

**Key controls** :

  * **Max length** : maximum number of tokens to generate (default 256)
  * **Sampling mode** : toggle sampling on/off and adjust temperature, top-k, top-p, repetition penalty, and seed
  * **Use default template** : apply the built-in system prompt for the model

**Output** :

  * **Generated text** : the model’s response as a plain text string



## Learn about Subgraph

This workflow uses Subgraph nodes for modular processing. Check out the Subgraph documentation to learn how to customize and extend the workflow.

## 

​

Model Download

Qwen3.5 models are loaded as text encoders in ComfyUI. Choose the variant that best suits your hardware:

## Qwen3.5 2B (bf16)

Lightweight, ~4.5 GB. Best for low VRAM setups and fast downloads.

## Qwen3.5 4B (bf16)

Balanced size and quality. Recommended for most consumer GPUs.

## Qwen3.5 9B (bf16)

Largest variant, ~19 GB. Higher quality output, requires more VRAM.

Place the downloaded `.safetensors` file in:
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   └── 📂 text_encoders/
    │       └── qwen3.5_4b_bf16.safetensors   # or 2b / 9b variant
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/llm/qwen/qwen3_5.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/llm/qwen/qwen3_5)

[Qwen 3.0 ComfyUI workflow examplePrevious](https://docs.comfy.org/tutorials/llm/qwen/qwen3)[ComfyUI MiniMax H3 Video Generation GuideNext](https://docs.comfy.org/tutorials/video/minimax/minimax-h3)

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
