---
url: https://docs.comfy.org/built-in-nodes/ModelAttentionBackend/
title: ModelAttentionBackend - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:34.233526+00:00
---

# ModelAttentionBackend - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ModelAttentionBackend/

Patch

# ModelAttentionBackend - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node selects the dense attention implementation for a model, clones the model, applies the chosen backend, and returns the patched clone.

Copy pageCopy page

This node selects the dense attention implementation for a model, clones the model, applies the chosen backend, and returns the patched clone. When used with Block Sparse Attention, this backend is used whenever sparse attention is inactive or unsupported. If the selected backend is unavailable, the node automatically falls back to PyTorch attention.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The model to patch.| MODEL| Yes|   
`attention`| The dense attention backend to apply. Comfy Kitchen attention uses quantized INT8 attention and is available only on Nvidia and AMD GPUs. Default: “pytorch attention”. If the selected backend is unavailable, PyTorch attention is used as a fallback.| COMBO| Yes| ”pytorch attention"  
"comfy kitchen attention”  
  
Note: The “comfy kitchen attention” option is only listed when the Comfy Kitchen INT8 attention module is available in the current environment.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| A clone of the input model with the selected attention backend applied.| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelAttentionBackend/en.md)

* * *

**Source fingerprint (SHA-256):** `4f6e4800c2a3bb09b47b7c8f0481e1b6de3070f57234e610df5d3ce60dfdb309`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ModelAttentionBackend.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ModelAttentionBackend)

[ContextWindowsManual - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ContextWindowsManual)[ModelNoiseScale - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ModelNoiseScale)

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
