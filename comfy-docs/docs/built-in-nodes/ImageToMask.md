---
url: https://docs.comfy.org/built-in-nodes/ImageToMask/
title: ImageToMask - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:11.706107+00:00
---

# ImageToMask - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ImageToMask/

Mask

# ImageToMask - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ImageToMask node is designed to convert an image into a mask based on a specified color channel.

Copy pageCopy page

The ImageToMask node is designed to convert an image into a mask based on a specified color channel. It allows for the extraction of mask layers corresponding to the red, green, blue, or alpha channels of an image, facilitating operations that require channel-specific masking or processing.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`image`| The ‘image’ parameter represents the input image from which a mask will be generated based on the specified color channel. It plays a crucial role in determining the content and characteristics of the resulting mask.| `IMAGE`  
`channel`| The ‘channel’ parameter specifies which color channel (red, green, blue, or alpha) of the input image should be used to generate the mask. This choice directly influences the mask’s appearance and which parts of the image are highlighted or masked out.| COMBO[STRING]  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`mask`| The output ‘mask’ is a binary or grayscale representation of the specified color channel from the input image, useful for further image processing or masking operations.| `MASK`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageToMask/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ImageToMask.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ImageToMask)

[ImageColorToMask - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ImageColorToMask)[InvertMask - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/InvertMask)

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
