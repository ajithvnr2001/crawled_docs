---
url: https://docs.comfy.org/built-in-nodes/ImageCropV2/
title: ImageCropV2 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:08.711225+00:00
---

# ImageCropV2 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ImageCropV2/

Transform

# ImageCropV2 - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Crop Image node extracts a rectangular section from an input image.

Copy pageCopy page

The Crop Image node extracts a rectangular section from an input image. You define the region to keep by specifying its top-left corner coordinates and its width and height. The node then returns the cropped portion of the original image.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The input image to be cropped.| IMAGE| Yes| N/A  
`crop_region`| Defines the rectangular area to extract from the image. It is specified by `x` (horizontal start), `y` (vertical start), `width`, and `height`. If the defined region extends beyond the image’s borders, it will be automatically adjusted to fit within the image dimensions.| BOUNDINGBOX| Yes| N/A  
  
**Note on Region Constraints:** The crop region is automatically constrained to stay within the bounds of the input image. If the specified `x` or `y` coordinate is greater than the image’s width or height, it will be set to the maximum valid position. The resulting crop width and height will be adjusted so the region does not exceed the image’s edges.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The cropped section of the original input image.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCropV2/en.md)

* * *

**Source fingerprint (SHA-256):** `c09c68a46c4b0418903a627b98dd848264d53b58bd3ffe99e40ef125b15b3aae`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ImageCropV2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ImageCropV2)

[ImageCropToMask - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ImageCropToMask)[ImageFlip - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ImageFlip)

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
