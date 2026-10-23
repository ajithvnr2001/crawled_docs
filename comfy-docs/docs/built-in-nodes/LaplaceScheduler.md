---
url: https://docs.comfy.org/built-in-nodes/LaplaceScheduler/
title: LaplaceScheduler - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:19.992179+00:00
---

# LaplaceScheduler - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LaplaceScheduler/

Schedulers

# LaplaceScheduler - ComfyUI Built-in Node Documentation

Copy pageCopy page

The LaplaceScheduler node generates a sequence of sigma values following a Laplace distribution for use in diffusion sampling.

Copy pageCopy page

The LaplaceScheduler node generates a sequence of sigma values following a Laplace distribution for use in diffusion sampling. It creates a schedule of noise levels that gradually decrease from a maximum to minimum value, using Laplace distribution parameters to control the progression. This scheduler is commonly used in custom sampling workflows to define the noise schedule for diffusion models.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`steps`| Number of sampling steps in the schedule (default: 20)| INT| Yes| 1 to 10000  
`sigma_max`| Maximum sigma value at the start of the schedule (default: 14.614642)| FLOAT| Yes| 0.0 to 5000.0  
`sigma_min`| Minimum sigma value at the end of the schedule (default: 0.0291675)| FLOAT| Yes| 0.0 to 5000.0  
`mu`| Mean parameter for the Laplace distribution (default: 0.0)| FLOAT| Yes| -10.0 to 10.0  
`beta`| Scale parameter for the Laplace distribution (default: 0.5)| FLOAT| Yes| 0.0 to 10.0  
  
Note: `sigma_max`, `sigma_min`, `mu`, and `beta` are advanced parameters.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`SIGMAS`| A sequence of sigma values following a Laplace distribution schedule| SIGMAS  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LaplaceScheduler/en.md)

* * *

**Source fingerprint (SHA-256):** `8e5ca00f4797f863a2cf8b9b115ec27beb7f65981cbb04eb036150402fc19389`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LaplaceScheduler.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LaplaceScheduler)

[KarrasScheduler - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/KarrasScheduler)[LTXVScheduler - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LTXVScheduler)

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
