---
url: https://docs.comfy.org/built-in-nodes/TencentSmartTopologyNode/
title: TencentSmartTopologyNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:08.146795+00:00
---

# TencentSmartTopologyNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/TencentSmartTopologyNode/

Tencent

# TencentSmartTopologyNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node performs smart retopology on a 3D model, automatically creating a new, cleaner mesh with optimized polygon count.

Copy pageCopy page

This node performs smart retopology on a 3D model, automatically creating a new, cleaner mesh with optimized polygon count. It connects to a Tencent Hunyuan 3D API to process the model, supporting GLB and OBJ file formats up to 200MB. The node returns the processed model as an OBJ file.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model_3d`| Input 3D model (GLB or OBJ). The file must be in GLB or OBJ format and cannot exceed 200MB.| FILE3D| Yes| -  
`polygon_type`| Surface composition type.| STRING| Yes| `"triangle"`  
`"quadrilateral"`  
`face_level`| Polygon reduction level.| STRING| Yes| `"medium"`  
`"high"`  
`"low"`  
`seed`| Seed controls whether the node should re-run; results are non-deterministic regardless of seed. (default: 0)| INT| No| 0 to 2147483647  
  
**Note:** The `seed` parameter is used to trigger a re-run of the node, but the final output is not guaranteed to be the same for the same seed value.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`OBJ`| The processed 3D model with optimized topology, returned in OBJ format.| FILE3D  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentSmartTopologyNode/en.md)

* * *

**Source fingerprint (SHA-256):** `effbccb4d239ffb6b575fc547dd54cbb61aa4508502345cb5bef1d66b320926b`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/TencentSmartTopologyNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/TencentSmartTopologyNode)

[TencentModelTo3DUVNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/TencentModelTo3DUVNode)[TencentTextToModelNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/TencentTextToModelNode)

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
