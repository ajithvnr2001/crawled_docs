---
url: https://docs.comfy.org/built-in-nodes/SamplerER_SDE/
title: SamplerER_SDE - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:56.521533+00:00
---

# SamplerER_SDE - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SamplerER_SDE/

Samplers

# SamplerER_SDE - ComfyUI Built-in Node Documentation

Copy pageCopy page

The SamplerERSDE node provides specialized sampling methods for diffusion models, offering different solver types: ER-SDE, Reverse-time SDE, and ODE.

Copy pageCopy page

The SamplerER_SDE node provides specialized sampling methods for diffusion models, offering different solver types: ER-SDE, Reverse-time SDE, and ODE. It lets you control the stochastic behavior and the number of computational stages of the sampling process. The node automatically adjusts settings based on the chosen solver type to keep the sampler working correctly.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`solver_type`| The type of solver to use for sampling. Determines the mathematical approach for the diffusion process (default: “ER-SDE”).| COMBO| Yes| ”ER-SDE"  
"Reverse-time SDE"  
"ODE”  
`max_stage`| The maximum number of stages for the sampling process (default: 3). Controls the computational complexity and quality. This is an advanced parameter.| INT| Yes| 1-3  
`eta`| Stochastic strength of SDEs.  
When eta=0, they reduce to deterministic ODE.  
Large eta may cause invalid outputs. If this occurs, try decreasing this value. (default: 1.0). This is an advanced parameter.| FLOAT| Yes| 0.0-10.0 (step: 0.01)  
`s_noise`| Noise scaling factor for the sampling process (default: 1.0). Controls the amount of noise applied during sampling. This is an advanced parameter.| FLOAT| Yes| 0.0-100.0 (step: 0.01)  
  
**Parameter Constraints:**

  * When `solver_type` is set to “ODE” or when `eta` is 0, the node switches to ODE mode and sets `s_noise` to 0.0, regardless of the value entered for `s_noise`.
  * The `eta` parameter controls the stochastic strength of both the “ER-SDE” and “Reverse-time SDE” solver types. It has no effect when the solver runs in ODE mode.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`sampler`| A configured sampler object that can be used in the sampling pipeline with the specified solver settings.| SAMPLER  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerER_SDE/en.md)

* * *

**Source fingerprint (SHA-256):** `5299ae9b45444cdc7c36bcb3c5e5a0600f9f904e57ae614554033434afdffd30`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SamplerER_SDE.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SamplerER_SDE)

[SamplerDPMPP_SDE - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SamplerDPMPP_SDE)[SamplerEulerAncestral - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SamplerEulerAncestral)

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
