---
url: https://docs.comfy.org/built-in-nodes/ConditioningSetDefaultCombine/
title: ConditioningSetDefaultCombine - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-25T12:24:46.862898+00:00
---

# ConditioningSetDefaultCombine - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ConditioningSetDefaultCombine/

Hooks

# ConditioningSetDefaultCombine - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node combines a primary conditioning input with a default conditioning input using a hook-based system.

Copy pageCopy page

This node combines a primary conditioning input with a default conditioning input using a hook-based system. It merges the two conditioning sources into a single output, allowing the default conditioning to serve as a fallback or base when the primary conditioning is incomplete.

## 

​

Inputs

Parameter| Description| Data Type| Input Type| Default| Range  
---|---|---|---|---|---  
`cond`| The primary conditioning input to be processed and combined| CONDITIONING| Required| -| -  
`cond_DEFAULT`| The default conditioning data to be combined with the primary conditioning| CONDITIONING| Required| -| -  
`hooks`| Optional hook configuration that controls how the conditioning data is processed and combined| HOOKS| Optional| -| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`CONDITIONING`| The combined conditioning data resulting from merging the primary and default conditioning inputs| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetDefaultCombine/en.md)

* * *

**Source fingerprint (SHA-256):** `5e6c95f454c7e262878cc362c6b199e01abff10f803c81afe6e76a317c30d039`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ConditioningSetDefaultCombine.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ConditioningSetDefaultCombine)

[CombineHooks8](https://docs.comfy.org/built-in-nodes/CombineHooks8)[PairConditioningSetDefaultCombine](https://docs.comfy.org/built-in-nodes/PairConditioningSetDefaultCombine)
