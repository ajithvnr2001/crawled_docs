---
url: https://docs.comfy.org/built-in-nodes/MoonvalleyImg2VideoNode/
title: MoonvalleyImg2VideoNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:38.636569+00:00
---

# MoonvalleyImg2VideoNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MoonvalleyImg2VideoNode/

Advanced

# MoonvalleyImg2VideoNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Moonvalley Marey Image to Video node transforms a reference image into a video using the Moonvalley API.

Copy pageCopy page

The Moonvalley Marey Image to Video node transforms a reference image into a video using the Moonvalley API. It takes an input image and a text prompt to generate a video with specified resolution, quality settings, and creative controls. The node handles the entire process from image upload to video generation and download.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The reference image used to generate the video| IMAGE| Yes| -  
`prompt`| Text description for video generation (multiline input)| STRING| Yes| -  
`negative_prompt`| Negative prompt text to exclude unwanted elements (default: extensive negative prompt list)| STRING| No| -  
`resolution`| Resolution of the output video (default: “16:9 (1920 x 1080)“)| COMBO| No| ”16:9 (1920 x 1080)"  
"9:16 (1080 x 1920)"  
"1:1 (1152 x 1152)"  
"4:3 (1536 x 1152)"  
"3:4 (1152 x 1536)“  
`prompt_adherence`| Guidance scale for generation control (default: 4.5, step: 1.0)| FLOAT| No| 1.0 - 20.0  
`seed`| Random seed value (default: 9, control after generate enabled)| INT| No| 0 - 4294967295  
`steps`| Number of denoising steps (default: 33, step: 1)| INT| No| 1 - 100  
  
**Constraints:**

  * The input image must have dimensions between 300x300 pixels and the maximum allowed height/width
  * Prompt and negative prompt text length is limited to the Moonvalley Marey maximum prompt length



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated video output| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoonvalleyImg2VideoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `674e69a7f106f6f961f10c179008b7bb1147bf0e569c72d207a105f3fab2aaf5`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MoonvalleyImg2VideoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MoonvalleyImg2VideoNode)

[LtxvApiTextToVideo - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LtxvApiTextToVideo)[MoonvalleyTxt2VideoNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/MoonvalleyTxt2VideoNode)

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
