---
url: https://docs.comfy.org/built-in-nodes/RenormCFG/
title: RenormCFG - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:50.539063+00:00
---

# RenormCFG - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/RenormCFG/

Patch

# RenormCFG - ComfyUI Built-in Node Documentation

Copy pageCopy page

The RenormCFG node modifies the classifier-free guidance (CFG) process in diffusion models by applying conditional scaling and normalization.

Copy pageCopy page

The RenormCFG node modifies the classifier-free guidance (CFG) process in diffusion models by applying conditional scaling and normalization. It adjusts the denoising process based on a specified timestep threshold and a renormalization factor, controlling the influence of conditional versus unconditional predictions during image generation. The resulting model is returned with this patched CFG behavior.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The diffusion model to apply renormalized CFG to| MODEL| Yes| -  
`cfg_trunc`| Timestep threshold for applying CFG scaling. When the current timestep is below this value, CFG scaling and renormalization are applied; otherwise, only the conditional prediction is used (default: 100.0)| FLOAT| No| 0.0 - 100.0 (step 0.01)  
`renorm_cfg`| Renormalization factor that limits the maximum norm of the CFG-scaled prediction relative to the original conditional prediction. A value of 0.0 disables renormalization (default: 1.0)| FLOAT| No| 0.0 - 100.0 (step 0.01)  
  
Note: `cfg_trunc` and `renorm_cfg` are advanced parameters. Renormalization only takes effect when `renorm_cfg` is greater than 0.0 and the current timestep is below `cfg_trunc`; if the new prediction norm is already below the computed maximum, no rescaling is performed.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| The modified model with the renormalized CFG function applied| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenormCFG/en.md)

* * *

**Source fingerprint (SHA-256):** `5925bdfe2d62ef7261d73cda661834102ae6600b1afe53f4093568a6e83ec2ab`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/RenormCFG.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/RenormCFG)

[ModelSamplingDiscrete - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ModelSamplingDiscrete)[RescaleCFG - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/RescaleCFG)

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
