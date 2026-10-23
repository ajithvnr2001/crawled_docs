---
url: https://docs.comfy.org/built-in-nodes/StableCascade_SuperResolutionControlnet/
title: StableCascade_SuperResolutionControlnet - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:05.052151+00:00
---

# StableCascade_SuperResolutionControlnet - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/StableCascade_SuperResolutionControlnet/

Stable Cascade

# StableCascade_SuperResolutionControlnet - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node is part of the experimental Stable Cascade group.

Copy pageCopy page

This node is part of the experimental Stable Cascade group. It prepares inputs for Stable Cascade super-resolution processing by encoding an input image with a VAE to create a controlnet input, and by generating empty (zero-filled) latent placeholders for stage C and stage B of the Stable Cascade pipeline.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The input image to be processed for super-resolution. Only the first 3 color channels (RGB) of the image are used for encoding.| IMAGE| Yes| -  
`vae`| The VAE model used to encode the input image| VAE| Yes| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`controlnet_input`| The VAE-encoded image representation suitable for controlnet input| IMAGE  
`stage_c`| Placeholder (zero-filled) latent representation for stage C of Stable Cascade processing, with 16 channels and dimensions based on the input image size divided by 16| LATENT  
`stage_b`| Placeholder (zero-filled) latent representation for stage B of Stable Cascade processing, with 4 channels and dimensions based on the input image size divided by 2| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_SuperResolutionControlnet/en.md)

* * *

**Source fingerprint (SHA-256):** `d9eff373ac7736f2e2f9788d1b43c04bb3212422aa1703d1d58ac512ce476925`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/StableCascade_SuperResolutionControlnet.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/StableCascade_SuperResolutionControlnet)

[UNetTemporalAttentionMultiply - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/UNetTemporalAttentionMultiply)[DifferentialDiffusion - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/DifferentialDiffusion)

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
