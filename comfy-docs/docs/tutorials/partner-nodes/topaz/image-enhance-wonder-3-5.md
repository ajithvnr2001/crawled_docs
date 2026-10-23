---
url: https://docs.comfy.org/tutorials/partner-nodes/topaz/image-enhance-wonder-3-5/
title: Topaz Image Enhance Wonder 3.5 - AI image enhancement - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:38.614291+00:00
---

# Topaz Image Enhance Wonder 3.5 - AI image enhancement - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/topaz/image-enhance-wonder-3-5/

## On this page

  * What Topaz Image Enhance Wonder 3.5 is good at
  * Example outputs
  * Topaz Image Enhance Wonder 3.5
    * Workflow overview
    * Steps to run
  * Get started



Topaz

# Topaz Image Enhance Wonder 3.5 - AI image enhancement

Copy pageCopy page

Upscale and enhance images with Topaz Image Enhance Wonder 3.5 in ComfyUI: generative detail restoration, noise reduction, and text sharpening

Copy pageCopy page

Topaz Image Enhance Wonder 3.5 is a generative enhancement model available in ComfyUI through the Topaz partner nodes. It adds fine detail, reduces noise, and sharpens text and structured graphics, with low, medium, and high enhancement strengths. It preserves the input aspect ratio and supports upscale factors from 1x to 6x.

## 

​

What Topaz Image Enhance Wonder 3.5 is good at

  * **Generative detail restoration** : Adds fine detail to the source image
  * **Noise reduction** : Cleans up noise while enhancing
  * **Text and graphics sharpening** : Sharpens text and structured graphics
  * **Adjustable strength** : Choose low, medium, or high enhancement strength
  * **Flexible output** : Preserves the input aspect ratio and supports upscale factors from 1x to 6x



## 

​

Example outputs

Image enhancement with fine detail added and noise reduced: ![Topaz Image Enhance Wonder 3.5 output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_topaz_image_enhance_wonder3_5.png)

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

Topaz Image Enhance Wonder 3.5

Upscale and enhance a single image with Wonder 3.5’s generative model, which adds fine detail, reduces noise, and sharpens text and structured graphics. The workflow takes 1 input image and produces 1 enhanced output alongside a side-by-side comparison. ![Topaz Image Enhance Wonder 3.5 workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_topaz_image_enhance_wonder3_5-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Topaz Image Enhance Wonder 3.5” in Template Library

![Topaz Image Enhance Wonder 3.5 output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_topaz_image_enhance_wonder3_5.png)

### 

​

Workflow overview

This workflow uses four nodes:

  * **LoadImage** : provides the source image
  * **TopazImageEnhanceV2** : the core node, configured with the `Wonder 3.5` enhancement model
  * **SaveImageAdvanced** : saves the enhanced output as PNG
  * **ImageCompare** : shows the enhanced result next to the original for comparison



### 

​

Steps to run

  1. **Load an image** : upload or select your input image in the **LoadImage** node
  2. **Select the model** : keep `Wonder 3.5` on the **TopazImageEnhanceV2** node
  3. **Choose enhancement strength** : `low`, `medium`, or `high`
  4. **Set upscale factor** : from 1x to 6x
  5. **Click Queue** : press `Ctrl+Enter` to generate



## 

​

Get started

  1. Update ComfyUI to the latest version
  2. Go to Template Library, search for `Topaz Image Enhance Wonder 3.5`



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/topaz/image-enhance-wonder-3-5.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/topaz/image-enhance-wonder-3-5)

[Tencent Hunyuan Image 3.5 Preview in ComfyUI: Text to Image and Edit WorkflowsPrevious](https://docs.comfy.org/tutorials/partner-nodes/tencent/hy-image-3-5)[Topaz Image Enhance Bloom 2 - AI creative image upscalingNext](https://docs.comfy.org/tutorials/partner-nodes/topaz/image-enhance-bloom-2)

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
