---
url: https://docs.comfy.org/built-in-nodes/SamplerSEEDS2/
title: SamplerSEEDS2 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:57.487764+00:00
---

# SamplerSEEDS2 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SamplerSEEDS2/

Samplers

# SamplerSEEDS2 - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node provides a configurable sampler for image generation.

Copy pageCopy page

This node provides a configurable sampler for image generation. It is based on a stochastic differential equation (SDE) solver and can behave like several specific samplers depending on its settings, including `seeds_2`, `exp_heun_2_x0`, and `exp_heun_2_x0_sde`.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`solver_type`| Selects the underlying solver algorithm for the sampler.| COMBO| Yes| ”phi_1"  
"phi_2”  
`eta`| Stochastic strength (default: 1.0).| FLOAT| No| 0.0 - 100.0  
`s_noise`| SDE noise multiplier (default: 1.0).| FLOAT| No| 0.0 - 100.0  
`r`| Relative step size for the intermediate stage (c2 node) (default: 0.5).| FLOAT| No| 0.01 - 1.0  
  
**Note:** The node description defines the following sampler presets:

  * `seeds_2`: default settings
  * `exp_heun_2_x0`: `solver_type` = “phi_2”, `r` = 1.0, `eta` = 0.0
  * `exp_heun_2_x0_sde`: `solver_type` = “phi_2”, `r` = 1.0, `eta` = 1.0, `s_noise` = 1.0



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`sampler`| A configured sampler object that can be passed to other sampling nodes.| SAMPLER  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSEEDS2/en.md)

* * *

**Source fingerprint (SHA-256):** `f48744a706a49ef93d41845bf8c308af971853f6150afd00ded45f0317ffc4f9`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SamplerSEEDS2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SamplerSEEDS2)

[SamplerSASolver - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SamplerSASolver)[VOIDSampler - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/VOIDSampler)

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
