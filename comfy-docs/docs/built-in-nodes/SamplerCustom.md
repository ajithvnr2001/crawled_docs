---
url: https://docs.comfy.org/built-in-nodes/SamplerCustom/
title: SamplerCustom - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:55.927649+00:00
---

# SamplerCustom - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SamplerCustom/

Custom

# SamplerCustom - ComfyUI Built-in Node Documentation

Copy pageCopy page

The SamplerCustom node is designed to provide a flexible and customizable sampling mechanism for various applications.

Copy pageCopy page

The SamplerCustom node is designed to provide a flexible and customizable sampling mechanism for various applications. It enables users to select and configure different sampling strategies tailored to their specific needs, enhancing the adaptability and efficiency of the sampling process.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`model`| The ‘model’ input type specifies the model to be used for sampling, playing a crucial role in determining the sampling behavior and output.| `MODEL`  
`add_noise`| The ‘add_noise’ input type allows users to specify whether noise should be added to the sampling process, influencing the diversity and characteristics of the generated samples.| `BOOLEAN`  
`noise_seed`| The ‘noise_seed’ input type provides a seed for the noise generation, ensuring reproducibility and consistency in the sampling process when adding noise.| `INT`  
`cfg`| The ‘cfg’ input type sets the configuration for the sampling process, allowing for fine-tuning of the sampling parameters and behavior.| `FLOAT`  
`positive`| The ‘positive’ input type represents positive conditioning information, guiding the sampling process towards generating samples that align with specified positive attributes.| `CONDITIONING`  
`negative`| The ‘negative’ input type represents negative conditioning information, steering the sampling process away from generating samples that exhibit specified negative attributes.| `CONDITIONING`  
`sampler`| The ‘sampler’ input type selects the specific sampling strategy to be employed, directly impacting the nature and quality of the generated samples.| `SAMPLER`  
`sigmas`| The ‘sigmas’ input type defines the noise levels to be used in the sampling process, affecting the exploration of the sample space and the diversity of the output.| `SIGMAS`  
`latent_image`| The ‘latent_image’ input type provides an initial latent image for the sampling process, serving as a starting point for sample generation.| `LATENT`  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`output`| The ‘output’ represents the primary result of the sampling process, containing the generated samples.| `LATENT`  
`denoised_output`| The ‘denoised_output’ represents the samples after a denoising process has been applied, potentially enhancing the clarity and quality of the generated samples.| `LATENT`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerCustom/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SamplerCustom.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SamplerCustom)

[APG - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/APG)[SamplerCustomAdvanced - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SamplerCustomAdvanced)

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
