---
url: https://docs.comfy.org/built-in-nodes/SamplerLCM/
title: SamplerLCM - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:57.103255+00:00
---

# SamplerLCM - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SamplerLCM/

Samplers

# SamplerLCM - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node provides an LCM (Latent Consistency Model) sampler with adjustable per-step noise.

Copy pageCopy page

This node provides an LCM (Latent Consistency Model) sampler with adjustable per-step noise. It lets you control how much noise is applied during sampling: `s_noise` acts as a multiplier on the model’s training noise scale, and the noise level can vary from the first step to the last step. The configured sampler can then be plugged into a sampling workflow.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`s_noise`| Per-step noise multiplier at the first step (1.0 = match training). Default: 1.0.| FLOAT| Yes| 0.0 to 64.0 (step: 0.01)  
`s_noise_end`| Per-step noise multiplier at the last step. Set equal to `s_noise` for a constant schedule. Default: 1.0.| FLOAT| Yes| 0.0 to 64.0 (step: 0.01)  
`noise_clip_std`| Clamp per-step noise to +/- N*std. 0 disables. Default: 0.0.| FLOAT| Yes| 0.0 to 10.0 (step: 0.01)  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`SAMPLER`| The configured LCM sampler object, ready to be used in a sampling workflow.| SAMPLER  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCM/en.md)

* * *

**Source fingerprint (SHA-256):** `0d18f2f977ddadeedcd7807233b48ebcc4e94c6213f8540b9037a45a9c70c6cf`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SamplerLCM.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SamplerLCM)

[SamplerEulerAncestralCFGPP - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SamplerEulerAncestralCFGPP)[SamplerLCMUpscale - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SamplerLCMUpscale)

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
