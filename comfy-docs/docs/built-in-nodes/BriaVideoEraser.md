---
url: https://docs.comfy.org/built-in-nodes/BriaVideoEraser/
title: BriaVideoEraser - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:27.101452+00:00
---

# BriaVideoEraser - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/BriaVideoEraser/

Bria

# BriaVideoEraser - ComfyUI Built-in Node Documentation

Copy pageCopy page

Erases whatever a per-frame mask covers from a video with Bria and fills the gap in.

Copy pageCopy page

Erases whatever a per-frame mask covers from a video with Bria and fills the gap in. The mask must be white on what should go and black elsewhere. Bria accepts clips of at most 5.1 seconds at 20 to 30 frames per second with even pixel dimensions; audio is kept by default. The returned clip can be a few frames shorter than the input.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`video`| Clip to erase from.| VIDEO| Yes| -  
`mask`| One mask per frame of the video, white where the object to erase is. Provide either a mask or a mask video, not both.| MASK| No| -  
`mask_video`| An already encoded mask video with the same dimensions and frame count as the video. Provide either a mask or a mask video, not both.| VIDEO| No| -  
`preserve_audio`| Keep the input’s audio track. Default: true.| BOOLEAN| No| `true`  
`false`  
  
**Notes on constraints:**

  * Exactly one of `mask` or `mask_video` must be connected. An error is raised if neither is provided, or if both are provided.
  * The video must be at most 5.1 seconds long and must run at 20 to 30 frames per second. Re-time the clip with Get Video Components and Create Video if needed.
  * The video must have even pixel dimensions (width and height divisible by 2). Crop or scale it first otherwise.
  * When using `mask`, it must contain one mask frame per video frame, and its aspect ratio must match the video. Masks are binarized at 50%: areas painted at less than half opacity are ignored, and an empty mask raises an error. If the mask resolution differs from the video, it is resized to the video dimensions.
  * When using `mask_video`, it must have the same dimensions and the same frame count as the video.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`video`| The edited clip with the masked areas erased and the gaps filled in. The output may be a few frames shorter than the input clip.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVideoEraser/en.md)

* * *

**Source fingerprint (SHA-256):** `525b90013b9d9ea4b224caf1f32479493c96f90e28acbf3cf7a4d16a6ca91a45`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/BriaVideoEraser.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/BriaVideoEraser)

[BriaTransparentVideoBackground - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/BriaTransparentVideoBackground)[BriaVideoGreenScreen - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/BriaVideoGreenScreen)

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
