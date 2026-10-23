---
url: https://docs.comfy.org/built-in-nodes/ImageScaleToMaxDimension/
title: ImageScaleToMaxDimension - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:11.236120+00:00
---

# ImageScaleToMaxDimension - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ImageScaleToMaxDimension/

Upscaling

# ImageScaleToMaxDimension - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ImageScaleToMaxDimension node resizes images to fit within a specified maximum dimension while maintaining the original aspect ratio.

Copy pageCopy page

The ImageScaleToMaxDimension node resizes images to fit within a specified maximum dimension while maintaining the original aspect ratio. It calculates whether the image is portrait or landscape oriented, then scales the larger dimension to match the target size while proportionally adjusting the smaller dimension. The node supports multiple upscaling methods for different quality and performance requirements.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The input image to be scaled| IMAGE| Yes| -  
`upscale_method`| The interpolation method used for scaling the image (default: “area”)| STRING| Yes| ”area"  
"lanczos"  
"bilinear"  
"nearest-exact"  
"bilinear"  
"bicubic”  
`largest_size`| The maximum dimension for the scaled image (default: 512)| INT| Yes| 0 to 16384  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The scaled image with the largest dimension matching the specified size| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScaleToMaxDimension/en.md)

* * *

**Source fingerprint (SHA-256):** `83eba56d9f673fb570edc6504fd82f1274ead1d3e055a1a8bcc207c178388015`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ImageScaleToMaxDimension.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ImageScaleToMaxDimension)

[ImageScaleBy - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ImageScaleBy)[ImageScaleToTotalPixels - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ImageScaleToTotalPixels)

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
