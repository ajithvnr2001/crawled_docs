---
url: https://docs.comfy.org/tutorials/flux/flux-1-kontext-dev/
title: ComfyUI FLUX Kontext Dev Native Workflow Example - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:19.621882+00:00
---

# ComfyUI FLUX Kontext Dev Native Workflow Example - ComfyUI

> Source: https://docs.comfy.org/tutorials/flux/flux-1-kontext-dev/

## On this page

  * About FLUX.1 Kontext Dev
    * Version Information
  * Model Download
  * FLUX.1 Kontext Dev Workflow
    * FLUX Kontext Dev Image Edit
    * 1\. Workflow and Input Image Download
    * 2\. Complete the workflow step by step
  * FLUX Kontext Prompt Techniques
    * 1\. Basic Modifications
    * 2\. Style Transfer
    * 3\. Character Consistency
    * 4\. Text Editing
  * Common Problem Solutions
    * Character Changes Too Much
    * Composition Position Changes
    * Style Application Inaccuracy
  * Core Principles
  * Best Practice Templates



FLUX

# ComfyUI FLUX Kontext Dev Native Workflow Example

Copy pageCopy page

FLUX.1 Kontext Dev workflow for ComfyUI: edit images with text and image input using Black Forest Labs’ open-source 12B multimodal editing model.

Copy pageCopy page

## 

​

About FLUX.1 Kontext Dev

FLUX.1 Kontext is a breakthrough multimodal image editing model from Black Forest Labs that supports simultaneous text and image input, intelligently understanding image context and performing precise editing. Its development version is an open-source diffusion transformer model with 12 billion parameters, featuring excellent context understanding and character consistency maintenance, ensuring that key elements such as character features and composition layout remain stable even after multiple iterative edits. It shares the same core capabilities as the FLUX.1 Kontext suite:

  * Character Consistency: Preserves unique elements in images across multiple scenes and environments, such as reference characters or objects in the image.
  * Editing: Makes targeted modifications to specific elements in the image without affecting other parts.
  * Style Reference: Generates novel scenes while preserving the unique style of the reference image according to text prompts.
  * Interactive Speed: Minimal latency in image generation and editing.

While the previously released API version offers the highest fidelity and speed, FLUX.1 Kontext [Dev] runs entirely on local machines, providing unparalleled flexibility for developers, researchers, and advanced users who wish to experiment.

### 

​

Version Information

  * **[FLUX.1 Kontext [pro]** : Commercial version, focused on rapid iterative editing
  * **FLUX.1 Kontext [max]** : Experimental version with stronger prompt adherence
  * **FLUX.1 Kontext [dev]** : Open source version (used in this tutorial), 12B parameters, mainly for research

Currently in ComfyUI, you can use all these versions, where [Pro and Max versions](https://docs.comfy.org/tutorials/partner-nodes/black-forest-labs/flux-1-kontext) can be called through Partner Nodes, while the Dev open source version please refer to the instructions in this guide.

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

Model Download

To run the workflows in this guide successfully, you first need to download the following model files. You can also directly get the model download links from the corresponding workflows, which already contain the model file download information. **Diffusion Model**

  * [flux1-dev-kontext_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/flux1-kontext-dev_ComfyUI/blob/main/split_files/diffusion_models/flux1-dev-kontext_fp8_scaled.safetensors)



If you want to use the original weights, you can visit Black Forest Labs’ related repository to obtain and use the original model weights.

**VAE**

  * [ae.safetensors](https://huggingface.co/Comfy-Org/Lumina_Image_2.0_Repackaged/blob/main/split_files/vae/ae.safetensors)

**Text Encoder**

  * [clip_l.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/blob/main/clip_l.safetensors)
  * [t5xxl_fp16.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/blob/main/t5xxl_fp16.safetensors) or [t5xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/blob/main/t5xxl_fp8_e4m3fn_scaled.safetensors)

Model save location
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   └── flux1-dev-kontext_fp8_scaled.safetensors
    │   ├── 📂 vae/
    │   │   └── ae.safetensor
    │   └── 📂 text_encoders/
    │       ├── clip_l.safetensors
    │       └── t5xxl_fp16.safetensors or t5xxl_fp8_e4m3fn_scaled.safetensors
    

## 

​

FLUX.1 Kontext Dev Workflow

### 

​

FLUX Kontext Dev Image Edit

Smart image editing that keeps characters consistent, edits specific parts without affecting others, and preserves original styles. ![FLUX Kontext Dev workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/flux_kontext_dev_basic-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “FLUX Kontext Dev” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## flux_kontext_dev_basic_input_image.jpg

`LoadImage` node 190 · `flux_kontext_dev_basic_input_image.jpg`

![flux_kontext_dev_basic_input_image.jpg](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/flux_kontext_dev_basic_input_image.jpg)

**Example output**

![Input image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/flux_kontext_dev_basic_input_image.jpg)![FLUX Kontext Dev example output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/flux_kontext_dev_basic.png)

This workflow uses the `Load Image(from output)` node to load the image to be edited, making it more convenient for you to access the edited image for multiple rounds of editing.

### 

​

1\. Workflow and Input Image Download

### 

​

2\. Complete the workflow step by step

![Workflow Step Guide](https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_1_kontext_dev_basic_step_guide.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=90995e36fa39a53693aeff3b560c60ef) You can refer to the numbers in the image to complete the workflow run:

  1. In the `Load Diffusion Model` node, load the `flux1-dev-kontext_fp8_scaled.safetensors` model
  2. In the `DualCLIP Load` node, ensure that `clip_l.safetensors` and `t5xxl_fp16.safetensors` or `t5xxl_fp8_e4m3fn_scaled.safetensors` are loaded
  3. In the `Load VAE` node, ensure that `ae.safetensors` model is loaded
  4. In the `Load Image(from output)` node, load the provided input image
  5. In the `CLIP Text Encode` node, modify the prompts, only English is supported
  6. Click the `Queue` button, or use the shortcut `Ctrl(cmd) + Enter` to run the workflow



## 

​

FLUX Kontext Prompt Techniques

### 

​

1\. Basic Modifications

  * Simple and direct: `"Change the car color to red"`
  * Maintain style: `"Change to daytime while maintaining the same style of the painting"`



### 

​

2\. Style Transfer

**Principles:**

  * Clearly name style: `"Transform to Bauhaus art style"`
  * Describe characteristics: `"Transform to oil painting with visible brushstrokes, thick paint texture"`
  * Preserve composition: `"Change to Bauhaus style while maintaining the original composition"`



### 

​

3\. Character Consistency

**Framework:**

  * Specific description: `"The woman with short black hair"` instead of “she”
  * Preserve features: `"while maintaining the same facial features, hairstyle, and expression"`
  * Step-by-step modifications: Change background first, then actions



### 

​

4\. Text Editing

  * Use quotes: `"Replace 'joy' with 'BFL'"`
  * Maintain format: `"Replace text while maintaining the same font style"`



## 

​

Common Problem Solutions

### 

​

Character Changes Too Much

❌ Wrong: `"Transform the person into a Viking"` ✅ Correct: `"Change the clothes to be a viking warrior while preserving facial features"`

### 

​

Composition Position Changes

❌ Wrong: `"Put him on a beach"` ✅ Correct: `"Change the background to a beach while keeping the person in the exact same position, scale, and pose"`

### 

​

Style Application Inaccuracy

❌ Wrong: `"Make it a sketch"` ✅ Correct: `"Convert to pencil sketch with natural graphite lines, cross-hatching, and visible paper texture"`

## 

​

Core Principles

  1. **Be Specific and Clear** \- Use precise descriptions, avoid vague terms
  2. **Step-by-step Editing** \- Break complex modifications into multiple simple steps
  3. **Explicit Preservation** \- State what should remain unchanged
  4. **Verb Selection** \- Use “change”, “replace” rather than “transform”



## 

​

Best Practice Templates

**Object Modification:** `"Change [object] to [new state], keep [content to preserve] unchanged"` **Style Transfer:** `"Transform to [specific style], while maintaining [composition/character/other] unchanged"` **Background Replacement:** `"Change the background to [new background], keep the subject in the exact same position and pose"` **Text Editing:** `"Replace '[original text]' with '[new text]', maintain the same font style"`

> **Remember:** The more specific, the better. Kontext excels at understanding detailed instructions and maintaining consistency.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/flux/flux-1-kontext-dev.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/flux/flux-1-kontext-dev)

[FLUX.1 Krea Dev ComfyUI Workflow TutorialPrevious](https://docs.comfy.org/tutorials/flux/flux1-krea-dev)[ComfyUI Flux.1 Text-to-Image Workflow ExampleNext](https://docs.comfy.org/tutorials/flux/flux-1-text-to-image)

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
