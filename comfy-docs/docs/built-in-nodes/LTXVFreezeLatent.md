---
url: https://docs.comfy.org/built-in-nodes/LTXVFreezeLatent/
title: LTXVFreezeLatent - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:18.072737+00:00
---

# LTXVFreezeLatent - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LTXVFreezeLatent/

Ltxv

# LTXVFreezeLatent - ComfyUI Built-in Node Documentation

Copy pageCopy page

The LTXV Freeze Latent node sets the noise mask of a latent to zero, which keeps that latent clean and unchanged while sampling runs.

Copy pageCopy page

The LTXV Freeze Latent node sets the noise mask of a latent to zero, which keeps that latent clean and unchanged while sampling runs. It works on both video and audio latents, so a latent can be frozen before it is concatenated with others or when it should not be denoised at all.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`latent`| Video or audio latent to freeze. Audio is 4D; video is 5D.| LATENT| Yes| N/A  
  
### 

​

Constraints

  * The latent must contain a plain tensor. A concatenated audio-video latent is not accepted; it must be split with the Separate AV Latent node first.
  * Only 4D latents (audio) and 5D latents (video) are supported. Any other shape causes an error.
  * The generated noise mask is created with zeros using the same device as the input tensor. For video latents the mask has shape (batch, 1, frames, 1, 1); for audio latents it has shape (batch, 1, frames, 1).



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`latent`| The input latent with an added noise mask of zeros, so it remains clean during sampling.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVFreezeLatent/en.md)

* * *

**Source fingerprint (SHA-256):** `d5d228687f0a124644323c0448dcce53ed6eb2224d3f44d1756079b2a71539ca`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LTXVFreezeLatent.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LTXVFreezeLatent)

[LTXVEmptyLatentAudio - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LTXVEmptyLatentAudio)[LTXVLatentUpsampler - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LTXVLatentUpsampler)

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
