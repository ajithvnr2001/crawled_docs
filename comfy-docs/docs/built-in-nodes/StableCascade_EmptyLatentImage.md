---
url: https://docs.comfy.org/built-in-nodes/StableCascade_EmptyLatentImage/
title: StableCascade_EmptyLatentImage - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:05.000697+00:00
---

# StableCascade_EmptyLatentImage - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/StableCascade_EmptyLatentImage/

Stable Cascade

# StableCascade_EmptyLatentImage - ComfyUI Built-in Node Documentation

Copy pageCopy page

The StableCascadeEmptyLatentImage node creates empty latent tensors for Stable Cascade models.

Copy pageCopy page

The StableCascade_EmptyLatentImage node creates empty latent tensors for Stable Cascade models. It generates two separate latent representations - one for stage C and another for stage B - with dimensions calculated from the input resolution and compression settings. This node provides a starting point for the Stable Cascade generation pipeline.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`width`| The width of the output image in pixels (default: 1024, step: 8)| INT| Yes| 256 to MAX_RESOLUTION  
`height`| The height of the output image in pixels (default: 1024, step: 8)| INT| Yes| 256 to MAX_RESOLUTION  
`compression`| The compression factor that determines the latent dimensions for stage C (default: 42, step: 1). This is an advanced parameter.| INT| Yes| 4 to 128  
`batch_size`| The number of latent samples to generate in a batch (default: 1)| INT| Yes| 1 to 4096  
  
Note: The `compression` value controls the stage C latent size: its height and width are the input `height` and `width` divided by `compression`. The stage B latent always uses a fixed compression of 4.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`stage_c`| The stage C latent tensor with dimensions [batch_size, 16, height//compression, width//compression]| LATENT  
`stage_b`| The stage B latent tensor with dimensions [batch_size, 4, height//4, width//4]| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_EmptyLatentImage/en.md)

* * *

**Source fingerprint (SHA-256):** `f336f87d0ec14b3716efda2cfaa194b1f80707d64821bb56ade7d88d9bd5b53f`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/StableCascade_EmptyLatentImage.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/StableCascade_EmptyLatentImage)

[SeedVR2TemporalMerge - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SeedVR2TemporalMerge)[StableCascade_StageC_VAEEncode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/StableCascade_StageC_VAEEncode)

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
