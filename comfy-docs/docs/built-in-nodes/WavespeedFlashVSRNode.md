---
url: https://docs.comfy.org/built-in-nodes/WavespeedFlashVSRNode/
title: WavespeedFlashVSRNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:26.442109+00:00
---

# WavespeedFlashVSRNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/WavespeedFlashVSRNode/

Wavespeed

# WavespeedFlashVSRNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The WavespeedFlashVSRNode is a fast, high-quality video upscaler that boosts resolution and restores clarity for low-resolution or blurry footage.

Copy pageCopy page

The WavespeedFlashVSRNode is a fast, high-quality video upscaler that boosts resolution and restores clarity for low-resolution or blurry footage. It processes a video input and outputs a new video at a user-selected higher resolution.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`video`| The input video file to be upscaled. Must be in MP4 container format with a duration between 5 seconds and 10 minutes.| VIDEO| Yes| N/A  
`target_resolution`| The desired resolution for the upscaled output video.| STRING| Yes| `"720p"`  
`"1080p"`  
`"2K"`  
`"4K"`  
  
**Input Constraints:**

  * The input `video` file must be in the MP4 container format.
  * The duration of the input `video` must be between 5 seconds and 10 minutes (600 seconds).



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The upscaled video file at the selected target resolution.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WavespeedFlashVSRNode/en.md)

* * *

**Source fingerprint (SHA-256):** `d7885eeb2dacfc2bc398d1bc991620be479f45d8edbdca7eb046a21500581529`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/WavespeedFlashVSRNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/WavespeedFlashVSRNode)

[WanTextToVideoApi - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/WanTextToVideoApi)[SamplerDpmpp2mSde - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SamplerDpmpp2mSde)

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
