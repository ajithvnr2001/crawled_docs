---
url: https://docs.comfy.org/built-in-nodes/SamplerDPMPP_2S_Ancestral/
title: SamplerDPMPP_2S_Ancestral - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:56.101221+00:00
---

# SamplerDPMPP_2S_Ancestral - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SamplerDPMPP_2S_Ancestral/

Samplers

# SamplerDPMPP_2S_Ancestral - ComfyUI Built-in Node Documentation

Copy pageCopy page

The SamplerDPMPP2SAncestral node creates a sampler that uses the DPM++ 2S Ancestral sampling method for generating images.

Copy pageCopy page

The SamplerDPMPP_2S_Ancestral node creates a sampler that uses the DPM++ 2S Ancestral sampling method for generating images. This sampler combines deterministic and stochastic elements to produce varied results while maintaining some consistency. It allows you to control the randomness and noise levels during the sampling process.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`eta`| Controls the amount of stochastic noise added during sampling (default: 1.0)| FLOAT| Yes| 0.0 - 100.0 (step 0.01)  
`s_noise`| Controls the scale of noise applied during the sampling process (default: 1.0)| FLOAT| Yes| 0.0 - 100.0 (step 0.01)  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`sampler`| Returns a configured sampler object that can be used in the sampling pipeline| SAMPLER  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_2S_Ancestral/en.md)

* * *

**Source fingerprint (SHA-256):** `8d20ec21e6c699965753413d9ef8b6191553c4b7b606d93c10470aa9d988a308`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SamplerDPMPP_2S_Ancestral.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SamplerDPMPP_2S_Ancestral)

[SamplerDPMPP_2M_SDE - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SamplerDPMPP_2M_SDE)[SamplerDPMPP_3M_SDE - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SamplerDPMPP_3M_SDE)

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
