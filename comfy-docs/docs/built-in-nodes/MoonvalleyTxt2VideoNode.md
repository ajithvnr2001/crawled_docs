---
url: https://docs.comfy.org/built-in-nodes/MoonvalleyTxt2VideoNode/
title: MoonvalleyTxt2VideoNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:37.662866+00:00
---

# MoonvalleyTxt2VideoNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MoonvalleyTxt2VideoNode/

Advanced

# MoonvalleyTxt2VideoNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Moonvalley Marey Text to Video node generates video content from text descriptions using the Moonvalley API.

Copy pageCopy page

The Moonvalley Marey Text to Video node generates video content from text descriptions using the Moonvalley API. It takes a text prompt and converts it into a video with customizable settings for resolution, quality, and style. The node handles the entire process from sending the generation request to downloading the final video output.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Text description of the video content to generate| STRING| Yes| -  
`negative_prompt`| Negative prompt text (default: extensive list of excluded elements like synthetic, scene cut, artifacts, noise, etc.)| STRING| No| -  
`resolution`| Resolution of the output video (default: “16:9 (1920 x 1080)“)| STRING| No| ”16:9 (1920 x 1080)"  
"9:16 (1080 x 1920)"  
"1:1 (1152 x 1152)"  
"4:3 (1536 x 1152)"  
"3:4 (1152 x 1536)"  
"21:9 (2560 x 1080)“  
`prompt_adherence`| Guidance scale for generation control (default: 4.0)| FLOAT| No| 1.0-20.0  
`seed`| Random seed value (default: 9)| INT| No| 0-4294967295  
`steps`| Inference steps (default: 33)| INT| No| 1-100  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`video`| The generated video output based on the text prompt| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoonvalleyTxt2VideoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `3654043567d7aca3af741d706ee07a8d2e28dbeb4b5b8755514b790aa7c1bd41`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MoonvalleyTxt2VideoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MoonvalleyTxt2VideoNode)

[MoonvalleyImg2VideoNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/MoonvalleyImg2VideoNode)[MoonvalleyVideo2VideoNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/MoonvalleyVideo2VideoNode)

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
