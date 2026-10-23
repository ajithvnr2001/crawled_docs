---
url: https://docs.comfy.org/built-in-nodes/MagnificImageUpscalerPreciseV2Node/
title: MagnificImageUpscalerPreciseV2Node - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:28.726603+00:00
---

# MagnificImageUpscalerPreciseV2Node - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MagnificImageUpscalerPreciseV2Node/

Magnific

# MagnificImageUpscalerPreciseV2Node - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Magnific Image Upscale (Precise V2) node performs high-fidelity image upscaling with fine control over sharpness, grain, and detail enhancement.

Copy pageCopy page

The Magnific Image Upscale (Precise V2) node performs high-fidelity image upscaling with fine control over sharpness, grain, and detail enhancement. It processes images through an external API, supporting up to a maximum output resolution of 10060×10060 pixels. The node offers different processing styles and can automatically downscale the input if the requested output would exceed the maximum allowed size.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The input image to be upscaled. Exactly one image is required. Minimum dimensions are 160x160 pixels. The aspect ratio must be between 1:3 and 3:1.| IMAGE| Yes| -  
`scale_factor`| The desired upscaling multiplier.| COMBO| Yes| `"2x"`  
`"4x"`  
`"8x"`  
`"16x"`  
`flavor`| Processing style: sublime for general use, photo for photographs, photo_denoiser for noisy photos.| COMBO| Yes| `"sublime"`  
`"photo"`  
`"photo_denoiser"`  
`sharpen`| Image sharpness intensity. Higher values increase edge definition and clarity. Default: 7.| INT| Yes| 0 to 100  
`smart_grain`| Intelligent grain/texture enhancement to prevent the image from looking too smooth or artificial. Default: 7.| INT| Yes| 0 to 100  
`ultra_detail`| Controls fine detail, textures, and micro-details added during upscaling. Default: 30.| INT| Yes| 0 to 100  
`auto_downscale`| Automatically downscale input image if output would exceed maximum resolution. Default: False. This is an advanced setting.| BOOLEAN| Yes| -  
  
**Note:** If `auto_downscale` is disabled and the requested output size (input dimensions × `scale_factor`) exceeds 10060x10060 pixels, the node will raise an error. When `auto_downscale` is enabled, the node will attempt to find an optimal scale factor that keeps quality loss minimal.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The resulting upscaled image.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageUpscalerPreciseV2Node/en.md)

* * *

**Source fingerprint (SHA-256):** `aeb2b3569fd7b1d2417890586b8ac84ff921c4405f63f190188af93044ccfd28`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MagnificImageUpscalerPreciseV2Node.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MagnificImageUpscalerPreciseV2Node)

[MagnificImageUpscalerCreativeNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/MagnificImageUpscalerCreativeNode)[MetaMuseImageEditApi - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/MetaMuseImageEditApi)

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
