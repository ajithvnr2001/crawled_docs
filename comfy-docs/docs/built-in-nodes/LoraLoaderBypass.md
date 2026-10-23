---
url: https://docs.comfy.org/built-in-nodes/LoraLoaderBypass/
title: LoraLoaderBypass - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:25.827952+00:00
---

# LoraLoaderBypass - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LoraLoaderBypass/

Loaders

# LoraLoaderBypass - ComfyUI Built-in Node Documentation

Copy pageCopy page

The LoraLoaderBypass node applies a LoRA (Low-Rank Adaptation) to a diffusion model and a CLIP model in a special “bypass” mode.

Copy pageCopy page

The LoraLoaderBypass node applies a LoRA (Low-Rank Adaptation) to a diffusion model and a CLIP model in a special “bypass” mode. Unlike a standard LoRA loader, this method does not permanently modify the base model’s weights. Instead, it computes the result by adding the LoRA’s contribution to the model’s normal forward pass, which is useful for training or when working with models that have their weights offloaded.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The diffusion model the LoRA will be applied to.| MODEL| Yes| -  
`clip`| The CLIP model the LoRA will be applied to.| CLIP| Yes| -  
`lora_name`| The name of the LoRA. Available LoRA files are loaded from the `loras` folder.| COMBO| Yes| List of available LoRA files  
`strength_model`| How strongly to modify the diffusion model. This value can be negative (default: 1.0).| FLOAT| Yes| -100.0 to 100.0 (step: 0.01)  
`strength_clip`| How strongly to modify the CLIP model. This value can be negative (default: 1.0).| FLOAT| Yes| -100.0 to 100.0 (step: 0.01)  
  
**Note:** If both `strength_model` and `strength_clip` are set to 0, the node returns the original, unmodified `model` and `clip` inputs without processing. **Note:** The selected LoRA file is cached after it is first loaded. It is only re-read from disk when a different `lora_name` is chosen.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`MODEL`| The modified diffusion model.| MODEL  
`CLIP`| The modified CLIP model.| CLIP  
  
**Note:** This node is marked as experimental.

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderBypass/en.md)

* * *

**Source fingerprint (SHA-256):** `025f0638a6690a53b1a6c4548dac24fb7e7f26e04ff4b1c88d29b061430037a8`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LoraLoaderBypass.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LoraLoaderBypass)

[LoadMoGeModel - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LoadMoGeModel)[LoraLoaderBypassModelOnly - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LoraLoaderBypassModelOnly)

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
