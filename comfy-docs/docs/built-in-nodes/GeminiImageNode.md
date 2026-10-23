---
url: https://docs.comfy.org/built-in-nodes/GeminiImageNode/
title: GeminiImageNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:59.508189+00:00
---

# GeminiImageNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/GeminiImageNode/

Gemini

# GeminiImageNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The GeminiImage node generates text and image responses from Google’s Gemini AI models.

Copy pageCopy page

The GeminiImage node generates text and image responses from Google’s Gemini AI models. It allows you to provide multimodal inputs including text prompts, images, and files to create coherent text and image outputs. The node handles all API communication and response parsing with the latest Gemini models.

## 

​

Inputs

Parameter| Description| Data Type| Input Type| Default| Range  
---|---|---|---|---|---  
`prompt`| Text prompt for generation| STRING| required| ""| -  
`model`| The Gemini model to use for generating responses| COMBO| required| gemini_2_5_flash_image_preview| Available Gemini models  
Options extracted from GeminiImageModel enum  
`seed`| When seed is fixed to a specific value, the model makes a best effort to provide the same response for repeated requests. Deterministic output isn’t guaranteed. Also, changing the model or parameter settings, such as the temperature, can cause variations in the response even when you use the same seed value. By default, a random seed value is used| INT| required| 42| 0 to 18446744073709551615  
`images`| Optional image(s) to use as context for the model. To include multiple images, you can use the Batch Images node| IMAGE| optional| None| -  
`files`| Optional file(s) to use as context for the model. Accepts inputs from the Gemini Generate Content Input Files node| GEMINI_INPUT_FILES| optional| None| -  
  
_Note: The node includes hidden parameters (`auth_token`, `comfy_api_key`, `unique_id`) that are automatically handled by the system and do not require user input._

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| The generated image response from the Gemini model| IMAGE  
`STRING`| The generated text response from the Gemini model| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImageNode/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/GeminiImageNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/GeminiImageNode)

[GeminiImage2Node - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/GeminiImage2Node)[GeminiNanoBanana2 - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/GeminiNanoBanana2)

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
