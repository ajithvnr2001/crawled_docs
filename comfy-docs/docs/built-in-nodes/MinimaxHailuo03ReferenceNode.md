---
url: https://docs.comfy.org/built-in-nodes/MinimaxHailuo03ReferenceNode/
title: MinimaxHailuo03ReferenceNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:33.155936+00:00
---

# MinimaxHailuo03ReferenceNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MinimaxHailuo03ReferenceNode/

Minimax

# MinimaxHailuo03ReferenceNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node generates a video using the MiniMax H3 models, conditioned on reference images, videos, and audio.

Copy pageCopy page

This node generates a video using the MiniMax H3 models, conditioned on reference images, videos, and audio. References are referred to in the prompt by their connection order: “Image 1”, “Image 2”, “Video 1”, “Audio 1”, and so on. Two models are available: “MiniMax H3” and “MiniMax H3 Max”.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| Model to use for video generation (default: “MiniMax H3”). Selecting “MiniMax H3” provides the MiniMax H3 generation and reference inputs below. Selecting “MiniMax H3 Max” provides the MiniMax H3 Max generation and reference inputs below.| DYNAMIC_COMBO| Yes| ”MiniMax H3"  
"MiniMax H3 Max”  
`seed`| Random seed. The same request with the same seed gives similar, but not guaranteed identical, results (default: 42).| INT| Yes| 0 to 4294967295  
`watermark`| Whether to add an AIGC watermark to the video (default: false). Only supported by the MiniMax H3 model.| BOOLEAN| No| true  
false  
  
### 

​

MiniMax H3 Inputs

These inputs are available when “MiniMax H3” is selected as the model.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Text prompt for video generation. Reference media can be referred to by their order, for example “Image 1”, “Image 2”, “Video 1”, or “Audio 1”.| STRING| Yes| Minimum 1 character  
`resolution`| Resolution of the output video (default: “768P”).| COMBO| Yes| ”768P"  
"2K”  
`ratio`| Aspect ratio of the output video (default: “adaptive”).| COMBO| Yes| ”adaptive"  
"16:9"  
"4:3"  
"1:1"  
"3:4"  
"9:16"  
"21:9”  
`duration`| Duration of the output video in seconds (default: 5).| INT| Yes| 4 to 15  
  
### 

​

MiniMax H3 Max Inputs

These inputs are available when “MiniMax H3 Max” is selected as the model.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Text prompt for video generation. Reference media can be referred to by their order, for example “Image 1”, “Image 2”, “Video 1”, or “Audio 1”.| STRING| Yes| 1 to 50000 characters  
`resolution`| Resolution of the output video (default: “768P”).| COMBO| Yes| ”480P"  
"768P”  
`ratio`| Aspect ratio of the output video (default: “adaptive”).| COMBO| Yes| ”adaptive"  
"16:9"  
"4:3"  
"1:1"  
"3:4"  
"9:16"  
"21:9”  
`duration`| Duration of the output video in seconds (default: 5).| INT| Yes| 5 to 15  
`prompt_expansion_mode`| How much effort is spent rewriting the prompt before generation (default: “balanced”).| COMBO| Yes| ”balanced"  
"quality”  
`reference_detail`| Detail level at which reference images are sent. “high” sends them at the largest size the model uses (up to a 2048 pixel short side); “standard” downsizes them to at most 2048x1024 to reduce the reference cost (default: “standard”).| COMBO| Yes| ”high"  
"standard”  
  
### 

​

Reference Inputs

These reference inputs are shared by both models. Each is a growable slot.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`reference_images`| Growable slot: connect up to 9 items (`image_1`…`image_9`). Subject or style reference images, referred to in the prompt as “Image 1”..”Image 9” in connection order. Up to 9 images.| IMAGE| No| 0 to 9 images  
`reference_videos`| Growable slot: connect up to 3 items (`video_1`…`video_3`). Motion or scene reference videos, referred to in the prompt as “Video 1”..”Video 3” in connection order. Up to 3 videos, 2-15 seconds each, 15 seconds in total.| VIDEO| No| 0 to 3 videos  
`reference_audios`| Growable slot: connect up to 3 items (`audio_1`…`audio_3`). Audio references, referred to in the prompt as “Audio 1”..”Audio 3” in connection order. Up to 3 clips, 2-15 seconds each, 15 seconds in total. Cannot be used without a reference image or video.| AUDIO| No| 0 to 3 clips  
  
### 

​

Parameter Constraints

  * At least one reference image or one reference video is required. Reference audio alone is not accepted.
  * Each reference image must have an aspect ratio between approximately 0.4 and 2.5 (2:5 to 5:2) and a minimum width and height of 256 pixels.
  * Each reference video must be between 2 and 15 seconds long with a frame rate between 23.976 and 60 FPS. The total duration of all reference videos cannot exceed 15 seconds.
  * Each reference audio clip must be between 2 and 15 seconds long. The total duration of all reference audio clips cannot exceed 15 seconds.
  * When “MiniMax H3 Max” is selected, the `watermark` setting must be disabled.
  * When “MiniMax H3 Max” is selected, the total number of reference files (images, videos, and audio combined) cannot exceed 12.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`video`| The generated video.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03ReferenceNode/en.md)

* * *

**Source fingerprint (SHA-256):** `b77eedb1f7757e60518c04484f1cc24c27cf6886b3ae31c15207ea49fd436a73`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MinimaxHailuo03ReferenceNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MinimaxHailuo03ReferenceNode)

[MinimaxHailuo03FirstLastFrameNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/MinimaxHailuo03FirstLastFrameNode)[MinimaxHailuo03RegenerateNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/MinimaxHailuo03RegenerateNode)

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
