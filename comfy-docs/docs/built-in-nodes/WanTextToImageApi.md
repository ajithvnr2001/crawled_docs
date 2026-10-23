---
url: https://docs.comfy.org/built-in-nodes/WanTextToImageApi/
title: WanTextToImageApi - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:26.038502+00:00
---

# WanTextToImageApi - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/WanTextToImageApi/

Wan

# WanTextToImageApi - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Wan Text to Image node generates images based on text descriptions.

Copy pageCopy page

The Wan Text to Image node generates images based on text descriptions. It uses AI models to create visual content from written prompts, supporting both English and Chinese text input. The node provides various controls to adjust the output image size, quality, and style preferences.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| Model to use (default: “wan2.5-t2i-preview”)| STRING| Yes| ”wan2.5-t2i-preview”  
`prompt`| Prompt describing the elements and visual features. Supports English and Chinese (default: empty)| STRING| Yes| -  
`negative_prompt`| Negative prompt describing what to avoid (default: empty)| STRING| No| -  
`width`| Image width in pixels (default: 1024, step: 32)| INT| No| 768-1440  
`height`| Image height in pixels (default: 1024, step: 32)| INT| No| 768-1440  
`seed`| Seed to use for generation (default: 0)| INT| No| 0-2147483647  
`prompt_extend`| Whether to enhance the prompt with AI assistance (default: True)| BOOLEAN| No| -  
`watermark`| Whether to add an AI-generated watermark to the result (default: False)| BOOLEAN| No| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated image based on the text prompt| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTextToImageApi/en.md)

* * *

**Source fingerprint (SHA-256):** `208b7c839da45316aeb1a14a3e9d176eeb09b2f931f764fb8a296da15ae3bd4e`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/WanTextToImageApi.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/WanTextToImageApi)

[WanImageToImageApi - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/WanImageToImageApi)[WavespeedImageUpscaleNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/WavespeedImageUpscaleNode)

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
