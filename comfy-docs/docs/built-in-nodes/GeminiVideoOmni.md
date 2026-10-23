---
url: https://docs.comfy.org/built-in-nodes/GeminiVideoOmni/
title: GeminiVideoOmni - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:59.745454+00:00
---

# GeminiVideoOmni - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/GeminiVideoOmni/

Gemini

# GeminiVideoOmni - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generate a video with audio from a text prompt using Google’s Gemini Omni Flash model.

Copy pageCopy page

Generate a video with audio from a text prompt using Google’s Gemini Omni Flash model. Optionally provide reference images and/or videos to guide or edit the result. Describe the desired length (3-10s) and aspect ratio (16:9 or 9:16) directly in the prompt.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The Gemini video model used to generate the video.| DYNAMIC_COMBO| Yes| ”Omni Flash”  
`seed`| Seed controls whether the node should re-run; results are non-deterministic regardless of seed (default: 42).| INT| Yes| 0 to 2147483647  
  
### 

​

Omni Flash Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Describe the video to generate. Specify the length and aspect ratio directly in the prompt, e.g. “a 6-second clip in 16:9”. Length may be 3-10 seconds; the aspect ratio must be 16:9 (landscape) or 9:16 (portrait). The output is 720p, 24 FPS, with audio.| STRING| Yes| Minimum 1 character after stripping whitespace  
`temperature`| Controls randomness. Lower is more focused/deterministic, higher is more varied (default: 1.0).| FLOAT| No| 0.0 to 2.0  
`top_p`| Nucleus sampling: sample from the smallest token set whose cumulative probability reaches top_p (default: 0.95).| FLOAT| No| 0.0 to 1.0  
  
### 

​

Reference Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`images`| Growable slot: connect one or more reference images (`image_1`…`image_14`) to guide or animate the video. Up to 14 images in total.| IMAGE| No| 0 to 14 images  
`videos`| Growable slot: connect one or more reference videos (`video_1`…`video_3`) to guide or edit. Up to 3 videos, each up to 10 seconds long.| VIDEO| No| 0 to 3 videos, each max 10 seconds  
  
Notes:

  * If an image input contains multiple frames, each frame counts toward the maximum of 14 images.
  * When reference images or videos are provided, the total encoded media size must stay under about 90 MB; otherwise the node raises an error.
  * When no reference images or videos are provided, the node generates the video from the text prompt alone.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`VIDEO`| The generated video with audio from the Gemini model.| VIDEO  
`STRING`| Any text response from the model, such as reasoning or explanations.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiVideoOmni/en.md)

* * *

**Source fingerprint (SHA-256):** `648844868affb68298d2eac8ac20095bfe378d32e721396781de330ef6a6d69f`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/GeminiVideoOmni.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/GeminiVideoOmni)

[ByteDanceVideoEnhanceNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ByteDanceVideoEnhanceNode)[GeminiVideoOmniV2 - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/GeminiVideoOmniV2)

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
