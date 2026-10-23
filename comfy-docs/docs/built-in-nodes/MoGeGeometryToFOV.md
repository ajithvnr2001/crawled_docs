---
url: https://docs.comfy.org/built-in-nodes/MoGeGeometryToFOV/
title: MoGeGeometryToFOV - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:34.611131+00:00
---

# MoGeGeometryToFOV - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MoGeGeometryToFOV/

Geometry Estimation

# MoGeGeometryToFOV - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node derives the field of view and focal length from the camera intrinsics stored in a MoGe geometry object.

Copy pageCopy page

This node derives the field of view and focal length from the camera intrinsics stored in a MoGe geometry object. It can return the vertical, horizontal, or diagonal FOV, in degrees or radians. The vertical FOV output can be used, for example, to feed the SAM3DBody_Predict node.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`moge_geometry`| The MoGe geometry object. It must contain an intrinsics matrix and at least one of `image`, `points`, or `depth` data, which is used to read the pixel height for the focal-length conversion.| MOGE_GEOMETRY| Yes| —  
`axis`| The axis along which the FOV is computed: “vertical” (fov_y), “horizontal” (fov_x), or “diagonal” (default: “vertical”).| COMBO| Yes| ”vertical"  
"horizontal"  
"diagonal”  
`unit`| Output unit for the FOV (default: “degrees”).| COMBO| Yes| ”degrees"  
"radians”  
  
Note: The node raises an error if `moge_geometry` contains no intrinsics (panorama geometry has none) or if it contains neither `image`, `points`, nor `depth` data.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`fov`| The field of view along the selected axis, in the selected unit (degrees or radians).| FLOAT  
`focal_pixels`| The lens focal length in pixels, derived from the vertical intrinsic and the pixel height.| FLOAT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeGeometryToFOV/en.md)

* * *

**Source fingerprint (SHA-256):** `983dc984847f93a8e002c73982571ecb38b7bae9c3dc4c201d9be17f785dcaed`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MoGeGeometryToFOV.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MoGeGeometryToFOV)

[MarigoldV2PostProcess - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/MarigoldV2PostProcess)[MoGeInference - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/MoGeInference)

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
