---
url: https://docs.comfy.org/built-in-nodes/RemeshMesh/
title: RemeshMesh - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-18T12:01:21.601062+00:00
---

# RemeshMesh - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/RemeshMesh/

Mesh

# RemeshMesh - ComfyUI Built-in Node Documentation

Copy pageCopy page

Remesh Mesh rebuilds a mesh with a clean, uniform tessellation by sampling a narrow-band distance field around the original surface and extracting it with Dual

Copy pageCopy page

Remesh Mesh rebuilds a mesh with a clean, uniform tessellation by sampling a narrow-band distance field around the original surface and extracting it with Dual Contouring. This normalizes messy, non-manifold, or self-intersecting topology, and is meant to be run before Decimate Mesh to reach an exact face count. Processing runs on the active compute device and the output mesh stays welded.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`mesh`| The input mesh to remesh.| MESH| Yes| —  
`resolution`| Voxel grid resolution (output density). 256 ~ 100k faces, 512 ~ 1M. For an exact face count, follow with Decimate Mesh. (default: 512)| INT| Yes| 32 - 2048  
`sign_mode`| Surface extraction mode. “udf” is robust to messy/non-manifold input; “sdf” produces a clean single surface with QEF (Quadratic Error Function) sharp-feature recovery, but needs consistent winding. “solid” builds one watertight solid from messy input: a global inside/outside graph cut (CelloCut) removes double shells and closes small holes. Slower. Selecting a mode reveals its specific sub-options. (default: “udf”)| DYNAMIC_COMBO| Yes| ”udf"  
"sdf"  
"solid”  
`band`| Narrow-band width in voxel units. In UDF mode also offsets the surface. In solid mode it is the closing radius: creases are filleted and gaps bridged at this size, the surface sits half a voxel out. (advanced, default: 1.0)| FLOAT| Yes| 0.5 - 4.0  
`project_back`| Linearly interpolate vertices toward the original surface (0 = pure DC, 1 = snapped). (advanced, default: 0.0)| FLOAT| Yes| 0.0 - 1.0  
`fix_poles`| Collapse valence-3 vertex pairs (DC T-junction artifact). (advanced, default: false)| BOOLEAN| Yes| true / false  
`smooth_iters`| Taubin smoothing iterations (0 = off). 2-3 cleans DC staircase-like artifacts; higher over-smooth QEF edges. (default: 0)| INT| Yes| 0 - 20  
`drop_small_components`| Drop components below this fraction of the largest’s face count. 0 disables. (advanced, default: 0.01)| FLOAT| Yes| 0.0 - 0.5  
`precluster_max_verts`| Cap input vertex count before the field queries; inputs above this are cluster-decimated to it first. Prevents OOM on huge meshes. (advanced, default: 20,000,000)| INT| Yes| 0 - 100,000,000  
  
### 

​

”udf” Mode Inputs

These parameters appear when `sign_mode` is set to `"udf"`.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`qef`| QEF (Quadratic Error Function) vertex placement: sharp edges on hard-surface input, jagged creases on organic input. (advanced, default: false)| BOOLEAN| No| true / false  
`drop_inverted_components`| Drop inward-normal (negative-volume) closed components — the UDF inner shell. (advanced, default: false)| BOOLEAN| No| true / false  
`drop_enclosed_components`| Drop components inside the largest’s bbox that fail a point-in-mesh raycast. Disable for legitimate nested parts. (advanced, default: false)| BOOLEAN| No| true / false  
  
### 

​

”sdf” Mode Inputs

These parameters appear when `sign_mode` is set to `"sdf"`.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`qef`| QEF (Quadratic Error Function) dual-vertex placement (recovers sharp features) vs edge-crossing centroid. (default: true)| BOOLEAN| No| true / false  
`manifold`| Manifold Dual Contouring: 1-4 dual verts/voxel for multi-sheet cases. Slower. (default: false)| BOOLEAN| No| true / false  
  
### 

​

”solid” Mode Inputs

These parameters appear when `sign_mode` is set to `"solid"`.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`fill`| Cost of closing an opening relative to following the surface. Lower closes larger openings (0 puts a lid on a cup); higher only closes small holes and cracks. (default: 20.0)| FLOAT| No| 0.0 - 1000.0  
`qef`| QEF (Quadratic Error Function) vertex placement: sharp edges on hard-surface input, jagged creases on organic input. (advanced, default: false)| BOOLEAN| No| true / false  
  
Note: The `qef` option has a different default depending on the selected mode — false in “udf” and “solid” modes, true in “sdf” mode. When `precluster_max_verts` is greater than 0 and the input mesh has more vertices than this value, the mesh is cluster-decimated down to that target before the field queries. After processing, the node displays the input-to-output face count change on the node (for example, “faces: 1.23M → 200K (-84%)”).

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`mesh`| The remeshed mesh with uniform tessellation and welded topology. Vertex colors are preserved when present on the input; any UVs, normals, and tangents are not carried over.| MESH  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RemeshMesh/en.md)

* * *

**Source fingerprint (SHA-256):** `d2869c681e0485f5946a53f0582188ded2183ecd741ea1ff6a591932b18b5abe`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/RemeshMesh.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/RemeshMesh)

[PaintMesh - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/PaintMesh)[RenderMesh - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/RenderMesh)

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
