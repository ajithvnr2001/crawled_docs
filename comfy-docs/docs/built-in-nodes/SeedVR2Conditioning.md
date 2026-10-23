---
url: https://docs.comfy.org/built-in-nodes/SeedVR2Conditioning/
title: SeedVR2Conditioning - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:00.370337+00:00
---

# SeedVR2Conditioning - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SeedVR2Conditioning/

Conditioning

# SeedVR2Conditioning - ComfyUI Built-in Node Documentation

Copy pageCopy page

Builds positive and negative conditioning from a VAE latent for use with the SeedVR2 model.

Copy pageCopy page

Builds positive and negative conditioning from a VAE latent for use with the SeedVR2 model. It validates the input latent and model structure, adds a mask channel to the latent, and returns both conditioning outputs.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The SeedVR2 model.| MODEL| Yes| -  
`vae_conditioning`| The SeedVR2 VAE latent to build conditioning from (display name: latent).| LATENT| Yes| -  
  
Note: The `vae_conditioning` latent must be a 5-D tensor in Comfy channel-first layout (B, C, T, H, W), where C is the expected SeedVR2 VAE channel count. The node raises an error if the latent is not 5-D, if the channel count does not match, or if the tensor appears to be in channel-last layout. The `model` input must have the expected SeedVR2 structure; the node resolves its inner diffusion model and reads its positive and negative conditioning. Internally, the node appends a constant mask channel to the latent and attaches the resulting condition to both the positive and negative conditioning outputs.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| The positive conditioning for sampling.| CONDITIONING  
`negative`| The negative conditioning for sampling.| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Conditioning/en.md)

* * *

**Source fingerprint (SHA-256):** `28e508bdd776e2e3f5f2f93bfc29a1a1d1c34a11dbdc7f421d197ddbfa85f0f5`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SeedVR2Conditioning.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SeedVR2Conditioning)

[SaveConditioning - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SaveConditioning)[StyleModelApply - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/StyleModelApply)

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
