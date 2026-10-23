---
url: https://docs.comfy.org/built-in-nodes/ViduTextToVideoNode/
title: ViduTextToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:21.613922+00:00
---

# ViduTextToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ViduTextToVideoNode/

Vidu

# ViduTextToVideoNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Vidu Text To Video Generation node creates videos from text descriptions.

Copy pageCopy page

The Vidu Text To Video Generation node creates videos from text descriptions. It uses the Vidu video generation model to transform your text prompts into video content with customizable settings for duration, aspect ratio, and visual style.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| Model name| COMBO| Yes| `viduq1`  
`prompt`| A textual description for video generation| STRING| Yes| -  
`duration`| Duration of the output video in seconds (default: 5)| INT| No| 5-5  
`seed`| Seed for video generation (0 for random) (default: 0)| INT| No| 0-2147483647  
`aspect_ratio`| The aspect ratio of the output video| COMBO| No| `16:9`  
`9:16`  
`1:1`  
`resolution`| Supported values may vary by model & duration| COMBO| No| `1080p`  
`movement_amplitude`| The movement amplitude of objects in the frame| COMBO| No| `auto`  
`small`  
`medium`  
`large`  
  
**Note:** The `prompt` field is required and cannot be empty. The `duration` parameter is currently fixed at 5 seconds.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated video based on the text prompt| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduTextToVideoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `913efbb516c40e03ced1fef59905c7efa7737f0506368c9afcacb3b65aa4af66`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ViduTextToVideoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ViduTextToVideoNode)

[ViduStartEndToVideoNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ViduStartEndToVideoNode)[HappyHorseImageToVideoApi - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/HappyHorseImageToVideoApi)

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
