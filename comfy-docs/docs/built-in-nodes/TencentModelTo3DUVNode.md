---
url: https://docs.comfy.org/built-in-nodes/TencentModelTo3DUVNode/
title: TencentModelTo3DUVNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:07.996883+00:00
---

# TencentModelTo3DUVNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/TencentModelTo3DUVNode/

Tencent

# TencentModelTo3DUVNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node uses the Tencent Hunyuan3D API to perform UV unfolding on a 3D model.

Copy pageCopy page

This node uses the Tencent Hunyuan3D API to perform UV unfolding on a 3D model. It takes a 3D model file as input, sends it to the API for processing, and returns the processed model in OBJ and FBX formats along with a generated UV texture image. The input model must have fewer than 30,000 faces.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model_3d`| Input 3D model (GLB, OBJ, or FBX). The model must have less than 30000 faces.| FILE3D| Yes| GLB  
OBJ  
FBX  
`seed`| Seed controls whether the node should re-run; results are non-deterministic regardless of seed. (default: 1)| INT| No| 0 to 2147483647  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`OBJ`| The processed 3D model file in OBJ format.| FILE3D  
`FBX`| The processed 3D model file in FBX format.| FILE3D  
`uv_image`| The generated UV texture image.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentModelTo3DUVNode/en.md)

* * *

**Source fingerprint (SHA-256):** `b69519df055043555ab7f4d75cfb3b77b9011d5a8e93d0b3ba30c7a8674bd2cb`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/TencentModelTo3DUVNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/TencentModelTo3DUVNode)

[TencentImageToModelNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/TencentImageToModelNode)[TencentSmartTopologyNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/TencentSmartTopologyNode)

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
