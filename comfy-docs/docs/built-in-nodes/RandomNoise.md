---
url: https://docs.comfy.org/built-in-nodes/RandomNoise/
title: RandomNoise - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:46.579849+00:00
---

# RandomNoise - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/RandomNoise/

Noise

# RandomNoise - ComfyUI Built-in Node Documentation

Copy pageCopy page

The RandomNoise node creates a noise generator based on a seed value for use during the sampling process.

Copy pageCopy page

The RandomNoise node creates a noise generator based on a seed value for use during the sampling process. The same seed always produces the same noise pattern, allowing for consistent, reproducible results across multiple runs. Samplers use the generated noise when processing latent images.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`noise_seed`| The seed value used to generate the random noise pattern (default: 0). The same seed always produces the same noise output. This input includes a control-after-generate option to automatically update the seed after each generation.| INT| Yes| 0 to 18446744073709551615  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`noise`| A noise object that generates random noise for latent samples based on the provided seed value. Used by samplers during the sampling process.| NOISE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RandomNoise/en.md)

* * *

**Source fingerprint (SHA-256):** `b55ff98c636c55f064ede82c6848ffa163d1fd9b0cf6195f4a35603cfbe2bc1e`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/RandomNoise.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/RandomNoise)

[DisableNoise - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/DisableNoise)[KSamplerSelect - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/KSamplerSelect)

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
