---
url: https://docs.comfy.org/built-in-nodes/Load3DAdvanced/
title: Load3DAdvanced - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:22.571559+00:00
---

# Load3DAdvanced - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Load3DAdvanced/

3D

# Load3DAdvanced - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Load 3D (Advanced) node loads a 3D model file from ComfyUI’s input/3d directory and provides the model data together with model placement and camera

Copy pageCopy page

The Load 3D (Advanced) node loads a 3D model file from ComfyUI’s `input/3d` directory and provides the model data together with model placement and camera information captured in the 3D viewer’s viewport state. It supports common 3D file formats and lets you set the render width and height of the viewport in pixels. This node is experimental.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model_file`| The 3D model file to load. Select “none” to skip loading a model file. Files can also be uploaded through the widget.| COMBO| Yes| `"none"`  
Available 3D model files in the `input/3d` directory  
`viewport_state`| The current viewport state containing camera and model information from the 3D viewer.| LOAD3D| Yes| -  
`width`| Render width of the viewport in pixels (default: 1024).| INT| Yes| Min: 1  
Max: 4096  
Default: 1024  
Step: 1  
`height`| Render height of the viewport in pixels (default: 1024).| INT| Yes| Min: 1  
Max: 4096  
Default: 1024  
Step: 1  
  
**Notes on Parameters:**

  * The `model_file` parameter only lists files with the following extensions: .gltf, .glb, .obj, .fbx, .stl
  * Files must be placed in the `input/3d` directory of your ComfyUI installation; subfolders are searched as well, and file paths are shown relative to the input directory
  * If `model_file` is “none”, no model data is loaded and the `model_3d` output will be empty
  * If `model_file` is set to a file that does not exist, the node returns a validation error: “Invalid 3D model file: {model_file}”
  * If `viewport_state` is not a valid viewport state object, it is treated as empty, so `model_3d_info` becomes an empty list and `camera_info` is returned as empty



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model_3d`| Loaded 3D model file (glb/obj/stl/etc.). Empty if no model file was selected.| FILE3DANY  
`model_3d_info`| Placement of each model in the scene: position, rotation, and scale (Y-up world space).| LOAD3DMODELINFO  
`camera_info`| Viewport camera information: position, look-at target, zoom, and type.| LOAD3DCAMERA  
`width`| Render width of the viewport in pixels.| INT  
`height`| Render height of the viewport in pixels.| INT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Load3DAdvanced/en.md)

* * *

**Source fingerprint (SHA-256):** `c79c53dde0c8b3afb7df7b972df749f5040c92d48b47e355c4497d9b0cbf1c22`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Load3DAdvanced.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Load3DAdvanced)

[Load3D - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Load3D)[Load3DAnimation - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Load3DAnimation)

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
