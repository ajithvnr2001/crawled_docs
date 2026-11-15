---
url: https://docs.comfy.org/built-in-nodes/CreateCameraOrbit/
title: Create Camera Orbit - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-15T14:35:53.718337+00:00
---

# Create Camera Orbit - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/CreateCameraOrbit/

3D

# Create Camera Orbit - ComfyUI Built-in Node Documentation

Copy pageCopy page

Builds a rig of cameras around the first camera’s target: a turntable by default, a tilted sweep when pitch is set, and optionally views straight down and up.

Copy pageCopy page

Builds a rig of cameras around the first camera’s target: a turntable by default, a tilted sweep when `pitch` is set, and optionally views straight down and up. Render Mesh renders one image per camera and Bake Texture From Views projects them back onto the mesh.

## Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`camera_info`| First camera of the orbit. A camera list orbits every camera in it.| LOAD3D_CAMERA| Yes| -  
`count`| Cameras evenly spaced along the sweep. Default: 4.| INT| Yes| 1 to 64  
`yaw`| Total turn around the target, in Create Camera Info’s yaw direction. Whole turns stop one step short of the first camera; other sweeps end on the last camera. Default: 360.0.| FLOAT| Yes| -720.0 to 720.0 (step 1.0)  
`pitch`| Total tilt over the target, positive rising like Create Camera Info’s pitch; past 90 the cameras pass over the top. Whole turns loop like `yaw`. Default: 0.0.| FLOAT| Yes| -720.0 to 720.0 (step 1.0)  
`poles`| Views straight down and/or up at the target, added after the orbit. Their image top points away from the first camera. Default: `"none"`.| COMBO| Yes| `"none"`  
`"top"`  
`"bottom"`  
`"top and bottom"`  
  
## Outputs

Output Name| Description| Data Type  
---|---|---  
`camera_info`| The camera list of the rig, in orbit order followed by the pole views.| LOAD3D_CAMERA  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateCameraOrbit/en.md)

* * *

**Source fingerprint (SHA-256):** `b251efc969f8db7cf03527594be3bbd2af037f1ebb56bdf508bf264ddd9f8c08`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/CreateCameraOrbit.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/CreateCameraOrbit)

[Create Camera Info](https://docs.comfy.org/built-in-nodes/CreateCameraInfo)[Get 3D Components](https://docs.comfy.org/built-in-nodes/Get3DComponents)
