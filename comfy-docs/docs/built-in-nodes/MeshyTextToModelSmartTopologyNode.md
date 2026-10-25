---
url: https://docs.comfy.org/built-in-nodes/MeshyTextToModelSmartTopologyNode/
title: MeshyTextToModelSmartTopologyNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-25T12:24:47.181237+00:00
---

# MeshyTextToModelSmartTopologyNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MeshyTextToModelSmartTopologyNode/

3d

# MeshyTextToModelSmartTopologyNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node generates a game-ready triangle mesh at a target face count with Meshy T2.5.

Copy pageCopy page

This node generates a game-ready triangle mesh at a target face count with Meshy T2.5. The topology is built at the requested polycount instead of being decimated afterwards, so the result is ready for a game engine without a separate retopology pass.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The Meshy model version to use for generation.| COMBO| Yes| `"meshy-t2.5"`  
`prompt`| The text description of the 3D model to generate.| STRING| Yes| 1 to 800 characters  
`target_polycount`| Approximate number of triangles in the generated mesh. Default: 15000.| INT| Yes| 100 to 30000  
`pose_mode`| The pose of the generated character. An empty string requests no specific pose. This is an advanced setting. Default: `""` (empty string).| COMBO| Yes| `""`  
`"A-pose"`  
`"T-pose"`  
`seed`| Seed controls whether the node should re-run; results are non-deterministic regardless of seed. Default: 42.| INT| Yes| 0 to 2147483647  
  
**Constraints:**

  * The prompt must contain between 1 and 800 characters.
  * `target_polycount` is the number of triangles the mesh is built from, not a limit applied after generation.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`meshy_task_id`| The unique identifier of the Meshy API task.| MESHY_TASK_ID  
`GLB`| The generated 3D model in GLB format.| FILE3DGLB  
`FBX`| The generated 3D model in FBX format.| FILE3DFBX  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextToModelSmartTopologyNode/en.md)

* * *

**Source fingerprint (SHA-256):** `9fcdc846a4ba39cf3d099629637fbb0cf6d9c8d65bcee8aff5ec6ac5c76b6af3`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MeshyTextToModelSmartTopologyNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MeshyTextToModelSmartTopologyNode)

[MeshyImageToModelSmartTopologyNode](https://docs.comfy.org/built-in-nodes/MeshyImageToModelSmartTopologyNode)[ByteDanceSeedAudio](https://docs.comfy.org/built-in-nodes/ByteDanceSeedAudio)
