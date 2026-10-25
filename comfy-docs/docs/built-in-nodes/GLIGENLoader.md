---
url: https://docs.comfy.org/built-in-nodes/GLIGENLoader/
title: GLIGENLoader - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-25T12:24:52.276053+00:00
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
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GLIGENLoader/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/GLIGENLoader.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/GLIGENLoader)

[FrameInterpolationModelLoader](https://docs.comfy.org/built-in-nodes/FrameInterpolationModelLoader)[HypernetworkLoader](https://docs.comfy.org/built-in-nodes/HypernetworkLoader)
