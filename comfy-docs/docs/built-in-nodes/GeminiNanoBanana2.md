---
url: https://docs.comfy.org/built-in-nodes/GeminiNanoBanana2/
title: GeminiNanoBanana2 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:59.417957+00:00
---

# GeminiNanoBanana2 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/GeminiNanoBanana2/

Gemini

# GeminiNanoBanana2 - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Nano Banana 2 node generates or edits images synchronously via the Google Vertex API using the Gemini 3.1 Flash Image model.

Copy pageCopy page

The Nano Banana 2 node generates or edits images synchronously via the Google Vertex API using the Gemini 3.1 Flash Image model. It sends a text prompt, along with optional reference images or files, and returns the generated image, any accompanying text, and optionally an image from the model’s thinking process. This node is marked as deprecated.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Text prompt describing the image to generate or the edits to apply. Include any constraints, styles, or details the model should follow. Cannot be empty or whitespace only. (default: empty)| STRING| Yes| N/A  
`model`| The Gemini model to use for image generation.| COMBO| Yes| ”Nano Banana 2 (Gemini 3.1 Flash Image)“  
`seed`| When the seed is fixed to a specific value, the model makes a best effort to provide the same response for repeated requests. Deterministic output isn’t guaranteed. Also, changing the model or parameter settings, such as the temperature, can cause variations in the response even when you use the same seed value. By default, a random seed value is used. (default: 42)| INT| Yes| 0 to 18446744073709551615  
`aspect_ratio`| If set to ‘auto’, matches your input image’s aspect ratio; if no image is provided, a 16:9 square is usually generated. (default: “auto”)| COMBO| Yes| ”auto"  
"1:1"  
"2:3"  
"3:2"  
"3:4"  
"4:3"  
"4:5"  
"5:4"  
"9:16"  
"16:9"  
"21:9”  
`resolution`| Target output resolution. For 2K/4K the native Gemini upscaler is used.| COMBO| Yes| ”1K"  
"2K"  
"4K”  
`response_modalities`| Determines the type of content the model returns: “IMAGE” returns only an image, “IMAGE+TEXT” also returns text. (advanced)| COMBO| Yes| ”IMAGE"  
"IMAGE+TEXT”  
`thinking_level`| Controls the depth of the model’s reasoning process.| COMBO| Yes| ”MINIMAL"  
"HIGH”  
`images`| Optional reference image(s). To include multiple images, use the Batch Images node (up to 14).| IMAGE| No| 1 to 14 images  
`files`| Optional file(s) to use as context for the model. Accepts inputs from the Gemini Generate Content Input Files node.| CUSTOM| No| N/A  
`system_prompt`| Foundational instructions that dictate an AI’s behavior. (default: a preset prompt that instructs the model to always produce an image) (advanced)| STRING| No| N/A  
  
**Note:** The `images` input supports a maximum of 14 images. If more are provided, the node raises an error. The `prompt` input must not be empty or whitespace-only.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The primary image generated or edited by the model.| IMAGE  
`string`| Any text content returned by the model.| STRING  
`thought_image`| First image from the model’s thinking process. Only available with `thinking_level` set to HIGH and the IMAGE+TEXT modality.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2/en.md)

* * *

**Source fingerprint (SHA-256):** `d781c92f04d420985f8a5a593eb5f28f1f7b2af13abd11f2a7f6f285edcd9900`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/GeminiNanoBanana2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/GeminiNanoBanana2)

[GeminiImageNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/GeminiImageNode)[GeminiNanoBanana2V2 - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/GeminiNanoBanana2V2)

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
