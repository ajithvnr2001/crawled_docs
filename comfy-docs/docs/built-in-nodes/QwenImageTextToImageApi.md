---
url: https://docs.comfy.org/built-in-nodes/QwenImageTextToImageApi/
title: QwenImageTextToImageApi - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:47.292634+00:00
---

# QwenImageTextToImageApi - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/QwenImageTextToImageApi/

Qwen

# QwenImageTextToImageApi - ComfyUI Built-in Node Documentation

Copy pageCopy page

Qwen Image 3 Text to Image generates one or more images from a text prompt using the Qwen-Image 3.0 models.

Copy pageCopy page

Qwen Image 3 Text to Image generates one or more images from a text prompt using the Qwen-Image 3.0 models. You select a model and provide a prompt, and the node returns the generated images as a batch.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| Model to use (default: “qwen-image-3.0-pro”). This composite selector also provides the prompt, negative prompt, image width, and image height.| DYNAMIC_COMBO| Yes| ”qwen-image-3.0-pro"  
"qwen-image-3.0”  
`n`| Number of images to generate, returned as a batch (default: 1).| INT| No| 1 to 6  
`seed`| Seed to use for generation (default: 42). Can be set to update automatically after each generation.| INT| No| 0 to 2147483647  
`prompt_extend`| Whether to enhance the prompt with AI assistance (default: true). Advanced option.| BOOLEAN| No| true  
false  
`watermark`| Whether to add an AI-generated watermark to the result (default: false). Advanced option.| BOOLEAN| No| true  
false  
  
### 

​

qwen-image-3.0-pro and qwen-image-3.0 Inputs

Shared by qwen-image-3.0-pro and qwen-image-3.0.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Prompt describing the image. Supports English and Chinese. Must contain at least 1 character.| STRING| Yes| Free text  
`negative_prompt`| Negative prompt describing what to avoid (default: "").| STRING| No| Free text  
`width`| The total pixel area must be between 512x512 and 2560x2560; any aspect ratio within that area works. (default: 1024)| INT| No| 256 to 2560 (step 16)  
`height`| The total pixel area must be between 512x512 and 2560x2560; any aspect ratio within that area works. (default: 1024)| INT| No| 256 to 2560 (step 16)  
  
Note: The `model` input is a composite selector with the sub-fields `model` (model ID), `prompt` (required, must contain at least 1 character), `negative_prompt` (optional), `width`, and `height`. The combined pixel area of `width` and `height` must be between 262,144 pixels (512x512) and 6,553,600 pixels (2560x2560), and the aspect ratio must stay between 1:8 and 8:1.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The generated image or images, returned as a batch.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageTextToImageApi/en.md)

* * *

**Source fingerprint (SHA-256):** `c58454d26360a78b795b28dd776fa8650ec0ec7b1e4a902e81b6561f292e0fa2`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/QwenImageTextToImageApi.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/QwenImageTextToImageApi)

[QwenImageEditApi - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/QwenImageEditApi)[RecraftColorRGB - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/RecraftColorRGB)

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
