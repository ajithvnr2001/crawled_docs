---
url: https://docs.comfy.org/built-in-nodes/VoxelToMeshBasic/
title: VoxelToMeshBasic - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:21.405103+00:00
---

# VoxelToMeshBasic - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/VoxelToMeshBasic/

3D

# VoxelToMeshBasic - ComfyUI Built-in Node Documentation

Copy pageCopy page

The VoxelToMeshBasic node converts 3D voxel data into mesh geometry.

Copy pageCopy page

The VoxelToMeshBasic node converts 3D voxel data into mesh geometry. It processes voxel volumes by applying a threshold value to determine which parts of the volume become solid surfaces in the resulting mesh. The node outputs a complete mesh structure with vertices and faces that can be used for 3D rendering and modeling.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`voxel`| The 3D voxel data to convert into a mesh| VOXEL| Yes| -  
`threshold`| The threshold value used to determine which voxels become part of the mesh surface (default: 0.6)| FLOAT| Yes| -1.0 to 1.0  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`MESH`| The generated 3D mesh containing vertices and faces| MESH  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VoxelToMeshBasic/en.md)

* * *

**Source fingerprint (SHA-256):** `95d729463e9d32fb0b8a82a397c6ed7fccaf190ec8a183d71a99fef170747fd1`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/VoxelToMeshBasic.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/VoxelToMeshBasic)

[VoxelToMesh - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/VoxelToMesh)[EasyCache - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/EasyCache)

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
