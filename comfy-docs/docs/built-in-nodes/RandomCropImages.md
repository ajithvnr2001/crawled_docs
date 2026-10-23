---
url: https://docs.comfy.org/built-in-nodes/RandomCropImages/
title: RandomCropImages - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:46.507196+00:00
---

# RandomCropImages - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/RandomCropImages/

Transform

# RandomCropImages - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Random Crop Images node randomly selects a rectangular section from each input image and crops it to a specified width and height.

Copy pageCopy page

The Random Crop Images node randomly selects a rectangular section from each input image and crops it to a specified width and height. This is commonly used for data augmentation to create variations of training images. The random position for the crop is determined by a seed value, ensuring the same crop can be reproduced.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The image to be cropped.| IMAGE| Yes| -  
`width`| The width of the crop area (default: 512).| INT| No| 1 - 8192  
`height`| The height of the crop area (default: 512).| INT| No| 1 - 8192  
`seed`| A number used to control the random position of the crop (default: 0).| INT| No| 0 - 18446744073709551615  
  
**Note:** The `width` and `height` parameters must be less than or equal to the dimensions of the input image. If a specified dimension is larger than the image, the crop will be limited to the image’s boundary.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The resulting image after the random crop has been applied.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RandomCropImages/en.md)

* * *

**Source fingerprint (SHA-256):** `8452a07a1cf66a520fb482f5239df3f33cfe3a77a28e289894ccd1d2544ecf40`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/RandomCropImages.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/RandomCropImages)

[ImageStitch - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ImageStitch)[ResizeAndPadImage - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ResizeAndPadImage)

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
