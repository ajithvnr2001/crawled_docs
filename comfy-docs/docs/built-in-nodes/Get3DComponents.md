---
url: https://docs.comfy.org/built-in-nodes/Get3DComponents/
title: Get3DComponents - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:00.556897+00:00
---

# Get3DComponents - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Get3DComponents/

3D

# Get3DComponents - ComfyUI Built-in Node Documentation

Copy pageCopy page

Get3DComponents parses a 3D model file (GLB, GLTF, OBJ, or STL) into an editable mesh that can be used by mesh-processing nodes such as decimate, remesh

Copy pageCopy page

Get3DComponents parses a 3D model file (GLB, GLTF, OBJ, or STL) into an editable mesh that can be used by mesh-processing nodes such as decimate, remesh, UV unwrap, and bake. All scene nodes and primitives are merged into one mesh with their transforms applied, and textures and material settings come from the first material. It is the counterpart of the MeshToFile3D node.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model_3d`| 3D model file from Load 3D or another 3D node. FBX/USDZ are not supported - convert to GLB first.| File3DGLB  
File3DGLTF  
File3DOBJ  
File3DSTL  
File3DAny| Yes| GLB  
GLTF  
OBJ  
STL  
  
Note: FBX and USDZ files are not supported and cause an error; convert them to GLB or GLTF first. If the file format cannot be recognized as GLB, GLTF, OBJ, or STL, the node raises an error listing the supported formats. If the glTF scene contains no triangle geometry, or if the file contains face indices that point outside the vertex list (a sign of a corrupt file), the node raises an error. If the 3D file contains multiple materials, only the first material’s textures and material factors are kept (a warning is logged). All scene primitives are merged into a single mesh with their transforms applied. This node is experimental.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`mesh`| Editable mesh containing vertices, faces, UVs, vertex colors, normals, and tangents, plus material information taken from the file (texture, metallic-roughness, normal map, emissive color, unlit flag, occlusion-in-metallic-roughness flag, and material data).| MESH  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Get3DComponents/en.md)

* * *

**Source fingerprint (SHA-256):** `f2cdc9767a50503988484f09d2b3d110caf086b8cd84f65034a4a1e17a94405e`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Get3DComponents.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Get3DComponents)

[CreateCameraInfo - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/CreateCameraInfo)[Load3D - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Load3D)

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
