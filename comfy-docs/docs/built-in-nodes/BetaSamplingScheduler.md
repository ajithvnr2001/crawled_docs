---
url: https://docs.comfy.org/built-in-nodes/BetaSamplingScheduler/
title: BetaSamplingScheduler - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:24.172024+00:00
---

# BetaSamplingScheduler - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/BetaSamplingScheduler/

Schedulers

# BetaSamplingScheduler - ComfyUI Built-in Node Documentation

Copy pageCopy page

The BetaSamplingScheduler node generates a sequence of noise levels (sigmas) for the sampling process using a beta scheduling algorithm.

Copy pageCopy page

The BetaSamplingScheduler node generates a sequence of noise levels (sigmas) for the sampling process using a beta scheduling algorithm. It takes a model and configuration parameters to create a customized noise schedule that controls the denoising process during image generation. This scheduler allows fine-tuning of the noise reduction trajectory through alpha and beta parameters.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The model used for sampling, which provides the model sampling object| MODEL| Yes| -  
`steps`| The number of sampling steps to generate sigmas for (default: 20)| INT| Yes| 1 to 10000  
`alpha`| Alpha parameter for the beta scheduler, controlling the scheduling curve (default: 0.6, advanced parameter)| FLOAT| Yes| 0.0 to 50.0 (step 0.01)  
`beta`| Beta parameter for the beta scheduler, controlling the scheduling curve (default: 0.6, advanced parameter)| FLOAT| Yes| 0.0 to 50.0 (step 0.01)  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`SIGMAS`| A sequence of noise levels (sigmas) used for the sampling process| SIGMAS  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BetaSamplingScheduler/en.md)

* * *

**Source fingerprint (SHA-256):** `80adae3cbedff7fe544a1fbcf638af7965f1216e422931063ecf67da53ddff95`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/BetaSamplingScheduler.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/BetaSamplingScheduler)

[BasicScheduler - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/BasicScheduler)[ExponentialScheduler - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ExponentialScheduler)

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
