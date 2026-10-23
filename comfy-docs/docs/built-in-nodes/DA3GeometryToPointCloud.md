---
url: https://docs.comfy.org/built-in-nodes/DA3GeometryToPointCloud/
title: DA3GeometryToPointCloud - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:49.733442+00:00
---

# DA3GeometryToPointCloud - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/DA3GeometryToPointCloud/

Geometry Estimation

# DA3GeometryToPointCloud - ComfyUI Built-in Node Documentation

Copy pageCopy page

Convert a depth map from a DA3GEOMETRY object into a 3D point cloud.

Copy pageCopy page

Convert a depth map from a DA3_GEOMETRY object into a 3D point cloud. It applies filtering based on confidence and sky masks, and transforms the points into a common world coordinate system suitable for multi-view scenes.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`da3_geometry`| The DA3_GEOMETRY object containing depth data and optional image, confidence, and sky maps| DA3_GEOMETRY| Yes| -  
`batch_index`| Which image of a batch to convert (default: 0)| INT| Yes| 0 to 4096  
`confidence_threshold`| Exclude pixels whose per-image normalised confidence is below this value (0 = keep all). Used when the geometry has a confidence map (Small/Base models). (default: 0.1)| FLOAT| Yes| 0.0 to 1.0  
`use_sky_mask`| Exclude sky-probability pixels (sky >= 0.5). Used when the geometry has a sky map (Mono/Metric models). (default: True)| BOOLEAN| Yes| True or False  
`downsample`| Take every Nth pixel (1 = full resolution). Higher values give fewer points and faster processing. (default: 1)| INT| Yes| 1 to 16  
  
**Notes:**

  * `batch_index` must be smaller than the batch size of the input geometry; otherwise the node raises an error.
  * If filtering removes all pixels, the node raises an error. Lowering `confidence_threshold` or disabling `use_sky_mask` can prevent this.
  * `confidence_threshold` is only applied when the geometry includes a confidence map (Small/Base models).
  * `use_sky_mask` is only applied when the geometry includes a sky map (Mono/Metric models).
  * When `downsample` is greater than 1, the camera intrinsics are scaled accordingly so the projected points remain correct.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`point_cloud`| A point cloud containing filtered 3D points, optional colors, and optional confidence values| DA3_POINT_CLOUD  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DA3GeometryToPointCloud/en.md)

* * *

**Source fingerprint (SHA-256):** `3cf5bdbb8afdfcfc02f9832a8cbc5a3df49da755dea6df01792aa6ef9e5d7287`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/DA3GeometryToPointCloud.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/DA3GeometryToPointCloud)

[DA3GeometryToMesh - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/DA3GeometryToMesh)[DA3Inference - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/DA3Inference)

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
