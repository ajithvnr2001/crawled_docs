---
url: https://docs.comfy.org/built-in-nodes/ModelSamplingSD3/
title: ModelSamplingSD3 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:37.395159+00:00
---

# ModelSamplingSD3 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ModelSamplingSD3/

Stable Diffusion

# ModelSamplingSD3 - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node applies Stable Diffusion 3 style sampling settings to a model.

Copy pageCopy page

This node applies Stable Diffusion 3 style sampling settings to a model. It makes a copy of the model and replaces its sampling method with a flow-based sampling configuration that uses the given `shift` value, which controls how the sampling distribution is shaped.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The input model to apply SD3 sampling parameters to| MODEL| Yes| -  
`shift`| Controls the sampling shift parameter (default: 3.0)| FLOAT| Yes| 0.0 - 100.0 (step: 0.01)  
  
Note: The `shift` value is applied together with a fixed internal multiplier of 1000. If the original model has a noise scale setting, that value is carried over to the modified model. The original model is not changed; a cloned and patched copy is returned.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| The modified model with SD3 sampling parameters applied| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingSD3/en.md)

* * *

**Source fingerprint (SHA-256):** `a77e38c2cebf6f21f841a953ec5c59096eaf60ffc205c24f34f635e54c5718cb`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ModelSamplingSD3.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ModelSamplingSD3)

[ModelSamplingStableCascade - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ModelSamplingStableCascade)[SUPIRApply - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SUPIRApply)

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
