---
url: https://docs.comfy.org/built-in-nodes/TripoMeshCompleteNode/
title: TripoMeshCompleteNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:12.717576+00:00
---

# TripoMeshCompleteNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/TripoMeshCompleteNode/

Tripo

# TripoMeshCompleteNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Completes the parts of a segmented 3D model and repairs missing or damaged regions of the mesh.

Copy pageCopy page

Completes the parts of a segmented 3D model and repairs missing or damaged regions of the mesh. It takes the task ID of a Tripo mesh segmentation result, requests the completion job from Tripo, and waits for it to finish. You can optionally limit the work to specific part names. The completed model is returned as a GLB file.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`segment_task_id`| Task ID of a Tripo mesh segmentation task. The parts of the segmented model from this task are completed. Connect the SEGMENT_TASK_ID output of a previous Tripo mesh segmentation node.| SEGMENT_TASK_ID| Yes| Single task ID  
`part_names`| Comma-separated part names to complete. Empty completes every part. Default: empty string. Extra spaces around names are removed and duplicate names are ignored.| STRING| No| Free text or empty  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model_file`| File name of the completed model. This output exists for backward compatibility only.| STRING  
`model task_id`| Task ID of the completed Tripo mesh completion task. Can be used as input by other Tripo nodes that expect a model task ID.| MODEL_TASK_ID  
`GLB`| The completed 3D model with repaired parts, downloaded as a GLB file.| GLB  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoMeshCompleteNode/en.md)

* * *

**Source fingerprint (SHA-256):** `c5709231fa2e33e6f3c9b25669acca1d4ae9adb882b90210d703aeddc0d11ecc`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/TripoMeshCompleteNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/TripoMeshCompleteNode)

[TripoImportModelNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/TripoImportModelNode)[TripoMultiviewToModelNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/TripoMultiviewToModelNode)

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
