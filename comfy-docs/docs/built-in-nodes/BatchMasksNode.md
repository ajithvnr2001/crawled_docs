---
url: https://docs.comfy.org/built-in-nodes/BatchMasksNode/
title: BatchMasksNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:23.162020+00:00
---

# BatchMasksNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/BatchMasksNode/

Mask

# BatchMasksNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Batch Masks node combines multiple individual mask inputs into a single batch.

Copy pageCopy page

The Batch Masks node combines multiple individual mask inputs into a single batch. It takes a variable number of mask inputs and outputs them as a single batched mask tensor, allowing for batch processing of masks in subsequent nodes. If the input masks have different sizes, they are automatically resized to match the dimensions of the first mask.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`mask`| The mask inputs to combine into a batch. At least one mask is required. You can add up to 50 masks total by clicking the ”+” button on the node. If masks have different sizes, they are automatically resized to match the first mask’s dimensions.| MASK| Yes| 1 to 50 masks  
  
**Note:** This node uses an autogrow input template. You must connect at least one mask. You can add up to 49 more mask inputs for a total of 50 masks. All connected masks will be combined into a single batch. If masks have different heights or widths, they are automatically resized to match the dimensions of the first mask using bilinear interpolation.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| A single batched mask containing all the input masks stacked together. If no masks are provided, returns None.| MASK  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchMasksNode/en.md)

* * *

**Source fingerprint (SHA-256):** `7e9bc4be72c7fa8fceab2cf167c72b7e1ff858c0281d977f2ad3ab433d9d58d6`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/BatchMasksNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/BatchMasksNode)

[MoGeRender - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/MoGeRender)[CropMask - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/CropMask)

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
