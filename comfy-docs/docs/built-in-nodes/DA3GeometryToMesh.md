---
url: https://docs.comfy.org/built-in-nodes/DA3GeometryToMesh/
title: DA3GeometryToMesh - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:49.643238+00:00
---

# DA3GeometryToMesh - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/DA3GeometryToMesh/

Geometry Estimation

# DA3GeometryToMesh - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node converts a DA3GEOMETRY packet into a 3D mesh by unprojecting the depth map and triangulating the resulting point cloud.

Copy pageCopy page

This node converts a DA3_GEOMETRY packet into a 3D mesh by unprojecting the depth map and triangulating the resulting point cloud. It processes a single image from a batch and produces a textured or untextured mesh suitable for 3D rendering.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`da3_geometry`| The DA3_GEOMETRY packet containing depth map, optional confidence map, optional sky map, and source image| DA3_GEOMETRY| Yes| -  
`batch_index`| Which image of a batch to convert. Per-image vertex counts differ so batches cannot be stacked (default: 0). Must be less than the batch size of the input geometry, otherwise an error is raised| INT| Yes| 0 to 4096  
`decimation`| Vertex stride. 1 = full resolution, 2 = half, etc. (default: 1)| INT| Yes| 1 to 8  
`discontinuity_threshold`| Drop triangles whose 3x3 depth span exceeds this fraction. 0 = off (default: 0.04)| FLOAT| Yes| 0.0 to 1.0  
`confidence_threshold`| Exclude pixels whose per-image normalised confidence is below this value. 0 = keep all, 1 = keep only the single most confident pixel. Used when the geometry has a confidence map (Small/Base models) (default: 0.1)| FLOAT| Yes| 0.0 to 1.0  
`use_sky_mask`| Exclude sky-probability pixels (sky >= 0.5) from the mesh. Used when the geometry has a sky map (Mono/Metric models) (default: True)| BOOLEAN| Yes| True or False  
`texture`| Use the source image as a base color texture (default: True)| BOOLEAN| Yes| True or False  
  
Pixels with non-finite, zero, or negative depth values are always excluded from the mesh. An error is raised if the resulting mesh is empty; the error message suggests raising `discontinuity_threshold`, lowering `confidence_threshold`, or disabling `use_sky_mask`.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`MESH`| A triangulated 3D mesh with vertices, faces, UV coordinates, and optional texture| MESH  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DA3GeometryToMesh/en.md)

* * *

**Source fingerprint (SHA-256):** `1d311223a8d131030bcd4930d21852a21ac9dd5758e7f8b8d20b1cf68698893b`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/DA3GeometryToMesh.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/DA3GeometryToMesh)

[Morphology - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Morphology)[DA3GeometryToPointCloud - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/DA3GeometryToPointCloud)

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
