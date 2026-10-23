---
url: https://docs.comfy.org/built-in-nodes/ImageColorSpace/
title: ImageColorSpace - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:07.472904+00:00
---

# ImageColorSpace - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ImageColorSpace/

Color

# ImageColorSpace - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ImageColorSpace node converts images between sRGB (Rec.709), linear Rec.709, HDR (Rec.2020 HLG), HDR PQ (Rec.2020 PQ), HDR LogC3

Copy pageCopy page

The ImageColorSpace node converts images between sRGB (Rec.709), linear Rec.709, HDR (Rec.2020 HLG), HDR PQ (Rec.2020 PQ), HDR LogC3, and HDR ACEScct color spaces. LogC3 uses the EI 800 curve with Rec.709 primaries and codes clamped to [0, 1]; ACEScct uses AP1 primaries and D60 white, with Bradford adaptation to D65. When converting to SDR output, or from HDR PQ to HDR, it tone-maps excess luminance across the batch and compresses out-of-gamut colors; linear and ACEScct outputs, and linear-to-HDR conversions, preserve extended values. HLG and PQ outputs clip negative channels. Conversions are computed in float32, and any alpha channel is passed through unchanged.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The input image to be converted.| IMAGE| Yes| Any valid image.  
`source`| Color space of the input pixels. Default: “sRGB”.| COMBO| Yes| `"sRGB"`  
`"HDR"`  
`"HDR PQ"`  
`"linear"`  
`"HDR LogC3"`  
`"HDR ACEScct"`  
`destination`| Color space of the output pixels. Set the save node to this same color space. Convert LogC3 or ACEScct to linear before saving EXR, or to sRGB/HDR/HDR PQ before saving video. Default: “sRGB”.| COMBO| Yes| `"sRGB"`  
`"HDR"`  
`"HDR PQ"`  
`"linear"`  
`"HDR LogC3"`  
`"HDR ACEScct"`  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The converted image in the specified destination color space.| IMAGE  
  
## 

​

Notes

  * Linear 1.0 uses the same 203-nit reference white as sRGB; HLG uses a 1000-nit reference display.
  * Linear and ACEScct outputs preserve extended values; linear-to-HDR conversions preserve highlights without tone mapping.
  * SDR output and PQ-to-HLG conversion tone-map excess luminance across the batch (sharing one white point so exposure does not change frame by frame) and compress out-of-gamut colors. HLG and PQ outputs clip negative channels.
  * Conversions are computed in float32 and return the intermediate device and dtype.
  * LogC3 and ACEScct are camera log encodings: convert them to linear for EXR saving, or to sRGB/HDR/HDR PQ before saving video.
  * Straight alpha is not color-transformed; only the RGB channels are converted.
  * If `source` and `destination` are the same, no color transformation is applied — the image is only moved to the intermediate device and dtype.



> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageColorSpace/en.md)

* * *

**Source fingerprint (SHA-256):** `fdf8b4f16a1e0c7ff9a86b8cc40f6f796175205e4b1f491b595a74a8456b9b94`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ImageColorSpace.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ImageColorSpace)

[SplitImageToTileList - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SplitImageToTileList)[ImageRGBToYUV - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ImageRGBToYUV)

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
