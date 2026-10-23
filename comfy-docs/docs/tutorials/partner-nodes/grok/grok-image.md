---
url: https://docs.comfy.org/tutorials/partner-nodes/grok/grok-image/
title: Grok Imagine Image in ComfyUI: AI Image Generation and Editing - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:30.164273+00:00
---

# Grok Imagine Image in ComfyUI: AI Image Generation and Editing - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/grok/grok-image/

## On this page

  * What Grok Imagine Image is good at
  * Example outputs
  * Grok: Text to Image
    * Workflow overview
    * Steps to run
  * Grok: Image Edit
    * Workflow overview
    * Steps to run



Grok

# Grok Imagine Image in ComfyUI: AI Image Generation and Editing

Copy pageCopy page

Generate and edit images with the Grok Imagine Image model in ComfyUI: text-to-image and natural-language image editing

Copy pageCopy page

Grok Image is xAI’s image generation model, available in ComfyUI through the Grok partner nodes. It generates images from text prompts and edits uploaded images with natural-language instructions, supporting 13 aspect ratios and 1K or 2K output.

## 

​

What Grok Imagine Image is good at

  * **Text-to-image generation** : creates single images from a text prompt describing the scene and style
  * **Natural-language image editing** : edits an uploaded image based on your prompt while keeping the original composition, changing the scene, lighting, or style
  * **Flexible aspect ratios** : supports 13 aspect ratios, including `1:1`, `16:9`, and `9:16`
  * **Resolution options** : outputs at 1K or 2K



## 

​

Example outputs

Text-to-image generation from a single prompt: ![Grok text-to-image output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_grok_text_to_image.png) Image editing with natural-language instructions, keeping the original composition: ![Grok image edit output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_grok_image_edit.png)

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

Grok: Text to Image

Generate images from a text prompt with the standard `grok-imagine-image` model. This workflow is the fastest way to create single images in ComfyUI with Grok, supporting 13 aspect ratios and 1K or 2K output. ![Grok text-to-image workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_grok_text_to_image-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Grok Imagine” in Template Library

![Grok text-to-image output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_grok_text_to_image.png)

### 

​

Workflow overview

This workflow uses two nodes:

  * **GrokImageNode** : the core node, configured with the `grok-imagine-image` model
  * **SaveImage** : saves the generated image



### 

​

Steps to run

  1. **Enter your prompt** : describe the scene and style in the **GrokImageNode**
  2. **Choose aspect ratio** : pick from ratios such as `1:1`, `16:9`, `9:16`, and more
  3. **Set resolution** : `1K` or `2K`
  4. **Click Queue** : press `Ctrl+Enter` to generate



## 

​

Grok: Image Edit

Edit an uploaded image with natural-language instructions. This workflow keeps the original composition and changes the scene, lighting, or style based on your prompt. ![Grok image edit workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_grok_image_edit-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Grok Imagine” in Template Library

![Grok image edit output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_grok_image_edit.png)

### 

​

Workflow overview

This workflow uses three nodes:

  * **LoadImage** : provides the source image to edit
  * **GrokImageEditNode** : the core node, configured with the `grok-imagine-image` model
  * **SaveImage** : saves the edited image



### 

​

Steps to run

  1. **Load an image** : connect your image to the **LoadImage** node
  2. **Describe the edit** : tell the model what to change in the **GrokImageEditNode** prompt
  3. **Click Queue** : press `Ctrl+Enter` to generate



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/grok/grok-image.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/grok/grok-image)

[Grok in ComfyUI: AI Image and Video GenerationPrevious](https://docs.comfy.org/tutorials/partner-nodes/grok/grok-overview)[Grok Imagine Image 2.0 in ComfyUI: AI Image Generation and EditingNext](https://docs.comfy.org/tutorials/partner-nodes/grok/grok-image-2-0)

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
