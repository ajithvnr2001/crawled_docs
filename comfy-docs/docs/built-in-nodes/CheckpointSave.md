---
url: https://docs.comfy.org/built-in-nodes/CheckpointSave/
title: CheckpointSave - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:35.319582+00:00
---

# CheckpointSave - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/CheckpointSave/

Merging

# CheckpointSave - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Save Checkpoint node is designed to save a complete Stable Diffusion model (including UNet, CLIP

Copy pageCopy page

The `Save Checkpoint` node is designed to save a complete Stable Diffusion model (including UNet, CLIP, and VAE components) as a **.safetensors** format checkpoint file. The Save Checkpoint is primarily used in model merging workflows. After creating a new merged model through nodes like `ModelMergeSimple`, `ModelMergeBlocks`, etc., you can use this node to save the result as a reusable checkpoint file.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`model`| The model parameter represents the primary model whose state is to be saved. It is essential for capturing the current state of the model for future restoration or analysis.| MODEL  
`clip`| The clip parameter is intended for the CLIP model associated with the primary model, allowing its state to be saved alongside the main model.| CLIP  
`vae`| The vae parameter is for the Variational Autoencoder (VAE) model, enabling its state to be saved for future use or analysis alongside the main model and CLIP.| VAE  
`filename_prefix`| This parameter specifies the prefix for the filename under which the checkpoint will be saved.| STRING  
  
Additionally, the node has two hidden inputs for metadata: **prompt (PROMPT)** : Workflow prompt information **extra_pnginfo (EXTRA_PNGINFO)** : Additional PNG information

## 

​

Outputs

This node will output a checkpoint file, and the corresponding output file path is `output/checkpoints/` directory

## 

​

Architecture Compatibility

  * Currently fully supported: SDXL, SD3, SVD and other mainstream architectures, see [source code](https://github.com/comfyanonymous/ComfyUI/blob/master/comfy_extras/nodes_model_merging.py#L176-L189)
  * Basic support: Other architectures can be saved but without standardized metadata information



## 

​

Related Links

Related source code: [nodes_model_merging.py#L227](https://github.com/comfyanonymous/ComfyUI/blob/master/comfy_extras/nodes_model_merging.py#L227)

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointSave/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/CheckpointSave.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/CheckpointSave)

[ModelMergeWAN2_1 - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ModelMergeWAN2_1)[CLIPMergeAdd - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/CLIPMergeAdd)

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
