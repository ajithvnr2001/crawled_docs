---
url: https://docs.comfy.org/built-in-nodes/StableCascade_StageC_VAEEncode/
title: StableCascade_StageC_VAEEncode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:05.443653+00:00
---

# StableCascade_StageC_VAEEncode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/StableCascade_StageC_VAEEncode/

Stable Cascade

# StableCascade_StageC_VAEEncode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The StableCascadeStageCVAEEncode node processes an input image through a VAE encoder to generate latent representations for the Stable Cascade model.

Copy pageCopy page

The StableCascade_StageC_VAEEncode node processes an input image through a VAE encoder to generate latent representations for the Stable Cascade model. It first resizes the image based on a compression factor and the VAE’s downscale ratio, then encodes the resized image. The node outputs two latent tensors: one for stage C (the actual encoded result) and one for stage B (a zero-filled placeholder).

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The input image to be encoded into latent space| IMAGE| Yes| -  
`vae`| The VAE model used for encoding the image| VAE| Yes| -  
`compression`| The compression factor applied to the image before encoding. The image dimensions are divided by this value, then multiplied by the VAE’s downscale ratio. This is an advanced parameter. (default: 42)| INT| Yes| 4-128 (step: 1)  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`stage_c`| The encoded latent representation for stage C of the Stable Cascade model| LATENT  
`stage_b`| A placeholder latent representation for stage B. Currently returns a zero-filled tensor with dimensions calculated from the input image size.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageC_VAEEncode/en.md)

* * *

**Source fingerprint (SHA-256):** `1679aaac77057fcc359e5428906d5227f6c2dde721aabbfb5a32c08738ac376c`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/StableCascade_StageC_VAEEncode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/StableCascade_StageC_VAEEncode)

[StableCascade_EmptyLatentImage - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/StableCascade_EmptyLatentImage)[EmptySD3LatentImage - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/EmptySD3LatentImage)

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
