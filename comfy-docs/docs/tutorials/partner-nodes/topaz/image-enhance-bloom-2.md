---
url: https://docs.comfy.org/tutorials/partner-nodes/topaz/image-enhance-bloom-2/
title: Topaz Image Enhance Bloom 2 - AI creative image upscaling - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:38.460595+00:00
---

# Topaz Image Enhance Bloom 2 - AI creative image upscaling - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/topaz/image-enhance-bloom-2/

## On this page

  * What Topaz Image Enhance Bloom 2 is good at
  * Example outputs
  * Topaz Image Enhance Bloom 2
    * Workflow overview
    * Steps to run
  * Get started



Topaz

# Topaz Image Enhance Bloom 2 - AI creative image upscaling

Copy pageCopy page

Upscale and enhance images with Topaz Image Enhance Bloom 2 in ComfyUI: creative upscaling that adds new detail, texture, and visual elements

Copy pageCopy page

Topaz Image Enhance Bloom 2 is a creative upscaling model available in ComfyUI through the Topaz partner nodes. It adds new detail, texture, and visual elements to your images, with a creativity control from 1 to 9 for subtle refinement or bold reinterpretation. It preserves the input aspect ratio and supports upscale factors from 1x to 6x.

## 

​

What Topaz Image Enhance Bloom 2 is good at

  * **Creative upscaling** : Adds new detail, texture, and visual elements to your images
  * **Adjustable creativity** : A control from 1 for restrained enhancement to 9 for pronounced reinterpretation
  * **Automatic prompting** : If the prompt is empty, the model creates one automatically
  * **Flexible output** : Preserves the input aspect ratio and supports upscale factors from 1x to 6x



## 

​

Example outputs

Creative upscaling of an AI-generated image, with new detail and texture added: ![Topaz Image Enhance Bloom 2 output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/Upscaled_topaz_bloom2.png)

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

Topaz Image Enhance Bloom 2

Enhance AI-generated images with Bloom 2’s creative upscaling model, which adds new detail, texture, and visual elements. The Creativity control ranges from 1 for restrained enhancement to 9 for pronounced reinterpretation. If the prompt is empty, the model creates one automatically. ![Topaz Image Enhance Bloom 2 workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_topaz_image_enhance_bloom2-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Topaz Image Enhance Bloom 2” in Template Library

![Topaz Image Enhance Bloom 2 output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/Upscaled_topaz_bloom2.png)

### 

​

Workflow overview

This workflow uses four nodes:

  * **LoadImage** : provides the source image
  * **TopazImageEnhanceV2** : the core node, configured with the `Bloom 2` enhancement model
  * **SaveImageAdvanced** : saves the enhanced output as PNG
  * **ImageCompare** : shows the enhanced result next to the original for comparison



### 

​

Steps to run

  1. **Load an image** : upload or select your input image in the **LoadImage** node
  2. **Select the model** : keep `Bloom 2` on the **TopazImageEnhanceV2** node
  3. **Set creativity** : from 1 for restrained enhancement to 9 for pronounced reinterpretation
  4. **Optional prompt** : leave empty to let the model create one automatically
  5. **Click Queue** : press `Ctrl+Enter` to generate



## 

​

Get started

  1. Update ComfyUI to the latest version
  2. Go to Template Library, search for `Topaz Image Enhance Bloom 2`



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/topaz/image-enhance-bloom-2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/topaz/image-enhance-bloom-2)

[Topaz Image Enhance Wonder 3.5 - AI image enhancementPrevious](https://docs.comfy.org/tutorials/partner-nodes/topaz/image-enhance-wonder-3-5)[Video ModelsNext](https://docs.comfy.org/tutorials/partner-nodes/video/overview)

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
