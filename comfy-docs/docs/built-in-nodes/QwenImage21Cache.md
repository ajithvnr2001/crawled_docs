---
url: https://docs.comfy.org/built-in-nodes/QwenImage21Cache/
title: QwenImage21Cache - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:46.257652+00:00
---

# QwenImage21Cache - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/QwenImage21Cache/

Qwen Image

# QwenImage21Cache - ComfyUI Built-in Node Documentation

Copy pageCopy page

The QwenImage21Cache node configures the KV prefix cache of the Qwen-Image 2.1 model: where the cached keys and values are stored and at what precision.

Copy pageCopy page

The QwenImage21Cache node configures the KV prefix cache of the Qwen-Image 2.1 model: where the cached keys and values are stored and at what precision. Text and reference tokens are computed once and reused across sampling steps, which is where most of the speedup on edit workflows comes from, and this node lets you trade memory for speed or rule the cache out entirely. This node is marked as experimental.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The Qwen-Image 2.1 model whose prefix cache is configured.| MODEL| Yes| -  
`device`| Where the cached keys and values are stored. `"auto"` (default) uses spare VRAM first and then RAM; `"gpu"` stores the cache in VRAM; `"cpu"` stores it in RAM and prefetches it behind compute, which costs little speed; `"off"` recomputes the prefix every step, which is slower but is the only way to rule the cache out.| COMBO| Yes| `"auto"`  
`"gpu"`  
`"cpu"`  
`"off"`  
`dtype`| Storage precision of the cache. `"default"` is lossless; `"int8"` halves the cache at about bf16 accuracy; `"int4"` quarters it but roughly doubles the per-step error.| COMBO| Yes| `"default"`  
`"int8"`  
`"int4"`  
  
When the cache does not fit, the model recomputes the prefix instead of evicting the other branch’s slot, so an oversized setting degrades speed rather than failing the run.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`MODEL`| The model with the cache device and precision applied, ready to be sampled.| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImage21Cache/en.md)

* * *

**Source fingerprint (SHA-256):** `0c10cdb465d1ee4063273ffbb4913def3830f7e329694cd0a2e292d6f3c37ae4`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/QwenImage21Cache.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/QwenImage21Cache)

[CLIPTextEncodePixArtAlpha - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/CLIPTextEncodePixArtAlpha)[TextEncodeQwenImage21 - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/TextEncodeQwenImage21)

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
