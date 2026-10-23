---
url: https://docs.comfy.org/built-in-nodes/SaveGLB/
title: SaveGLB - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:58.497365+00:00
---

# SaveGLB - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SaveGLB/

3D

# SaveGLB - ComfyUI Built-in Node Documentation

Copy pageCopy page

The SaveGLB node saves 3D mesh data or 3D file inputs to the output directory.

Copy pageCopy page

The SaveGLB node saves 3D mesh data or 3D file inputs to the output directory. It accepts mesh data and common 3D file formats (GLB, GLTF, OBJ, FBX, STL, USDZ, PLY, SPLAT, SPZ, KSPLAT) and exports them with the specified filename prefix. Mesh inputs are written as GLB files, one per batch item, while 3D file inputs are saved in their original format.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`mesh`| Mesh or 3D file to save| MESH or FILE3D| Yes| Mesh data  
GLB  
GLTF  
OBJ  
FBX  
STL  
USDZ  
PLY  
SPLAT  
SPZ  
KSPLAT  
Any splat format  
Any point cloud format  
Any 3D file format  
`filename_prefix`| The prefix for the output filename (default: “3d/ComfyUI”). The prefix can include a subfolder path, so files are saved under the “3d” subfolder of the output directory by default| STRING| No| -  
  
Note: When the `mesh` input is a 3D file, the node saves it using its original format extension (GLB is used if the file has no format). When it is mesh data, each item in the batch is saved as a separate `.glb` file; empty items (with no vertices or faces) are skipped with a warning. Output filenames follow the pattern `{filename_prefix}_{counter:05}_.{ext}` with an incrementing counter. Workflow metadata (prompt and extra PNG info) is embedded in the saved files when metadata is enabled.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`ui`| Displays the saved 3D files in the user interface with filename, subfolder, and type information| UI  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveGLB/en.md)

* * *

**Source fingerprint (SHA-256):** `366b56c4fd6e3c2f7783222990792a982857b3419a2becfa27ddfa37853bb22c`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SaveGLB.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SaveGLB)

[SaveGaussianSplat - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SaveGaussianSplat)[SavePointCloud - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SavePointCloud)

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
