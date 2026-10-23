---
url: https://docs.comfy.org/built-in-nodes/TripoPSeriesMultiviewToModelNode/
title: TripoPSeriesMultiviewToModelNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:13.945523+00:00
---

# TripoPSeriesMultiviewToModelNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/TripoPSeriesMultiviewToModelNode/

Tripo

# TripoPSeriesMultiviewToModelNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generates a low-poly 3D model with clean topology from several views of the same subject using Tripo’s P2 model.

Copy pageCopy page

Generates a low-poly 3D model with clean topology from several views of the same subject using Tripo’s P2 model. The front view is required and one to three of the left, back and right views can be added to improve the result. The model comes back as a triangle mesh (GLB) or, when `model.quad` is enabled, as a quad-dominant mesh (FBX).

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| Tripo P-series model to use. Selecting a model reveals its own inputs below.| DYNAMIC_COMBO| Yes| `"P2"`  
  
### 

​

P2 Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model.image`| Front view (0°) of the subject.| IMAGE| Yes| -  
`model.image_left`| Left view (90°), the subject’s own left side.| IMAGE| No| -  
`model.image_back`| Back view (180°).| IMAGE| No| -  
`model.image_right`| Right view (270°), the subject’s own right side.| IMAGE| No| -  
`model.quad`| Return a quad-dominant mesh on the FBX output instead of a triangle mesh on the GLB output (default: False).| BOOLEAN| Yes| True/False  
`model.face_limit`| Target face count. `-1` lets Tripo choose. With `model.quad` enabled the limit is 48 to 25,000, otherwise 48 to 50,000 (default: -1).| INT| Yes| -1, or 48 to 50000  
`model.texture`| Base color texture resolution: standard is 2K, detailed 4K and extreme 8K. `"none"` returns an untextured mesh (default: `"standard"`).| COMBO| Yes| `"standard"`  
`"detailed"`  
`"extreme"`  
`"none"`  
`model.pbr`| Add metallic, roughness and normal maps to the base color. Ignored when `model.texture` is `"none"` (default: True).| BOOLEAN| Yes| True/False  
`model.model_seed`| Seed for the geometry (default: 42).| INT| Yes| 0 to 2147483647  
`model.texture_alignment`| Match the colors of the input images, or fit the textures to the generated geometry. Ignored when `model.texture` is `"none"` (default: `"original_image"`). Advanced setting.| COMBO| Yes| `"original_image"`  
`"geometry"`  
`model.orientation`| `"align_image"` rotates the model to the viewpoint of the input images. Ignored when `model.texture` is `"none"` (default: `"default"`). Advanced setting.| COMBO| Yes| `"default"`  
`"align_image"`  
`model.texture_seed`| Seed for the textures (default: 42). Advanced setting.| INT| Yes| 0 to 2147483647  
`model.auto_size`| Scale the model to its real-world size in meters through its scene transform. Ignored when `model.texture` is `"none"` (default: False). Advanced setting.| BOOLEAN| Yes| True/False  
`model.export_uv`| UV unwrap the mesh when it is untextured. Textured meshes are always unwrapped (default: True). Advanced setting.| BOOLEAN| Yes| True/False  
`model.compress_geometry`| Apply meshopt geometry compression: much smaller files, but ComfyUI’s 3D preview cannot display them. Ignored for quad meshes (default: False). Advanced setting.| BOOLEAN| Yes| True/False  
  
**Notes:**

  * `model.image` is required, and at least one of `model.image_left`, `model.image_back` or `model.image_right` has to be connected as well; the node raises an error if the front view is the only image.
  * Only the first image of each batch is used.
  * `model.face_limit` is a target rather than a hard cap, so the result can contain more faces than requested. `-1` leaves the choice to Tripo.
  * `model.quad` decides which output carries the mesh. With it enabled the model arrives on the FBX output and the GLB output stays empty; with it disabled the model arrives on GLB and FBX stays empty. The node raises an error if the empty output is the one you connected.
  * `model.texture`, `model.pbr`, `model.texture_seed`, `model.auto_size`, `model.texture_alignment` and `model.orientation` only apply to textured models: with `"none"` the node sends no texture settings and returns bare geometry.
  * `model.compress_geometry` has no effect on quad meshes.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model task_id`| The unique task ID for the model generation request.| MODEL_TASK_ID  
`GLB`| The generated 3D model in GLB format. Empty when `model.quad` is enabled.| FILE3DGLB  
`FBX`| The generated 3D model in FBX format. Only populated when `model.quad` is enabled.| FILE3DFBX  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoPSeriesMultiviewToModelNode/en.md)

* * *

**Source fingerprint (SHA-256):** `cea0a65ca001bc8298af9fbe2a83f592abf497987e634b0126482f3d2a18571c`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/TripoPSeriesMultiviewToModelNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/TripoPSeriesMultiviewToModelNode)

[TripoPSeriesImageToModelNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/TripoPSeriesImageToModelNode)[TripoPSeriesTextToModelNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/TripoPSeriesTextToModelNode)

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
