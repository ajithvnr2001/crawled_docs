---
url: https://docs.comfy.org/built-in-nodes/VideoRandomTemporalCrop/
title: VideoRandomTemporalCrop - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:19.028816+00:00
---

# VideoRandomTemporalCrop - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/VideoRandomTemporalCrop/

Transform

# VideoRandomTemporalCrop - ComfyUI Built-in Node Documentation

Copy pageCopy page

Randomly crop a continuous range of frames from an input video.

Copy pageCopy page

Randomly crop a continuous range of frames from an input video. The number of frames to keep is set by the `length` parameter, and the start position is chosen randomly using the `seed` parameter. The node operates lazily, meaning it does not process the entire video until the output is used downstream.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`video`| Input video.| VIDEO| Yes| –  
`length`| Number of frames to keep. If `length` is greater than the total number of frames in the video, the entire video is kept. (default: 16)| INT| Yes| min: 1, max: 99999  
`seed`| Random seed. (default: 0)| INT| Yes| min: 0, max: 0xFFFFFFFFFFFFFFFF  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`video`| Cropped video (lazy).| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoRandomTemporalCrop/en.md)

* * *

**Source fingerprint (SHA-256):** `8249feb5ac3607fcabf3de0ec4d2eb90ab4aa46c18613040c341b825c9db1b1e`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/VideoRandomTemporalCrop.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/VideoRandomTemporalCrop)

[LTXVPreprocess - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LTXVPreprocess)[VideoTemporalCrop - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/VideoTemporalCrop)

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
