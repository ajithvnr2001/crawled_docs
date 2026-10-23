---
url: https://docs.comfy.org/built-in-nodes/Save3DAdvanced/
title: Save3DAdvanced - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:57.982072+00:00
---

# Save3DAdvanced - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Save3DAdvanced/

3D

# Save3DAdvanced - ComfyUI Built-in Node Documentation

Copy pageCopy page

Saves a 3D model to a file in the ComfyUI output directory and produces a preview of the saved scene.

Copy pageCopy page

Saves a 3D model to a file in the ComfyUI output directory and produces a preview of the saved scene. It also passes the 3D model, its placement in the scene, camera information, and viewport dimensions through to downstream nodes. When model placement or camera information are not connected, the node uses the values stored in the viewport state.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model_3d`| 3D model file from an upstream 3D node.| FILE3D| Yes| GLB  
GLTF  
FBX  
OBJ  
STL  
USDZ  
Any  
`filename_prefix`| Prefix used for the saved file name (default: “3d/ComfyUI”).| STRING| Yes| Free text  
`viewport_state`| Viewport state containing camera and model placement information, typically from a Load 3D node.| LOAD3D| Yes| -  
`model_3d_info`| Placement of each model in the scene: position, rotation, and scale (Y-up world space). Overrides the model placement stored in `viewport_state` when connected.| LOAD3DMODELINFO| No| -  
`camera_info`| Viewport camera information: position, look-at target, zoom, and type. Overrides the camera information stored in `viewport_state` when connected.| LOAD3DCAMERA| No| -  
`width`| Render width of the viewport in pixels (default: 1024).| INT| Yes| 1 to 4096  
`height`| Render height of the viewport in pixels (default: 1024).| INT| Yes| 1 to 4096  
  
Note: `model_3d_info` and `camera_info` are optional. When either input is not connected, the node falls back to the corresponding values stored in `viewport_state`.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model_3d`| The 3D model file passed through from the input.| FILE3D  
`model_3d_info`| Placement of each model in the scene: position, rotation, and scale (Y-up world space).| LOAD3DMODELINFO  
`camera_info`| Viewport camera information: position, look-at target, zoom, and type.| LOAD3DCAMERA  
`width`| The render width value passed through from the input.| INT  
`height`| The render height value passed through from the input.| INT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Save3DAdvanced/en.md)

* * *

**Source fingerprint (SHA-256):** `27cb15c5cf382e6e5b8164cfd456993404222c61d59edff2d51f9f1c8e47b25f`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Save3DAdvanced.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Save3DAdvanced)

[PreviewPointCloud - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/PreviewPointCloud)[SaveGaussianSplat - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SaveGaussianSplat)

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
