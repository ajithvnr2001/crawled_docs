---
url: https://docs.comfy.org/built-in-nodes/CenterCropImages/
title: CenterCropImages - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:34.357405+00:00
---

# CenterCropImages - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/CenterCropImages/

Transform

# CenterCropImages - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Center Crop Images node crops an image from its center to a specified width and height.

Copy pageCopy page

The Center Crop Images node crops an image from its center to a specified width and height. It calculates the central region of the input image and extracts a rectangular area of the defined dimensions. If the requested crop size is larger than the image, the crop will be constrained to the image’s boundaries.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The input image to be cropped.| IMAGE| Yes| -  
`width`| The width of the crop area (default: 512).| INT| Yes| 1 to 8192  
`height`| The height of the crop area (default: 512).| INT| Yes| 1 to 8192  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The resulting image after the center crop operation.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CenterCropImages/en.md)

* * *

**Source fingerprint (SHA-256):** `1b22529602e3aca816b583158c4bb5aa51de3478ac8068c2a69a3392fb12746f`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/CenterCropImages.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/CenterCropImages)

[GLSLShader - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/GLSLShader)[CropByBBoxes - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/CropByBBoxes)

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
