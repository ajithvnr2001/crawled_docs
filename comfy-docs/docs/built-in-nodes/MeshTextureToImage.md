---
url: https://docs.comfy.org/built-in-nodes/MeshTextureToImage/
title: MeshTextureToImage - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:31.155779+00:00
---

# MeshTextureToImage - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MeshTextureToImage/

Texturing

# MeshTextureToImage - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node extracts a mesh’s baked textures and returns them as separate images: base color, metallic, roughness, occlusion, and normal map.

Copy pageCopy page

This node extracts a mesh’s baked textures and returns them as separate images: base color, metallic, roughness, occlusion, and normal map. Texture channels that were not baked come back as neutral defaults — white for occlusion and a flat blue for the normal map.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`mesh`| The mesh whose baked textures are extracted. The mesh must have a base color texture; meshes that only have vertex colors (for example after a PaintMesh node) do not contain a texture and cause an error.| MESH| Yes| —  
  
Note: The mesh must have a baked base color texture. If it does not, the node raises an error and recommends running BakeTextureFromVoxel first. When the metallic-roughness texture is missing, the `metallic` and `roughness` outputs are black (0). The `occlusion` output is white unless the mesh contains baked ambient occlusion (the mesh’s occlusion-in-metallic-roughness flag is set). The `normal_map` output is a flat neutral blue when no normal map was baked.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`base_color`| The base color texture of the mesh as an image.| IMAGE  
`metallic`| The metallic channel from the mesh’s occlusion-roughness-metallic texture, as a grayscale image. Black (0) means non-metallic, white (1) means fully metallic. Black when the texture is missing.| IMAGE  
`roughness`| The roughness channel from the mesh’s occlusion-roughness-metallic texture, as a grayscale image. Black when the texture is missing.| IMAGE  
`occlusion`| The ambient occlusion channel from the mesh’s occlusion-roughness-metallic texture, as a grayscale image. White (no occlusion) when ambient occlusion was not baked.| IMAGE  
`normal_map`| The normal map texture of the mesh. A flat neutral normal map (0.5, 0.5, 1.0, appearing as flat blue) when no normal map was baked.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshTextureToImage/en.md)

* * *

**Source fingerprint (SHA-256):** `775fd50601ed9ebfc48abf1832c58acbac0f48b5faaebb5f7f46ae4a501278c4`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MeshTextureToImage.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MeshTextureToImage)

[BakeTextureFromVoxel - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/BakeTextureFromVoxel)[RenderUVAtlas - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/RenderUVAtlas)

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
