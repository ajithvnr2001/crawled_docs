---
url: https://docs.comfy.org/built-in-nodes/DecimateMesh/
title: DecimateMesh - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:50.049444+00:00
---

# DecimateMesh - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/DecimateMesh/

Mesh

# DecimateMesh - ComfyUI Built-in Node Documentation

Copy pageCopy page

Simplifies a 3D mesh to a target face count using QEM (quadric error metric) simplification, running the computation on the active compute device.

Copy pageCopy page

Simplifies a 3D mesh to a target face count using QEM (quadric error metric) simplification, running the computation on the active compute device. The `"midpoint"` placement mode is the cumesh-faithful preset that provides the best quality while preserving thin features such as hair, whereas `"qem"` places vertices at the QEM-optimal position with optional line and feature-edge controls. The output mesh stays welded.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`mesh`| The 3D mesh to simplify.| MESH| Yes| -  
`target_face_count`| Target max faces. 0 disables. (default: 200000)| INT| Yes| 0 to 50000000  
`placement_mode`| midpoint: cumesh-faithful (recommended). qem: QEM-optimal placement. (default: `"midpoint"`)| DYNAMIC_COMBO| Yes| `"midpoint"`  
`"qem"`  
  
### 

​

Midpoint Inputs

The `"midpoint"` placement mode does not expose additional sub-parameters; it uses the default midpoint placement preset.

### 

​

QEM Inputs

The following sub-parameters appear in the interface only when `placement_mode` is set to `"qem"`.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`line_quadric_weight`| Per-edge line-quadric weight; preserves sharp ridges/valleys. 0 = off. (default: 0.0)| FLOAT| No| 0.0 to 100.0  
`feature_edge_quadric_weight`| Extra quadric weight on dihedral feature edges (creases). 0 = off. (default: 0.0)| FLOAT| No| 0.0 to 1000.0  
`feature_edge_min_dihedral_deg`| Minimum dihedral angle (degree) to count an edge as a feature edge. (default: 30.0)| FLOAT| No| 0.0 to 180.0  
`clamp_v_to_edge`| Project the QEM-optimal position onto the collapsed edge segment. (default: true)| BOOLEAN| No| `true`  
`false`  
  
Note: Decimation is skipped when `target_face_count` is 0 or when the mesh already has no more faces than the target. The node displays a face reduction summary on itself, for example `faces: 1.23M → 200K (-84%)`.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`mesh`| The simplified mesh with the reduced face count; connectivity stays welded.| MESH  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DecimateMesh/en.md)

* * *

**Source fingerprint (SHA-256):** `55336e5b52e27d940e5402ecd74fd0ac847a1c6acd35955eccf72aab8ed940f9`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/DecimateMesh.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/DecimateMesh)

[ComfyUI Built-in NodesPrevious](https://docs.comfy.org/built-in-nodes/overview)[FillHoles - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/FillHoles)

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
