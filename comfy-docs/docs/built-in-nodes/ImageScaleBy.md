---
url: https://docs.comfy.org/built-in-nodes/ImageScaleBy/
title: ImageScaleBy - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:10.991875+00:00
---

# ImageScaleBy - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ImageScaleBy/

Upscaling

# ImageScaleBy - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ImageScaleBy node is designed for upscaling images by a specified scale factor using various interpolation methods.

Copy pageCopy page

The ImageScaleBy node is designed for upscaling images by a specified scale factor using various interpolation methods. It allows for the adjustment of the image size in a flexible manner, catering to different upscaling needs.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`image`| The input image to be upscaled. This parameter is crucial as it provides the base image that will undergo the upscaling process.| `IMAGE`  
`upscale_method`| Specifies the interpolation method to be used for upscaling. The choice of method can affect the quality and characteristics of the upscaled image.| COMBO[STRING]  
`scale_by`| The factor by which the image will be upscaled. This determines the increase in size of the output image relative to the input image.| `FLOAT`  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`image`| The upscaled image, which is larger than the input image according to the specified scale factor and interpolation method.| `IMAGE`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScaleBy/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ImageScaleBy.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ImageScaleBy)

[ImageScale - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ImageScale)[ImageScaleToMaxDimension - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ImageScaleToMaxDimension)

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
