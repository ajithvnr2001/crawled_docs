---
url: https://docs.comfy.org/built-in-nodes/Video Slice/
title: Video Slice - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:19.338660+00:00
---

# Video Slice - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Video Slice/

Video

# Video Slice - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Video Slice node allows you to extract a specific segment from a video.

Copy pageCopy page

The Video Slice node allows you to extract a specific segment from a video. You can define a start time and a duration to trim the video, or simply skip the beginning frames. If the requested duration is longer than the remaining video, the node can either return what’s available or raise an error.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`video`| The input video to be sliced.| VIDEO| Yes| -  
`start_time`| Start time in seconds (default: 0.0).| FLOAT| Yes| -1e5 to 1e5  
`duration`| Duration in seconds, or 0 for unlimited duration (default: 0.0).| FLOAT| Yes| 0.0 and above  
`strict_duration`| If True, when the specified duration is not possible, an error will be raised (default: False).| BOOLEAN| Yes| -  
  
**Note:** If the video cannot be sliced for the given `start_time` and `duration`, the node raises an error. When `strict_duration` is False, the node returns the available portion of the video when the requested duration exceeds the remaining length; when True, it raises an error instead.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`video`| The trimmed video segment.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](<https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Video> Slice/en.md)

* * *

**Source fingerprint (SHA-256):** `439b76528742c1fbe230eee9502e945847ae99a58a9bd81a7a7dc3b20e15d450`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Video%20Slice.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Video%20Slice)

[SaveWEBM - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SaveWEBM)[VideoCrop - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/VideoCrop)

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
