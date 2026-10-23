---
url: https://docs.comfy.org/built-in-nodes/ApplyTextureToMesh/
title: ApplyTextureToMesh - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:19.995439+00:00
---

# ApplyTextureToMesh - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ApplyTextureToMesh/

Texturing

# ApplyTextureToMesh - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node attaches baked texture images to a mesh’s UV layout so they can be exported together with the mesh by the SaveGLB node.

Copy pageCopy page

This node attaches baked texture images to a mesh’s UV layout so they can be exported together with the mesh by the SaveGLB node. Feed it the same UV-unwrapped mesh you baked the textures from, along with the baked image maps. Optional metallic, roughness, and occlusion maps are packed into a single ORM texture, and supplying a normal map also stores the smooth vertex normals and tangent basis needed for correct shading.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`mesh`| The UV-unwrapped mesh that the baked textures will be attached to. Must be the same mesh used during baking; an error is raised if the mesh has no UVs.| MESH| Yes| —  
`base_color`| The baked base color image. Stored as the mesh’s texture and clamped to the 0-1 range.| IMAGE| Yes| —  
`metallic`| The baked metallic map. Used as the blue channel of the combined ORM texture; defaults to 0 when not provided.| IMAGE| No| —  
`roughness`| The baked roughness map. Used as the green channel of the combined ORM texture; defaults to 1 when not provided.| IMAGE| No| —  
`occlusion`| The baked ambient occlusion map. Used as the red channel of the combined ORM texture; defaults to 1 when not provided. When provided, the ORM texture is also flagged as the occlusion texture for SaveGLB.| IMAGE| No| —  
`normal_map`| The baked tangent-space normal map. When provided, the node recomputes the per-vertex tangents and exports smooth vertex normals so the normal map shades correctly.| IMAGE| No| —  
  
Note: The `mesh` input must have UV coordinates; if it does not, the node raises an error asking you to connect the same UV-unwrapped mesh used for baking. Note: When any of `metallic`, `roughness`, or `occlusion` is connected, all three are packed into a single glTF ORM texture with channels R = occlusion, G = roughness, B = metallic. Missing maps are filled with defaults (occlusion 1, roughness 1, metallic 0), and maps with different resolutions are resized to the largest width and height among the provided maps. Note: When `normal_map` is connected, the mesh’s stored normals are replaced with computed smooth vertex normals and a per-vertex tangent basis is added. UV coordinates that fall outside the [0,1] range are uniformly scaled into [0,1] while preserving aspect ratio; a warning is logged if the UV span looks like a tiled/UDIM layout. For batched meshes, UV normalization is applied separately to each item in the batch using the same logic as the bake step, so both stay aligned.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`mesh`| The input mesh with the texture images attached to its UV layout, ready to be saved by SaveGLB.| MESH  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ApplyTextureToMesh/en.md)

* * *

**Source fingerprint (SHA-256):** `7492922c9c7c0117366cb8b9017fc192eb8dd6b6594fd429044d60408693210e`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ApplyTextureToMesh.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ApplyTextureToMesh)

[TransformSplat - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/TransformSplat)[BakeAmbientOcclusion - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/BakeAmbientOcclusion)

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
