---
url: https://docs.comfy.org/built-in-nodes/SDTurboScheduler/
title: SDTurboScheduler - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:55.660247+00:00
---

# SDTurboScheduler - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SDTurboScheduler/

Schedulers

# SDTurboScheduler - ComfyUI Built-in Node Documentation

Copy pageCopy page

SDTurboScheduler is designed to generate a sequence of sigma values for image sampling

Copy pageCopy page

SDTurboScheduler is designed to generate a sequence of sigma values for image sampling, adjusting the sequence based on the denoise level and the number of steps specified. It leverages a specific model’s sampling capabilities to produce these sigma values, which are crucial for controlling the denoising process during image generation.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`model`| The model parameter specifies the generative model to be used for sigma value generation. It is crucial for determining the specific sampling behavior and capabilities of the scheduler.| `MODEL`  
`steps`| The steps parameter determines the length of the sigma sequence to be generated, directly influencing the granularity of the denoising process.| `INT`  
`denoise`| The denoise parameter adjusts the starting point of the sigma sequence, allowing for finer control over the denoising level applied during image generation.| `FLOAT`  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`sigmas`| A sequence of sigma values generated based on the specified model, steps, and denoise level. These values are essential for controlling the denoising process in image generation.| `SIGMAS`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SdTurboScheduler/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SDTurboScheduler.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SDTurboScheduler)

[PolyexponentialScheduler - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/PolyexponentialScheduler)[VPScheduler - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/VPScheduler)

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
