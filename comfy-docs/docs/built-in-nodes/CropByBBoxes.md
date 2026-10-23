---
url: https://docs.comfy.org/built-in-nodes/CropByBBoxes/
title: CropByBBoxes - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:49.563066+00:00
---

# CropByBBoxes - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/CropByBBoxes/

Transform

# CropByBBoxes - ComfyUI Built-in Node Documentation

Copy pageCopy page

The CropByBBoxes node extracts and resizes specific rectangular regions from an input image batch.

Copy pageCopy page

The CropByBBoxes node extracts and resizes specific rectangular regions from an input image batch. It uses provided bounding box coordinates to define the area to crop from each image. The cropped regions are then resized to a specified output dimension, with options to either stretch the crop or pad it to preserve its original aspect ratio.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The input batch of images to crop.| IMAGE| Yes| -  
`bboxes`| The list of bounding boxes defining the regions to crop. This input is forced, meaning it must be connected.| BOUNDINGBOX| Yes| -  
`output_width`| The width each crop is resized to (default: 512).| INT| No| 64 - 4096  
`output_height`| The height each crop is resized to (default: 512).| INT| No| 64 - 4096  
`padding`| Extra padding in pixels added on each side of the bounding box before cropping (default: 0).| INT| No| 0 - 1024  
`keep_aspect`| Whether to stretch the crop to fit the output size, or pad with black pixels to preserve its aspect ratio (default: “stretch”).| COMBO| No| `"stretch"`  
`"pad"`  
  
**Note:** The node processes one image frame at a time. If multiple bounding boxes are provided for a single frame, it calculates a single crop region that is the union (the smallest rectangle containing all boxes) of all provided boxes. If a calculated crop region is invalid (e.g., zero width or height), the node will create a fallback crop from the center-top of the image.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| All cropped and resized regions, stacked into a single image batch.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CropByBBoxes/en.md)

* * *

**Source fingerprint (SHA-256):** `7524d629e61f5af2475f819bc9431d4f4173feb5ad59f9bcf81d822330fb3e22`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/CropByBBoxes.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/CropByBBoxes)

[CenterCropImages - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/CenterCropImages)[ImageCrop - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ImageCrop)

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
