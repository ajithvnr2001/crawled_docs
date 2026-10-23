---
url: https://docs.comfy.org/built-in-nodes/MeshToFile3D/
title: MeshToFile3D - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:31.646547+00:00
---

# MeshToFile3D - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MeshToFile3D/

3D

# MeshToFile3D - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node serializes a mesh into a GLB file object that can be passed to Save 3D or Preview 3D nodes.

Copy pageCopy page

This node serializes a mesh into a GLB file object that can be passed to Save 3D or Preview 3D nodes. It carries all mesh data along, including UVs, colors, normals, texture, normal/occlusion/emissive maps, and material settings. Only the first item of a multi-item batch is used.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`mesh`| The mesh to convert into a GLB file, including UVs, colors, normals, texture, normal/occlusion/emissive maps, and material. Only one item per batch is supported; if a batch contains multiple items, the first one is used.| MESH| Yes| Single mesh  
  
Note: The node supports one item per batch only. If the input mesh contains more than one item in its batch, a warning is logged and the first item is used. The mesh must contain at least one vertex and one face; an empty mesh raises an error.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model_3d`| A GLB (glTF Binary) file object containing the serialized mesh, ready to be saved or previewed by other 3D nodes.| FILE3D  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshToFile3D/en.md)

* * *

**Source fingerprint (SHA-256):** `f004c2907c0df2e0127e49b4767d1624bf89c72665fc7028347a0b8a63a5772e`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MeshToFile3D.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MeshToFile3D)

[Load3DAnimation - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Load3DAnimation)[Preview3D - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Preview3D)

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
