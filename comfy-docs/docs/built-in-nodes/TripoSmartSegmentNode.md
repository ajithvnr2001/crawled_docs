---
url: https://docs.comfy.org/built-in-nodes/TripoSmartSegmentNode/
title: TripoSmartSegmentNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:14.321383+00:00
---

# TripoSmartSegmentNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/TripoSmartSegmentNode/

Tripo

# TripoSmartSegmentNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Splits a 3D model into semantically meaningful parts and gives each part a name.

Copy pageCopy page

Splits a 3D model into semantically meaningful parts and gives each part a name. It can either segment an existing model (provided through a task ID) or first generate a model from an image and then segment it. The resulting `segment task_id` can be used by other Tripo nodes, such as Complete Mesh Parts, Retopology, Texture model, and Convert model, in the same way as a Tripo: Segment Model result.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`source`| Segment an existing model, or generate a model from an image and segment it. The selected option determines which additional inputs appear.| DYNAMIC_COMBO| Yes| `"model"`  
`"image"`  
  
### 

​

Model Inputs

Shown when `source` is set to `"model"`.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model_task_id`| A GLB result. Quad (FBX) meshes must go through Tripo: Convert model (GLTF) first.| MODEL_TASK_ID| Yes| -  
`granularity`| How finely the model is split into parts (default: “medium”).| COMBO| No| `"coarse"`  
`"medium"`  
`"fine"`  
`hint`| Optional text naming the parts to look for, e.g. ‘game character with sword and armor’ (default: empty).| STRING| No| -  
  
### 

​

Image Inputs

Shown when `source` is set to `"image"`. Tripo first generates a model from the image, then segments it.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The image used to generate the model that will be segmented.| IMAGE| Yes| -  
`granularity`| How finely the model is split into parts (default: “medium”).| COMBO| No| `"coarse"`  
`"medium"`  
`"fine"`  
`hint`| Optional text naming the parts to look for, e.g. ‘game character with sword and armor’ (default: empty).| STRING| No| -  
  
**Notes:**

  * `granularity` and `hint` are shared by both `source` options and are optional. When `hint` is left empty, no hint is sent to the service.
  * When `source` is `"model"`, only GLB models are accepted. Other formats, such as quad (FBX) meshes, must be converted first with Tripo: Convert model (GLTF).
  * The task is polled until it reaches a terminal state, with an estimated duration of about 180 seconds. If Tripo returns an incomplete segmentation result, the node reports an error.
  * Price badge: approximately 0.85 USD when `source` is `"image"` and approximately 0.55 USD when `source` is `"model"` (values shown as approximate).



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`segment task_id`| Task ID of the segmentation task, usable as input for other Tripo nodes.| SEGMENT_TASK_ID  
`model task_id`| The model that was segmented (generated from the image, or imported).| MODEL_TASK_ID  
`GLB`| The segmented 3D model file.| FILE3DGLB  
`part_names`| Comma-separated names of the parts.| STRING  
`parts`| Tripo’s description of the parts it found.| STRING  
`mask`| Mask image produced by the segmentation.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSmartSegmentNode/en.md)

* * *

**Source fingerprint (SHA-256):** `ba041da49e20b1ac085770078cce6ac87ef70eee927ba0ee9e5655a058893f1c`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/TripoSmartSegmentNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/TripoSmartSegmentNode)

[TripoSegmentNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/TripoSegmentNode)[TripoTextToModelNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/TripoTextToModelNode)

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
