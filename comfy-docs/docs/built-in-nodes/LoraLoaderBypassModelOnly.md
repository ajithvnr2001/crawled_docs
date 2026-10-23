---
url: https://docs.comfy.org/built-in-nodes/LoraLoaderBypassModelOnly/
title: LoraLoaderBypassModelOnly - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:25.719724+00:00
---

# LoraLoaderBypassModelOnly - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LoraLoaderBypassModelOnly/

Loaders

# LoraLoaderBypassModelOnly - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node applies a LoRA (Low-Rank Adaptation) to a model to modify its behavior, but only affects the model component itself.

Copy pageCopy page

This node applies a LoRA (Low-Rank Adaptation) to a model to modify its behavior, but only affects the model component itself. It loads a specified LoRA file and adjusts the model’s weights by a given strength, leaving other components like the CLIP text encoder unchanged.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The base model to which the LoRA adjustments will be applied.| MODEL| Yes| -  
`lora_name`| The name of the LoRA file to load and apply. The options are populated from the files in the `loras` directory.| STRING| Yes| (List of available LoRA files)  
`strength_model`| The strength of the LoRA’s effect on the model’s weights. A positive value applies the LoRA, a negative value applies the inverse, and a value of 0 has no effect (default: 1.0).| FLOAT| Yes| -100.0 to 100.0  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| The modified model with the LoRA adjustments applied to its weights.| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderBypassModelOnly/en.md)

* * *

**Source fingerprint (SHA-256):** `e0e1ad2d6481a1b9771d7eae833ffab0737a967d4af6e57b946d1b2223fe45bf`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LoraLoaderBypassModelOnly.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LoraLoaderBypassModelOnly)

[LoraLoaderBypass - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LoraLoaderBypass)[LoraModelLoader - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LoraModelLoader)

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
