---
url: https://docs.comfy.org/built-in-nodes/OpenAIGPTImageNodeV2/
title: OpenAIGPTImageNodeV2 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:39.364952+00:00
---

# OpenAIGPTImageNodeV2 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/OpenAIGPTImageNodeV2/

Openai

# OpenAIGPTImageNodeV2 - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node generates images using OpenAI’s GPT Image API.

Copy pageCopy page

This node generates images using OpenAI’s GPT Image API. It supports five models — `gpt-image-2.5-flare`, `gpt-image-2.5-sunburst`, `gpt-image-2`, `gpt-image-1.5`, and `gpt-image-1` — lets you attach reference images for image editing, and can use a mask to specify which parts of an image to replace.

## 

​

Inputs

### 

​

Common Inputs

These inputs are always visible.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The OpenAI GPT Image model to use. Selecting a model reveals additional parameters specific to that model.| DYNAMIC_COMBO| Yes| `"gpt-image-2.5-flare"`  
`"gpt-image-2.5-sunburst"`  
`"gpt-image-2"`  
`"gpt-image-1.5"`  
`"gpt-image-1"`  
`prompt`| Text prompt for GPT Image (default: `""`).| STRING| Yes| N/A  
`n`| How many images to generate (default: `1`).| INT| Yes| 1 to 8  
`seed`| Seed for reproducibility (default: `0`). Not implemented yet in backend.| INT| Yes| 0 to 2147483647  
  
### 

​

gpt-image-2.5-flare and gpt-image-2.5-sunburst Inputs

These inputs appear when `model` is set to `gpt-image-2.5-flare` or `gpt-image-2.5-sunburst`. Both models share the same parameter set.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model.size`| Image size. Select “Custom” to use the custom width and height (default: `"auto"`).| COMBO| Yes| `"auto"`  
`"1024x1024"`  
`"1024x1536"`  
`"1536x1024"`  
`"2048x2048"`  
`"2048x1152"`  
`"1152x2048"`  
`"3840x2160"`  
`"2160x3840"`  
`"Custom"`  
`model.custom_width`| Used only when `model.size` is “Custom”. Must be a multiple of 16 (default: `1024`).| INT| No| 480 to 3840 (step 16)  
`model.custom_height`| Used only when `model.size` is “Custom”. Must be a multiple of 16 (default: `1024`).| INT| No| 480 to 3840 (step 16)  
`model.background`| Return image with or without background (default: `"auto"`).| COMBO| Yes| `"auto"`  
`"opaque"`  
`"transparent"`  
`model.quality`| Image quality, affects cost and generation time (default: `"low"`).| COMBO| Yes| `"low"`  
`"medium"`  
`"high"`  
`"xhigh"`  
`"max"`  
`model.images`| Optional reference image(s) for image editing. Up to 16 images. See Reference Inputs for details.| IMAGE| No| 0 to 16  
`model.mask`| Optional mask for inpainting (white areas will be replaced). Requires exactly one reference image.| MASK| No| N/A  
  
### 

​

gpt-image-2 Inputs

These inputs appear when `model` is set to `gpt-image-2`.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model.size`| Image size. Select “Custom” to use the custom width and height (default: `"auto"`).| COMBO| Yes| `"auto"`  
`"1024x1024"`  
`"1024x1536"`  
`"1536x1024"`  
`"2048x2048"`  
`"2048x1152"`  
`"1152x2048"`  
`"3840x2160"`  
`"2160x3840"`  
`"Custom"`  
`model.custom_width`| Used only when `model.size` is “Custom”. Must be a multiple of 16 (default: `1024`).| INT| No| 480 to 3840 (step 16)  
`model.custom_height`| Used only when `model.size` is “Custom”. Must be a multiple of 16 (default: `1024`).| INT| No| 480 to 3840 (step 16)  
`model.background`| Return image with or without background (default: `"auto"`).| COMBO| Yes| `"auto"`  
`"opaque"`  
`model.quality`| Image quality, affects cost and generation time (default: `"low"`).| COMBO| Yes| `"low"`  
`"medium"`  
`"high"`  
`model.images`| Optional reference image(s) for image editing. Up to 16 images. See Reference Inputs for details.| IMAGE| No| 0 to 16  
`model.mask`| Optional mask for inpainting (white areas will be replaced). Requires exactly one reference image.| MASK| No| N/A  
  
### 

​

gpt-image-1.5 and gpt-image-1 Inputs

These inputs appear when `model` is set to `gpt-image-1.5` or `gpt-image-1`. Both models share the same parameter set.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model.size`| Image size (default: `"auto"`).| COMBO| Yes| `"auto"`  
`"1024x1024"`  
`"1024x1536"`  
`"1536x1024"`  
`model.background`| Return image with or without background (default: `"auto"`).| COMBO| Yes| `"auto"`  
`"opaque"`  
`"transparent"`  
`model.quality`| Image quality, affects cost and generation time (default: `"low"`).| COMBO| Yes| `"low"`  
`"medium"`  
`"high"`  
`model.images`| Optional reference image(s) for image editing. Up to 16 images. See Reference Inputs for details.| IMAGE| No| 0 to 16  
`model.mask`| Optional mask for inpainting (white areas will be replaced). Requires exactly one reference image.| MASK| No| N/A  
  
### 

​

Reference Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model.images`| Growable slot: connect 1..N items (e.g. `image_1`…`image_16`); up to 16 reference images for all models.| IMAGE| No| 0 to 16  
`model.mask`| Optional mask for inpainting (white areas will be replaced). Requires exactly one reference image.| MASK| No| N/A  
  
**Parameter Constraints and Limitations:**

  * When `model.size` is “Custom” (`gpt-image-2.5-flare`, `gpt-image-2.5-sunburst`, and `gpt-image-2` only), `model.custom_width` and `model.custom_height` must both be multiples of 16, the longest edge must not exceed 3840, the aspect ratio must not exceed 3:1, and the total pixel count must be between 655,360 and 8,294,400.
  * `model.mask` requires exactly one reference image in `model.images`: it cannot be used without an image, and it cannot be used with more than one image.
  * When `model.mask` is used, its height and width must match the height and width of the reference image.
  * When `model.images` is provided, the node runs in image editing mode; without `model.images`, it generates images from the prompt alone.
  * Reference images and the mask are downscaled before being sent to the API.
  * `"xhigh"` and `"max"` quality levels are only available for `gpt-image-2.5-flare` and `gpt-image-2.5-sunburst`.
  * `seed` is currently not implemented in the backend.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The generated image or images. All returned images are stacked into one batch; if their dimensions differ, they are resized to match the first image.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageNodeV2/en.md)

* * *

**Source fingerprint (SHA-256):** `9cf1a9fa3e2cd98aff6c42432164ac5e6c55b7bcdc9815043cb359c6968ac172`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/OpenAIGPTImageNodeV2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/OpenAIGPTImageNodeV2)

[OpenAIGPTImage1 - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/OpenAIGPTImage1)[OpenRouterImageNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/OpenRouterImageNode)

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
