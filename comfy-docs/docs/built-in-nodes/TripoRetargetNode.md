---
url: https://docs.comfy.org/built-in-nodes/TripoRetargetNode/
title: TripoRetargetNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:13.690290+00:00
---

# TripoRetargetNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/TripoRetargetNode/

Tripo

# TripoRetargetNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The TripoRetargetNode applies a preset animation to an existing rigged 3D model.

Copy pageCopy page

The TripoRetargetNode applies a preset animation to an existing rigged 3D model. It takes the task ID of a model that was previously rigged, sends a retarget request to the Tripo API, and downloads the resulting animated file. The animated model can be returned as GLB or FBX, with optional mesh geometry and optional in-place playback.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`original_model_task_id`| The task ID of the previously rigged 3D model to retarget. The referenced task must be a rig task.| RIG_TASK_ID| Yes| -  
`animation`| The animation preset to apply to the rigged model. `preset:*` animations work with both rig models. `preset:biped:*` animations are made for rigs from model v1.0-20240301; a v2.5 rig accepts only chop, climb, dive, fall, hurt, idle, jump, run, shoot, slash, turn and walk.| COMBO| Yes| `"preset:idle"`  
`"preset:walk"`  
`"preset:run"`  
`"preset:dive"`  
`"preset:climb"`  
`"preset:jump"`  
`"preset:slash"`  
`"preset:shoot"`  
`"preset:hurt"`  
`"preset:fall"`  
`"preset:turn"`  
`"preset:quadruped:walk"`  
`"preset:hexapod:walk"`  
`"preset:octopod:walk"`  
`"preset:serpentine:march"`  
`"preset:aquatic:march"`  
plus additional `"preset:biped:*"` options shown in the UI  
`out_format`| Output file format; the result arrives on the matching output. (default: glb)| COMBO| No| `"glb"`  
`"fbx"`  
`export_with_geometry`| Include the mesh in the export; off exports the animated skeleton only. (default: True)| BOOLEAN| No| True  
False  
`animate_in_place`| Play the animation in place, without root displacement. (default: False)| BOOLEAN| No| True  
False  
`auth_token_comfy_org`| Authentication token for Comfy.org API access (hidden parameter).| AUTH_TOKEN_COMFY_ORG| No| -  
`api_key_comfy_org`| API key for Comfy.org service access (hidden parameter).| API_KEY_COMFY_ORG| No| -  
`unique_id`| Unique identifier for tracking the operation (hidden parameter).| UNIQUE_ID| No| -  
  
Note: Animations in the `preset:*` group work with both rig models. Animations in the `preset:biped:*` group are made for rigs from model v1.0-20240301; a v2.5 rig accepts only chop, climb, dive, fall, hurt, idle, jump, run, shoot, slash, turn and walk. If the referenced rig was created with the Mixamo spec and a model version starting with `v1.0`, the retargeting call fails with an error. The requested output format must be GLB or FBX; if the service returns any other file type, the node raises an error.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model_file`| The generated animated 3D model file (for backward compatibility only).| STRING  
`retarget task_id`| The task ID for tracking the retargeting operation.| RETARGET_TASK_ID  
`GLB`| The animated 3D model in GLB format. Populated when `out_format` is glb.| FILE3DGLB  
`FBX`| The animated 3D model in FBX format. Populated when `out_format` is fbx.| FILE3DFBX  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetargetNode/en.md)

* * *

**Source fingerprint (SHA-256):** `4814858b940ece13f85010ff81fcdac0258fe8550aebd914be2613e8f40c0e5a`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/TripoRetargetNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/TripoRetargetNode)

[TripoPSeriesTextToModelNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/TripoPSeriesTextToModelNode)[TripoRetopologyNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/TripoRetopologyNode)

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
