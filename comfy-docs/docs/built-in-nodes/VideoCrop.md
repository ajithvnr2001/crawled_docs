---
url: https://docs.comfy.org/built-in-nodes/VideoCrop/
title: VideoCrop - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:19.079542+00:00
---

# VideoCrop - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/VideoCrop/

Video

# VideoCrop - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node crops a video to a rectangular region defined in pixels, keeping only the area inside that rectangle.

Copy pageCopy page

This node crops a video to a rectangular region defined in pixels, keeping only the area inside that rectangle. It saves a temporary MP4 preview of the cropped result and outputs the cropped video.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`video`| The source video that will be cropped.| VIDEO| Yes| Any video  
`crop`| Crop region in pixels. Zero width/height keeps the full frame. The crop rectangle provides `x`, `y`, `width`, and `height` values, all with a default of 0.| VIDEO_EDIT| Yes| `x` ≥ 0  
`y` ≥ 0  
`width` ≥ 0  
`height` ≥ 0  
All values default to 0  
  
Note: The crop region is described in pixel coordinates. When the width and height are 0, no cropping is applied and the node outputs the full input video.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`video`| The video cropped to the selected rectangular region. When the crop width and height are 0, the output is the full input video. The cropped result is also saved as a temporary MP4 file and shown as a video preview.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoCrop/en.md)

* * *

**Source fingerprint (SHA-256):** `0c4ebd51027669fc232fe42a5e8840b5e4e95083b6794cd7b4c43123ddc0341b`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/VideoCrop.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/VideoCrop)

[Video Slice - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Video%20Slice)[VideoFrameSample - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/VideoFrameSample)

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
