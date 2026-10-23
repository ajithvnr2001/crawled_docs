---
url: https://docs.comfy.org/built-in-nodes/SeedVR2TemporalMerge/
title: SeedVR2TemporalMerge - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:01.163647+00:00
---

# SeedVR2TemporalMerge - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SeedVR2TemporalMerge/

Seedvr

# SeedVR2TemporalMerge - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node recombines sampled SeedVR2 latent temporal chunks into a single full-length latent.

Copy pageCopy page

This node recombines sampled SeedVR2 latent temporal chunks into a single full-length latent. When a temporal overlap is specified, it crossfades each overlapping region with a Hann window to create smooth transitions between chunks; when the overlap is 0, it performs plain concatenation.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`latents`| The sampled temporal chunks in sequence order.| LATENT| Yes| List of latents  
`temporal_overlap`| The temporal_overlap output of Split SeedVR2 Latent. 0 = plain concatenation. (default: 0)| INT| Yes| 0 to 16384  
  
**Note:** The `temporal_overlap` value must be greater than or equal to 0. All chunks must be 5-dimensional video latents (B, C, T, H, W) and must match in every dimension except the temporal axis (T); only the final chunk may be shorter than the others. If only one chunk is provided, it is returned unchanged.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`latent`| The recombined full-length latent.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2TemporalMerge/en.md)

* * *

**Source fingerprint (SHA-256):** `647653fc651462f62bcc9dca2919cfcaa4b476b4c679b0a1111698facab83f28`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SeedVR2TemporalMerge.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SeedVR2TemporalMerge)

[SeedVR2TemporalChunk - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SeedVR2TemporalChunk)[StableCascade_EmptyLatentImage - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/StableCascade_EmptyLatentImage)

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
