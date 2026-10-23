---
url: https://docs.comfy.org/built-in-nodes/CFGNorm/
title: CFGNorm - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:32.224324+00:00
---

# CFGNorm - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/CFGNorm/

Guidance

# CFGNorm - ComfyUI Built-in Node Documentation

Copy pageCopy page

CFGNorm adjusts how classifier-free guidance (CFG) is applied in diffusion models by comparing the size (norm) of the conditional prediction with the guided

Copy pageCopy page

CFGNorm adjusts how classifier-free guidance (CFG) is applied in diffusion models by comparing the size (norm) of the conditional prediction with the guided prediction and rescaling the result. A `strength` value controls how much of the adjustment is applied. By default the scaling only attenuates the guidance output, while enabling `pre_cfg` rescales the combined noise before the sampler’s CFG combine without clamping, which can amplify the result.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The diffusion model to apply CFG normalization to| MODEL| Yes| -  
`strength`| Controls the intensity of the normalization effect applied to the CFG scaling (default: 1.0)| FLOAT| Yes| 0.0 to 100.0 (step 0.01)  
`pre_cfg`| If true, rescale the combined noise BEFORE the sampler’s CFG combine, without clamping (can amplify). Matches the norm-scaled CFG used by models like Lens. Default false keeps the original post-CFG x0-space attenuate-only behavior. (default: False)| BOOLEAN| No| true / false  
  
Note: This node is marked as experimental.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`patched_model`| Returns the modified model with CFG normalization applied to its sampling process| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGNorm/en.md)

* * *

**Source fingerprint (SHA-256):** `427dda498ebda2642489aa2591f063355a77b1e064e0dc7fa8570ed8200c2734`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/CFGNorm.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/CFGNorm)

[ModelComputeDtype - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ModelComputeDtype)[CFGZeroStar - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/CFGZeroStar)

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
