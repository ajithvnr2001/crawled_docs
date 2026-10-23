---
url: https://docs.comfy.org/built-in-nodes/TripoImportModelNode/
title: TripoImportModelNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:12.933685+00:00
---

# TripoImportModelNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/TripoImportModelNode/

Tripo

# TripoImportModelNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node imports an external 3D model into Tripo so that Tripo post-processing nodes, such as Texture, Rig, and Convert, can use it.

Copy pageCopy page

This node imports an external 3D model into Tripo so that Tripo post-processing nodes, such as Texture, Rig, and Convert, can use it. The node uploads the file to Tripo and returns a task ID that identifies the imported model for use by those nodes. GLB is recommended because textures are preserved only when embedded in the file, and texturing an imported model requires a texture prompt. This node is free to use.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model_3d`| 3D model to import (GLB / FBX / OBJ / STL, up to 150 MB). OBJ and STL files carry no embedded textures.| FILE3D| Yes| GLB  
FBX  
OBJ  
STL  
Any 3D format  
  
**Note:** Only GLB, FBX, OBJ, and STL formats are supported. GLTF (.gltf) cannot be imported because it references external files; export a single-file GLB instead. The model file must be 150 MB or smaller. GLB is recommended because textures survive import only when embedded in the file. OBJ and STL files do not carry embedded textures. Texturing an imported model requires a texture prompt.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model task_id`| A task ID that identifies the imported model, for use with Tripo post-processing nodes| MODEL_TASK_ID  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImportModelNode/en.md)

* * *

**Source fingerprint (SHA-256):** `bf91e964c5705f7377868dd06bbf5d57b41cc3607fc377cd45886d3d6c5ceddc`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/TripoImportModelNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/TripoImportModelNode)

[TripoImageToMultiviewNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/TripoImageToMultiviewNode)[TripoMeshCompleteNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/TripoMeshCompleteNode)

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
