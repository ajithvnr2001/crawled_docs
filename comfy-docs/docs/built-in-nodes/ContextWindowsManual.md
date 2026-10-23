---
url: https://docs.comfy.org/built-in-nodes/ContextWindowsManual/
title: ContextWindowsManual - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:42.919090+00:00
---

# ContextWindowsManual - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ContextWindowsManual/

Patch

# ContextWindowsManual - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Context Windows (Manual) node allows you to manually configure context windows for a model during sampling

Copy pageCopy page

The Context Windows (Manual) node allows you to manually configure context windows for a model during sampling, creating overlapping context segments with a specified length, overlap, and scheduling pattern so data is processed in manageable chunks while maintaining continuity between segments. It provides advanced options for controlling how context windows are applied, including noise shuffling, conditioning retention, and causal window fixes. This node is experimental.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The model to apply context windows to during sampling.| MODEL| Yes| -  
`context_length`| The length of the context window (default: 16).| INT| Yes| 1+  
`context_overlap`| The overlap of the context window (default: 4).| INT| Yes| 0+  
`context_schedule`| Step-dependent scheduling algorithm for context windows (default: STATIC_STANDARD).| COMBO| Yes| `STATIC_STANDARD`  
`UNIFORM_STANDARD`  
`UNIFORM_LOOPED`  
`BATCHED`  
`context_stride`| The stride of the context window; only applicable to uniform schedules (default: 1).| INT| Yes| 1+  
`closed_loop`| Whether to close the context window loop; only applicable to looped schedules (default: False).| BOOLEAN| Yes| -  
`fuse_method`| The method to use to fuse the context windows (default: PYRAMID).| COMBO| Yes| Static fuse methods (see `ContextFuseMethods.LIST_STATIC`)  
`dim`| The dimension to apply the context windows to (default: 0).| INT| Yes| 0-5  
`freenoise`| Whether to apply FreeNoise noise shuffling, improves window blending (default: False).| BOOLEAN| Yes| -  
`cond_retain_index_list`| List of latent indices to retain in the conditioning tensors for each window. For concat-style I2V models (e.g. Wan I2V, HunyuanVideo I2V, Cosmos I2V, SVD) the encoded start image lives in the c_concat conditioning channels; setting this to ‘0’ will retain that start image content at sub-pos 0 of every window (default: "").| STRING| No| -  
`split_conds_to_windows`| Whether to split multiple conditionings (created by ConditionCombine) to each window based on region index (default: False).| BOOLEAN| No| -  
`latent_retain_index_list`| List of latent indices to retain in the noise latent itself for each window. Use for workflows where reference content (e.g. a start image) lives directly in the noise latent rather than in separate conditioning channels (e.g. inplace-style I2V like LTXV, AnimateDiff). Independent of cond_retain_index_list (default: "").| STRING| No| -  
`causal_window_fix`| Whether to add a causal fix frame to non-0-indexed context windows (default: True).| BOOLEAN| No| -  
  
**Parameter Constraints:**

  * `context_stride` is only used when a uniform schedule is selected (`UNIFORM_STANDARD` or `UNIFORM_LOOPED`).
  * `closed_loop` is only applicable to looped schedules (`UNIFORM_LOOPED`).
  * `dim` must be between 0 and 5 inclusive.
  * `cond_retain_index_list` and `latent_retain_index_list` expect a comma-separated list of integer indices as a string (e.g., “0,1,2”).
  * `latent_retain_index_list` is independent of `cond_retain_index_list`.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| The model with context windows applied during sampling.| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ContextWindowsManual/en.md)

* * *

**Source fingerprint (SHA-256):** `39dc39ece3d3c10c13ca8c4b85af4fbbebbcaba8a019145a6d4727c3df7b302b`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ContextWindowsManual.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ContextWindowsManual)

[BlockSparseAttention - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/BlockSparseAttention)[ModelAttentionBackend - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ModelAttentionBackend)

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
