---
url: https://docs.comfy.org/built-in-nodes/LatentApplyOperationCFG/
title: LatentApplyOperationCFG - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:20.097869+00:00
---

# LatentApplyOperationCFG - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LatentApplyOperationCFG/

Operations

# LatentApplyOperationCFG - ComfyUI Built-in Node Documentation

Copy pageCopy page

The LatentApplyOperationCFG node applies a latent operation inside the classifier-free guidance (CFG) step of a model’s sampling process.

Copy pageCopy page

The LatentApplyOperationCFG node applies a latent operation inside the classifier-free guidance (CFG) step of a model’s sampling process. It intercepts the conditioning outputs produced before CFG, applies the connected operation to the latent values, and returns the model with this modified sampling behavior.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The model to which the CFG operation will be applied| MODEL| Yes| -  
`operation`| The latent operation to apply during the CFG sampling process| LATENT_OPERATION| Yes| -  
`start_percent`| Fraction of the denoising schedule at which the operation starts being applied; 0 is the beginning of the schedule (default: 0.0)| FLOAT| No| 0.0 to 1.0 (step 0.001)  
`end_percent`| Fraction of the denoising schedule at which the operation stops being applied; 1 is the end of the schedule (default: 1.0)| FLOAT| No| 0.0 to 1.0 (step 0.001)  
  
Note: This node is marked as experimental. The operation is applied to the model’s conditioning outputs during the CFG sampling process. When two conditioning outputs are present, the operation is applied to the difference between the first and second output, and the second output is added back to the result. When only one conditioning output is present, the operation is applied directly to it. The operation only runs between the `start_percent` and `end_percent` points of the denoising schedule, so it can be limited to part of the schedule; outside that window the conditioning outputs are returned unchanged.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| The modified model with the CFG operation applied to its sampling process| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperationCFG/en.md)

* * *

**Source fingerprint (SHA-256):** `6a5f59f02eaec38334c63d871e48e89aa983a5ac2ca10801161cdc9e13cacdf2`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LatentApplyOperationCFG.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LatentApplyOperationCFG)

[LatentApplyOperation - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LatentApplyOperation)[LatentOperationBlend - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LatentOperationBlend)

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
