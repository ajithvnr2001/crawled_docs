---
url: https://docs.comfy.org/built-in-nodes/ModelSamplingContinuousEDM/
title: ModelSamplingContinuousEDM - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-25T12:24:52.362918+00:00
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
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingContinuousEDM/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ModelSamplingContinuousEDM.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ModelSamplingContinuousEDM)

[ModelSamplingAuraFlow](https://docs.comfy.org/built-in-nodes/ModelSamplingAuraFlow)[ModelSamplingContinuousV](https://docs.comfy.org/built-in-nodes/ModelSamplingContinuousV)
