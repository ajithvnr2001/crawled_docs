---
url: https://docs.comfy.org/built-in-nodes/DeprecatedDiffusersLoader/
title: DeprecatedDiffusersLoader - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:50.552178+00:00
---

# DeprecatedDiffusersLoader - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/DeprecatedDiffusersLoader/

Loaders

# DeprecatedDiffusersLoader - ComfyUI Built-in Node Documentation

Copy pageCopy page

The DiffusersLoader node is designed for loading models from the diffusers library, specifically handling the loading of UNet, CLIP

Copy pageCopy page

The DiffusersLoader node is designed for loading models from the diffusers library, specifically handling the loading of UNet, CLIP, and VAE models based on provided model paths. It facilitates the integration of these models into the ComfyUI framework, enabling advanced functionalities such as text-to-image generation, image manipulation, and more.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`model_path`| Specifies the path to the model to be loaded. This path is crucial as it determines which model will be utilized for subsequent operations, affecting the output and capabilities of the node.| COMBO[STRING]  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`model`| The loaded UNet model, which is part of the output tuple. This model is essential for image synthesis and manipulation tasks within the ComfyUI framework.| MODEL  
`clip`| The loaded CLIP model, included in the output tuple if requested. This model enables advanced text and image understanding and manipulation capabilities.| CLIP  
`vae`| The loaded VAE model, included in the output tuple if requested. This model is crucial for tasks involving latent space manipulation and image generation.| VAE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DeprecatedDiffusersLoader/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/DeprecatedDiffusersLoader.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/DeprecatedDiffusersLoader)

[DeprecatedCheckpointLoader - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/DeprecatedCheckpointLoader)[SaveLoRANode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SaveLoRANode)

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
