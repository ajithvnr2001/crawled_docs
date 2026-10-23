---
url: https://docs.comfy.org/built-in-nodes/GetVideoComponents/
title: GetVideoComponents - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:01.377165+00:00
---

# GetVideoComponents - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/GetVideoComponents/

Video

# GetVideoComponents - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Get Video Components node extracts all the main elements from a video file.

Copy pageCopy page

The Get Video Components node extracts all the main elements from a video file. It separates the video into individual frames, extracts the audio track, and provides the video’s frame rate, bit depth, and color space. This allows you to work with each component independently for further processing or analysis.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`video`| The video to extract components from.| VIDEO| Yes| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`images`| The individual frames extracted from the video as separate images.| IMAGE  
`audio`| The audio track extracted from the video.| AUDIO  
`fps`| The frame rate of the video in frames per second.| FLOAT  
`bit_depth`| The bit depth of the video.| COMBO  
`color_space`| The color space of the video.| COMBO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetVideoComponents/en.md)

* * *

**Source fingerprint (SHA-256):** `b57dbf1120105885d17361f07ec96c078aac9ae9a84beb63319885df679e4f81`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/GetVideoComponents.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/GetVideoComponents)

[FrameInterpolate - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/FrameInterpolate)[LoadVideo - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LoadVideo)

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
