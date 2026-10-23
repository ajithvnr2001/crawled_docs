---
url: https://docs.comfy.org/built-in-nodes/MediaPipeFaceMask/
title: MediaPipeFaceMask - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-18T12:01:28.298816+00:00
---

# MediaPipeFaceMask - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MediaPipeFaceMask/

Detection

# MediaPipeFaceMask - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node creates a binary mask (a black and white image) based on face landmarks detected by MediaPipe.

Copy pageCopy page

## 

​

Overview

This node creates a binary mask (a black and white image) based on face landmarks detected by MediaPipe. It draws filled polygon shapes for each detected face region, producing one mask per frame in a batch. When multiple faces are detected in the same frame, their masks are combined into a single mask.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`face_landmarks`| The face landmarks data from a MediaPipe face detection node.| FACE_LANDMARKS| Yes| -  
`regions`| Selects which facial regions to include in the mask. `"all"` creates a mask from the union of all face regions (face oval, lips, eyes, irises). `"custom"` allows you to toggle each region individually. Default: `"all"`| COMBO| Yes| `"all"`  
`"custom"`  
  
When `regions` is set to `"custom"`, the following additional boolean parameters become available:

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`face_oval`| Include the face oval region in the mask. Default: True| BOOLEAN| No| True/False  
`lips`| Include the lips region in the mask. Default: True| BOOLEAN| No| True/False  
`eyes`| Include the eyes region in the mask. Default: True| BOOLEAN| No| True/False  
`irises`| Include the irises region in the mask. Default: True| BOOLEAN| No| True/False  
  
**Note:** When using `"all"` mode, the mask includes all regions combined. Since the face oval encloses the other regions, selecting `"all"` effectively produces the same result as selecting only the face oval.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`MASK`| A binary mask tensor where face regions are white (value 1.0) and background is black (value 0.0). The mask has the same dimensions as the input image and contains one mask per frame in the batch.| MASK  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MediaPipeFaceMask/en.md)

* * *

**Source fingerprint (SHA-256):** `92270002a42ed59bc75e676a6881e1899186d3c8a1bb4dd4c0d39b3762b5bb66`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MediaPipeFaceMask.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MediaPipeFaceMask)

[MediaPipeFaceLandmarker - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/MediaPipeFaceLandmarker)[MediaPipeFaceMeshVisualize - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/MediaPipeFaceMeshVisualize)

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
