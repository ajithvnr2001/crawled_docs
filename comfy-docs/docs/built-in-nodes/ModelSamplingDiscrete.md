---
url: https://docs.comfy.org/built-in-nodes/ModelSamplingDiscrete/
title: ModelSamplingDiscrete - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:37.578339+00:00
---

# ModelSamplingDiscrete - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ModelSamplingDiscrete/

Patch

# ModelSamplingDiscrete - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node is designed to modify the sampling behavior of a model by applying a discrete sampling strategy.

Copy pageCopy page

This node is designed to modify the sampling behavior of a model by applying a discrete sampling strategy. It allows for the selection of different sampling methods, such as epsilon, v_prediction, lcm, or x0, and optionally adjusts the model’s noise reduction strategy based on the zero-shot noise ratio (zsnr) setting.

## 

​

Inputs

Parameter| Description| Data Type| Python dtype  
---|---|---|---  
`model`| The model to which the discrete sampling strategy will be applied. This parameter is crucial as it defines the base model that will undergo modification.| MODEL| `torch.nn.Module`  
`sampling`| Specifies the discrete sampling method to be applied to the model. The choice of method affects how the model generates samples, offering different strategies for sampling.| COMBO[STRING]| `str`  
`zsnr`| A boolean flag that, when enabled, adjusts the model’s noise reduction strategy based on the zero-shot noise ratio. This can influence the quality and characteristics of the generated samples.| `BOOLEAN`| `bool`  
  
## 

​

Outputs

Parameter| Description| Data Type| Python dtype  
---|---|---|---  
`model`| The modified model with the applied discrete sampling strategy. This model is now equipped to generate samples using the specified method and adjustments.| MODEL| `torch.nn.Module`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingDiscrete/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ModelSamplingDiscrete.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ModelSamplingDiscrete)

[ModelSamplingContinuousV - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ModelSamplingContinuousV)[RenormCFG - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/RenormCFG)

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
