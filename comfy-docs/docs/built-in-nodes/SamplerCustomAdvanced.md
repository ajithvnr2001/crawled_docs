---
url: https://docs.comfy.org/built-in-nodes/SamplerCustomAdvanced/
title: SamplerCustomAdvanced - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:56.357300+00:00
---

# SamplerCustomAdvanced - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SamplerCustomAdvanced/

Custom

# SamplerCustomAdvanced - ComfyUI Built-in Node Documentation

Copy pageCopy page

The SamplerCustomAdvanced node performs advanced latent space sampling using custom noise, guidance, and sampling configurations.

Copy pageCopy page

The SamplerCustomAdvanced node performs advanced latent space sampling using custom noise, guidance, and sampling configurations. It processes a latent image through a guided sampling process with a customizable noise generator and sigma schedule, producing both the final sampled output and a denoised version when available.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`noise`| The noise generator that provides the initial noise pattern and seed for the sampling process| NOISE| Yes| -  
`guider`| The guidance model that directs the sampling process toward the desired output| GUIDER| Yes| -  
`sampler`| The sampling algorithm that defines how the latent space is traversed during generation| SAMPLER| Yes| -  
`sigmas`| The sigma schedule that controls the noise levels throughout the sampling steps| SIGMAS| Yes| -  
`latent_image`| The initial latent representation that serves as the starting point for sampling. Supports an optional `noise_mask` key for selective denoising, and optional `downscale_ratio_spacial` and `downscale_ratio_temporal` keys for advanced latent handling| LATENT| Yes| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The final sampled latent representation after completing the sampling process. Any `downscale_ratio_spacial` or `downscale_ratio_temporal` keys from the input latent are removed from this output| LATENT  
`denoised_output`| A denoised version of the output when the sampling process produces an intermediate clean prediction (x0), otherwise returns the same as `output`. When available, this represents the model’s best estimate of the clean latent| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerCustomAdvanced/en.md)

* * *

**Source fingerprint (SHA-256):** `23cffad0f7cf74dcd494c2828b2116bb4d00a1e55e42ded074b587ac20183290`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SamplerCustomAdvanced.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SamplerCustomAdvanced)

[SamplerCustom - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SamplerCustom)[BasicGuider - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/BasicGuider)

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
