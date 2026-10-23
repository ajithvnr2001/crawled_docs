---
url: https://docs.comfy.org/built-in-nodes/FillHoles/
title: FillHoles - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:54.802019+00:00
---

# FillHoles - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/FillHoles/

Mesh

# FillHoles - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node fills holes in a 3D mesh by detecting open boundary edges and creating new faces to close them.

Copy pageCopy page

This node fills holes in a 3D mesh by detecting open boundary edges and creating new faces to close them. It runs on the GPU, preserves existing geometry and UVs, and can process single meshes, lists of meshes, or batches of meshes.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`mesh`| The 3D mesh to process. Accepts a single mesh, a list of meshes, or a batched mesh.| MESH| Yes| -  
`max_perimeter`| Max hole perimeter to fill. 0 disables. (default: 0.03)| FLOAT| Yes| 0.0 to no upper limit (step 0.0001)  
`weld_epsilon_rel`| Pre-weld tolerance (fraction of bounding box diagonal); boundary detection needs welded vertices. 0 skips. (default: 1e-5)| FLOAT| Yes| 0.0 to no upper limit (step 1e-6)  
`max_vertices`| Cap boundary vertices per cycle; centroid-fan only works for small near-planar holes. Keep ≤16. (default: 16)| INT| Yes| 3 to 1024  
`fill_chains`| Also fill open chains (not just cycles). Noisy; OFF matches cumesh. (default: False)| BOOLEAN| Yes| True or False  
  
Note: When `max_perimeter` is greater than 0, the node fills holes; when it is 0, hole filling is skipped entirely. When `weld_epsilon_rel` is greater than 0, the node pre-welds duplicate vertices before detecting holes. The welding tolerance starts at the given fraction of the bounding box diagonal and automatically increases by doubling until the mesh is considered welded or the tolerance reaches a cap of 1e-2. Holes with more than 8 boundary vertices use a centroid-fan fill (inserting a new centroid vertex), while smaller holes use a vertex-fan fill that reuses an existing boundary vertex. By default only closed boundary cycles are filled; set `fill_chains` to True to also close open chains.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`mesh`| The mesh with holes filled, matching the input batch format.| MESH  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FillHoles/en.md)

* * *

**Source fingerprint (SHA-256):** `c0fd7f0c2d6eea098efb1dcfd80eaa52997e185b9c442b483f75318eea082196`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/FillHoles.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/FillHoles)

[DecimateMesh - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/DecimateMesh)[GetMeshInfo - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/GetMeshInfo)

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
