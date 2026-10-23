---
url: https://docs.comfy.org/tutorials/partner-nodes/grok/grok-image-2-0/
title: Grok Imagine Image 2.0 in ComfyUI: AI Image Generation and Editing - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:30.274808+00:00
---

# Grok Imagine Image 2.0 in ComfyUI: AI Image Generation and Editing - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/grok/grok-image-2-0/

## On this page

  * What Grok Imagine Image 2.0 is good at
  * Example outputs
  * Grok Imagine Image 2.0: Text to Image
    * Workflow overview
    * Steps to run
  * Grok Imagine Image 2.0: Image Edit
    * Workflow overview
    * Steps to run



Grok

# Grok Imagine Image 2.0 in ComfyUI: AI Image Generation and Editing

Copy pageCopy page

Generate and edit images with Grok Imagine Image 2.0 in ComfyUI: Aurora engine, crisp short-text rendering, 1K/2K output, and up to 3 reference images

Copy pageCopy page

Grok Imagine Image 2.0 is xAI’s latest image model, available in ComfyUI through the Grok partner nodes. Built on the Aurora engine, it excels at crisp short-text rendering and produces 1K or 2K images across 14 aspect ratios, making it well suited for posters, covers, product and brand visuals, and character-driven scenes where consistency matters.

## 

​

What Grok Imagine Image 2.0 is good at

  * **Crisp short-text rendering** : the Aurora engine renders short text cleanly, making it well suited for posters, covers, and product and brand visuals
  * **Reference-guided image editing** : edits images with precise, natural-language instructions and up to 3 reference images to modify elements, swap backgrounds, or restyle scenes
  * **Character consistency** : keeps a character consistent across multiple outputs in character-driven scenes
  * **14 aspect ratios** : from `1:1` to `9:20`
  * **Cost control** : 1K or 2K resolution with low or medium quality options to balance cost and fidelity



## 

​

Example outputs

Poster-style text-to-image generation with crisp text rendering: ![Grok Imagine Image 2.0 text-to-image output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_grok_imagine_image_2_t2i.png) Image editing guided by character and product reference images: ![Grok Imagine Image 2.0 image edit output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_grok_imagine_image_2_image_edit.png)

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

Grok Imagine Image 2.0: Text to Image

Generate a full poster-style image from a single text prompt with the Aurora engine. This workflow excels at crisp short-text rendering, making it well suited for posters, covers, product and brand visuals, and character-driven scenes. It outputs 1K or 2K images across 14 aspect ratios, with low or medium quality options to control cost. ![Grok Imagine Image 2.0 text-to-image workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_grok_imagine_image_2_t2i-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Grok Imagine Image 2.0” in Template Library

![Grok Imagine Image 2.0 text-to-image output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_grok_imagine_image_2_t2i.png)

### 

​

Workflow overview

This workflow uses two nodes:

  * **GrokImageNode** : the core node, configured with the `grok-imagine-image-2.0` model
  * **SaveImageAdvanced** : saves the generated image as PNG



### 

​

Steps to run

  1. **Enter your prompt** : describe the scene, style, and any text you want rendered in the **GrokImageNode**
  2. **Choose aspect ratio** : pick from 14 ratios, from `1:1` to `9:20`
  3. **Select resolution** : `1K` for faster results or `2K` for more detail
  4. **Set quality** : `low` or `medium` to control cost and fidelity
  5. **Set seed** : control whether the node re-runs; outputs are not reproducible regardless of seed
  6. **Click Queue** : press `Ctrl+Enter` to generate



## 

​

Grok Imagine Image 2.0: Image Edit

Edit images with precise, natural-language instructions and up to 3 reference images. Use this workflow to modify specific elements, swap backgrounds, restyle scenes, or keep a character consistent across multiple outputs. The Aurora engine delivers crisp short-text rendering at 1K or 2K resolution across 14 aspect ratios. ![Grok Imagine Image 2.0 image edit workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_grok_imagine_image_2_image_edit-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Grok Imagine Image 2.0” in Template Library

![Grok Imagine Image 2.0 image edit output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_grok_imagine_image_2_image_edit.png)

### 

​

Workflow overview

This workflow uses four nodes:

  * **LoadImage** x2: provide the character and product reference images (the node accepts up to 3)
  * **GrokImageEditNodeV2** : the core node, configured with the `grok-imagine-image-2.0` model
  * **SaveImage** : saves the edited image



### 

​

Steps to run

  1. **Load your references** : connect up to 3 reference images to the **LoadImage** nodes
  2. **Describe the edit** : tell the model what to keep, change, or restyle in the **GrokImageEditNodeV2** prompt
  3. **Set resolution** : `1K` or `2K`
  4. **Click Queue** : press `Ctrl+Enter` to generate



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/grok/grok-image-2-0.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/grok/grok-image-2-0)

[Grok Imagine Image in ComfyUI: AI Image Generation and EditingPrevious](https://docs.comfy.org/tutorials/partner-nodes/grok/grok-image)[Grok Imagine Image Quality in ComfyUI: AI Image GenerationNext](https://docs.comfy.org/tutorials/partner-nodes/grok/grok-image-quality)

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
