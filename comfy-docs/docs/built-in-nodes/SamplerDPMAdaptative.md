---
url: https://docs.comfy.org/built-in-nodes/SamplerDPMAdaptative/
title: SamplerDPMAdaptative - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:56.280643+00:00
---

# SamplerDPMAdaptative - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SamplerDPMAdaptative/

Samplers

# SamplerDPMAdaptative - ComfyUI Built-in Node Documentation

Copy pageCopy page

The SamplerDPMAdaptative node implements an adaptive DPM (Diffusion Probabilistic Model) sampler that automatically adjusts step sizes during the sampling

Copy pageCopy page

The SamplerDPMAdaptative node implements an adaptive DPM (Diffusion Probabilistic Model) sampler that automatically adjusts step sizes during the sampling process. It uses tolerance-based error control to determine optimal step sizes, balancing computational efficiency with sampling accuracy. This adaptive approach helps maintain quality while potentially reducing the number of steps needed.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`order`| The order of the sampler method (default: 3)| INT| Yes| 2-3  
`rtol`| Relative tolerance for error control (default: 0.05)| FLOAT| Yes| 0.0-100.0  
`atol`| Absolute tolerance for error control (default: 0.0078)| FLOAT| Yes| 0.0-100.0  
`h_init`| Initial step size (default: 0.05)| FLOAT| Yes| 0.0-100.0  
`pcoeff`| Proportional coefficient for step size control (default: 0.0)| FLOAT| Yes| 0.0-100.0  
`icoeff`| Integral coefficient for step size control (default: 1.0)| FLOAT| Yes| 0.0-100.0  
`dcoeff`| Derivative coefficient for step size control (default: 0.0)| FLOAT| Yes| 0.0-100.0  
`accept_safety`| Safety factor for step acceptance (default: 0.81)| FLOAT| Yes| 0.0-100.0  
`eta`| Stochasticity parameter (default: 0.0)| FLOAT| Yes| 0.0-100.0  
`s_noise`| Noise scaling factor (default: 1.0)| FLOAT| Yes| 0.0-100.0  
  
All inputs are advanced parameters used to fine-tune the adaptive sampling behavior. All numeric inputs allow decimal values and accept a minimum of 0.0 and a maximum of 100.0, except `order`, which is limited to the integer values 2 or 3.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`sampler`| Returns a configured DPM adaptive sampler instance| SAMPLER  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMAdaptative/en.md)

* * *

**Source fingerprint (SHA-256):** `07b2e5b9f21ec101eabccc6be245d043e64a996a14db10434b03eaae0a91b1d8`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SamplerDPMAdaptative.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SamplerDPMAdaptative)

[SamplerARVideo - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SamplerARVideo)[SamplerDPMPP_2M_SDE - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SamplerDPMPP_2M_SDE)

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
