---
url: https://docs.comfy.org/built-in-nodes/OpenAIDalle3/
title: OpenAIDalle3 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:39.477385+00:00
---

# OpenAIDalle3 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/OpenAIDalle3/

Advanced

# OpenAIDalle3 - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generates images synchronously via OpenAI’s DALL·E 3 endpoint.

Copy pageCopy page

Generates images synchronously via OpenAI’s DALL·E 3 endpoint. This node takes a text prompt and creates corresponding images using OpenAI’s DALL·E 3 model, allowing you to specify image quality, style, and dimensions.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Text prompt for DALL·E (default: "")| STRING| Yes| -  
`seed`| Not implemented yet in backend (default: 0)| INT| No| 0 to 2147483647  
`quality`| Image quality (default: “standard”)| COMBO| No| ”standard"  
"hd”  
`style`| Vivid causes the model to lean towards generating hyper-real and dramatic images. Natural causes the model to produce more natural, less hyper-real looking images. (default: “natural”)| COMBO| No| ”natural"  
"vivid”  
`size`| Image size (default: “1024x1024”)| COMBO| No| ”1024x1024"  
"1024x1792"  
"1792x1024”  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| The generated image from DALL·E 3| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIDalle3/en.md)

* * *

**Source fingerprint (SHA-256):** `9077628610503d8c0afdd04e30dadac46106bd577d10f2d7aa10864db4430605`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/OpenAIDalle3.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/OpenAIDalle3)

[OpenAIDalle2 - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/OpenAIDalle2)[OpenAIVideoSora2 - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/OpenAIVideoSora2)

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
