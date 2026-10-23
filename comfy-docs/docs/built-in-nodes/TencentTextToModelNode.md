---
url: https://docs.comfy.org/built-in-nodes/TencentTextToModelNode/
title: TencentTextToModelNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:08.361100+00:00
---

# TencentTextToModelNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/TencentTextToModelNode/

Tencent

# TencentTextToModelNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node uses Tencent’s Hunyuan3D Pro API to generate a 3D model from a text description.

Copy pageCopy page

This node uses Tencent’s Hunyuan3D Pro API to generate a 3D model from a text description. It sends a request to create a generation task, polls for the result, and downloads the final model files in GLB and OBJ formats.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The version of the Hunyuan3D model to use. The LowPoly option is unavailable for the `3.1` model.| COMBO| Yes| `"3.0"`  
`"3.1"`  
`prompt`| The text description of the 3D model to generate. Supports up to 1024 characters.| STRING| Yes| -  
`face_count`| The target number of faces for the generated 3D model. Default: 500000.| INT| Yes| 3000 - 1500000  
`generate_type`| The type of 3D model to generate. The available options and their associated parameters are:  
\- **Normal** : Generates a standard model. Includes a `pbr` parameter (default: `False`).  
\- **LowPoly** : Generates a low-polygon model. Includes `polygon_type` (`"triangle"` or `"quadrilateral"`) and `pbr` (default: `False`) parameters.  
\- **Geometry** : Generates a geometry-only model.| DYNAMICCOMBO| Yes| `"Normal"`  
`"LowPoly"`  
`"Geometry"`  
`seed`| A seed value for the generation. Results are non-deterministic regardless of seed. Setting a new seed controls whether the node should re-run. Default: 0.| INT| No| 0 - 2147483647  
  
**Note:** The `generate_type` parameter is dynamic. Selecting `"LowPoly"` will reveal additional inputs for `polygon_type` and `pbr`. Selecting `"Normal"` will reveal an input for `pbr`. Selecting `"Geometry"` will not reveal any additional inputs. **Constraint:** The `"LowPoly"` generate type cannot be used with the `"3.1"` model.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model_file`| A legacy output for backward compatibility.| STRING  
`GLB`| The generated 3D model in the GLB file format.| FILE3DGLB  
`OBJ`| The generated 3D model in the OBJ file format.| FILE3DOBJ  
`texture_image`| The texture image extracted from the generated OBJ file, if available.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentTextToModelNode/en.md)

* * *

**Source fingerprint (SHA-256):** `8110b6a70cdd26d5d0dcb791e654a6292895693e25076b982951c65f787422d6`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/TencentTextToModelNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/TencentTextToModelNode)

[TencentSmartTopologyNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/TencentSmartTopologyNode)[TripoConversionNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/TripoConversionNode)

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
