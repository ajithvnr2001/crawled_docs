---
url: https://docs.comfy.org/built-in-nodes/UNetTemporalAttentionMultiply/
title: UNetTemporalAttentionMultiply - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:15.472587+00:00
---

# UNetTemporalAttentionMultiply - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/UNetTemporalAttentionMultiply/

Attention Experiments

# UNetTemporalAttentionMultiply - ComfyUI Built-in Node Documentation

Copy pageCopy page

The UNetTemporalAttentionMultiply node applies multiplication factors to different types of attention mechanisms in a temporal UNet model.

Copy pageCopy page

The UNetTemporalAttentionMultiply node applies multiplication factors to different types of attention mechanisms in a temporal UNet model. It modifies the model by adjusting the weights of self-attention and cross-attention layers, distinguishing between structural and temporal components. This allows fine-tuning of how much influence each attention type has on the model’s output.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The input model to modify with attention multipliers| MODEL| Yes| -  
`self_structural`| Multiplier for self-attention structural components (default: 1.0)| FLOAT| No| 0.0 - 10.0  
`self_temporal`| Multiplier for self-attention temporal components (default: 1.0)| FLOAT| No| 0.0 - 10.0  
`cross_structural`| Multiplier for cross-attention structural components (default: 1.0)| FLOAT| No| 0.0 - 10.0  
`cross_temporal`| Multiplier for cross-attention temporal components (default: 1.0)| FLOAT| No| 0.0 - 10.0  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| The modified model with adjusted attention weights| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNetTemporalAttentionMultiply/en.md)

* * *

**Source fingerprint (SHA-256):** `b43c7c51cbc71349dd267c4abe1704899a394e205a60a13b45869f690d83a0f0`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/UNetTemporalAttentionMultiply.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/UNetTemporalAttentionMultiply)

[UNetSelfAttentionMultiply - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/UNetSelfAttentionMultiply)[StableCascade_SuperResolutionControlnet - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/StableCascade_SuperResolutionControlnet)

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
