---
url: https://docs.comfy.org/built-in-nodes/TripoPSeriesTextToModelNode/
title: TripoPSeriesTextToModelNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:13.594860+00:00
---

# TripoPSeriesTextToModelNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/TripoPSeriesTextToModelNode/

Tripo

# TripoPSeriesTextToModelNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generates a low-poly 3D model with clean topology from a text prompt using Tripo’s P2 model.

Copy pageCopy page

Generates a low-poly 3D model with clean topology from a text prompt using Tripo’s P2 model. The result comes back as a triangle mesh (GLB) or, when `model.quad` is enabled, as a quad-dominant mesh (FBX).

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
`model.prompt`| Text description of the 3D model to generate. Must not be empty, up to 1024 characters (default: empty).| STRING| Yes| Up to 1024 characters  
`model.negative_prompt`| Text description of what to avoid in the generated model (default: empty).| STRING| No| Up to 255 characters  
`model.quad`| Return a quad-dominant mesh on the FBX output instead of a triangle mesh on the GLB output (default: False).| BOOLEAN| Yes| True/False  
`model.face_limit`| Target face count. `-1` lets Tripo choose. With `model.quad` enabled the limit is 48 to 25,000, otherwise 48 to 50,000 (default: -1).| INT| Yes| -1, or 48 to 50000  
`model.texture`| Base color texture resolution: standard is 2K, detailed 4K and extreme 8K. `"none"` returns an untextured mesh (default: `"standard"`).| COMBO| Yes| `"standard"`  
`"detailed"`  
`"extreme"`  
`"none"`  
`model.pbr`| Add metallic, roughness and normal maps to the base color. Ignored when `model.texture` is `"none"` (default: True).| BOOLEAN| Yes| True/False  
`model.model_seed`| Seed for the geometry (default: 42).| INT| Yes| 0 to 2147483647  
`model.image_seed`| Seed for the image Tripo draws from the prompt before modeling (default: 42). Advanced setting.| INT| Yes| 0 to 2147483647  
`model.texture_seed`| Seed for the textures (default: 42). Advanced setting.| INT| Yes| 0 to 2147483647  
`model.auto_size`| Scale the model to its real-world size in meters through its scene transform. Ignored when `model.texture` is `"none"` (default: False). Advanced setting.| BOOLEAN| Yes| True/False  
`model.export_uv`| UV unwrap the mesh when it is untextured. Textured meshes are always unwrapped (default: True). Advanced setting.| BOOLEAN| Yes| True/False  
`model.compress_geometry`| Apply meshopt geometry compression: much smaller files, but ComfyUI’s 3D preview cannot display them. Ignored for quad meshes (default: False). Advanced setting.| BOOLEAN| Yes| True/False  
  
**Notes:**

  * `model.prompt` is required; `model.negative_prompt` is optional and limited to 255 characters.
  * `model.face_limit` is a target rather than a hard cap, so the result can contain more faces than requested. `-1` leaves the choice to Tripo.
  * `model.quad` decides which output carries the mesh. With it enabled the model arrives on the FBX output and the GLB output stays empty; with it disabled the model arrives on GLB and FBX stays empty. The node raises an error if the empty output is the one you connected.
  * `model.texture`, `model.pbr`, `model.texture_seed` and `model.auto_size` only apply to textured models: with `"none"` the node sends no texture settings and returns bare geometry.
  * `model.compress_geometry` has no effect on quad meshes.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model task_id`| The unique task ID for the model generation request.| MODEL_TASK_ID  
`GLB`| The generated 3D model in GLB format. Empty when `model.quad` is enabled.| FILE3DGLB  
`FBX`| The generated 3D model in FBX format. Only populated when `model.quad` is enabled.| FILE3DFBX  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoPSeriesTextToModelNode/en.md)

* * *

**Source fingerprint (SHA-256):** `e55596c1a237cf6b92e3bdead4359f380c6cba60992dcc61b5ee4e6b1bdd843b`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/TripoPSeriesTextToModelNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/TripoPSeriesTextToModelNode)

[TripoPSeriesMultiviewToModelNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/TripoPSeriesMultiviewToModelNode)[TripoRetargetNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/TripoRetargetNode)

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
