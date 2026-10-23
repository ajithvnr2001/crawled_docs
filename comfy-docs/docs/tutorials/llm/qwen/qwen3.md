---
url: https://docs.comfy.org/tutorials/llm/qwen/qwen3/
title: Qwen 3.0 ComfyUI workflow example - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:24.800991+00:00
---

# Qwen 3.0 ComfyUI workflow example - ComfyUI

> Source: https://docs.comfy.org/tutorials/llm/qwen/qwen3/

## On this page

  * Use Cases
  * Available workflow
    * Qwen3.0: Text Generation
  * Model Download



LLM

# Qwen 3.0 ComfyUI workflow example

Copy pageCopy page

Qwen 3.0 is Alibaba Cloud’s open-source LLM with strong reasoning capabilities, available in 4B for text generation and structured reasoning tasks.

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

**Qwen 3.0** (also known as Qwen3) is a powerful open-source LLM from Alibaba Cloud built for text generation, reasoning, and structured analysis. It is natively supported in ComfyUI through the built-in `TextGenerate` node. **Model highlights** :

  * **Strong reasoning** : Qwen3-4B-Thinking supports step-by-step chain-of-thought reasoning
  * **Text generation focused** : optimized for structured text output, analysis, and coding tasks
  * **ComfyUI native** : works with the built-in `TextGenerate` node, no custom nodes needed
  * **Lightweight** : shares the same text encoder format as Qwen3.5, available in 2B, 4B, and 9B variants to fit different hardware



## 

​

Use Cases

Qwen 3.0 is well-suited for tasks that require structured text generation and intelligent reasoning within a ComfyUI workflow:

  * **Prompt optimization** : feed existing prompts to Qwen 3.0 and ask it to rewrite, expand, or refine them for better image generation results. For example, convert a short keyword prompt into detailed, structured descriptions with style, lighting, and composition details.
  * **Workflow logic reasoning** : use the model to analyze workflow parameters, suggest processing steps, or generate structured instructions that feed into other nodes.
  * **Text-based analysis** : extract information, classify content, or generate structured reports from text inputs.
  * **Chain-of-thought reasoning** : enable thinking mode for complex multi-step tasks that benefit from intermediate reasoning before producing the final output.



## 

​

Available workflow

### 

​

Qwen3.0: Text Generation

Input a text prompt to generate detailed, reasoned responses using the Qwen3-4B-Thinking model. ![Qwen 3.0 text generation workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/llm_qwen3_text_gen-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Qwen3.0: Text Generation” in Template Library

This workflow demonstrates the core **text generation** capabilities of Qwen 3.0. It accepts a text prompt and generates detailed, structured responses using the model’s built-in reasoning capabilities. **Inputs** :

  * **Text prompt** : your question, instruction, or task description

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

Qwen 3.0 models are loaded as text encoders in ComfyUI. The model files are shared with Qwen3.5. Download the variant that best fits your hardware:

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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/llm/qwen/qwen3.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/llm/qwen/qwen3)

[Gemma 4 ComfyUI workflow examplePrevious](https://docs.comfy.org/tutorials/llm/gemma4/gemma4)[Qwen3.5 ComfyUI workflow exampleNext](https://docs.comfy.org/tutorials/llm/qwen/qwen3_5)

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
