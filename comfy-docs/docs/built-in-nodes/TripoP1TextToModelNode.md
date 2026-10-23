---
url: https://docs.comfy.org/built-in-nodes/TripoP1TextToModelNode/
title: TripoP1TextToModelNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-18T12:01:27.859541+00:00
---

# TripoP1TextToModelNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/TripoP1TextToModelNode/

Tripo

# TripoP1TextToModelNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Tripo P1 text-to-3D. This node generates a 3D model from a text description using the Tripo P1 API.

Copy pageCopy page

Tripo P1 text-to-3D. This node generates a 3D model from a text description using the Tripo P1 API. It is optimized for creating low-poly, game-ready meshes with stable topology, making it suitable for real-time applications.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`output_mode`| Controls whether the generated model contains only geometry or also color/PBR textures. “Geometry only” returns an untextured mesh. “Textured” adds color/PBR maps and reveals the texture options below.| DYNAMIC_COMBO| Yes| `"Geometry only"`  
`"Textured"`  
`prompt`| The text description of the 3D model you want to generate. Up to 1024 characters. Required and cannot be empty.| STRING| Yes| Up to 1024 characters  
`negative_prompt`| A text description of what you do not want in the generated model. Up to 255 characters. Default: not set.| STRING| No| Up to 255 characters  
`image_seed`| A seed value used to control randomness. Default: 42.| INT| No| 0 to 2147483647  
`face_limit`| Target face count, 48-20000. -1 lets Tripo pick adaptively. Default: -1.| INT| No| -1 to 20000  
`model_seed`| A seed value used to control randomness. Default: 42.| INT| No| 0 to 2147483647  
`auto_size`| Scale the output to approximate real-world meters. Default: False.| BOOLEAN| No| True / False  
`export_uv`| UV unwrap during generation. Turn off for faster geometry-only runs. Default: True.| BOOLEAN| No| True / False  
`compress_geometry`| Apply meshopt geometry compression (EXT_meshopt_compression). Smaller files, but ComfyUI’s 3D preview cannot display them; decompress before editing. Default: False.| BOOLEAN| No| True / False  
  
### 

​

Geometry only Inputs

No extra inputs are available when `output_mode` is set to `"Geometry only"`. Texture-related parameters are not sent to Tripo in this mode.

### 

​

Textured Inputs

These inputs appear only when `output_mode` is set to `"Textured"`.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`pbr`| Include PBR maps. When on, base texture is forced on too. Default: True.| BOOLEAN| Yes| True / False  
`texture_quality`| Texture quality preset. detailed = HD textures, extreme = 8K Ultra textures. Default: “standard”.| COMBO| Yes| `"standard"`  
`"detailed"`  
`"extreme"`  
`texture_seed`| A seed value for texture generation, used to control randomness. Default: 42.| INT| Yes| 0 to 2147483647  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model_file`| The generated model file name, kept for backward compatibility only.| STRING  
`model task_id`| The unique task ID for the model generation request.| MODEL_TASK_ID  
`GLB`| The generated 3D model in GLB format.| FILE3DGLB  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1TextToModelNode/en.md)

* * *

**Source fingerprint (SHA-256):** `53a5573384294612b912558436e82f3481717d2ba3d50b73f1e40c3065aff2a0`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/TripoP1TextToModelNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/TripoP1TextToModelNode)

[TripoP1MultiviewToModelNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/TripoP1MultiviewToModelNode)[TripoPSeriesImageToModelNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/TripoPSeriesImageToModelNode)

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
