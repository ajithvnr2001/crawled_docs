---
url: https://docs.comfy.org/built-in-nodes/OptimalStepsScheduler/
title: OptimalStepsScheduler - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:40.260403+00:00
---

# OptimalStepsScheduler - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/OptimalStepsScheduler/

Schedulers

# OptimalStepsScheduler - ComfyUI Built-in Node Documentation

Copy pageCopy page

The OptimalStepsScheduler node creates a noise schedule (a sequence of sigma values) for use during diffusion sampling.

Copy pageCopy page

The OptimalStepsScheduler node creates a noise schedule (a sequence of sigma values) for use during diffusion sampling. It chooses the base noise levels from the selected model type, adjusts the schedule when denoising is only partially applied, and interpolates the levels so the returned sigmas match the requested step count.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model_type`| The type of diffusion model to use for the noise level calculation. Each option uses its own predefined table of noise levels.| COMBO| Yes| ”FLUX"  
"Wan"  
"Chroma”  
`steps`| The total number of sampling steps to calculate (default: 20).| INT| Yes| 3 to 1000  
`denoise`| Controls the denoising strength, which adjusts the effective number of steps (default: 1.0).| FLOAT| Yes| 0.0 to 1.0 (step: 0.01)  
  
**Note:** The base noise level table for the selected `model_type` is resampled with log-linear interpolation whenever its length does not equal `steps + 1`, so the output always matches the requested step count. **Note:** When `denoise` is less than 1.0, the node uses `round(steps * denoise)` as the total number of effective steps and keeps only the matching tail of the schedule. If `denoise` is 0.0 or lower, the node returns an empty tensor.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`sigmas`| A sequence of sigma values representing the noise schedule for diffusion sampling. The final value in the sequence is always set to 0.| SIGMAS  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OptimalStepsScheduler/en.md)

* * *

**Source fingerprint (SHA-256):** `fd48c94ca16c8a3d8e6f0138018e7b13c15d100d6147807bcb23d838899045b7`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/OptimalStepsScheduler.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/OptimalStepsScheduler)

[LTXVScheduler - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LTXVScheduler)[PolyexponentialScheduler - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/PolyexponentialScheduler)

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
