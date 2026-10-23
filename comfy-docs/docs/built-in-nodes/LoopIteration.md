---
url: https://docs.comfy.org/built-in-nodes/LoopIteration/
title: LoopIteration - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:24.791941+00:00
---

# LoopIteration - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LoopIteration/

Advanced

# LoopIteration - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node provides iteration metadata for loop-style workflows.

Copy pageCopy page

This node provides iteration metadata for loop-style workflows. It receives list-based inputs and passes through the first element of each list, so a loop can track the current index, whether it is the first or last step, the current list item, and any running iteration value. Cache behavior is controlled by the `reuse_cache` flag. This node is marked as developer-only.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`iteration_index`| The index of the current iteration, supplied as a list. The first element is passed through to the output.| INT| Yes| -  
`is_first`| Indicates whether the current iteration is the first one, supplied as a list. The first element is passed through to the output.| BOOLEAN| Yes| -  
`is_last`| Indicates whether the current iteration is the last one, supplied as a list. The first element is passed through to the output.| BOOLEAN| Yes| -  
`list_item`| The item taken from the list for this iteration. Optional; the first element is passed through to the output when provided, otherwise None is returned.| ANY| No| -  
`current_iteration_value`| The value carried by the current iteration. Optional; when provided, the full value is passed through to the output, otherwise None is returned.| ANY| No| -  
`reuse_cache`| Controls whether the result may be reused from cache. When enabled, the node keeps a stable fingerprint so cached results can be reused. When disabled, a non-matching fingerprint is produced so the node runs again on each iteration.| BOOLEAN| Yes| -  
  
Note: This node is list-input enabled, meaning each input is expected to arrive as a list and the node outputs only the first element of each list (except `current_iteration_value`, which is passed through as a list). It also accepts additional inputs beyond those listed here.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`iteration_index`| The index of the current iteration.| INT  
`is_first`| Whether the current iteration is the first one.| BOOLEAN  
`is_last`| Whether the current iteration is the last one.| BOOLEAN  
`list_item`| The item taken from the list for this iteration, or None when no item was provided.| ANY  
`current_iteration_value`| The value carried by the current iteration, or None when no value was provided. This output is returned as a list.| ANY  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoopIteration/en.md)

* * *

**Source fingerprint (SHA-256):** `c7072f22bd382f567792d2ea7a30312c64d33c213551f8983c25cd7b95adc4fb`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LoopIteration.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LoopIteration)

[KlingVirtualTryOnNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/KlingVirtualTryOnNode)[LoopProgress - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LoopProgress)

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
