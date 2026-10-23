---
url: https://docs.comfy.org/built-in-nodes/LumaRay32ImageToVideoNode/
title: LumaRay32ImageToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:27.716701+00:00
---

# LumaRay32ImageToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LumaRay32ImageToVideoNode/

Luma

# LumaRay32ImageToVideoNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generate a video from a start and/or end frame using Luma’s Ray 3.2 model.

Copy pageCopy page

Generate a video from a start and/or end frame using Luma’s Ray 3.2 model. Image-anchored generations are always 5 seconds in duration.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Text prompt for the video generation.| STRING| Yes| 1 to 6000 characters  
`resolution`| The output resolution of the generated video (default: “720p”).| COMBO| Yes| ”360p"  
"540p"  
"720p"  
"1080p”  
`loop`| Make the video loop seamlessly. Not available when an end_frame is set.| BOOLEAN| Yes| True  
False  
`seed`| Seed value for reproducible generation.| INT| Yes| 0 to 2147483647  
`start_frame`| First frame of the generated video.| IMAGE| No| -  
`end_frame`| Last frame of the generated video.| IMAGE| No| -  
  
**Note:** At least one of `start_frame` or `end_frame` must be provided. If both are provided, the generated video will transition from the start frame to the end frame. The `loop` option cannot be enabled when an `end_frame` is set.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`video`| The generated video output.| VIDEO  
`generation_id`| The unique identifier for the generation request.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32ImageToVideoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `ff479c196f10153ffa09af6acfb4e286d1934aa28a5e9b413613097a2cfb5f2a`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LumaRay32ImageToVideoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LumaRay32ImageToVideoNode)

[LumaRay32ExtendVideoNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LumaRay32ExtendVideoNode)[LumaRay32KeyframeNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LumaRay32KeyframeNode)

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
