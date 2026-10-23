---
url: https://docs.comfy.org/built-in-nodes/unCLIPCheckpointLoader/
title: unCLIPCheckpointLoader - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:32.677368+00:00
---

# unCLIPCheckpointLoader - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/unCLIPCheckpointLoader/

Loaders

# unCLIPCheckpointLoader - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node will detect models located in the ComfyUI/models/checkpoints folder

Copy pageCopy page

This node will detect models located in the `ComfyUI/models/checkpoints` folder, and it will also read models from additional paths configured in the extra_model_paths.yaml file. Sometimes, you may need to **refresh the ComfyUI interface** to allow it to read the model files from the corresponding folder. The unCLIPCheckpointLoader node is designed for loading checkpoints specifically tailored for unCLIP models. It facilitates the retrieval and initialization of models, CLIP vision modules, and VAEs from a specified checkpoint, streamlining the setup process for further operations or analyses.

## 

​

Inputs

Field| Description| Comfy dtype  
---|---|---  
`ckpt_name`| Specifies the name of the checkpoint to be loaded, identifying and retrieving the correct checkpoint file from a predefined directory, determining the initialization of models and configurations.| `COMBO[STRING]`  
  
## 

​

Outputs

Field| Description| Comfy dtype| Python dtype  
---|---|---|---  
`model`| Represents the primary model loaded from the checkpoint.| `MODEL`| `torch.nn.Module`  
`clip`| Represents the CLIP module loaded from the checkpoint, if available.| `CLIP`| `torch.nn.Module`  
`vae`| Represents the VAE module loaded from the checkpoint, if available.| `VAE`| `torch.nn.Module`  
`clip_vision`| Represents the CLIP vision module loaded from the checkpoint, if available.| `CLIP_VISION`| `torch.nn.Module`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UnclipCheckpointLoader/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/unCLIPCheckpointLoader.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/unCLIPCheckpointLoader)

[TripleCLIPLoader - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/TripleCLIPLoader)[UNETLoader - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/UNETLoader)

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
