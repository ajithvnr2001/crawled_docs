---
url: https://docs.comfy.org/built-in-nodes/ThresholdMask/
title: ThresholdMask - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:10.396442+00:00
---

# ThresholdMask - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ThresholdMask/

Mask

# ThresholdMask - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ThresholdMask node converts a mask to a binary mask by applying a threshold value.

Copy pageCopy page

The ThresholdMask node converts a mask to a binary mask by applying a threshold value. It compares each pixel in the input mask against the specified threshold value and creates a new mask where pixels above the threshold become 1 (white) and pixels below or equal to the threshold become 0 (black).

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`mask`| The input mask to be processed| MASK| Yes| -  
`value`| The threshold value for binarization (default: 0.5)| FLOAT| Yes| 0.0 - 1.0  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`mask`| The resulting binary mask after thresholding| MASK  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ThresholdMask/en.md)

* * *

**Source fingerprint (SHA-256):** `eff4479b70c1ca87ba9ba17b771edf5d816cf13c12ac0767cd7ee79d18e326c3`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ThresholdMask.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ThresholdMask)

[SolidMask - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SolidMask)[VOIDQuadmaskPreprocess - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/VOIDQuadmaskPreprocess)

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
