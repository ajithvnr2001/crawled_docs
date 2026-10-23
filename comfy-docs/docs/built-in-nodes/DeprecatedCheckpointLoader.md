---
url: https://docs.comfy.org/built-in-nodes/DeprecatedCheckpointLoader/
title: DeprecatedCheckpointLoader - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:50.264235+00:00
---

# DeprecatedCheckpointLoader - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/DeprecatedCheckpointLoader/

Loaders

# DeprecatedCheckpointLoader - ComfyUI Built-in Node Documentation

Copy pageCopy page

The CheckpointLoader node is designed for advanced loading operations, specifically to load model checkpoints along with their configurations.

Copy pageCopy page

The CheckpointLoader node is designed for advanced loading operations, specifically to load model checkpoints along with their configurations. It facilitates the retrieval of model components necessary for initializing and running generative models, including configurations and checkpoints from specified directories.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`config_name`| Specifies the name of the configuration file to be used. This is crucial for determining the model’s parameters and settings, affecting the model’s behavior and performance.| COMBO[STRING]  
`ckpt_name`| Indicates the name of the checkpoint file to be loaded. This directly influences the state of the model being initialized, impacting its initial weights and biases.| COMBO[STRING]  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`model`| Represents the primary model loaded from the checkpoint, ready for further operations or inference.| MODEL  
`clip`| Provides the CLIP model component, if available and requested, loaded from the checkpoint.| CLIP  
`vae`| Delivers the VAE model component, if available and requested, loaded from the checkpoint.| VAE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DeprecatedCheckpointLoader/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/DeprecatedCheckpointLoader.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/DeprecatedCheckpointLoader)

[ConditioningTimestepsRange - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ConditioningTimestepsRange)[DeprecatedDiffusersLoader - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/DeprecatedDiffusersLoader)

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
