---
url: https://docs.comfy.org/built-in-nodes/ImagePadForOutpaint/
title: ImagePadForOutpaint - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:10.524975+00:00
---

# ImagePadForOutpaint - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ImagePadForOutpaint/

Transform

# ImagePadForOutpaint - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node is designed for preparing images for the outpainting process by adding padding around them.

Copy pageCopy page

This node is designed for preparing images for the outpainting process by adding padding around them. It adjusts the image dimensions to ensure compatibility with outpainting algorithms, facilitating the generation of extended image areas beyond the original boundaries.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`image`| The ‘image’ input is the primary image to be prepared for outpainting, serving as the base for padding operations.| `IMAGE`  
`left`| Specifies the amount of padding to add to the left side of the image, influencing the expanded area for outpainting.| `INT`  
`top`| Determines the amount of padding to add to the top of the image, affecting the vertical expansion for outpainting.| `INT`  
`right`| Defines the amount of padding to add to the right side of the image, impacting the horizontal expansion for outpainting.| `INT`  
`bottom`| Indicates the amount of padding to add to the bottom of the image, contributing to the vertical expansion for outpainting.| `INT`  
`feathering`| Controls the smoothness of the transition between the original image and the added padding, enhancing the visual integration for outpainting.| `INT`  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`image`| The output ‘image’ represents the padded image, ready for the outpainting process.| `IMAGE`  
`mask`| The output ‘mask’ indicates the areas of the original image and the added padding, useful for guiding the outpainting algorithms.| `MASK`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImagePadForOutpaint/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ImagePadForOutpaint.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ImagePadForOutpaint)

[ImageFlip - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ImageFlip)[ImageRotate - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ImageRotate)

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
