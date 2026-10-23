---
url: https://docs.comfy.org/built-in-nodes/SamplerDpmppSde/
title: SamplerDpmppSde - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:56.729951+00:00
---

# SamplerDpmppSde - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SamplerDpmppSde/

Samplers

# SamplerDpmppSde - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node is designed to generate a sampler for the DPM++ SDE (Stochastic Differential Equation) model.

Copy pageCopy page

This node is designed to generate a sampler for the DPM++ SDE (Stochastic Differential Equation) model. It adapts to both CPU and GPU execution environments, optimizing the sampler’s implementation based on the available hardware.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`eta`| Specifies the step size for the SDE solver, influencing the granularity of the sampling process.| FLOAT  
`s_noise`| Determines the level of noise to be applied during the sampling process, affecting the diversity of the generated samples.| FLOAT  
`r`| Controls the ratio of noise reduction in the sampling process, impacting the clarity and quality of the generated samples.| FLOAT  
`noise_device`| Selects the execution environment (CPU or GPU) for the sampler, optimizing performance based on available hardware.| COMBO[STRING]  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`sampler`| The generated sampler configured with the specified parameters, ready for use in sampling operations.| SAMPLER  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDpmppSde/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SamplerDpmppSde.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SamplerDpmppSde)

[SamplerDpmpp2mSde - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SamplerDpmpp2mSde)[AddTextPrefix - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/AddTextPrefix)

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
