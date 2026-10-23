---
url: https://docs.comfy.org/built-in-nodes/LTXVScheduler/
title: LTXVScheduler - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:18.829460+00:00
---

# LTXVScheduler - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LTXVScheduler/

Schedulers

# LTXVScheduler - ComfyUI Built-in Node Documentation

Copy pageCopy page

The LTXVScheduler node generates sigma values for a custom sampling process.

Copy pageCopy page

The LTXVScheduler node generates sigma values for a custom sampling process. It calculates the noise schedule from the number of tokens in the provided latent, or uses a default of 4096 tokens when no latent is connected, and can optionally stretch the sigma values so the final value matches the specified `terminal` value.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`steps`| Number of sampling steps (default: 20)| INT| Yes| 1-10000  
`max_shift`| Maximum shift value used in the sigma calculation (default: 2.05)| FLOAT| Yes| 0.0-100.0 (step: 0.01)  
`base_shift`| Base shift value used in the sigma calculation (default: 0.95)| FLOAT| Yes| 0.0-100.0 (step: 0.01)  
`stretch`| Stretch the sigmas to be in the range [terminal, 1] (default: True)| BOOLEAN| Yes| True/False  
`terminal`| The terminal value of the sigmas after stretching (default: 0.1). Used only when `stretch` is enabled.| FLOAT| Yes| 0.0-0.99 (step: 0.01)  
`latent`| Optional latent input used to calculate the token count for sigma adjustment. When not provided, a default token count of 4096 is used.| LATENT| No| -  
  
**Note:** When `stretch` is enabled, the non-zero sigma values are rescaled so that the last non-zero sigma equals the `terminal` value.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`sigmas`| Sigma values generated for the sampling process| SIGMAS  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVScheduler/en.md)

* * *

**Source fingerprint (SHA-256):** `5b4907e905e27a951c332c400e24023ef089df7a5f4a17b1fc8ba42a41302399`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LTXVScheduler.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LTXVScheduler)

[LaplaceScheduler - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LaplaceScheduler)[OptimalStepsScheduler - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/OptimalStepsScheduler)

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
