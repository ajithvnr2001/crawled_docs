---
url: https://docs.comfy.org/built-in-nodes/ModelSamplingContinuousEDM/
title: ModelSamplingContinuousEDM - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:37.059605+00:00
---

# ModelSamplingContinuousEDM - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ModelSamplingContinuousEDM/

Patch

# ModelSamplingContinuousEDM - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node is designed to enhance a model’s sampling capabilities by integrating continuous EDM (Energy-based Diffusion Models) sampling techniques.

Copy pageCopy page

This node is designed to enhance a model’s sampling capabilities by integrating continuous EDM (Energy-based Diffusion Models) sampling techniques. It allows for the dynamic adjustment of the noise levels within the model’s sampling process, offering a more refined control over the generation quality and diversity.

## 

​

Inputs

Parameter| Description| Data Type| Python dtype  
---|---|---|---  
`model`| The model to be enhanced with continuous EDM sampling capabilities. It serves as the foundation for applying the advanced sampling techniques.| `MODEL`| `torch.nn.Module`  
`sampling`| Specifies the type of sampling to be applied, either ‘eps’ for epsilon sampling or ‘v_prediction’ for velocity prediction, influencing the model’s behavior during the sampling process.| COMBO[STRING]| `str`  
`sigma_max`| The maximum sigma value for noise level, allowing for upper bound control in the noise injection process during sampling.| `FLOAT`| `float`  
`sigma_min`| The minimum sigma value for noise level, setting the lower limit for noise injection, thus affecting the model’s sampling precision.| `FLOAT`| `float`  
  
## 

​

Outputs

Parameter| Description| Data Type| Python dtype  
---|---|---|---  
`model`| The enhanced model with integrated continuous EDM sampling capabilities, ready for further use in generation tasks.| MODEL| `torch.nn.Module`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingContinuousEdm/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ModelSamplingContinuousEDM.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ModelSamplingContinuousEDM)

[ModelSamplingAuraFlow - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ModelSamplingAuraFlow)[ModelSamplingContinuousV - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ModelSamplingContinuousV)

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
