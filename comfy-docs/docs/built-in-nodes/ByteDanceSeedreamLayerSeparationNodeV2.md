---
url: https://docs.comfy.org/built-in-nodes/ByteDanceSeedreamLayerSeparationNodeV2/
title: ByteDanceSeedreamLayerSeparationNodeV2 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:30.886202+00:00
---

# ByteDanceSeedreamLayerSeparationNodeV2 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ByteDanceSeedreamLayerSeparationNodeV2/

Bytedance

# ByteDanceSeedreamLayerSeparationNodeV2 - ComfyUI Built-in Node Documentation

Copy pageCopy page

ByteDance Seedream 5.0 Layer Separation decomposes an image into a background plate plus up to 16 repositionable transparent layers, each with stacking order

Copy pageCopy page

ByteDance Seedream 5.0 Layer Separation decomposes an image into a background plate plus up to 16 repositionable transparent layers, each with stacking order, bounding box, name, and description. It returns the background, per-layer images with masks, placement boxes, and a ready-to-edit layer stack. The `model` selector chooses between Seedream 5.0 Pro and the faster Seedream 5.0 Flash.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The Seedream model used for the separation. “seedream 5.0 pro” (default) gives the highest separation quality and also exposes a `prompt_optimization` control; “seedream 5.0 flash” is faster and cheaper and has no prompt-optimization control.| DYNAMIC_COMBO| Yes| ”seedream 5.0 pro"  
"seedream 5.0 flash”  
  
### 

​

Seedream 5.0 Pro and 5.0 Flash Inputs

These inputs are available with both models.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The image to separate. Exactly one image, at least 512x512 pixels, aspect ratio between 1:16 and 16:1. Inputs larger than about 4MP are downscaled before upload.| IMAGE| Yes| Single image  
`prompt`| How to separate the image. Leave empty to auto-detect and separate all major elements. Describe elements in natural language to control the separation, or target exact regions with `<bbox>left top right bottom</bbox>` tags (0-1000 per-mille coordinates). Default: empty string.| STRING| Yes| Multiline text  
`size`| Output resolution level. “auto” follows the input image size (clamped to the 1K-2K range). Default: “auto”.| COMBO| Yes| ”auto"  
"1K"  
"1.5K"  
"2K”  
`seed`| Seed to use for generation. Default: 42.| INT| Yes| 0 to 2147483647  
`watermark`| Whether to add an “AI generated” watermark to the images. Default: false.| BOOLEAN| Yes| false  
true  
`crop_layers`| Geometry of the layers/masks batch outputs (layer_stack is unaffected and always tight). Full canvas: each layer on a base-sized canvas at its bounding-box position - recompose directly with ImageCompositeMasked. Minimal size: each layer cropped to its bounding box (padded to the largest layer for batching) - much smaller tensors; rebuild placement with Layers From Bounding Boxes using the bboxes output. Default: false (full canvas).| BOOLEAN| Yes| false (full canvas)  
true (minimal size)  
  
### 

​

Seedream 5.0 Pro Only Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt_optimization`| Prompt-optimization mode: “standard” gives higher quality, “fast” shorter generation time. Only available with Seedream 5.0 Pro. Default: “standard”.| COMBO| Yes| ”standard"  
"fast”  
  
**Note:** The input `image` must be a single image; batches are not supported. The image must be at least 512x512 pixels with an aspect ratio between 1:16 and 16:1. Seedream 5.0 Flash has no `prompt_optimization` input.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`base_image`| The base image (background plate) the layers stack onto.| IMAGE  
`base_mask`| Transparency of the base image (1 = transparent, LoadImage convention); currently always fully opaque.| MASK  
`layers`| Transparent layers ordered bottom to top. Full canvas mode: placed on a black base-sized canvas at their bounding-box position. Minimal size mode: cropped to their bounding box, anchored top-left, padded to the largest layer.| IMAGE  
`masks`| Per-layer transparency, index-aligned with the layers batch (1 = transparent, LoadImage convention). For ImageCompositeMasked-style compositing, add InvertMask first.| MASK  
`bboxes`| One placement box per layer, index-aligned with the layers batch (feed both, plus masks, into Layers From Bounding Boxes to rebuild per-layer placement): `{x, y, width, height, metadata: {name, desc, z_index, native_size, content_rect, flags}}`. `content_rect = [left, top, width, height]` is the layer’s content region within its own frame; it lands on the canvas at the box position plus that offset.| BOUNDING_BOX  
`layer_stack`| Ready-to-edit layer document for Create Layered Image: the base plate plus each element as its own named, tight-cropped layer at its true position and stacking order. Connect directly, or extend with Add Layer.| LAYERS  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamLayerSeparationNodeV2/en.md)

* * *

**Source fingerprint (SHA-256):** `b106ca63d37aea68079f0032a1f7dfeefee9f759c71bb1605bbfe66c3d9dad62`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ByteDanceSeedreamLayerSeparationNodeV2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ByteDanceSeedreamLayerSeparationNodeV2)

[ByteDanceSeedreamLayerSeparationNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ByteDanceSeedreamLayerSeparationNode)[ByteDanceSeedreamNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ByteDanceSeedreamNode)

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
