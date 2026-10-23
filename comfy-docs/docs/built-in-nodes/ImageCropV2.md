---
url: https://docs.comfy.org/built-in-nodes/ImageCropV2/
title: ImageCropV2 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-23T16:38:44.114991+00:00
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

[ImageCropToMask](https://docs.comfy.org/built-in-nodes/ImageCropToMask)[ImageFlip](https://docs.comfy.org/built-in-nodes/ImageFlip)
