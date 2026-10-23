---
url: https://docs.comfy.org/built-in-nodes/MoGeRender/
title: MoGeRender - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:34.712399+00:00
---

# MoGeRender - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MoGeRender/

Geometry Estimation

# MoGeRender - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node takes a MOGEGEOMETRY packet (produced by a MoGe depth/normal estimation node) and renders it into a standard image format.

Copy pageCopy page

This node takes a MOGE_GEOMETRY packet (produced by a MoGe depth/normal estimation node) and renders it into a standard image format. You can choose to output a depth map, a colored depth map, a normal map, or a mask.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`moge_geometry`| The geometry data packet from a MoGe estimation node.| MOGE_GEOMETRY| Yes| N/A  
`output`| The type of image to render from the geometry data. `depth` outputs a grayscale depth map, `depth_colored` outputs a colored depth map, `normal_opengl` and `normal_directx` output normal maps, and `mask` outputs a mask. DirectX vs OpenGL controls the normal-map green-channel convention. DirectX: green = -Y down (Unreal). OpenGL: green = +Y up (Blender, Substance, Unity, glTF). (default: “depth”)| COMBO| Yes| `"depth"`  
`"depth_colored"`  
`"normal_opengl"`  
`"normal_directx"`  
`"mask"`  
  
**Note:** The geometry packet must contain data matching the chosen `output` mode. The `depth` and `depth_colored` modes require depth data in the packet. The `normal_opengl` and `normal_directx` modes require normal data, or points data from which normals are derived. The `mask` mode requires mask data. If the required data is missing, the node raises an error.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| The rendered image as a batch of RGB tensors. The content depends on the `output` mode: a grayscale depth map, a colored depth map, a normal map, or a mask converted to RGB. The output batch size matches the input geometry batch size.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeRender/en.md)

* * *

**Source fingerprint (SHA-256):** `ca602f7a7d6eb1b1d00986459621d94ecf9331266ff1d3ce7bb759d24448a346`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MoGeRender.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MoGeRender)

[MoGePointMapToMesh - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/MoGePointMapToMesh)[BatchMasksNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/BatchMasksNode)

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
