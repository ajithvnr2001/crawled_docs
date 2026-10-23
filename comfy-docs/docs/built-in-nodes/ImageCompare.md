---
url: https://docs.comfy.org/built-in-nodes/ImageCompare/
title: ImageCompare - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-18T12:01:27.399052+00:00
---

# ImageCompare - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ImageCompare/

Image

# ImageCompare - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Image Compare node provides a visual interface to compare two images side-by-side using a draggable slider.

Copy pageCopy page

## 

​

Overview

The Image Compare node provides a visual interface to compare two images side-by-side using a draggable slider. It is designed as an output node, meaning it does not pass data to other nodes but instead displays the images directly in the user interface for inspection.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image_a`| The first image to compare.| IMAGE| No| -  
`image_b`| The second image to compare.| IMAGE| No| -  
`compare_view`| The control that enables the slider comparison view in the UI.| IMAGECOMPARE| Yes| -  
  
**Note:** This node is an output node. While `image_a` and `image_b` are optional, at least one image must be provided for the node to have a visible effect. The node will display an empty area for any image input that is not connected. Each provided image batch is saved to temporary storage under the prefixes `comfy.compare.a` and `comfy.compare.b` respectively, then shown in the slider view.

## 

​

Outputs

This node is an output node and does not produce any data outputs for use in other nodes. Its function is to display the provided images in the ComfyUI interface.

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCompare/en.md)

* * *

**Source fingerprint (SHA-256):** `bc065572c5631ed80c0590aabae775c51d0f607895a87cb2cca78037ab9a6638`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ImageCompare.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ImageCompare)

[ImageBatch - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ImageBatch)[ImageCompositor - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ImageCompositor)

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
