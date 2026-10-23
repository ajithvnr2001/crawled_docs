---
url: https://docs.comfy.org/built-in-nodes/FluxProFillNode/
title: FluxProFillNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:29.193351+00:00
---

# FluxProFillNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/FluxProFillNode/

BFL

# FluxProFillNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Inpaints image based on mask and prompt.

Copy pageCopy page

Inpaints image based on mask and prompt. This node uses the Flux.1 model to fill in masked areas of an image according to the provided text description, generating new content that matches the surrounding image.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The input image to be inpainted| IMAGE| Yes| -  
`mask`| The mask defining which areas of the image should be filled| MASK| Yes| -  
`prompt`| Prompt for the image generation (default: empty string)| STRING| No| -  
`prompt_upsampling`| Whether to perform upsampling on the prompt. If active, automatically modifies the prompt for more creative generation, but results are nondeterministic (same seed will not produce exactly the same result). (default: false)| BOOLEAN| No| -  
`guidance`| Guidance strength for the image generation process (default: 60)| FLOAT| No| 1.5-100  
`steps`| Number of steps for the image generation process (default: 50)| INT| No| 15-50  
`seed`| The random seed used for creating the noise. (default: 0)| INT| No| 0-18446744073709551615  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output_image`| The generated image with the masked areas filled according to the prompt| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProFillNode/en.md)

* * *

**Source fingerprint (SHA-256):** `11aa071c52897788d9d7dae4105ffdf747d3cb91d75a0ad7cfacd7ca1ddd2ac1`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/FluxProFillNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/FluxProFillNode)

[FluxProExpandNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/FluxProExpandNode)[FluxProUltraImageNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/FluxProUltraImageNode)

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
