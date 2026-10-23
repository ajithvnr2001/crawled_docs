---
url: https://docs.comfy.org/built-in-nodes/MeshyAnimateModelNode/
title: MeshyAnimateModelNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:31.467664+00:00
---

# MeshyAnimateModelNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MeshyAnimateModelNode/

Meshy

# MeshyAnimateModelNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node applies a specific animation action to a previously rigged 3D character using the Meshy service.

Copy pageCopy page

This node applies a specific animation action to a previously rigged 3D character using the Meshy service. It takes a task ID from an earlier rigging operation and an action ID to select the desired animation from the library, then returns the animated model in both GLB and FBX file formats.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`rig_task_id`| The unique task ID from a previously completed Meshy character rigging operation.| MESHY_RIGGED_TASK_ID| Yes| N/A  
`action_id`| The ID number of the animation action to apply. Visit <https://docs.meshy.ai/en/api/animation-library> for a list of available values. (default: 0)| INT| Yes| 0 to 696  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model_file`| A string identifier for the animated model. This output is provided for backward compatibility only.| STRING  
`GLB`| The animated 3D model file in GLB format.| FILE3DGLB  
`FBX`| The animated 3D model file in FBX format.| FILE3DFBX  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyAnimateModelNode/en.md)

* * *

**Source fingerprint (SHA-256):** `760e94d3a92910051d9b473545191842dc9672e6c4a59c3d1cd9cfdc5eb2589d`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MeshyAnimateModelNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MeshyAnimateModelNode)

[TrainLoraNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/TrainLoraNode)[MeshyImageToModelNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/MeshyImageToModelNode)

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
