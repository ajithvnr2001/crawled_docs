---
url: https://docs.comfy.org/built-in-nodes/ImageFlip/
title: ImageFlip - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-23T16:38:44.314767+00:00
---

# ImageFlip - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ImageFlip/

Transform

# ImageFlip - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ImageFlip node flips images along different axes.

Copy pageCopy page

The ImageFlip node flips images along different axes. It can flip images vertically along the x-axis or horizontally along the y-axis. The node uses torch.flip operations to perform the flipping based on the selected method.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The input image to be flipped| IMAGE| Yes| -  
`flip_method`| The flipping direction to apply (default: “x-axis: vertically”)| STRING| Yes| ”x-axis: vertically"  
"y-axis: horizontally”  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The flipped output image| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageFlip/en.md)

* * *

**Source fingerprint (SHA-256):** `481cd167d57746f242fcc4b5f2e3bb0bff0184b5870626d5f24a34422464ddd6`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ImageFlip.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ImageFlip)

[ImageCropV2](https://docs.comfy.org/built-in-nodes/ImageCropV2)[ImagePadForOutpaint](https://docs.comfy.org/built-in-nodes/ImagePadForOutpaint)
