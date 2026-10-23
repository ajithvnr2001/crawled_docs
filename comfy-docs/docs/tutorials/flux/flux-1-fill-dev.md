---
url: https://docs.comfy.org/tutorials/flux/flux-1-fill-dev/
title: ComfyUI Flux.1 fill dev Example - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:19.242742+00:00
---

# ComfyUI Flux.1 fill dev Example - ComfyUI

> Source: https://docs.comfy.org/tutorials/flux/flux-1-fill-dev/

## On this page

  * Introduction to Flux.1 fill dev Model
  * Flux.1 Fill dev and related models installation
  * Flux.1 Fill dev inpainting workflow
    * Flux.1 Inpaint
    * 1\. Inpainting workflow and asset
    * 2\. Steps to run the workflow
  * Flux.1 Fill dev Outpainting Workflow
    * Flux.1 Outpaint
    * 1\. Outpainting workflow and asset
    * 2\. Steps to run the workflow



FLUX

# ComfyUI Flux.1 fill dev Example

Copy pageCopy page

This guide demonstrates how to use Flux.1 fill dev to create Inpainting and Outpainting workflows.

Copy pageCopy page

![Flux.1 fill dev](https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux-fill-dev-demo.jpeg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=e9b567aff5fbd43dce197d819f5f028e)

## 

​

Introduction to Flux.1 fill dev Model

Flux.1 fill dev is one of the core tools in the [FLUX.1 Tools suite](https://blackforestlabs.ai/flux-1-tools/) launched by [Black Forest Labs](https://blackforestlabs.ai/), specifically designed for image inpainting and outpainting. Key features of Flux.1 fill dev:

  * Powerful image inpainting and outpainting capabilities, with results second only to the commercial version FLUX.1 Fill [pro].
  * Excellent prompt understanding and following ability, precisely capturing user intent while maintaining high consistency with the original image.
  * Advanced guided distillation training technology, making the model more efficient while maintaining high-quality output.
  * Friendly licensing terms, with generated outputs usable for personal, scientific, and commercial purposes, please refer to the [FLUX.1 [dev] non-commercial license](https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md) for details.

Open Source Repository: [FLUX.1 [dev]](https://huggingface.co/black-forest-labs/FLUX.1-dev) This guide will demonstrate inpainting and outpainting workflows based on the Flux.1 fill dev model. If you’re not familiar with inpainting and outpainting workflows, you can refer to [ComfyUI Layout Inpainting Example](https://docs.comfy.org/tutorials/basic/inpaint) and [ComfyUI Image Extension Example](https://docs.comfy.org/tutorials/basic/outpaint) for some related explanations.

## 

​

Flux.1 Fill dev and related models installation

Before we begin, let’s complete the installation of the Flux.1 Fill dev model files. The inpainting and outpainting workflows will use exactly the same model files. If you’ve previously used the full version of the [Flux.1 Text-to-Image workflow](https://docs.comfy.org/tutorials/flux/flux-1-text-to-image), then you only need to download the **flux1-fill-dev.safetensors** model file in this section. However, since downloading the corresponding model requires agreeing to the corresponding usage agreement, please visit the [black-forest-labs/FLUX.1-Fill-dev](https://huggingface.co/black-forest-labs/FLUX.1-Fill-dev) page and make sure you have agreed to the corresponding agreement as shown in the image below. ![Flux Agreement](https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux1_fill_dev_agreement.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=388a26b32b5841dbf6ef32f31537e43d) Complete model list: |- [clip_l.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/blob/main/clip_l.safetensors) |- [t5xxl_fp16.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/blob/main/t5xxl_fp16.safetensors) |- [ae.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-schnell/blob/main/ae.safetensors) |- [flux1-fill-dev.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-Fill-dev/blob/main/flux1-fill-dev.safetensors) File storage location:
    
    
    ComfyUI/
    ├── models/
    │   ├── text_encoders/
    │   │    ├── clip_l.safetensors
    │   │    └── t5xxl_fp16.safetensors
    │   ├── vae/
    │   │    └── ae.safetensors
    │   └── diffusion_models/
    │        └── flux1-fill-dev.safetensors
    

## 

​

Flux.1 Fill dev inpainting workflow

### 

​

Flux.1 Inpaint

Fill missing parts of images using Flux.1 Fill Inpainting. ![Flux.1 inpaint workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/flux_fill_inpaint_example-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Flux.1 Inpaint” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## flux_fill_inpaint_example_input_image.png

`LoadImage` node 17 · `flux_fill_inpaint_example_input_image.png`

![flux_fill_inpaint_example_input_image.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/flux_fill_inpaint_example_input_image.png)

**Example output**

![Input image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/flux_fill_inpaint_example_input_image.png)![Flux.1 inpaint example output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/flux_fill_inpaint_example.png)

### 

​

1\. Inpainting workflow and asset

The corresponding image already contains an alpha channel, so you don’t need to draw a mask separately. If you want to draw your own mask, please [click here](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/flux/inpaint/flux_fill_inpaint_input_original.png) to get the image without a mask, and refer to the MaskEditor usage section in the [ComfyUI Layout Inpainting Example](https://docs.comfy.org/tutorials/basic/inpaint#using-the-mask-editor) to learn how to draw a mask in the `Load Image` node.

### 

​

2\. Steps to run the workflow

![ComfyUI Flux.1 Fill dev Inpainting Workflow](https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_inpaint.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=8d4238c0487b7ddf527ec044aa02d578)

  1. Ensure the `Load Diffusion Model` node has `flux1-fill-dev.safetensors` loaded.
  2. Ensure the `DualCLIPLoader` node has the following models loaded: 
     * clip_name1: `t5xxl_fp16.safetensors`
     * clip_name2: `clip_l.safetensors`
  3. Ensure the `Load VAE` node has `ae.safetensors` loaded.
  4. Upload the input image provided in the document to the `Load Image` node; if you’re using the version without a mask, remember to complete the mask drawing using the mask editor
  5. Click the `Queue` button, or use the shortcut `Ctrl(cmd) + Enter` to run the workflow



## 

​

Flux.1 Fill dev Outpainting Workflow

### 

​

Flux.1 Outpaint

Extend images beyond boundaries using Flux.1 outpainting. ![Flux.1 outpaint workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/flux_fill_outpaint_example-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Flux.1 Outpaint” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## flux_fill_outpaint_example_input_image.png

`LoadImage` node 17 · `flux_fill_outpaint_example_input_image.png`

![flux_fill_outpaint_example_input_image.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/flux_fill_outpaint_example_input_image.png)

### 

​

1\. Outpainting workflow and asset

### 

​

2\. Steps to run the workflow

![ComfyUI Flux.1 Fill dev Outpainting Workflow](https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_outpaint.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=5f152f459be5f120b3895636685cb3d3)

  1. Ensure the `Load Diffusion Model` node has `flux1-fill-dev.safetensors` loaded.
  2. Ensure the `DualCLIPLoader` node has the following models loaded: 
     * clip_name1: `t5xxl_fp16.safetensors`
     * clip_name2: `clip_l.safetensors`
  3. Ensure the `Load VAE` node has `ae.safetensors` loaded.
  4. Upload the input image provided in the document to the `Load Image` node
  5. Click the `Queue` button, or use the shortcut `Ctrl(cmd) + Enter` to run the workflow



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/flux/flux-1-fill-dev.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/flux/flux-1-fill-dev)

[ByteDance USO ComfyUI Native Workflow examplePrevious](https://docs.comfy.org/tutorials/flux/flux-1-uso)[ComfyUI Flux.1 ControlNet ExamplesNext](https://docs.comfy.org/tutorials/flux/flux-1-controlnet)

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
