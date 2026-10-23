---
url: https://docs.comfy.org/built-in-nodes/UNetCrossAttentionMultiply/
title: UNetCrossAttentionMultiply - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:15.548445+00:00
---

# UNetCrossAttentionMultiply - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/UNetCrossAttentionMultiply/

Attention Experiments

# UNetCrossAttentionMultiply - ComfyUI Built-in Node Documentation

Copy pageCopy page

The UNetCrossAttentionMultiply node applies multiplication factors to the cross-attention mechanism in a UNet model.

Copy pageCopy page

The UNetCrossAttentionMultiply node applies multiplication factors to the cross-attention mechanism in a UNet model. It allows you to scale the query, key, value, and output components of the cross-attention layers to experiment with different attention behaviors and effects.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The UNet model to modify with attention scaling factors| MODEL| Yes| -  
`q`| Scaling factor for query components in cross-attention (default: 1.0)| FLOAT| No| 0.0 - 10.0  
`k`| Scaling factor for key components in cross-attention (default: 1.0)| FLOAT| No| 0.0 - 10.0  
`v`| Scaling factor for value components in cross-attention (default: 1.0)| FLOAT| No| 0.0 - 10.0  
`out`| Scaling factor for output components in cross-attention (default: 1.0)| FLOAT| No| 0.0 - 10.0  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| The modified UNet model with scaled cross-attention components| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNetCrossAttentionMultiply/en.md)

* * *

**Source fingerprint (SHA-256):** `f55a6809be88bfb32fa2c70fabd0e5bb7360be78670c9473d4a79517b811454e`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/UNetCrossAttentionMultiply.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/UNetCrossAttentionMultiply)

[CLIPAttentionMultiply - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/CLIPAttentionMultiply)[UNetSelfAttentionMultiply - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/UNetSelfAttentionMultiply)

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
