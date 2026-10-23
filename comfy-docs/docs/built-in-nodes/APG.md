---
url: https://docs.comfy.org/built-in-nodes/APG/
title: APG - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:18.789560+00:00
---

# APG - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/APG/

Custom

# APG - ComfyUI Built-in Node Documentation

Copy pageCopy page

The APG (Adaptive Projected Guidance) node modifies the sampling process by adjusting how guidance is applied during diffusion.

Copy pageCopy page

The APG (Adaptive Projected Guidance) node modifies the sampling process by adjusting how guidance is applied during diffusion. It separates the guidance vector into parallel and orthogonal components relative to the conditional output, allowing for more controlled image generation. The node provides parameters to scale the guidance, normalize its magnitude, and apply momentum for smoother transitions between diffusion steps.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The diffusion model to apply adaptive projected guidance to| MODEL| Yes| -  
`eta`| Controls the scale of the parallel guidance vector. Default CFG behavior at a setting of 1 (default: 1.0).| FLOAT| No| -10.0 to 10.0  
`norm_threshold`| Normalize guidance vector to this value, normalization disabled at a setting of 0 (default: 5.0).| FLOAT| No| 0.0 to 50.0  
`momentum`| Controls a running average of guidance during diffusion, disabled at a setting of 0 (default: 0.0).| FLOAT| No| -5.0 to 1.0  
  
Note: When the noise level (`sigma`) increases during sampling, the momentum running average resets to zero. If the model provides only a single conditioning output (no separate unconditional conditioning), the guidance adjustment is skipped and the conditioning is left unchanged.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| Returns the modified model with adaptive projected guidance applied to its sampling process| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/APG/en.md)

* * *

**Source fingerprint (SHA-256):** `df0c76aee28479d49c4e471e54d1d32082adc6921a6a50b506675144a79e018a`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/APG.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/APG)

[ZImageFunControlnet - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ZImageFunControlnet)[SamplerCustom - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SamplerCustom)

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
