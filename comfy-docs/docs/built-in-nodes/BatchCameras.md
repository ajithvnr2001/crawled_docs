---
url: https://docs.comfy.org/built-in-nodes/BatchCameras/
title: Batch Cameras - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-15T14:35:53.450796+00:00
---

# Batch Cameras - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/BatchCameras/

3D

# Batch Cameras - ComfyUI Built-in Node Documentation

Copy pageCopy page

Joins cameras and camera orbits into one camera list, in input order.

Copy pageCopy page

Joins cameras and camera orbits into one camera list, in input order. Render Mesh and Render Splat render one image per camera in the list, which is how a multi-view render is built.

## Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`cameras`| Growable slot of cameras, from Create Camera Info, Create Camera Orbit or a viewer. A camera list counts as every camera in it.| AUTOGROW| Yes| 1 to 50 cameras  
  
## Outputs

Output Name| Description| Data Type  
---|---|---  
`camera_info`| One camera list holding every input camera, in input order.| LOAD3D_CAMERA  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchCameras/en.md)

* * *

**Source fingerprint (SHA-256):** `a5ddae7f539a2d70efc1b156f7b4ec4b219d7cf78544b882f7b8f9538ae9a88d`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/BatchCameras.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/BatchCameras)

[Unwrap Mesh UVs](https://docs.comfy.org/built-in-nodes/UnwrapMesh)[Create 3D Animation File](https://docs.comfy.org/built-in-nodes/BuildPoseFile)
