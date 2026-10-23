---
url: https://docs.comfy.org/built-in-nodes/ModelSamplingAuraFlow/
title: ModelSamplingAuraFlow - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:37.282678+00:00
---

# ModelSamplingAuraFlow - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ModelSamplingAuraFlow/

Patch

# ModelSamplingAuraFlow - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ModelSamplingAuraFlow node applies a specialized sampling configuration to diffusion models, specifically designed for AuraFlow model architectures.

Copy pageCopy page

The ModelSamplingAuraFlow node applies a specialized sampling configuration to diffusion models, specifically designed for AuraFlow model architectures. It modifies the model’s sampling behavior by applying a shift value that adjusts the sampling distribution. This node inherits from the SD3 model sampling framework and provides fine control over the sampling process.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The diffusion model to apply the AuraFlow sampling configuration to| MODEL| Yes| -  
`shift`| The shift value to apply to the sampling distribution (default: 1.73, step: 0.01)| FLOAT| Yes| 0.0 - 100.0  
`sampling`| The sampling mode used when patching the model (default: “flow”). Marked as an advanced option.| COMBO| No| ”flow"  
"img_to_img_velocity”  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| The modified model with AuraFlow sampling configuration applied| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingAuraFlow/en.md)

* * *

**Source fingerprint (SHA-256):** `5c1381d2dec9ac84a7ee6cd134de444ab50f657eafd960263c63a055d0a139d6`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ModelSamplingAuraFlow.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ModelSamplingAuraFlow)

[ModelNoiseScale - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ModelNoiseScale)[ModelSamplingContinuousEDM - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ModelSamplingContinuousEDM)

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
