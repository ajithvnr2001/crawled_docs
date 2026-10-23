---
url: https://docs.comfy.org/built-in-nodes/HunyuanImageEditApi/
title: HunyuanImageEditApi - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:04.846569+00:00
---

# HunyuanImageEditApi - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/HunyuanImageEditApi/

Tencent

# HunyuanImageEditApi - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Tencent HY Image: Edit node edits or combines reference images from a text instruction with Tencent’s Hunyuan Image model.

Copy pageCopy page

The Tencent HY Image: Edit node edits or combines reference images from a text instruction with Tencent’s Hunyuan Image model. Connect one to five images, describe the change in the prompt and refer to the images as `@Image1`, `@Image2` and so on. The node uploads the reference images, sends the request to the API, and returns the edited result.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The model used for editing. The selected model determines which additional inputs are shown.| DYNAMIC_COMBO| Yes| `"hy-image-3.5-preview"`  
  
### 

​

hy-image-3.5-preview Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| The editing instructions. Supports `@Image1`-style references to the connected images. Must not be empty (default: empty).| STRING| Yes| Any text  
`aspect_ratio`| Aspect ratio of the output. `"auto"` follows the aspect ratio of the first reference image and is not available at 4K. Ignored when `resolution` is `"custom"`.| COMBO| Yes| `"auto"`  
`"1:1"`  
`"3:2"`  
`"2:3"`  
`"4:3"`  
`"3:4"`  
`"16:9"`  
`"9:16"`  
`"21:9"`  
`"9:21"` (default: `"auto"`)  
`resolution`| Pixel area of the output: 1K is about 1024x1024, 2K about 2048x2048 and 4K about 4096x4096. Anything above 2K is rendered at 2K and upscaled by the model. Set to `"custom"` to use `width` and `height` instead of a preset area.| COMBO| Yes| `"1K"`  
`"2K"`  
`"4K"`  
`"custom"` (default: `"2K"`)  
`width`| Width of the output in pixels. Used only when `resolution` is `"custom"`.| INT| Yes| 256-8192, steps of 16 (default: 2048)  
`height`| Height of the output in pixels. Used only when `resolution` is `"custom"`.| INT| Yes| 256-8192, steps of 16 (default: 2048)  
`seed`| Seed used for generation. Results still vary between runs with the same seed.| INT| Yes| 0-2147483647 (default: 42)  
`reference_detail`| How much detail of the reference images the model sees: `"standard"` allows up to 1024x1024 pixels per image, `"high"` up to 2048x2048 and preserves small text and fine detail better, but takes longer. This is an advanced parameter.| COMBO| No| `"standard"`  
`"high"` (default: `"standard"`)  
`watermark`| Whether to add an AI-generated watermark to the result. This is an advanced parameter.| BOOLEAN| No| true  
false (default: false)  
  
### 

​

Reference Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`images`| The reference images to edit or combine. Growable slot: connect 1 to 5 images (`image_1` through `image_5`). Refer to them in the prompt as `@Image1` … `@Image5`, numbered in input order; a batched input counts once per image.| IMAGE| Yes| 1-5 images  
  
`prompt` must not be empty, and a prompt reference such as `@Image3` raises an error when only 1 or 2 images are connected. At most 5 reference images can be used in total, counting each image of a batch separately. With the `"custom"` resolution, `width` and `height` must both be multiples of 16 and their product must not exceed the 4096 x 4096 pixel area limit (about 16.7 megapixels); any aspect ratio works, although beyond roughly 6:1 the model starts repeating the subject. The `"auto"` aspect ratio only works within the 2K area limit, so at 4K pick an explicit aspect ratio or use `"custom"`.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| The edited image produced from the reference images and the prompt.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanImageEditApi/en.md)

* * *

**Source fingerprint (SHA-256):** `46c112347b51a2983521f87bbeb047289515f4073c48ba5d909fd3bae4597633`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/HunyuanImageEditApi.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/HunyuanImageEditApi)

[RunwayTextToImageNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/RunwayTextToImageNode)[HunyuanImageTextToImageApi - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/HunyuanImageTextToImageApi)

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
