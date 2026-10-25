---
url: https://docs.comfy.org/built-in-nodes/UNETLoader/
title: UNETLoader - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-25T12:24:52.929513+00:00
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
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNETLoader/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/UNETLoader.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/UNETLoader)

[unCLIPCheckpointLoader](https://docs.comfy.org/built-in-nodes/unCLIPCheckpointLoader)[UpscaleModelLoader](https://docs.comfy.org/built-in-nodes/UpscaleModelLoader)
