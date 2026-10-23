---
url: https://docs.comfy.org/built-in-nodes/TripoSplatPreprocessImage/
title: TripoSplatPreprocessImage - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:14.411852+00:00
---

# TripoSplatPreprocessImage - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/TripoSplatPreprocessImage/

Triposplat

# TripoSplatPreprocessImage - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node crops each input image to a centered square on a black background and adds padding to reach the specified output size.

Copy pageCopy page

This node crops each input image to a centered square on a black background and adds padding to reach the specified output size. It is designed to prepare images for the TripoSplat 3D model by ensuring consistent square framing and optional alpha matte erosion to prevent border artifacts.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The input image(s) to preprocess.| IMAGE| Yes| -  
`mask`| Alpha mask for the image, used to determine the crop region.| MASK| Yes| -  
`erode_radius`| Erode the alpha matte by this pixel radius before cropping (avoids border bleed). Default: 1. Set to 0 to disable erosion.| INT| Yes| 0 to 16  
`size`| Square image size. The model is trained at 1024; other sizes run but are off-distribution. Default: 1024.| INT| Yes| 256 to 4096 (step of 16)  
  
**Note:** The `mask` input is required and must be provided. If the mask has a different batch size than the image, it is automatically repeated to match. If the mask dimensions differ from the image dimensions, the mask is resized to match the image using bilinear interpolation. The output size is automatically rounded down to the nearest multiple of 16 (minimum 16) to ensure compatibility with DINOv3 patch and Flux2 VAE stride requirements. The node raises an error if the mask contains no foreground pixels (empty mask). When `erode_radius` is 0, no erosion is applied. The square crop is centered on the mask’s alpha bounding box and sized to 1.2 times the larger bounding box dimension; any area outside the image bounds is filled with black.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The preprocessed image(s) cropped to a centered square on a black background with padding, at the requested `size` resolution.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatPreprocessImage/en.md)

* * *

**Source fingerprint (SHA-256):** `ec66941846398ee6637576b11ae9d2f9576f6b05ed2ef730cdbf99a68fe9b838`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/TripoSplatPreprocessImage.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/TripoSplatPreprocessImage)

[TripoSplatConditioning - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/TripoSplatConditioning)[VOIDInpaintConditioning - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/VOIDInpaintConditioning)

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
