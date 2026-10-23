---
url: https://docs.comfy.org/built-in-nodes/ImageCrop/
title: ImageCrop - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:08.931578+00:00
---

# ImageCrop - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ImageCrop/

Transform

# ImageCrop - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ImageCrop node is designed for cropping images to a specified width and height starting from a given x and y coordinate.

Copy pageCopy page

The `ImageCrop` node is designed for cropping images to a specified width and height starting from a given x and y coordinate. This functionality is essential for focusing on specific regions of an image or for adjusting the image size to meet certain requirements.

## 

​

Inputs

Field| Description| Data Type  
---|---|---  
`image`| The input image to be cropped. This parameter is crucial as it defines the source image from which a region will be extracted based on the specified dimensions and coordinates.| `IMAGE`  
`width`| Specifies the width of the cropped image. This parameter determines how wide the resulting cropped image will be.| `INT`  
`height`| Specifies the height of the cropped image. This parameter determines the height of the resulting cropped image.| `INT`  
`x`| The x-coordinate of the top-left corner of the cropping area. This parameter sets the starting point for the width dimension of the crop.| `INT`  
`y`| The y-coordinate of the top-left corner of the cropping area. This parameter sets the starting point for the height dimension of the crop.| `INT`  
  
## 

​

Outputs

Field| Description| Data Type  
---|---|---  
`image`| The cropped image as a result of the cropping operation. This output is significant for further processing or analysis of the specified image region.| `IMAGE`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCrop/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ImageCrop.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ImageCrop)

[CropByBBoxes - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/CropByBBoxes)[ImageCropToMask - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ImageCropToMask)

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
