---
url: https://docs.comfy.org/built-in-nodes/CameraAngle/
title: CameraAngle - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:33.865313+00:00
---

# CameraAngle - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/CameraAngle/

3D

# CameraAngle - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node picks a camera angle around a subject and turns that choice into two things: a camerainfo structure that 3D nodes can render

Copy pageCopy page

This node picks a camera angle around a subject and turns that choice into two things: a `camera_info` structure that 3D nodes can render, and a plain-English shot description you can paste into a prompt. The subject sits at the origin of the scene, where downstream 3D nodes centre their models, so the angle you pick here matches the preview. Use it to frame a render before generating, or to describe a viewpoint such as `front view eye-level shot medium shot` for an image or video model. The 3D preview in the node shows the resulting camera position.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`horizontal_angle`| Azimuth around the subject in degrees: 0 is the front, 90 the right side, and 180 the back. (default: 0)| INT| Yes| 0 to 360  
`vertical_angle`| Elevation in degrees. Negative values look up from below, positive values look down from above. (default: 0)| INT| Yes| -30 to 60  
`zoom`| Lens zoom on the subject: 0 is a wide shot, 10 a close-up. The value is also carried into `camera_info.zoom`. (default: 5.0)| FLOAT| Yes| 0.0 to 10.0 (step 0.1)  
`image`| Optional reference image, shown on the front of the subject cube in the 3D preview.| IMAGE| No| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`camera_info`| Camera information for 3D nodes: position, look-at target, zoom factor, camera type, and field of view. The camera keeps a fixed 35 degree field of view and is placed 6 units from the target.| LOAD3DCAMERA  
`prompt`| Short shot description built from the angle, the elevation, and the distance, for example `front view eye-level shot medium shot`.| STRING  
  
## 

​

Shot Description Terms

The `prompt` output combines one term from each group below. Values are clamped to the widget ranges first.

  * Horizontal angle is split into eight 45 degree sectors: `front view`, `front-right quarter view`, `right side view`, `back-right quarter view`, `back view`, `back-left quarter view`, `left side view`, `front-left quarter view`.
  * Vertical angle becomes `low-angle shot` below -15 degrees, `eye-level shot` below 15, `elevated shot` below 45, and `high-angle shot` from 45 degrees up.
  * Zoom becomes `wide shot` below 2, `medium shot` below 6, and `close-up` at 6 or more.

The `camera_info.zoom` factor scales the widget value onto 1.0 to 1.875, so zoom 0 gives 1.0 and zoom 10 gives 1.875.

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CameraAngle/en.md)

* * *

**Source fingerprint (SHA-256):** `8ed2cd186bc6ca02dbc8da006b2e9156245ef691a2257f286f6e32ffa480fd5d`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/CameraAngle.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/CameraAngle)

[BuildPoseFile - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/BuildPoseFile)[CreateCameraInfo - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/CreateCameraInfo)

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
