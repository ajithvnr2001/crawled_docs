---
url: https://docs.comfy.org/built-in-nodes/SamplerSASolver/
title: SamplerSASolver - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:58.176035+00:00
---

# SamplerSASolver - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SamplerSASolver/

Samplers

# SamplerSASolver - ComfyUI Built-in Node Documentation

Copy pageCopy page

The SamplerSASolver node creates and configures a custom sampler for diffusion models.

Copy pageCopy page

The SamplerSASolver node creates and configures a custom sampler for diffusion models. It uses the “sa_solver” sampling algorithm with a configurable predictor-corrector scheme and stochastic differential equation (SDE) settings, returning a sampler object that can be plugged into a sampling node. The `sde_start_percent` and `sde_end_percent` values are converted into sigma values using the connected model’s sampling schedule to define the interval in which the stochastic component is applied.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The diffusion model whose sampling schedule is used to build the sampler| MODEL| Yes| -  
`eta`| Controls the step size scaling factor of the SDE solver (default: 1.0)| FLOAT| No| 0.0 - 10.0  
`sde_start_percent`| Starting percentage of the sampling process where the stochastic (SDE) component begins; converted to a sigma value using the model’s schedule (default: 0.2)| FLOAT| No| 0.0 - 1.0  
`sde_end_percent`| Ending percentage of the sampling process where the stochastic (SDE) component stops; converted to a sigma value using the model’s schedule (default: 0.8)| FLOAT| No| 0.0 - 1.0  
`s_noise`| Controls the amount of noise added during sampling (default: 1.0)| FLOAT| No| 0.0 - 100.0  
`predictor_order`| The order of the predictor component in the solver (default: 3)| INT| No| 1 - 6  
`corrector_order`| The order of the corrector component in the solver (default: 4)| INT| No| 0 - 6  
`use_pece`| Enables the PECE (Predict-Evaluate-Correct-Evaluate) method (default: disabled)| BOOLEAN| No| -  
`simple_order_2`| Enables simplified second-order calculations (default: disabled)| BOOLEAN| No| -  
  
All optional inputs are marked as advanced in the interface.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`sampler`| A configured sampler object (using the `sa_solver` algorithm) that can be used by sampling nodes| SAMPLER  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSASolver/en.md)

* * *

**Source fingerprint (SHA-256):** `31da2d436665bf533c28b32248f632edab8f6d92372402904702ae954230f98d`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SamplerSASolver.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SamplerSASolver)

[SamplerLMS - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SamplerLMS)[SamplerSEEDS2 - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SamplerSEEDS2)

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
