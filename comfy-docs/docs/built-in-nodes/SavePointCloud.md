---
url: https://docs.comfy.org/built-in-nodes/SavePointCloud/
title: SavePointCloud - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:59.940461+00:00
---

# SavePointCloud - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SavePointCloud/

3D

# SavePointCloud - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Save Point Cloud node saves a 3D point cloud file to the output directory and optionally provides preview data for the 3D viewer.

Copy pageCopy page

The Save Point Cloud node saves a 3D point cloud file to the output directory and optionally provides preview data for the 3D viewer. It handles file naming and saving, while also passing through camera and model information for display purposes.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model_3d`| Point cloud file (.ply)| FILE3D_POINT_CLOUD_ANY or FILE3D_PLY| Yes| -  
`filename_prefix`| Prefix for the saved file name (default: “3d/ComfyUI”)| STRING| Yes| -  
`viewport_state`| Current viewport state containing camera and model information| LOAD3D| Yes| -  
`model_3d_info`| Additional model information for the 3D viewer| LOAD3D_MODEL_INFO| No| -  
`camera_info`| Camera information for the 3D viewer| LOAD3D_CAMERA| No| -  
`width`| Width of the preview display in pixels (default: 1024)| INT| Yes| 1 to 4096  
`height`| Height of the preview display in pixels (default: 1024)| INT| Yes| 1 to 4096  
  
The saved file is written to the output directory using the `filename_prefix` with a 5-digit counter appended (for example, `3d/ComfyUI_00001.ply`). When the optional `camera_info` input is not connected, the camera information is taken from `viewport_state`; similarly, when `model_3d_info` is not connected, the model information is taken from `viewport_state` (or an empty list if none is available).

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model_3d`| The saved point cloud file| FILE3D_POINT_CLOUD_ANY  
`model_3d_info`| Model information for the 3D viewer| LOAD3D_MODEL_INFO  
`camera_info`| Camera information for the 3D viewer| LOAD3D_CAMERA  
`width`| Width of the preview display| INT  
`height`| Height of the preview display| INT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SavePointCloud/en.md)

* * *

**Source fingerprint (SHA-256):** `ce8f005c431843a57d87a4aff2eed7a1604ebdf360f83b3aaaadc3ed364d218a`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SavePointCloud.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SavePointCloud)

[SaveGLB - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SaveGLB)[VoxelToMesh - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/VoxelToMesh)

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
