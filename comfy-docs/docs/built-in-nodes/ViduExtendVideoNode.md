---
url: https://docs.comfy.org/built-in-nodes/ViduExtendVideoNode/
title: ViduExtendVideoNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:20.404914+00:00
---

# ViduExtendVideoNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ViduExtendVideoNode/

Vidu

# ViduExtendVideoNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Vidu Video Extension node generates additional frames to extend the length of an existing video.

Copy pageCopy page

The Vidu Video Extension node generates additional frames to extend the length of an existing video. It uses a specified AI model to create a continuation based on the source video and an optional text prompt.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| Model to use for video extension. Selecting a model reveals its specific duration and resolution settings.| DYNAMIC_COMBO| Yes| `"viduq2-pro"`  
`"viduq2-turbo"`  
`video`| The source video to extend.| VIDEO| Yes| -  
`prompt`| An optional text prompt for the extended video (max 2000 characters; default: empty).| STRING| Yes| -  
`seed`| A seed value for controlling the randomness of the generation (default: 1).| INT| Yes| 0 to 2147483647  
`end_frame`| An optional image to use as the target end frame for the extension.| IMAGE| No| -  
  
### 

​

viduq2-pro and viduq2-turbo Inputs

These settings are shared by both models.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`duration`| Duration of the extended video in seconds (default: 4). This setting appears after selecting a model.| INT| Yes| 1 to 7  
`resolution`| Resolution of the output video. This setting appears after selecting a model.| COMBO| Yes| `"720p"`  
`"1080p"`  
  
**Note:** The source `video` must have a duration between 4 and 55 seconds. If `end_frame` is provided, its aspect ratio must be between 1:4 and 4:1, and its width and height must each be at least 128 pixels.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The newly generated video file containing the extended footage.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduExtendVideoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `bfa79dd1aee8a3e56d95fe7a899454b5c5f93679e098f59fc3bf58d93d290819`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ViduExtendVideoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ViduExtendVideoNode)

[Vidu4ReferenceVideoNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Vidu4ReferenceVideoNode)[ViduImageToVideoNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ViduImageToVideoNode)

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
