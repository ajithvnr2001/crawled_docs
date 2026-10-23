---
url: https://docs.comfy.org/tutorials/partner-nodes/openai/gpt-image-2/
title: OpenAI GPT-Image-2 in ComfyUI: Reasoning Image Generation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-19T14:35:07.092402+00:00
---

# OpenAI GPT-Image-2 in ComfyUI: Reasoning Image Generation - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/openai/gpt-image-2/

## On this page

  * What GPT-Image-2 is good at
    * Reasoning-driven generation
    * Image editing that preserves what matters
    * Up to eight consistent images per prompt
  * Hybrid Pipelines
  * Example outputs
  * Getting Started
  * Available workflows
    * Text to image (T2I)
    * Image edit



OpenAI

# OpenAI GPT-Image-2 in ComfyUI: Reasoning Image Generation

Copy pageCopy page

Use OpenAI GPT-Image-2 in ComfyUI for reasoning-driven image generation: dense text and UI rendering, 2K image editing, and up to eight consistent images.

Copy pageCopy page

OpenAI GPT-Image-2 (`gpt-image-2`) is OpenAI’s newest image model, available in ComfyUI through Partner Nodes. It is the first OpenAI image model that _reasons_ before it generates: instead of one-shot sampling, the model plans the composition, checks its work, and iterates. This node supports:

  * Text-to-image generation with strong handling of dense text, UI elements, iconography, infographics, maps, slides, and manga panels
  * Image editing with high structural fidelity at up to 2K resolution
  * Up to 8 consistent images from a single prompt, preserving character and object continuity

GPT-Image-2 is selected as a `model` option on the **OpenAI GPT Image 2.5** node in the Node Library. The node calls OpenAI’s image generation API synchronously and returns images that match the description.

## 

​

What GPT-Image-2 is good at

### 

​

Reasoning-driven generation

GPT-Image-2 plans the composition before rendering. This makes it well suited for prompts that have historically broken image models: for example, a poster with a seven-item bulleted list in 11pt Helvetica, centered: and produces clean output for dense text, small UI elements, iconography, infographics, maps, and slides.

### 

​

Image editing that preserves what matters

GPT-Image-2 handles targeted edits with structural fidelity, keeping everything outside the edit zone pixel-stable while applying the requested change cleanly at up to 2K resolution. Use it for tasks like colorizing black-and-white photos or shifting a scene from noon to dusk without warping faces, geometry, or fine detail.

### 

​

Up to eight consistent images per prompt

The model can return up to **eight distinct images from a single prompt** while preserving character and object continuity across the series. This is useful for storyboarding, reference sheets, character turnarounds, and product variants without seed-locking or prompt gymnastics. Feed the batch straight into a `Save Image` node or chain it into a video workflow downstream. ![GPT-Image-2 consistent images example](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/openai/gpt_image_2/consistent_example.jpg)

## 

​

Hybrid Pipelines

GPT-Image-2 slots naturally into hybrid pipelines: use it for the text-heavy hero frame, then hand off to your local models for upscaling, stylization, or video generation: the best model for each step, in one graph.

## 

​

Example outputs

Text-to-image generation with reasoning-driven composition: ![GPT-Image-2 Text-to-Image example](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/openai/gpt_image_2/gpt_image_2_t2i_1.jpg) Image editing on an input image, preserving structure outside the edit zone: ![GPT-Image-2 Image-to-Image example](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/openai/gpt_image_2/gpt_image_2_i2i_1.jpg) ![GPT-Image-2 Image Edit example 1](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/openai/gpt_image_2/gpt_image_2_image_edit_1.jpg)

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

Getting Started

  1. Update ComfyUI to the latest version (v0.19.4 or later), or use [Comfy Cloud](https://links.comfy.org/4u4o7Pv).
  2. In the Node Library, search for **OpenAI GPT Image 2.5** and add the node.
  3. Set the `model` field to `gpt-image-2`.



## 

​

Available workflows

### 

​

Text to image (T2I)

Generate an image from a text prompt with GPT-Image-2’s reasoning-driven composition.

## Run Text-to-Image on Cloud

Try the Text-to-Image workflow instantly on Comfy Cloud.

## Download Text-to-Image workflow

Download the workflow JSON.

![GPT-Image-2 Text-to-Image workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openai_gpt_image_2_t2i-1.webp) ![GPT-Image-2 Text-to-Image example](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/openai/gpt_image_2/gpt_image_2_t2i_1.jpg)

### 

​

Image edit

Edit an input image with high structural fidelity at up to 2K resolution.

## Run Image Edit on Cloud

Try the Image Edit workflow instantly on Comfy Cloud.

## Download Image Edit workflow

Download the workflow JSON.

![GPT-Image-2 Image Edit workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openai_gpt_image_2_image_edit-1.webp)

## Download Sample Input Image

Get the example input image for this workflow

![GPT-Image-2 Image-to-Image example](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/openai/gpt_image_2/gpt_image_2_i2i_1.jpg) ![GPT-Image-2 Image Edit example 1](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/openai/gpt_image_2/gpt_image_2_image_edit_1.jpg) ![GPT-Image-2 Image Edit example 2](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/openai/gpt_image_2/gpt_image_2_image_edit_2.jpg)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/openai/gpt-image-2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/openai/gpt-image-2)

[OpenAI GPT Image 2.5 Node: Flare and Sunburst WorkflowsPrevious](https://docs.comfy.org/tutorials/partner-nodes/openai/gpt-image-2-5)[OpenAI GPT-Image-1 in ComfyUI: Text-to-Image and InpaintingNext](https://docs.comfy.org/tutorials/partner-nodes/openai/gpt-image-1)

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
