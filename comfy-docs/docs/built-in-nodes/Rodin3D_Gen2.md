---
url: https://docs.comfy.org/built-in-nodes/Rodin3D_Gen2/
title: Rodin3D_Gen2 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:52.553870+00:00
---

# Rodin3D_Gen2 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Rodin3D_Gen2/

Rodin

# Rodin3D_Gen2 - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Rodin3DGen2 node generates 3D assets using the Rodin API.

Copy pageCopy page

The Rodin3D_Gen2 node generates 3D assets using the Rodin API. It takes input images and converts them into 3D models with various material types and polygon counts. The node handles the entire generation process including task creation, status polling, and file downloading automatically.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`Images`| Input images to use for 3D model generation. Accepts 1 to 5 images.| IMAGE| Yes| -  
`Seed`| Random seed value for generation (default: 0)| INT| No| 0-65535  
`Material_Type`| Type of material to apply to the 3D model (default: “PBR”)| COMBO| No| ”PBR"  
"Shaded”  
`Polygon_count`| Target polygon count and mesh type for the generated 3D model. “Quad” options use quad-based meshes, “Triangle” options use triangle-based meshes (default: “500K-Triangle”)| COMBO| No| ”4K-Quad"  
"8K-Quad"  
"18K-Quad"  
"50K-Quad"  
"2K-Triangle"  
"20K-Triangle"  
"150K-Triangle"  
"500K-Triangle”  
`TAPose`| Whether to apply TAPose processing (default: False). This is an advanced parameter.| BOOLEAN| No| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`3D Model Path`| File path to the generated 3D model (for backward compatibility)| STRING  
`GLB`| The generated 3D model in GLB format| FILE3DGLB  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen2/en.md)

* * *

**Source fingerprint (SHA-256):** `6ee8b52152e84cca48c7875ce066ab19805a42e5cccc84865c6027a4f6fd3b16`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Rodin3D_Gen2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Rodin3D_Gen2)

[Rodin3D_Detail - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Rodin3D_Detail)[Rodin3D_Gen25_Image - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Rodin3D_Gen25_Image)

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
