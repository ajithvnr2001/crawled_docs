---
url: https://docs.comfy.org/built-in-nodes/AdjustBrightness/
title: AdjustBrightness - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:19.566357+00:00
---

# AdjustBrightness - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/AdjustBrightness/

Adjustments

# AdjustBrightness - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Adjust Brightness node changes how bright an image looks.

Copy pageCopy page

The Adjust Brightness node changes how bright an image looks. It multiplies the image’s color values by a `factor` and keeps the results within the valid 0.0 to 1.0 range. A factor of 1.0 leaves the image unchanged, values below 1.0 make it darker, and values above 1.0 make it brighter.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The input image to adjust. Accepts a single image or a batch of images.| IMAGE| Yes| -  
`factor`| Brightness factor. 1.0 = no change, <1.0 = darker, >1.0 = brighter. (default: 1.0)| FLOAT| No| 0.0 - 2.0  
  
Note: If the input image has an alpha channel (RGBA), only the color channels are adjusted. The alpha channel is copied from the input unchanged because it stores transparency, not color.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The output image with adjusted brightness. If the input has an alpha channel, the alpha values remain unchanged.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AdjustBrightness/en.md)

* * *

**Source fingerprint (SHA-256):** `64c1499d16deb5922fa63538182cd227e8f2ba9ded5962064ce9f228a0f4a163`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/AdjustBrightness.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/AdjustBrightness)

[TorchCompileModel - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/TorchCompileModel)[AdjustContrast - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/AdjustContrast)

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
