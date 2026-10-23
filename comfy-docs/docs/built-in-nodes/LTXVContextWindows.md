---
url: https://docs.comfy.org/built-in-nodes/LTXVContextWindows/
title: LTXVContextWindows - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:17.784696+00:00
---

# LTXVContextWindows - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LTXVContextWindows/

Ltxv

# LTXVContextWindows - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node sets context windows for LTXV-like models during sampling.

Copy pageCopy page

This node sets context windows for LTXV-like models during sampling. It divides generation into overlapping windows to help manage memory usage and improve temporal coherence.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The model to apply context windows to during sampling.| MODEL| Yes| -  
`context_length`| The length of the context window in real frames. Must be 8*n + 1. (default: 145)| INT| Yes| Minimum: 1  
Maximum: nodes.MAX_RESOLUTION  
Step: 8  
`context_overlap`| The overlap of the context window in real frames. (default: 40)| INT| Yes| Minimum: 0  
Step: 8  
`context_schedule`| Step-dependent scheduling algorithm for context windows. (default: “UNIFORM_STANDARD”)| COMBO| Yes| `"STATIC_STANDARD"`  
`"UNIFORM_STANDARD"`  
`"UNIFORM_LOOPED"`  
`"BATCHED"`  
`context_stride`| The stride of the context window; only applicable to uniform schedules. (default: 1)| INT| Yes| Minimum: 1  
`closed_loop`| Whether to close the context window loop; only applicable to looped schedules. (default: False)| BOOLEAN| Yes| True  
False  
`fuse_method`| The method to use to fuse the context windows. Available options are defined by `ContextFuseMethods.LIST_STATIC`. (default: “PYRAMID”)| COMBO| Yes| Defined by `ContextFuseMethods.LIST_STATIC`  
`freenoise`| Whether to apply FreeNoise noise shuffling, improves window blending. (default: True)| BOOLEAN| Yes| True  
False  
`retain_first_frame`| Retain the first latent frame in every context window (may help retain initial reference). (default: False)| BOOLEAN| Yes| True  
False  
`split_conds_to_windows`| Whether to split multiple conditionings (created by ConditionCombine) to each window based on region index. (default: False)| BOOLEAN| Yes| True  
False  
  
**Note:** The `context_length` value is provided in real frames and is internally converted to latent frames using the formula `((context_length - 1) // 8) + 1`, with a minimum of 1. The `context_overlap` value is also provided in real frames and is converted to latent frames using integer division by 8, with a minimum of 0. The tooltip for `context_length` indicates it must follow the pattern 8*n + 1.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`MODEL`| The model with context windows applied for sampling.| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVContextWindows/en.md)

* * *

**Source fingerprint (SHA-256):** `148649d0a938e08c932a163f5d7614332626fba37b8f79db7f92bbcf422e692f`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LTXVContextWindows.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LTXVContextWindows)

[HiDreamO1PatchSeamSmoothing - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/HiDreamO1PatchSeamSmoothing)[ModelSamplingLTXV - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ModelSamplingLTXV)

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
