---
url: https://docs.comfy.org/built-in-nodes/CLIPAttentionMultiply/
title: CLIPAttentionMultiply - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:32.565182+00:00
---

# CLIPAttentionMultiply - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/CLIPAttentionMultiply/

Attention Experiments

# CLIPAttentionMultiply - ComfyUI Built-in Node Documentation

Copy pageCopy page

The CLIPAttentionMultiply node allows you to adjust the attention mechanism in CLIP models by applying multiplication factors to different components

Copy pageCopy page

The CLIPAttentionMultiply node allows you to adjust the attention mechanism in CLIP models by applying multiplication factors to different components of the self-attention layers. It works by modifying the query, key, value, and output projection weights and biases in the CLIP model’s attention mechanism. This experimental node creates a modified copy of the input CLIP model with the specified scaling factors applied.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`clip`| The CLIP model to modify| CLIP| Yes| -  
`q`| Multiplication factor for query projection weights and biases (default: 1.0)| FLOAT| Yes| 0.0 - 10.0  
`k`| Multiplication factor for key projection weights and biases (default: 1.0)| FLOAT| Yes| 0.0 - 10.0  
`v`| Multiplication factor for value projection weights and biases (default: 1.0)| FLOAT| Yes| 0.0 - 10.0  
`out`| Multiplication factor for output projection weights and biases (default: 1.0)| FLOAT| Yes| 0.0 - 10.0  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`CLIP`| Returns a modified CLIP model with the specified attention scaling factors applied| CLIP  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPAttentionMultiply/en.md)

* * *

**Source fingerprint (SHA-256):** `1f5c437cb4a372dfd69ad3c10e2b8cfc68821e0fe82dcf37df5e6fd64aa0b436`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/CLIPAttentionMultiply.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/CLIPAttentionMultiply)

[Sd4xupscaleConditioning - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Sd4xupscaleConditioning)[UNetCrossAttentionMultiply - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/UNetCrossAttentionMultiply)

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
