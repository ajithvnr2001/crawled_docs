---
url: https://docs.comfy.org/built-in-nodes/ByteDanceSeedreamNodeV2/
title: ByteDanceSeedreamNodeV2 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:30.653444+00:00
---

# ByteDanceSeedreamNodeV2 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ByteDanceSeedreamNodeV2/

Bytedance

# ByteDanceSeedreamNodeV2 - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node generates or edits images using ByteDance’s Seedream models (versions 4.0, 4.5, 5.0 Lite, and 5.0 Pro).

Copy pageCopy page

This node generates or edits images using ByteDance’s Seedream models (versions 4.0, 4.5, 5.0 Lite, and 5.0 Pro). It provides unified text-to-image generation and precise single-sentence image editing at up to 4K resolution. This is the legacy (V2) version of the Seedream node.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The Seedream model version to use for generation. Each model has different capabilities and pricing.| DYNAMIC_COMBO| Yes| `"seedream 5.0 pro"`  
`"seedream 5.0 lite"`  
`"seedream-4-5-251128"`  
`"seedream-4-0-250828"`  
`prompt`| Text prompt for creating or editing an image (default: empty string).| STRING| Yes| N/A  
`seed`| Seed to use for generation (default: 0).| INT| Yes| 0 to 2147483647  
`watermark`| Whether to add an “AI generated” watermark to the image (default: False).| BOOLEAN| Yes| True / False  
`thinking`| Enable the model’s prompt-optimization reasoning (‘thinking’) for better adherence. Can substantially increase generation time — notably on Seedream 5.0 Pro. Can only be disabled for text-to-image (not when reference images are provided) (default: True).| BOOLEAN| No| True / False  
  
### 

​

`seedream 5.0 pro` Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`size_preset`| Pick a recommended size. Select Custom to use the width and height below.| COMBO| Yes| Multiple model-specific presets available, includes `Custom`  
`width`| Custom width for image. Value is working only if `size_preset` is set to `Custom` (default: 2048).| INT| Yes| 1024 to 3136 (step 2)  
`height`| Custom height for image. Value is working only if `size_preset` is set to `Custom` (default: 2048).| INT| Yes| 1024 to 2496 (step 2)  
  
### 

​

`seedream 5.0 lite` Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`size_preset`| Pick a recommended size. Select Custom to use the width and height below.| COMBO| Yes| Multiple model-specific presets available, includes `Custom`  
`width`| Custom width for image. Value is working only if `size_preset` is set to `Custom` (default: 2048).| INT| Yes| 1024 to 6240 (step 2)  
`height`| Custom height for image. Value is working only if `size_preset` is set to `Custom` (default: 2048).| INT| Yes| 1024 to 4992 (step 2)  
`max_images`| Maximum number of images to generate. With 1, exactly one image is produced. With >1, the model generates between 1 and max_images related images (e.g., story scenes, character variations). Total images (input + generated) cannot exceed 15. (default: 1)| INT| Yes| 1 to 14  
`fail_on_partial`| If enabled, abort execution if any requested images are missing or return an error. (default: False)| BOOLEAN| Yes| True / False  
  
### 

​

`seedream-4-5-251128` Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`size_preset`| Pick a recommended size. Select Custom to use the width and height below.| COMBO| Yes| Multiple model-specific presets available, includes `Custom`  
`width`| Custom width for image. Value is working only if `size_preset` is set to `Custom` (default: 2048).| INT| Yes| 1024 to 6240 (step 2)  
`height`| Custom height for image. Value is working only if `size_preset` is set to `Custom` (default: 2048).| INT| Yes| 1024 to 4992 (step 2)  
`max_images`| Maximum number of images to generate. With 1, exactly one image is produced. With >1, the model generates between 1 and max_images related images (e.g., story scenes, character variations). Total images (input + generated) cannot exceed 15. (default: 1)| INT| Yes| 1 to 10  
`fail_on_partial`| If enabled, abort execution if any requested images are missing or return an error. (default: False)| BOOLEAN| Yes| True / False  
  
### 

​

`seedream-4-0-250828` Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`size_preset`| Pick a recommended size. Select Custom to use the width and height below.| COMBO| Yes| Multiple model-specific presets available, includes `Custom`  
`width`| Custom width for image. Value is working only if `size_preset` is set to `Custom` (default: 2048).| INT| Yes| 1024 to 6240 (step 2)  
`height`| Custom height for image. Value is working only if `size_preset` is set to `Custom` (default: 2048).| INT| Yes| 1024 to 4992 (step 2)  
`max_images`| Maximum number of images to generate. With 1, exactly one image is produced. With >1, the model generates between 1 and max_images related images (e.g., story scenes, character variations). Total images (input + generated) cannot exceed 15. (default: 1)| INT| Yes| 1 to 10  
`fail_on_partial`| If enabled, abort execution if any requested images are missing or return an error. (default: False)| BOOLEAN| Yes| True / False  
  
### 

​

Reference Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`images`| Growable slot: connect 1..N items (e.g. `image_1`, `image_2`, …); the count limit depends on the selected model (see model sections). Optional reference image(s) for image-to-image or multi-reference generation. With no reference images, the node works in text-to-image mode.| IMAGE| No| 0 to 10 images (`seedream 5.0 pro`, `seedream-4-5-251128`, `seedream-4-0-250828`)  
0 to 14 images (`seedream 5.0 lite`)  
  
### 

​

Notes on constraints

  * `width` and `height` only take effect when `size_preset` is set to `Custom`.
  * The total number of reference images plus generated images cannot exceed 15.
  * `thinking` can only be disabled for text-to-image generation, not when reference images are provided.
  * Seedream 5.0 Pro does not support batch generation: it always produces a single image, so `max_images` and `fail_on_partial` are not available for this model.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The generated or edited image as a tensor. If multiple images were requested, they are concatenated into a single batch.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNodeV2/en.md)

* * *

**Source fingerprint (SHA-256):** `f1a84171d94c602ec5417e43857ddf511ab1e54caa089b1928f740d3a38423f8`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ByteDanceSeedreamNodeV2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ByteDanceSeedreamNodeV2)

[ByteDanceSeedreamNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ByteDanceSeedreamNode)[ByteDanceSeedreamNodeV3 - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ByteDanceSeedreamNodeV3)

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
