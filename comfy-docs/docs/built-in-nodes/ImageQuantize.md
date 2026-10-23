---
url: https://docs.comfy.org/built-in-nodes/ImageQuantize/
title: ImageQuantize - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:10.365543+00:00
---

# ImageQuantize - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ImageQuantize/

Filters

# ImageQuantize - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ImageQuantize node is designed to reduce the number of colors in an image to a specified number

Copy pageCopy page

The ImageQuantize node is designed to reduce the number of colors in an image to a specified number, optionally applying dithering techniques to maintain visual quality. This process is useful for creating palette-based images or reducing the color complexity for certain applications.

## 

​

Inputs

Field| Description| Data Type  
---|---|---  
`image`| The input image tensor to be quantized. It affects the node’s execution by being the primary data upon which color reduction is performed.| `IMAGE`  
`colors`| Specifies the number of colors to reduce the image to. It directly influences the quantization process by determining the color palette size.| `INT`  
`dither`| Determines the dithering technique to be applied during quantization, affecting the visual quality and appearance of the output image.| COMBO[STRING]  
  
## 

​

Outputs

Field| Description| Data Type  
---|---|---  
`image`| The quantized version of the input image, with reduced color complexity and optionally dithered to maintain visual quality.| `IMAGE`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageQuantize/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ImageQuantize.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ImageQuantize)

[ImageBlur - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ImageBlur)[ImageSharpen - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ImageSharpen)

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
