---
url: https://docs.comfy.org/built-in-nodes/ByteDanceImageEditNode/
title: ByteDanceImageEditNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:29.535228+00:00
---

# ByteDanceImageEditNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ByteDanceImageEditNode/

Bytedance

# ByteDanceImageEditNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ByteDance Image Edit node allows you to modify images using ByteDance’s AI models through an API.

Copy pageCopy page

The ByteDance Image Edit node allows you to modify images using ByteDance’s AI models through an API. You provide an input image and a text prompt describing the desired changes, and the node processes the image according to your instructions. The node handles the API communication automatically and returns the edited image.

## 

​

Inputs

Parameter| Description| Data Type| Input Type| Default| Range  
---|---|---|---|---|---  
`model`| Model name| MODEL| COMBO| seededit_3| Image2ImageModelName options  
`image`| The base image to edit| IMAGE| IMAGE| -| -  
`prompt`| Instruction to edit image| STRING| STRING| ""| -  
`seed`| Seed to use for generation| INT| INT| 0| 0-2147483647  
`guidance_scale`| Higher value makes the image follow the prompt more closely| FLOAT| FLOAT| 5.5| 1.0-10.0  
`watermark`| Whether to add an “AI generated” watermark to the image| BOOLEAN| BOOLEAN| True| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| The edited image returned from the ByteDance API| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageEditNode/en.md)

* * *

**Source fingerprint (SHA-256):** `9dc13d89f84756b545120efb5535e08ada163d4534975809f5056bdf7d8bfb73`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ByteDanceImageEditNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ByteDanceImageEditNode)

[Flux 1.1 [pro] Ultra Image - ComfyUI Native Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/partner-node/image/bfl/flux-1-1-pro-ultra-image)[Ideogram V1 - ComfyUI Native Node DocumentationNext](https://docs.comfy.org/built-in-nodes/partner-node/image/ideogram/ideogram-v1)

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
