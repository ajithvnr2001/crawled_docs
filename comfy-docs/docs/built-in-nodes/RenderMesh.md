---
url: https://docs.comfy.org/built-in-nodes/RenderMesh/
title: RenderMesh - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:50.329530+00:00
---

# RenderMesh - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/RenderMesh/

Mesh

# RenderMesh - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node renders a 3D mesh into a 2D image by ray-casting a single view.

Copy pageCopy page

This node renders a 3D mesh into a 2D image by ray-casting a single view. It can output the textured mesh, vertex colors, a solid shaded surface, surface normals, or depth. The camera and optional model transform can come from a Load3D / Preview3D viewer; if no camera is connected, a default front view is auto-framed.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`mesh`| The 3D mesh to render.| MESH| Yes| —  
`mode`| What to render. auto: texture if present, else vertex colours, else shaded clay. (default: “auto”)| COMBO| Yes| `"auto"`  
`"texture"`  
`"vertex colors"`  
`"solid"`  
`"normal"`  
`"depth"`  
`width`| Width of the rendered image in pixels. (default: 1024)| INT| Yes| 64 to 4096 (step 8)  
`height`| Height of the rendered image in pixels. (default: 1024)| INT| Yes| 64 to 4096 (step 8)  
`background`| Background color used for pixels the mesh does not cover. (default: “#000000”)| COLOR| Yes| —  
`model_3d_info`| Model transform from the same Load3D / Preview3D viewer. Connect it with camera_info to match the viewer framing.| LOAD3D_MODEL_INFO| No| —  
`camera_info`| Camera from a Load3D / Preview3D viewer or a Create Camera Info node. If none is connected, a default front view is auto-framed.| LOAD3D_CAMERA| No| —  
  
Note: Only the first item of a batched mesh is rendered — if the mesh batch contains more than one item, the node logs a warning and uses the first one. The `texture` mode requires the mesh to have both a texture and UVs, and the `vertex colors` mode requires vertex colors; if the data for the selected mode is not available, the node falls back to the solid shaded render. The `normal` mode uses the mesh’s smooth vertex normals when present, otherwise the per-face normal. In `depth` mode, closer surfaces appear brighter (near = white) and pixels not covered by the mesh stay black. The `model_3d_info` and `camera_info` are meant to be connected together from the same Load3D / Preview3D viewer so the render matches the viewer framing.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The rendered image of the mesh.| IMAGE  
`mask`| A mask that is 1.0 where the mesh was rendered and 0.0 elsewhere.| MASK  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenderMesh/en.md)

* * *

**Source fingerprint (SHA-256):** `d23e85a904520eb2dfed899eb3e6a9cf45c980df00c034503687ac4eccc66ac4`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/RenderMesh.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/RenderMesh)

[RemeshMesh - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/RemeshMesh)[RotateMesh - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/RotateMesh)

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
