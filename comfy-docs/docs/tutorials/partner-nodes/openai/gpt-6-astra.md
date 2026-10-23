---
url: https://docs.comfy.org/tutorials/partner-nodes/openai/gpt-6-astra/
title: GPT-6 Astra in ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:35.366057+00:00
---

# GPT-6 Astra in ComfyUI - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/openai/gpt-6-astra/

## On this page

  * When to pick GPT-6 Astra
  * Using the model in the OpenAI Chat node
  * Reasoning effort
  * GPT-6 Astra template



OpenAI

# GPT-6 Astra in ComfyUI

Copy pageCopy page

Use OpenAI GPT-6 Astra through the OpenAI Chat node for complex reasoning, image analysis, prompt generation, and LLM-driven workflows in ComfyUI

Copy pageCopy page

**GPT-6 Astra** is OpenAI’s most capable model, built for the hardest end-to-end work: complex reasoning, coding, computer use, research, and document creation. Released on September 3, 2026, it supports a 1,050,000-token context window, text and image input, and reasoning effort levels from `low` through `max`. In ComfyUI, GPT-6 Astra runs through the `OpenAI Chat` node: select `gpt-6-astra` in the node’s `model` dropdown. This page focuses on how to use the model inside ComfyUI workflows. For node basics shared by all models, see the [OpenAI Chat tutorial](https://docs.comfy.org/tutorials/partner-nodes/openai/chat).

To use the Partner Nodes, you need to ensure that you are logged in properly and using a permitted network environment. Please refer to the [Partner Nodes Overview](https://docs.comfy.org/tutorials/partner-nodes/overview) section of the documentation to understand the specific requirements for using the Partner Nodes.

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

When to pick GPT-6 Astra

The `OpenAI Chat` node offers many models, from `gpt-5-nano` to `gpt-6-astra`. GPT-6 Astra is the strongest but also the most expensive option, so it fits tasks where cheaper models struggle:

  * **Long-context image analysis** : feeding many images (via `Batch Images`) or large prompt files and asking for a structured analysis in one pass
  * **Prompt engineering** : turning a reference image or a rough idea into a detailed, comma-separated positive prompt for image or video models
  * **Agentic workflows** : multi-step tasks like analyzing a dataset description, then writing a generation plan, then drafting the prompts themselves
  * **Complex instruction following** : precise output formats (JSON, YAML, fixed section order) that smaller models tend to break

For simple captioning or short answers, `gpt-5` or `gpt-5-mini` produce good results at a fraction of the cost. See the [pricing table](https://docs.comfy.org/tutorials/partner-nodes/pricing) for the per-model rates.

## 

​

Using the model in the OpenAI Chat node

The `OpenAI Chat` node takes:

  * `prompt`: the instruction. For prompt-generation tasks, describe exactly what to extract from the image and the output format you want
  * `images`: optional image context. Connect a `LoadImage`, or `Batch Images` for multiple images; every connected image is sent to the model
  * `files`: optional documents from the `OpenAI Chat Input Files` node
  * `advanced_options`: optional configuration from the `OpenAI Chat Advanced Options` node

The output is a `String`. Typical ways to use it downstream:

  * Into a `Preview Any` node to read the response
  * Into `Save Text` to write the generated prompt to a `.txt` file
  * Into the positive prompt input of a `CLIP Text Encode` node, creating fully automatic image or video generation pipelines where the LLM writes the prompt
  * Into text inputs of partner nodes, for example to draft a scene description before video generation



## 

​

Reasoning effort

GPT-6 Astra is a reasoning model. Connect an `OpenAI Chat Advanced Options` node and set `reasoning_effort` to control the trade-off between response quality and cost:

Level| Behavior  
---|---  
`default`| The model chooses automatically  
`low`| Fastest and cheapest, good for straightforward analysis  
`medium`| Balanced default for prompt generation  
`high`| Thorough analysis of complex images or instructions  
`xhigh`| Deep multi-step reasoning  
`max`| Maximum reasoning for the hardest tasks  
  
The same node also exposes `max_output_tokens` (16 to 16384, including reasoning tokens) and an `instructions` field that acts as a persistent system prompt, useful for fixing an output format across many runs.

## 

​

GPT-6 Astra template

A separate template shows GPT-6 Astra analyzing an image and generating a structured AI art prompt from it. The workflow loads an image, sends an analysis prompt to the `OpenAI Chat` node with `model` set to `gpt-6-astra`, and writes the result to a text file through `Save Text`. ![GPT-6 Astra workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openai_gpt6_astra-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “GPT-6 Astra” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## blue_poppies_field.png

`LoadImage` node · `blue_poppies_field.png`

Steps:

  1. Load your image in the `LoadImage` node
  2. In the `OpenAI Chat` node, adjust the analysis prompt or switch `model` as needed. The template’s prompt asks the model to extract subject, composition, camera, lighting, color palette, texture, and style, then output a comma-separated positive prompt only
  3. Click `Run`. The generated prompt appears in the preview and is saved to a `.txt` file by the `Save Text` node

To go further, copy the saved prompt into a `CLIP Text Encode` node or an image / video model node and generate directly from the model’s output. GPT-6 Astra bills from API token usage, at a higher rate than other OpenAI Chat models. See the [pricing table](https://docs.comfy.org/tutorials/partner-nodes/pricing) for details.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/openai/gpt-6-astra.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/openai/gpt-6-astra)

[OpenAI Chat in ComfyUI: Conversations and Image UnderstandingPrevious](https://docs.comfy.org/tutorials/partner-nodes/openai/chat)[OpenRouter LLM in ComfyUI: Many Models in One NodeNext](https://docs.comfy.org/tutorials/partner-nodes/openrouter/llm)

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
