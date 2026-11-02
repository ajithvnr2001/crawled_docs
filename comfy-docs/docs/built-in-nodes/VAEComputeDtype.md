---
url: https://docs.comfy.org/built-in-nodes/VAEComputeDtype/
title: VAEComputeDtype - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-02T16:54:33.606216+00:00
---

# VAEComputeDtype - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/VAEComputeDtype/

Debug

# VAEComputeDtype - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node sets the compute dtype used when a VAE encodes or decodes, without changing the rest of the model graph.

Copy pageCopy page

This node sets the compute dtype used when a VAE encodes or decodes, without changing the rest of the model graph. It returns a copy of the input VAE with the requested precision, so a workflow can run one branch at a higher precision while others stay unchanged. “default” keeps whatever compute dtype the input VAE already uses.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`vae`| VAE to adjust. The node works on a copy, so the connected VAE is not modified.| VAE| Yes| -  
`dtype`| Compute dtype for VAE encoding and decoding. “default” keeps the input VAE’s compute dtype (default: “default”).| COMBO| Yes| ”default"  
"fp32"  
"fp16"  
"bf16”  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`vae`| The copy of the VAE with the selected compute dtype applied.| VAE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEComputeDtype/en.md)

* * *

**Source fingerprint (SHA-256):** `239e5829d76b4bd43ec300fc2b7c8c408b5bd4a93918da417ecf43817aee3e12`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/VAEComputeDtype.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/VAEComputeDtype)

[ModelComputeDtype](https://docs.comfy.org/built-in-nodes/ModelComputeDtype)[CFGNorm](https://docs.comfy.org/built-in-nodes/CFGNorm)
