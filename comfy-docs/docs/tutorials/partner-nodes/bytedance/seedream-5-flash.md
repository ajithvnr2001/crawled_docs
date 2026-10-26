---
url: https://docs.comfy.org/tutorials/partner-nodes/bytedance/seedream-5-flash/
title: ByteDance Seedream 5.0 Flash: Fast Image Generation in ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:04:01.858573+00:00
---

# ByteDance Seedream 5.0 Flash: Fast Image Generation in ComfyUI - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/bytedance/seedream-5-flash/

## On this page

Back to top

  * What Seedream 5.0 Flash is good at
  * Example outputs
  * Seedream 5.0 Flash text-to-image workflow
  * Seedream 5.0 Flash image edit workflow
  * Get started



ByteDance

# ByteDance Seedream 5.0 Flash: Fast Image Generation in ComfyUI

Copy pageCopy page

Generate and edit images up to 2K with Seedream 5.0 Flash in ComfyUI, the flat-rate tier of the ByteDance Seedream 5.0 image family

Copy pageCopy page

Seedream 5.0 Flash is the fast tier of ByteDance’s Seedream 5.0 image family, alongside Seedream 5.0 Pro and Seedream 5.0 Lite. It generates an image from a text prompt and edits an existing image from a single instruction in the same node, and it bills one flat rate per generated image at every resolution it supports. A run returns one image between 1K and 2K, with eight aspect ratios available in each of the 1K, 1.5K, and 2K tiers. Up to 10 reference images can be attached for multi-reference compositions such as a product shot placed into a new layout. The same model can also be selected in the layer separation node, which splits a flat image into editable transparent layers.

## 

​

What Seedream 5.0 Flash is good at

  * **Flat rate at every resolution** : One price per generated image at 1K, 1.5K, and 2K, so the resolution you pick does not change the cost
  * **Generation and editing in one node** : Generate from a prompt, or attach a reference image and describe the change in a sentence
  * **Multi-reference input** : Accepts up to 10 reference images, which is enough to combine several subjects, products, or styles in one composition
  * **Text rendering** : Handles captions, labels, and layout text inside the generated image
  * **Single image per run** : Each run returns one image. The batch and sequential generation options available on other Seedream models are not exposed for this model
  * **Layer separation** : Selectable as the model in the layer separation node for turning a flat image into an editable layer stack



## 

​

Example outputs

Text-to-image generation, producing one image at the selected size preset: ![Seedream 5.0 Flash text to image example](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_bytedance_seedream_5_0_flash_t2i.png) Image editing from a single reference image and a text instruction: ![Seedream 5.0 Flash image edit example](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_bytedance_seedream_5_0_flash_image_edit.png)

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

Seedream 5.0 Flash text-to-image workflow

Generate an image from a text prompt. The workflow returns a single image at the size preset selected on the node. ![Seedream 5.0 Flash text-to-image workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_seedream_5_0_flash_t2i-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Seedream 5.0 Flash” in Template Library

## 

​

Seedream 5.0 Flash image edit workflow

Edit an existing image with a text instruction. Connect the source image to the node’s `image_1` input and describe the change you want, from swapping a background to rebuilding a product set around the subject in the reference. ![Seedream 5.0 Flash image edit workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_seedream_5_0_flash_image_edit-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Seedream 5.0 Flash” in Template Library

## 

​

Get started

  1. Update ComfyUI to version 0.37.3 or later
  2. Go to Template Library, search for `Seedream 5.0 Flash`



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/bytedance/seedream-5-flash.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/bytedance/seedream-5-flash)

[FIBO 2.0](https://docs.comfy.org/tutorials/partner-nodes/bria/fibo)[Seedream 5 Pro](https://docs.comfy.org/tutorials/partner-nodes/bytedance/seedream-5-pro)
