---
url: https://docs.comfy.org/built-in-nodes/RotateMesh/
title: RotateMesh - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:53.274785+00:00
---

# RotateMesh - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/RotateMesh/

Mesh

# RotateMesh - ComfyUI Built-in Node Documentation

Copy pageCopy page

Rotate a 3D mesh around the world axes using either Euler XYZ angles (in degrees) or a quaternion.

Copy pageCopy page

Rotate a 3D mesh around the world axes using either Euler XYZ angles (in degrees) or a quaternion. In Euler XYZ mode the rotations are applied as X then Y then Z; in quaternion mode the (w, x, y, z) quaternion is automatically normalized. The rotation is applied to the mesh’s vertices, and the normals and tangents are rotated as well so lighting and shading remain correct.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`mode`| The rotation mode to use. `"euler_xyz"` applies rotation as X then Y then Z angles about the world axes (in degrees). `"quaternion"` uses a (w, x, y, z) quaternion that is automatically normalized.| DYNAMIC_COMBO| Yes| `"euler_xyz"`  
`"quaternion"`  
`mesh`| The 3D mesh to rotate.| MESH| Yes| —  
  
### 

​

euler_xyz Inputs

These inputs appear when `mode` is set to `"euler_xyz"`.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`angle_x`| Rotation around the X axis in degrees. (default: 0.0)| FLOAT| No| -360.0 to 360.0 (step: 0.1)  
`angle_y`| Rotation around the Y axis in degrees. (default: 0.0)| FLOAT| No| -360.0 to 360.0 (step: 0.1)  
`angle_z`| Rotation around the Z axis in degrees. (default: 0.0)| FLOAT| No| -360.0 to 360.0 (step: 0.1)  
  
### 

​

quaternion Inputs

These inputs appear when `mode` is set to `"quaternion"`.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`qw`| W component of the quaternion (w, x, y, z). (default: 1.0)| FLOAT| No| -1.0 to 1.0 (step: 0.001)  
`qx`| X component of the quaternion (w, x, y, z). (default: 0.0)| FLOAT| No| -1.0 to 1.0 (step: 0.001)  
`qy`| Y component of the quaternion (w, x, y, z). (default: 0.0)| FLOAT| No| -1.0 to 1.0 (step: 0.001)  
`qz`| Z component of the quaternion (w, x, y, z). (default: 0.0)| FLOAT| No| -1.0 to 1.0 (step: 0.001)  
  
**Note:** When `mode` is `"euler_xyz"` and all three angles are 0.0, or when `mode` is `"quaternion"` and the quaternion is the identity (1, 0, 0, 0), the mesh is returned unchanged. The quaternion is automatically normalized before use; if its magnitude is below 1e-8, the node raises an error.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`mesh`| The rotated mesh. Vertices are rotated, and normals are rotated as directions. Tangents have their X, Y, Z components rotated while the W (handedness) component is kept unchanged.| MESH  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RotateMesh/en.md)

* * *

**Source fingerprint (SHA-256):** `38b120a3f719264d1269275ecfefa145b507c688735e4a461bb89517c697674f`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/RotateMesh.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/RotateMesh)

[RenderMesh - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/RenderMesh)[WeldVertices - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/WeldVertices)

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
