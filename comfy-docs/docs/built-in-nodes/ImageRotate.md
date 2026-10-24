---
url: https://docs.comfy.org/built-in-nodes/ImageRotate/
title: ImageRotate - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-24T11:54:50.809655+00:00
---

# ImageRotate - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ImageRotate/

Transform

# ImageRotate - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ImageRotate node rotates an input image by specified angles.

Copy pageCopy page

The ImageRotate node rotates an input image by specified angles. It supports four rotation options: no rotation, 90 degrees clockwise, 180 degrees, and 270 degrees clockwise. The rotation is performed using efficient tensor operations that maintain the image data integrity.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The input image to be rotated| IMAGE| Yes| -  
`rotation`| The rotation angle to apply to the image (default: “none”)| STRING| Yes| ”none"  
"90 degrees"  
"180 degrees"  
"270 degrees”  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The rotated output image| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageRotate/en.md)

* * *

**Source fingerprint (SHA-256):** `1de36d9e42e64fe80cc13dd7da96bd946f02ba78d81317f073cf54c4e5bd12f7`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ImageRotate.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ImageRotate)

[ImagePadForOutpaint](https://docs.comfy.org/built-in-nodes/ImagePadForOutpaint)[ImageStitch](https://docs.comfy.org/built-in-nodes/ImageStitch)
