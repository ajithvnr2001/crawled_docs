---
url: https://docs.comfy.org/built-in-nodes/MagnificImageUpscalerCreativeNode/
title: MagnificImageUpscalerCreativeNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:28.938599+00:00
---

# MagnificImageUpscalerCreativeNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MagnificImageUpscalerCreativeNode/

Magnific

# MagnificImageUpscalerCreativeNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node uses the Magnific AI service to upscale and creatively enhance an image.

Copy pageCopy page

This node uses the Magnific AI service to upscale and creatively enhance an image. It allows you to guide the enhancement with a text prompt, choose a specific style to optimize for, and control various aspects of the creative process like detail, resemblance to the original, and stylization strength. The node outputs an upscaled image at your chosen factor (2x, 4x, 8x, or 16x), with a maximum output size of 25.3 megapixels.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The input image to be upscaled and enhanced.| IMAGE| Yes| -  
`prompt`| A text description to guide the creative enhancement of the image. Default is an empty string (no prompt is sent in that case).| STRING| Yes| -  
`scale_factor`| The factor by which to upscale the image’s dimensions.| COMBO| Yes| `"2x"`  
`"4x"`  
`"8x"`  
`"16x"`  
`optimized_for`| The style or content type to optimize the enhancement process for.| COMBO| Yes| `"standard"`  
`"soft_portraits"`  
`"hard_portraits"`  
`"art_n_illustration"`  
`"videogame_assets"`  
`"nature_n_landscapes"`  
`"films_n_photography"`  
`"3d_renders"`  
`"science_fiction_n_horror"`  
`creativity`| Controls the level of creative interpretation applied to the image (default: 0).| INT| Yes| -10 to 10  
`hdr`| The level of definition and detail (default: 0).| INT| Yes| -10 to 10  
`resemblance`| The level of resemblance to the original image (default: 0).| INT| Yes| -10 to 10  
`fractality`| The strength of the prompt and intricacy per square pixel (default: 0).| INT| Yes| -10 to 10  
`engine`| The specific AI engine to use for processing. This is an advanced parameter.| COMBO| Yes| `"automatic"`  
`"magnific_illusio"`  
`"magnific_sharpy"`  
`"magnific_sparkle"`  
`auto_downscale`| Automatically downscale input image if output would exceed maximum pixel limit (default: False). This is an advanced parameter.| BOOLEAN| Yes| -  
  
**Constraints:**

  * The input `image` must be exactly one image.
  * The input image must have a minimum height and width of 160 pixels.
  * The input image’s aspect ratio must be between 1:3 and 3:1.
  * The final output size (input dimensions multiplied by the `scale_factor`) cannot exceed 25,300,000 pixels. If this limit would be exceeded: 
    * When `auto_downscale` is enabled, the node automatically reduces the input image size (the additional downscaling is kept to at most 2x) or uses a lower `scale_factor` so the output stays within the limit.
    * When `auto_downscale` is disabled, the node raises an error.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The creatively enhanced and upscaled output image.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageUpscalerCreativeNode/en.md)

* * *

**Source fingerprint (SHA-256):** `36c38e87f9f1e568c78cf794aeb0a268c6d25d639006eb2cf18ee040d3071ad4`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MagnificImageUpscalerCreativeNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MagnificImageUpscalerCreativeNode)

[MagnificImageStyleTransferNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/MagnificImageStyleTransferNode)[MagnificImageUpscalerPreciseV2Node - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/MagnificImageUpscalerPreciseV2Node)

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
