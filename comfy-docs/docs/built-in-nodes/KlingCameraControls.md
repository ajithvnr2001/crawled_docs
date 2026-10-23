---
url: https://docs.comfy.org/built-in-nodes/KlingCameraControls/
title: KlingCameraControls - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:14.100250+00:00
---

# KlingCameraControls - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/KlingCameraControls/

Advanced

# KlingCameraControls - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Kling Camera Controls node allows you to configure various camera movement and rotation parameters for creating motion control effects in video generation.

Copy pageCopy page

The Kling Camera Controls node allows you to configure various camera movement and rotation parameters for creating motion control effects in video generation. It provides controls for camera positioning, rotation, and zoom to simulate different camera movements.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`camera_control_type`| Specifies the type of camera control configuration to use| COMBO| Yes| `"simple"`  
`"advanced"`  
`horizontal_movement`| Controls camera’s movement along horizontal axis (x-axis). Negative indicates left, positive indicates right (default: 0.0)| FLOAT| No| -10.0 to 10.0  
`vertical_movement`| Controls camera’s movement along vertical axis (y-axis). Negative indicates downward, positive indicates upward (default: 0.0)| FLOAT| No| -10.0 to 10.0  
`pan`| Controls camera’s rotation in vertical plane (x-axis). Negative indicates downward rotation, positive indicates upward rotation (default: 0.5)| FLOAT| No| -10.0 to 10.0  
`tilt`| Controls camera’s rotation in horizontal plane (y-axis). Negative indicates left rotation, positive indicates right rotation (default: 0.0)| FLOAT| No| -10.0 to 10.0  
`roll`| Controls camera’s rolling amount (z-axis). Negative indicates counterclockwise, positive indicates clockwise (default: 0.0)| FLOAT| No| -10.0 to 10.0  
`zoom`| Controls change in camera’s focal length. Negative indicates narrower field of view, positive indicates wider field of view (default: 0.0)| FLOAT| No| -10.0 to 10.0  
  
**Note:** At least one of the camera control parameters (`horizontal_movement`, `vertical_movement`, `pan`, `tilt`, `roll`, or `zoom`) must have a non-zero value for the configuration to be valid.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`camera_control`| Returns the configured camera control settings for use in video generation| CAMERA_CONTROL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControls/en.md)

* * *

**Source fingerprint (SHA-256):** `dbba1083b662bb2563c77dec857e4f3123e4e53d58a1d51f2646288af28ebba0`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/KlingCameraControls.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/KlingCameraControls)

[KlingCameraControlI2VNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/KlingCameraControlI2VNode)[KlingCameraControlT2VNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/KlingCameraControlT2VNode)

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
