---
url: https://docs.comfy.org/built-in-nodes/UNETLoader/
title: UNETLoader - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:15.997561+00:00
---

# UNETLoader - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/UNETLoader/

Loaders

# UNETLoader - ComfyUI Built-in Node Documentation

Copy pageCopy page

The UNETLoader node is designed for loading U-Net models by name, facilitating the use of pre-trained U-Net architectures within the system.

Copy pageCopy page

The UNETLoader node is designed for loading U-Net models by name, facilitating the use of pre-trained U-Net architectures within the system. This node will detect models located in the `ComfyUI/models/diffusion_models` folder.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`unet_name`| Specifies the name of the U-Net model to be loaded. This name is used to locate the model within a predefined directory structure, enabling the dynamic loading of different U-Net models.| COMBO[STRING]  
`weight_dtype`| 🚧 fp8_e4m3fn fp9_e5m2| …  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`model`| Returns the loaded U-Net model, allowing it to be utilized for further processing or inference within the system.| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UnetLoader/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/UNETLoader.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/UNETLoader)

[unCLIPCheckpointLoader - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/unCLIPCheckpointLoader)[UpscaleModelLoader - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/UpscaleModelLoader)

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
