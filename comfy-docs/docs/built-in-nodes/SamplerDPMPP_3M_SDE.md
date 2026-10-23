---
url: https://docs.comfy.org/built-in-nodes/SamplerDPMPP_3M_SDE/
title: SamplerDPMPP_3M_SDE - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:56.430023+00:00
---

# SamplerDPMPP_3M_SDE - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SamplerDPMPP_3M_SDE/

Samplers

# SamplerDPMPP_3M_SDE - ComfyUI Built-in Node Documentation

Copy pageCopy page

The SamplerDPMPP3MSDE node creates a DPM++ 3M SDE sampler for use in the sampling process.

Copy pageCopy page

The SamplerDPMPP_3M_SDE node creates a DPM++ 3M SDE sampler for use in the sampling process. This sampler uses a third-order multistep stochastic differential equation method with configurable noise parameters. The node allows you to choose whether noise calculations are performed on the GPU or CPU.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`eta`| Controls the stochasticity of the sampling process (default: 1.0)| FLOAT| Yes| 0.0 - 100.0  
`s_noise`| Controls the amount of noise added during sampling (default: 1.0)| FLOAT| Yes| 0.0 - 100.0  
`noise_device`| Selects the device for noise calculations, either GPU or CPU (default: “gpu”)| COMBO| Yes| ”gpu"  
"cpu”  
  
Note: All three inputs are advanced parameters. When `noise_device` is set to “cpu”, the standard `dpmpp_3m_sde` sampler is created; when set to “gpu”, the GPU-accelerated `dpmpp_3m_sde_gpu` sampler is created.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`sampler`| Returns a configured sampler object for use in sampling workflows| SAMPLER  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_3M_SDE/en.md)

* * *

**Source fingerprint (SHA-256):** `0f624398c67e50639fc41384b50b91bab93797bd785dda25f1f5fc649e46825b`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SamplerDPMPP_3M_SDE.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SamplerDPMPP_3M_SDE)

[SamplerDPMPP_2S_Ancestral - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SamplerDPMPP_2S_Ancestral)[SamplerDPMPP_SDE - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SamplerDPMPP_SDE)

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
