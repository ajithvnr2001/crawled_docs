---
url: https://docs.comfy.org/built-in-nodes/SamplerDPMPP_2M_SDE/
title: SamplerDPMPP_2M_SDE - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:56.009961+00:00
---

# SamplerDPMPP_2M_SDE - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SamplerDPMPP_2M_SDE/

Samplers

# SamplerDPMPP_2M_SDE - ComfyUI Built-in Node Documentation

Copy pageCopy page

The SamplerDPMPP2MSDE node creates a DPM++ 2M SDE sampler for diffusion models.

Copy pageCopy page

The SamplerDPMPP_2M_SDE node creates a DPM++ 2M SDE sampler for diffusion models. This sampler uses second-order differential equation solvers with stochastic differential equations to generate samples. It provides different solver types and noise handling options to control the sampling process.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`solver_type`| The type of differential equation solver to use for the sampling process (default: “midpoint”)| COMBO| Yes| `"midpoint"`  
`"heun"`  
`eta`| Controls the stochasticity of the sampling process (default: 1.0)| FLOAT| Yes| 0.0 - 100.0  
`s_noise`| Controls the amount of noise added during sampling (default: 1.0)| FLOAT| Yes| 0.0 - 100.0  
`noise_device`| The device where noise calculations are performed. When set to “cpu”, the sampler uses CPU-based noise generation; when set to “gpu”, it uses GPU-based noise generation for potentially faster performance (default: “gpu”)| COMBO| Yes| `"gpu"`  
`"cpu"`  
  
Note: `eta`, `s_noise`, and `noise_device` are marked as advanced parameters and appear in the advanced section of the node’s UI.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`sampler`| A configured sampler object ready for use in the sampling pipeline| SAMPLER  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_2M_SDE/en.md)

* * *

**Source fingerprint (SHA-256):** `42f5f098fa7573ca8a1a6085b72675ee6cb0ae8e7865c5793a815a6ef2495f82`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SamplerDPMPP_2M_SDE.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SamplerDPMPP_2M_SDE)

[SamplerDPMAdaptative - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SamplerDPMAdaptative)[SamplerDPMPP_2S_Ancestral - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SamplerDPMPP_2S_Ancestral)

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
