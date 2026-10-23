---
url: https://docs.comfy.org/built-in-nodes/MeshyRefineNode/
title: MeshyRefineNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:31.580118+00:00
---

# MeshyRefineNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MeshyRefineNode/

Meshy

# MeshyRefineNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Meshy: Refine Draft Model node takes a 3D draft model from a previous Meshy task and improves it

Copy pageCopy page

The Meshy: Refine Draft Model node takes a 3D draft model from a previous Meshy task and improves it, optionally adding textures using a text prompt or a reference image. It submits the refinement job to the Meshy API and returns the finished model as GLB and FBX files once the task is complete.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The AI model used to refine the draft model.| COMBO| Yes| `"meshy-7.1"`  
`"meshy-7"`  
`"meshy-6"`  
`"latest"`  
`meshy_task_id`| The unique task ID of the draft model you want to refine.| MESHY_TASK_ID| Yes| -  
`enable_pbr`| Generate PBR Maps (metallic, roughness, normal) in addition to the base color. Note: this should be set to false when using Sculpture style, as Sculpture style generates its own set of PBR maps. (default: False)| BOOLEAN| Yes| -  
`texture_prompt`| Provide a text prompt to guide the texturing process. Maximum 600 characters. Cannot be used at the same time as `texture_image`. (default: empty string)| STRING| Yes| Maximum 600 characters  
`texture_image`| Only one of `texture_image` or `texture_prompt` may be used at the same time.| IMAGE| No| -  
`texture_resolution`| Base color texture resolution. Higher resolutions capture more surface detail.| COMBO| Yes| `"2k"`  
`"4k"`  
`"8k"`  
  
**Note:** The `texture_prompt` and `texture_image` inputs are mutually exclusive. You cannot provide both a text prompt and an image for texturing in the same operation.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model_file`| The filename of the generated GLB model. (For backward compatibility only)| STRING  
`meshy_task_id`| The unique task ID for the submitted refinement job.| MESHY_TASK_ID  
`GLB`| The final refined 3D model in GLB format.| FILE3DGLB  
`FBX`| The final refined 3D model in FBX format.| FILE3DFBX  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyRefineNode/en.md)

* * *

**Source fingerprint (SHA-256):** `d9aac584e6abf9688c97bf01ea515bca13844d08c93923a672fb2853266926c8`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MeshyRefineNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MeshyRefineNode)

[MeshyMultiImageToModelNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/MeshyMultiImageToModelNode)[MeshyRigModelNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/MeshyRigModelNode)

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
