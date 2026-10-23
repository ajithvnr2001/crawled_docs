---
url: https://docs.comfy.org/built-in-nodes/SamplerEulerAncestral/
title: SamplerEulerAncestral - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:57.012552+00:00
---

# SamplerEulerAncestral - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SamplerEulerAncestral/

Samplers

# SamplerEulerAncestral - ComfyUI Built-in Node Documentation

Copy pageCopy page

The SamplerEulerAncestral node creates an Euler Ancestral sampler that can be used during image generation.

Copy pageCopy page

The SamplerEulerAncestral node creates an Euler Ancestral sampler that can be used during image generation. This sampler combines Euler integration with ancestral sampling, which adds a degree of randomness at each step to produce varied results. The node lets you adjust how much randomness is applied through its settings.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`eta`| Controls the step size and stochasticity of the sampling process (default: 1.0). This is an advanced parameter.| FLOAT| Yes| 0.0 - 100.0  
`s_noise`| Controls the amount of noise added during sampling (default: 1.0). This is an advanced parameter.| FLOAT| Yes| 0.0 - 100.0  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`sampler`| Returns a configured Euler Ancestral sampler that can be used in the sampling pipeline.| SAMPLER  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestral/en.md)

* * *

**Source fingerprint (SHA-256):** `0d3c1f0ffe01eb6cc17fd53e743713f659218ec19001c670440472ae7d0d3887`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SamplerEulerAncestral.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SamplerEulerAncestral)

[SamplerER_SDE - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SamplerER_SDE)[SamplerEulerAncestralCFGPP - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SamplerEulerAncestralCFGPP)

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
