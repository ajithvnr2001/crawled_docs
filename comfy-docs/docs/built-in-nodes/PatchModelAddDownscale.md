---
url: https://docs.comfy.org/built-in-nodes/PatchModelAddDownscale/
title: PatchModelAddDownscale - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:41.053761+00:00
---

# PatchModelAddDownscale - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/PatchModelAddDownscale/

Unet

# PatchModelAddDownscale - ComfyUI Built-in Node Documentation

Copy pageCopy page

PatchModelAddDownscale (Kohya Deep Shrink) applies the Kohya Deep Shrink technique to a model by shrinking intermediate features at a chosen block and then

Copy pageCopy page

PatchModelAddDownscale (Kohya Deep Shrink) applies the Kohya Deep Shrink technique to a model by shrinking intermediate features at a chosen block and then scaling them back to their original size. The shrinking only happens during a selected part of the denoising process, which can reduce processing cost while keeping the final result close to the original.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The model to apply the downscale patch to| MODEL| Yes| -  
`block_number`| The specific block number where downscaling will be applied (default: 3)| INT| Yes| 1-32  
`downscale_factor`| The factor by which to downscale the features (default: 2.0)| FLOAT| Yes| 0.1-9.0  
`start_percent`| The starting point in the denoising process where downscaling begins (default: 0.0)| FLOAT| Yes| 0.0-1.0  
`end_percent`| The ending point in the denoising process where downscaling stops (default: 0.35)| FLOAT| Yes| 0.0-1.0  
`downscale_after_skip`| Whether to apply downscaling after skip connections (default: True)| BOOLEAN| Yes| -  
`downscale_method`| The interpolation method used for downscaling operations (default: “bicubic”)| COMBO| Yes| ”bicubic"  
"nearest-exact"  
"bilinear"  
"area"  
"bislerp”  
`upscale_method`| The interpolation method used for upscaling operations (default: “bicubic”)| COMBO| Yes| ”bicubic"  
"nearest-exact"  
"bilinear"  
"area"  
"bislerp”  
  
The downscale patch is applied only when the current denoising step falls within the range defined by `start_percent` and `end_percent`, and only at the block selected by `block_number`. When `downscale_after_skip` is enabled, the patch is applied after the skip connection; when disabled, it is applied before the skip connection. Features are scaled back up to their original size afterwards, but only when the current feature size no longer matches the size recorded before downscaling. The parameters `block_number`, `start_percent`, `end_percent`, and `downscale_after_skip` are marked as advanced options in the node interface.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| The modified model with downscale patch applied| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatchModelAddDownscale/en.md)

* * *

**Source fingerprint (SHA-256):** `aa9434a521ab585b290a3bd8db804469bd3bb02103a0d830b6be6eb8e8c26a5e`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/PatchModelAddDownscale.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/PatchModelAddDownscale)

[HyperTile - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/HyperTile)[PerturbedAttentionGuidance - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/PerturbedAttentionGuidance)

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
