---
url: https://docs.comfy.org/built-in-nodes/ByteDanceSeedreamNode/
title: ByteDanceSeedreamNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:28.576263+00:00
---

# ByteDanceSeedreamNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ByteDanceSeedreamNode/

Bytedance

# ByteDanceSeedreamNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ByteDance Seedream 4.5 & 5.0 node provides unified text-to-image generation and precise single-sentence editing capabilities at up to 4K resolution.

Copy pageCopy page

The ByteDance Seedream 4.5 & 5.0 node provides unified text-to-image generation and precise single-sentence editing capabilities at up to 4K resolution. It can create new images from text prompts or edit existing images using text instructions. The node supports both single image generation and sequential generation of multiple related images. **Note:** This node is marked as deprecated in the source code.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The Seedream model to use for generation.| STRING| Yes| ”seedream 5.0 pro"  
"seedream 5.0 lite"  
"seedream-4-5-251128"  
"seedream-4-0-250828”  
`prompt`| Text prompt for creating or editing an image. Must be at least 1 character long.| STRING| Yes| -  
`image`| Input image(s) for image-to-image generation. Reference image(s) for single or multi-reference generation. Maximum of 14 reference images for seedream-5-0-260128, or 10 for other models.| IMAGE| No| -  
`size_preset`| Pick a recommended size. Select Custom to use the width and height below.| STRING| No| Multiple options available  
`width`| Custom width for image. Value is working only if `size_preset` is set to `Custom`. Default: 2048.| INT| No| 1024 to 6240 (step 2)  
`height`| Custom height for image. Value is working only if `size_preset` is set to `Custom`. Default: 2048.| INT| No| 1024 to 4992 (step 2)  
`sequential_image_generation`| Group image generation mode. “disabled” generates a single image. “auto” lets the model decide whether to generate multiple related images (e.g., story scenes, character variations). Default: “disabled”.| STRING| No| ”disabled"  
"auto”  
`max_images`| Maximum number of images to generate when sequential_image_generation=‘auto’. Total images (input + generated) cannot exceed 15. Default: 1.| INT| No| 1 to 15 (step 1)  
`seed`| Seed to use for generation. Default: 0.| INT| No| 0 to 2147483647 (step 1)  
`watermark`| Whether to add an “AI generated” watermark to the image. Default: False.| BOOLEAN| No| -  
`fail_on_partial`| If enabled, abort execution if any requested images are missing or return an error. Default: True.| BOOLEAN| No| -  
  
**Notes on parameter constraints:**

  * The minimum image resolution depends on the selected model: 3.68MP for seedream-4-5 and seedream-5-0 models, 0.92MP for seedream-4-0 models.
  * The maximum image resolution is 10.4MP for seedream-5-0 models and 16.78MP for other models.
  * Reference images must have an aspect ratio between 1:3 and 3:1.
  * When `sequential_image_generation` is set to “auto”, the total number of input images plus `max_images` cannot exceed 15.
  * The `width` and `height` parameters are only used when `size_preset` is set to “Custom”.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| Generated image(s) based on the input parameters and prompt. Returns a single image tensor or a batch of image tensors if multiple images are generated.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNode/en.md)

* * *

**Source fingerprint (SHA-256):** `78086df431c887c241796ddb5db1ebbfe5b57faab0839da842be81480f1e113b`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ByteDanceSeedreamNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ByteDanceSeedreamNode)

[ByteDanceSeedreamLayerSeparationNodeV2 - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ByteDanceSeedreamLayerSeparationNodeV2)[ByteDanceSeedreamNodeV2 - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ByteDanceSeedreamNodeV2)

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
