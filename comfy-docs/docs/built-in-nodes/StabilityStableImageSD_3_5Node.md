---
url: https://docs.comfy.org/built-in-nodes/StabilityStableImageSD_3_5Node/
title: StabilityStableImageSD_3_5Node - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:04.644700+00:00
---

# StabilityStableImageSD_3_5Node - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/StabilityStableImageSD_3_5Node/

Advanced

# StabilityStableImageSD_3_5Node - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node generates images synchronously using Stability AI’s Stable Diffusion 3.5 model.

Copy pageCopy page

This node generates images synchronously using Stability AI’s Stable Diffusion 3.5 model. It creates images based on text prompts and can also modify existing images when provided as input. The node supports various aspect ratios and style presets to customize the output.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| What you wish to see in the output image. A strong, descriptive prompt that clearly defines elements, colors, and subjects will lead to better results. (default: empty string)| STRING| Yes| -  
`model`| The Stable Diffusion 3.5 model to use for generation.| COMBO| Yes| `sd3.5-large`  
`sd3.5-large-turbo`  
`sd3.5-medium`  
`aspect_ratio`| Aspect ratio of generated image. (default: 1:1)| COMBO| Yes| `16:9`  
`1:1`  
`21:9`  
`2:3`  
`3:2`  
`4:5`  
`5:4`  
`9:16`  
`9:21`  
`style_preset`| Optional desired style of generated image. Select “None” for no style preset.| COMBO| No| `3d-model`  
`analog-film`  
`anime`  
`cinematic`  
`comic-book`  
`digital-art`  
`enhance`  
`fantasy-art`  
`isometric`  
`line-art`  
`low-poly`  
`modeling-compound`  
`neon-punk`  
`origami`  
`photographic`  
`pixel-art`  
`tile-texture`  
`None`  
`cfg_scale`| How strictly the diffusion process adheres to the prompt text (higher values keep your image closer to your prompt). (default: 4.0)| FLOAT| Yes| 1.0 to 10.0  
`seed`| The random seed used for creating the noise. (default: 0)| INT| Yes| 0 to 4294967294  
`image`| Optional input image for image-to-image generation. When provided, the node switches to image-to-image mode and the `aspect_ratio` parameter is ignored.| IMAGE| No| -  
`negative_prompt`| Keywords of what you do not wish to see in the output image. This is an advanced feature. (default: empty string)| STRING| No| -  
`image_denoise`| Denoise of input image; 0.0 yields image identical to input, 1.0 is as if no image was provided at all. (default: 0.5) This parameter is only used when an `image` is provided.| FLOAT| No| 0.0 to 1.0  
  
**Note:** When an `image` is provided, the node switches to image-to-image generation mode and the `aspect_ratio` parameter is automatically determined from the input image. When no `image` is provided, the `image_denoise` parameter is ignored.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The generated or modified image.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityStableImageSD_3_5Node/en.md)

* * *

**Source fingerprint (SHA-256):** `0ef029d4651fb4a9132899a6df1a2c2de6152dd9091129573f366a2aac39bbae`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/StabilityStableImageSD_3_5Node.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/StabilityStableImageSD_3_5Node)

[StabilityAudioToAudio - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/StabilityAudioToAudio)[StabilityStableImageUltraNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/StabilityStableImageUltraNode)

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
