---
url: https://docs.comfy.org/built-in-nodes/GLIGENLoader/
title: GLIGENLoader - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:59.030124+00:00
---

# GLIGENLoader - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/GLIGENLoader/

Loaders

# GLIGENLoader - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node will detect models located in the ComfyUI/models/gligen folder

Copy pageCopy page

This node will detect models located in the `ComfyUI/models/gligen` folder, and it will also read models from additional paths configured in the extra_model_paths.yaml file. Sometimes, you may need to **refresh the ComfyUI interface** to allow it to read the model files from the corresponding folder. The `GLIGENLoader` node is designed for loading GLIGEN models, which are specialized generative models. It facilitates the process of retrieving and initializing these models from specified paths, making them ready for further generative tasks.

## 

​

Inputs

Field| Description| Comfy dtype  
---|---|---  
`gligen_name`| The name of the GLIGEN model to be loaded, specifying which model file to retrieve and load, crucial for the initialization of the GLIGEN model.| `COMBO[STRING]`  
  
## 

​

Outputs

Field| Description| Data Type  
---|---|---  
`gligen`| The loaded GLIGEN model, ready for use in generative tasks, representing the fully initialized model loaded from the specified path.| `GLIGEN`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GligenLoader/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/GLIGENLoader.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/GLIGENLoader)

[FrameInterpolationModelLoader - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/FrameInterpolationModelLoader)[HypernetworkLoader - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/HypernetworkLoader)

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
