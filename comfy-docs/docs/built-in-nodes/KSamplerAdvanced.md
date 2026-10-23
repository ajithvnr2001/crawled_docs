---
url: https://docs.comfy.org/built-in-nodes/KSamplerAdvanced/
title: KSamplerAdvanced - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:13.004361+00:00
---

# KSamplerAdvanced - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/KSamplerAdvanced/

Sampling

# KSamplerAdvanced - ComfyUI Built-in Node Documentation

Copy pageCopy page

The KSamplerAdvanced node is designed to enhance the sampling process by providing advanced configurations and techniques.

Copy pageCopy page

The KSamplerAdvanced node is designed to enhance the sampling process by providing advanced configurations and techniques. It aims to offer more sophisticated options for generating samples from a model, improving upon the basic KSampler functionalities.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`model`| Specifies the model from which samples are to be generated, playing a crucial role in the sampling process.| MODEL  
`add_noise`| Determines whether noise should be added to the sampling process, affecting the diversity and quality of the generated samples.| COMBO[STRING]  
`noise_seed`| Sets the seed for noise generation, ensuring reproducibility in the sampling process.| INT  
`steps`| Defines the number of steps to be taken in the sampling process, impacting the detail and quality of the output.| INT  
`cfg`| Controls the conditioning factor, influencing the direction and space of the sampling process.| FLOAT  
`sampler_name`| Selects the specific sampler to be used, allowing for customization of the sampling technique.| COMBO[STRING]  
`scheduler`| Chooses the scheduler for controlling the sampling process, affecting the progression and quality of samples.| COMBO[STRING]  
`positive`| Specifies the positive conditioning to guide the sampling towards desired attributes.| CONDITIONING  
`negative`| Specifies the negative conditioning to steer the sampling away from certain attributes.| CONDITIONING  
`latent_image`| Provides the initial latent image to be used in the sampling process, serving as a starting point.| LATENT  
`start_at_step`| Determines the starting step of the sampling process, allowing for control over the sampling progression.| INT  
`end_at_step`| Sets the ending step of the sampling process, defining the scope of the sampling.| INT  
`return_with_leftover_noise`| Indicates whether to return the sample with leftover noise, affecting the final output’s appearance.| COMBO[STRING]  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`latent`| The output represents the latent image generated from the model, reflecting the applied configurations and techniques.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KSamplerAdvanced/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/KSamplerAdvanced.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/KSamplerAdvanced)

[KSampler - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/KSampler)[LoadTrainingDataset - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LoadTrainingDataset)

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
