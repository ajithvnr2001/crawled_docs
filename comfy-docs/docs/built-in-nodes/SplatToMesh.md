---
url: https://docs.comfy.org/built-in-nodes/SplatToMesh/
title: SplatToMesh - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:04.216340+00:00
---

# SplatToMesh - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SplatToMesh/

Splat

# SplatToMesh - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node converts a 3D Gaussian splat into a colored mesh surface.

Copy pageCopy page

This node converts a 3D Gaussian splat into a colored mesh surface. It works by rasterizing the gaussians onto a density grid, extracting an iso-surface at a chosen density level, and then applying optional smoothing and cleanup to produce a clean, colored triangle mesh.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`splat`| The input gaussian splat to convert to a mesh| SPLAT| Yes| -  
`resolution`| Density-grid resolution along the longest axis. Higher values produce finer surface detail but require more VRAM and processing time (grows with resolution^3). Default: 384| INT| Yes| 64 - 768 (step 16)  
`kernel`| Maximum splat half-width in voxels. Each gaussian is rasterized over a window sized to its own 3-sigma, capped at this value. Small surfels stay cheap while large ones aren’t truncated. Raise if sparse splats leave gaps. Default: 5| INT| Yes| 1 - 8  
`smooth`| Taubin mesh-smoothing iterations. Smooths the surface without shrinking it (volume-preserving), unlike blurring the density. 0 means no smoothing. Default: 0| INT| Yes| 0 - 60  
`level`| Iso-surface level. Auto-picked by Otsu thresholding; this value biases the auto-pick (1.0 = auto, lower values produce fatter/more-connected surfaces, higher values produce thinner/tighter surfaces). Default: 0.4| FLOAT| Yes| 0.0 - 2.0 (step 0.01)  
`min_component`| Drops connected components smaller than this many vertices. Removes detached floater blobs and the inner shell of double walls. 0 keeps all components. Default: 500| INT| Yes| 0 - 100000 (step 50)  
`min_opacity`| Ignores gaussians fainter than this value before meshing. Default: 0.02| FLOAT| Yes| 0.0 - 1.0 (step 0.01)  
`color_sharpen`| Crisps up the vertex texture. 1.0 gives physically-correct blend; higher values bias each voxel’s color toward its dominant gaussian instead of averaging neighbors (de-smears the texture). Affects color only, not geometry. Default: 2.0| FLOAT| Yes| 1.0 - 8.0 (step 0.5)  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`mesh`| The extracted colored mesh with unlit rendering (emissive-like) to match the splat appearance| MESH  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplatToMesh/en.md)

* * *

**Source fingerprint (SHA-256):** `5a7060c26252b587ce533e5682abe880a6fcc83f6671232489c3de64b094cd84`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SplatToMesh.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SplatToMesh)

[SplatToFile3D - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SplatToFile3D)[TransformSplat - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/TransformSplat)

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
