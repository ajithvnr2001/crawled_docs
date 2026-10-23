---
url: https://docs.comfy.org/built-in-nodes/PreviewPointCloud/
title: PreviewPointCloud - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:45.009022+00:00
---

# PreviewPointCloud - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/PreviewPointCloud/

3D

# PreviewPointCloud - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Preview Point Cloud node lets you view a 3D point cloud file in the ComfyUI interface without saving it to the ComfyUI output directory.

Copy pageCopy page

The Preview Point Cloud node lets you view a 3D point cloud file in the ComfyUI interface without saving it to the ComfyUI output directory. It saves the point cloud to a temporary location and displays it in a 3D preview window, while also passing the model data, model information, camera information, and preview dimensions through for further processing.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model_3d`| Point cloud file (.ply)| FILE3D| Yes| -  
`model_3d_info`| Information about the 3D model| LOAD3DMODELINFO| No| -  
`viewport_state`| The current state of the 3D viewport| LOAD3D| Yes| -  
`camera_info`| Camera information for the 3D view| LOAD3DCAMERA| No| -  
`width`| Width of the preview window (default: 1024)| INT| Yes| 1 to 4096  
`height`| Height of the preview window (default: 1024)| INT| Yes| 1 to 4096  
  
Note: `model_3d_info` and `camera_info` are optional advanced inputs. When they are not connected, the node falls back to the corresponding values stored in `viewport_state`. The point cloud file is written to ComfyUI’s temporary directory rather than the output directory. This is an output (terminal) node, so it is primarily used to display the preview in the interface.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model_3d`| The point cloud model data| FILE3D  
`model_3d_info`| Information about the 3D model| LOAD3DMODELINFO  
`camera_info`| Camera information for the 3D view| LOAD3DCAMERA  
`width`| Width of the preview window| INT  
`height`| Height of the preview window| INT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewPointCloud/en.md)

* * *

**Source fingerprint (SHA-256):** `a0b13d9d5658343a6a7c25408d5e5cd9249c92264b76aa448a6553b370f4d782`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/PreviewPointCloud.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/PreviewPointCloud)

[PreviewGaussianSplat - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/PreviewGaussianSplat)[Save3DAdvanced - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Save3DAdvanced)

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
