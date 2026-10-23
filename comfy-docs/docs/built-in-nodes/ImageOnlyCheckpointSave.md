---
url: https://docs.comfy.org/built-in-nodes/ImageOnlyCheckpointSave/
title: ImageOnlyCheckpointSave - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:10.186202+00:00
---

# ImageOnlyCheckpointSave - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ImageOnlyCheckpointSave/

Merging

# ImageOnlyCheckpointSave - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node saves a checkpoint file that bundles a model together with its CLIP vision encoder and VAE.

Copy pageCopy page

This node saves a checkpoint file that bundles a model together with its CLIP vision encoder and VAE. The file is written in safetensors format to the output directory, using the given filename prefix, so the image-related components of a model can be stored as a single checkpoint.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The model to be saved in the checkpoint| MODEL| Yes| -  
`clip_vision`| The CLIP vision encoder to be saved in the checkpoint| CLIP_VISION| Yes| -  
`vae`| The VAE (Variational Autoencoder) to be saved in the checkpoint| VAE| Yes| -  
`filename_prefix`| The prefix for the output filename (default: “checkpoints/ComfyUI”)| STRING| Yes| -  
`prompt`| Hidden parameter that receives the workflow prompt data| PROMPT| No| -  
`extra_pnginfo`| Hidden parameter that receives additional PNG metadata| EXTRA_PNGINFO| No| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
-| This node does not return any outputs| -  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageOnlyCheckpointSave/en.md)

* * *

**Source fingerprint (SHA-256):** `8ff4b3a78d8da523eaa5f784f847e954ba73b4d6037e748dcce592b447fcdee9`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ImageOnlyCheckpointSave.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ImageOnlyCheckpointSave)

[CLIPSave - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ClipSave)[ModelMergeAdd - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ModelMergeAdd)

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
