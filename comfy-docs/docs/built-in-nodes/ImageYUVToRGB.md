---
url: https://docs.comfy.org/built-in-nodes/ImageYUVToRGB/
title: ImageYUVToRGB - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:11.847666+00:00
---

# ImageYUVToRGB - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ImageYUVToRGB/

Color

# ImageYUVToRGB - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ImageYUVToRGB node converts YUV color space images to RGB color space.

Copy pageCopy page

The ImageYUVToRGB node converts YUV color space images to RGB color space. It takes three separate input images representing the Y (luma), U (blue projection), and V (red projection) components and combines them into a single RGB image.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`Y`| The Y (luminance) component input image. If the image has more than three channels, only the first three are used and averaged into a single channel.| IMAGE| Yes| -  
`U`| The U (blue projection) component input image. If the image has more than three channels, only the first three are used and averaged into a single channel.| IMAGE| Yes| -  
`V`| The V (red projection) component input image. If the image has more than three channels, only the first three are used and averaged into a single channel.| IMAGE| Yes| -  
  
**Note:** All three input images (Y, U, and V) must be provided together and must have compatible dimensions (matching height, width, and batch size) for the conversion to succeed.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The converted RGB image| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageYUVToRGB/en.md)

* * *

**Source fingerprint (SHA-256):** `47e90b1a9aeb5ddfccea4493021b83e06faad3f84d40c8b0f2b3cec59b192c2e`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ImageYUVToRGB.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ImageYUVToRGB)

[ImageSDRToHDR - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ImageSDRToHDR)[NormalizeImages - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/NormalizeImages)

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
