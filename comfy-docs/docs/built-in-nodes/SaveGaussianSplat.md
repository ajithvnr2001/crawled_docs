---
url: https://docs.comfy.org/built-in-nodes/SaveGaussianSplat/
title: SaveGaussianSplat - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:58.779903+00:00
---

# SaveGaussianSplat - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SaveGaussianSplat/

3D

# SaveGaussianSplat - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node saves a Gaussian splat 3D file to the output directory.

Copy pageCopy page

This node saves a Gaussian splat 3D file to the output directory. It handles the file saving process and provides preview data for the 3D viewport.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model_3d`| A gaussian splat 3D file.| FILE3D| Yes| SplatAny  
PLY  
SPLAT  
SPZ  
KSPLAT  
`filename_prefix`| The prefix for the saved filename (default: “3d/ComfyUI”).| STRING| Yes| Any valid filename prefix  
`viewport_state`| The current viewport state containing camera and model information.| LOAD3D| Yes| -  
`model_3d_info`| Additional model 3D information for the viewport.| LOAD3DMODELINFO| No| -  
`camera_info`| Camera information for the viewport preview.| LOAD3DCAMERA| No| -  
`width`| The width of the preview (default: 1024).| INT| Yes| 1 to 4096  
`height`| The height of the preview (default: 1024).| INT| Yes| 1 to 4096  
  
Note: If `camera_info` or `model_3d_info` are not provided, the node uses the corresponding values from `viewport_state` when available.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model_3d`| The Gaussian splat 3D file that was saved to the output directory.| FILE3D  
`model_3d_info`| Model 3D information for the viewport.| LOAD3DMODELINFO  
`camera_info`| Camera information for the viewport preview.| LOAD3DCAMERA  
`width`| The width of the preview.| INT  
`height`| The height of the preview.| INT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveGaussianSplat/en.md)

* * *

**Source fingerprint (SHA-256):** `f2d6b98d2ce1fe11df8ba440b7f46a21e2308966c15daa5ca0bdca7dab1726cc`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SaveGaussianSplat.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SaveGaussianSplat)

[Save3DAdvanced - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Save3DAdvanced)[SaveGLB - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SaveGLB)

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
