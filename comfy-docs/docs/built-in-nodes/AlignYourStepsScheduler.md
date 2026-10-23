---
url: https://docs.comfy.org/built-in-nodes/AlignYourStepsScheduler/
title: AlignYourStepsScheduler - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:20.770107+00:00
---

# AlignYourStepsScheduler - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/AlignYourStepsScheduler/

Schedulers

# AlignYourStepsScheduler - ComfyUI Built-in Node Documentation

Copy pageCopy page

The AlignYourStepsScheduler node generates sigma values (noise levels) for the denoising process based on different model types.

Copy pageCopy page

The AlignYourStepsScheduler node generates sigma values (noise levels) for the denoising process based on different model types. It calculates appropriate noise levels for each step of the sampling process and adjusts the total number of steps according to the `denoise` parameter, helping align the sampling steps with the specific requirements of different diffusion models.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model_type`| Specifies the type of model to use for sigma calculation (default: “SD1”)| COMBO| Yes| `"SD1"`  
`"SDXL"`  
`"SVD"`  
`steps`| The total number of sampling steps to generate (default: 10)| INT| Yes| 1 to 10000  
`denoise`| Controls how much to denoise the image, where 1.0 uses all steps and lower values use fewer steps (default: 1.0)| FLOAT| Yes| 0.0 to 1.0 (step: 0.01)  
  
Note: Each model type has a built-in noise level schedule containing 11 sigma values (for 10 steps). When `denoise` is 0.0, the node returns an empty sigma tensor. When `denoise` is between 0.0 and 1.0, the effective number of steps is calculated as `round(steps × denoise)`, and only the corresponding last portion of the sigma schedule is used. If the requested `steps` value does not match the built-in schedule length, the noise levels are log-linearly interpolated to match the requested step count. The final sigma value is always set to 0.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`sigmas`| Returns the calculated sigma values for the denoising process| SIGMAS  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AlignYourStepsScheduler/en.md)

* * *

**Source fingerprint (SHA-256):** `3adbe1016c1ff4b9b7ad3737f50b168f54444d4ca355488e60537d1136f85d3f`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/AlignYourStepsScheduler.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/AlignYourStepsScheduler)

[VOIDSampler - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/VOIDSampler)[BasicScheduler - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/BasicScheduler)

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
