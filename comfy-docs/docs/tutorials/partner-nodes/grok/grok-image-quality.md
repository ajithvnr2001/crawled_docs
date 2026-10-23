---
url: https://docs.comfy.org/tutorials/partner-nodes/grok/grok-image-quality/
title: Grok Imagine Image Quality in ComfyUI: AI Image Generation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:30.058455+00:00
---

# Grok Imagine Image Quality in ComfyUI: AI Image Generation - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/grok/grok-image-quality/

## On this page

  * What Grok Imagine Image Quality is good at
  * Example outputs
  * Grok Imagine Image Quality: Generation
    * Workflow overview
    * Steps to run



Grok

# Grok Imagine Image Quality in ComfyUI: AI Image Generation

Copy pageCopy page

Generate enhanced images with Grok Imagine Image Quality in ComfyUI: improved detail, better text rendering, and stronger creative control

Copy pageCopy page

Grok Imagine Image Quality is xAI’s higher-fidelity image model, available in ComfyUI through the Grok partner nodes. It adds improved detail, better text rendering, and stronger creative control compared to the standard Grok image model.

## 

​

What Grok Imagine Image Quality is good at

  * **Improved detail** : higher-fidelity output than the standard Grok image model
  * **Better text rendering** : handles prompts that include text you want rendered in the image
  * **Stronger creative control** : more control over the generated result compared to the standard model
  * **Resolution options** : outputs at 1K or 2K



## 

​

Example outputs

Enhanced image generation with the `grok-imagine-image-quality` model: ![Grok Imagine Image Quality generation output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_grok_imagine_image_quality_image_generation.png)

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

Grok Imagine Image Quality: Generation

Generate enhanced images with the `grok-imagine-image-quality` model, which adds improved detail, better text rendering, and stronger creative control compared to the standard model. ![Grok Imagine Image Quality generation workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_grok_imagine_image_quality_image_generation-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Grok Imagine Image Quality” in Template Library

![Grok Imagine Image Quality generation output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_grok_imagine_image_quality_image_generation.png)

### 

​

Workflow overview

This workflow uses two nodes:

  * **GrokImageNode** : the core node, configured with the `grok-imagine-image-quality` model
  * **SaveImage** : saves the generated image



### 

​

Steps to run

  1. **Enter your prompt** : describe the scene and any text you want rendered in the **GrokImageNode**
  2. **Choose aspect ratio** : pick from the available ratios
  3. **Set resolution** : `1K` or `2K`
  4. **Click Queue** : press `Ctrl+Enter` to generate



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/grok/grok-image-quality.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/grok/grok-image-quality)

[Grok Imagine Image 2.0 in ComfyUI: AI Image Generation and EditingPrevious](https://docs.comfy.org/tutorials/partner-nodes/grok/grok-image-2-0)[ComfyUI Ideogram 4.0 Partner Node TutorialNext](https://docs.comfy.org/tutorials/partner-nodes/ideogram/ideogram-v4)

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
