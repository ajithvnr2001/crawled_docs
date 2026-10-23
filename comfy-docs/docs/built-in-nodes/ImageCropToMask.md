---
url: https://docs.comfy.org/built-in-nodes/ImageCropToMask/
title: ImageCropToMask - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:08.018201+00:00
---

# ImageCropToMask - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ImageCropToMask/

Transform

# ImageCropToMask - ComfyUI Built-in Node Documentation

Copy pageCopy page

Crops an image to the bounding box of its mask, producing a centered subject over a solid background color.

Copy pageCopy page

Crops an image to the bounding box of its mask, producing a centered subject over a solid background color. The node composites the masked image over the chosen background and resizes the result to the specified output dimensions, making it suitable for 3D pipelines that expect a centered, background-free subject at a fixed resolution.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`images`| The input image or batch of images to crop.| IMAGE| Yes| —  
`masks`| The mask or batch of masks that defines the subject area. A single mask is applied to all images; otherwise the mask batch size must match the image batch size. If the mask resolution differs from the image resolution, the mask is automatically resized to match.| MASK| Yes| —  
`width`| Output width in pixels. (default: 1024)| INT| Yes| 64 to 4096 (step 8)  
`height`| Output height in pixels. (default: 1024)| INT| Yes| 64 to 4096 (step 8)  
`pad_factor`| Extra margin around the mask bounding box as a multiplier. (default: 1.0)| FLOAT| Yes| 1.0 to 2.0 (step 0.01)  
`grow_mask`| Grow or shrink the mask by this many pixels before cropping. Positive values expand the mask, negative values shrink it. (default: 0)| INT| Yes| -32 to 32 (step 1)  
`background`| Background color behind the masked subject. (default: #000000)| COLOR| Yes| —  
  
Note: The crop region is centered on the mask’s bounding box and its aspect ratio matches `width` / `height`. The node automatically detects and corrects an inverted mask (foreground pixels along the border, background in the center). If the mask contains no foreground pixels, the node tries the inverted mask; if that is also empty, it logs a warning and crops the entire image. An error is raised when the mask batch size does not match the image batch size and is not a single mask.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`images`| The cropped composite images (masked subject over the chosen background color), resized to `width` x `height`. The batch size matches the input image batch.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCropToMask/en.md)

* * *

**Source fingerprint (SHA-256):** `fcc14b5db7318699526dd544d404f78f9d1ab362b73769276f113f2b1062b214`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ImageCropToMask.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ImageCropToMask)

[ImageCrop - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ImageCrop)[ImageCropV2 - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ImageCropV2)

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
