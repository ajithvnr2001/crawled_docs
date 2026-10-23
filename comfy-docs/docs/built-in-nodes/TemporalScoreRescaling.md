---
url: https://docs.comfy.org/built-in-nodes/TemporalScoreRescaling/
title: TemporalScoreRescaling - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:07.779422+00:00
---

# TemporalScoreRescaling - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/TemporalScoreRescaling/

Unet

# TemporalScoreRescaling - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node applies Temporal Score Rescaling (TSR) to a diffusion model.

Copy pageCopy page

This node applies Temporal Score Rescaling (TSR) to a diffusion model. It patches the model so that, during sampling, the predicted score or noise is rescaled to steer the diversity of generated results. This is implemented as a post-CFG (Classifier-Free Guidance) function.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The diffusion model to be patched with the TSR function.| MODEL| Yes| -  
`tsr_k`| Controls the rescaling strength. Lower k produces more detailed results; higher k produces smoother results in image generation. Setting k = 1 disables rescaling. (default: 0.95)| FLOAT| Yes| 0.01 - 100.0  
`tsr_sigma`| Controls how early rescaling takes effect. Larger values take effect earlier. (default: 1.0)| FLOAT| Yes| 0.01 - 100.0  
  
Note: Rescaling is skipped when `tsr_k` is set to 1, when the sigma value is 0, or when the signal-to-noise ratio is 0.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`patched_model`| The input model, now patched with the Temporal Score Rescaling function applied to its sampling process.| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TemporalScoreRescaling/en.md)

* * *

**Source fingerprint (SHA-256):** `4d4e3c64fb6e3a3fe4725ea944a361b46d871943a10e65d72d70e0e6d757dfca`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/TemporalScoreRescaling.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/TemporalScoreRescaling)

[PerturbedAttentionGuidance - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/PerturbedAttentionGuidance)[TomePatchModel - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/TomePatchModel)

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
