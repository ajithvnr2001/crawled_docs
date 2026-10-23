---
url: https://docs.comfy.org/built-in-nodes/ExponentialScheduler/
title: ExponentialScheduler - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:54.915419+00:00
---

# ExponentialScheduler - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ExponentialScheduler/

Schedulers

# ExponentialScheduler - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ExponentialScheduler node is designed to generate a sequence of sigma values following an exponential schedule for diffusion sampling processes.

Copy pageCopy page

The `ExponentialScheduler` node is designed to generate a sequence of sigma values following an exponential schedule for diffusion sampling processes. It provides a customizable approach to control the noise levels applied at each step of the diffusion process, allowing for fine-tuning of the sampling behavior.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`steps`| Specifies the number of steps in the diffusion process. It influences the length of the generated sigma sequence and thus the granularity of the noise application.| INT  
`sigma_max`| Defines the maximum sigma value, setting the upper limit of noise intensity in the diffusion process. It plays a crucial role in determining the range of noise levels applied.| FLOAT  
`sigma_min`| Sets the minimum sigma value, establishing the lower boundary of noise intensity. This parameter helps in fine-tuning the starting point of the noise application.| FLOAT  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`sigmas`| A sequence of sigma values generated according to the exponential schedule. These values are used to control the noise levels at each step of the diffusion process.| SIGMAS  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ExponentialScheduler/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ExponentialScheduler.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ExponentialScheduler)

[BetaSamplingScheduler - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/BetaSamplingScheduler)[Flux2Scheduler - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Flux2Scheduler)

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
