---
url: https://docs.comfy.org/built-in-nodes/VideoTrim/
title: VideoTrim - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:19.569867+00:00
---

# VideoTrim - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/VideoTrim/

Video

# VideoTrim - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node cuts a video to a chosen time window by setting a start time and a duration.

Copy pageCopy page

This node cuts a video to a chosen time window by setting a start time and a duration. It also offers a strict mode that raises an error when the requested duration cannot be achieved.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`video`| The video to trim.| VIDEO| Yes| —  
`trim`| Trim window using start/end frames. The window is converted into a start time (in seconds from the beginning of the video) and a duration (in seconds). When both the start time and the duration are 0, the video is returned without any trimming.| VIDEO_EDIT| Yes| start_time: >= 0, default 0  
duration: >= 0, default 0  
`strict_duration`| If True, when the specified duration is not possible, an error will be raised. (default: False)| BOOLEAN| No| true  
false  
  
Note: The trim duration must be >= 0; negative values raise an error. The requested trim window must fit inside the source video. If the trim cannot be applied, an error is raised that reports the source duration, start time, and target duration.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`video`| The trimmed video. When the trim window is empty (start time and duration both 0), the original video is returned unchanged.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTrim/en.md)

* * *

**Source fingerprint (SHA-256):** `ba8f8ccbae7e8aebda553810b81ccaa427d45523142bd00746c4e2f4e5b41a1b`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/VideoTrim.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/VideoTrim)

[VideoFrameSample - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/VideoFrameSample)

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
