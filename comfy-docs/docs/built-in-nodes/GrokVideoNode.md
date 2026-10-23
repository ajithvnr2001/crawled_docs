---
url: https://docs.comfy.org/built-in-nodes/GrokVideoNode/
title: GrokVideoNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:27.714806+00:00
---

# GrokVideoNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/GrokVideoNode/

Grok

# GrokVideoNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Grok Video node generates a short video from a text description.

Copy pageCopy page

The Grok Video node generates a short video from a text description. It can create a video from scratch using a prompt, or generate a video from a single input image. The node sends the request to an external API and returns the generated video.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The model to use for video generation (default: `"grok-imagine-video-1.5-lite"`).| COMBO| Yes| `"grok-imagine-video"`  
`"grok-imagine-video-1.5"`  
`"grok-imagine-video-1.5-lite"`  
`prompt`| Text description of the desired video. Optional for the `grok-imagine-video-1.5` models when an input image is provided.| STRING| Yes| -  
`resolution`| The resolution of the output video. `1080p` is not available for `grok-imagine-video`.| COMBO| Yes| `"480p"`  
`"720p"`  
`"1080p"`  
`aspect_ratio`| The aspect ratio of the output video. Ignored when an input image is provided; the video follows the image’s aspect ratio.| COMBO| Yes| `"auto"`  
`"16:9"`  
`"4:3"`  
`"3:2"`  
`"1:1"`  
`"2:3"`  
`"3:4"`  
`"9:16"`  
`duration`| The duration of the output video in seconds (default: 6).| INT| Yes| 1 to 15  
`seed`| Seed to determine if node should re-run; actual results are nondeterministic regardless of seed (default: 0).| INT| Yes| 0 to 2147483647  
`image`| Optional starting image. If omitted, the video is generated from the text prompt alone.| IMAGE| No| -  
  
**Note:** When an `image` is provided, only one input image is supported; providing multiple images will cause an error. The `prompt` must be non-empty after stripping whitespace when no image is provided, or when using `grok-imagine-video` even with an image. For the `grok-imagine-video-1.5` models, the `prompt` is optional only when an input image is provided. The `1080p` resolution is not available for `grok-imagine-video`. When `aspect_ratio` is set to `"auto"`, the aspect ratio is chosen automatically by the service; when an input image is provided, `aspect_ratio` is ignored and the video follows the image’s aspect ratio.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated video.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `ed5a1c39598a319d5b350b19f39a352dedd1150471695d25f7637fc0f8735d02`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/GrokVideoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/GrokVideoNode)

[GrokVideoExtendNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/GrokVideoExtendNode)[GrokVideoReferenceNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/GrokVideoReferenceNode)

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
