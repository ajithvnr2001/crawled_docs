---
url: https://docs.comfy.org/built-in-nodes/DiffControlNetLoader/
title: DiffControlNetLoader - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-25T12:24:51.972453+00:00
---

# DiffControlNetLoader - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/DiffControlNetLoader/

Loaders

# DiffControlNetLoader - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node will detect models located in the ComfyUI/models/controlnet folder

Copy pageCopy page

This node will detect models located in the `ComfyUI/models/controlnet` folder, and it will also read models from additional paths configured in the extra_model_paths.yaml file. Sometimes, you may need to **refresh the ComfyUI interface** to allow it to read the model files from the corresponding folder. The DiffControlNetLoader node is designed for loading differential control networks, which are specialized models that can modify the behavior of another model based on control net specifications. This node allows for the dynamic adjustment of model behaviors by applying differential control nets, facilitating the creation of customized model outputs.

## 

​

Inputs

Field| Description| Comfy dtype  
---|---|---  
`model`| The base model to which the differential control net will be applied, allowing for customization of the model’s behavior.| `MODEL`  
`control_net_name`| Identifies the specific differential control net to be loaded and applied to the base model for modifying its behavior.| `COMBO[STRING]`  
  
## 

​

Outputs

Field| Description| Comfy dtype  
---|---|---  
`control_net`| A differential control net that has been loaded and is ready to be applied to a base model for behavior modification.| `CONTROL_NET`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DiffControlNetLoader/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/DiffControlNetLoader.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/DiffControlNetLoader)

[ConditioningLoader](https://docs.comfy.org/built-in-nodes/ConditioningLoader)[DiffusersLoader](https://docs.comfy.org/built-in-nodes/DiffusersLoader)
