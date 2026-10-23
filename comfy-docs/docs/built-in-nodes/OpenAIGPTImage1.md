---
url: https://docs.comfy.org/built-in-nodes/OpenAIGPTImage1/
title: OpenAIGPTImage1 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:39.127894+00:00
---

# OpenAIGPTImage1 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/OpenAIGPTImage1/

Openai

# OpenAIGPTImage1 - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generates images synchronously through OpenAI’s GPT Image endpoint.

Copy pageCopy page

Generates images synchronously through OpenAI’s GPT Image endpoint. It can create new images from a text prompt or edit existing images when an input image and optional mask are provided. The node supports the `gpt-image-1`, `gpt-image-1.5`, and `gpt-image-2` models and is marked as deprecated.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Text prompt for GPT Image (default: "")| STRING| Yes| -  
`seed`| Random seed for generation; not implemented yet in backend (default: 0)| INT| No| 0 to 2147483647  
`quality`| Image quality, affects cost and generation time (default: “low”)| COMBO| No| ”low"  
"medium"  
"high”  
`background`| Return image with or without background (default: “auto”)| COMBO| No| ”auto"  
"opaque"  
"transparent”  
`size`| Image size. Select “Custom” to use the custom width and height (GPT Image 2 only) (default: “auto”)| COMBO| No| ”auto"  
"1024x1024"  
"1024x1536"  
"1536x1024"  
"2048x2048"  
"2048x1152"  
"1152x2048"  
"3840x2160"  
"2160x3840"  
"Custom”  
`n`| How many images to generate (default: 1)| INT| No| 1 to 8  
`image`| Optional reference image for image editing| IMAGE| No| -  
`mask`| Optional mask for inpainting (white areas will be replaced)| MASK| No| -  
`model`| GPT Image model to use (default: “gpt-image-2”)| COMBO| No| ”gpt-image-1"  
"gpt-image-1.5"  
"gpt-image-2”  
`custom_width`| Used only when `size` is “Custom”. Must be a multiple of 16 (GPT Image 2 only) (default: 1024)| INT| No| 1024 to 3840, step 16  
`custom_height`| Used only when `size` is “Custom”. Must be a multiple of 16 (GPT Image 2 only) (default: 1024)| INT| No| 1024 to 3840, step 16  
  
**Parameter Constraints:**

  * When `image` is provided, the node uses the image editing endpoint.
  * `mask` can only be used when `image` is provided.
  * When using `mask`, only single images are supported (batch size must be 1).
  * `mask` and `image` must be the same size.
  * Custom resolution (`size` = “Custom”) is only supported by the `gpt-image-2` model.
  * Custom width and height must be multiples of 16.
  * The longest edge of a custom resolution must be 3840 or less.
  * Custom resolution aspect ratio must not exceed 3:1.
  * Custom resolution total pixels must be between 655,360 and 8,294,400.
  * The `gpt-image-1` and `gpt-image-1.5` models only support the sizes `auto`, `1024x1024`, `1024x1536`, and `1536x1024`. Other sizes are only supported by the `gpt-image-2` model.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| Generated or edited image(s). Multiple images are returned as a batch; if returned images have different dimensions, they are resized to match the first image.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImage1/en.md)

* * *

**Source fingerprint (SHA-256):** `f0f0db7fd2cdf8efd2155522b289aa8f3f939fa79a6e9060b0ffbb2dd20efa1e`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/OpenAIGPTImage1.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/OpenAIGPTImage1)

[MetaMuseImageTextToImageApi - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/MetaMuseImageTextToImageApi)[OpenAIGPTImageNodeV2 - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/OpenAIGPTImageNodeV2)

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
