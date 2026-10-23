---
url: https://docs.comfy.org/built-in-nodes/BriaTransparentVideoBackground/
title: BriaTransparentVideoBackground - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:27.599207+00:00
---

# BriaTransparentVideoBackground - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/BriaTransparentVideoBackground/

Bria

# BriaTransparentVideoBackground - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node removes the background from a video using Bria’s AI service and outputs the cut-out frames along with an alpha mask.

Copy pageCopy page

This node removes the background from a video using Bria’s AI service and outputs the cut-out frames along with an alpha mask. Connect both outputs to a compositing node, or feed them to a Save WEBM node to write a transparent video.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`video`| The input video to process. The video must be 60 seconds or shorter.| VIDEO| Yes| -  
`seed`| Seed controls whether the node should re-run; results are non-deterministic regardless of seed (default: 0)| INT| Yes| 0 to 2147483647  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`images`| The video frames with the background removed, as RGB images in the range 0.0 to 1.0| IMAGE  
`mask`| The alpha mask for the video frames, following the Load Image convention where 1 means transparent| MASK  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaTransparentVideoBackground/en.md)

* * *

**Source fingerprint (SHA-256):** `536bd52af29218d2a342086e92799d3d9310da5ae5cbf02d705ba7503a4d73c8`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/BriaTransparentVideoBackground.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/BriaTransparentVideoBackground)

[BriaRemoveVideoBackground - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/BriaRemoveVideoBackground)[BriaVideoEraser - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/BriaVideoEraser)

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
