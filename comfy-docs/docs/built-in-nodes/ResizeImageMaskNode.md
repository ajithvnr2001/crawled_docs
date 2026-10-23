---
url: https://docs.comfy.org/built-in-nodes/ResizeImageMaskNode/
title: ResizeImageMaskNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:51.259084+00:00
---

# ResizeImageMaskNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ResizeImageMaskNode/

Image

# ResizeImageMaskNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Resize Image/Mask node provides multiple methods to change the dimensions of an input image or mask.

Copy pageCopy page

The Resize Image/Mask node provides multiple methods to change the dimensions of an input image or mask. It can scale by a multiplier, set specific dimensions, match the size of another input, or adjust based on pixel count, using various interpolation methods for quality.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`input`| The image or mask to be resized.| IMAGE or MASK| Yes| N/A  
`resize_type`| The method used to determine the new size. The required parameters change based on the selected type.| COMBO| Yes| `SCALE_BY`  
`SCALE_DIMENSIONS`  
`SCALE_LONGER_DIMENSION`  
`SCALE_SHORTER_DIMENSION`  
`SCALE_WIDTH`  
`SCALE_HEIGHT`  
`SCALE_TOTAL_PIXELS`  
`MATCH_SIZE`  
`multiplier`| The scaling factor. Required when `resize_type` is `SCALE_BY` (default: 1.00).| FLOAT| No| 0.01 to 8.0  
`width`| The target width in pixels. Required when `resize_type` is `SCALE_DIMENSIONS` or `SCALE_WIDTH` (default: 512).| INT| No| 0 to 8192  
`height`| The target height in pixels. Required when `resize_type` is `SCALE_DIMENSIONS` or `SCALE_HEIGHT` (default: 512).| INT| No| 0 to 8192  
`crop`| The cropping method to apply when dimensions don’t match the aspect ratio. Only available when `resize_type` is `SCALE_DIMENSIONS` or `MATCH_SIZE` (default: “center”).| COMBO| No| `"disabled"`  
`"center"`  
`longer_size`| The target size for the longer side of the image. Required when `resize_type` is `SCALE_LONGER_DIMENSION` (default: 512).| INT| No| 0 to 8192  
`shorter_size`| The target size for the shorter side of the image. Required when `resize_type` is `SCALE_SHORTER_DIMENSION` (default: 512).| INT| No| 0 to 8192  
`megapixels`| The target total number of megapixels. Required when `resize_type` is `SCALE_TOTAL_PIXELS` (default: 1.0).| FLOAT| No| 0.01 to 16.0  
`match`| An image or mask whose dimensions the input will be resized to match. Required when `resize_type` is `MATCH_SIZE`.| IMAGE or MASK| No| N/A  
`scale_method`| The interpolation algorithm used for scaling (default: “area”).| COMBO| Yes| `"nearest-exact"`  
`"bilinear"`  
`"area"`  
`"bicubic"`  
`"lanczos"`  
  
**Note:** The `crop` parameter is only available and relevant when the `resize_type` is set to `SCALE_DIMENSIONS` or `MATCH_SIZE`. When using `SCALE_WIDTH` or `SCALE_HEIGHT`, the other dimension is automatically scaled to maintain the original aspect ratio.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`resized`| The resized image or mask, matching the data type of the input.| IMAGE or MASK  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeImageMaskNode/en.md)

* * *

**Source fingerprint (SHA-256):** `9ac0b153608ac971bb11d9d12ebd1f0f4d6e926604e8727a1bc3a311d95fbc03`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ResizeImageMaskNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ResizeImageMaskNode)

[PreviewImage - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/PreviewImage)[SaveAnimatedPNG - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SaveAnimatedPNG)

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
