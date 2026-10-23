---
url: https://docs.comfy.org/built-in-nodes/ImageScale/
title: ImageScale - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:10.653240+00:00
---

# ImageScale - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ImageScale/

Upscaling

# ImageScale - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ImageScale node is designed for resizing images to specific dimensions, offering a selection of upscale methods and the ability to crop the resized image.

Copy pageCopy page

The ImageScale node is designed for resizing images to specific dimensions, offering a selection of upscale methods and the ability to crop the resized image. It abstracts the complexity of image upscaling and cropping, providing a straightforward interface for modifying image dimensions according to user-defined parameters.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`image`| The input image to be upscaled. This parameter is central to the node’s operation, serving as the primary data upon which resizing transformations are applied. The quality and dimensions of the output image are directly influenced by the original image’s properties.| `IMAGE`  
`upscale_method`| Specifies the method used for upscaling the image. The choice of method can affect the quality and characteristics of the upscaled image, influencing the visual fidelity and potential artifacts in the resized output.| COMBO[STRING]  
`width`| The target width for the upscaled image. This parameter directly influences the dimensions of the output image, determining the horizontal scale of the resizing operation.| `INT`  
`height`| The target height for the upscaled image. This parameter directly influences the dimensions of the output image, determining the vertical scale of the resizing operation.| `INT`  
`crop`| Determines whether and how the upscaled image should be cropped, offering options for disabled cropping or center cropping. This affects the final composition of the image by potentially removing edges to fit the specified dimensions.| COMBO[STRING]  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`image`| The upscaled (and optionally cropped) image, ready for further processing or visualization.| `IMAGE`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScale/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ImageScale.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ImageScale)

[ResizeImagesByShorterEdge - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ResizeImagesByShorterEdge)[ImageScaleBy - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ImageScaleBy)

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
