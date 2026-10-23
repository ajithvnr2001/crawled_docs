---
url: https://docs.comfy.org/built-in-nodes/SAM3_TrackPreview/
title: SAM3_TrackPreview - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-18T12:01:27.493278+00:00
---

# SAM3_TrackPreview - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SAM3_TrackPreview/

Detection

# SAM3_TrackPreview - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node creates a video preview of tracked objects, drawing each tracked object with a distinct color overlay and a number label.

Copy pageCopy page

## 

​

Overview

This node creates a video preview of tracked objects, drawing each tracked object with a distinct color overlay and a number label. It does not output any image or video tensors — instead, it saves the resulting preview video directly to a temporary file.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`track_data`| The tracking data containing packed masks and object information from a SAM3 tracking node.| TRACK_DATA| Yes| -  
`images`| Optional input images to use as the background for the preview. If not provided, a black background is used.| IMAGE| No| -  
`opacity`| The opacity of the color overlay applied to tracked objects (default: 0.5).| FLOAT| No| 0.0 to 1.0 (step: 0.05)  
`fps`| The frame rate of the output video (default: 24.0).| FLOAT| No| 1.0 to 120.0 (step: 1.0)  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`ui`| A UI element that displays the generated preview video. No tensor data is returned.| PREVIEW_VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_TrackPreview/en.md)

* * *

**Source fingerprint (SHA-256):** `76389f354c8acdf249137d966765069d530034a0f8eeb39d769bde3c0f7a1bd0`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SAM3_TrackPreview.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SAM3_TrackPreview)

[SAM3_Detect - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SAM3_Detect)[SAM3_TrackToMask - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SAM3_TrackToMask)

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
