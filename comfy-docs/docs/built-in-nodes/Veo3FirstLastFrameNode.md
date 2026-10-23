---
url: https://docs.comfy.org/built-in-nodes/Veo3FirstLastFrameNode/
title: Veo3FirstLastFrameNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:18.656191+00:00
---

# Veo3FirstLastFrameNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Veo3FirstLastFrameNode/

Veo

# Veo3FirstLastFrameNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Veo3FirstLastFrameNode uses Google’s Veo 3 model to generate a video based on a text prompt

Copy pageCopy page

The Veo3FirstLastFrameNode uses Google’s Veo 3 model to generate a video based on a text prompt, with a provided first and last frame that define the start and end of the video sequence.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Text description of the video (default: empty string).| STRING| Yes| N/A  
`negative_prompt`| Negative text prompt to guide what to avoid in the video (default: empty string).| STRING| No| N/A  
`resolution`| The resolution of the output video.| COMBO| Yes| `"720p"`  
`"1080p"`  
`"4k"`  
`aspect_ratio`| Aspect ratio of the output video (default: “16:9”).| COMBO| No| `"16:9"`  
`"9:16"`  
`duration`| Duration of the output video in seconds (default: 8, step: 2).| INT| No| 4 to 8  
`seed`| Seed for video generation (default: 0).| INT| No| 0 to 4294967295  
`first_frame`| The start frame for the video.| IMAGE| Yes| N/A  
`last_frame`| The end frame for the video.| IMAGE| Yes| N/A  
`model`| The specific Veo model to use for generation (default: “veo-3.1-generate”).| COMBO| No| `"veo-3.1-generate"`  
`"veo-3.1-fast-generate"`  
`"veo-3.1-lite"`  
`generate_audio`| Generate audio for the video (default: True).| BOOLEAN| No| N/A  
  
**Note:** The `veo-3.1-lite` model does not support 4K resolution. If you select `veo-3.1-lite` and `4k` resolution, an error will occur.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated video file.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Veo3FirstLastFrameNode/en.md)

* * *

**Source fingerprint (SHA-256):** `2fe55d2a1d018e58fd290c901c596708898acda835d2358adf36ed80103aeb6e`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Veo3FirstLastFrameNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Veo3FirstLastFrameNode)

[TopazVideoEnhanceV2 - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/TopazVideoEnhanceV2)[Veo3VideoGenerationNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Veo3VideoGenerationNode)

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
