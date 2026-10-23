---
url: https://docs.comfy.org/built-in-nodes/HunyuanImageTextToImageApi/
title: HunyuanImageTextToImageApi - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:04.611348+00:00
---

# HunyuanImageTextToImageApi - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/HunyuanImageTextToImageApi/

Tencent

# HunyuanImageTextToImageApi - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Tencent HY Image: Text to Image node generates an image from a text description with Tencent’s Hunyuan Image model.

Copy pageCopy page

The Tencent HY Image: Text to Image node generates an image from a text description with Tencent’s Hunyuan Image model. The prompt is sent to the API, which rewrites and expands it before rendering, and the finished image is returned as an image batch.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The model used for generation. The selected model determines which additional inputs are shown.| DYNAMIC_COMBO| Yes| `"hy-image-3.5-preview"`  
  
### 

​

hy-image-3.5-preview Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Describes the image to generate. The model rewrites and expands it before rendering. Must not be empty (default: empty).| STRING| Yes| Any text  
`aspect_ratio`| Aspect ratio of the output. `"auto"` lets the model pick the ratio from the prompt and is not available at 4K. Ignored when `resolution` is `"custom"`.| COMBO| Yes| `"auto"`  
`"1:1"`  
`"3:2"`  
`"2:3"`  
`"4:3"`  
`"3:4"`  
`"16:9"`  
`"9:16"`  
`"21:9"`  
`"9:21"` (default: `"auto"`)  
`resolution`| Pixel area of the image: 1K is about 1024x1024, 2K about 2048x2048 and 4K about 4096x4096. Anything above 2K is rendered at 2K and upscaled by the model. Set to `"custom"` to use `width` and `height` instead of a preset area.| COMBO| Yes| `"1K"`  
`"2K"`  
`"4K"`  
`"custom"` (default: `"2K"`)  
`width`| Width of the image in pixels. Used only when `resolution` is `"custom"`.| INT| Yes| 256-8192, steps of 16 (default: 2048)  
`height`| Height of the image in pixels. Used only when `resolution` is `"custom"`.| INT| Yes| 256-8192, steps of 16 (default: 2048)  
`seed`| Seed used for generation. Results still vary between runs with the same seed.| INT| Yes| 0-2147483647 (default: 42)  
`watermark`| Whether to add an AI-generated watermark to the result. This is an advanced parameter.| BOOLEAN| No| true  
false (default: false)  
  
`prompt` must not be empty. With the `"custom"` resolution, `width` and `height` must both be multiples of 16 and their product must not exceed the 4096 x 4096 pixel area limit (about 16.7 megapixels); any aspect ratio works, although beyond roughly 6:1 the model starts repeating the subject. The `"auto"` aspect ratio needs the model to choose a size, so it only works within the 2K area limit: at 4K, pick an explicit aspect ratio or use `"custom"`.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| The generated image.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanImageTextToImageApi/en.md)

* * *

**Source fingerprint (SHA-256):** `1d4e70d688c5aa4e79b81447da559e201078454077da34769f2a4f544fbba63f`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/HunyuanImageTextToImageApi.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/HunyuanImageTextToImageApi)

[HunyuanImageEditApi - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/HunyuanImageEditApi)[TopazImageEnhance - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/TopazImageEnhance)

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
