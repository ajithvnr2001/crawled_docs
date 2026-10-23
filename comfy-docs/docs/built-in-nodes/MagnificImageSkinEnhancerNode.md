---
url: https://docs.comfy.org/built-in-nodes/MagnificImageSkinEnhancerNode/
title: MagnificImageSkinEnhancerNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:28.538019+00:00
---

# MagnificImageSkinEnhancerNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MagnificImageSkinEnhancerNode/

Magnific

# MagnificImageSkinEnhancerNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Magnific Image Skin Enhancer node applies specialized AI processing to portrait images to improve skin appearance.

Copy pageCopy page

The Magnific Image Skin Enhancer node applies specialized AI processing to portrait images to improve skin appearance. It offers three distinct modes for different enhancement goals: creative for artistic effects, faithful for preserving the original look, and flexible for targeted improvements like lighting or realism. The node uploads the image to an external API for processing and returns the enhanced result.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The portrait image to enhance.| IMAGE| Yes| -  
`sharpen`| Sharpening intensity level (default: 0).| INT| No| 0 to 100  
`smart_grain`| Smart grain intensity level (default: 2).| INT| No| 0 to 100  
`mode`| The processing mode to use. `"creative"` is for artistic enhancement, `"faithful"` for preserving the original appearance, and `"flexible"` for targeted optimization.| COMBO| Yes| `"creative"`  
`"faithful"`  
`"flexible"`  
`skin_detail`| Skin detail enhancement level. This input is only available when the `mode` is set to `"faithful"` (default: 80).| INT| No| 0 to 100  
`optimized_for`| Enhancement optimization target. This input is only available when the `mode` is set to `"flexible"`.| COMBO| No| `"enhance_skin"`  
`"improve_lighting"`  
`"enhance_everything"`  
`"transform_to_real"`  
`"no_make_up"`  
  
**Constraints:**

  * The node accepts exactly one input image.
  * The input image must have a minimum height and width of 160 pixels.
  * The input image aspect ratio must be between 1:3 and 3:1 (non-strict validation).
  * The `skin_detail` parameter is only active when `mode` is set to `"faithful"`.
  * The `optimized_for` parameter is only active when `mode` is set to `"flexible"`.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The enhanced portrait image.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageSkinEnhancerNode/en.md)

* * *

**Source fingerprint (SHA-256):** `2430cc0fb1d2042a8eda78f7f5a5794fa6b4e555d3957616ae6891374b556a76`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MagnificImageSkinEnhancerNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MagnificImageSkinEnhancerNode)

[MagnificImageRelightNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/MagnificImageRelightNode)[MagnificImageStyleTransferNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/MagnificImageStyleTransferNode)

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
