---
url: https://docs.comfy.org/built-in-nodes/MeshyMultiImageToModelNode/
title: MeshyMultiImageToModelNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:31.383189+00:00
---

# MeshyMultiImageToModelNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MeshyMultiImageToModelNode/

Meshy

# MeshyMultiImageToModelNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node uses the Meshy API to generate a 3D model from multiple input images.

Copy pageCopy page

This node uses the Meshy API to generate a 3D model from multiple input images. It uploads the provided images, submits a processing task, and returns the resulting 3D model files (GLB and FBX) along with the task ID for reference.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| Specifies the AI model version to use.| COMBO| Yes| `"meshy-7.1"`  
`"meshy-7"`  
`"meshy-6"`  
`"latest"`  
`should_remesh`| Determines whether the generated mesh is processed. When set to `"false"`, the node returns an unprocessed triangular mesh. When set to `"true"`, the remesh settings below are shown.| DYNAMIC_COMBO| Yes| `"true"`  
`"false"`  
`symmetry_mode`| Controls whether symmetry is applied to the generated model.| COMBO| Yes| `"auto"`  
`"on"`  
`"off"`  
`should_texture`| Determines whether textures are generated. Setting it to `"false"` skips the texture phase and returns a mesh without textures. When set to `"true"`, the texture settings below are shown.| DYNAMIC_COMBO| Yes| `"true"`  
`"false"`  
`pose_mode`| Specify the pose mode for the generated model.| COMBO| Yes| `""` (empty)  
`"A-pose"`  
`"T-pose"`  
`seed`| Seed controls whether the node should re-run; results are non-deterministic regardless of seed. (default: 0)| INT| Yes| 0 to 2147483647  
`ultra_mode`| Run an extra refinement pass at 2048³ for higher-fidelity geometry with finer surface detail. Requires the `"meshy-7.1"`, `"meshy-7"` or `"latest"` model (default: `False`).| BOOLEAN| No| `True`  
`False`  
  
### 

​

Remesh Settings (visible when `should_remesh` is `"true"`)

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`topology`| The target polygon type for the remeshed output.| COMBO| No| `"triangle"`  
`"quad"`  
`target_polycount`| The target number of polygons for the remeshed model (default: 300000).| INT| No| 100 to 300000  
  
### 

​

Texture Settings (visible when `should_texture` is `"true"`)

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`enable_pbr`| Generate PBR Maps (metallic, roughness, normal) in addition to the base color. (default: False)| BOOLEAN| No| True / False  
`texture_prompt`| Provide a text prompt to guide the texturing process. Maximum 600 characters. Cannot be used at the same time as `texture_image`. (default: empty)| STRING| No| Up to 600 characters  
`texture_image`| Only one of `texture_image` or `texture_prompt` may be used at the same time.| IMAGE| No| -  
`texture_resolution`| Base color texture resolution. Higher resolutions capture more surface detail.| COMBO| No| `"2k"`  
`"4k"`  
`"8k"`  
  
### 

​

Image Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`images`| Growable slot: connect 2 to 4 input images (`image_1`, `image_2`, `image_3`, `image_4`). These images are used to generate the 3D model.| IMAGE| Yes| 2 to 4 images  
  
**Notes**

  * You must provide between 2 and 4 images for the `images` input.
  * The `topology` and `target_polycount` parameters are only active when `should_remesh` is set to `"true"`.
  * The `enable_pbr`, `texture_prompt`, `texture_image`, and `texture_resolution` parameters are only active when `should_texture` is set to `"true"`.
  * `texture_prompt` and `texture_image` are mutually exclusive; you cannot use both at the same time. `texture_prompt` is limited to 600 characters.
  * The `seed` value does not make results deterministic; changing it simply causes the node to re-run the generation task.
  * `ultra_mode` requires the `"meshy-7.1"`, `"meshy-7"` or `"latest"` model; any other model raises an error.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model_file`| The filename of the generated GLB model. This output is provided for backward compatibility only.| STRING  
`meshy_task_id`| The unique identifier for the Meshy API task.| MESHY_TASK_ID  
`GLB`| The generated 3D model in GLB format.| FILE3DGLB  
`FBX`| The generated 3D model in FBX format.| FILE3DFBX  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyMultiImageToModelNode/en.md)

* * *

**Source fingerprint (SHA-256):** `9475279c0990fc069b4fef2bf0e2e20218ca1a9591a261ce6d33a2b651782ddb`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MeshyMultiImageToModelNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MeshyMultiImageToModelNode)

[MeshyImageToModelNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/MeshyImageToModelNode)[MeshyRefineNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/MeshyRefineNode)

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
