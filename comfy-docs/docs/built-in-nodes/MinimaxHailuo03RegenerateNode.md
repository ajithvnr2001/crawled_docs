---
url: https://docs.comfy.org/built-in-nodes/MinimaxHailuo03RegenerateNode/
title: MinimaxHailuo03RegenerateNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:33.501027+00:00
---

# MinimaxHailuo03RegenerateNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MinimaxHailuo03RegenerateNode/

Minimax

# MinimaxHailuo03RegenerateNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node re-renders a MiniMax H3 768P video output at 2K resolution.

Copy pageCopy page

This node re-renders a MiniMax H3 768P video output at 2K resolution. It uploads the unmodified 768P video and the exact prompt used to generate it, starts a MiniMax H3 regeneration job, and returns the re-rendered 2K video. If the original generation used first or last frames or reference media, attach the same inputs.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The model to use for video regeneration. Selecting “MiniMax H3” reveals the prompt, resolution, and reference media settings.| DYNAMIC_COMBO| Yes| ”MiniMax H3”  
`video`| The MiniMax H3 768P output video to re-render. Connect the unmodified output of a MiniMax H3 video node (24 FPS, 4-15 seconds). 2K outputs cannot be used.| VIDEO| Yes| 24 FPS, 4-15 seconds  
`first_frame`| First frame image from the original generation, if one was used.| IMAGE| No| Image  
`last_frame`| Last frame image from the original generation, if one was used.| IMAGE| No| Image  
`watermark`| Whether to add an AIGC watermark to the video. Default is false.| BOOLEAN| Yes| false / true  
  
### 

​

MiniMax H3 Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| The exact prompt used to generate the source video. Must not be empty.| STRING| Yes| Text (multiline)  
`resolution`| Resolution to re-render the source video at.| COMBO| Yes| ”2K”  
  
### 

​

Reference Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`reference_images`| Growable slot: connect `image_1` through `image_9` (up to 9 images). Reference images from the original generation, in the same order.| IMAGE| No| 0-9 images  
`reference_videos`| Growable slot: connect `video_1` through `video_3` (up to 3 videos). Reference videos from the original generation, in the same order.| VIDEO| No| 0-3 videos  
`reference_audios`| Growable slot: connect `audio_1` through `audio_3` (up to 3 clips). Audio references from the original generation, in the same order. Cannot be used without a reference image or video.| AUDIO| No| 0-3 clips  
  
### 

​

Constraints

  * The `prompt` must not be empty.
  * The source `video` must be an unmodified MiniMax H3 768P output: 24 FPS, width and height divisible by 32, at most 1,032,192 total pixels, and 107 to 362 frames in steps of 17 (4 to 15 seconds at 24 FPS). 2K outputs cannot be used as the source.
  * `first_frame` and `last_frame` are mutually exclusive with reference media (`reference_images`, `reference_videos`, `reference_audios`). Use frames for an image-to-video prompt, or reference media for a reference-to-video prompt.
  * `reference_audios` requires at least one `reference_images` or `reference_videos` input.
  * `first_frame`, `last_frame`, and each `reference_image` must have an aspect ratio between 0.4 and 2.5 and be at least 256x256 pixels.
  * `reference_videos`: each video must be 23.976 to 60 FPS and 2-15 seconds long; total duration cannot exceed 15 seconds.
  * `reference_audios`: each clip must be 2-15 seconds long; total duration cannot exceed 15 seconds.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`video`| The re-rendered MiniMax H3 video at 2K resolution.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03RegenerateNode/en.md)

* * *

**Source fingerprint (SHA-256):** `4b5aa6dee12364cf6f44e7ee78b984c3568529b97051637a6ac62db9761d3a77`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MinimaxHailuo03RegenerateNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MinimaxHailuo03RegenerateNode)

[MinimaxHailuo03ReferenceNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/MinimaxHailuo03ReferenceNode)[MinimaxHailuo03TextToVideoNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/MinimaxHailuo03TextToVideoNode)

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
