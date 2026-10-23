---
url: https://docs.comfy.org/built-in-nodes/KlingImageToVideoWithAudio/
title: KlingImageToVideoWithAudio - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:14.675654+00:00
---

# KlingImageToVideoWithAudio - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/KlingImageToVideoWithAudio/

Kling

# KlingImageToVideoWithAudio - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Kling Image(First Frame) to Video with Audio node uses the Kling AI model to generate a short video from a single starting image and a text prompt.

Copy pageCopy page

The Kling Image(First Frame) to Video with Audio node uses the Kling AI model to generate a short video from a single starting image and a text prompt. It creates a video sequence that begins with the provided image and can optionally include AI-generated audio to accompany the visuals.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model_name`| The specific version of the Kling AI model to use for video generation.| COMBO| Yes| `"kling-v2-6"`  
`start_frame`| The image that will serve as the first frame of the generated video. The image must be at least 300x300 pixels and have an aspect ratio between 1:2.5 and 2.5:1.| IMAGE| Yes| -  
`prompt`| Positive text prompt. This describes the video content you want to generate. The prompt must be between 1 and 2500 characters long.| STRING| Yes| -  
`mode`| The operational mode for the video generation.| COMBO| Yes| `"pro"`  
`duration`| The length of the video to generate, in seconds.| COMBO| Yes| `5`  
`10`  
`generate_audio`| When enabled, the node will generate audio to accompany the video. When disabled, the video will be silent. (default: True)| BOOLEAN| No| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`video`| The generated video file, which may include audio depending on the `generate_audio` input.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageToVideoWithAudio/en.md)

* * *

**Source fingerprint (SHA-256):** `e0b834a297f7afd72cfb779a92557f0dc680eacd4d0e18bab0e7c59ae8624965`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/KlingImageToVideoWithAudio.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/KlingImageToVideoWithAudio)

[KlingImage2VideoNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/KlingImage2VideoNode)[KlingLipSyncAudioToVideoNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/KlingLipSyncAudioToVideoNode)

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
