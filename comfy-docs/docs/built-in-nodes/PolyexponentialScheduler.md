---
url: https://docs.comfy.org/built-in-nodes/PolyexponentialScheduler/
title: PolyexponentialScheduler - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:43.471083+00:00
---

# PolyexponentialScheduler - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/PolyexponentialScheduler/

Schedulers

# PolyexponentialScheduler - ComfyUI Built-in Node Documentation

Copy pageCopy page

The PolyexponentialScheduler node is designed to generate a sequence of noise levels (sigmas) based on a polyexponential noise schedule.

Copy pageCopy page

The PolyexponentialScheduler node is designed to generate a sequence of noise levels (sigmas) based on a polyexponential noise schedule. This schedule is a polynomial function in the logarithm of sigma, allowing for a flexible and customizable progression of noise levels throughout the diffusion process.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`steps`| Specifies the number of steps in the diffusion process, affecting the granularity of the generated noise levels.| INT  
`sigma_max`| The maximum noise level, setting the upper bound of the noise schedule.| FLOAT  
`sigma_min`| The minimum noise level, setting the lower bound of the noise schedule.| FLOAT  
`rho`| A parameter that controls the shape of the polyexponential noise schedule, influencing how noise levels progress between the minimum and maximum values.| FLOAT  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`sigmas`| The output is a sequence of noise levels (sigmas) tailored to the specified polyexponential noise schedule.| SIGMAS  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PolyexponentialScheduler/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/PolyexponentialScheduler.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/PolyexponentialScheduler)

[OptimalStepsScheduler - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/OptimalStepsScheduler)[SDTurboScheduler - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SDTurboScheduler)

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
