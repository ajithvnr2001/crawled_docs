---
url: https://docs.comfy.org/built-in-nodes/HitPawVideoEnhance/
title: HitPawVideoEnhance - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:04.178896+00:00
---

# HitPawVideoEnhance - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/HitPawVideoEnhance/

Hitpaw

# HitPawVideoEnhance - ComfyUI Built-in Node Documentation

Copy pageCopy page

The HitPaw Video Enhance node uses an external API to improve the quality of videos.

Copy pageCopy page

The HitPaw Video Enhance node uses an external API to improve the quality of videos. It upscales low-resolution videos to a higher resolution, removes visual artifacts, and reduces noise. The processing cost is calculated per second of the input video.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The AI model to use for video enhancement. Selecting a model reveals a nested `resolution` parameter. The available models and their supported resolutions vary.| DYNAMIC_COMBO| Yes| `"Portrait Restore Model (1x)"`  
`"Portrait Restore Model (2x)"`  
`"General Restore Model (1x)"`  
`"General Restore Model (2x)"`  
`"General Restore Model (4x)"`  
`"Ultra HD Model (2x)"`  
`"Generative Model (1x)"`  
`video`| The input video file to be enhanced.| VIDEO| Yes| N/A  
  
### 

​

Portrait Restore, General Restore, and Ultra HD Model Inputs

These resolution options are shared by Portrait Restore Model (1x), Portrait Restore Model (2x), General Restore Model (1x), General Restore Model (2x), General Restore Model (4x), and Ultra HD Model (2x).

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model.resolution`| The target resolution for the enhanced video. Selecting `"original"` keeps the input video’s resolution.| COMBO| Yes| `"original"`  
`"720p"`  
`"1080p"`  
`"2K/QHD"`  
`"4K/UHD"`  
`"8K"`  
  
### 

​

Generative Model (1x) Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model.resolution`| The target resolution for the enhanced video. Selecting `"original"` keeps the input video’s resolution. The `"8K"` option is not available for this model.| COMBO| Yes| `"original"`  
`"720p"`  
`"1080p"`  
`"2K/QHD"`  
`"4K/UHD"`  
  
**Notes:**

  * The input `video` must be between 0.5 seconds and 60 minutes (3600 seconds) in duration.
  * The selected `resolution` must be at least as large as the input video’s dimensions. For square videos, it must be at least as large as the video’s width and height. For non-square videos, it must be at least as large as the video’s shorter dimension. If the target resolution is smaller, an error is raised. Selecting `"original"` keeps the input video’s resolution.
  * When a resolution other than `"original"` is selected, non-square videos are scaled so that their shorter dimension matches the selected resolution while preserving the aspect ratio. Square videos are scaled so that both dimensions match the square target size of the selected resolution (for example, `"4K/UHD"` produces 2048×2048).



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`video`| The enhanced video file.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HitPawVideoEnhance/en.md)

* * *

**Source fingerprint (SHA-256):** `42803c7137d62dbce5021cd2bd9b9fba1a89c80e7b3f237f8a0eb03858c49967`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/HitPawVideoEnhance.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/HitPawVideoEnhance)

[HiggsfieldMotionTransferNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/HiggsfieldMotionTransferNode)[KlingAvatarNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/KlingAvatarNode)

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
