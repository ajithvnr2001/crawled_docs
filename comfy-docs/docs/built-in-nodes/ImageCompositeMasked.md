---
url: https://docs.comfy.org/built-in-nodes/ImageCompositeMasked/
title: ImageCompositeMasked - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:07.773056+00:00
---

# ImageCompositeMasked - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ImageCompositeMasked/

Compositing

# ImageCompositeMasked - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ImageCompositeMasked node is designed for compositing images

Copy pageCopy page

The `ImageCompositeMasked` node is designed for compositing images, allowing for the overlay of a source image onto a destination image at specified coordinates, with optional resizing and masking.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`destination`| The destination image onto which the source image will be composited. It serves as the background for the composite operation.| `IMAGE`  
`source`| The source image to be composited onto the destination image. This image can optionally be resized to fit the destination image’s dimensions.| `IMAGE`  
`x`| The x-coordinate in the destination image where the top-left corner of the source image will be placed.| `INT`  
`y`| The y-coordinate in the destination image where the top-left corner of the source image will be placed.| `INT`  
`resize_source`| A boolean flag indicating whether the source image should be resized to match the destination image’s dimensions.| `BOOLEAN`  
`mask`| An optional mask that specifies which parts of the source image should be composited onto the destination image. This allows for more complex compositing operations, such as blending or partial overlays.| `MASK`  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`image`| The resulting image after the compositing operation, which combines elements of both t| `IMAGE`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCompositeMasked/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ImageCompositeMasked.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ImageCompositeMasked)

[NormalizeImages - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/NormalizeImages)[JoinImageWithAlpha - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/JoinImageWithAlpha)

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
