---
url: https://docs.comfy.org/built-in-nodes/SAM3DBody_Smooth/
title: SAM3DBody_Smooth - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:54.414316+00:00
---

# SAM3DBody_Smooth - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SAM3DBody_Smooth/

Detection

# SAM3DBody_Smooth - ComfyUI Built-in Node Documentation

Copy pageCopy page

Smooth SAM3D Body Pose Data reduces frame-to-frame jitter in a sequence of 3D body poses by averaging motion over time.

Copy pageCopy page

Smooth SAM3D Body Pose Data reduces frame-to-frame jitter in a sequence of 3D body poses by averaging motion over time. Camera and appearance data are smoothed fully, while mesh geometry is smoothed less when the subject rotates quickly, so fast spins are not flattened.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`mhr_pose_data`| The MHR pose data sequence to smooth, containing model parameters, shape parameters, expression parameters, MHR70 keypoint layout, and related mesh data.| MHR_POSE_DATA| Yes| —  
`strength`| Smoothing strength. 0 = raw, 1 = smoothed. (default: 1.0)| FLOAT| Yes| 0.0 to 1.0 (step 0.05)  
`method`| gaussian: symmetric weighted average, best general-purpose smoother.  
savgol: sliding polynomial fit, preserves sharp peaks. (default: “savgol”)| COMBO| Yes| ”gaussian"  
"savgol”  
`window`| Temporal window in frames (odd values). (default: 7)| INT| Yes| 1 to 51 (odd values, step 2)  
`rotation_threshold_degrees`| Disables smoothing for this root rotation rate (degree/frame) to preserve fast spins. 30° suits most content, low values might disable smoothing on ordinary jitter and silently impacts quality. 0 = disable. (default: 30.0)| FLOAT| Yes| 0.0 to 90.0 (step 1.0)  
  
Note: When `strength` is 0.0 or lower, or `window` is 1 or lower, the node returns the input data unchanged. The input must contain at least 2 frames and keypoint data; otherwise the node returns the input data unchanged. When `rotation_threshold_degrees` is 0.0, the rotation-based smoothing backoff is disabled.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`mhr_pose_data`| The smoothed MHR pose data sequence with reduced frame-to-frame jitter.| MHR_POSE_DATA  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3DBody_Smooth/en.md)

* * *

**Source fingerprint (SHA-256):** `a80a1c121f1d2bc49e9112576775588d5deab4690c4cd6ec9c1f98de78457b30`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SAM3DBody_Smooth.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SAM3DBody_Smooth)

[SAM3DBody_Render - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SAM3DBody_Render)[SDPoseDrawKeypoints - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SDPoseDrawKeypoints)

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
