---
url: https://docs.comfy.org/built-in-nodes/GeminiNanoBanana2V2/
title: GeminiNanoBanana2V2 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:59.610511+00:00
---

# GeminiNanoBanana2V2 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/GeminiNanoBanana2V2/

Gemini

# GeminiNanoBanana2V2 - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node generates or edits images by sending a text prompt to Google’s Vertex AI API through Gemini image models.

Copy pageCopy page

This node generates or edits images by sending a text prompt to Google’s Vertex AI API through Gemini image models. It creates new images from a description or modifies existing images using optional reference images.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| Selects the Gemini image model to use. The chosen model determines the available resolution options and model-specific inputs.| DYNAMIC_COMBO| Yes| `"Gemini Nano Banana 2.1"`  
`"Nano Banana 2 (Gemini 3.1 Flash Image)"`  
`"Nano Banana 2 Lite"`  
`prompt`| Text prompt describing the image to generate or the edits to apply. Include any constraints, styles, or details the model should follow. Must not be empty. (default: empty)| STRING| Yes| N/A  
`seed`| When the seed is fixed to a specific value, the model makes a best effort to provide the same response for repeated requests. Deterministic output isn’t guaranteed. Also, changing the model or parameter settings, such as the temperature, can cause variations in the response even when you use the same seed value. By default, a random seed value is used. (default: 42)| INT| Yes| 0 to 18446744073709551615  
`response_modalities`| Determines the response format. IMAGE returns only an image; IMAGE+TEXT returns an image and a text response. (default: IMAGE) Advanced parameter.| COMBO| Yes| `"IMAGE"`  
`"IMAGE+TEXT"`  
`system_prompt`| Foundational instructions that dictate an AI’s behavior. Defaults to a built-in prompt that instructs the model to always produce an image. Advanced parameter.| STRING| No| N/A  
`temperature`| Controls randomness in generation. Lower is more focused/deterministic. (default: 1.0) Advanced parameter.| FLOAT| No| 0.0 to 2.0 (step 0.01)  
`top_p`| Nucleus sampling threshold. Lower is more focused, higher more diverse. (default: 0.95) Advanced parameter.| FLOAT| No| 0.0 to 1.0 (step 0.01)  
  
### 

​

Gemini Nano Banana 2.1 Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`aspect_ratio`| If set to ‘auto’, matches your input image’s aspect ratio; if no image is provided, a 16:9 square is usually generated. (default: auto)| COMBO| Yes| `"auto"`  
`"1:1"`  
`"2:3"`  
`"3:2"`  
`"3:4"`  
`"4:3"`  
`"4:5"`  
`"5:4"`  
`"9:16"`  
`"16:9"`  
`"21:9"`  
`"1:4"`  
`"4:1"`  
`"8:1"`  
`"1:8"`  
`resolution`| Target output resolution.| COMBO| Yes| `"1K"`  
`"2K"`  
`"4K"`  
`thinking_level`| Selects the thinking level used by the model.| COMBO| Yes| `"MINIMAL"`  
`"MEDIUM"`  
`"HIGH"`  
  
### 

​

Nano Banana 2 (Gemini 3.1 Flash Image) Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`aspect_ratio`| If set to ‘auto’, matches your input image’s aspect ratio; if no image is provided, a 16:9 square is usually generated. (default: auto)| COMBO| Yes| `"auto"`  
`"1:1"`  
`"2:3"`  
`"3:2"`  
`"3:4"`  
`"4:3"`  
`"4:5"`  
`"5:4"`  
`"9:16"`  
`"16:9"`  
`"21:9"`  
`"1:4"`  
`"4:1"`  
`"8:1"`  
`"1:8"`  
`resolution`| Target output resolution.| COMBO| Yes| `"1K"`  
`"2K"`  
`"4K"`  
`thinking_level`| Selects the thinking level used by the model.| COMBO| Yes| `"MINIMAL"`  
`"HIGH"`  
  
### 

​

Nano Banana 2 Lite Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`aspect_ratio`| If set to ‘auto’, matches your input image’s aspect ratio; if no image is provided, a 16:9 square is usually generated. (default: auto)| COMBO| Yes| `"auto"`  
`"1:1"`  
`"2:3"`  
`"3:2"`  
`"3:4"`  
`"4:3"`  
`"4:5"`  
`"5:4"`  
`"9:16"`  
`"16:9"`  
`"21:9"`  
`"1:4"`  
`"4:1"`  
`"8:1"`  
`"1:8"`  
`resolution`| Target output resolution.| COMBO| Yes| `"1K"`  
`thinking_level`| Selects the thinking level used by the model.| COMBO| Yes| `"MINIMAL"`  
`"HIGH"`  
  
### 

​

Reference Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`images`| Optional reference image(s). Up to 14 images total. Growable slot: connect `image_1` through `image_14`.| IMAGE| No| 0 to 14 images  
`files`| Optional file(s) to use as context for the model. Accepts inputs from the Gemini Generate Content Input Files node.| GEMINI_INPUT_FILES| No| N/A  
  
**Note:** A maximum of 14 reference images can be connected to the `images` input; exceeding this limit raises an error.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| The generated or edited image.| IMAGE  
`STRING`| A text description or caption generated by the model. Empty when no text is returned, such as when `response_modalities` is set to `IMAGE`.| STRING  
`thought_image`| First image from the model’s thinking process. Only available with IMAGE+TEXT modality.| IMAGE  
  
**Note:** The `STRING` output is empty when `response_modalities` is set to `IMAGE`. If the model does not generate an image in this mode, the node raises an error suggesting switching to IMAGE+TEXT to view the model’s reasoning.

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2V2/en.md)

* * *

**Source fingerprint (SHA-256):** `238d661259e99fd0ce8cae227d873713bbad60aa5eccb32447be464317e39ddd`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/GeminiNanoBanana2V2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/GeminiNanoBanana2V2)

[GeminiNanoBanana2 - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/GeminiNanoBanana2)[GrokImageEditNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/GrokImageEditNode)

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
