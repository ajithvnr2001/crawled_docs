---
url: https://docs.comfy.org/built-in-nodes/RenderUVAtlas/
title: RenderUVAtlas - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-18T12:01:27.021780+00:00
---

# RenderUVAtlas - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/RenderUVAtlas/

Texturing

# RenderUVAtlas - ComfyUI Built-in Node Documentation

Copy pageCopy page

Renders a mesh’s UV layout as an image. Each connected UV region (chart) is filled with a distinct color

Copy pageCopy page

Renders a mesh’s UV layout as an image. Each connected UV region (chart) is filled with a distinct color, and chart boundary edges are outlined in black on a dark gray background.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`mesh`| The 3D mesh whose UV layout will be rendered. The mesh must have UV coordinates; otherwise the node raises the error “mesh has no UVs to render. Run UnwrapMesh first.”| MESH| Yes| -  
`resolution`| The width and height, in pixels, of the rendered square image (default: 1024).| INT| Yes| 64 to 4096 (step 64)  
  
Note: If the mesh contains a batch dimension (3D UV or face arrays), only the first item in the batch is rendered.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The rendered UV atlas image, returned as a single-image batch. Each UV chart is colored, and chart boundary edges are outlined in black.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenderUVAtlas/en.md)

* * *

**Source fingerprint (SHA-256):** `b462101036418350390ffed621e583c6de14d5ea34d1e427342dc44ec3fd1922`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/RenderUVAtlas.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/RenderUVAtlas)

[MeshTextureToImage - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/MeshTextureToImage)[UnwrapMesh - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/UnwrapMesh)

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
