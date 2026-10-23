---
url: https://docs.comfy.org/built-in-nodes/ImageSDRToHDR/
title: ImageSDRToHDR - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:10.723650+00:00
---

# ImageSDRToHDR - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ImageSDRToHDR/

Color

# ImageSDRToHDR - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Convert SDR to HDR node expands standard dynamic range sRGB images into Rec.2020 HLG HDR.

Copy pageCopy page

The **Convert SDR to HDR** node expands standard dynamic range sRGB images into Rec.2020 HLG HDR. It keeps the existing look of the image and maps its brightness into a wider range, so the result must be saved with an HDR color space selected. Alpha is preserved unchanged.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The SDR image(s) in sRGB to expand into HDR.| IMAGE| Yes| -  
`algorithm`| HDR expansion algorithm. Selecting an algorithm reveals its parameters (`target_luminance`).| DYNAMIC_COMBO| Yes| `"lottes"`  
  
### 

​

lottes Inputs

These parameters appear when `algorithm` is set to `"lottes"`.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`target_luminance`| Peak-white target in nits. 0 keeps the calibrated rendering. Dark images are not normalized to this peak. (default: 650.0)| FLOAT| Yes| 0.0 to 10000.0 (step 1.0)  
  
Each image of the batch is converted separately: the sRGB encoding is inverted to linear light, the brightness is expanded with a Lottes-style rational curve blended with a calibrated monotonic log-gain curve, and the result is re-encoded as Rec.2020 HLG. Because the output is HDR, the save node must use the `HDR` color space; saving it as sRGB renders the brightness incorrectly. HLG assumes a 1000-nit reference display, so `target_luminance` values below 1000 keep that reference and a value of `0` leaves the calibrated rendering untouched. Single-channel images are expanded to three channels before conversion, and the alpha channel is copied through unchanged.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| The Rec.2020 HLG HDR image(s).| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageSDRToHDR/en.md)

* * *

**Source fingerprint (SHA-256):** `51eb0beac3d48345a30ba66d80d95873384cf5155fc06c33353b6d1dc029658a`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ImageSDRToHDR.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ImageSDRToHDR)

[ImageRGBToYUV - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ImageRGBToYUV)[ImageYUVToRGB - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ImageYUVToRGB)

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
