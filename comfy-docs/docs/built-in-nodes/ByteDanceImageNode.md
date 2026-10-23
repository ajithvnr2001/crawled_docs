---
url: https://docs.comfy.org/built-in-nodes/ByteDanceImageNode/
title: ByteDanceImageNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-18T12:01:27.596429+00:00
---

# ByteDanceImageNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ByteDanceImageNode/

Advanced

# ByteDanceImageNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ByteDance Image node generates images using ByteDance models through an API based on text prompts.

Copy pageCopy page

The ByteDance Image node generates images using ByteDance models through an API based on text prompts. It allows you to select a model, specify image dimensions, and control various generation parameters like seed and guidance scale. The node connects to ByteDance’s image generation service and returns the created image.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The ByteDance model to use for image generation. Currently only one model option is available.| STRING| Yes| `"seedream-3-0-t2i-250415"`  
`prompt`| The text prompt used to generate the image. Must be at least 1 character long after stripping whitespace.| STRING| Yes| -  
`size_preset`| Pick a recommended size. Select Custom to use the width and height below. Available presets are defined by the `RECOMMENDED_PRESETS` list.| STRING| Yes| See description  
`width`| Custom width for the image. This value is only used when `size_preset` is set to `Custom`. Default: 1024.| INT| Yes| 512 to 2048 (step 64)  
`height`| Custom height for the image. This value is only used when `size_preset` is set to `Custom`. Default: 1024.| INT| Yes| 512 to 2048 (step 64)  
`seed`| Seed to use for generation. Default: 0.| INT| No| 0 to 2147483647 (step 1)  
`guidance_scale`| Higher value makes the image follow the prompt more closely. Default: 2.5.| FLOAT| No| 1.0 to 10.0 (step 0.01)  
`watermark`| Whether to add an “AI generated” watermark to the image. Default: False. This is an advanced parameter.| BOOLEAN| No| True / False  
  
**Note on size parameters:** The `width` and `height` parameters are only used when `size_preset` is set to `Custom`. If a preset size is selected, the preset’s dimensions override the custom width and height values. Both width and height must be between 512 and 2048 pixels when using custom dimensions.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| The generated image returned from the ByteDance API as a tensor.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageNode/en.md)

* * *

**Source fingerprint (SHA-256):** `0b40c75ca43ef3cccbc644e64822f701a0d772decacd813c58d7d5ac60c230a1`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ByteDanceImageNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ByteDanceImageNode)

[SelectVAEDevice - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SelectVAEDevice)[ByteDanceImageReferenceNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ByteDanceImageReferenceNode)

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
