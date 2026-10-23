---
url: https://docs.comfy.org/built-in-nodes/GeminiImage2Node/
title: GeminiImage2Node - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:59.133455+00:00
---

# GeminiImage2Node - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/GeminiImage2Node/

Gemini

# GeminiImage2Node - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generate or edit images synchronously through the Google Vertex AI Gemini API.

Copy pageCopy page

Generate or edit images synchronously through the Google Vertex AI Gemini API. You provide a text prompt and can optionally attach reference images or Gemini input files. The node returns the generated image and, depending on the selected response mode, a text response.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Text prompt describing the image to generate or the edits to apply. Include any constraints, styles, or details the model should follow. The prompt must contain at least one character after whitespace is removed.| STRING| Yes| N/A  
`model`| The Gemini model to use for generation. The “Nano Banana 2 (Gemini 3.1 Flash Image)” option is sent as `gemini-3.1-flash-image`; “gemini-3-pro-image-preview” is sent as `gemini-3-pro-image`.| COMBO| Yes| ”gemini-3-pro-image-preview"  
"Nano Banana 2 (Gemini 3.1 Flash Image)“  
`seed`| When the seed is fixed to a specific value, the model makes a best effort to provide the same response for repeated requests. Deterministic output isn’t guaranteed. Also, changing the model or parameter settings, such as the temperature, can cause variations in the response even when you use the same seed value. By default, a random seed value is used. Default: 42.| INT| Yes| 0 to 18446744073709551615  
`aspect_ratio`| If set to ‘auto’, matches your input image’s aspect ratio; if no image is provided, a 16:9 square is usually generated. Default: “auto”.| COMBO| Yes| ”auto"  
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
`response_modalities`| Choose ‘IMAGE’ for image-only output, or ‘IMAGE+TEXT’ to return both the generated image and a text response. Advanced setting.| COMBO| Yes| ”IMAGE+TEXT"  
"IMAGE”  
`images`| Optional reference image(s). To include multiple images, use the Batch Images node (up to 14).| IMAGE| No| N/A  
`files`| Optional file(s) to use as context for the model. Accepts inputs from the Gemini Generate Content Input Files node.| GEMINI_INPUT_FILES| No| N/A  
`system_prompt`| Foundational instructions that dictate an AI’s behavior. Default: a pre-defined system prompt for image generation. Advanced setting.| STRING| No| N/A  
  
**Constraints:**

  * The `images` input supports a maximum of 14 images. If more are provided, an error is raised.
  * When more than 10 images are provided, the first 10 are uploaded as URL references and the remaining images are sent inline in the request.
  * The `files` input must be connected to a node that outputs the `GEMINI_INPUT_FILES` data type.
  * When `response_modalities` is set to `"IMAGE"`, only the image is returned and the text output is empty.
  * The `prompt` input is validated and must contain at least one character after whitespace is removed.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The image generated or edited by the Gemini model.| IMAGE  
`string`| The text response from the model. This output is empty if `response_modalities` is set to `"IMAGE"`.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImage2Node/en.md)

* * *

**Source fingerprint (SHA-256):** `02293dad786d4b441da3174fa76f6c5847f122d294bd7e1f765ffd72420034a4`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/GeminiImage2Node.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/GeminiImage2Node)

[ClarityCrystalUpscaleNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ClarityCrystalUpscaleNode)[GeminiImageNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/GeminiImageNode)

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
