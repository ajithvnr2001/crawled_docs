---
url: https://docs.comfy.org/built-in-nodes/MeshyImageToModelNode/
title: MeshyImageToModelNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:31.249251+00:00
---

# MeshyImageToModelNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MeshyImageToModelNode/

Meshy

# MeshyImageToModelNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Meshy: Image to Model node uses the Meshy API to generate a 3D model from a single input image.

Copy pageCopy page

The Meshy: Image to Model node uses the Meshy API to generate a 3D model from a single input image. It uploads your image, submits a processing task, and returns the generated 3D model files (GLB and FBX) along with the task ID for reference.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| Specifies the AI model version to use for generation.| COMBO| Yes| `"meshy-7.1"`  
`"meshy-7"`  
`"meshy-6"`  
`"latest"`  
`image`| The input image to convert into a 3D model.| IMAGE| Yes| -  
`should_remesh`| When set to `"false"`, returns an unprocessed triangular mesh.| DYNAMIC_COMBO| Yes| `"true"`  
`"false"`  
`topology`| The target polygon topology for the remeshed model. This input is only available when `should_remesh` is set to `"true"`.| COMBO| No*| `"triangle"`  
`"quad"`  
`target_polycount`| The target number of polygons for the remeshed model. This input is only available when `should_remesh` is set to `"true"`. Default: 300000.| INT| No*| 100 - 300000  
`symmetry_mode`| Controls the symmetry applied to the generated 3D model.| COMBO| Yes| `"auto"`  
`"on"`  
`"off"`  
`should_texture`| Determines whether textures are generated. Setting it to `"false"` skips the texture phase and returns a mesh without textures.| DYNAMIC_COMBO| Yes| `"true"`  
`"false"`  
`enable_pbr`| Generate PBR Maps (metallic, roughness, normal) in addition to the base color. This input is only available when `should_texture` is set to `"true"`. Default: `False`.| BOOLEAN| No*| -  
`texture_prompt`| Provide a text prompt to guide the texturing process. Maximum 600 characters. Cannot be used at the same time as `texture_image`. This input is only available when `should_texture` is set to `"true"`. Default: empty string.| STRING| No*| -  
`texture_image`| Only one of `texture_image` or `texture_prompt` may be used at the same time. This input is only available when `should_texture` is set to `"true"`.| IMAGE| No*| -  
`texture_resolution`| Base color texture resolution. Higher resolutions capture more surface detail. This input is only available when `should_texture` is set to `"true"`.| COMBO| No*| `"2k"`  
`"4k"`  
`"8k"`  
`pose_mode`| Specify the pose mode for the generated model. This is an advanced parameter.| COMBO| Yes| `""` (empty)  
`"A-pose"`  
`"T-pose"`  
`seed`| Seed controls whether the node should re-run; results are non-deterministic regardless of seed. Default: 0.| INT| Yes| 0 - 2147483647  
`ultra_mode`| Run an extra refinement pass for higher-fidelity geometry with finer surface detail. Default: `False`.| BOOLEAN| Yes| -  
`ultra_resolution`| Resolution of the ultra pass: `"2k"` runs it at 2048³, `"4k"` at 4096³ for the finest surface detail. 4k requires the `"meshy-7.1"` or `"latest"` model. Used only when `ultra_mode` is enabled (default: `"2k"`).| COMBO| No| `"2k"`  
`"4k"`  
  
**Note on Parameter Constraints:**

  * The `topology` and `target_polycount` inputs are only available when `should_remesh` is set to `"true"`.
  * The `enable_pbr`, `texture_prompt`, `texture_image`, and `texture_resolution` inputs are only available when `should_texture` is set to `"true"`.
  * When `should_texture` is set to `"true"`, `texture_prompt` and `texture_image` cannot be used at the same time. If both are provided, the node raises an error.
  * `texture_prompt` has a maximum length of 600 characters.
  * When `ultra_mode` is enabled, the `model` parameter must be set to `"meshy-7.1"`, `"meshy-7"` or `"latest"`; any other model raises an error. With `"meshy-7"` the ultra pass always runs at 2048³, and the `"4k"` ultra resolution requires `"meshy-7.1"` or `"latest"`.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model_file`| The filename of the generated GLB model. Maintained for backward compatibility only.| STRING  
`meshy_task_id`| The unique identifier for the Meshy API task, which can be used for reference or troubleshooting.| MESHY_TASK_ID  
`GLB`| The generated 3D model in the GLB file format.| FILE3DGLB  
`FBX`| The generated 3D model in the FBX file format.| FILE3DFBX  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyImageToModelNode/en.md)

* * *

**Source fingerprint (SHA-256):** `38528b48c3f792a459008a52f65fae248ef1dadafb37fe4dc6b697d25bc89f4f`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MeshyImageToModelNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MeshyImageToModelNode)

[MeshyAnimateModelNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/MeshyAnimateModelNode)[MeshyMultiImageToModelNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/MeshyMultiImageToModelNode)

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
