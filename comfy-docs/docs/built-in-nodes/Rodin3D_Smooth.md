---
url: https://docs.comfy.org/built-in-nodes/Rodin3D_Smooth/
title: Rodin3D_Smooth - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:52.996792+00:00
---

# Rodin3D_Smooth - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Rodin3D_Smooth/

Rodin

# Rodin3D_Smooth - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Rodin 3D Smooth node generates 3D assets using the Rodin API by processing input images and converting them into smooth 3D models.

Copy pageCopy page

The Rodin 3D Smooth node generates 3D assets using the Rodin API by processing input images and converting them into smooth 3D models. It takes multiple images as input and produces a downloadable 3D model file. The node handles the entire generation process including task creation, status polling, and file downloading automatically.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`Images`| Input images to use for 3D model generation. Multiple images can be provided (up to 5).| IMAGE| Yes| -  
`Seed`| Random seed value for generation consistency (default: 0).| INT| No| 0 to 65535  
`Material_Type`| Type of material to apply to the 3D model (default: “PBR”).| STRING| No| ”PBR"  
"Shaded”  
`Polygon_count`| Target polygon count for the generated 3D model. Determines the mesh quality and detail level (default: “18K-Quad”).| STRING| No| ”4K-Quad"  
"8K-Quad"  
"18K-Quad"  
"50K-Quad"  
"200K-Triangle”  
  
**Note:** The node accepts up to 5 input images. If no images are provided, an error will be raised.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`3D Model Path`| File path to the downloaded 3D model (for backward compatibility only).| STRING  
`GLB`| The generated 3D model in GLB format.| FILE3DGLB  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Smooth/en.md)

* * *

**Source fingerprint (SHA-256):** `c7dc23d2a7a8e2d425fc389476ef381f4ebf974f522c6e3774222866eee064e9`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Rodin3D_Smooth.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Rodin3D_Smooth)

[Rodin3D_Sketch - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Rodin3D_Sketch)[Tencent3DPartNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Tencent3DPartNode)

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
