---
url: https://docs.comfy.org/built-in-nodes/SplatToFile3D/
title: SplatToFile3D - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:03.730479+00:00
---

# SplatToFile3D - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SplatToFile3D/

Splat

# SplatToFile3D - ComfyUI Built-in Node Documentation

Copy pageCopy page

The SplatToFile3D node converts a gaussian splat into a File3D object that can be used with Save or Preview 3D nodes.

Copy pageCopy page

The SplatToFile3D node converts a gaussian splat into a File3D object that can be used with Save or Preview 3D nodes. It supports one item per batch only and allows you to choose from different output file formats for the exported 3D data.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`splat`| The gaussian splat data to be serialized into a file| SPLAT| Yes| -  
`format`| The output file format for the 3D file (default: “ply”). ply: standard 3D Gaussian Splat with full spherical harmonics. ksplat: mkkellogg SplatBuffer (level 0, uncompressed), base color only. spz: Niantic gzip-compressed (~10x smaller), base color only| COMBO| Yes| ”ply"  
"ksplat"  
"spz”  
  
Note: This node supports one item per batch only. If the input splat contains more than one item in the batch, the node logs a warning and uses the first item. If an unsupported format is provided, the node raises an error.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model_3d`| A File3D object containing the serialized gaussian splat data in the selected format, ready for saving or previewing| FILE3D  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplatToFile3D/en.md)

* * *

**Source fingerprint (SHA-256):** `4bb49f417a66f25fce577894a67f39bae6157c4eb88ccf8fad77d74141a50409`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SplatToFile3D.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SplatToFile3D)

[RenderSplat - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/RenderSplat)[SplatToMesh - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SplatToMesh)

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
