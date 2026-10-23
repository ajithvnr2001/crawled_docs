---
url: https://docs.comfy.org/built-in-nodes/WanCameraEmbedding/
title: WanCameraEmbedding - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:22.570015+00:00
---

# WanCameraEmbedding - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/WanCameraEmbedding/

Camera

# WanCameraEmbedding - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node generates a camera trajectory embedding using Plücker embeddings for the camera path you choose.

Copy pageCopy page

This node generates a camera trajectory embedding using Plücker embeddings for the camera path you choose. It builds a sequence of camera poses simulating movements such as panning, zooming, or rotating, and converts them into an embedding tensor that can be used in video generation pipelines.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`camera_pose`| The type of camera movement to simulate (default: “Static”)| COMBO| Yes| ”Static"  
"Pan Up"  
"Pan Down"  
"Pan Left"  
"Pan Right"  
"Zoom In"  
"Zoom Out"  
"Anti Clockwise (ACW)"  
"ClockWise (CW)“  
`width`| The width of the output in pixels (default: 832, step: 16)| INT| Yes| 16 to MAX_RESOLUTION  
`height`| The height of the output in pixels (default: 480, step: 16)| INT| Yes| 16 to MAX_RESOLUTION  
`length`| The length of the camera trajectory sequence (default: 81, step: 4)| INT| Yes| 1 to MAX_RESOLUTION  
`speed`| The speed of the camera movement (default: 1.0, step: 0.1)| FLOAT| No| 0.0 to 10.0  
`fx`| The focal length x parameter (default: 0.5, step: 0.000000001)| FLOAT| No| 0.0 to 1.0  
`fy`| The focal length y parameter (default: 0.5, step: 0.000000001)| FLOAT| No| 0.0 to 1.0  
`cx`| The principal point x coordinate (default: 0.5, step: 0.01)| FLOAT| No| 0.0 to 1.0  
`cy`| The principal point y coordinate (default: 0.5, step: 0.01)| FLOAT| No| 0.0 to 1.0  
  
Note: `fx`, `fy`, `cx`, and `cy` are advanced camera intrinsic parameters. The `speed` parameter scales the rotation angle and translation distance of the selected camera motion.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`camera_embedding`| The generated camera embedding tensor containing the trajectory sequence| TENSOR  
`width`| The width value that was used for processing| INT  
`height`| The height value that was used for processing| INT  
`length`| The length value that was used for processing| INT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraEmbedding/en.md)

* * *

**Source fingerprint (SHA-256):** `1a2f98d83d18033581823dee61b5a3686d560c749c55223f81febca89654a29f`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/WanCameraEmbedding.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/WanCameraEmbedding)

[WanAnimateToVideo - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/WanAnimateToVideo)[WanCameraImageToVideo - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/WanCameraImageToVideo)

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
