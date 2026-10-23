---
url: https://docs.comfy.org/built-in-nodes/BakeTextureFromVoxel/
title: BakeTextureFromVoxel - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:22.376213+00:00
---

# BakeTextureFromVoxel - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/BakeTextureFromVoxel/

Texturing

# BakeTextureFromVoxel - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node bakes PBR textures onto a 3D mesh using the mesh’s existing UV layout.

Copy pageCopy page

This node bakes PBR textures onto a 3D mesh using the mesh’s existing UV layout. It rasterizes the mesh in UV space and samples color and material attributes from a sparse voxel volume at each texel, outputting a base color image plus metallic and roughness maps. It does not unwrap the mesh, so a UV unwrap node must be connected upstream; the resulting images are intended to be paired with the same mesh in ApplyTextureToMesh for saving as GLB.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`mesh`| The 3D mesh to bake textures onto. Must already have a UV layout; a UV unwrap node must be connected upstream.| MESH| Yes|   
`voxel_colors`| Sparse voxel volume containing per-voxel colors and optional PBR attributes (metallic and roughness channels).| VOXEL| Yes|   
`texture_size`| Square UV atlas resolution (display name: “resolution”, default: 2048).| INT| Yes| 64 to 8192  
`reference_mesh`| Optional dense pre-decimation mesh; back-projects each texel onto its true surface before sampling, removing faceted baking on coarse meshes.| MESH| No|   
  
Notes:

  * The input mesh must have UVs. If no UVs are present, the node raises an error. UVs must be 1:1 with the vertices (one UV per vertex).
  * When the mesh and voxel coordinates contain a batch dimension, each batch item is baked separately. If a batch item has no voxels or no faces, it is skipped and a black texture is emitted for it.
  * When `reference_mesh` is provided for a batch, it is matched by batch index unless it contains only a single mesh, in which case that mesh is used for all items.
  * Texels that are not covered by any UV triangle are filled from the nearest covered texel so that texture seams do not pull in black.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`base_color`| RGB base color texture map. Values are float in the 0–1 range.| IMAGE  
`metallic`| Grayscale metallic map (float, 0–1). Black when the voxel colors contain no metallic channel.| IMAGE  
`roughness`| Grayscale roughness map (float, 0–1). Black when the voxel colors contain no roughness channel.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeTextureFromVoxel/en.md)

* * *

**Source fingerprint (SHA-256):** `080dcb670620f1cb97523d04fc45293e03d139e513845d0fa7b1c4d2f8bdf32d`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/BakeTextureFromVoxel.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/BakeTextureFromVoxel)

[BakeNormalMapFromMesh - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/BakeNormalMapFromMesh)[MeshTextureToImage - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/MeshTextureToImage)

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
