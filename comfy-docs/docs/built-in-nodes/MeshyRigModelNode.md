---
url: https://docs.comfy.org/built-in-nodes/MeshyRigModelNode/
title: MeshyRigModelNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:31.839700+00:00
---

# MeshyRigModelNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MeshyRigModelNode/

Meshy

# MeshyRigModelNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Meshy: Rig Model node takes a 3D model from a previous Meshy task and automatically creates a skeleton for it

Copy pageCopy page

The Meshy: Rig Model node takes a 3D model from a previous Meshy task and automatically creates a skeleton for it, producing a rigged character that can be posed and animated. The node outputs the rigged model in both GLB and FBX file formats.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`meshy_task_id`| The unique task ID from a previous Meshy operation (e.g., text-to-3D or image-to-3D) that generated the model to be rigged.| MESHY_TASK_ID| Yes| N/A  
`height_meters`| The approximate height of the character model in meters. This aids in scaling and rigging accuracy (default: 1.7).| FLOAT| Yes| 0.1 to 15.0  
`texture_image`| The model’s UV-unwrapped base color texture image.| IMAGE| No| N/A  
  
**Note:** The auto-rigging process is currently not suitable for untextured meshes, non-humanoid assets, or humanoid assets with unclear limb and body structure.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model_file`| A legacy output kept for backward compatibility only, containing the filename of the GLB model.| STRING  
`rig_task_id`| The unique task ID for this rigging operation, which can be used to reference the result in later Meshy nodes.| MESHY_RIGGED_TASK_ID  
`GLB`| The rigged 3D character model saved in the GLB file format.| FILE3DGLB  
`FBX`| The rigged 3D character model saved in the FBX file format.| FILE3DFBX  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyRigModelNode/en.md)

* * *

**Source fingerprint (SHA-256):** `6ae79359fa54f36dd2491a952fe54fa56866038758e8cd475a2d2f8e9e47e3b3`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MeshyRigModelNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MeshyRigModelNode)

[MeshyRefineNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/MeshyRefineNode)[MeshyTextToModelNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/MeshyTextToModelNode)

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
