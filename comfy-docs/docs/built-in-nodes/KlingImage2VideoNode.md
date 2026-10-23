---
url: https://docs.comfy.org/built-in-nodes/KlingImage2VideoNode/
title: KlingImage2VideoNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:14.764035+00:00
---

# KlingImage2VideoNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/KlingImage2VideoNode/

Kling

# KlingImage2VideoNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Kling Image to Video Node generates a short video using a starting image as the first frame.

Copy pageCopy page

The Kling Image to Video Node generates a short video using a starting image as the first frame. It combines the image with text prompts and generation settings, then returns the resulting video along with its ID and duration.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`start_frame`| The reference image used to generate the video. The image must be at least 300x300 pixels and have an aspect ratio between 1:2.5 and 2.5:1.| IMAGE| Yes| -  
`prompt`| Positive text prompt. Must not be empty. Maximum 500 characters.| STRING| Yes| -  
`negative_prompt`| Negative text prompt. Maximum 500 characters. Leave empty if not used.| STRING| Yes| -  
`model_name`| The model used for video generation.| COMBO| Yes| `"kling-v2-5-turbo"`  
`cfg_scale`| Controls how closely the video follows the prompt. Higher values mean stronger adherence (default: 0.8).| FLOAT| Yes| 0.0 to 1.0  
`mode`| The generation mode.| COMBO| Yes| `"pro"`  
`aspect_ratio`| The aspect ratio of the generated video (default: `"16:9"`).| COMBO| Yes| `"16:9"`  
`"9:16"`  
`"1:1"`  
`duration`| The duration of the generated video in seconds (default: `"5"`).| COMBO| Yes| `"5"`  
`"10"`  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated video output.| VIDEO  
`video_id`| Unique identifier for the generated video.| STRING  
`duration`| Duration information for the generated video.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImage2VideoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `f4a461819bc05f92d867bddcc78a66ad7beaa10707ef8cae3e7eb9e6f72c890a`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/KlingImage2VideoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/KlingImage2VideoNode)

[KlingFirstLastFrameNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/KlingFirstLastFrameNode)[KlingImageToVideoWithAudio - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/KlingImageToVideoWithAudio)

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
