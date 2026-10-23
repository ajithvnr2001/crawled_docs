---
url: https://docs.comfy.org/built-in-nodes/RunwayTextToImageNode/
title: RunwayTextToImageNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:53.675099+00:00
---

# RunwayTextToImageNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/RunwayTextToImageNode/

Runway

# RunwayTextToImageNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Runway Text to Image node generates images from text prompts using Runway’s Gen 4 model.

Copy pageCopy page

The Runway Text to Image node generates images from text prompts using Runway’s Gen 4 model. You can provide a text description and optionally include a reference image to guide the image generation process. The node handles the API communication and returns the generated image.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Text prompt for the generation (default: "")| STRING| Yes| -  
`ratio`| Aspect ratio for the generated image| COMBO| Yes| ”16:9"  
"1:1"  
"21:9"  
"2:3"  
"3:2"  
"4:5"  
"5:4"  
"9:16"  
"9:21”  
`reference_image`| Optional reference image to guide the generation| IMAGE| No| -  
  
**Note:** The reference image must have dimensions not exceeding 7999x7999 pixels and an aspect ratio between 0.5 and 2.0. When a reference image is provided, it guides the image generation process.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated image based on the text prompt and optional reference image| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayTextToImageNode/en.md)

* * *

**Source fingerprint (SHA-256):** `c9403da2e9ad8f663d3eea32eb549843696262e4472fc8d58c1f56ef9cc5aa7d`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/RunwayTextToImageNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/RunwayTextToImageNode)

[ReveImageRemixNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ReveImageRemixNode)[HunyuanImageEditApi - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/HunyuanImageEditApi)

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
