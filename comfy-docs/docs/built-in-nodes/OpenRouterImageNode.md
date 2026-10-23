---
url: https://docs.comfy.org/built-in-nodes/OpenRouterImageNode/
title: OpenRouterImageNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:39.900099+00:00
---

# OpenRouterImageNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/OpenRouterImageNode/

Openrouter

# OpenRouterImageNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node generates or edits images through OpenRouter using Microsoft’s MAI-Image-2.6 models.

Copy pageCopy page

This node generates or edits images through OpenRouter using Microsoft’s MAI-Image-2.6 models. It supports text-to-image generation as well as image-guided editing with up to five reference images, in seven aspect ratios at either 1K or 1.5K resolution.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The OpenRouter image model used to generate the image. Selecting a model reveals the model-specific options listed below.| DYNAMIC_COMBO| Yes| `microsoft/mai-image-2.6`  
`microsoft/mai-image-2.6-flash`  
  
### 

​

Mai Image 2.6 and Mai Image 2.6 Flash Inputs

Shared by both model options (`microsoft/mai-image-2.6` and `microsoft/mai-image-2.6-flash`), which expose the same set of parameters.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Describes the image to generate, or the edit to apply to the reference images. Up to 20000 characters. Default: `""` (empty). At least 1 character is required after removing surrounding whitespace.| STRING| Yes| 1 to 20000 characters  
`aspect_ratio`| Aspect ratio of the generated image, also applied when reference images are connected. Default: `"1:1"`. `"auto"` lets the model choose the ratio for text to image (rendered at the 1.5K size) and keeps the aspect ratio of the first reference image when editing.| COMBO| Yes| `"1:1"`  
`"16:9"`  
`"9:16"`  
`"3:2"`  
`"2:3"`  
`"4:3"`  
`"3:4"`  
`"auto"`  
`resolution`| Output size tier. 1K is about 1 megapixel (1:1 is 1024x1024, 16:9 is 1360x768); 1.5K is about 2.3 megapixels (1:1 is 1536x1536, 16:9 is 2048x1152). Default: `"1K"`. Ignored when `aspect_ratio` is `"auto"`.| COMBO| Yes| `"1K"`  
`"1.5K"`  
`seed`| Seed to determine if the node should re-run; the API has no seed, so actual results are nondeterministic regardless of this value. Default: `42`.| INT| Yes| 0 to 2147483647  
  
### 

​

Reference Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image_1` … `image_5`| Growable slot: connect 1 to 5 reference images for image-guided editing; a batched input counts once per image. Slots are optional and can be left empty (minimum 0 connected).| IMAGE| No| 0 to 5 images  
  
**Notes:**

  * A maximum of 5 reference images is supported in total across all connected slots; a batched input counts once per image.
  * The `prompt` must contain at least 1 character after surrounding whitespace is removed, and cannot exceed 20000 characters.
  * Reference images are sent as PNG data and are limited to a total of 2048 x 2048 pixels.
  * The `aspect_ratio` setting is applied to the output even when reference images are connected.
  * When `aspect_ratio` is `"auto"`, the `resolution` setting is ignored. With no reference images the model picks the ratio for text to image and renders at the 1.5K size; with reference images connected the aspect ratio of the first reference image is kept.
  * The seed value does not affect the API result; it only determines whether the node re-runs.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| The generated or edited image. If the service returns several images, they are combined into a single batched IMAGE output. An error is raised if no image is returned or if a returned image cannot be decoded.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenRouterImageNode/en.md)

* * *

**Source fingerprint (SHA-256):** `d201c18deccd2523041a24427996f51127ca201dfe10fad60c6f768ab79bf852`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/OpenRouterImageNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/OpenRouterImageNode)

[OpenAIGPTImageNodeV2 - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/OpenAIGPTImageNodeV2)[QuiverImageToSVGNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/QuiverImageToSVGNode)

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
