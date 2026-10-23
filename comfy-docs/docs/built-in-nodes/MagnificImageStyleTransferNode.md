---
url: https://docs.comfy.org/built-in-nodes/MagnificImageStyleTransferNode/
title: MagnificImageStyleTransferNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:28.869628+00:00
---

# MagnificImageStyleTransferNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MagnificImageStyleTransferNode/

Magnific

# MagnificImageStyleTransferNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node applies the visual style from a reference image to your input image.

Copy pageCopy page

This node applies the visual style from a reference image to your input image. It uses an external AI service to process the images, allowing you to control the strength of the style transfer and the preservation of the original image’s structure.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The image to apply style transfer to.| IMAGE| Yes| -  
`reference_image`| The reference image to extract style from.| IMAGE| Yes| -  
`prompt`| An optional text prompt to guide the style transfer.| STRING| No| -  
`style_strength`| Percentage of style strength (default: 100).| INT| No| 0 to 100  
`structure_strength`| Maintains the structure of the original image (default: 50).| INT| No| 0 to 100  
`flavor`| Style transfer flavor.| COMBO| No| ”faithful"  
"gen_z"  
"psychedelia"  
"detaily"  
"clear"  
"donotstyle"  
"donotstyle_sharp”  
`engine`| Processing engine selection.| COMBO| No| ”balanced"  
"definio"  
"illusio"  
"3d_cartoon"  
"colorful_anime"  
"caricature"  
"real"  
"super_real"  
"softy”  
`portrait_mode`| Enable portrait mode for facial enhancements.| COMBO| No| ”disabled"  
"enabled”  
`portrait_style`| Visual style applied to portrait images. This input is only available when `portrait_mode` is set to “enabled”.| COMBO| No| ”standard"  
"pop"  
"super_pop”  
`portrait_beautifier`| Facial beautification intensity on portraits. This input is only available when `portrait_mode` is set to “enabled”.| COMBO| No| ”none"  
"beautify_face"  
"beautify_face_max”  
`fixed_generation`| When disabled, expect each generation to introduce a degree of randomness, leading to more diverse outcomes (default: True).| BOOLEAN| No| -  
  
**Constraints:**

  * Exactly one `image` and one `reference_image` are required.
  * Both images must have an aspect ratio between 1:3 and 3:1.
  * Both images must have a minimum height and width of 160 pixels.
  * The `portrait_style` and `portrait_beautifier` parameters are only active when `portrait_mode` is set to “enabled”.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The resulting image after style transfer has been applied.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageStyleTransferNode/en.md)

* * *

**Source fingerprint (SHA-256):** `edffec024ebe7cbf7c42008e14c1b99d6fafcf5b9da62b0b560d194a585dc9ad`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MagnificImageStyleTransferNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MagnificImageStyleTransferNode)

[MagnificImageSkinEnhancerNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/MagnificImageSkinEnhancerNode)[MagnificImageUpscalerCreativeNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/MagnificImageUpscalerCreativeNode)

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
