---
url: https://docs.comfy.org/built-in-nodes/UnwrapMesh/
title: UnwrapMesh - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-18T12:01:28.650433+00:00
---

# UnwrapMesh - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/UnwrapMesh/

Texturing

# UnwrapMesh - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generates a UV atlas for a 3D mesh. The mesh surface is split into charts, each chart is flattened into two dimensions

Copy pageCopy page

Generates a UV atlas for a 3D mesh. The mesh surface is split into charts, each chart is flattened into two dimensions, and the flattened charts are packed into a [0,1] UV atlas. Vertices on chart seams are duplicated (one copy per chart, same position, own UV), so the output mesh can contain more vertices than the input mesh, and the output faces may differ in count from the input.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`mesh`| The input mesh to unwrap. Accepts a single mesh or a batch of meshes; batches are processed one item at a time.| MESH| Yes| —  
`segmenter`| Charting algorithm to use. `pec`: fast parallel-edge-collapse charting on GPU. `adaptive`: CPU, slower. (default: “pec”)| COMBO| Yes| ”pec"  
"adaptive”  
`resolution`| Target atlas resolution for texel-density auto-scale (0 = fit-to-content). (default: 1024)| INT| Yes| 0 to 8192 (step 256)  
`padding`| Texel padding between charts. (default: 1)| INT| Yes| 0 to 16  
`weld_distance`| Coincident-vert merge radius as a fraction of mesh extent (0 = auto). Raise to ~0.001 if you get per-triangle charts (unwelded input). (default: 0.0)| FLOAT| Yes| 0.0 to 1.0 (step 0.0001)  
  
Note: if the input mesh contains unwelded vertices, the node may warn that face adjacency is low and produce per-face UV charts; increasing `weld_distance` merges coincident vertices before unwrapping. Degenerate faces (faces that reuse the same vertex index) are dropped during processing.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`mesh`| The input mesh with a generated UV atlas in the range [0,1]. Seam vertices are duplicated, so the output vertex count can exceed the input. Vertex colors and texture from the input mesh are preserved.| MESH  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UnwrapMesh/en.md)

* * *

**Source fingerprint (SHA-256):** `fcab6f0b621693d862ee74b5ec498498d2f1f247a66f478704377598a6b39388`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/UnwrapMesh.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/UnwrapMesh)

[RenderUVAtlas - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/RenderUVAtlas)[BuildPoseFile - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/BuildPoseFile)

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
