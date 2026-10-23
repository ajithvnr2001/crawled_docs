---
url: https://docs.comfy.org/built-in-nodes/ConcatenateVideo/
title: ConcatenateVideo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:28.410190+00:00
---

# ConcatenateVideo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ConcatenateVideo/

Video

# ConcatenateVideo - ComfyUI Built-in Node Documentation

Copy pageCopy page

Concatenates multiple video segments into a single video, preserving the order in which they are connected.

Copy pageCopy page

Concatenates multiple video segments into a single video, preserving the order in which they are connected. Compatible encoded inputs are combined without being decoded, and an optional separate audio track can be supplied to replace the original audio.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`videos`| Video segments to concatenate in input order. Connect 1 to 100 videos; each video appears as a separate input slot labeled `video_1`, `video_2`, etc.| VIDEO| Yes| 1 to 100 segments  
`codec`| Codec used to encode video tensors. Auto uses H.264; already encoded videos remain unchanged. Default: “auto”| COMBO| Yes| `"auto"`  
Other options are defined by the available video codec types.  
`complete_audio`| Optional complete soundtrack for the concatenated video. Overrides audio carried by the input videos.| AUDIO| No| N/A  
  
**Note:** The `videos` input accepts between 1 and 100 video segments. If `complete_audio` is provided, it replaces the audio of all input videos. When `codec` is set to “auto”, compatible encoded inputs are concatenated without decoding.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`VIDEO`| The concatenated video.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConcatenateVideo/en.md)

* * *

**Source fingerprint (SHA-256):** `f591aecb83754127e1c86ed0488548f9e7d99f3559c95a1c86c55fa5d430713d`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ConcatenateVideo.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ConcatenateVideo)

[VideoTemporalCrop - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/VideoTemporalCrop)[CreateVideo - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/CreateVideo)

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
