---
url: https://docs.comfy.org/built-in-nodes/DualCLIPLoader/
title: DualCLIPLoader - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-25T12:24:51.867737+00:00
---

# DualCLIPLoader - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/DualCLIPLoader/

Loaders

# DualCLIPLoader - ComfyUI Built-in Node Documentation

Copy pageCopy page

The DualCLIPLoader node is designed for loading two CLIP models simultaneously

Copy pageCopy page

The DualCLIPLoader node is designed for loading two CLIP models simultaneously, facilitating operations that require the integration or comparison of features from both models. This node will detect models located in the `ComfyUI/models/text_encoders` folder.

## 

​

Inputs

Parameter| Description| Comfy dtype  
---|---|---  
`clip_name1`| Specifies the name of the first CLIP model to be loaded. This parameter is crucial for identifying and retrieving the correct model from a predefined list of available CLIP models.| COMBO[STRING]  
`clip_name2`| Specifies the name of the second CLIP model to be loaded. This parameter enables the loading of a second distinct CLIP model for comparative or integrative analysis alongside the first model.| COMBO[STRING]  
`type`| Choose from “sdxl”, “sd3”, “flux” to adapt to different models.| `option`  
  
  * The order of loading does not affect the output effect



## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`clip`| The output is a combined CLIP model that integrates the features or functionalities of the two specified CLIP models.| CLIP  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCLIPLoader/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/DualCLIPLoader.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/DualCLIPLoader)

[DiffusersLoader](https://docs.comfy.org/built-in-nodes/DiffusersLoader)[FrameInterpolationModelLoader](https://docs.comfy.org/built-in-nodes/FrameInterpolationModelLoader)
