---
url: https://docs.comfy.org/built-in-nodes/VOIDSampler/
title: VOIDSampler - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:18.078415+00:00
---

# VOIDSampler - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/VOIDSampler/

Samplers

# VOIDSampler - ComfyUI Built-in Node Documentation

Copy pageCopy page

VOIDSampler is a specialized DDIM sampler designed for VOID inpainting models.

Copy pageCopy page

VOIDSampler is a specialized DDIM sampler designed for VOID inpainting models. It reproduces the exact denoising process VOID was trained with, skipping the noise scaling that standard KSamplers apply. Use this node together with SamplerCustom or SamplerCustomAdvanced, paired with RandomNoise or VOIDWarpedNoiseSource.

## 

​

Inputs

This node has no configurable input parameters. It is a self-contained sampler that applies a fixed DDIM sampling algorithm.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
 _No inputs_|  This node does not accept any input parameters.| -| -| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`SAMPLER`| A sampler object implementing the VOID DDIM algorithm, ready to be connected to SamplerCustom or SamplerCustomAdvanced nodes.| SAMPLER  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDSampler/en.md)

* * *

**Source fingerprint (SHA-256):** `b8bb6d3d7220cca4a6dd252efe9c92953b1c5c67c14365e5e0583bc9bdb133be`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/VOIDSampler.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/VOIDSampler)

[SamplerSEEDS2 - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SamplerSEEDS2)[AlignYourStepsScheduler - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/AlignYourStepsScheduler)

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
