---
url: https://docs.comfy.org/built-in-nodes/AdjustContrast/
title: AdjustContrast - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:19.742652+00:00
---

# AdjustContrast - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/AdjustContrast/

Adjustments

# AdjustContrast - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Adjust Contrast node adjusts the contrast of an input image by scaling the difference between light and dark areas around the midpoint of the color range.

Copy pageCopy page

The Adjust Contrast node adjusts the contrast of an input image by scaling the difference between light and dark areas around the midpoint of the color range. A factor of 1.0 leaves the image unchanged, values below 1.0 reduce contrast, and values above 1.0 increase contrast.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The input image to have its contrast adjusted.| IMAGE| Yes| -  
`factor`| Contrast factor. 1.0 = no change, <1.0 = less contrast, >1.0 = more contrast. (default: 1.0)| FLOAT| No| 0.0 - 2.0  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The resulting image with adjusted contrast. Pixel values are clamped to the 0.0–1.0 range. If the input image has an alpha channel, that channel is preserved unchanged.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AdjustContrast/en.md)

* * *

**Source fingerprint (SHA-256):** `489f840cc3d98339a5cf7b55e9179c60878c58b2f992740796c7d49642e05932`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/AdjustContrast.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/AdjustContrast)

[AdjustBrightness - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/AdjustBrightness)[RemoveBackground - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/RemoveBackground)

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
