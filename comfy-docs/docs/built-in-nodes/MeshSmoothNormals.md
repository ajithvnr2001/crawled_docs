---
url: https://docs.comfy.org/built-in-nodes/MeshSmoothNormals/
title: MeshSmoothNormals - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:30.784536+00:00
---

# MeshSmoothNormals - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MeshSmoothNormals/

Mesh

# MeshSmoothNormals - ComfyUI Built-in Node Documentation

Copy pageCopy page

Compute smooth per-vertex normals for a mesh and attach them.

Copy pageCopy page

Compute smooth per-vertex normals for a mesh and attach them. Meshes without normals are shaded flat (per-face) by glTF viewers; this node makes them shade smoothly. With a crease angle below 180, edges sharper than the threshold are kept hard by splitting vertices along them.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`mesh`| The input mesh to process.| MESH| Yes| -  
`crease_angle`| Edges whose dihedral angle exceeds this value (degrees) stay hard (vertices are split). 180 = fully smooth; lower preserves sharp edges (e.g. ~30-60 for hard-surface). Default: 180.0.| FLOAT| Yes| 0.0 to 180.0 (step 1.0)  
  
When `crease_angle` is 180 or higher, the mesh topology is unchanged. When set below 180, vertices are split along hard edges, which may increase the vertex count. When vertices are split, per-vertex data (colors, UVs, and tangents) is duplicated to match the new vertex layout, and the resulting mesh is rebuilt as a variable-size batch.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`mesh`| The input mesh with smooth normal data attached, or with split vertices and normals when a crease angle is set.| MESH  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshSmoothNormals/en.md)

* * *

**Source fingerprint (SHA-256):** `bbe9c0fba68369d8e9d3fb68e635869233804f3aac458e7c217d94977e77b9be`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MeshSmoothNormals.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MeshSmoothNormals)

[MergeMeshes - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/MergeMeshes)[PaintMesh - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/PaintMesh)

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
