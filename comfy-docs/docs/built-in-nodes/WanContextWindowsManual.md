---
url: https://docs.comfy.org/built-in-nodes/WanContextWindowsManual/
title: WanContextWindowsManual - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:23.499983+00:00
---

# WanContextWindowsManual - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/WanContextWindowsManual/

Wan

# WanContextWindowsManual - ComfyUI Built-in Node Documentation

Copy pageCopy page

The WAN Context Windows (Manual) node lets you manually configure context windows for Wan-style video models.

Copy pageCopy page

The WAN Context Windows (Manual) node lets you manually configure context windows for Wan-style video models. It applies these settings during sampling, giving you control over the window length, overlap, scheduling, and fusion method used while the model processes video. Context length and overlap are specified in real frames and are converted internally for the model’s 2D processing.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The model to apply context windows to during sampling.| MODEL| Yes| -  
`context_length`| The length of the context window in real frames. Must be 4*n + 1 (default: 81).| INT| Yes| 1 to 16384 (MAX_RESOLUTION), step 4  
`context_overlap`| The overlap of the context window in real frames (default: 30).| INT| Yes| 0 or higher  
`context_schedule`| Step-dependent scheduling algorithm for context windows (default: “uniform_standard”).| COMBO| Yes| `"static_standard"`  
`"uniform_standard"`  
`"uniform_looped"`  
`"batched"`  
`context_stride`| The stride of the context window; only applicable to uniform schedules (default: 1).| INT| Yes| 1 or higher  
`closed_loop`| Whether to close the context window loop; only applicable to looped schedules (default: False).| BOOLEAN| Yes| -  
`fuse_method`| The method to use to fuse the context windows (default: “pyramid”).| COMBO| Yes| `"pyramid"`  
`"gaussian"`  
`"average"`  
`"overlap"`  
`freenoise`| Whether to apply FreeNoise noise shuffling, improves window blending (default: True).| BOOLEAN| Yes| -  
`retain_first_frame`| Retain the first I2V frame in every context window (may help retain initial reference) (default: False).| BOOLEAN| Yes| -  
`split_conds_to_windows`| Whether to split multiple conditionings (created by ConditionCombine) to each window based on region index (default: False).| BOOLEAN| Yes| -  
  
**Note:** `context_stride` only affects uniform schedules, and `closed_loop` only applies to looped schedules. The context length and overlap are specified in real frames and are automatically converted and clamped to minimum valid values during processing (`context_length` becomes ((length - 1) / 4) + 1, `context_overlap` becomes overlap / 4). `context_length` must follow the form 4*n + 1. `retain_first_frame` is intended for image-to-video use. `split_conds_to_windows` expects multiple conditionings created by the ConditionCombine node. The `fuse_method` parameter includes several options beyond just “pyramid”.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| The model with the applied context window configuration.| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanContextWindowsManual/en.md)

* * *

**Source fingerprint (SHA-256):** `cf4927371e9d4b509f2e6e5319cd6109e3ef36da6b3faee278bcf8c906672857`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/WanContextWindowsManual.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/WanContextWindowsManual)

[TomePatchModel - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/TomePatchModel)[WanUni3CControlnetApply - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/WanUni3CControlnetApply)

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
