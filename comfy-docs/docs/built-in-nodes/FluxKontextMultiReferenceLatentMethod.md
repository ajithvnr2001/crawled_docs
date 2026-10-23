---
url: https://docs.comfy.org/built-in-nodes/FluxKontextMultiReferenceLatentMethod/
title: FluxKontextMultiReferenceLatentMethod - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:57.291101+00:00
---

# FluxKontextMultiReferenceLatentMethod - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/FluxKontextMultiReferenceLatentMethod/

FLUX

# FluxKontextMultiReferenceLatentMethod - ComfyUI Built-in Node Documentation

Copy pageCopy page

The FluxKontextMultiReferenceLatentMethod node updates conditioning data by storing a chosen reference latents method inside it.

Copy pageCopy page

The FluxKontextMultiReferenceLatentMethod node updates conditioning data by storing a chosen reference latents method inside it. The stored method is then used when reference latents are handled in later generation steps. This node is marked as experimental and belongs to the Flux conditioning system.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`conditioning`| The conditioning data to be modified with the reference latents method| CONDITIONING| Yes| -  
`reference_latents_method`| The method used for reference latents processing. If a value containing “uxo” or “uso” is selected, it is converted to “uxo” before being stored. This parameter is marked as advanced.| COMBO| Yes| `"offset"`  
`"index"`  
`"uxo/uno"`  
`"index_timestep_zero"`  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`conditioning`| The modified conditioning data with the reference latents method applied| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextMultiReferenceLatentMethod/en.md)

* * *

**Source fingerprint (SHA-256):** `cbe069d0c9f8adbf7f8c909b1cd644d9cd3730e934f0e5856213ff06fa8ecc56`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/FluxKontextMultiReferenceLatentMethod.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/FluxKontextMultiReferenceLatentMethod)

[FluxKontextImageScale - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/FluxKontextImageScale)[GLIGENTextBoxApply - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/GLIGENTextBoxApply)

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
