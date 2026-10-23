---
url: https://docs.comfy.org/built-in-nodes/TripoSegmentNode/
title: TripoSegmentNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:14.803338+00:00
---

# TripoSegmentNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/TripoSegmentNode/

Tripo

# TripoSegmentNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node splits a 3D model into individual parts.

Copy pageCopy page

This node splits a 3D model into individual parts. It sends the model to the Tripo segmentation service, waits for the job to finish, and returns the segmented model in GLB format along with a comma-separated list of part names. These part names feed downstream steps such as Tripo: Complete Mesh Parts, Tripo: Retopology and Tripo: Convert model.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model_task_id`| The task ID of the 3D model to be segmented into parts.| MODEL_TASK_ID| Yes| N/A  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model_file`| Output file name of the segmented GLB model, in the form `<task_id>.glb`. Kept for backward compatibility only.| STRING  
`segment task_id`| The task ID of the segmentation job that produced the result.| SEGMENT_TASK_ID  
`GLB`| The segmented 3D model, as a GLB file.| GLB  
`part_names`| Comma-separated names of the parts.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSegmentNode/en.md)

* * *

**Source fingerprint (SHA-256):** `3218f87bfdc347d58b639cbe57b01cf7625c95c753bf381e35b4a28376eeb0e8`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/TripoSegmentNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/TripoSegmentNode)

[TripoRigNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/TripoRigNode)[TripoSmartSegmentNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/TripoSmartSegmentNode)

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
