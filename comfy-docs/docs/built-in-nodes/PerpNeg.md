---
url: https://docs.comfy.org/built-in-nodes/PerpNeg/
title: PerpNeg - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:41.157850+00:00
---

# PerpNeg - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/PerpNeg/

Experimental

# PerpNeg - ComfyUI Built-in Node Documentation

Copy pageCopy page

The PerpNeg node applies perpendicular negative guidance to a model’s sampling process.

Copy pageCopy page

The PerpNeg node applies perpendicular negative guidance to a model’s sampling process. This node modifies the model’s configuration function to adjust noise predictions using negative conditioning and scaling factors. It has been deprecated and replaced by the PerpNegGuider node for improved functionality.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The model to apply perpendicular negative guidance to| MODEL| Yes| -  
`empty_conditioning`| Empty conditioning used for negative guidance calculations| CONDITIONING| Yes| -  
`neg_scale`| Scaling factor for negative guidance (default: 1.0)| FLOAT| No| 0.0 - 100.0  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| The modified model with perpendicular negative guidance applied| MODEL  
  
**Note** : This node is deprecated and has been replaced by PerpNegGuider. It is marked as experimental and should not be used in production workflows.

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerpNeg/en.md)

* * *

**Source fingerprint (SHA-256):** `016bd9a9a9ee42855c15b3e582ada03557297df9a786d977439edd9d3363a5ba`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/PerpNeg.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/PerpNeg)

[Mahiro - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Mahiro)[PerpNegGuider - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/PerpNegGuider)

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
