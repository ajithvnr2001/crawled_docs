---
url: https://docs.comfy.org/built-in-nodes/KlingCameraControlT2VNode/
title: KlingCameraControlT2VNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:13.990344+00:00
---

# KlingCameraControlT2VNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/KlingCameraControlT2VNode/

Advanced

# KlingCameraControlT2VNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Kling Text to Video Camera Control Node transforms text into cinematic videos with professional camera movements that simulate real-world cinematography.

Copy pageCopy page

Kling Text to Video Camera Control Node transforms text into cinematic videos with professional camera movements that simulate real-world cinematography. This node supports controlling virtual camera actions including zoom, rotation, pan, tilt, and first-person view while maintaining focus on your original text. The duration, mode, and model name are hard-coded because camera control is only supported in pro mode with the kling-v1-5 model at 5-second duration.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Positive text prompt| STRING| Yes| -  
`negative_prompt`| Negative text prompt| STRING| Yes| -  
`cfg_scale`| Controls how closely the output follows the prompt (default: 0.75)| FLOAT| No| 0.0-1.0  
`aspect_ratio`| The aspect ratio for the generated video (default: “16:9”)| COMBO| No| ”16:9"  
"9:16"  
"1:1"  
"21:9"  
"3:4"  
"4:3”  
`camera_control`| Can be created using the Kling Camera Controls node. Controls the camera movement and motion during the video generation.| CAMERA_CONTROL| No| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated video with camera control effects| VIDEO  
`video_id`| The unique identifier for the generated video| STRING  
`duration`| The duration of the generated video| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControlT2VNode/en.md)

* * *

**Source fingerprint (SHA-256):** `7975d97c4f9242a9ae3c17be03696d174a2495bd53fb9fc4405f86c44167fa21`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/KlingCameraControlT2VNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/KlingCameraControlT2VNode)

[KlingCameraControls - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/KlingCameraControls)[KlingDualCharacterVideoEffectNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/KlingDualCharacterVideoEffectNode)

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
