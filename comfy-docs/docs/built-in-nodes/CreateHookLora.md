---
url: https://docs.comfy.org/built-in-nodes/CreateHookLora/
title: CreateHookLora - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:46.522174+00:00
---

# CreateHookLora - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/CreateHookLora/

Create

# CreateHookLora - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Create Hook LoRA node generates hook objects for applying LoRA (Low-Rank Adaptation) modifications to models.

Copy pageCopy page

The Create Hook LoRA node generates hook objects for applying LoRA (Low-Rank Adaptation) modifications to models. It loads a specified LoRA file and creates hooks that can adjust model and CLIP strengths, then combines these hooks with any existing hooks passed to it. The node efficiently manages LoRA loading by caching previously loaded LoRA files to avoid redundant operations.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`lora_name`| The name of the LoRA file to load from the loras directory| STRING| Yes| Multiple options available  
`strength_model`| The strength multiplier for model adjustments (default: 1.0)| FLOAT| Yes| -20.0 to 20.0  
`strength_clip`| The strength multiplier for CLIP adjustments (default: 1.0)| FLOAT| Yes| -20.0 to 20.0  
`prev_hooks`| Optional existing hook group to combine with the new LoRA hooks| HOOKS| No| N/A  
  
**Parameter Constraints:**

  * If both `strength_model` and `strength_clip` are set to 0, the node will skip creating new LoRA hooks and return the existing hooks unchanged
  * The node caches the last loaded LoRA file to optimize performance when the same LoRA is used repeatedly



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`HOOKS`| A hook group containing the combined LoRA hooks and any previous hooks| HOOKS  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookLora/en.md)

* * *

**Source fingerprint (SHA-256):** `42d5d776bfc9b239191952e2bce23513d183f904fc3c15039469381a547486f8`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/CreateHookLora.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/CreateHookLora)

[ConditioningSetPropertiesAndCombine - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ConditioningSetPropertiesAndCombine)[CreateHookLoraModelOnly - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/CreateHookLoraModelOnly)

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
