---
url: https://docs.comfy.org/built-in-nodes/HypernetworkLoader/
title: HypernetworkLoader - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:06.035256+00:00
---

# HypernetworkLoader - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/HypernetworkLoader/

Loaders

# HypernetworkLoader - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node will detect models located in the ComfyUI/models/hypernetworks folder

Copy pageCopy page

This node will detect models located in the `ComfyUI/models/hypernetworks` folder, and it will also read models from additional paths configured in the extra_model_paths.yaml file. Sometimes, you may need to **refresh the ComfyUI interface** to allow it to read the model files from the corresponding folder. The HypernetworkLoader node is designed to enhance or modify the capabilities of a given model by applying a hypernetwork. It loads a specified hypernetwork and applies it to the model, potentially altering its behavior or performance based on the strength parameter. This process allows for dynamic adjustments to the model’s architecture or parameters, enabling more flexible and adaptive AI systems.

## 

​

Inputs

Field| Description| Comfy dtype  
---|---|---  
`model`| The base model to which the hypernetwork will be applied, determining the architecture to be enhanced or modified.| `MODEL`  
`hypernetwork_name`| The name of the hypernetwork to be loaded and applied to the model, impacting the model’s modified behavior or performance.| `COMBO[STRING]`  
`strength`| A scalar adjusting the intensity of the hypernetwork’s effect on the model, allowing fine-tuning of the alterations.| `FLOAT`  
  
## 

​

Outputs

Field| Description| Data Type  
---|---|---  
`model`| The modified model after the hypernetwork has been applied, showcasing the impact of the hypernetwork on the original model.| `MODEL`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HypernetworkLoader/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/HypernetworkLoader.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/HypernetworkLoader)

[GLIGENLoader - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/GLIGENLoader)[ImageOnlyCheckpointLoader - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ImageOnlyCheckpointLoader)

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
