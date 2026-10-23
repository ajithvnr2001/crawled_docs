---
url: https://docs.comfy.org/built-in-nodes/RecraftV4TextToImageNode/
title: RecraftV4TextToImageNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:48.879953+00:00
---

# RecraftV4TextToImageNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/RecraftV4TextToImageNode/

Recraft

# RecraftV4TextToImageNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generates images from text prompts using Recraft V4 and V4.1 models.

Copy pageCopy page

Generates images from text prompts using Recraft V4 and V4.1 models. It sends the prompt and selected settings to the Recraft API and returns the generated image or images. If style reference images are used, the created style ID is also returned.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The model to use for generation. The recraftv4_styles models are built for style-consistent generation and always require a style_id or style_references. `recraftv4_1_flash` is the fastest and cheapest model and supports no styles at all.| DYNAMIC_COMBO| Yes| ”recraftv4_1"  
"recraftv4_1_flash"  
"recraftv4_1_utility"  
"recraftv4_1_pro"  
"recraftv4_1_utility_pro"  
"recraftv4"  
"recraftv4_pro"  
"recraftv4_styles"  
"recraftv4_styles_pro”  
`prompt`| Prompt for the image generation. Maximum 10,000 characters.| STRING| Yes| 1 to 10000 characters  
`negative_prompt`| This input is ignored: negative prompt is not supported by Recraft V4 and V4.1 models.| STRING| Yes| N/A  
`n`| The number of images to generate (default: 1).| INT| Yes| 1 to 6  
`seed`| Seed to determine if node should re-run; actual results are nondeterministic regardless of seed (default: 0).| INT| Yes| 0 to 18446744073709551615  
`recraft_controls`| Optional additional controls over the generation via the Recraft Controls node.| CUSTOM| No| N/A  
`style_id`| UUID of a Recraft V4 style to apply, e.g. from the Recraft V4 Create Style node or the style_id output of a previous run. Cannot be combined with style_references (default: empty).| STRING| No| Valid UUID string  
`style_match`| How closely to follow the style: precise reproduces it in detail, flexible matches the general look. Only used when a style is provided (default: “precise”).| COMBO| No| ”precise"  
"flexible”  
  
### 

​

recraftv4_1, recraftv4_1_flash, recraftv4_1_utility, recraftv4, and recraftv4_styles Inputs

These models share the same `size` parameter.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`size`| The size of the generated image (default: “1024x1024”).| COMBO| Yes| Multiple options available (standard Recraft V4 sizes; includes “1024x1024”)  
  
### 

​

recraftv4_1_pro, recraftv4_1_utility_pro, recraftv4_pro, and recraftv4_styles_pro Inputs

These models share the same `size` parameter.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`size`| The size of the generated image (default: “2048x2048”).| COMBO| Yes| Multiple options available (pro Recraft V4 sizes; includes “2048x2048”)  
  
### 

​

Reference Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`style_references`| Reference images to create a style from on the fly, billed on top of the generation. The created style is returned as style_id for reuse. Cannot be combined with style_id. Growable slot: connect 1..N images (style_reference_1, style_reference_2, …).| IMAGE| No| 0 to the maximum number of reference images allowed by the Recraft API; total encoded size must not exceed 10 MB  
  
**Note:** The `size` parameter is a dynamic input whose available options change based on the selected `model`. The `recraftv4_styles` and `recraftv4_styles_pro` models always require a style: connect style reference images or provide a `style_id`. The `style_id` and `style_references` inputs are mutually exclusive — provide only one of them. A `style_id` must be a valid UUID. The `style_match` input is only used when a style is provided. Style reference images are billed on top of the generation and their total encoded size must not exceed 10 MB. The `seed` value does not guarantee reproducible image outputs. If you use a style ID from the Infinite Style Library, make sure it is not a Vector art style, as this may return SVG data instead of an image.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated image or batch of images.| IMAGE  
`style_id`| The style ID used or created by this generation. When style reference images are provided, the created style is returned here for reuse; empty string when no style is used.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToImageNode/en.md)

* * *

**Source fingerprint (SHA-256):** `690286e663f27b525e58f81a7f883e490dacd48c1a34ee7b8e9ad4efd9935ff1`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/RecraftV4TextToImageNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/RecraftV4TextToImageNode)

[RecraftV4CreateStyleNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/RecraftV4CreateStyleNode)[RecraftV4TextToVectorNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/RecraftV4TextToVectorNode)

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
