---
url: https://docs.comfy.org/built-in-nodes/BriaVideoReplaceBackground/
title: BriaVideoReplaceBackground - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:27.429516+00:00
---

# BriaVideoReplaceBackground - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/BriaVideoReplaceBackground/

Bria

# BriaVideoReplaceBackground - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node replaces the background of a video with a supplied image or video using Bria’s API.

Copy pageCopy page

This node replaces the background of a video with a supplied image or video using Bria’s API. The output keeps the foreground video’s resolution and frame rate; a background with a different aspect ratio is stretched to fit, so matching aspect ratios produces undistorted results.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`video`| Foreground video whose background is replaced.| VIDEO| Yes| -  
`background_image`| Background image to composite behind the foreground. Provide either a background image or a background video, not both.| IMAGE| No| -  
`background_video`| Background video to composite behind the foreground. Provide either a background image or a background video, not both.| VIDEO| No| -  
`seed`| Seed controls whether the node should re-run; results are non-deterministic regardless of seed. (default: 0)| INT| Yes| 0 to 2147483647  
  
**Note:** You must provide exactly one of `background_image` or `background_video` — not both and not neither. The foreground video and the background video (if used) must each be 60 seconds or shorter. When `background_image` is used, its alpha channel is removed before processing.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`video`| The resulting video with the background replaced, encoded as MP4 (H.264).| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVideoReplaceBackground/en.md)

* * *

**Source fingerprint (SHA-256):** `c487cf7dd434b8523ce64f241c2171c82bb5e0abdc5c3ca3e8b1a1259aeab490`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/BriaVideoReplaceBackground.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/BriaVideoReplaceBackground)

[BriaVideoGreenScreen - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/BriaVideoGreenScreen)[ByteDance2DraftToFinalVideoNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ByteDance2DraftToFinalVideoNode)

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
