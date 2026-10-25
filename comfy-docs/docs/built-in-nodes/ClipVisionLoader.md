---
url: https://docs.comfy.org/built-in-nodes/ClipVisionLoader/
title: CLIPVisionLoader - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-25T12:24:51.520862+00:00
---

# CLIPVisionLoader - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ClipVisionLoader/

Loaders

# CLIPVisionLoader - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node automatically detects models located in the ComfyUI/models/clipvision folder

Copy pageCopy page

This node automatically detects models located in the `ComfyUI/models/clip_vision` folder, as well as any additional model paths configured in the `extra_model_paths.yaml` file. If you add models after starting ComfyUI, please **refresh the ComfyUI interface** to ensure the latest model files are listed.

## 

​

Inputs

Field| Description| Data Type  
---|---|---  
`clip_name`| Lists all supported model files in the `ComfyUI/models/clip_vision` folder.| COMBO[STRING]  
  
## 

​

Outputs

Field| Description| Data Type  
---|---|---  
`clip_vision`| Loaded CLIP Vision model, ready for encoding images or other vision-related tasks.| CLIP_VISION  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPVisionLoader/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ClipVisionLoader.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ClipVisionLoader)

[CLIPLoader](https://docs.comfy.org/built-in-nodes/ClipLoader)[ConditioningLoader](https://docs.comfy.org/built-in-nodes/ConditioningLoader)
