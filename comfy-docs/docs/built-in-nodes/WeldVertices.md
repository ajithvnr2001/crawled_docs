---
url: https://docs.comfy.org/built-in-nodes/WeldVertices/
title: WeldVertices - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:26.864422+00:00
---

# WeldVertices - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/WeldVertices/

Mesh

# WeldVertices - ComfyUI Built-in Node Documentation

Copy pageCopy page

Weld Vertices merges coincident vertices in a 3D mesh, so faces that previously had separate corner points end up sharing the same vertices.

Copy pageCopy page

Weld Vertices merges coincident vertices in a 3D mesh, so faces that previously had separate corner points end up sharing the same vertices. It groups nearby vertices using grid quantization with a tolerance based on the mesh bounding box, and averages vertex colors for each merged group. This is useful when a mesh arrives unwelded, meaning each face has its own vertices and no shared edges, and can serve as a pre-pass before topology-aware operations such as FillHoles or DecimateMesh.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`mesh`| The input 3D mesh whose coincident vertices will be merged.| MESH| Yes| -  
`epsilon_rel`| Weld tolerance (fraction of bbox diagonal). 1e-5 for float dedup; 1e-3 for visibly-close-but-distinct verts. Default: 1e-5.| FLOAT| Yes| 0.0 to unlimited (step 1e-6)  
`epsilon_abs`| Absolute weld tolerance (overrides epsilon_rel when > 0). Default: 0.0.| FLOAT| Yes| 0.0 to unlimited (step 1e-6)  
  
Note: When `epsilon_abs` is greater than 0, it takes precedence over `epsilon_rel` and the relative tolerance is ignored. When `epsilon_abs` is 0, the relative tolerance `epsilon_rel` is used, converted into an absolute distance by multiplying it with the mesh bounding box diagonal.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`mesh`| The welded mesh with merged vertices, updated face indices, and averaged vertex colors (if the input mesh had colors).| MESH  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WeldVertices/en.md)

* * *

**Source fingerprint (SHA-256):** `f8779e764b344de651b8459f6e4c28773509d9596a98fd164dc7044278856435`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/WeldVertices.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/WeldVertices)

[RotateMesh - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/RotateMesh)[File3DToSplat - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/File3DToSplat)

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
