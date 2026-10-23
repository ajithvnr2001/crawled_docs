---
url: https://docs.comfy.org/built-in-nodes/GITSScheduler/
title: GITSScheduler - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:58.669836+00:00
---

# GITSScheduler - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/GITSScheduler/

Schedulers

# GITSScheduler - ComfyUI Built-in Node Documentation

Copy pageCopy page

The GITSScheduler node generates noise schedule sigmas for the GITS (Generative Iterative Time Steps) sampling method.

Copy pageCopy page

The GITSScheduler node generates noise schedule sigmas for the GITS (Generative Iterative Time Steps) sampling method. It calculates sigma values based on a coefficient parameter and number of steps, with a denoising factor that can reduce the total steps used. The node uses pre-defined noise levels and interpolation to create the final sigma schedule.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`coeff`| Advanced parameter. The coefficient value that controls the noise schedule curve (default: 1.20). The value is rounded to two decimals and selects which pre-defined noise level table is used.| FLOAT| Yes| 0.80 - 1.50 (step 0.05)  
`steps`| The total number of sampling steps to generate sigmas for (default: 10).| INT| Yes| 2 - 1000  
`denoise`| Denoising factor that reduces the number of steps used (default: 1.0).| FLOAT| Yes| 0.0 - 1.0 (step 0.01)  
  
**Note:** When `denoise` is 0.0 or less, the node returns an empty tensor. When `denoise` is less than 1.0, the actual number of steps used is calculated as `round(steps * denoise)`, and only the last corresponding part of the schedule is kept. For steps between 2 and 20, the node selects a matching pre-defined noise schedule. For steps greater than 20, the node uses log-linear interpolation to extend the pre-defined noise levels to the desired number of steps.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`sigmas`| The generated sigma values for the noise schedule. For N sampling steps, N+1 sigma values are returned, and the last sigma is set to 0.| SIGMAS  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GITSScheduler/en.md)

* * *

**Source fingerprint (SHA-256):** `f46681970fece985f6a4b62d0817d1ea306f1ca9a20189f937512dd5717f458b`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/GITSScheduler.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/GITSScheduler)

[Flux2Scheduler - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Flux2Scheduler)[Ideogram4Scheduler - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Ideogram4Scheduler)

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
