---
url: https://docs.comfy.org/built-in-nodes/HunyuanVideo15LatentUpscaleWithModel/
title: HunyuanVideo15LatentUpscaleWithModel - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:05.884448+00:00
---

# HunyuanVideo15LatentUpscaleWithModel - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/HunyuanVideo15LatentUpscaleWithModel/

Hunyuan Video

# HunyuanVideo15LatentUpscaleWithModel - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Hunyuan Video 15 Latent Upscale With Model node increases the resolution of a latent image representation.

Copy pageCopy page

The Hunyuan Video 15 Latent Upscale With Model node increases the resolution of a latent image representation. It first upscales the latent samples to a specified size using a chosen interpolation method, then refines the upscaled result using a specialized Hunyuan Video 1.5 upscale model to improve quality.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The Hunyuan Video 1.5 latent upscale model used to refine the upscaled samples.| LATENT_UPSCALE_MODEL| Yes| N/A  
`samples`| The latent image representation to be upscaled.| LATENT| Yes| N/A  
`upscale_method`| The interpolation algorithm used for the initial upscaling step (default: `"bilinear"`).| COMBO| Yes| `"nearest-exact"`  
`"bilinear"`  
`"area"`  
`"bicubic"`  
`"bislerp"`  
`width`| The target width for the upscaled latent, in pixels. A value of 0 will calculate the width automatically based on the target height and the original aspect ratio. The final output width will be a multiple of 16 (default: 1280).| INT| Yes| 0 to 16384 (step: 8)  
`height`| The target height for the upscaled latent, in pixels. A value of 0 will calculate the height automatically based on the target width and the original aspect ratio. The final output height will be a multiple of 16 (default: 720).| INT| Yes| 0 to 16384 (step: 8)  
`crop`| Determines how the upscaled latent is cropped to fit the target dimensions.| COMBO| Yes| `"disabled"`  
`"center"`  
  
**Note on Dimensions:** If both `width` and `height` are set to 0, the node returns the input `samples` unchanged. If only one dimension is set to 0, the other dimension is calculated to preserve the original aspect ratio. Both values are clamped to a minimum of 64, and the upscale target passed to the interpolation step is `width // 16` by `height // 16`, so the requested dimensions are effectively rounded down to multiples of 16.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`LATENT`| The upscaled and model-refined latent image representation, returned as a float tensor on the CPU.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15LatentUpscaleWithModel/en.md)

* * *

**Source fingerprint (SHA-256):** `71af49eefb010aadd30f8699b751ad901b1ee385d6cbeedd3a83995a1a623516`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/HunyuanVideo15LatentUpscaleWithModel.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/HunyuanVideo15LatentUpscaleWithModel)

[EmptyHunyuanVideo15Latent - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/EmptyHunyuanVideo15Latent)[EmptyLTXVLatentVideo - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/EmptyLTXVLatentVideo)

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
