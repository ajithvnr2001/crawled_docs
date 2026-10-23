---
url: https://docs.comfy.org/built-in-nodes/PairConditioningCombine/
title: PairConditioningCombine - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:40.453579+00:00
---

# PairConditioningCombine - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/PairConditioningCombine/

Cond Pair

# PairConditioningCombine - ComfyUI Built-in Node Documentation

Copy pageCopy page

The PairConditioningCombine node merges two separate conditioning pairs (each consisting of a positive and negative conditioning) into a single combined pair.

Copy pageCopy page

The PairConditioningCombine node merges two separate conditioning pairs (each consisting of a positive and negative conditioning) into a single combined pair. It takes the positive and negative conditioning from two different sources and combines them using ComfyUI’s internal logic, outputting one final positive and one final negative conditioning. This node is experimental and designed for advanced conditioning manipulation workflows.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`positive_A`| First positive conditioning input| CONDITIONING| Yes| -  
`negative_A`| First negative conditioning input| CONDITIONING| Yes| -  
`positive_B`| Second positive conditioning input| CONDITIONING| Yes| -  
`negative_B`| Second negative conditioning input| CONDITIONING| Yes| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| Combined positive conditioning output| CONDITIONING  
`negative`| Combined negative conditioning output| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningCombine/en.md)

* * *

**Source fingerprint (SHA-256):** `34c14207930ba31fea054b2e641e9666e738ed786aa117449c4a27667bde41b1`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/PairConditioningCombine.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/PairConditioningCombine)

[CombineHooksFour - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/CombineHooksFour)[PairConditioningSetDefaultAndCombine - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/PairConditioningSetDefaultAndCombine)

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
