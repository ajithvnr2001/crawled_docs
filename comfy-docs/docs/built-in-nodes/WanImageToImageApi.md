---
url: https://docs.comfy.org/built-in-nodes/WanImageToImageApi/
title: WanImageToImageApi - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:24.205532+00:00
---

# WanImageToImageApi - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/WanImageToImageApi/

Wan

# WanImageToImageApi - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Wan Image to Image node generates an image from one or two input images and a text prompt.

Copy pageCopy page

The Wan Image to Image node generates an image from one or two input images and a text prompt. It transforms your input images based on the description you provide, creating a new image that maintains the aspect ratio of your original input. The output image is fixed at 1.6 megapixels regardless of the input size.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| Model to use (default: “wan2.5-i2i-preview”).| COMBO| Yes| ”wan2.5-i2i-preview”  
`image`| Single-image editing or multi-image fusion. Maximum 2 images.| IMAGE| Yes| -  
`prompt`| Prompt describing the elements and visual features. Supports English and Chinese (default: empty).| STRING| Yes| -  
`negative_prompt`| Negative prompt describing what to avoid (default: empty).| STRING| No| -  
`seed`| Seed to use for generation (default: 0).| INT| No| 0 to 2147483647  
`watermark`| Whether to add an AI-generated watermark to the result (default: false).| BOOLEAN| No| -  
  
**Note:** This node accepts exactly 1 or 2 input images. If you provide more than 2 images or no images at all, the node will return an error.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The generated image based on the input images and text prompts.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToImageApi/en.md)

* * *

**Source fingerprint (SHA-256):** `e78e5fb43d92c839448d3449b89445fb5db081ee8c947e44edcc048b8740f45d`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/WanImageToImageApi.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/WanImageToImageApi)

[TopazImageEnhanceV2 - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/TopazImageEnhanceV2)[WanTextToImageApi - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/WanTextToImageApi)

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
