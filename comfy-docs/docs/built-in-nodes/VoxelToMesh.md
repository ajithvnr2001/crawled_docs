---
url: https://docs.comfy.org/built-in-nodes/VoxelToMesh/
title: VoxelToMesh - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:21.310232+00:00
---

# VoxelToMesh - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/VoxelToMesh/

3D

# VoxelToMesh - ComfyUI Built-in Node Documentation

Copy pageCopy page

The VoxelToMesh node converts 3D voxel data into a mesh geometry by extracting a surface at a specified threshold value.

Copy pageCopy page

The VoxelToMesh node converts 3D voxel data into a mesh geometry by extracting a surface at a specified threshold value. It offers two algorithms for surface extraction: a basic method that creates simple box-like faces, and a surface net method that produces smoother, more detailed meshes. The node processes each voxel grid in the input and generates vertices and faces that form a 3D mesh representation.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`voxel`| The input voxel data to convert to mesh geometry| VOXEL| Yes| -  
`algorithm`| The algorithm used for surface extraction. “surface net” produces smoother meshes, while “basic” creates simple box-like faces (default: “surface net”)| COMBO| Yes| `"surface net"`  
`"basic"`  
`threshold`| The threshold value for surface extraction. Voxels with values above this threshold are considered solid (default: 0.6)| FLOAT| Yes| -1.0 to 1.0  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`MESH`| The generated 3D mesh containing vertices and faces from all input voxel grids. If all voxel grids produce meshes with identical shapes, the output is a stacked tensor; otherwise, a variable-length batch is returned| MESH  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VoxelToMesh/en.md)

* * *

**Source fingerprint (SHA-256):** `b600be13f1a484d8c0cc1f9c3918630d00c15d35008bcac0f677b21ef64b5d98`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/VoxelToMesh.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/VoxelToMesh)

[SavePointCloud - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SavePointCloud)[VoxelToMeshBasic - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/VoxelToMeshBasic)

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
