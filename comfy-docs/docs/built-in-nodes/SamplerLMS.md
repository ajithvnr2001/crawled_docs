---
url: https://docs.comfy.org/built-in-nodes/SamplerLMS/
title: SamplerLMS - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:57.746675+00:00
---

# SamplerLMS - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SamplerLMS/

Samplers

# SamplerLMS - ComfyUI Built-in Node Documentation

Copy pageCopy page

The SamplerLMS node creates a Least Mean Squares (LMS) sampler for use in diffusion models.

Copy pageCopy page

The SamplerLMS node creates a Least Mean Squares (LMS) sampler for use in diffusion models. It generates a sampler object that can be used in the sampling process, allowing you to control the order of the LMS algorithm for numerical stability and accuracy.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`order`| The order parameter for the LMS sampler algorithm, which controls the numerical method’s accuracy and stability (default: 4). This parameter is shown in the advanced section of the node interface.| INT| Yes| 1 to 100  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`sampler`| A configured LMS sampler object that can be used in the sampling pipeline| SAMPLER  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLMS/en.md)

* * *

**Source fingerprint (SHA-256):** `3d59fbbd5b9b0bfa2ee3b384aca08855988d0b7a2a94d805f978b9dd7caa0f39`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SamplerLMS.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SamplerLMS)

[SamplerLCMUpscale - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SamplerLCMUpscale)[SamplerSASolver - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SamplerSASolver)

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
