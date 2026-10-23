---
url: https://docs.comfy.org/built-in-nodes/GetICLoRAParameters/
title: GetICLoRAParameters - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:00.993917+00:00
---

# GetICLoRAParameters - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/GetICLoRAParameters/

Ltxv

# GetICLoRAParameters - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node reads the metadata from a LoRA-loaded model to extract IC-LoRA parameters, such as the reference downscale factor.

Copy pageCopy page

This node reads the metadata from a LoRA-loaded model to extract IC-LoRA parameters, such as the reference downscale factor. It outputs these parameters as a structured object that can be connected to the LTXVAddGuide node when a LoRA requires special handling of the guides.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`iclora_model`| Direct output from a LoRA Loader for the specific IC-LoRA from which to extract the metadata.| MODEL| Yes| N/A  
  
Note: If the LoRA metadata is missing or does not contain a `reference_downscale_factor` entry, the node outputs a default value of 1. When present, the factor is rounded and set to a minimum of 1.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`iclora_parameters`| IC-LoRA parameters extracted from the LoRA metadata (e.g., reference_downscale_factor). Connect to LTXVAddGuide if the LoRA requires special handling of the guides.| IC_LORA_PARAMETERS  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetICLoRAParameters/en.md)

* * *

**Source fingerprint (SHA-256):** `5f6becad0c7673b8cde1e099bd7ba5be7106da958b8967f8e693ba2a704baaef`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/GetICLoRAParameters.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/GetICLoRAParameters)

[LotusConditioning - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LotusConditioning)[LTXVAddGeneratedKeyframes - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LTXVAddGeneratedKeyframes)

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
