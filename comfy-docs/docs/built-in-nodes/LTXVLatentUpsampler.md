---
url: https://docs.comfy.org/built-in-nodes/LTXVLatentUpsampler/
title: LTXVLatentUpsampler - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:18.743279+00:00
---

# LTXVLatentUpsampler - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LTXVLatentUpsampler/

Ltxv

# LTXVLatentUpsampler - ComfyUI Built-in Node Documentation

Copy pageCopy page

The LTXVLatentUpsampler node increases the spatial resolution of a video latent representation by a factor of two.

Copy pageCopy page

The LTXVLatentUpsampler node increases the spatial resolution of a video latent representation by a factor of two. It uses a dedicated upscale model to process the latent data, which is first un-normalized and then re-normalized using the provided VAE’s channel statistics. This node is designed for video workflows within the latent space.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`samples`| The input latent representation of the video to be upscaled.| LATENT| Yes|   
`upscale_model`| The loaded model used to perform the 2x upscaling on the latent data.| LATENT_UPSCALE_MODEL| Yes|   
`vae`| The VAE model used to un-normalize the input latents before upscaling and to normalize the output latents afterwards.| VAE| Yes|   
  
Note: This node is marked as experimental in ComfyUI.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`LATENT`| The upscaled latent representation, with spatial dimensions doubled compared to the input. The output latent has the same batch size, number of channels, and temporal length as the input. The `noise_mask` from the input, if present, is removed from the output.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVLatentUpsampler/en.md)

* * *

**Source fingerprint (SHA-256):** `7d7f0b733cb3758e9ec985cac30134d719b130b5b86c35bfdd14576a5b4575db`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LTXVLatentUpsampler.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LTXVLatentUpsampler)

[LTXVFreezeLatent - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LTXVFreezeLatent)[LTXVSeparateAVLatent - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LTXVSeparateAVLatent)

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
