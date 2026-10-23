---
url: https://docs.comfy.org/built-in-nodes/DifferentialDiffusion/
title: DifferentialDiffusion - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:27.832236+00:00
---

# DifferentialDiffusion - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/DifferentialDiffusion/

Experimental

# DifferentialDiffusion - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Differential Diffusion node modifies the denoising process by applying a binary mask based on timestep thresholds.

Copy pageCopy page

The Differential Diffusion node modifies the denoising process by applying a binary mask based on timestep thresholds. It creates a mask that blends between the original denoise mask and a threshold-based binary mask, allowing controlled adjustment of the diffusion process strength.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The diffusion model to modify| MODEL| Yes| -  
`strength`| Controls the blending strength between the original denoise mask and the binary threshold mask (default: 1.0)| FLOAT| No| 0.0 - 1.0  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| The modified diffusion model with updated denoise mask function| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DifferentialDiffusion/en.md)

* * *

**Source fingerprint (SHA-256):** `26387c3e6c7ead5415b36cfc9b9eef73448527e70646ab253984ff9627f69a25`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/DifferentialDiffusion.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/DifferentialDiffusion)

[StableCascade_SuperResolutionControlnet - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/StableCascade_SuperResolutionControlnet)[FluxKVCache - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/FluxKVCache)

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
