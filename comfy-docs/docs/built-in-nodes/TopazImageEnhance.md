---
url: https://docs.comfy.org/built-in-nodes/TopazImageEnhance/
title: TopazImageEnhance - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:10.598308+00:00
---

# TopazImageEnhance - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/TopazImageEnhance/

Topaz

# TopazImageEnhance - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Topaz Image Enhance node provides industry-standard upscaling and image enhancement.

Copy pageCopy page

The Topaz Image Enhance node provides industry-standard upscaling and image enhancement. It processes a single input image using a cloud-based AI model to improve quality, detail, and resolution. The node offers fine-grained control over the enhancement process, including options for creative guidance, subject focus, and facial preservation. This node is a legacy version and is marked as deprecated in the interface.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The AI model to use for image enhancement.| COMBO| Yes| `"Reimagine"`  
`image`| The input image to be enhanced. Only one image is supported.| IMAGE| Yes| -  
`prompt`| Optional text prompt for creative upscaling guidance (default: empty).| STRING| No| -  
`subject_detection`| Controls which part of the image the enhancement focuses on (default: “All”).| COMBO| No| `"All"`  
`"Foreground"`  
`"Background"`  
`face_enhancement`| Enhance faces (if present) during processing (default: True).| BOOLEAN| No| -  
`face_enhancement_creativity`| Set the creativity level for face enhancement (default: 0.0).| FLOAT| No| 0.0 - 1.0  
`face_enhancement_strength`| Controls how sharp enhanced faces are relative to the background (default: 1.0).| FLOAT| No| 0.0 - 1.0  
`crop_to_fill`| By default, the image is letterboxed when the output aspect ratio differs. Enable to crop the image to fill the output dimensions (default: False).| BOOLEAN| No| -  
`output_width`| Zero value means to calculate automatically (usually it will be original size or output_height if specified) (default: 0).| INT| No| 0 - 32000  
`output_height`| Zero value means to output in the same height as original or output width (default: 0).| INT| No| 0 - 32000  
`creativity`| Controls the overall creativity level of the enhancement (default: 3).| INT| No| 1 - 9  
`face_preservation`| Preserve subjects’ facial identity (default: True).| BOOLEAN| No| -  
`color_preservation`| Preserve the original colors (default: True).| BOOLEAN| No| -  
  
**Note:** This node can only process a single input image. Providing a batch of multiple images will result in an error.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The enhanced output image.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhance/en.md)

* * *

**Source fingerprint (SHA-256):** `1a0e708cdea9ec4f92f7f3aaabbdeea06a8fdab2f91a45ad2dea15f2bc2e8fa3`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/TopazImageEnhance.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/TopazImageEnhance)

[HunyuanImageTextToImageApi - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/HunyuanImageTextToImageApi)[TopazImageEnhanceV2 - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/TopazImageEnhanceV2)

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
