---
url: https://docs.comfy.org/built-in-nodes/Preview3DAdvanced/
title: Preview3DAdvanced - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:44.553177+00:00
---

# Preview3DAdvanced - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Preview3DAdvanced/

3D

# Preview3DAdvanced - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node displays a 3D model preview in the UI without saving the file to the ComfyUI output directory.

Copy pageCopy page

This node displays a 3D model preview in the UI without saving the file to the ComfyUI output directory. It saves the model to a temporary file and passes through the model data, model information, camera information, and preview dimensions for further processing downstream.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model_3d`| 3D model file from an upstream 3D node.| FILE3D| Yes| GLB, GLTF, FBX, OBJ, STL, USDZ, or any supported 3D format  
`model_3d_info`| Placement of each model in the scene: position, rotation, and scale (Y-up world space). Optional. Advanced option.| LOAD3DMODELINFO| No| -  
`viewport_state`| The current viewport state containing camera and model information.| LOAD3D| Yes| -  
`camera_info`| Viewport camera information: position, look-at target, zoom, and type. Optional. Advanced option.| LOAD3DCAMERA| No| -  
`width`| Render width of the viewport in pixels. Default: 1024.| INT| Yes| 1 to 4096  
`height`| Render height of the viewport in pixels. Default: 1024.| INT| Yes| 1 to 4096  
  
Note: When `camera_info` or `model_3d_info` are not connected, their values are taken from `viewport_state` when available. If `viewport_state` contains no camera information, `camera_info` is None. If `viewport_state` has no model information, `model_3d_info` defaults to an empty list. If `viewport_state` is not a dictionary, it is treated as empty.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model_3d`| 3D model file (glb/obj/stl/etc.) from an upstream 3D node, passed through unchanged.| FILE3D  
`model_3d_info`| Placement of each model in the scene: position, rotation, and scale (Y-up world space). Uses the input value, or falls back to the value stored in `viewport_state`.| LOAD3DMODELINFO  
`camera_info`| Viewport camera information: position, look-at target, zoom, and type. Uses the input value, or falls back to the value stored in `viewport_state`.| LOAD3DCAMERA  
`width`| Render width of the viewport in pixels.| INT  
`height`| Render height of the viewport in pixels.| INT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Preview3DAdvanced/en.md)

* * *

**Source fingerprint (SHA-256):** `f2d3d35ed35fe68edebcde8fd8421d26850b04e3ae5b7147f1020c8ed904c480`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Preview3DAdvanced.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Preview3DAdvanced)

[Preview3D - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Preview3D)[Preview3DAnimation - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Preview3DAnimation)

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
