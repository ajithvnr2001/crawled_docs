---
url: https://docs.comfy.org/built-in-nodes/VideoTemporalCrop/
title: VideoTemporalCrop - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:19.410425+00:00
---

# VideoTemporalCrop - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/VideoTemporalCrop/

Transform

# VideoTemporalCrop - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node crops a continuous range of frames from a video.

Copy pageCopy page

This node crops a continuous range of frames from a video. It works in a fully lazy manner, meaning it only processes the selected portion of the video as needed later in the workflow.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`video`| Input video.| VIDEO| Yes| –  
`start_frame`| Starting frame index (default: 0).| INT| Yes| 0 to 99999  
`length`| Number of frames to keep (default: 16).| INT| Yes| 1 to 99999  
  
Note: `start_frame` is limited to the last frame of the video, and `length` is reduced if it would extend beyond the available frames.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`video`| Cropped video (lazy).| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTemporalCrop/en.md)

* * *

**Source fingerprint (SHA-256):** `1d28a55399c9fe7ca47f0aaa872751ac89c5419a6f6be6636fbf7f020a02749d`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/VideoTemporalCrop.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/VideoTemporalCrop)

[VideoRandomTemporalCrop - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/VideoRandomTemporalCrop)[ConcatenateVideo - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ConcatenateVideo)

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
