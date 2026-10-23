---
url: https://docs.comfy.org/built-in-nodes/SAM3DBody_Predict/
title: SAM3DBody_Predict - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:54.103154+00:00
---

# SAM3DBody_Predict - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SAM3DBody_Predict/

Detection

# SAM3DBody_Predict - ComfyUI Built-in Node Documentation

Copy pageCopy page

SAM3D Body Prediction runs 3D body and hand pose estimation on input images, detecting one or more people per frame.

Copy pageCopy page

SAM3D Body Prediction runs 3D body and hand pose estimation on input images, detecting one or more people per frame. Tracking data or bounding boxes can be supplied to improve detection; when neither is provided, the node falls back to full-frame single-person detection.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`sam3d_body_model`| The SAM3D body model to use for prediction.| SAM3D_BODY_MODEL| Yes| —  
`image`| Image or batch of images to run body prediction on.| IMAGE| Yes| —  
`track_data`| Tracking data from SAM3 Video Track, required for multi-person detection.| SAM3_TRACK_DATA| No| —  
`bboxes`| Per-frame bounding boxes used for better detection. Can be used as an alternative to tracking data.| BBOX| No| —  
`run_hand_refinement`| Improves hand pose at the cost of extra inference time and memory use. Default: true.| BOOLEAN| No| true  
false  
`fov`| Vertical FoV in degrees. Affects predicted depth and absolute scale. 0 = fall back to ~53° (16:9). Default: 0.0.| FLOAT| No| 0.0 or greater  
`batch_size`| Max person crops to process as a batch. Larger values use more VRAM for faster inference. Default: 64.| INT| No| 1 to 512  
  
Note: When `track_data` is provided, it takes precedence over `bboxes`. If neither `track_data` nor `bboxes` is provided, the node falls back to single-person full-frame detection. Bounding boxes can be provided for a single frame (applied to every frame) or per frame.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`mhr_pose_data`| Body pose data bundle containing per-frame pose detection results, face geometry, the input image size, canonical vertex colors, and a hand vertex mask.| MHR_POSE_DATA  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3DBody_Predict/en.md)

* * *

**Source fingerprint (SHA-256):** `f1039349cd2809423053bffde1c7d119c7c42f217327d23c608b1224d183770e`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SAM3DBody_Predict.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SAM3DBody_Predict)

[SAM3DBody_Loader - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SAM3DBody_Loader)[SAM3DBody_Render - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SAM3DBody_Render)

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
