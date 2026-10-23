---
url: https://docs.comfy.org/built-in-nodes/CombineHooksFour/
title: CombineHooksFour - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:28.543757+00:00
---

# CombineHooksFour - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/CombineHooksFour/

Combine

# CombineHooksFour - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Combine Hooks [4] node merges up to four separate hook groups into a single combined hook group.

Copy pageCopy page

The Combine Hooks [4] node merges up to four separate hook groups into a single combined hook group. It takes any combination of the four available hook inputs and combines them using ComfyUI’s hook combination system. This allows you to consolidate multiple hook configurations for streamlined processing in advanced workflows.

## 

​

Inputs

Parameter| Description| Data Type| Input Type| Default| Range  
---|---|---|---|---|---  
`hooks_A`| First hook group to combine| HOOKS| optional| None| -  
`hooks_B`| Second hook group to combine| HOOKS| optional| None| -  
`hooks_C`| Third hook group to combine| HOOKS| optional| None| -  
`hooks_D`| Fourth hook group to combine| HOOKS| optional| None| -  
  
**Note:** All four hook inputs are optional. The node will combine only the hook groups that are provided, and will return an empty hook group if no inputs are connected.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`HOOKS`| Combined hook group containing all provided hook configurations| HOOKS  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CombineHooksFour/en.md)

* * *

**Source fingerprint (SHA-256):** `92a8038e7b5a7491afcbd48830a1e278fe4d697321fb874821ebf7edd09d5815`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/CombineHooksFour.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/CombineHooksFour)

[CombineHooksEight - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/CombineHooksEight)[PairConditioningCombine - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/PairConditioningCombine)

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
