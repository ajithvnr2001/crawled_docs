---
url: https://docs.comfy.org/tutorials/basic/multiple-loras/
title: ComfyUI Multiple LoRAs: Chain Loaders for Blended Styles - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:17.970035+00:00
---

# ComfyUI Multiple LoRAs: Chain Loaders for Blended Styles - ComfyUI

> Source: https://docs.comfy.org/tutorials/basic/multiple-loras/

## On this page

  * Model Installation
  * Multi-LoRA Workflow
  * Complete the Workflow Step by Step
  * Try It Yourself



Basic Examples

# ComfyUI Multiple LoRAs: Chain Loaders for Blended Styles

Copy pageCopy page

Apply two or more LoRA models at once in ComfyUI by chaining Load LoRA nodes, blending styles and characters in a single generation.

Copy pageCopy page

In our [ComfyUI LoRA Example](https://docs.comfy.org/tutorials/basic/lora), we introduced how to load and use a single LoRA model, mentioning the node’s chain connection capability. ![LoRA Node Chaining](https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/chain_link.png?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=905ee3b2883bf67bd986989f57f62caf) This tutorial demonstrates chaining multiple `Load LoRA` nodes to apply two LoRA models simultaneously: [blindbox_V1Mix](https://civitai.com/models/25995?modelVersionId=32988) and [MoXinV1](https://civitai.com/models/12597?modelVersionId=14856). The comparison below shows individual effects of these LoRAs using identical parameters: ![Single LoRA Effects Comparison](https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/compare.png?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=3f26ac1b06c82aa86bf13062a1409131) By chaining multiple LoRA models, we achieve a blended style in the final output: ![Multi-LoRA Application Result](https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/multiple_loras.png?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=f96d5ad3564a7ce69c8acc643eab0776)

## 

​

Model Installation

Download the [dreamshaper_8.safetensors](https://civitai.com/api/download/models/128713?type=Model&format=SafeTensor&size=pruned&fp=fp16) file and put it in your `ComfyUI/models/checkpoints` folder. Download the [blindbox_V1Mix.safetensors](https://civitai.com/api/download/models/32988?type=Model&format=SafeTensor&size=full&fp=fp16) file and put it in your `ComfyUI/models/loras` folder. Download the [MoXinV1.safetensors](https://civitai.com/api/download/models/14856?type=Model&format=SafeTensor&size=full&fp=fp16) file and put it in your `ComfyUI/models/loras` folder.

## 

​

Multi-LoRA Workflow

Download the image below and **drag it into ComfyUI** to load the workflow: ![ComfyUI Workflow - Multiple LoRAs](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/multiple_loras.png)

Images containing workflow JSON in their metadata can be directly dragged into ComfyUI or loaded using the menu `Workflows` -> `Open (ctrl+o)`.

## 

​

Complete the Workflow Step by Step

Follow the steps in the diagram below to ensure the workflow runs correctly. ![Multi-LoRA Workflow Diagram](https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/flow_diagram.png?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=daa5ef546221542dfe0b2ec8b408f689)

  1. Ensure `Load Checkpoint` loads **dreamshaper_8.safetensors**
  2. Ensure first `Load LoRA` loads **blindbox_V1Mix.safetensors**
  3. Ensure second `Load LoRA` loads **MoXinV1.safetensors**
  4. Click `Queue` or press `Ctrl/Cmd + Enter` to generate



## 

​

Try It Yourself

  1. Adjust `strength_model` values in both `Load LoRA` nodes to control each LoRA’s influence
  2. Explore [CivitAI](https://civitai.com/models) for additional LoRAs and create custom combinations



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/basic/multiple-loras.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/basic/multiple-loras)

[ComfyUI LoRA ExamplePrevious](https://docs.comfy.org/tutorials/basic/lora)[ControlNet in ComfyUI: Preprocessors, Models, and WorkflowsNext](https://docs.comfy.org/tutorials/controlnet/controlnet)

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
