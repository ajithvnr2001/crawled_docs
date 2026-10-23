---
url: https://docs.comfy.org/built-in-nodes/ByteDanceFirstLastFrameNode/
title: ByteDanceFirstLastFrameNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:29.043688+00:00
---

# ByteDanceFirstLastFrameNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ByteDanceFirstLastFrameNode/

Bytedance

# ByteDanceFirstLastFrameNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node generates a video using a text prompt along with first and last frame images.

Copy pageCopy page

This node generates a video using a text prompt along with first and last frame images. It takes your description and the two key frames to create a complete video sequence that transitions between them. The node provides various options to control the video’s resolution, aspect ratio, duration, and other generation parameters.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The model used for video generation (default: `"seedance-1-5-pro-251215"`).| COMBO| Yes| `"seedance-1-5-pro-251215"`  
`"seedance-1-0-pro-250528"`  
`prompt`| The text prompt used to generate the video. Must not be empty and must not contain reserved parameter keywords (`resolution`, `ratio`, `duration`, `seed`, `camerafixed`, `watermark`).| STRING| Yes| -  
`first_frame`| First frame to be used for the video. Must be between 300x300 and 6000x6000 pixels, with an aspect ratio between 0.4 and 2.5.| IMAGE| Yes| -  
`last_frame`| Last frame to be used for the video. Must be between 300x300 and 6000x6000 pixels, with an aspect ratio between 0.4 and 2.5.| IMAGE| Yes| -  
`resolution`| The resolution of the output video.| COMBO| Yes| `"480p"`  
`"720p"`  
`"1080p"`  
`aspect_ratio`| The aspect ratio of the output video.| COMBO| Yes| `"adaptive"`  
`"16:9"`  
`"4:3"`  
`"1:1"`  
`"3:4"`  
`"9:16"`  
`"21:9"`  
`duration`| The duration of the output video in seconds. When using `seedance-1-5-pro-251215`, the minimum duration is 4 seconds. (default: 5)| INT| Yes| 3 - 12  
`seed`| Seed to use for generation. (default: 0)| INT| No| 0 - 2147483647  
`camera_fixed`| Specifies whether to fix the camera. The platform appends an instruction to fix the camera to your prompt, but does not guarantee the actual effect. (default: False)| BOOLEAN| No| -  
`watermark`| Whether to add an “AI generated” watermark to the video. (default: False)| BOOLEAN| No| -  
`generate_audio`| This parameter is ignored for any model except `seedance-1-5-pro-251215`. (default: False)| BOOLEAN| No| -  
  
**Note:** For the `seedance-1-5-pro-251215` model, `duration` must be 4 seconds or greater. Both `first_frame` and `last_frame` must be between 300x300 and 6000x6000 pixels and have an aspect ratio between 0.4 and 2.5. The `prompt` is checked and rejected if it contains reserved parameter keywords.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated video file.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceFirstLastFrameNode/en.md)

* * *

**Source fingerprint (SHA-256):** `ae0f3a34a21baad7f04f6917e98d16dc64496479a050896869ec6693a9a9ebaf`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ByteDanceFirstLastFrameNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ByteDanceFirstLastFrameNode)

[ByteDanceCreateVideoAsset - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ByteDanceCreateVideoAsset)[ByteDanceImageToVideoNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ByteDanceImageToVideoNode)

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
