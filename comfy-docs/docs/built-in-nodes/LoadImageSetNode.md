---
url: https://docs.comfy.org/built-in-nodes/LoadImageSetNode/
title: LoadImageSetNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-24T11:54:50.013371+00:00
---

# LoadImageSetNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LoadImageSetNode/

Image

# LoadImageSetNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The LoadImageSetNode loads multiple images from the input directory for batch processing and training purposes.

Copy pageCopy page

The LoadImageSetNode loads multiple images from the input directory for batch processing and training purposes. It supports various image formats and can optionally resize the images using different methods. This node processes all selected images as a batch and returns them as a single tensor.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`images`| Select multiple images from the input directory. Supports PNG, JPG, JPEG, WEBP, BMP, GIF, JPE, APNG, TIF, and TIFF formats. Allows batch selection of images.| IMAGE| Yes| Multiple image files  
`resize_method`| Optional method to resize loaded images (default: “None”). Choose “None” to keep original sizes, “Stretch” to force resize, “Crop” to maintain aspect ratio by cropping, or “Pad” to maintain aspect ratio by adding padding.| STRING| No| ”None"  
"Stretch"  
"Crop"  
"Pad”  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| A tensor containing all loaded images as a batch for further processing.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageSetNode/en.md)

* * *

**Source fingerprint (SHA-256):** `acf0255bcf170ef3ac3b86a3f3e060c3b81064ca8924918a026ec8e3b86f7ac0`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LoadImageSetNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LoadImageSetNode)

[LoadImageSetFromFolderNode](https://docs.comfy.org/built-in-nodes/LoadImageSetFromFolderNode)[LoadImageTextDataSetFromFolder](https://docs.comfy.org/built-in-nodes/LoadImageTextDataSetFromFolder)
