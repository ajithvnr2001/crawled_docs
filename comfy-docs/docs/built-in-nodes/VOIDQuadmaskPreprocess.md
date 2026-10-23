---
url: https://docs.comfy.org/built-in-nodes/VOIDQuadmaskPreprocess/
title: VOIDQuadmaskPreprocess - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-19T14:35:07.574290+00:00
---

# VOIDQuadmaskPreprocess - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/VOIDQuadmaskPreprocess/

Mask

# VOIDQuadmaskPreprocess - ComfyUI Built-in Node Documentation

Copy pageCopy page

The VOIDQuadmaskPreprocess node prepares a mask for VOID inpainting by converting it into a special four-level “quadmask.” It takes an input mask

Copy pageCopy page

## 

​

Overview

The VOIDQuadmaskPreprocess node prepares a mask for VOID inpainting by converting it into a special four-level “quadmask.” It takes an input mask, optionally dilates the primary region, then quantizes the mask values into four distinct levels representing different semantic regions (primary object, overlap, affected area, and background). Finally, it inverts and normalizes the mask so the output values are in the range [0, 1], where 1.0 indicates the area to remove and 0.0 indicates the area to keep.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`mask`| The input mask to be preprocessed.| MASK| Yes| N/A  
`dilate_width`| Dilation radius for the primary mask region. A value of 0 means no dilation is applied. (default: 0)| INT| No| 0 to 50 (step: 1)  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`quadmask`| The preprocessed quadmask with values in [0, 1], representing four discrete levels: 1.0 (primary object to remove), ~0.75 (overlap of primary and affected), ~0.50 (affected region), and 0.0 (background to keep).| MASK  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDQuadmaskPreprocess/en.md)

* * *

**Source fingerprint (SHA-256):** `a972ff74686baaa3a3659a74517d3b6f7335e8f62d09be9329d0e71d1fad137a`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/VOIDQuadmaskPreprocess.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/VOIDQuadmaskPreprocess)

[ThresholdMask - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ThresholdMask)[SeedVR2PostProcessing - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SeedVR2PostProcessing)

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
