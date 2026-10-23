---
url: https://docs.comfy.org/built-in-nodes/DiffusersLoader/
title: DiffusersLoader - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:50.990277+00:00
---

# DiffusersLoader - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/DiffusersLoader/

Loaders

# DiffusersLoader - ComfyUI Built-in Node Documentation

Copy pageCopy page

The DiffusersLoader node loads pre-trained models saved in the diffusers format.

Copy pageCopy page

The DiffusersLoader node loads pre-trained models saved in the diffusers format. It searches the configured `diffusers` folders for directories that contain a `model_index.json` file, lets you select one, and loads it as the MODEL, CLIP, and VAE components used in the pipeline. This node is deprecated, but remains available for compatibility with Hugging Face diffusers models.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model_path`| The path to the diffusers model directory to load. The node automatically scans the configured diffusers folders (including linked subfolders) for directories containing a `model_index.json` file and lists the available options. The selected path is validated before loading; an invalid or missing model raises an error.| COMBO| Yes| Auto-populated list of folders containing `model_index.json`  
(relative paths inside the configured `diffusers` folders)  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`MODEL`| The loaded model component from the diffusers format.| MODEL  
`CLIP`| The loaded CLIP model component from the diffusers format.| CLIP  
`VAE`| The loaded VAE (Variational Autoencoder) component from the diffusers format.| VAE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DiffusersLoader/en.md)

* * *

**Source fingerprint (SHA-256):** `75238342d05eac7528f981a2d4544accb6053891cd078a77751cc838054225d4`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/DiffusersLoader.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/DiffusersLoader)

[DiffControlNetLoader - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/DiffControlNetLoader)[DualCLIPLoader - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/DualCLIPLoader)

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
