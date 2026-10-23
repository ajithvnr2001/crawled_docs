---
url: https://docs.comfy.org/built-in-nodes/MoGePointMapToMesh/
title: MoGePointMapToMesh - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:34.405369+00:00
---

# MoGePointMapToMesh - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MoGePointMapToMesh/

Geometry Estimation

# MoGePointMapToMesh - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node converts a MoGe point map into a 3D mesh.

Copy pageCopy page

This node converts a MoGe point map into a 3D mesh. It takes geometry data produced by a MoGe depth estimation node and triangulates it into a mesh with UV coordinates and an optional texture.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`moge_geometry`| The MoGe geometry data containing point maps, depth, and optionally the source image.| MOGE_GEOMETRY| Yes| N/A  
`batch_index`| Which image of a batched MoGe geometry to mesh. Per-image vertex counts differ, so batches can’t be stacked into a single MESH (default: 0).| INT| Yes| 0 to 4096  
`decimation`| Vertex stride; 1 = full resolution (default: 1).| INT| Yes| 1 to 8  
`discontinuity_threshold`| Drop pixels whose 3x3 depth span exceeds this fraction. 0 = off (default: 0.04).| FLOAT| Yes| 0.0 to 1.0  
`texture`| Carry the source image through as the baseColor texture (default: True).| BOOLEAN| Yes| True/False  
  
Note: `batch_index` must be smaller than the batch size of the input `moge_geometry`; selecting an out-of-range index raises an error. The input must contain a points output, otherwise the node raises an error. If the triangulation produces an empty mesh, the node raises an error — setting `discontinuity_threshold` to 0 disables the depth-discontinuity filter. The output mesh is converted to glTF coordinates: perspective MoGe data (X right, Y down, Z forward) is flipped to match glTF (Y up, Z back), and panoramic data (geometry without intrinsic parameters) is rotated accordingly with corrected winding. When `texture` is enabled, the source image from `moge_geometry` is used as the baseColor texture.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`MESH`| A 3D mesh with vertices, faces, UV coordinates, and an optional baseColor texture from the source image.| MESH  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePointMapToMesh/en.md)

* * *

**Source fingerprint (SHA-256):** `626925866eed6805d2ce87529909fc76b9484cd2e8118fdd1669a237d44b9b0b`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MoGePointMapToMesh.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MoGePointMapToMesh)

[MoGePanoramaInference - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/MoGePanoramaInference)[MoGeRender - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/MoGeRender)

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
