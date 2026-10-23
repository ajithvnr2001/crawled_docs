---
url: https://docs.comfy.org/built-in-nodes/MergeMeshes/
title: MergeMeshes - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:30.663760+00:00
---

# MergeMeshes - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MergeMeshes/

Mesh

# MergeMeshes - ComfyUI Built-in Node Documentation

Copy pageCopy page

MergeMeshes combines multiple mesh inputs into a single mesh by stacking their vertices, faces, UV coordinates, and vertex colors

Copy pageCopy page

MergeMeshes combines multiple mesh inputs into a single mesh by stacking their vertices, faces, UV coordinates, and vertex colors, and offsetting face indices so all parts join correctly into one continuous mesh.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`meshes`| Growable slot: connect 2 to 50 mesh objects (named `mesh_1`, `mesh_2`, …, `mesh_50`). All connected meshes are merged into one output mesh.| MESH| Yes| 2 to 50 meshes  
  
**Note:** At least one mesh must be provided; otherwise the node raises an error. Only the first mesh item from each input mesh’s batch is used. Input meshes are moved to CPU before merging. If any input mesh has UV data, the output includes UVs and meshes without UVs receive zero-filled UV values. If any input mesh has vertex colors, the output includes vertex colors; meshes without colors receive white (value 1) colors, and color channels are padded to the largest channel count found among inputs. Only the texture from the first input that provides one is kept; additional textures are dropped.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`mesh`| The merged mesh containing all input vertices, faces, UVs, and colors combined into one mesh.| MESH  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MergeMeshes/en.md)

* * *

**Source fingerprint (SHA-256):** `0ce49b522f6348d524df20d6c27eb8bd9575c4a781790f6f8e3ac4f3ee255d38`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MergeMeshes.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MergeMeshes)

[GetMeshInfo - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/GetMeshInfo)[MeshSmoothNormals - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/MeshSmoothNormals)

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
