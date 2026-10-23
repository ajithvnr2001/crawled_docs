---
url: https://docs.comfy.org/built-in-nodes/KarrasScheduler/
title: KarrasScheduler - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:13.659336+00:00
---

# KarrasScheduler - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/KarrasScheduler/

Schedulers

# KarrasScheduler - ComfyUI Built-in Node Documentation

Copy pageCopy page

The KarrasScheduler node is designed to generate a sequence of noise levels (sigmas) based on the Karras et al. (2022) noise schedule.

Copy pageCopy page

The KarrasScheduler node is designed to generate a sequence of noise levels (sigmas) based on the Karras et al. (2022) noise schedule. This scheduler is useful for controlling the diffusion process in generative models, allowing for fine-tuned adjustments to the noise levels applied at each step of the generation process.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`steps`| Specifies the number of steps in the noise schedule, affecting the granularity of the generated sigmas sequence.| INT  
`sigma_max`| The maximum sigma value in the noise schedule, setting the upper bound of noise levels.| FLOAT  
`sigma_min`| The minimum sigma value in the noise schedule, setting the lower bound of noise levels.| FLOAT  
`rho`| A parameter that controls the shape of the noise schedule curve, influencing how noise levels progress from sigma_min to sigma_max.| FLOAT  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`sigmas`| The generated sequence of noise levels (sigmas) following the Karras et al. (2022) noise schedule.| SIGMAS  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KarrasScheduler/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/KarrasScheduler.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/KarrasScheduler)

[Ideogram4Scheduler - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Ideogram4Scheduler)[LaplaceScheduler - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LaplaceScheduler)

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
