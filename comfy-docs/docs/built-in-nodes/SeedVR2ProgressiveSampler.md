---
url: https://docs.comfy.org/built-in-nodes/SeedVR2ProgressiveSampler/
title: SeedVR2ProgressiveSampler - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:00.695150+00:00
---

# SeedVR2ProgressiveSampler - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SeedVR2ProgressiveSampler/

Advanced

# SeedVR2ProgressiveSampler - ComfyUI Built-in Node Documentation

Copy pageCopy page

Sequential temporal chunking sampler for SeedVR2 native workflows.

Copy pageCopy page

Sequential temporal chunking sampler for SeedVR2 native workflows. This node processes long video latents by splitting them into smaller temporal chunks, sampling each chunk sequentially, and blending the results together. It serves as a drop-in replacement for the standard KSampler when working with SeedVR2 models on sequences that would otherwise cause out-of-memory errors.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The model used for denoising the input latent| MODEL| Yes|   
`seed`| The random seed used for creating the noise (default: 0)| INT| Yes| 0 to 0xffffffffffffffff  
`steps`| The number of steps used in the denoising process (default: 20)| INT| Yes| 1 to 10000  
`cfg`| The Classifier-Free Guidance scale balances creativity and adherence to the prompt. Higher values result in images more closely matching the prompt however too high values will negatively impact quality (default: 1.0)| FLOAT| Yes| 0.0 to 100.0  
`sampler_name`| The algorithm used when sampling, this can affect the quality, speed, and style of the generated output| COMBO| Yes| Multiple options available  
`scheduler`| The scheduler controls how noise is gradually removed to form the image| COMBO| Yes| Multiple options available  
`positive`| The conditioning describing the attributes you want to include in the image| CONDITIONING| Yes|   
`negative`| The conditioning describing the attributes you want to exclude from the image| CONDITIONING| Yes|   
`latent`| The latent image to denoise| LATENT| Yes|   
`denoise`| The amount of denoising applied, lower values will maintain the structure of the initial image allowing for image to image sampling (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`frames_per_chunk`| Pixel frames per temporal chunk. Must be a 4n+1 value (1, 5, 9, 13, 17, 21, …) to match SeedVR2 constraints (default: 21)| INT| Yes| 1 to 16384 (step of 4)  
`temporal_overlap`| Latent frames blended between adjacent chunks to hide the seam; 0 means no blend (default: 0)| INT| Yes| 0 to 16384  
`chunking_mode`| manual = use frames_per_chunk exactly; auto = shrink the chunk until it fits in VRAM (default: “manual”)| COMBO| Yes| ”manual"  
"auto”  
  
**Note on`frames_per_chunk`:** This parameter must be a 4n+1 pixel-frame count (1, 5, 9, 13, 17, 21, …). The node will raise an error if an invalid value is provided. **Note on`temporal_overlap`:** The overlap value is automatically capped to be at most one less than the latent chunk size to ensure valid chunk processing. **Note on`chunking_mode`:** When set to “auto”, the node will automatically try smaller chunk sizes if the current chunk causes an out-of-memory error. If all attempts fail, the node raises an error.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`latent`| The denoised latent output, concatenated from all temporal chunks back into a single collapsed SeedVR2 latent tensor| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2ProgressiveSampler/en.md)

* * *

**Source fingerprint (SHA-256):** `a4574c3e619954b5569551b5b2ba112ecbff918dcebb5ba718a14e77701144a9`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SeedVR2ProgressiveSampler.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SeedVR2ProgressiveSampler)

[OpenAIVideoSora2 - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/OpenAIVideoSora2)[StabilityAudioInpaint - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/StabilityAudioInpaint)

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
