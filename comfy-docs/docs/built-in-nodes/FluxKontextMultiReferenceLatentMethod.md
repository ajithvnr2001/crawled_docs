---
url: https://docs.comfy.org/built-in-nodes/FluxKontextMultiReferenceLatentMethod/
title: FluxKontextMultiReferenceLatentMethod - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-25T12:24:52.091423+00:00
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
`"index_timestep_zero_isolated"`  
`"index_timestep_zero_text_start"`  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`conditioning`| The modified conditioning data with the reference latents method applied| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextMultiReferenceLatentMethod/en.md)

* * *

**Source fingerprint (SHA-256):** `de2e3d34f9e47a90ff37300489bffef8082eb92deefbc2ce338b17b0d853ac77`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/FluxKontextMultiReferenceLatentMethod.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/FluxKontextMultiReferenceLatentMethod)

[FluxKontextImageScale](https://docs.comfy.org/built-in-nodes/FluxKontextImageScale)[GLIGENTextBoxApply](https://docs.comfy.org/built-in-nodes/GLIGENTextBoxApply)
