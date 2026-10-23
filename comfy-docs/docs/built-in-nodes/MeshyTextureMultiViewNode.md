---
url: https://docs.comfy.org/built-in-nodes/MeshyTextureMultiViewNode/
title: MeshyTextureMultiViewNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:31.970402+00:00
---

# MeshyTextureMultiViewNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MeshyTextureMultiViewNode/

Meshy

# MeshyTextureMultiViewNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node textures a previously created 3D model using 1 to 4 reference views of the same object.

Copy pageCopy page

This node textures a previously created 3D model using 1 to 4 reference views of the same object. You provide the task ID of the original model and the reference images; the node sends them to the Meshy service, waits for the job to finish, and returns the textured model as GLB and FBX files.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The AI model used for the texturing job. Only “meshy-7” is currently available.| COMBO| Yes| `"meshy-7"`  
`meshy_task_id`| The task ID of the previously created 3D model to be textured.| MESHY_TASK_ID| Yes| —  
`multiview_images`| Reference views of the same object. The first image is the primary (front) view; the order of the remaining views does not matter. Growable slot: connect 1 to 4 images (`image_1` to `image_4`).| IMAGE| Yes| 1 to 4 images  
`enable_original_uv`| Use the original UV of the model instead of generating new UVs. When enabled, Meshy preserves existing textures from the uploaded model. If the model has no original UV, the quality of the output might not be as good. (default: True; advanced option)| BOOLEAN| No| True / False  
`pbr`| Enables PBR (physically based rendering) texture generation. (default: False; advanced option)| BOOLEAN| No| True / False  
`texture_resolution`| Base color texture resolution. Higher resolutions capture more surface detail.| COMBO| Yes| `"2k"`  
`"4k"`  
`"8k"`  
  
**Note:** `multiview_images` must contain between 1 and 4 images. The node validates this at runtime and raises an error if the count is outside this range. If a connected image contains a batch of multiple images, each image in the batch counts toward the limit. The first image is used as the primary (front) view; the order of the remaining images does not matter.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model_file`| Model file name. This output is kept for backward compatibility only.| STRING  
`meshy_task_id`| Task ID of the texturing job.| MESHY_TASK_ID  
`GLB`| The textured 3D model downloaded in GLB format.| FILE3DGLB  
`FBX`| The textured 3D model downloaded in FBX format.| FILE3DFBX  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextureMultiViewNode/en.md)

* * *

**Source fingerprint (SHA-256):** `3a08d003683a182121471a064833c09b932c7c84c20fd5cb5ac0285e135b2b7e`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MeshyTextureMultiViewNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MeshyTextureMultiViewNode)

[MeshyTextToModelNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/MeshyTextToModelNode)[MeshyTextureNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/MeshyTextureNode)

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
