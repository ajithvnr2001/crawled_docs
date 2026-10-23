---
url: https://docs.comfy.org/built-in-nodes/SamplerDPMPP_SDE/
title: SamplerDPMPP_SDE - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:27.487888+00:00
---

# SamplerDPMPP_SDE - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SamplerDPMPP_SDE/

Samplers

# SamplerDPMPP_SDE - ComfyUI Built-in Node Documentation

Copy pageCopy page

SamplerDPMPPSDE creates a DPM++ SDE (Stochastic Differential Equation) sampler for use in the sampling process.

Copy pageCopy page

## 

​

Overview

SamplerDPMPP_SDE creates a DPM++ SDE (Stochastic Differential Equation) sampler for use in the sampling process. This sampler provides a stochastic sampling method with configurable noise parameters and device selection. It returns a sampler object that can be used in the sampling pipeline.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`eta`| Controls the stochasticity of the sampling process (default: 1.0)| FLOAT| Yes| 0.0 - 100.0  
`s_noise`| Controls the amount of noise added during sampling (default: 1.0)| FLOAT| Yes| 0.0 - 100.0  
`r`| A parameter that influences the sampling behavior (default: 0.5)| FLOAT| Yes| 0.0 - 100.0  
`noise_device`| Selects the device where noise calculations are performed. When set to “cpu”, the `dpmpp_sde` sampler is created; when set to “gpu”, the `dpmpp_sde_gpu` sampler is created (default: “gpu”)| COMBO| Yes| ”gpu"  
"cpu”  
  
Note: All inputs are marked as advanced parameters. The `noise_device` selection changes which sampler variant is created: “cpu” maps to `dpmpp_sde` and “gpu” maps to `dpmpp_sde_gpu`.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`sampler`| Returns a configured DPM++ SDE sampler object for use in sampling pipelines| SAMPLER  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_SDE/en.md)

* * *

**Source fingerprint (SHA-256):** `56949712f245abfcc48c09d7d14a1a7778e80ba58535e538484c382d7e0d02c6`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SamplerDPMPP_SDE.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SamplerDPMPP_SDE)

[SamplerDPMPP_3M_SDE - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SamplerDPMPP_3M_SDE)[SamplerER_SDE - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SamplerER_SDE)

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
