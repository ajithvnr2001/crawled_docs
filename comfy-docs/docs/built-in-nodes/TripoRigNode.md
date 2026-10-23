---
url: https://docs.comfy.org/built-in-nodes/TripoRigNode/
title: TripoRigNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:14.141113+00:00
---

# TripoRigNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/TripoRigNode/

Tripo

# TripoRigNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node takes an existing Tripo 3D model and creates a rigged version of it, meaning the model gets a skeleton so it can be animated.

Copy pageCopy page

This node takes an existing Tripo 3D model and creates a rigged version of it, meaning the model gets a skeleton so it can be animated. You provide the task ID of the model to rig, choose the rig version, skeleton type, bone-naming style, and output file format, and the node sends the job to Tripo, waits until it finishes, then returns the downloaded result.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`original_model_task_id`| The task ID of the original 3D model to be rigged. This is usually the ID produced by an earlier Tripo model-generation node.| MODEL_TASK_ID| Yes| -  
`model_version`| Rig model version to use. v1.0: humanoid (biped) characters only, 90+ animation presets. v2.5: non-humanoid creatures (quadruped, hexapod, octopod, avian, serpentine, aquatic). Default: `v1.0-20240301`.| COMBO| No| ”v1.0-20240301"  
"v2.5-20260210”  
`rig_type`| Skeleton type. “auto” runs Tripo’s free rig check first and uses the recommended type. Default: “auto”.| COMBO| No| ”auto"  
"biped"  
"quadruped"  
"hexapod"  
"octopod"  
"avian"  
"serpentine"  
"aquatic”  
`spec`| Bone naming: Tripo native or Mixamo-compatible. Tripo cannot retarget its animation presets onto a v1.0 rig made with the mixamo spec; use tripo for Tripo: Retarget rigged model. Default: “tripo”.| COMBO| No| ”tripo"  
"mixamo”  
`out_format`| Output file format; the result arrives on the matching output. Default: “glb”.| COMBO| No| ”glb"  
"fbx”  
  
**Note:** The v1.0 model version (`v1.0-20240301`) only supports biped skeletons. If a non-biped `rig_type` is used with this version, the node raises an error and instructs you to use `v2.5-20260210` instead. **Note:** When `rig_type` is “auto”, Tripo first checks whether the model can be rigged and picks the recommended skeleton type. If Tripo reports that the model cannot be rigged, the node fails with an error. **Note:** The node expects Tripo to return a GLB or FBX file. If Tripo returns any other file type, the node raises an error. **Note:** Only the output matching `out_format` is populated: `GLB` when `out_format` is “glb”, and `FBX` when `out_format` is “fbx”. The other 3D output is empty.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model_file`| The generated rigged model file name (task ID plus format extension). Kept for backward compatibility only.| STRING  
`rig task_id`| The task ID for tracking the rig generation process.| RIG_TASK_ID  
`GLB`| The rigged model as a GLB 3D file. Populated when `out_format` is “glb”.| FILE3DGLB  
`FBX`| The rigged model as an FBX 3D file. Populated when `out_format` is “fbx”.| FILE3DFBX  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRigNode/en.md)

* * *

**Source fingerprint (SHA-256):** `b9c1b6d27b6278bcee4fc22e11c11e65cd22ea92cab3fc6c74f84d3deb2024d6`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/TripoRigNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/TripoRigNode)

[TripoRigCheckNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/TripoRigCheckNode)[TripoSegmentNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/TripoSegmentNode)

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
