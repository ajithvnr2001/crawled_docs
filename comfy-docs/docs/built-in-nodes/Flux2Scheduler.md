---
url: https://docs.comfy.org/built-in-nodes/Flux2Scheduler/
title: Flux2Scheduler - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:55.752653+00:00
---

# Flux2Scheduler - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Flux2Scheduler/

Schedulers

# Flux2Scheduler - ComfyUI Built-in Node Documentation

Copy pageCopy page

Flux2Scheduler generates a sequence of noise levels (sigmas) for the denoising process, specifically tailored for the Flux model.

Copy pageCopy page

Flux2Scheduler generates a sequence of noise levels (sigmas) for the denoising process, specifically tailored for the Flux model. It calculates a schedule based on the number of denoising steps and the dimensions of the target image, which influences the progression of noise removal during image generation.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`steps`| The number of denoising steps to perform. A higher value typically leads to more detailed results but takes longer to process (default: 20).| INT| Yes| 1 to 4096  
`width`| The width of the image to be generated, in pixels. This value influences the noise schedule calculation (default: 1024).| INT| Yes| 16 to 16384  
`height`| The height of the image to be generated, in pixels. This value influences the noise schedule calculation (default: 1024).| INT| Yes| 16 to 16384  
  
Note: The schedule is computed from the image sequence length, which is derived from `width` and `height` as `(width * height) / 256`, reflecting the model’s 16x latent downsampling. Larger images produce longer sequences, which shifts the noise schedule accordingly.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`sigmas`| A sequence of noise level values (sigmas) that define the denoising schedule for the sampler.| SIGMAS  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2Scheduler/en.md)

* * *

**Source fingerprint (SHA-256):** `9606177f37f7bc03aef524623f03b7f24bcdc3d9327dcdf74863fe2befeb2b65`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Flux2Scheduler.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Flux2Scheduler)

[ExponentialScheduler - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ExponentialScheduler)[GITSScheduler - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/GITSScheduler)

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
