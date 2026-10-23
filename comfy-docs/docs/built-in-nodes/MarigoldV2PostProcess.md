---
url: https://docs.comfy.org/built-in-nodes/MarigoldV2PostProcess/
title: MarigoldV2PostProcess - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:29.273795+00:00
---

# MarigoldV2PostProcess - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MarigoldV2PostProcess/

Geometry Estimation

# MarigoldV2PostProcess - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node converts a decoded Marigold V2 prediction into a viewable image.

Copy pageCopy page

This node converts a decoded Marigold V2 prediction into a viewable image. It takes the raw prediction tensor and formats it depending on which type of prediction it is: normalized depth (near objects appear bright), unit-length surface normals, or sRGB albedo.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The decoded Marigold V2 prediction to be converted into a displayable image.| IMAGE| Yes| -  
`prediction`| The type of prediction contained in the input, which determines how the data is converted. `"depth"` normalizes the depth values so that near surfaces are bright and far surfaces are dark, then copies the result into all three color channels. `"normals"` rescales the values to the -1..1 range, normalizes them into unit surface normals, and maps them back to 0..1. `"albedo"` applies a linear-to-sRGB conversion to the values.| COMBO| Yes| `"depth"`  
`"normals"`  
`"albedo"`  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| The processed image in the selected representation: normalized depth (grayscale repeated across three channels), unit surface normals, or sRGB albedo.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MarigoldV2PostProcess/en.md)

* * *

**Source fingerprint (SHA-256):** `848b29e2dfcd34c44cf9707b9b26cb13c18e82bb16618a15afbe477a1d620e1e`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MarigoldV2PostProcess.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MarigoldV2PostProcess)

[DA3Render - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/DA3Render)[MoGeGeometryToFOV - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/MoGeGeometryToFOV)

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
