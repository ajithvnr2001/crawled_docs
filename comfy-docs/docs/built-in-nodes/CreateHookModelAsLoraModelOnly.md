---
url: https://docs.comfy.org/built-in-nodes/CreateHookModelAsLoraModelOnly/
title: CreateHookModelAsLoraModelOnly - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:47.401914+00:00
---

# CreateHookModelAsLoraModelOnly - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/CreateHookModelAsLoraModelOnly/

Create

# CreateHookModelAsLoraModelOnly - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node creates a hook that applies a LoRA (Low-Rank Adaptation) model to modify only the model component of a neural network.

Copy pageCopy page

This node creates a hook that applies a LoRA (Low-Rank Adaptation) model to modify only the model component of a neural network. It loads a checkpoint file and applies it with a specified strength to the model while leaving the CLIP component unchanged. This is an experimental node that extends the functionality of the base CreateHookModelAsLora class.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`ckpt_name`| The checkpoint file to load as a LoRA model. Available options depend on the checkpoints folder contents.| STRING| Yes| Multiple options available  
`strength_model`| The strength multiplier for applying the LoRA to the model component (default: 1.0)| FLOAT| Yes| -20.0 to 20.0  
`prev_hooks`| Optional previous hooks to chain with this hook| HOOKS| No| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`hooks`| The created hook group containing the LoRA model modification| HOOKS  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookModelAsLoraModelOnly/en.md)

* * *

**Source fingerprint (SHA-256):** `adbeaede65aa89d48c59225ca1c8edc4c9394a364f93a00dae4a83a2270f093b`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/CreateHookModelAsLoraModelOnly.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/CreateHookModelAsLoraModelOnly)

[CreateHookModelAsLora - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/CreateHookModelAsLora)[SetModelHooksOnCond - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SetModelHooksOnCond)

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
