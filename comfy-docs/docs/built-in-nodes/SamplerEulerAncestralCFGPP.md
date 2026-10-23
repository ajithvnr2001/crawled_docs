---
url: https://docs.comfy.org/built-in-nodes/SamplerEulerAncestralCFGPP/
title: SamplerEulerAncestralCFGPP - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:57.311521+00:00
---

# SamplerEulerAncestralCFGPP - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SamplerEulerAncestralCFGPP/

Samplers

# SamplerEulerAncestralCFGPP - ComfyUI Built-in Node Documentation

Copy pageCopy page

The SamplerEulerAncestralCFG++ node creates a sampler that uses the Euler Ancestral method with classifier-free guidance (CFG++) for image generation.

Copy pageCopy page

The SamplerEulerAncestralCFG++ node creates a sampler that uses the Euler Ancestral method with classifier-free guidance (CFG++) for image generation. This sampler combines ancestral sampling techniques with guidance conditioning to produce diverse image variations while maintaining coherence, and allows fine-tuning through parameters that control noise and step size adjustments.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`eta`| Controls the step size during sampling, with higher values resulting in more aggressive updates (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`s_noise`| Adjusts the amount of noise added during the sampling process (default: 1.0)| FLOAT| Yes| 0.0 - 10.0  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`sampler`| Returns a configured sampler object that can be used in the image generation pipeline| SAMPLER  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestralCFGPP/en.md)

* * *

**Source fingerprint (SHA-256):** `de83cb4c3e9aeee60f1554ad1af8181adb4fa62e3d23cec02a6f4396b96500c1`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SamplerEulerAncestralCFGPP.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SamplerEulerAncestralCFGPP)

[SamplerEulerAncestral - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SamplerEulerAncestral)[SamplerLCM - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SamplerLCM)

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
