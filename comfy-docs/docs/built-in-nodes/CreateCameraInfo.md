---
url: https://docs.comfy.org/built-in-nodes/CreateCameraInfo/
title: CreateCameraInfo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:45.149734+00:00
---

# CreateCameraInfo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/CreateCameraInfo/

3D

# CreateCameraInfo - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Create Camera Info node builds a camera information structure for 3D rendering.

Copy pageCopy page

The Create Camera Info node builds a camera information structure for 3D rendering. It supports three modes for defining the camera: orbit (yaw/pitch/distance around a target), look_at (explicit world position), and quaternion (position plus rotation). The coordinate system is right-handed with Y as the up axis.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`mode`| How to define the camera: orbit angles, an explicit position, or a position + quaternion.| DYNAMIC_COMBO| Yes| `"orbit"`  
`"look_at"`  
`"quaternion"`  
`target_x`| Look-at point (orbit pivot / aim). In orbit mode, move it to pan/translate the whole camera. Ignored in quaternion mode. Defaults to the origin. (default: 0.0)| FLOAT| No| -1000.0 to 1000.0  
`target_y`| Y component of the target point. (default: 0.0)| FLOAT| No| -1000.0 to 1000.0  
`target_z`| Z component of the target point. (default: 0.0)| FLOAT| No| -1000.0 to 1000.0  
`roll`| Camera roll about the view axis, in degrees. (default: 0.0)| FLOAT| No| -180.0 to 180.0  
`fov`| Vertical field of view in degrees. (default: 35.0)| FLOAT| No| 1.0 to 120.0  
`zoom`| Digital zoom (focal-length multiplier). Values greater than 1 zoom in without moving the camera. (default: 1.0)| FLOAT| No| 0.01 to 100.0  
`camera_type`| Projection used by Render Splat: perspective (foreshortening) or orthographic (parallel). (default: “perspective”)| COMBO| No| `"perspective"`  
`"orthographic"`  
  
### 

​

Mode-Specific Parameters

When `mode` is set to `"orbit"`, the following parameters become available:

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`yaw`| Horizontal rotation angle around the target. (default: 35.0)| FLOAT| Yes| -360.0 to 360.0  
`pitch`| Vertical rotation angle around the target. (default: 30.0)| FLOAT| Yes| -89.0 to 89.0  
`distance`| Camera distance from the target. (default: 4.0)| FLOAT| Yes| 0.01 to 1000.0  
  
When `mode` is set to `"look_at"`, the following parameters become available:

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`position_x`| Camera position in world space (right-handed, Y-up). (default: 4.0)| FLOAT| Yes| -1000.0 to 1000.0  
`position_y`| Y component of the camera position. (default: 4.0)| FLOAT| Yes| -1000.0 to 1000.0  
`position_z`| Z component of the camera position. (default: 4.0)| FLOAT| Yes| -1000.0 to 1000.0  
  
When `mode` is set to `"quaternion"`, the following parameters become available:

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`position_x`| Camera position in world space (right-handed, Y-up). (default: 4.0)| FLOAT| Yes| -1000.0 to 1000.0  
`position_y`| Y component of the camera position. (default: 4.0)| FLOAT| Yes| -1000.0 to 1000.0  
`position_z`| Z component of the camera position. (default: 4.0)| FLOAT| Yes| -1000.0 to 1000.0  
`quat_x`| X component of the camera world-rotation quaternion. (default: 0.0)| FLOAT| Yes| -1.0 to 1.0  
`quat_y`| Y component of the camera world-rotation quaternion. (default: 0.0)| FLOAT| Yes| -1.0 to 1.0  
`quat_z`| Z component of the camera world-rotation quaternion. (default: 0.0)| FLOAT| Yes| -1.0 to 1.0  
`quat_w`| Camera world-rotation quaternion (three.js: looks down local -Z). Normalized for you. (default: 1.0)| FLOAT| Yes| -1.0 to 1.0  
  
**Note:** The `target_x`, `target_y`, and `target_z` parameters are ignored when `mode` is set to `"quaternion"`. In `"orbit"` mode, these target parameters define the pivot point around which the camera orbits.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`camera_info`| Camera information structure containing position, rotation, field of view, zoom, and projection type for 3D rendering.| LOAD3DCAMERA  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateCameraInfo/en.md)

* * *

**Source fingerprint (SHA-256):** `5a9703e8e01ad2cd92a97da8d892c278765a9cef8bcd38e3336d1f73717d9895`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/CreateCameraInfo.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/CreateCameraInfo)

[CameraAngle - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/CameraAngle)[Get3DComponents - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Get3DComponents)

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
