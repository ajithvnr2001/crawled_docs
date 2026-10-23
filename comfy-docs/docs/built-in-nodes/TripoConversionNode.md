---
url: https://docs.comfy.org/built-in-nodes/TripoConversionNode/
title: TripoConversionNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:12.113171+00:00
---

# TripoConversionNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/TripoConversionNode/

Tripo

# TripoConversionNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node converts an existing Tripo 3D model into another 3D file format.

Copy pageCopy page

This node converts an existing Tripo 3D model into another 3D file format. It takes the task ID of a model previously created or processed by a Tripo operation (such as model generation, rigging, retargeting, or segmentation), submits a conversion task to the Tripo API, waits for that task to finish, and then returns the converted model file.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`original_model_task_id`| Task ID of the Tripo model to convert. It must come from an earlier Tripo model generation, rigging, retargeting, or segmentation task. If the ID is missing or empty, the node raises an error.| STRING| Yes| MODEL_TASK_ID  
RIG_TASK_ID  
RETARGET_TASK_ID  
SEGMENT_TASK_ID  
`format`| Target file format for the converted 3D model.| COMBO| Yes| GLTF  
USDZ  
FBX  
OBJ  
STL  
3MF  
`quad`| Convert triangles to quads when enabled (default: False).| BOOLEAN| No| True or False  
`face_limit`| Maximum number of faces in the converted model. Set to -1 for no limit (default: -1).| INT| No| -1 to 2000000  
`texture_size`| Resolution of the output textures in pixels (default: 4096).| INT| No| 128 to 8192  
`texture_format`| File format used for exported textures (default: JPEG).| COMBO| No| BMP  
DPX  
HDR  
JPEG  
OPEN_EXR  
PNG  
TARGA  
TIFF  
WEBP  
`force_symmetry`| Force the model to be symmetrical when enabled (default: False).| BOOLEAN| No| True or False  
`flatten_bottom`| Flatten the bottom of the model when enabled (default: False).| BOOLEAN| No| True or False  
`flatten_bottom_threshold`| Flattening depth used with `flatten_bottom` (default: 0.01). This value is only applied when `flatten_bottom` is enabled.| FLOAT| No| 0.01 to 1.0  
`pivot_to_center_bottom`| Move the pivot point to the center bottom of the model when enabled (default: False).| BOOLEAN| No| True or False  
`scale_factor`| Scale factor applied to the converted model (default: 1.0).| FLOAT| No| 0.01 and above  
`with_animation`| Keep the skeleton and animation of rigged or retargeted models (default: True).| BOOLEAN| No| True or False  
`pack_uv`| Repack the UV coordinates when enabled (default: False).| BOOLEAN| No| True or False  
`bake`| Bake advanced materials into the base textures for broader compatibility (default: True).| BOOLEAN| No| True or False  
`part_names`| Comma-separated list of model part names to send to the conversion. Empty entries are ignored and duplicate names are removed. Leave empty to omit this option (default: empty).| STRING| No| Comma-separated list of part names  
`fbx_preset`| FBX compatibility preset. bake_scale bakes the scale transform into the geometry (default: blender).| COMBO| No| blender  
mixamo  
3dsmax  
bake_scale  
`export_vertex_colors`| Export vertex colors when enabled (default: False).| BOOLEAN| No| True or False  
`export_orientation`| Forward axis of the exported model. default keeps Tripo’s +x (default: default).| COMBO| No| default  
+x  
-x  
+y  
-y  
`animate_in_place`| Animate the model in place when enabled (default: False).| BOOLEAN| No| True or False  
  
**Note:** Except for `original_model_task_id` and `format`, all inputs are optional advanced settings. Most settings left at their default values are omitted from the conversion request so the Tripo API can use its standard behavior. The `with_animation` and `bake` options are always sent. `flatten_bottom_threshold` is only applied when `flatten_bottom` is enabled.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model_3d`| Converted model in the requested format. OBJ is delivered by Tripo as a ZIP archive (mesh, material and textures).| FILE_3D  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoConversionNode/en.md)

* * *

**Source fingerprint (SHA-256):** `b6be09bf6b1c5ccd6de5ae56ed28bfe1f0b81c1ca8ff61623e3094917c98d68a`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/TripoConversionNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/TripoConversionNode)

[TencentTextToModelNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/TencentTextToModelNode)[TripoEditMultiviewNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/TripoEditMultiviewNode)

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
