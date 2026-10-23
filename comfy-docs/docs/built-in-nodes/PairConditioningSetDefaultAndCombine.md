---
url: https://docs.comfy.org/built-in-nodes/PairConditioningSetDefaultAndCombine/
title: PairConditioningSetDefaultAndCombine - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:40.935333+00:00
---

# PairConditioningSetDefaultAndCombine - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/PairConditioningSetDefaultAndCombine/

Cond Pair

# PairConditioningSetDefaultAndCombine - ComfyUI Built-in Node Documentation

Copy pageCopy page

The PairConditioningSetDefaultAndCombine node sets default conditioning values and combines them with input conditioning data.

Copy pageCopy page

The **PairConditioningSetDefaultAndCombine** node sets default conditioning values and combines them with input conditioning data. It takes positive and negative conditioning inputs along with their default counterparts, then processes them through ComfyUI’s hook system to produce final conditioning outputs that incorporate the default values.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`positive`| The primary positive conditioning input to be processed| CONDITIONING| Yes| -  
`negative`| The primary negative conditioning input to be processed| CONDITIONING| Yes| -  
`positive_DEFAULT`| The default positive conditioning values to be used as fallback| CONDITIONING| Yes| -  
`negative_DEFAULT`| The default negative conditioning values to be used as fallback| CONDITIONING| Yes| -  
`hooks`| Optional hook group for custom processing logic| HOOKS| No| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| The processed positive conditioning with default values incorporated| CONDITIONING  
`negative`| The processed negative conditioning with default values incorporated| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetDefaultAndCombine/en.md)

* * *

**Source fingerprint (SHA-256):** `dfa47d0fe02e81db8b68d20ae9b765c2518773f4f7fc8caf774cb870267dbb21`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/PairConditioningSetDefaultAndCombine.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/PairConditioningSetDefaultAndCombine)

[PairConditioningCombine - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/PairConditioningCombine)[PairConditioningSetProperties - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/PairConditioningSetProperties)

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
