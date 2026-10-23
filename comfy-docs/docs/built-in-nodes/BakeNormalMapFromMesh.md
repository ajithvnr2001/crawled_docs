---
url: https://docs.comfy.org/built-in-nodes/BakeNormalMapFromMesh/
title: BakeNormalMapFromMesh - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:22.180031+00:00
---

# BakeNormalMapFromMesh - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/BakeNormalMapFromMesh/

Texturing

# BakeNormalMapFromMesh - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node bakes a tangent-space normal map from a high-poly mesh onto a low-poly mesh’s UV layout, capturing surface detail that was lost during decimation.

Copy pageCopy page

This node bakes a tangent-space normal map from a high-poly mesh onto a low-poly mesh’s UV layout, capturing surface detail that was lost during decimation. Connect the UV-unwrapped low-poly mesh and the high-poly mesh it came from, and the node outputs an image ready for the `normal_map` input of Apply Texture To Mesh.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`low_poly`| The UV-unwrapped low-poly mesh that receives the baked detail. Must have existing UVs; the node never unwraps.| MESH| Yes| —  
`high_poly`| The high-poly mesh whose surface detail is baked into the low-poly’s UV layout.| MESH| Yes| —  
`resolution`| Edge length in pixels of the square output normal map (default: 1024).| INT| Yes| 64 to 8192 (step 64)  
`cage_distance`| Surface search band, as a fraction of the bounding box diagonal. Raise for wrong/missing patches under heavy decimation; lower if it grabs across gaps. Default: 0.05.| FLOAT| Yes| 0.001 to 0.5 (step 0.001)  
`ignore_backfaces`| Skip high-poly surfaces facing away from the texel, so crevices/enclosed spaces don’t grab the opposite wall. Disable only if the high-poly winding is inconsistent. Default: true.| BOOLEAN| Yes| true / false  
  
Note: `low_poly` must have UV coordinates. If it has none, the node raises an error because it bakes onto the existing UV layout and does not unwrap the mesh. When `low_poly` is a batch, each item is baked in order; if `high_poly` contains only one item, that item is reused for every batch item. Empty meshes in the batch are skipped with a warning and produce a flat mid-gray (0.5) normal map. If the low-poly UVs spill outside the [0,1] range, they are uniformly fitted into [0,1] (with a warning when the layout looks tiled/UDIM), so the bake and Apply Texture To Mesh use the same UVs.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`normal_map`| The baked tangent-space normal map (glTF/OpenGL +Y convention) as a square resolution × resolution RGB image with values in [0,1]. Connect it to the `normal_map` input of Apply Texture To Mesh.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeNormalMapFromMesh/en.md)

* * *

**Source fingerprint (SHA-256):** `29df10014b5998b741d71db21d0c982d7bca85ad966a720063af15062e203322`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/BakeNormalMapFromMesh.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/BakeNormalMapFromMesh)

[BakeAmbientOcclusion - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/BakeAmbientOcclusion)[BakeTextureFromVoxel - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/BakeTextureFromVoxel)

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
