---
url: https://docs.comfy.org/built-in-nodes/ImageRGBToYUV/
title: ImageRGBToYUV - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:10.008129+00:00
---

# ImageRGBToYUV - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ImageRGBToYUV/

Color

# ImageRGBToYUV - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ImageRGBToYUV node converts an RGB image into YUV-style color components using an RGB-to-YCbCr color conversion.

Copy pageCopy page

The ImageRGBToYUV node converts an RGB image into YUV-style color components using an RGB-to-YCbCr color conversion. It splits the result into three separate images — Y (luminance, or brightness), U (blue-difference chroma), and V (red-difference chroma) — and returns each component at the same width and height as the input.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The input RGB image to convert into Y, U, and V components. If the image contains an alpha channel, only the first three (RGB) channels are used.| IMAGE| Yes| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`Y`| The luminance (brightness) component of the YUV color space, returned as a three-channel image| IMAGE  
`U`| The blue-difference chroma component of the YUV color space, returned as a three-channel image| IMAGE  
`V`| The red-difference chroma component of the YUV color space, returned as a three-channel image| IMAGE  
  
Each output has the same width and height as the input image. The corresponding Y, U, or V component is repeated across all three channels so that every output is returned as a standard three-channel image.

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageRGBToYUV/en.md)

* * *

**Source fingerprint (SHA-256):** `1a75ce64dfaec316a8f4b3a210cede388c9ba12d3ab3ec5ec14b0027be383744`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ImageRGBToYUV.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ImageRGBToYUV)

[ImageColorSpace - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ImageColorSpace)[ImageSDRToHDR - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ImageSDRToHDR)

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
