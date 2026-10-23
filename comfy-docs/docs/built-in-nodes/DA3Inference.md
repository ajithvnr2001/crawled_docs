---
url: https://docs.comfy.org/built-in-nodes/DA3Inference/
title: DA3Inference - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:49.815796+00:00
---

# DA3Inference - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/DA3Inference/

Geometry Estimation

# DA3Inference - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node runs the Depth Anything 3 model on an image to estimate depth and geometry information.

Copy pageCopy page

This node runs the Depth Anything 3 model on an image to estimate depth and geometry information. In multi-view mode, multiple images are processed together as separate views of the same scene to produce geometrically consistent depth maps and camera poses.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`da3_model`| The Depth Anything 3 model to use for inference| DA3_MODEL| Yes| -  
`image`| Input image or images to process| IMAGE| Yes| -  
`resolution`| Resolution the model runs at (longest side, multiple of 14). Lower values are faster and use less VRAM. Higher values produce more detail. The output is upsampled back to the original size (default: 504)| INT| Yes| 140 to 2520 (step: 14)  
`resize_method`| upper_bound_resize: scale so the longest side equals the resolution (caps memory, default). lower_bound_resize: scale so the shortest side equals the resolution (preserves more detail on tall/wide images, uses more memory)| COMBO| Yes| `"upper_bound_resize"`  
`"lower_bound_resize"`  
`mode`| mono: single view image processing (works with any model variant). multiview: all images processed together for geometric consistency and camera pose estimation (for Small and Base models only)| COMBO| Yes| `"mono"`  
`"multiview"`  
`ref_view_strategy`| Which view acts as the geometric anchor in multi-view mode. saddle_balanced: the view most average across all others (best general choice). saddle_sim_range: the view most visually distinct from the others. first / middle: fixed positional picks (default: saddle_balanced)| COMBO| No (conditional)| `"saddle_balanced"`  
`"saddle_sim_range"`  
`"first"`  
`"middle"`  
`pose_method`| How the camera field-of-view is estimated (for Small and Base models only). cam_dec: learned from image features. ray_pose: derived geometrically from the model’s 3D ray output. Affects perspective correctness of the 3D output (default: cam_dec)| COMBO| No (conditional)| `"cam_dec"`  
`"ray_pose"`  
  
**Notes on parameter constraints:**

  * The `ref_view_strategy` and `pose_method` parameters are only available when `mode` is set to `"multiview"`.
  * Multi-view mode requires a Small or Base model variant. Models with other head types (such as Metric or Mono) do not support cross-view attention or camera pose estimation.
  * When `pose_method` is set to `"cam_dec"`, the model must have a camera decoder. If set to `"ray_pose"`, the model must have a DualDPT head.
  * If the selected `pose_method` is not compatible with the loaded model, an error will be raised.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`da3_geometry`| Dictionary of non-normalized tensors. Always contains the keys: depth, image, mode. Optional keys include: sky (for Mono/Metric models), confidence (for Small/Base models), extrinsics and intrinsics (for multi-view mode)| DA3_GEOMETRY  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DA3Inference/en.md)

* * *

**Source fingerprint (SHA-256):** `e91dd47e6a01719cdd6b6ce8a9bcc45933cac72c5e147ac42906d2f83ab7c250`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/DA3Inference.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/DA3Inference)

[DA3GeometryToPointCloud - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/DA3GeometryToPointCloud)[DA3Render - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/DA3Render)

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
