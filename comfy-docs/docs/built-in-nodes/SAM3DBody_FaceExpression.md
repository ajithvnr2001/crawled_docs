---
url: https://docs.comfy.org/built-in-nodes/SAM3DBody_FaceExpression/
title: SAM3DBody_FaceExpression - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:54.007951+00:00
---

# SAM3DBody_FaceExpression - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SAM3DBody_FaceExpression/

Detection

# SAM3DBody_FaceExpression - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node adds facial expressions to a SAM3D body by detecting faces in an image with the MediaPipe Face Landmarker

Copy pageCopy page

This node adds facial expressions to a SAM3D body by detecting faces in an image with the MediaPipe Face Landmarker, matching each detected face to a tracked person, and mapping the 52 ARKit blendshapes onto MHR’s 72-axis expression parameters. It then re-runs the body model so the output mesh vertices and keypoints reflect the new expression.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`sam3d_body_model`| The SAM3D body model containing the face landmark detector used to detect faces and regenerate the body mesh.| SAM3D_BODY_MODEL| Yes| -  
`mhr_pose_data`| Pose data containing per-frame tracked persons with bounding boxes, keypoints, and expression parameters. The node matches each detected face to a person and writes updated expression parameters into this data.| MHR_POSE_DATA| Yes| -  
`image`| Image frames used to detect faces. If the image batch has fewer frames than the pose data, the last frame is reused for the remaining frames.| IMAGE| Yes| -  
`strength`| Global multiplier on all blendshapes. >1 exaggerates. Default: 1.0.| FLOAT| No| 0.0 to 4.0 (step 0.05, default 1.0)  
`mouth_strength`| Multiplier on mouth/jaw shapes. MediaPipe’s jawOpen saturates near 1.0. Default: 1.0.| FLOAT| No| 0.0 to 4.0 (step 0.05, default 1.0)  
`eye_strength`| Multiplier on eye shapes. MediaPipe rarely exceeds 0.5; 2-3x often needed. Default: 2.0.| FLOAT| No| 0.0 to 4.0 (step 0.05, default 2.0)  
`brow_strength`| Multiplier on brow/cheek/sneer shapes. MediaPipe outputs ~0.1-0.3; 2-3x. Default: 2.0.| FLOAT| No| 0.0 to 4.0 (step 0.05, default 2.0)  
`input_threshold`| Deadzone on MediaPipe’s raw output (below = zero, above = linear remap). Default: 0.02.| FLOAT| No| 0.0 to 0.5 (step 0.01, default 0.02)  
`blendshape_smooth_window`| Gaussian window on MediaPipe’s per-frame signal before MHR mapping. MediaPipe’s raw output swings 30-70% frame-to-frame on static faces. 1 = disabled. Use odd values. Default: 7.| INT| No| 1 to 31 (step 2, default 7)  
  
Note: A per-clip baseline subtraction is applied only when at least 30 frames in the clip contain detected persons. Detection gaps of up to 12 frames per person are filled by interpolation.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`mhr_pose_data`| The updated pose data. Each tracked person’s expression parameters are replaced with the mapped face expression, and the mesh vertices and keypoints are regenerated to match.| MHR_POSE_DATA  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3DBody_FaceExpression/en.md)

* * *

**Source fingerprint (SHA-256):** `b2299e51be3556e639d5b04fcbee541ecf41e0d84c2c8a0fd4e211b2f6caba0b`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SAM3DBody_FaceExpression.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SAM3DBody_FaceExpression)

[SAM3_VideoTrack - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SAM3_VideoTrack)[SAM3DBody_Loader - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SAM3DBody_Loader)

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
