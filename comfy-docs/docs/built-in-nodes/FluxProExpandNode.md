---
url: https://docs.comfy.org/built-in-nodes/FluxProExpandNode/
title: FluxProExpandNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-18T12:01:27.631471+00:00
---

# FluxProExpandNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/FluxProExpandNode/

BFL

# FluxProExpandNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Outpaints image based on prompt. This node expands an image by adding pixels to the top, bottom, left

Copy pageCopy page

Outpaints image based on prompt. This node expands an image by adding pixels to the top, bottom, left, and right sides while generating new content that matches the provided text description.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The input image to be expanded| IMAGE| Yes| -  
`prompt`| Prompt for the image generation (default: "")| STRING| No| -  
`prompt_upsampling`| Whether to perform upsampling on the prompt. If active, automatically modifies the prompt for more creative generation, but results are nondeterministic (same seed will not produce exactly the same result). (default: False)| BOOLEAN| No| -  
`top`| Number of pixels to expand at the top of the image (default: 0)| INT| No| 0-2048  
`bottom`| Number of pixels to expand at the bottom of the image (default: 0)| INT| No| 0-2048  
`left`| Number of pixels to expand at the left of the image (default: 0)| INT| No| 0-2048  
`right`| Number of pixels to expand at the right of the image (default: 0)| INT| No| 0-2048  
`guidance`| Guidance strength for the image generation process (default: 60)| FLOAT| No| 1.5-100  
`steps`| Number of steps for the image generation process (default: 50)| INT| No| 15-50  
`seed`| The random seed used for creating the noise. (default: 0)| INT| No| 0-18446744073709551615  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The expanded output image| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProExpandNode/en.md)

* * *

**Source fingerprint (SHA-256):** `faff1e1311a3208066a499a358923c6e335ea1785baeafe3761484641f7f12d6`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/FluxProExpandNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/FluxProExpandNode)

[FluxEraseNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/FluxEraseNode)[FluxProFillNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/FluxProFillNode)

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
