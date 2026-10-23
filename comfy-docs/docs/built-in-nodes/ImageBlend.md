---
url: https://docs.comfy.org/built-in-nodes/ImageBlend/
title: ImageBlend - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:06.695184+00:00
---

# ImageBlend - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ImageBlend/

Filters

# ImageBlend - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ImageBlend node is designed to blend two images together based on a specified blending mode and blend factor.

Copy pageCopy page

The `ImageBlend` node is designed to blend two images together based on a specified blending mode and blend factor. It supports various blending modes such as normal, multiply, screen, overlay, soft light, and difference, allowing for versatile image manipulation and compositing techniques. This node is essential for creating composite images by adjusting the visual interaction between two image layers.

## 

​

Inputs

Field| Description| Data Type  
---|---|---  
`image1`| The first image to be blended. It serves as the base layer for the blending operation.| `IMAGE`  
`image2`| The second image to be blended. Depending on the blend mode, it modifies the appearance of the first image.| `IMAGE`  
`blend_factor`| Determines the weight of the second image in the blend. A higher blend factor gives more prominence to the second image in the resulting blend.| `FLOAT`  
`blend_mode`| Specifies the method of blending the two images. Supports modes like normal, multiply, screen, overlay, soft light, and difference, each producing a unique visual effect.| COMBO[STRING]  
  
## 

​

Outputs

Field| Description| Data Type  
---|---|---  
`image`| The resulting image after blending the two input images according to the specified blend mode and factor.| `IMAGE`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageBlend/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ImageBlend.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ImageBlend)

[ImageAddNoise - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ImageAddNoise)[ImageBlur - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ImageBlur)

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
