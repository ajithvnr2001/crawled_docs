---
url: https://docs.comfy.org/built-in-nodes/Tencent3DTextureEditNode/
title: Tencent3DTextureEditNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:07.915670+00:00
---

# Tencent3DTextureEditNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Tencent3DTextureEditNode/

Tencent

# Tencent3DTextureEditNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node uses the Tencent Hunyuan3D API to edit the textures of a 3D model.

Copy pageCopy page

This node uses the Tencent Hunyuan3D API to edit the textures of a 3D model. You provide a 3D model and a text description of the desired changes, and the node returns a new version of the model with its textures redrawn according to your prompt.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model_3d`| 3D model in FBX format. Model should have less than 100000 faces.| FILE3D| Yes| FBX, Any  
`prompt`| Describes texture editing. Supports up to 1024 UTF-8 characters.| STRING| Yes|   
`seed`| Seed controls whether the node should re-run; results are non-deterministic regardless of seed. (default: 0)| INT| No| 0 to 2147483647  
  
**Note:** The `model_3d` input must be a file in the FBX format. Other 3D file formats are not supported by this node. The `prompt` parameter is required and must be between 1 and 1024 characters in length.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`GLB`| The processed 3D model in GLB format.| FILE3D  
`OBJ`| The processed 3D model in OBJ format.| FILE3D  
`texture_image`| The newly generated texture image for the 3D model.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Tencent3DTextureEditNode/en.md)

* * *

**Source fingerprint (SHA-256):** `eedddc8bd47a4af6e45a516f2817e7c1dded575d9e28ea9b66a1d7a39b93526c`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Tencent3DTextureEditNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Tencent3DTextureEditNode)

[Tencent3DPartNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Tencent3DPartNode)[TencentImageToModelNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/TencentImageToModelNode)

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
