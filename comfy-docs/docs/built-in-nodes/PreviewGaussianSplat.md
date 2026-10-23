---
url: https://docs.comfy.org/built-in-nodes/PreviewGaussianSplat/
title: PreviewGaussianSplat - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:44.365731+00:00
---

# PreviewGaussianSplat - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/PreviewGaussianSplat/

3D

# PreviewGaussianSplat - ComfyUI Built-in Node Documentation

Copy pageCopy page

The PreviewGaussianSplat node displays a 3D gaussian splat file in a preview window without saving it to the ComfyUI output directory.

Copy pageCopy page

The PreviewGaussianSplat node displays a 3D gaussian splat file in a preview window without saving it to the ComfyUI output directory. It accepts a 3D model file in various gaussian splat formats, saves a temporary copy for previewing, and passes the model data through for further processing in the workflow. This node is marked as experimental and acts as an output node.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model_3d`| A gaussian splat 3D file.| FILE3D| Yes| splat  
ply  
spz  
ksplat  
`model_3d_info`| Optional metadata information about the 3D model. When not connected, the node uses the model info from `viewport_state`.| LOAD3DMODELINFO| No| -  
`viewport_state`| The current state of the 3D viewport, including camera and model information.| LOAD3D| Yes| -  
`camera_info`| Optional camera information for the preview. When not connected, the node uses the camera info from `viewport_state`.| LOAD3DCAMERA| No| -  
`width`| The width of the preview render in pixels (default: 1024).| INT| Yes| 1 to 4096  
`height`| The height of the preview render in pixels (default: 1024).| INT| Yes| 1 to 4096  
  
Note: When `camera_info` or `model_3d_info` are not provided, the node falls back to the camera and model information stored in `viewport_state`. If `viewport_state` is not a valid viewport state object, it is treated as empty.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model_3d`| The input 3D gaussian splat file, passed through unchanged.| FILE3D  
`model_3d_info`| Metadata information about the 3D model, either from the input or derived from the viewport state.| LOAD3DMODELINFO  
`camera_info`| Camera information for the preview, either from the input or derived from the viewport state.| LOAD3DCAMERA  
`width`| The width of the preview render.| INT  
`height`| The height of the preview render.| INT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewGaussianSplat/en.md)

* * *

**Source fingerprint (SHA-256):** `4fc86c692724ce406f9bba9aa9ebe22a92e72a25d11abf8f55d1b99044bb1acd`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/PreviewGaussianSplat.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/PreviewGaussianSplat)

[Preview3DAnimation - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Preview3DAnimation)[PreviewPointCloud - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/PreviewPointCloud)

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
