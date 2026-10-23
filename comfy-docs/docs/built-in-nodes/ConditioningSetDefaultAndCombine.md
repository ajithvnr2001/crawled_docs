---
url: https://docs.comfy.org/built-in-nodes/ConditioningSetDefaultAndCombine/
title: ConditioningSetDefaultAndCombine - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:42.245858+00:00
---

# ConditioningSetDefaultAndCombine - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ConditioningSetDefaultAndCombine/

Cond Single

# ConditioningSetDefaultAndCombine - ComfyUI Built-in Node Documentation

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
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetDefaultAndCombine/en.md)

* * *

**Source fingerprint (SHA-256):** `5e6c95f454c7e262878cc362c6b199e01abff10f803c81afe6e76a317c30d039`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ConditioningSetDefaultAndCombine.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ConditioningSetDefaultAndCombine)

[PairConditioningSetPropertiesAndCombine - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/PairConditioningSetPropertiesAndCombine)[ConditioningSetProperties - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ConditioningSetProperties)

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
