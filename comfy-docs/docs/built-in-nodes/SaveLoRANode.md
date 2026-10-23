---
url: https://docs.comfy.org/built-in-nodes/SaveLoRANode/
title: SaveLoRANode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:59.455047+00:00
---

# SaveLoRANode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SaveLoRANode/

Model Merging

# SaveLoRANode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The SaveLoRA node saves LoRA (Low-Rank Adaptation) models to your output directory.

Copy pageCopy page

The SaveLoRA node saves LoRA (Low-Rank Adaptation) models to your output directory. It takes a LoRA model as input and creates a safetensors file with an automatically generated filename. You can customize the filename prefix and optionally include the training step count in the filename for better organization.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`lora`| The LoRA model to save. Do not use the model with LoRA layers.| LORA_MODEL| Yes| -  
`prefix`| The prefix to use for the saved LoRA file (default: “loras/ComfyUI_trained_lora”).| STRING| Yes| -  
`steps`| Optional: The number of steps the LoRA has been trained for, used to name the saved file.| INT| No| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
 _None_|  This node does not return any outputs but saves the LoRA model to the output directory.| -  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLoRANode/en.md)

* * *

**Source fingerprint (SHA-256):** `06a1067433aa4b720b51050b09fbad4870caf12c5e92f788d44ea022a39efef4`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SaveLoRANode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SaveLoRANode)

[DeprecatedDiffusersLoader - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/DeprecatedDiffusersLoader)[MultiGPU_Options - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/MultiGPU_Options)

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
