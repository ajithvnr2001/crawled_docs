---
url: https://docs.comfy.org/built-in-nodes/LoraModelLoader/
title: LoraModelLoader - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:25.398153+00:00
---

# LoraModelLoader - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LoraModelLoader/

Loaders

# LoraModelLoader - ComfyUI Built-in Node Documentation

Copy pageCopy page

The LoraModelLoader node applies trained LoRA (Low-Rank Adaptation) weights to a diffusion model.

Copy pageCopy page

The LoraModelLoader node applies trained LoRA (Low-Rank Adaptation) weights to a diffusion model. It modifies the base model by loading LoRA weights from a trained LoRA model and adjusting their influence strength. This allows you to customize the behavior of diffusion models without retraining them from scratch, including a bypass mode that leaves the base model weights unchanged.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The diffusion model the LoRA will be applied to.| MODEL| Yes| -  
`lora`| The LoRA model to apply to the diffusion model.| LORA_MODEL| Yes| -  
`strength_model`| How strongly to modify the diffusion model. This value can be negative (default: 1.0).| FLOAT| Yes| -100.0 to 100.0  
`bypass`| When enabled, applies LoRA in bypass mode without modifying base model weights. Useful for training and when model weights are offloaded (default: False).| BOOLEAN| Yes| True or False  
  
**Note:** When `strength_model` is set to 0, the node returns the original model without applying any LoRA modifications.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| The modified diffusion model with LoRA weights applied.| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraModelLoader/en.md)

* * *

**Source fingerprint (SHA-256):** `81eb2a9b0376fe7453f6e7e422414472e80a3d1b92bb6874b91df6de8aed0d9a`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LoraModelLoader.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LoraModelLoader)

[LoraLoaderBypassModelOnly - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LoraLoaderBypassModelOnly)[LTXAVTextEncoderLoader - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LTXAVTextEncoderLoader)

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
