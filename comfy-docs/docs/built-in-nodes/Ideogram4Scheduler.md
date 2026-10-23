---
url: https://docs.comfy.org/built-in-nodes/Ideogram4Scheduler/
title: Ideogram4Scheduler - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:05.200520+00:00
---

# Ideogram4Scheduler - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Ideogram4Scheduler/

Schedulers

# Ideogram4Scheduler - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Ideogram 4 Scheduler node generates a sequence of sigma values (noise levels) for the diffusion sampling process

Copy pageCopy page

The Ideogram 4 Scheduler node generates a sequence of sigma values (noise levels) for the diffusion sampling process, based on the Ideogram 4 reference schedule. It creates a custom noise schedule that adapts to the image dimensions and allows fine-tuning through statistical parameters.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`steps`| The number of sampling steps to generate the schedule for (default: 20). The output contains `steps + 1` sigma values.| INT| Yes| 1 to 200  
`width`| The width of the image in pixels (default: 1024). The resolution relative to a 512×512 reference shifts the noise schedule.| INT| Yes| 256 to 8192 (step: 16)  
`height`| The height of the image in pixels (default: 1024). The resolution relative to a 512×512 reference shifts the noise schedule.| INT| Yes| 256 to 8192 (step: 16)  
`mu`| The mean parameter for the logit-normal distribution, controlling the central noise level. Combined with the resolution term to form the logSNR shift (default: 0.0).| FLOAT| Yes| -10.0 to 10.0 (step: 0.05)  
`std`| The standard deviation parameter for the logit-normal distribution, controlling the spread of noise levels (default: 1.75).| FLOAT| Yes| 0.1 to 5.0 (step: 0.05)  
  
Note: The schedule is derived from a logit-normal distribution over reference time. A resolution term equal to `0.5 * log((width × height) / (512 × 512))` is added to `mu`, so larger or smaller images shift the schedule relative to a 512×512 reference at the same `mu` value.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`SIGMAS`| A tensor of sigma values representing the noise schedule, with length equal to `steps + 1`. The values descend from high noise to low noise, with the final value set to 0.0 for complete denoising.| SIGMAS  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Ideogram4Scheduler/en.md)

* * *

**Source fingerprint (SHA-256):** `af0749713ce223d2246fc24b5100f18aa68d56746480990282899c223578b8f4`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Ideogram4Scheduler.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Ideogram4Scheduler)

[GITSScheduler - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/GITSScheduler)[KarrasScheduler - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/KarrasScheduler)

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
