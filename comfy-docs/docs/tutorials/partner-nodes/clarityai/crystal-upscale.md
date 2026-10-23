---
url: https://docs.comfy.org/tutorials/partner-nodes/clarityai/crystal-upscale/
title: Clarity AI Crystal Upscaler in ComfyUI: Faithful Upscaling - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:27.753883+00:00
---

# Clarity AI Crystal Upscaler in ComfyUI: Faithful Upscaling - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/clarityai/crystal-upscale/

## On this page

  * Available workflows
    * Image Upscale
    * Workflow overview
    * Steps to run
  * Node controls
  * Tips
  * Get started



Clarity AI

# Clarity AI Crystal Upscaler in ComfyUI: Faithful Upscaling

Copy pageCopy page

Upscale images with Clarity AI’s Crystal Upscaler in ComfyUI: faithful detail restoration up to 100 megapixels, with scale factor and creativity controls.

Copy pageCopy page

**Clarity AI Crystal Upscaler** is a high-fidelity image upscaler in ComfyUI. Instead of inventing new content, it re-renders the image at a larger size while staying close to the original: faces, skin, and fine texture come back sharp, and the structure of the picture is preserved. It is built for portraits, product shots, and print-ready enlargements where faithful detail matters more than a creative reinterpretation. In ComfyUI the model runs through the **Clarity AI Crystal Upscale** partner node. It is a cloud API node: it needs a Comfy account with credits and downloads no local model. You take one image in and get one upscaled image out, alongside a side-by-side comparison. See [Partner Node pricing](https://docs.comfy.org/tutorials/partner-nodes/pricing) for the per-megapixel rate. Output is capped at 100 megapixels and 65535 pixels per side. The node multiplies the input width and height by the `scale_factor`, so a smaller source or a lower factor is how you stay inside the limit.

## 

​

Available workflows

### 

​

Image Upscale

Upscale a single image and compare the result against the original. The template loads a source image, upscales it at 2x, and shows an `ImageCompare` view of the input and the output. ![Clarity AI Crystal Upscale workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_clarity_ai_crystal_upscale-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Clarity AI: Crystal Upscaler” in Template Library

**Input material**

## watch_spa_black.png

Load into the `LoadImage` node that feeds the Clarity AI Crystal Upscale node

### 

​

Workflow overview

The template uses four nodes:

  * **LoadImage** : provides the source image
  * **ClarityCrystalUpscaleNode** : the core node, configured with the `crystal-upscaler` model
  * **SaveImageAdvanced** : saves the upscaled output as PNG
  * **ImageCompare** : shows the upscaled result next to the original



### 

​

Steps to run

  1. **Load an image** : upload or select your source image in the **LoadImage** node
  2. **Select the model** : keep `crystal-upscaler` on the **Clarity AI Crystal Upscale** node
  3. **Set the scale factor** : choose how much to enlarge the image, from 1x to 200x
  4. **Set creativity** : `0` stays closest to the original; higher values let the model reconstruct more detail
  5. **Click Queue** or press `Ctrl+Enter` to generate



## 

​

Node controls

Control| Values| Effect  
---|---|---  
`image`| one image| Source image. The node takes exactly one image; a batch is rejected  
`scale_factor`| 1.0 to 200.0, default 2.0| Multiplies the input width and height. Output is capped at 100 megapixels and 65535 pixels per side  
`creativity`| 0 to 10, default 0| `0` preserves the original most closely. Higher values let the model reconstruct more detail instead of strictly following the source. Has no effect when the shorter side of the image is 256 pixels or less  
  
## 

​

Tips

  * **Start at 2x and raise the factor only if you need it**. The factor multiplies both sides of the image, so a large factor can push the output past 100 megapixels or 65535 pixels per side and fail the run.
  * **Set`creativity` to 0 for product and archival shots**. It stays closest to the source; raise it only when you want the model to rebuild texture the source no longer contains.
  * **Small inputs ignore`creativity`**. Images whose shorter side is 256 pixels or less use the same result regardless of the setting.
  * **Check the comparison view**. The template pairs the output with the input, so you can judge whether the added detail is faithful before committing to a large render.



## 

​

Get started

  1. Update ComfyUI to the latest version
  2. Go to Template Library, search for `Clarity AI: Crystal Upscaler`



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/clarityai/crystal-upscale.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/clarityai/crystal-upscale)

[ByteDance Seedream 5.0 Lite - Smart AI Image CreationPrevious](https://docs.comfy.org/tutorials/partner-nodes/bytedance/seedream-5-lite)[Nano Banana Pro: Studio-Quality AI Image GenerationNext](https://docs.comfy.org/tutorials/partner-nodes/google/nano-banana-pro)

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
