---
url: https://docs.comfy.org/built-in-nodes/CreateHookModelAsLora/
title: CreateHookModelAsLora - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:46.995145+00:00
---

# CreateHookModelAsLora - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/CreateHookModelAsLora/

Create

# CreateHookModelAsLora - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node creates a hook model as a LoRA (Low-Rank Adaptation) by loading checkpoint weights and applying strength adjustments to both the model and CLIP

Copy pageCopy page

This node creates a hook model as a LoRA (Low-Rank Adaptation) by loading checkpoint weights and applying strength adjustments to both the model and CLIP components. It allows you to apply LoRA-style modifications to existing models through a hook-based approach, enabling fine-tuning and adaptation without permanent model changes. The node can combine with previous hooks and caches loaded weights for efficiency.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`ckpt_name`| The checkpoint file to load weights from (select from available checkpoints)| STRING| Yes| Multiple options available  
`strength_model`| The strength multiplier applied to the model weights (default: 1.0)| FLOAT| Yes| -20.0 to 20.0  
`strength_clip`| The strength multiplier applied to the CLIP weights (default: 1.0)| FLOAT| Yes| -20.0 to 20.0  
`prev_hooks`| Optional previous hooks to combine with the newly created LoRA hooks| HOOKS| No| -  
  
**Parameter Constraints:**

  * The `ckpt_name` parameter loads checkpoints from the available checkpoints folder
  * Both strength parameters accept values from -20.0 to 20.0 with 0.01 step increments
  * When `prev_hooks` is not provided, the node creates a new hook group
  * The node caches loaded weights to avoid reloading the same checkpoint multiple times



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`HOOKS`| The created LoRA hooks, combined with any previous hooks if provided| HOOKS  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookModelAsLora/en.md)

* * *

**Source fingerprint (SHA-256):** `8c0dd6b2e8e99e1d7dbc864aa802c0713842fb0d4ee018ea5cbedfb7896a770d`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/CreateHookModelAsLora.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/CreateHookModelAsLora)

[CreateHookLoraModelOnly - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/CreateHookLoraModelOnly)[CreateHookModelAsLoraModelOnly - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/CreateHookModelAsLoraModelOnly)

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
